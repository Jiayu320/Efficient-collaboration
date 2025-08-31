import requests
import json
import os
import re
import sys
import time
import pathlib
from collections import defaultdict
import concurrent.futures
from openai import OpenAI
import transformers

from config import ModelConfig, load_config, parse_args
from performance import PerformanceTracker, calculate_performance_metrics
from output_performance import count_tokens
from token_patch import get_deepseek_tokenizer, count_deepseek_tokens, append_output, get_collected_tokens, reset_collected_output

# 正则表达式函数，用于去除ASY绘图代码
def remove_asy_tags(text):
    """
    移除文本中的[asy]...[/asy]标签及其内容
    
    参数:
        text: 包含可能的[asy]标签的文本
        
    返回:
        清理后的文本
    """
    # 使用非贪婪模式匹配[asy]和[/asy]之间的所有内容（包括换行符）
    return re.sub(r'\[asy\].*?\[/asy\]', '', text, flags=re.DOTALL)

# 全局客户端对象，预先初始化
small_model_client = None

# 重写方法，用于替换计算tokens的方式
original_split_method = str.split
def monkey_patch_split():
    """
    使用猴子补丁替换所有split方法调用的计算方式
    """
    def deepseek_tokenize_split(self, *args, **kwargs):
        """替换split方法为使用deepseek tokenizer"""
        # 检查是否是在计算tokens的上下文中
        frame = sys._getframe(1)
        if 'completion_tokens' in frame.f_locals and frame.f_code.co_name in ['run_parallel_execution', 'run_sequential_execution']:
            return [None] * count_deepseek_tokens(self)  # 返回一个列表，其长度等于token数量
        return original_split_method(self, *args, **kwargs)
    
    # 应用猴子补丁
    str.split = deepseek_tokenize_split
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
    small_model_client = model_config.get_client(client_type="small")
    model_config.api_base = original_api_base
    
    # 如果大模型和小模型使用不同的API，则分别初始化
    if model_config.large_api_base != model_config.small_api_base:
        # 临时修改API基础URL创建大模型客户端
        model_config.api_base = model_config.large_api_base
        large_model_client = model_config.get_client(client_type="large")
        model_config.api_base = original_api_base
    else:
        large_model_client = small_model_client
    
    # 如果使用本地部署的路由模型
    if model_config.use_local_router:
        router_model_client = model_config.get_client(client_type="router")
        print("使用本地部署的路由模型")
    # 否则，如果路由模型和小模型使用不同的API，则分别初始化
    elif model_config.router_api_base != model_config.small_api_base:
        # 临时修改API基础URL创建路由模型客户端
        model_config.api_base = model_config.router_api_base
        router_model_client = model_config.get_client(client_type="router")
        model_config.api_base = original_api_base
    else:
        router_model_client = small_model_client
        
    print("所有模型客户端已初始化")

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
                
                # 使用DeepSeek tokenizer计算token数量
                estimated_prompt_tokens = count_tokens(prompt)
                estimated_completion_tokens = count_tokens(content)
                
                # 确保token数量至少为1
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
    
    # 添加原始问题（移除ASY绘图代码）
    cleaned_query = remove_asy_tags(query)
    final_result += f"## 原始问题\n{cleaned_query}\n\n"
    
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
        
    # 重置收集的输出内容
    reset_collected_output()
    返回:
        (tasks, stats_tracker): 任务字典和性能统计跟踪器
    """
    global xml_buffer, tasks, completed_steps, futures, router_model_client
    
    # 创建性能统计跟踪器
    stats_tracker = PerformanceTracker(config)
    
    # 初始化所有客户端
    initialize_clients(config)
    
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

    if config.use_local_router:
        system_prompt = '''
        You are an assistant whose job is to generate a solution plan. Given a math problem, generate a solution plan less than 10 steps in XML format with the following constraints:
        1. Plan must contain EXACTLY 1-10 steps (never more than 10)
        2. Each step must be distinct and non-redundant
        3. Merge trivial steps into logical units
        4. Focus on key insights and critical transitions
        5. Avoid step-by-step computations, focus on conceptual transitions
        6. Mark computational steps with Difficulty≥3
        7. Ensure all Rely attributes reference valid step IDs
        8. Make sure the Task is ended with a question mark (?)
        9. Format: 
        <Plan>
        <Step ID="1" Task="..." Difficulty="1-10" Token="the number of tokens required" Rely="Output only relevant steps"/>
        ...
        </Plan>
        Make sure the format with paired tags is correct and all steps are properly nested within the <Plan> tag.

        Difficulty scale:
        1-2: Basic computation
        3-4: Standard operations 
        5-6: Logical analysis 
        7-10: Advanced synthesis

        Output ONLY the XML plan with no additional text.'''
    else:
        '''准确率45.00%'''
        system_prompt = '''You are an assistant whose job is to generate a solution plan. Given a math problem, generate a solution plan less than 10 steps in XML format with the following constraints:
        1. Plan must contain EXACTLY 1-10 steps (never more than 10)
        2. Each step must be distinct and non-redundant
        3. Merge trivial steps into logical units
        4. Focus on key insights and critical transitions
        5. Avoid step-by-step computations, focus on conceptual transitions
        6. Mark computational steps with Difficulty≥3
        7. Ensure all Rely attributes reference valid step IDs
        8. Make sure the Task is ended with a question mark (?)
        9. Format: 
        <Plan>
        <Step ID="1" Task="..." Difficulty="1-10" Token="Estimate the number of tokens required to complete a subtask" Rely="Output only relevant steps"/>
        ...
        </Plan>
        Make sure the format with paired tags is correct and all steps are properly nested within the <Plan> tag.

        Difficulty scale:
        1-2: Basic computation
        3-4: Standard operations 
        5-6: Logical analysis 
        7-10: Advanced synthesis

        Output ONLY the XML plan with no additional text.
        Example:
        Question: Let's say a language  $L \\subseteq \\{0,1\\}^*$  is in  $\\textbf{P}_{angel}$  if there exists a polynomial  $p : \\mathbb{N} \\mapsto \\mathbb{N}$ , a sequence of strings  $\\{\\alpha_n\\}_{n \\in \\mathbb{N}}$  with  $\\alpha_n \\in \\{0,1\\}^{p(n)}$ , and a deterministic polynomial time Turing Machine  $M$  such that for every  $x \\in \\{0,1\\}^n$   $$ x \\in L \\Leftrightarrow M(x, \\alpha_n) = 1 $$  Let us call  $\\alpha_n$  to be the *angel string*for all  $x$  of the length  $n$ . Note that the *angel string* is  $\\textbf{not}$  similar to a *witness* or *certificate*as used in the definition of  $\\textbf{NP}$  For example, all unary languages, even  $UHALT$  which is undecidable, are in  $\\textbf{P}_{angel}$  because the \\textit{angel string} can simply be a single bit that tells us if the given unary string is in  $UHALT$  or not.\n\n\nA set  $S \\subseteq \\Sigma^*$  is said to be **sparse** if there exists a polynomial   $p : \\mathbb{N} \\mapsto \\mathbb{N}$  such that for each  $n \\in \\mathbb{N}$ , the number of strings of length  $n$  in  $S$  is bounded by  $p(n)$ . In other words,  $|S^{=n}| \\leq p(n)$ , where  $S^{=n} \\subseteq S$  contains all the strings in  $S$  that are of length  $n$ . \n\n[list=1]\n    [*] Given  $k \\in \\mathbb{N}$  sparse sets  $S_1, S_2 \\ldots S_k$ , show that there exists a sparse set  $S$  and a deterministic polynomial time TM  $M$  with oracle access to  $S$  such that given an input  $\\langle x,i \\rangle$  the TM  $M$  will accept it if and only if  $x \\in S_i$ .\n    Define the set  $S$  (note that it need not be computable), and give the description of  $M$  with oracle  $S$ .\n    Note that a TM  $M$  with oracle access to  $S$  can query whether  $s \\in S$  and get the correct answer in return in constant time. [/*]\n    \n    [*] Let us define a variant of  $\\textbf{P}_{angel}$  called  $\\textbf{P}_{bad-angel}$  with a constraint that there should exists a polynomial time algorithm that can **compute** the angel string for any length  $n \\in \\mathbb{N}$ . In other words, there is a poly-time algorithm  $A$  such that  $\\alpha_n = A(n)$ . \n    Is  $\\textbf{P} =\\textbf{P}_{bad-angel}$ ? Is  $\\textbf{NP}=\\textbf{P}_{bad-angel}$ ? Justify.\n    [/*]\n    \n    [*] Let the language  $L \\in$   $\\textbf{P}_{angel}$ . Show that there exists a sparse set  $S_L$  and a deterministic polynomial time TM  $M$  with oracle access to  $S_L$  that can decide the language  $L$ .  [/*]
        Plan: <Plan><Step ID=\"1\" Task=\"What does a sparse set mean in this context?\" Difficulty=\"2\" Token=\"20\" Rely=\"\"/><Step ID=\"2\" Task=\"How can we construct a set S that encodes information about k sparse sets?\" Difficulty=\"3\" Token=\"30\" Rely=\"1\"/><Step ID=\"3\" Task=\"How can we design a polynomial time TM M with oracle access to S to decide membership in Si?\" Difficulty=\"4\" Token=\"40\" Rely=\"2\"/><Step ID=\"4\" Task=\"What is the key difference between P_angel and P_bad-angel?\" Difficulty=\"2\" Token=\"20\" Rely=\"\"/><Step ID=\"5\" Task=\"Is P equal to P_bad-angel? Why or why not?\" Difficulty=\"3\" Token=\"35\" Rely=\"4\"/><Step ID=\"6\" Task=\"Is NP equal to P_bad-angel? Why or why not?\" Difficulty=\"4\" Token=\"40\" Rely=\"4,5\"/><Step ID=\"7\" Task=\"For a language L in P_angel, how can we encode the angel strings into a sparse set S_L?\" Difficulty=\"4\" Token=\"35\" Rely=\"1,4\"/><Step ID=\"8\" Task=\"How can we design a TM with oracle access to S_L to decide L?\" Difficulty=\"4\" Token=\"35\" Rely=\"7\"/></Plan>
        Question: Consider the following two person game. A number of pebbles are situated on the table. Two players make their moves alternately. A move consists of taking off the table  $x$  pebbles where  $x$  is the square of any positive integer. The player who is unable to make a move loses. Prove that there are infinitely many initial situations in which the second player can win no matter how his opponent plays.
        Plan: <Plan><Step ID=\"1\" Task=\"What are the valid moves in this game?\" Difficulty=\"1\" Token=\"20\" Rely=\"\"/><Step ID=\"2\" Task=\"Which positions are winning for the first player?\" Difficulty=\"4\" Token=\"40\" Rely=\"1\"/><Step ID=\"3\" Task=\"Which positions are winning for the second player?\" Difficulty=\"4\" Token=\"40\" Rely=\"1,2\"/><Step ID=\"4\" Task=\"Can we identify a pattern for winning second player positions?\" Difficulty=\"5\" Token=\"50\" Rely=\"3\"/><Step ID=\"5\" Task=\"For which specific number(s) of pebbles can the second player force a win?\" Difficulty=\"4\" Token=\"50\" Rely=\"4\"/><Step ID=\"6\" Task=\"Can we prove there are infinitely many such winning positions?\" Difficulty=\"5\" Token=\"60\" Rely=\"5\"/><Step ID=\"7\" Task=\"Can we express these winning positions as a formula or pattern?\" Difficulty=\"4\" Token=\"40\" Rely=\"5,6\"/></Plan>
        Question: An IPv4 packet contains the following data (in hexadecimal value) in the IP header: 4500 0034 B612 4000 4006 6F80 0A00 008B 5BC6 AEE0 . Does the header contains error?
        Plan: <Plan><Step ID=\"1\" Task=\"What is the structure and format of an IPv4 header?\" Difficulty=\"2\" Token=\"30\" Rely=\"\"/><Step ID=\"2\" Task=\"What does each part of the given hexadecimal data represent in the IPv4 header?\" Difficulty=\"3\" Token=\"40\" Rely=\"1\"/><Step ID=\"3\" Task=\"What is the header length according to the data?\" Difficulty=\"2\" Token=\"20\" Rely=\"2\"/><Step ID=\"4\" Task=\"Calculate the header checksum from the given data?\" Difficulty=\"4\" Token=\"50\" Rely=\"2\"/><Step ID=\"5\" Task=\"What is the checksum value provided in the header?\" Difficulty=\"2\" Token=\"20\" Rely=\"2\"/><Step ID=\"6\" Task=\"Does the calculated checksum match the provided checksum?\" Difficulty=\"3\" Token=\"30\" Rely=\"4,5\"/><Step ID=\"7\" Task=\"Are there any other potential errors in the header fields?\" Difficulty=\"3\" Token=\"40\" Rely=\"2\"/><Step ID=\"8\" Task=\"Does the IPv4 header contain any errors based on all checks?\" Difficulty=\"2\" Token=\"25\" Rely=\"6,7\"/></Plan>
        Question: A stationary source emits sound of frequency $f_{0}=492 \\mathrm{~Hz}$. The sound is reflected by a large car approaching the source with a speed of $2 \\mathrm{~ms}^{-1}$. The reflected signal is received by the source and superposed with the original. What will be the beat frequency of the resulting signal in Hz? (Given that the speed of sound in air is $330 \\mathrm{~ms}^{-1}$ and the car reflects the sound at the frequency it has received).
        Plan: <Plan><Step ID=\"1\" Task=\"What is the frequency received by the approaching car?\" Difficulty=\"3\" Token=\"30\" Rely=\"\"/><Step ID=\"2\" Task=\"What is the frequency reflected by the car?\" Difficulty=\"2\" Token=\"20\" Rely=\"1\"/><Step ID=\"3\" Task=\"What is the frequency of the reflected sound received back at the source?\" Difficulty=\"3\" Token=\"30\" Rely=\"2\"/><Step ID=\"4\" Task=\"What is the beat frequency when the original signal and reflected signal superpose?\" Difficulty=\"2\" Token=\"25\" Rely=\"3\"/></Plan>
        Question: 2.2 Find the numerical value of $\\frac{\\rho_{i} T_{i}}{\\rho_{a} T_{a}}-1$ using $\\gamma=0.0250 \\mathrm{Nm}^{-1}, R_{0}=1.00 \\mathrm{~cm}$, and $P_{a}=1.013 \\times 10^{5} \\mathrm{Nm}^{-2}$.
        Plan: <Plan><Step ID=\"1\" Task=\"What is the relationship between pressure, density, and temperature for an ideal gas?\" Difficulty=\"2\" Token=\"30\" Rely=\"\"/><Step ID=\"2\" Task=\"How are the internal pressure (Pi) and external pressure (Pa) related using the Young-Laplace equation?\" Difficulty=\"3\" Token=\"35\" Rely=\"\"/><Step ID=\"3\" Task=\"Calculate the internal pressure (Pi) using γ, R0, and Pa?\" Difficulty=\"3\" Token=\"30\" Rely=\"2\"/><Step ID=\"4\" Task=\"How can we express the ratio of ρiTi/ρaTa in terms of pressures Pi and Pa?\" Difficulty=\"3\" Token=\"35\" Rely=\"1\"/><Step ID=\"5\" Task=\"Calculate the numerical value of Pi/Pa using the given values?\" Difficulty=\"3\" Token=\"25\" Rely=\"3\"/><Step ID=\"6\" Task=\"Calculate the numerical value of ρiTi/ρaTa using the pressure ratio?\" Difficulty=\"3\" Token=\"25\" Rely=\"4,5\"/><Step ID=\"7\" Task=\"Calculate the final value of ρiTi/ρaTa - 1?\" Difficulty=\"2\" Token=\"20\" Rely=\"6\"/></Plan>
        Question: "Mrs. Walter gave an exam in a mathematics class of five students. She entered the scores in random order into a spreadsheet, which recalculated the class average after each score was entered. Mrs. Walter noticed that after each score was entered, the average was always an integer. The scores (listed in ascending order) were 71,76,80,82,and 91. What was the last score Mrs. Walter entered?"
        Plan: <Plan><Step ID=\"1\" Task=\"What is the average of all five scores?\" Difficulty=\"2\" Token=\"25\" Rely=\"\"/><Step ID=\"2\" Task=\"What are the possible sums after entering 1, 2, 3, 4, and 5 scores?\" Difficulty=\"3\" Token=\"40\" Rely=\"\"/><Step ID=\"3\" Task=\"What are the possible averages after entering each score?\" Difficulty=\"3\" Token=\"40\" Rely=\"2\"/><Step ID=\"4\" Task=\"Which averages are integers?\" Difficulty=\"2\" Token=\"30\" Rely=\"3\"/><Step ID=\"5\" Task=\"What are the possible orders for entering the scores to get integer averages each time?\" Difficulty=\"4\" Token=\"60\" Rely=\"4\"/><Step ID=\"6\" Task=\"For each possible order, what is the last score entered?\" Difficulty=\"3\" Token=\"40\" Rely=\"5\"/><Step ID=\"7\" Task=\"Is there only one possible last score or multiple possibilities?\" Difficulty=\"2\" Token=\"30\" Rely=\"6\"/><Step ID=\"8\" Task=\"What was the last score Mrs. Walter entered?\" Difficulty=\"1\" Token=\"20\" Rely=\"7\"/></Plan>
        '''
    user_prompt = f'''
    Question: {query}
    Plan:
    '''
    # 使用预初始化的路由模型客户端
    try:
        # 记录路由模型开始生成计划的时间，用于计算首个令牌响应时间
        router_start_time = time.time()
        first_token_received = False
        ttft = None
        
        # 根据配置决定是使用本地路由模型还是远程路由模型
        if config.use_local_router:
            response_stream = router_model_client.chat.completions.create(
                model=config.local_router_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query}
                ],
                stream=True,
                temperature=0.5,
                top_p=0.95,
                max_tokens=8192,
                extra_body={"enable_thinking": False}
            )
        else:
            response_stream = router_model_client.chat.completions.create(
                model=config.router_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                stream=True,
                temperature=0.3
            )
        
        # 使用deepseek_v3_tokenizer计算tokens
        prompt_tokens = count_deepseek_tokens(system_prompt) + count_deepseek_tokens(query)
        completion_tokens = 0
        full_completion = ""  # 用于收集所有输出内容
        
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
                    
                    # 使用deepseek_v3_tokenizer更新完成tokens计数
                    completion_tokens += count_deepseek_tokens(content)
                    
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

def dataset_run_parallel_execution(query, solution, config, workers=4):
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

    if config.use_local_router:
        system_prompt = '''Generate a solution plan that breaks down the problem into logical steps, identifying dependencies, difficulty levels and token usage.'''
    else:
        system_prompt = '''You are an assistant whose job is to break down the problem into 1-10 easy-to-solve sub-questions. Given a math problem, generate a solution plan less than 10 steps in XML format with the following constraints:
            1. Plan must contain EXACTLY 1-10 steps (never more than 10)
            2. Each step must be distinct and non-redundant
            3. Mark computational steps with Difficulty≥3
            4. Ensure all Rely attributes reference valid step IDs
            5. Make sure the Task is a question ended with a question mark (?)
            6. Make sure the sub-questions are easy to solve
            7. Format: 
            <Plan>
                <Step ID="1" Task="..." Difficulty="1-5" Token="Estimate the number of tokens required to complete a subtask" Rely="Output only relevant steps"/>
                ...
            </Plan>
            Make sure the format with paired tags is correct and all steps are properly nested within the <Plan> tag.

            Difficulty scale:
            1-2: Basic computation
            3-4: Standard operations 
            5-6: Logical analysis 
            7-10: Advanced synthesis

            Example:
            Question: Four years ago, Kody was only half as old as Mohamed. If Mohamed is currently twice 30 years old, how old is Kody?
            Plan:
            <Plan>
                <Step ID="1" Task="How old is Mohamed now?" Difficulty="1" Token="15" Rely=""/>
                <Step ID="2" Task="What was Mohamed's age 4 years ago?" Difficulty="1" Token="20" Rely="1"/>
                <Step ID="3" Task="What was Kody's age 4 years ago?" Difficulty="2" Token="25" Rely="2"/>
                <Step ID="4" Task="How old is Kody currently?" Difficulty="1" Token="15" Rely="3"/>
            </Plan>
            
            Output ONLY the XML plan with no additional text. 
        '''
        user_query = f'''
            Question: {query}
            Solution: {solution}
            Please generate a solution plan for the question in XML format you can use the solution as a reference.
        '''
    # 使用预初始化的路由模型客户端
    try:
        # 记录路由模型开始生成计划的时间，用于计算首个令牌响应时间
        router_start_time = time.time()
        first_token_received = False
        ttft = None
        
        # 根据配置决定是使用本地路由模型还是远程路由模型
        if config.use_local_router:
            response_stream = router_model_client.chat.completions.create(
                model=config.local_router_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_query}
                ],
                stream=True,
                temperature=0.5,
                top_p=0.95,
                max_tokens=8192,
                extra_body={"enable_thinking": False}
            )
        else:
            response_stream = router_model_client.chat.completions.create(
                model=config.router_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_query}
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
                    
                    # 使用deepseek_v3_tokenizer更新完成tokens计数
                    completion_tokens += count_deepseek_tokens(content)
                    
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
    global large_model_client
    
    prompt = f"""Here is a math problem with a standard answer and a student's solution. Please help me determine if the student's solution is correct. If the numerical value are same, then it is correct.
                               
                Problem: {question}

                Standard answer: {gold_answer}

                Answer: {final_answer}

                If the student's answer is correct, just output True; otherwise, just output False.
                No explanation is required.
    """
    
    # 使用全局预初始化的客户端，而不是每次创建新客户端
    client = large_model_client
    
    try:
        response = client.chat.completions.create(
            model=model_config.large_model,
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
    global large_model_client
    
    prompt = f"""Here is a math problem and a student's solution. Please help me determine if the student's solution is correct. If the numerical value are same, then it is correct.
                               
                Problem: {question}

                Answer: {final_answer}

                If the student's answer is correct, just output True; otherwise, just output False.
                No explanation is required.
    """
    
    # 使用全局预初始化的客户端，而不是每次创建新客户端
    client = large_model_client
    
    try:
        response = client.chat.completions.create(
            model=model_config.large_model,
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
    if model_config.use_local_router:
        prompt = f"""Please determine the difficulty of the following math problem. 
        Difficulty scale:
        1-10 (1=simplest, 10=hardest)
        Problem: {question}
        Please output only the difficulty level as a number. No other explanations or details are needed.
        """
    else:
        prompt = f"""Please determine the difficulty of the following math problem. 
        Difficulty scale:
        1-10 (1=simplest, 10=hardest)
        Problem: {question}
        Please output only the difficulty level as a number. No other explanations or details are needed.
        """
        prompt_ori = f"""Please determine the difficulty of the following math problem. 
        Difficulty scale:
        1=Basic 2=Simple 3=Moderate 4=Complex 5=Advanced
        Problem: {question}
        Please output only the difficulty level as a number. No other explanations or details are needed.
        """
    client = model_config.get_client(client_type="large")
    try:
        response = client.chat.completions.create(
            model=model_config.large_model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            stream=False
        )
        
        difficulty = response.choices[0].message.content.strip()
        print(f"问题难度判断结果: {difficulty}")
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

def build_report_path(base_dir="data_reports", is_dataset=False, dataset_name="", config=None, timestamp=None):
    """构建层次化的报告路径
    
    参数:
        base_dir: 基础目录，默认为data_reports
        is_dataset: 是否为数据集报告(True)或单个问题报告(False)
        dataset_name: 数据集名称，仅当is_dataset=True时有效
        config: 模型配置对象
        timestamp: 时间戳，如果为None则自动生成
        
    返回:
        完整的目录路径
    """
    if timestamp is None:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        
    # 获取模型名称，避免路径中的非法字符
    def clean_name(name):
        if name is None:
            return "unknown"
        # 提取模型名称的核心部分
        if "/" in name:
            name = name.split("/")[-1]
        # 移除可能导致路径问题的字符
        return ''.join(c for c in name if c.isalnum() or c in '_-.')
    
    # 获取模型名称
    router_name = "local_router" if config and config.use_local_router else clean_name(config.router_model if config else None)
    large_model = clean_name(config.large_model if config else None)
    small_model = clean_name(config.small_model if config else None)
    
    # 构建路径
    path_parts = [base_dir]
    
    if is_dataset:
        # 数据集路径结构: data_reports/dataset/数据集名称/router/large/small/时间戳
        dataset_name = os.path.basename(dataset_name) if dataset_name else "unknown_dataset"
        path_parts.extend(["dataset", dataset_name, router_name, large_model, small_model, timestamp])
    else:
        # 单个问题路径结构: data_reports/single/router/large/small/时间戳
        path_parts.extend(["single", router_name, large_model, small_model, timestamp])
    
    # 构建完整路径
    full_path = os.path.join(*path_parts)
    
    # 确保目录存在
    os.makedirs(full_path, exist_ok=True)
    
    return full_path

def save_result_to_file(final_result, config, workers, correctness_report, performance_report, dependency_report, theoretical_report=None):
    """将结果保存到文件
    
    参数:
        final_result: 最终结果文本
        config: 模型配置对象
        workers: 工作线程数
        correctness_report: 正确性报告
        performance_report: 性能报告
        dependency_report: 依赖关系报告
        theoretical_report: 理论性能报告（可选）
    """
    try:
        # 使用新的层次化目录结构
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        output_dir = build_report_path(
            base_dir="data_reports", 
            is_dataset=False, 
            config=config, 
            timestamp=timestamp
        )
        
        # 使用简化的文件名
        output_file = os.path.join(output_dir, "result.md")
        
        model_usage = f"使用小模型: {config.small_model}\n\n使用大模型: {config.large_model}\n\n使用路由模型: {config.router_model}\n\n"
        threshold_info = f"难度阈值: {config.threshold}\n\n工作线程数: {workers}\n\n"
        model_usage += threshold_info
        
        # 将性能报告、依赖关系报告和理论性能报告添加到最终结果中
        final_result_with_stats = model_usage + "\n\n" + final_result + "\n\n" + correctness_report + performance_report + "\n\n" + dependency_report
        
        # 如果有理论性能报告，也添加进去
        if theoretical_report:
            final_result_with_stats += "\n\n" + theoretical_report

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
