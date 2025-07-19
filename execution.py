'''
包含主要的执行逻辑
任务解析与XML处理函数
模型调用与步骤处理函数
任务路由与并行执行函数
结果汇总与报告生成函数
'''
import requests
import json
import os
import re
import time
from collections import defaultdict
import concurrent.futures
from openai import OpenAI

from config import ModelConfig, load_config, parse_args
from performance import PerformanceTracker, calculate_performance_metrics

# 全局客户端对象，预先初始化
small_model_client = None
large_model_client = None
router_model_client = None

# 全局变量
# 用于存储解析后的任务数据
tasks = defaultdict(dict)
current_step = None
xml_buffer = ""

# Track completed steps
completed_steps = set()
# Store futures for each step
futures = {}
# 映射future对象到step_id，用于回调
future_to_id = {}

def initialize_clients(model_config):
    """预先初始化模型客户端"""
    global small_model_client, large_model_client, router_model_client
    
    # 初始化小模型客户端
    original_api_base = model_config.api_base
    model_config.api_base = model_config.small_api_base
    small_model_client = model_config.get_client()
    model_config.api_base = original_api_base
    
    # 如果大模型和小模型使用不同的API，则分别初始化
    if model_config.large_api_base != model_config.small_api_base:
        # 临时修改API基础URL创建大模型客户端
        model_config.api_base = model_config.large_api_base
        large_model_client = model_config.get_client()
        model_config.api_base = original_api_base
    else:
        large_model_client = small_model_client
        
    # 如果路由模型和小模型使用不同的API，则分别初始化
    if model_config.router_api_base != model_config.small_api_base:
        # 临时修改API基础URL创建路由模型客户端
        model_config.api_base = model_config.router_api_base
        router_model_client = model_config.get_client()
        model_config.api_base = original_api_base
    else:
        router_model_client = small_model_client
        
    print("所有模型客户端已初始化")

def warmup_models(model_config):
    """预热模型以减少首次请求的TTFT"""
    global small_model_client, large_model_client, router_model_client
    
    print("预热模型中...")
    
    # 简单的预热提示
    warmup_prompt = "Hello, I'm warming up."
    
    try:
        # 预热小模型
        small_model_client.chat.completions.create(
            model=model_config.small_model,
            messages=[{"role": "user", "content": warmup_prompt}],
            max_tokens=5
        )
        print("小模型预热完成")
        
        # 预热大模型
        if large_model_client != small_model_client:
            large_model_client.chat.completions.create(
                model=model_config.large_model,
                messages=[{"role": "user", "content": warmup_prompt}],
                max_tokens=5
            )
            print("大模型预热完成")
        
        # 预热路由模型
        if router_model_client != small_model_client and router_model_client != large_model_client:
            router_model_client.chat.completions.create(
                model=model_config.router_model,
                messages=[{"role": "user", "content": warmup_prompt}],
                max_tokens=5
            )
            print("路由模型预热完成")
        
        print("所有模型预热完成")
    except Exception as e:
        print(f"模型预热失败: {e}")

def parse_step_attributes(attr_str):
    """解析属性字符串为字典"""
    attrs = {}
    # 使用正则匹配属性键值对
    pattern = r'(\w+)="(.*?)"'
    for match in re.finditer(pattern, attr_str):
        key, value = match.groups()
        attrs[key] = value
    return attrs

def process_xml_buffer():
    """处理XML缓冲区中的完整标签"""
    global xml_buffer, tasks, current_step
    
    # 查找完整的<Step>标签
    step_match = re.search(r'<Step\s+(.*?)/>', xml_buffer, re.DOTALL)
    if not step_match:
        # 检查是否有结束标签
        if '</Plan>' in xml_buffer:
            xml_buffer = ""
        return False
    
    full_tag = step_match.group(0)
    attr_str = step_match.group(1).strip()
    
    # 从缓冲区移除已处理的部分
    xml_buffer = xml_buffer[step_match.end():]
    
    # 解析属性
    attrs = parse_step_attributes(attr_str)
    if 'ID' not in attrs:
        return True
    
    # 添加到任务字典
    step_id = attrs['ID']
    tasks[step_id] = attrs
    tasks[step_id]['Result'] = None  # 添加Result字段
    
    # 设置当前步骤（用于后续结果收集）
    current_step = step_id
    return True

def generate_step_result(prompt, difficulty, model_config, stats_tracker=None):
    """生成步骤结果
    
    参数:
        prompt: 提示词
        difficulty: 任务难度
        model_config: 模型配置对象
        stats_tracker: 性能统计跟踪器
    """
    global small_model_client, large_model_client
    
    # 根据难度选择模型
    model = model_config.select_model_by_difficulty(difficulty)
    
    # 根据模型选择对应的客户端
    if model == model_config.small_model:
        client = small_model_client
    else:
        client = large_model_client
    
    # 调用API
    try:
        start_time = time.time()
        first_token_time = None
        
        # 使用流式API来测量首个令牌响应时间
        try:
            response_stream = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                stream=True
            )
        except Exception as e:
            # 如果流式API调用失败，尝试使用非流式API
            print(f"流式API调用失败，尝试使用非流式API: {e}")
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                stream=False
            )
            used_time = time.time() - start_time
            # 在这种情况下我们无法测量TTFT
            ttft = None
            return response.choices[0].message.content
        
        # 收集完整响应
        collected_content = ""
        completion_tokens = 0
        prompt_tokens = 0
        
        for chunk in response_stream:
            if first_token_time is None:
                first_token_time = time.time()
                
            # 从每个块中提取内容并累加
            if hasattr(chunk.choices[0], 'delta') and hasattr(chunk.choices[0].delta, 'content'):
                content = chunk.choices[0].delta.content
                if content:
                    collected_content += content
                    completion_tokens += 1  # 近似计算完成tokens
            
        # 计算首个令牌响应时间
        ttft = first_token_time - start_time if first_token_time else None
        
        # 创建一个模拟的完整响应对象
        class MockResponse:
            def __init__(self, content, model_name):
                self.choices = [type('obj', (object,), {
                    'message': type('obj', (object,), {
                        'content': content
                    })
                })]
                
                # 估算token数量 - 使用更准确的方法
                # 粗略估计英文token为单词数的1.3倍，中文为字符数的1.5倍
                prompt_words = len(prompt.split())
                prompt_chinese_chars = sum(1 for c in prompt if '\u4e00' <= c <= '\u9fff')
                content_words = len(content.split())
                content_chinese_chars = sum(1 for c in content if '\u4e00' <= c <= '\u9fff')
                
                estimated_prompt_tokens = int((prompt_words * 1.3) + (prompt_chinese_chars * 1.5))
                estimated_completion_tokens = int((content_words * 1.3) + (content_chinese_chars * 1.5))
                
                if estimated_prompt_tokens < 1:
                    estimated_prompt_tokens = 1
                if estimated_completion_tokens < 1:
                    estimated_completion_tokens = 1
                
                self.usage = type('obj', (object,), {
                    'prompt_tokens': estimated_prompt_tokens,
                    'completion_tokens': estimated_completion_tokens,
                    'total_tokens': estimated_prompt_tokens + estimated_completion_tokens
                })
                self.model = model_name
                
        # 使用收集的内容创建模拟响应
        response = MockResponse(collected_content, model)
        
        # 如果没有收集到内容，可能是API调用有问题
        if not collected_content:
            print("警告: 流式API未返回任何内容")
            # 尝试非流式调用作为后备
            try:
                backup_response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    stream=False
                )
                return backup_response.choices[0].message.content
            except Exception as backup_error:
                print(f"备份调用也失败: {backup_error}")
                return f"错误: API调用未返回内容"
        used_time = time.time() - start_time
        model_name = model_config.small_model if model == model_config.small_model else model_config.large_model
        model_type = "small_model" if model == model_config.small_model else "large_model"
        
        print(f"{model_name} API调用成功，使用时间: {used_time:.2f}秒")
        if ttft is not None:
            print(f"首个令牌响应时间 (TTFT): {ttft:.3f}秒")
            
        # 如果有统计跟踪器，更新token使用统计和TTFT统计
        if stats_tracker and hasattr(response, 'usage'):
            stats_tracker.update_token_usage(
                model_type,
                response.usage.prompt_tokens,
                response.usage.completion_tokens
            )
            # 更新首个令牌响应时间
            if ttft is not None:
                stats_tracker.update_ttft(model_type, ttft)
        
        try:
            return response.choices[0].message.content
        except AttributeError:
            print("错误: 无法从响应中提取内容")
            if hasattr(response, 'choices') and response.choices and hasattr(response.choices[0], 'message'):
                return str(response.choices[0].message)
            return "API调用失败，未能获取有效响应"
    except Exception as e:
        print(f"API调用失败: {e}")
        return f"错误: API调用失败 - {str(e)}"

def build_step_prompt(current_step, tasks, query):
    """构建当前步骤的提示"""
    prompt_template = """
    You are a mathematical problem-solving assistant. I will provide you with a math problem and a specific step from my solution plan. Your task is to complete ONLY this specific step based on the description and token limit.
    PROBLEM:
    {Problem}
    CURRENT STEP:
    Task: {Task}
    Relied Results: {Relied_Results}
    Let's think step by step and use less than {Token} tokens:
    """
    # 获得依赖的任务的具体结果
    relied_results = tasks[current_step].get('Rely', '')
    if relied_results:
        relied_results = [tasks[step_id]['Result'] for step_id in relied_results.split(',') if step_id in tasks]
    else:
        relied_results = []
    return prompt_template.format(
        Problem=query,
        Task=tasks[current_step].get('Task', ''),
        Token=tasks[current_step].get('Token', ''),
        Relied_Results=relied_results
    ), tasks[current_step].get('Difficulty', '')

def is_step_ready(step_id, tasks):
    """Check if a step is ready to be processed (dependencies completed or none)"""
    rely_str = tasks[step_id].get('Rely', '')
    if not rely_str:
        return True
    
    rely_steps = rely_str.split(',')
    return all(step in completed_steps for step in rely_steps)

def process_step(step_id, tasks, query, model_config, stats_tracker=None):
    """处理单个步骤
    
    参数:
        step_id: 步骤ID
        tasks: 任务字典
        query: 原始查询
        model_config: 模型配置对象
        stats_tracker: 性能统计跟踪器
    """
    try:
        print(f"\n开始执行步骤 {step_id}: {tasks[step_id].get('Task', '未知任务')}")
        prompt, difficulty = build_step_prompt(step_id, tasks, query)
        
        # 使用模型配置生成结果
        result = generate_step_result(prompt, difficulty, model_config, stats_tracker)
        
        tasks[step_id]['Result'] = result
        completed_steps.add(step_id)
        print(f"步骤 {step_id} 执行完成")
        return step_id
    except Exception as e:
        print(f"步骤 {step_id} 执行出错: {e}")
        # 即使出错也标记为完成，避免死锁
        completed_steps.add(step_id)
        tasks[step_id]['Result'] = f"错误: {str(e)}"
        return step_id

def completion_callback(future):
    """处理完成任务的回调函数
    
    参数:
        future: 已完成的Future对象
    """
    global future_to_id, futures, completed_steps, tasks
    
    # 获取对应的step_id
    step_id = future_to_id.get(future)
    if not step_id:
        print("警告: 无法找到与Future对应的任务ID")
        return
        
    try:
        # 获取结果，这里不会阻塞因为任务已完成
        future.result()
        print(f"回调中: 步骤 {step_id} 已完成")
        # 标记为已完成
        completed_steps.add(step_id)
    except Exception as e:
        print(f"回调中: 任务 {step_id} 执行错误: {e}")
        # 即使出错也标记为完成，避免死锁
        completed_steps.add(step_id)
        tasks[step_id]['Result'] = f"错误: {str(e)}"
    finally:
        # 从跟踪字典中移除
        if future in future_to_id:
            del future_to_id[future]
        if step_id in futures:
            del futures[step_id]

def router(tasks, model_config, query, executor, stats_tracker=None):
    """调度任务并行执行"""
    global futures, future_to_id
    has_new_tasks = False
    
    # 计算可以执行的任务及其优先级
    ready_tasks = []
    for step_id in tasks:
        if step_id not in futures and step_id not in completed_steps:
            if is_step_ready(step_id, tasks):
                # 优先级计算：基于依赖任务的数量和任务ID（较早的任务优先）
                rely_str = tasks[step_id].get('Rely', '')
                rely_count = len(rely_str.split(',')) if rely_str else 0
                priority = (rely_count, int(step_id))
                ready_tasks.append((step_id, priority))
    
    # 按优先级排序（依赖少的先执行）
    ready_tasks.sort(key=lambda x: x[1])
    
    # 批量提交任务到执行器
    for step_id, _ in ready_tasks:
        print(f"调度步骤 {step_id}: {tasks[step_id].get('Task', '未知任务')}")
        future = executor.submit(process_step, step_id, tasks, query, model_config, stats_tracker)
        # 添加回调
        future.add_done_callback(completion_callback)
        # 保存映射关系
        futures[step_id] = future
        future_to_id[future] = step_id
        has_new_tasks = True
    
    # 使用回调而非主动检查已完成任务
    # 不需要在这里检查完成的任务，因为有回调处理
    # 但保留对已完成任务的检查，确保路由算法正常运行
    completed_future_ids = [step_id for step_id, f in list(futures.items()) if f.done()]
    if completed_future_ids:
        has_new_tasks = True
    
    # 如果有正在运行的任务，继续路由
    if futures:
        return True
    
    return has_new_tasks

def print_results(tasks):
    """打印任务执行结果
    
    参数:
        tasks: 任务字典
    """
    print("\n\n执行结果:")
    for step_id, attrs in sorted(tasks.items(), key=lambda x: int(x[0])):
        print(f"\n--- 步骤 {step_id}: {attrs.get('Task', '未知任务')} ---")
        if 'Result' in attrs and attrs['Result']:
            print(attrs['Result'])
        else:
            print("(无结果)")
        print(f"--- 步骤 {step_id} 结束 ---")
    
def wait_for_completion_and_get_final_result(tasks, query, config, stats_tracker=None):
    """等待所有任务完成并返回最终结果
    
    参数:
        tasks: 任务字典
        query: 原始查询
        config: 模型配置
        stats_tracker: 性能统计跟踪器
        
    返回:
        最终结果字符串
    """
    # 确保所有任务已完成
    if not all('Result' in task and task['Result'] for task in tasks.values()):
        print("等待所有任务完成...")
    
    # 按步骤ID排序
    sorted_tasks = sorted(tasks.items(), key=lambda x: int(x[0]))
    
    # 构建最终结果
    final_result = "# 问题求解最终结果\n\n"
    
    # 添加原始问题
    final_result += f"## 原始问题\n{query}\n\n"
    
    # 添加解决方案步骤
    final_result += "## 解决步骤\n\n"
    for step_id, attrs in sorted_tasks:
        final_result += f"### 步骤 {step_id}: {attrs.get('Task', '未知任务')}\n"
        if 'Result' in attrs and attrs['Result']:
            final_result += f"{attrs['Result']}\n\n"
        else:
            final_result += "（此步骤未完成）\n\n"
    
    # 已经完成了所有的subtask,向router小模型询问最终结果
    prompt = """Based on the results of all steps below, please provide only the final answer. No other explanations or details are needed.

    PROBLEM:
    {query}

    SOLUTION STEPS:
    {steps}
    """
    
    # 构建步骤结果文本
    steps_text = ""
    for step_id, attrs in sorted_tasks:
        step_text = f"步骤 {step_id}: {attrs.get('Task', '未知任务')}\n"
        if 'Result' in attrs and attrs['Result']:
            step_text += f"{attrs['Result']}\n\n"
        else:
            step_text += "（此步骤未完成）\n\n"
        steps_text += step_text
    
    # 调用小模型获取最终答案
    try:
        final_prompt = prompt.format(query=query, steps=steps_text)
        final_answer = generate_step_result(final_prompt, "1", config, stats_tracker)  # 使用小模型（难度为1，低于阈值）
        final_result += f"## 最终答案\n{final_answer}\n"
        # 停止性能跟踪
        stats_tracker.stop_tracking()

    except Exception as e:
        print(f"获取最终答案时出错: {e}")
        # 如果失败，回退到使用最后一个步骤的结果
        if sorted_tasks:
            last_step_id, last_step = sorted_tasks[-1]
            final_result += f"## 最终答案\n"
            if 'Result' in last_step and last_step['Result']:
                final_result += f"{last_step['Result']}\n"
                # 停止性能跟踪
                stats_tracker.stop_tracking()
            else:
                final_result += "（未能获得最终答案）\n"
                # 停止性能跟踪
                stats_tracker.stop_tracking()
    
    return final_result

def generate_task_dependency_report(tasks):
    """生成任务依赖关系报告
    
    参数:
        tasks: 任务字典
    
    返回:
        任务依赖关系报告文本
    """
    report = "# 任务规划依赖关系\n\n"
    
    # 按步骤ID排序
    sorted_tasks = sorted(tasks.items(), key=lambda x: int(x[0]))
    
    report += "| 步骤ID | 任务描述 | 依赖步骤 | 难度 | Token限制 |\n"
    report += "| ------ | -------- | -------- | ---- | --------- |\n"
    
    for step_id, attrs in sorted_tasks:
        task_desc = attrs.get('Task', '未知任务')
        rely = attrs.get('Rely', '无')
        difficulty = attrs.get('Difficulty', '未指定')
        token_limit = attrs.get('Token', '未指定')
        
        report += f"| {step_id} | {task_desc} | {rely} | {difficulty} | {token_limit} |\n"
    
    return report

def run_parallel_execution(query, config, workers=4):
    """运行并行执行流程
    
    参数:
        query: 要解决的问题
        config: 模型配置对象
        workers: 并行工作线程数
    """
    global xml_buffer, tasks, completed_steps, futures, router_model_client
    
    # 创建性能统计跟踪器
    stats_tracker = PerformanceTracker(config)
    
    # 初始化所有客户端
    initialize_clients(config)
    
    # 预热模型，减少TTFT
    warmup_models(config)
    
    # 重置全局状态
    xml_buffer = ""
    tasks = defaultdict(dict)
    completed_steps = set()
    futures = {}
    future_to_id = {}
    
    # 创建线程池
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=workers)
    
    # 初始化变量跟踪解析进度
    task_count = 0
    print("开始处理问题：", query)
    print("正在获取解决方案计划...")
    system_prompt = '''You are an assistant whose job is to generate a solution plan. Given a math problem, generate a solution plan less than 10 steps in XML format with the following constraints:
    1. Plan must contain EXACTLY 1-10 steps (never more than 10)
    2. Each step must be distinct and non-redundant
    3. Merge trivial steps into logical units
    4. Focus on key insights and critical transitions
    5. Avoid step-by-step computations, focus on conceptual transitions
    6. Mark computational steps with Difficulty≥3
    7. Ensure all Rely attributes reference valid step IDs
    8. Format: 
    <Plan>
    <Step ID="1" Task="..." Difficulty="1-5" Token="Estimate the number of tokens required to complete a subtask" Rely="Output only relevant steps"/>
    ...
    </Plan>
    Make sure the format with paired tags is correct and all steps are properly nested within the <Plan> tag.

    Difficulty scale:
    1=Basic 2=Simple 3=Moderate 4=Complex 5=Advanced

    Output ONLY the XML plan with no additional text.'''
    
    # 使用预初始化的路由模型客户端
    try:
        # 记录路由模型开始生成计划的时间，用于计算首个令牌响应时间
        router_start_time = time.time()
        first_token_received = False
        ttft = None
        
        response_stream = router_model_client.chat.completions.create(
            model=config.router_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ],
            stream=True
        )
        
        # 计算输入tokens (估计值，实际应该通过API返回)
        prompt_tokens = len(system_prompt.split()) + len(query.split())
        completion_tokens = 0
        
        for chunk in response_stream:
            if hasattr(chunk.choices[0], 'delta') and hasattr(chunk.choices[0].delta, 'content'):
                content = chunk.choices[0].delta.content
                if content:
                    # 记录首个token响应时间
                    if not first_token_received:
                        ttft = time.time() - router_start_time
                        first_token_received = True
                        if stats_tracker:
                            stats_tracker.update_ttft("router_model", ttft)
                    
                    print(content, end="", flush=True)  # 实时输出
                    
                    # 更新完成tokens计数
                    completion_tokens += len(content.split())
                    
                    # 添加到XML缓冲区
                    xml_buffer += content
                    
                    # 尝试解析缓冲区中的完整标签
                    parsed_count = 0
                    while process_xml_buffer():
                        parsed_count += 1
                        task_count += 1
                    
                    # 只有在解析到新任务时才启动路由
                    if parsed_count > 0:
                        print(f"\n已解析 {task_count} 个任务，启动任务调度...")
                        router(tasks, config, query, executor)
        
        # 更新router模型的token使用情况
        if stats_tracker:
            stats_tracker.update_token_usage("router_model", prompt_tokens, completion_tokens)
                        
    except Exception as e:
        print(f"\n处理响应时出错: {e}")
    
    print(f"\n计划生成完成，共解析 {task_count} 个任务")
    
    # 继续处理可能的剩余XML标签
    while process_xml_buffer():
        pass
    
    # 处理所有剩余任务直到全部完成
    print("\n\n开始执行所有任务...")
    while tasks and any(step_id not in completed_steps for step_id in tasks):
        if not router(tasks, config, query, executor, stats_tracker):
            break
    
    # 关闭线程池
    executor.shutdown()
    
    return tasks, stats_tracker

def judge_correct(question, gold_answer, final_answer, model_config):
    """判断最终答案是否正确
    
    参数:
        question: 问题文本
        gold_answer: 金标准答案
        final_answer: 最终生成的答案
        model_config: 模型配置对象
        
    返回:
        是否正确的布尔值和判断结果文本
    """
    prompt = f"""Here is a math problem with a standard answer and a student's solution. Please help me determine if the student's solution is correct. If the numerical value are same, then it is correct.
                               
                Problem: {question}

                Standard answer: {gold_answer}

                Answer: {final_answer}

                If the student's answer is correct, just output True; otherwise, just output False.
                No explanation is required.
    """
    
    # 使用小模型进行判断，因为这是简单任务
    client = model_config.get_client()
    
    try:
        response = client.chat.completions.create(
            model=model_config.small_model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            stream=False
        )
        
        result_text = response.choices[0].message.content.strip()
        # 解析结果文本，确定是否正确
        is_correct = "true" in result_text.lower() and "false" not in result_text.lower()
        
        return is_correct, result_text
    except Exception as e:
        print(f"判断答案正确性时出错: {e}")
        return False, f"判断错误: {str(e)}"

def LLM_judge(question, final_answer, model_config):
    """使用大模型判断答案是否正确
    
    参数:
        question: 问题文本
        final_answer: 最终生成的答案
        model_config: 模型配置对象
        
    返回:
        是否正确的布尔值和判断结果文本
    """
    prompt = f"""Here is a math problem and a student's solution. Please help me determine if the student's solution is correct. If the numerical value are same, then it is correct.
                               
                Problem: {question}

                Answer: {final_answer}

                If the student's answer is correct, just output True; otherwise, just output False.
                No explanation is required.
    """
    
    client = model_config.get_client()
    
    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ],
            stream=False
        )
        
        result_text = response.choices[0].message.content.strip()
        # 解析结果文本，确定是否正确
        is_correct = "true" in result_text.lower() and "false" not in result_text.lower()
        
        return is_correct, result_text
    except Exception as e:
        print(f"判断答案正确性时出错: {e}")
        return False, f"判断错误: {str(e)}"

def judge_question_difficulty(question, model_config):
    """判断问题难度
    
    参数:
        question: 问题文本
        model_config: 模型配置对象
        
    返回:
        问题难度（字符串）
    """
    prompt = f"""Please determine the difficulty of the following math problem. 
    Difficulty scale:
    1=Basic 2=Simple 3=Moderate 4=Complex 5=Advanced
    Problem: {question}
    Please output only the difficulty level as a number. No other explanations or details are needed.
    """
    client = model_config.get_client()
    try:
        response = client.chat.completions.create(
            model=model_config.small_model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            stream=False
        )
        
        difficulty = response.choices[0].message.content.strip()

        return difficulty
    except Exception as e:
        return f"错误: 判断问题难度时出错 - {str(e)}" 

def call_small_model_directly(question, model_config, stats_tracker=None):
    """直接调用小模型进行处理
    
    参数:
        question: 问题文本
        model_config: 模型配置对象
        stats_tracker: 性能统计跟踪器（可选）
        
    返回:
        小模型的响应内容
    """
    # 构建提示词
    prompt = """You are a math problem-solving assistant. I will provide you with a math problem. Your task is to solve it step by step and provide the final answer.

    PROBLEM:
    {question}
    """.format(question=question)
    return generate_step_result(prompt, "1", model_config, stats_tracker)

def call_large_model_directly(question, model_config, stats_tracker=None):
    """直接调用大模型进行处理
    
    参数:
        question: 问题文本
        model_config: 模型配置对象
        stats_tracker: 性能统计跟踪器（可选）
        
    返回:
        大模型的响应内容
    """
    # 构建提示词
    prompt = """You are a math problem-solving assistant. I will provide you with a math problem. Your task is to solve it step by step and provide the final answer.

    PROBLEM:
    {question}
    """.format(question=question)
    return generate_step_result(prompt, "5", model_config, stats_tracker)

def save_result_to_file(final_result, config, workers, correctness_report, performance_report, dependency_report):
    """将结果保存到文件
    
    参数:
        final_result: 最终结果文本
        config: 模型配置对象
        workers: 工作线程数
        correctness_report: 正确性报告
        performance_report: 性能报告
        dependency_report: 依赖关系报告
    """
    try:
        output_dir = "results"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(output_dir, f"result_{timestamp}.md")
        model_usage = f"使用小模型: {config.small_model}\n\n使用大模型: {config.large_model}\n\n使用路由模型: {config.router_model}\n\n"
        threshold_info = f"难度阈值: {config.threshold}\n\n工作线程数: {workers}\n\n"
        model_usage += threshold_info
        
        # 将性能报告和依赖关系报告添加到最终结果中
        final_result_with_stats = model_usage + "\n\n" + final_result + "\n\n" + correctness_report + performance_report + "\n\n" + dependency_report

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(final_result_with_stats)
        print(f"结果已保存至: {output_file}")
        return output_file
    except Exception as e:
        print(f"保存结果时出错: {e}")
        return None

def warmup_models(model_config):
    """预热模型以减少首次请求的TTFT"""
    global small_model_client, large_model_client, router_model_client
    
    print("预热模型中...")
    
    # 简单的预热提示
    warmup_prompt = "Hello, I'm warming up."
    
    try:
        # 预热小模型
        small_model_client.chat.completions.create(
            model=model_config.small_model,
            messages=[{"role": "user", "content": warmup_prompt}],
            max_tokens=5
        )
        
        # 预热大模型
        if large_model_client != small_model_client:
            large_model_client.chat.completions.create(
                model=model_config.large_model,
                messages=[{"role": "user", "content": warmup_prompt}],
                max_tokens=5
            )
        
        # 预热路由模型
        if router_model_client != small_model_client and router_model_client != large_model_client:
            router_model_client.chat.completions.create(
                model=model_config.router_model,
                messages=[{"role": "user", "content": warmup_prompt}],
                max_tokens=5
            )
        
        print("模型预热完成")
    except Exception as e:
        print(f"模型预热失败: {e}")
