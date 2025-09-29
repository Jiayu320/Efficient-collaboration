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
# 导入日志配置模块
from log_config import get_logger, log_separator


def get_api_key(file_path):
    """从文件中获取API密钥"""
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return f.read().strip()
    else:
        logger = get_logger()
        logger.error(f"API密钥文件 '{file_path}' 未找到")
        raise FileNotFoundError(f"API密钥文件 '{file_path}' 未找到")
    
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
    if small_model_client is None:
        small_model_client = model_config.get_client(client_type="small")
    if large_model_client is None:
        large_model_client = model_config.get_client(client_type="large")
    if router_model_client is None:
        router_model_client = model_config.get_client(client_type="router")
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
    You are a specialized AI module acting as a **domain expert, a critical reviewer,** and a precision-focused computational engine. Your function is to execute a single, specific subtask from a larger problem-solving plan with absolute accuracy, leveraging your internal knowledge base and reasoning capabilities.
    You will be provided with the following inputs:

    1.  **`PROBLEM`**: The overall problem for context.
    2.  **`CURRENT STEP (Task)`**: The specific, isolated instruction you must execute.
    3.  **`CONTEXT (Results from prior steps)`**: Crucial information from completed steps. **You MUST critically evaluate this context for correctness before using it.**

    Your output must strictly adhere to the following two-part format:

    1.  **`Reasoning:`**:
        - **Correction First (If Necessary):** Before any other action, you MUST validate the provided `CONTEXT`. If you identify any factual, logical, or calculational errors from the previous steps, your first action is to clearly state the correction. Start with the prefix "Correction:". For example: "Correction: The formula for DC in Step 2 was incorrect. The correct calculation should be...".
        - **State Principle:** After addressing any necessary corrections, if the `Task` requires a specific formula, constant, or scientific principle, you MUST state it clearly.
        - **Explain Process:** Finally, provide a brief, step-by-step explanation of your process for completing the `CURRENT STEP (Task)`, using the corrected context and stated principles. Show your work.

    2.  **`Answer:`**: State the final, direct answer to the `Task`. This should be the conclusive output of your reasoning, presented as cleanly as possible (e.g., a number, a full formula, a short statement).

    **CRITICAL RULES:**
    * Your primary duty is accuracy. This includes **correcting any errors found in the `CONTEXT`** before proceeding to solve the `Task`.
    * Focus exclusively on solving the `Task`. Provide only the requested information or calculation.
    * **DO NOT** add conversational filler, greetings, or sign-offs.
    * Your 'Answer' must ONLY contain the direct answer. Do not include extra text, option letters, or reasoning.
    * Your entire response must be under **{Token}** tokens.

    **PROBLEM:**
    {Problem}

    **CURRENT STEP:**
    Task: {Task}

    {Relied_Results}
    """
    # 获得依赖的任务的具体结果
    rely_ids = tasks[current_step].get('Rely', '')
    if rely_ids != '':
        relied_results = "\n    **CONTEXT (Results from prior steps):**\n"
        # 遍历每个依赖的步骤ID
        for step_id in rely_ids.split(','):
            if step_id in tasks and 'Result' in tasks[step_id] and tasks[step_id]['Result']:
                relied_results += f"\n    Task {step_id}: {tasks[step_id].get('Task', '')} ; Result: {tasks[step_id]['Result']}"
    else:
        relied_results = ""
    
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
        # === 新增：获取日志记录器 ===
        logger = get_logger()
        # ============================

        print(f"\n开始执行步骤 {step_id}: {tasks[step_id].get('Task', '未知任务')}")
        prompt, difficulty = build_step_prompt(step_id, tasks, query)
        
        # === 新增：记录执行器模型的输入 ===
        model_type = "大模型" if int(difficulty) >= model_config.threshold else "小模型"
        logger.info(f"===== Prompt 给执行器 ({model_type} - 步骤 {step_id}) =====")
        logger.info(prompt)
        log_separator()
        # =================================

        # 使用模型配置生成结果
        result = generate_step_result(prompt, difficulty, model_config, stats_tracker)
        
        # === 新增：记录执行器模型的输出 ===
        logger.info(f"===== 来自执行器 ({model_type} - 步骤 {step_id}) 的输出 =====")
        logger.info(result)
        log_separator()
        # =================================

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
    # === 新增：获取日志记录器 ===
    logger = get_logger()
    # ============================

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

        # === 新增：记录最终总结的Prompt ===
        logger.info("===== Prompt 给最终总结模型 (小模型) =====")
        logger.info(final_prompt)
        log_separator()
        # =================================

        final_answer = generate_step_result(final_prompt, "1", config, stats_tracker)  # 使用小模型（难度为1，低于阈值）

        # === 新增：记录最终总结的输出 ===
        logger.info("===== 来自最终总结模型 (小模型) 的输出 =====")
        logger.info(final_answer)
        log_separator()
        # =================================

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

def dataset_run_parallel_execution(query, solution, config, workers=4, dataset_build_config=None):
    """
    为构建数据集生成规划。
    给定一个问题和参考答案，利用规划模型生成训练数据。

    参数:
        query: 要解决的问题
        solution: 用于指导planner的参考答案
        config: 模型配置对象
        workers: 并行工作线程数 (此函数中未使用)
        dataset_build_config: 包含数据集构建设置的字典
    
    返回:
        一个元组 (full_plan_with_thinking, plan_only, system_prompt)。
        失败时返回 (None, None, None)。
    """
    global xml_buffer, tasks, router_model_client
    
    logger = get_logger()

    # 如果未提供，则使用默认构建配置
    if dataset_build_config is None:
        dataset_build_config = {
            'use_ground_truth_to_guide_planner': True,
            'save_thinking': True,
        }

    # 确保客户端已初始化
    initialize_clients(config)
    
    # 为此运行重置状态
    xml_buffer = ""
    tasks = defaultdict(dict)
    
    print(f"正在为问题构建数据集: {query[:100]}...")
    logger.info(f"正在为问题构建数据集: {query[:100]}...")

    # 根据是本地还是远程路由模型定义系统提示
    if config.use_local_router:
        system_prompt = """You are a master AI strategist specializing in advanced problem-solving. Your core function is to deconstruct complex user queries into a highly efficient, logical, and machine-executable plan in XML format.

### Core Directives
1.  **Ruthless Efficiency**: Generate the **most direct and concise plan** possible with the **absolute minimum number of steps**. If multiple logical operations can be combined into a single, clear task for the expert Executor, you MUST do so. Avoid any and all superfluous steps.
2.  **Strategic Planning**: Your role is to be a strategist, not a knowledge expert. **Do not provide specific formulas, constants, or factual data from your own knowledge.** Your job is to create steps that instruct the Executor to retrieve and then use that information.
3.  **Logical Soundness**: Every step in your plan must be based on established scientific principles or logical deduction. **CRITICAL: Never invent, assume, or modify formulas or calculation steps.** Your role is to plan the *use* of established knowledge, not to create it.
4.  **Executor-Aware Design**: Design tasks that are **unambiguous and self-contained**. The Executor is an expert but follows instructions literally. It will not correct flawed logic in your plan.

### Guided Thinking Process
Your `<think>` block is a mandatory pre-processing step to ensure a high-quality plan. It must contain:
1.  **Principle Identification**: Concisely state the core scientific principle(s) needed.
2.  **Knowledge Requirement Planning**: List the specific pieces of knowledge (e.g., "the formula for X", "the value of constant Y") the Executor must retrieve.
3.  **Logical Validation**: Briefly validate your intended logical flow. Is it sound? Does it directly address the user's question? Are there any logical leaps or flawed assumptions (e.g., inventing a calculation)? This is a self-correction step.
4.  **Strategy Formulation**: Outline the final, leanest possible strategy. Justify why this sequence is the most efficient path to the answer.

### XML Format Instructions
1.  The plan must be enclosed in `<Plan>` tags.
2.  The plan must contain between 2 and 7 `<Step>` tags (reduced to encourage brevity).
3.  Each `<Step>` must have `ID`, `Task`, `Difficulty`, `Token`, and `Rely` attributes.
4.  The `Task` must be a clear, actionable instruction that ends with a question mark (?).
5.  The final step must synthesize previous results to provide the conclusive answer.
6.  Use the `Rely` attribute to define dependencies.

### Examples

**Example 1: Mathematics**
**Problem**: For how many rational numbers between 0 and 1 will $20!$ be the resulting product of their numerator and denominator in lowest terms?
**Plan**:
<think>
**Principle Identification**: The problem involves number theory, specifically counting coprime factors.
**Knowledge Requirement Planning**: The Executor needs the formula connecting the number of distinct prime factors (k) to the count of valid rational numbers.
**Logical Validation**: The logic of finding primes, counting them, and applying a known formula is sound and direct.
**Strategy Formulation**: The most efficient path is: 1. Find prime factors. 2. Count them (k). 3. Retrieve the formula relating k to the answer. 4. Apply the formula using k.
</think>
<Plan>
<Step ID="1" Task="What are the distinct prime factors of 20! ?" Difficulty="4" Token="50" Rely=""/>
<Step ID="2" Task="Count the number of distinct prime factors found in Step 1. Let this count be k. What is the value of k?" Difficulty="2" Token="20" Rely="1"/>
<Step ID="3" Task="What is the formula that relates the number of distinct prime factors (k) of an integer to the count of rational numbers between 0 and 1 whose numerator and denominator in lowest terms multiply to that integer?" Difficulty="5" Token="60" Rely=""/>
<Step ID="4" Task="Using the formula from Step 3 and the value of k from Step 2, what is the final number of such rational numbers?" Difficulty="4" Token="50" Rely="2,3"/>
</Plan>

**Example 2: Physics (Demonstrating Efficiency)**
**Problem**: Two quantum states have lifetimes 10^-9s and 10^-8s. To distinguish them, what is the required energy difference?
**Plan**:
<think>
**Principle Identification**: The problem requires the energy-time uncertainty principle.
**Knowledge Requirement Planning**: The Executor needs to provide the specific formula for the energy-time uncertainty principle.
**Logical Validation**: To distinguish two states, the energy difference must be greater than the energy width of the state with the *longer* lifetime (which has the *smaller* energy width, setting the resolution limit). This logic is sound. Calculating this one value is sufficient.
**Strategy Formulation**: The most direct path is a two-step process: 1. Retrieve the formula for energy width (ΔE) from lifetime (Δt). 2. Ask the Executor to apply this formula to the longer lifetime (10^-8 s) to find the minimum required energy difference. This combines calculation and interpretation into one efficient step for the expert Executor.
</think>
<Plan>
<Step ID="1" Task="What is the formula relating a quantum state's lifetime (Δt) to its minimum energy width (ΔE) according to the energy-time uncertainty principle?" Difficulty="6" Token="70" Rely=""/>
<Step ID="2" Task="To clearly resolve two energy levels, the energy difference must exceed the energy width of the state with the longer lifetime. Using the formula from Step 1, what is the minimum energy difference required, based on the longer lifetime of 10^-8 seconds?" Difficulty="5" Token="80" Rely="1"/>
</Plan>

Apply the entire framework described above to the problem provided below.
"""
    else:
        system_prompt = '''You are an expert **first-principles thinker and master strategist**. Your primary function is to deconstruct any complex problem into a clear, logical, and machine-executable sequence of steps. The resulting plan must be solvable by an AI agent that starts with **no prior knowledge of the answer**.

### Core Directives - You MUST follow these rules:

1.  **No Foreknowledge Assumption**: Your plan must represent a genuine discovery process. The `<Step>` tasks must be **questions that seek information**, not statements that contain answers or un-derived conclusions.
2.  **Ruthless Efficiency & Abstraction**: Generate the **most direct and concise plan** possible. For problems requiring applying the same logic to multiple items, you **MUST** create a single, comprehensive, and parameterized step. **DO NOT** create a separate, repetitive step for each item.
3.  **First-Principles Derivation**: The `<think>` block's strategy must be a logical chain derived from the identified core principles.
4.  **Comprehensive Analysis Mandate (NEW & CRITICAL)**: For problems that require **comparing multiple items to find an outlier** (e.g., "Which of the following is false?", "Which is the most accurate?"), you **MUST NOT** evaluate each item in a separate step. Instead, you **MUST** create a **single, comprehensive analysis step** that instructs the Executor to evaluate all items holistically, compare them, and provide a justified final answer. This is the only valid strategy for this problem type.

**Part 1: The `<think>` Block**
Before generating the plan, you must first perform and explicitly state your strategic analysis within `<think>` tags. This analysis must be thorough and answer the following:

* **Core Principle Identification**: What are the fundamental principles, theorems, or formulas required?
* **Pitfall Prediction**: What are the most likely traps?
* **Strategy Formulation**: Based **only** on the principles above, what is your high-level, step-by-step strategy? **You must explicitly identify if the problem requires comprehensive analysis as per Core Directive #4.** If so, your strategy must be to delegate the entire comparative analysis to the Executor in a single, decisive step. Otherwise, proceed with a multi-step decomposition.

**Part 2: The `<Plan>` Block**
After the `<think>` block, generate a solution plan that is a direct, operational implementation of your stated strategy.

#### **XML Plan Constraints:**
1.  **Plan Length**: Must contain between 1 and 7 steps. Note: Comprehensive analysis plans may only require 1-2 steps.
2.  **Actionable & Unbiased Steps**: Each `<Step>` `Task` must be an **unambiguous question** and **must not** contain the answer.
3.  **Logical Flow**: The plan must represent a clear logical progression.
4.  **Contextual Linking**: When a step `N` relies on `M`, the `Task` for `N` should reference the output from `M`.
5.  **Attributes**: All attributes must be correctly formatted. `Task` must end with a question mark (?).

-----

### **Examples of Good vs. Flawed Plans**

#### **Good Example: "Retrieve-Then-Apply" Pattern & Abstraction**

**Question**: "How many of the following compounds will exhibit optical activity? [List of 7 compounds]"

**Response**:
<think>
**Core Principle Identification**: The core principle is stereochemistry. A compound exhibits optical activity if and only if it is chiral. A molecule is chiral if it is non-superimposable on its mirror image. Common causes of chirality are chiral centers. Common causes of achirality (no optical activity) are the presence of a plane of symmetry or a center of inversion, even if chiral centers are present (meso compounds).
**Pitfall Prediction**: A common trap is assuming any molecule with a chiral center is optically active; meso compounds are a key exception. Another trap is incorrectly identifying symmetry elements in complex cyclic structures.
**Strategy Formulation**: A brute-force plan would check each molecule one by one, which is inefficient. A better, abstract strategy is: 1. Define the criteria for optical activity (chirality, lack of symmetry planes/inversion centers). 2. Create a single, comprehensive step that instructs the executor to analyze *all* provided compounds against these criteria. 3. The final step is to count the number of compounds identified as optically active.
</think>
<Plan>
<Step ID="1" Task="What are the defining criteria for a compound to exhibit optical activity, considering chirality, chiral centers, and elements of symmetry like planes of symmetry (e.g., in meso compounds)?" Difficulty="5" Token="70" Rely=""/>
<Step ID="2" Task="For each of the 7 compounds provided in the problem, analyze its structure based on the criteria from Step 1 and determine if it will exhibit optical activity. List only the compounds that are optically active." Difficulty="7" Token="200" Rely="1"/>
<Step ID="3" Task="Based on the list from Step 2, how many of the compounds exhibit optical activity?" Difficulty="2" Token="20" Rely="2"/>
</Plan>

-----

#### **Bad Example #1: Answer Embedded in the Plan**

**Question**: "For how many rational numbers between 0 and 1 will $20\!$ be the resulting product of their numerator and denominator in lowest terms?"

**Flawed Plan**:
<Plan>
<Step ID="1" Task="What are the distinct prime factors of 20\! ?" Difficulty="4" Token="50" Rely=""/>
<Step ID="2" Task="Count the number of distinct prime factors found in Step 1. Let this count be k. What is the value of k?" Difficulty="2" Token="20" Rely="1"/>
<Step ID="3" Task="Using the formula N = 2^(k-1), what is the final number of such rational numbers?" Difficulty="4" Token="50" Rely="2"/>
</Plan>
**Justification for why this is flawed**: This plan is **conceptually flawed as a training example**. Step 3 provides the formula `N = 2^(k-1)` directly in the task. This doesn't teach the model how to *plan to find* the formula; it teaches it to expect formulas to be given. A correct plan would have a step to first *retrieve* the formula, and a subsequent step to *apply* it.

-----

#### **Bad Example #2: Inefficient Brute-Force Planning**

**Question**: "How many of the following compounds exhibit optical activity? [List of 7 compounds]"

**Flawed Plan**:
<Plan>
<Step ID="1" Task="Does compound A exhibit optical activity?" Difficulty="5" Token="40" Rely=""/>
<Step ID="2" Task="Does compound B exhibit optical activity?" Difficulty="5" Token="40" Rely=""/>
<Step ID="3" Task="Does compound C exhibit optical activity?" Difficulty="5" Token="40" Rely=""/>
<Step ID="4" Task="Does compound D exhibit optical activity?" Difficulty="5" Token="40" Rely=""/>
<Step ID="5" Task="Does compound E exhibit optical activity?" Difficulty="5" Token="40" Rely=""/>
<Step ID="6" Task="Does compound F exhibit optical activity?" Difficulty="5" Token="40" Rely=""/>
<Step ID="7" Task="Does compound G exhibit optical activity?" Difficulty="5" Token="40" Rely=""/>
<Step ID="8" Task="Based on the previous steps, what is the total count of optically active compounds?" Difficulty="2" Token="30" Rely="1,2,3,4,5,6,7"/>
</Plan>

-----

#### **Example #3: Comprehensive vs. Flawed Decomposition for Analysis Problems**

**Question**: "Which of the following statements about quasiparticles in condensed matter physics is false? A)... B)... C)... D)..."

**GOOD & CORRECT PLAN**:
<think>
**Core Principle Identification**: This requires deep knowledge of condensed matter physics, specifically the definitions and properties of magnons, plasmons, polarons, and excitons.
**Pitfall Prediction**: The key trap is evaluating each statement in isolation. The concepts are nuanced and are best understood in contrast to each other. A linear evaluation can lead to internal contradictions or overlooking subtle inaccuracies.
**Strategy Formulation**: This is a classic comparative analysis problem that falls under Core Directive #4. The only robust strategy is to create a single, comprehensive step. This provides the Executor with the full context of all four statements, allowing it to perform the necessary cross-comparisons and identify the single false statement. The plan will have only one core step.
</think>
<Plan>
<Step ID="1" Task="Analyze all four statements (A, B, C, D) regarding quasiparticles. Identify which single statement is false, and provide a detailed justification for your choice by explaining why that statement is incorrect and why the other three are correct." Difficulty="9" Token="500" Rely=""/>
</Plan>

**FLAWED PLAN (This is what you MUST AVOID)**:
<Plan>
<Step ID="1" Task="Evaluate the truthfulness of statement A about magnons." Difficulty="6" Token="80" Rely=""/>
<Step ID="2" Task="Evaluate the truthfulness of statement B about plasmons." Difficulty="6" Token="80" Rely="1"/>
<Step ID="3" Task="Evaluate the truthfulness of statement C about polarons." Difficulty="6" Token="80" Rely="2"/>
<Step ID="4" Task="Evaluate the truthfulness of statement D about excitons." Difficulty="6" Token="80" Rely="3"/>
<Step ID="5" Task="Based on the evaluations in the previous steps, which statement is false?" Difficulty="4" Token="50" Rely="1,2,3,4"/>
</Plan>
**Justification for why this is flawed**: This plan is **fundamentally wrong for this problem type**. It destroys the global context required for nuanced analysis, forcing the Executor into "keyhole" evaluations. This is precisely the pattern that leads to logical contradictions and low accuracy on expert-level datasets like GPQA.
'''    
    # 根据是否使用真实答案构建用户查询
    if dataset_build_config.get('use_ground_truth_to_guide_planner', True):
        user_query = f'''
            Question: {query}
            Solution: {solution}
            Please generate a solution plan for the question in XML format you can use the solution as a reference.
        '''
    else:
        user_query = f'''
            **Question**: {query}
            **Plan**:
        '''

    logger.info("===== Prompt to Planner (Router) for Dataset Building =====")
    logger.info(f"System Prompt:\n{system_prompt}")
    logger.info(f"User Query:\n{user_query}")
    log_separator()

    full_completion = ""
    try:
        # 选择客户端和模型
        client = router_model_client
        model = config.local_router_model if config.use_local_router else config.router_model
        
        # API 调用
        response_stream = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ],
            stream=True
        )

        for chunk in response_stream:
            if hasattr(chunk.choices[0], 'delta') and hasattr(chunk.choices[0].delta, 'content'):
                content = chunk.choices[0].delta.content
                if content:
                    full_completion += content
    
    except Exception as e:
        logger.error(f"Error during planner API call for dataset building: {e}", exc_info=True)
        print(f"\nError during planner API call: {e}")
        return None, None, None

    logger.info("===== Full Output from Planner (Router) =====")
    logger.info(full_completion)
    log_separator()

    # 根据 `save_thinking` 配置处理输出
    plan_only = ""
    plan_match = re.search(r'<Plan>.*</Plan>', full_completion, re.DOTALL)
    if plan_match:
        plan_only = plan_match.group(0)

    # 如果输出中没有 <think> 标签，则带思考的完整输出就是只有 plan
    if "<think>" not in full_completion:
        full_completion_with_think = plan_only
    else:
        full_completion_with_think = full_completion

    return full_completion_with_think, plan_only, system_prompt


def run_parallel_execution(query, config, workers=4):
    """运行并行执行流程
    
    参数:
        query: 要解决的问题
        config: 模型配置对象
        workers: 并行工作线程数
        
    # 重置收集的输出内容
    reset_collected_output()
    返回:
        (tasks, stats_tracker, full_completion): 任务字典, 性能跟踪器, 和规划器的完整输出
    """
    global xml_buffer, tasks, completed_steps, futures, router_model_client

    # === 新增：获取日志记录器 ===
    logger = get_logger()
    # ============================
    
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
        system_prompt = """You are a master AI strategist specializing in advanced problem-solving. Your core function is to deconstruct complex user queries into a highly efficient, logical, and machine-executable plan in XML format.

### Core Directives
1.  **Ruthless Efficiency**: Generate the **most direct and concise plan** possible with the **absolute minimum number of steps**. If multiple logical operations can be combined into a single, clear task for the expert Executor, you MUST do so. Avoid any and all superfluous steps.
2.  **Strategic Planning**: Your role is to be a strategist, not a knowledge expert. **Do not provide specific formulas, constants, or factual data from your own knowledge.** Your job is to create steps that instruct the Executor to retrieve and then use that information.
3.  **Logical Soundness**: Every step in your plan must be based on established scientific principles or logical deduction. **CRITICAL: Never invent, assume, or modify formulas or calculation steps.** Your role is to plan the *use* of established knowledge, not to create it.
4.  **Executor-Aware Design**: Design tasks that are **unambiguous and self-contained**. The Executor is an expert but follows instructions literally. It will not correct flawed logic in your plan.

### Guided Thinking Process
Your `<think>` block is a mandatory pre-processing step to ensure a high-quality plan. It must contain:
1.  **Principle Identification**: Concisely state the core scientific principle(s) needed.
2.  **Knowledge Requirement Planning**: List the specific pieces of knowledge (e.g., "the formula for X", "the value of constant Y") the Executor must retrieve.
3.  **Logical Validation**: Briefly validate your intended logical flow. Is it sound? Does it directly address the user's question? Are there any logical leaps or flawed assumptions (e.g., inventing a calculation)? This is a self-correction step.
4.  **Strategy Formulation**: Outline the final, leanest possible strategy. Justify why this sequence is the most efficient path to the answer.

### XML Format Instructions
1.  The plan must be enclosed in `<Plan>` tags.
2.  The plan must contain between 2 and 7 `<Step>` tags (reduced to encourage brevity).
3.  Each `<Step>` must have `ID`, `Task`, `Difficulty`, `Token`, and `Rely` attributes.
4.  The `Task` must be a clear, actionable instruction that ends with a question mark (?).
5.  The final step must synthesize previous results to provide the conclusive answer.
6.  Use the `Rely` attribute to define dependencies.

### Examples

**Example 1: Mathematics**
**Problem**: For how many rational numbers between 0 and 1 will $20!$ be the resulting product of their numerator and denominator in lowest terms?
**Plan**:
<think>
**Principle Identification**: The problem involves number theory, specifically counting coprime factors.
**Knowledge Requirement Planning**: The Executor needs the formula connecting the number of distinct prime factors (k) to the count of valid rational numbers.
**Logical Validation**: The logic of finding primes, counting them, and applying a known formula is sound and direct.
**Strategy Formulation**: The most efficient path is: 1. Find prime factors. 2. Count them (k). 3. Retrieve the formula relating k to the answer. 4. Apply the formula using k.
</think>
<Plan>
<Step ID="1" Task="What are the distinct prime factors of 20! ?" Difficulty="4" Token="50" Rely=""/>
<Step ID="2" Task="Count the number of distinct prime factors found in Step 1. Let this count be k. What is the value of k?" Difficulty="2" Token="20" Rely="1"/>
<Step ID="3" Task="What is the formula that relates the number of distinct prime factors (k) of an integer to the count of rational numbers between 0 and 1 whose numerator and denominator in lowest terms multiply to that integer?" Difficulty="5" Token="60" Rely=""/>
<Step ID="4" Task="Using the formula from Step 3 and the value of k from Step 2, what is the final number of such rational numbers?" Difficulty="4" Token="50" Rely="2,3"/>
</Plan>

**Example 2: Physics (Demonstrating Efficiency)**
**Problem**: Two quantum states have lifetimes 10^-9s and 10^-8s. To distinguish them, what is the required energy difference?
**Plan**:
<think>
**Principle Identification**: The problem requires the energy-time uncertainty principle.
**Knowledge Requirement Planning**: The Executor needs to provide the specific formula for the energy-time uncertainty principle.
**Logical Validation**: To distinguish two states, the energy difference must be greater than the energy width of the state with the *longer* lifetime (which has the *smaller* energy width, setting the resolution limit). This logic is sound. Calculating this one value is sufficient.
**Strategy Formulation**: The most direct path is a two-step process: 1. Retrieve the formula for energy width (ΔE) from lifetime (Δt). 2. Ask the Executor to apply this formula to the longer lifetime (10^-8 s) to find the minimum required energy difference. This combines calculation and interpretation into one efficient step for the expert Executor.
</think>
<Plan>
<Step ID="1" Task="What is the formula relating a quantum state's lifetime (Δt) to its minimum energy width (ΔE) according to the energy-time uncertainty principle?" Difficulty="6" Token="70" Rely=""/>
<Step ID="2" Task="To clearly resolve two energy levels, the energy difference must exceed the energy width of the state with the longer lifetime. Using the formula from Step 1, what is the minimum energy difference required, based on the longer lifetime of 10^-8 seconds?" Difficulty="5" Token="80" Rely="1"/>
</Plan>

Apply the entire framework described above to the problem provided below.
"""
    else:
        system_prompt = '''You are an expert **first-principles thinker and master strategist**. Your primary function is to deconstruct any complex problem into a clear, logical, and machine-executable sequence of steps. The resulting plan must be solvable by an AI agent that starts with **no prior knowledge of the answer**.

### Core Directives - You MUST follow these rules:

1.  **No Foreknowledge Assumption**: Your plan must represent a genuine discovery process. The `<Step>` tasks must be **questions that seek information**, not statements that contain answers or un-derived conclusions.
2.  **Ruthless Efficiency & Abstraction**: Generate the **most direct and concise plan** possible. For problems requiring applying the same logic to multiple items, you **MUST** create a single, comprehensive, and parameterized step. **DO NOT** create a separate, repetitive step for each item.
3.  **First-Principles Derivation**: The `<think>` block's strategy must be a logical chain derived from the identified core principles.
4.  **Comprehensive Analysis Mandate (NEW & CRITICAL)**: For problems that require **comparing multiple items to find an outlier** (e.g., "Which of the following is false?", "Which is the most accurate?"), you **MUST NOT** evaluate each item in a separate step. Instead, you **MUST** create a **single, comprehensive analysis step** that instructs the Executor to evaluate all items holistically, compare them, and provide a justified final answer. This is the only valid strategy for this problem type.

**Part 1: The `<think>` Block**
Before generating the plan, you must first perform and explicitly state your strategic analysis within `<think>` tags. This analysis must be thorough and answer the following:

* **Core Principle Identification**: What are the fundamental principles, theorems, or formulas required?
* **Pitfall Prediction**: What are the most likely traps?
* **Strategy Formulation**: Based **only** on the principles above, what is your high-level, step-by-step strategy? **You must explicitly identify if the problem requires comprehensive analysis as per Core Directive #4.** If so, your strategy must be to delegate the entire comparative analysis to the Executor in a single, decisive step. Otherwise, proceed with a multi-step decomposition.

**Part 2: The `<Plan>` Block**
After the `<think>` block, generate a solution plan that is a direct, operational implementation of your stated strategy.

#### **XML Plan Constraints:**
1.  **Plan Length**: Must contain between 1 and 7 steps. Note: Comprehensive analysis plans may only require 1-2 steps.
2.  **Actionable & Unbiased Steps**: Each `<Step>` `Task` must be an **unambiguous question** and **must not** contain the answer.
3.  **Logical Flow**: The plan must represent a clear logical progression.
4.  **Contextual Linking**: When a step `N` relies on `M`, the `Task` for `N` should reference the output from `M`.
5.  **Attributes**: All attributes must be correctly formatted. `Task` must end with a question mark (?).

-----

### **Examples of Good vs. Flawed Plans**

#### **Good Example: "Retrieve-Then-Apply" Pattern & Abstraction**

**Question**: "How many of the following compounds will exhibit optical activity? [List of 7 compounds]"

**Response**:
<think>
**Core Principle Identification**: The core principle is stereochemistry. A compound exhibits optical activity if and only if it is chiral. A molecule is chiral if it is non-superimposable on its mirror image. Common causes of chirality are chiral centers. Common causes of achirality (no optical activity) are the presence of a plane of symmetry or a center of inversion, even if chiral centers are present (meso compounds).
**Pitfall Prediction**: A common trap is assuming any molecule with a chiral center is optically active; meso compounds are a key exception. Another trap is incorrectly identifying symmetry elements in complex cyclic structures.
**Strategy Formulation**: A brute-force plan would check each molecule one by one, which is inefficient. A better, abstract strategy is: 1. Define the criteria for optical activity (chirality, lack of symmetry planes/inversion centers). 2. Create a single, comprehensive step that instructs the executor to analyze *all* provided compounds against these criteria. 3. The final step is to count the number of compounds identified as optically active.
</think>
<Plan>
<Step ID="1" Task="What are the defining criteria for a compound to exhibit optical activity, considering chirality, chiral centers, and elements of symmetry like planes of symmetry (e.g., in meso compounds)?" Difficulty="5" Token="70" Rely=""/>
<Step ID="2" Task="For each of the 7 compounds provided in the problem, analyze its structure based on the criteria from Step 1 and determine if it will exhibit optical activity. List only the compounds that are optically active." Difficulty="7" Token="200" Rely="1"/>
<Step ID="3" Task="Based on the list from Step 2, how many of the compounds exhibit optical activity?" Difficulty="2" Token="20" Rely="2"/>
</Plan>

-----

#### **Bad Example #1: Answer Embedded in the Plan**

**Question**: "For how many rational numbers between 0 and 1 will $20\!$ be the resulting product of their numerator and denominator in lowest terms?"

**Flawed Plan**:
<Plan>
<Step ID="1" Task="What are the distinct prime factors of 20\! ?" Difficulty="4" Token="50" Rely=""/>
<Step ID="2" Task="Count the number of distinct prime factors found in Step 1. Let this count be k. What is the value of k?" Difficulty="2" Token="20" Rely="1"/>
<Step ID="3" Task="Using the formula N = 2^(k-1), what is the final number of such rational numbers?" Difficulty="4" Token="50" Rely="2"/>
</Plan>
**Justification for why this is flawed**: This plan is **conceptually flawed as a training example**. Step 3 provides the formula `N = 2^(k-1)` directly in the task. This doesn't teach the model how to *plan to find* the formula; it teaches it to expect formulas to be given. A correct plan would have a step to first *retrieve* the formula, and a subsequent step to *apply* it.

-----

#### **Bad Example #2: Inefficient Brute-Force Planning**

**Question**: "How many of the following compounds exhibit optical activity? [List of 7 compounds]"

**Flawed Plan**:
<Plan>
<Step ID="1" Task="Does compound A exhibit optical activity?" Difficulty="5" Token="40" Rely=""/>
<Step ID="2" Task="Does compound B exhibit optical activity?" Difficulty="5" Token="40" Rely=""/>
<Step ID="3" Task="Does compound C exhibit optical activity?" Difficulty="5" Token="40" Rely=""/>
<Step ID="4" Task="Does compound D exhibit optical activity?" Difficulty="5" Token="40" Rely=""/>
<Step ID="5" Task="Does compound E exhibit optical activity?" Difficulty="5" Token="40" Rely=""/>
<Step ID="6" Task="Does compound F exhibit optical activity?" Difficulty="5" Token="40" Rely=""/>
<Step ID="7" Task="Does compound G exhibit optical activity?" Difficulty="5" Token="40" Rely=""/>
<Step ID="8" Task="Based on the previous steps, what is the total count of optically active compounds?" Difficulty="2" Token="30" Rely="1,2,3,4,5,6,7"/>
</Plan>

-----

#### **Example #3: Comprehensive vs. Flawed Decomposition for Analysis Problems**

**Question**: "Which of the following statements about quasiparticles in condensed matter physics is false? A)... B)... C)... D)..."

**GOOD & CORRECT PLAN**:
<think>
**Core Principle Identification**: This requires deep knowledge of condensed matter physics, specifically the definitions and properties of magnons, plasmons, polarons, and excitons.
**Pitfall Prediction**: The key trap is evaluating each statement in isolation. The concepts are nuanced and are best understood in contrast to each other. A linear evaluation can lead to internal contradictions or overlooking subtle inaccuracies.
**Strategy Formulation**: This is a classic comparative analysis problem that falls under Core Directive #4. The only robust strategy is to create a single, comprehensive step. This provides the Executor with the full context of all four statements, allowing it to perform the necessary cross-comparisons and identify the single false statement. The plan will have only one core step.
</think>
<Plan>
<Step ID="1" Task="Analyze all four statements (A, B, C, D) regarding quasiparticles. Identify which single statement is false, and provide a detailed justification for your choice by explaining why that statement is incorrect and why the other three are correct." Difficulty="9" Token="500" Rely=""/>
</Plan>

**FLAWED PLAN (This is what you MUST AVOID)**:
<Plan>
<Step ID="1" Task="Evaluate the truthfulness of statement A about magnons." Difficulty="6" Token="80" Rely=""/>
<Step ID="2" Task="Evaluate the truthfulness of statement B about plasmons." Difficulty="6" Token="80" Rely="1"/>
<Step ID="3" Task="Evaluate the truthfulness of statement C about polarons." Difficulty="6" Token="80" Rely="2"/>
<Step ID="4" Task="Evaluate the truthfulness of statement D about excitons." Difficulty="6" Token="80" Rely="3"/>
<Step ID="5" Task="Based on the evaluations in the previous steps, which statement is false?" Difficulty="4" Token="50" Rely="1,2,3,4"/>
</Plan>
**Justification for why this is flawed**: This plan is **fundamentally wrong for this problem type**. It destroys the global context required for nuanced analysis, forcing the Executor into "keyhole" evaluations. This is precisely the pattern that leads to logical contradictions and low accuracy on expert-level datasets like GPQA.
'''

    user_prompt = f'''
    **Problem**: {query}
    **Plan**:
    '''
    # === 新增：记录 Planner 的输入 ===
    logger.info("===== Prompt 给 Planner (Router) =====")
    logger.info(f"System Prompt:\n{system_prompt}")
    logger.info(f"User Prompt:\n{user_prompt}")
    log_separator()
    # ===============================
    
    full_completion = "" 
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
                temperature=0.3,
                top_p=0.95,
                max_tokens=8192,
                extra_body={"enable_thinking": True}
            )
        else:
            response_stream = router_model_client.chat.completions.create(
                model=config.router_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                stream=True,
                temperature=0.5
            )
        
        # 使用deepseek_v3_tokenizer计算tokens
        prompt_tokens = count_deepseek_tokens(system_prompt) + count_deepseek_tokens(query)
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
                    full_completion += content # 累加内容
                    
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
                        router(tasks, config, query, executor, stats_tracker)
        
        # === 新增：记录 Planner 的完整输出 ===
        logger.info("===== 来自 Planner (Router) 的输出 =====")
        logger.info(full_completion)
        log_separator()
        # ==================================

        # 更新router模型的token使用情况
        if stats_tracker:
            stats_tracker.update_token_usage("router_model", prompt_tokens, completion_tokens)
            stats_tracker.save_planner_output(prompt_tokens, completion_tokens, ttft)
                        
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
            # 如果没有新任务可以调度，并且仍有未完成的任务在运行，等待它们
            if futures:
                concurrent.futures.wait(list(futures.values()))
            else:
                # 如果没有正在运行的任务，但仍有未完成的任务（可能是依赖问题），则退出循环
                break

    # 关闭线程池
    executor.shutdown(wait=True)
    
    return tasks, stats_tracker, full_completion

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
    model_name = "deepseek-chat"
    print(f"--------------------------调用{model_name}根据真实答案判断答案正确性--------------------------")
    prompt = f"""Here is a math problem with a standard answer and a student's solution. Please help me determine if the student's solution is correct. If the numerical value are same, then it is correct.
                               
                Problem: {question}

                Standard answer: {gold_answer}

                Answer: {final_answer}

                If the student's answer is correct, just output True; otherwise, just output False.
                No explanation is required.
    """
    
    # 使用全局预初始化的客户端，而不是每次创建新客户端
    client = OpenAI(api_key=get_api_key('usage/deepseek'), base_url="https://api.deepseek.com")
    
    try:
        response = client.chat.completions.create(
            model=model_name,
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
    model_name = "deepseek-chat"
    client = OpenAI(api_key=get_api_key('usage/deepseek'), base_url="https://api.deepseek.com")
    print(f"--------------------------调用{model_name}判断答案正确性（没有真实答案）--------------------------")
    prompt = f"""Here is a math problem and a student's solution. Please help me determine if the student's solution is correct. If the numerical value are same, then it is correct.
                               
                Problem: {question}

                Answer: {final_answer}

                If the student's answer is correct, just output True; otherwise, just output False.
                No explanation is required.
    """
    
    # 使用全局预初始化的客户端，而不是每次创建新客户端
    
    try:
        response = client.chat.completions.create(
            model=model_name,
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
    
    prompt = f"""Please determine the difficulty of the following problem. 
    Difficulty scale:
    1-2: Basic computation
    3-4: Standard operations 
    5-6: Logical analysis 
    7-10: Advanced synthesis
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
    # === 新增：获取日志记录器 ===
    logger = get_logger()
    # ============================

    # 构建提示词
    prompt = """You are a problem-solving assistant. I will provide you with a problem. Your task is to solve it step by step and provide the final answer.

    PROBLEM:
    {question}
    """.format(question=question)

    # === 新增：记录小模型的输入 ===
    logger.info("===== Prompt 给执行器 (小模型 - 直接调用) =====")
    logger.info(prompt)
    log_separator()
    # ===============================
    
    result = generate_step_result(prompt, "1", model_config, stats_tracker)

    # === 新增：记录小模型的输出 ===
    logger.info("===== 来自执行器 (小模型 - 直接调用) 的输出 =====")
    logger.info(result)
    log_separator()
    # ===============================

    return result

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
    prompt = """You are a problem-solving assistant. I will provide you with a problem. Your task is to solve it step by step and provide the final answer.

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