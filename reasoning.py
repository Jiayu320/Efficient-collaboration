import requests
import json
import os
import re
from collections import defaultdict
from openai import OpenAI
import time
import argparse
import yaml
from typing import Dict, Any


class ModelConfig:
    """模型配置类，用于管理API和模型设置"""
    
    def __init__(self, 
                 small_model="qwen/qwen3-14b:free", 
                 large_model="qwen/qwen3-235b-a22b", 
                 threshold=2,
                 api_key_path="usage/openrouter",
                 prompt_path="prompt/generate_prompt.txt",
                 api_base="https://openrouter.ai/api/v1"):
        """
        初始化模型配置
        
        参数:
            small_model: 小模型的名称
            large_model: 大模型的名称
            threshold: 使用大模型的难度阈值
            api_key_path: API密钥文件路径
            prompt_path: 提示词文件路径
            api_base: API基础URL
        """
        self.small_model = small_model
        self.large_model = large_model
        self.threshold = threshold
        self.api_key_path = api_key_path
        self.api_base = api_base
        
        # 加载API密钥
        self.api_key = self._get_api_key(api_key_path)
        
        # 加载提示词
        try:
            with open(prompt_path, 'r', encoding='utf-8') as f:
                self.system_prompt = f.read()
        except Exception as e:
            print(f"无法加载提示词文件: {e}")
            self.system_prompt = ""
    
    def _get_api_key(self, file_path):
        """从文件中获取API密钥"""
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return f.read().strip()
        else:
            raise FileNotFoundError(f"API密钥文件 '{file_path}' 未找到")
    
    def get_headers(self):
        """获取API请求头"""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def get_payload(self, query, model_override=None):
        """获取API请求载荷"""
        model = model_override if model_override else self.small_model
        return {
            "model": model,
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": query}
            ],
            "stream": True
        }
    
    def get_client(self):
        """获取OpenAI客户端"""
        return OpenAI(
            base_url=self.api_base,
            api_key=self.api_key
        )
    
    def select_model_by_difficulty(self, difficulty):
        """根据难度选择模型"""
        difficulty = int(difficulty) if difficulty.isdigit() else 0
        if difficulty < self.threshold:
            return self.small_model
        else:
            return self.large_model


def load_config(config_path="config.yaml") -> Dict[str, Any]:
    """加载YAML配置文件
    
    参数:
        config_path: 配置文件路径
        
    返回:
        配置字典
    """
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        return config
    except Exception as e:
        print(f"无法加载配置文件 {config_path}: {e}")
        # 返回默认配置
        return {
            "models": {
                "small_model": "qwen/qwen3-14b:free",
                "large_model": "qwen/qwen3-235b-a22b",
                "threshold": 2
            },
            "api": {
                "key_path": "usage/openrouter",
                "base_url": "https://openrouter.ai/api/v1"
            },
            "system": {
                "prompt_path": "prompt/generate_prompt.txt",
                "workers": 4
            },
            "query": "What is the result of 1+1?"
        }

def parse_args():
    """解析命令行参数，可覆盖配置文件中的设置"""
    parser = argparse.ArgumentParser(description='并行任务处理系统')
    parser.add_argument('--config', type=str, default="config.yaml",
                      help='配置文件路径')
    parser.add_argument('--query', type=str,
                      help='要解决的问题 (覆盖配置文件)')
    parser.add_argument('--small-model', type=str,
                      help='小模型名称 (覆盖配置文件)')
    parser.add_argument('--large-model', type=str,
                      help='大模型名称 (覆盖配置文件)')
    parser.add_argument('--threshold', type=int,
                      help='使用大模型的难度阈值 (覆盖配置文件)')
    parser.add_argument('--api-key', type=str,
                      help='API密钥文件路径 (覆盖配置文件)')
    parser.add_argument('--workers', type=int,
                      help='并行工作线程数 (覆盖配置文件)')
    return parser.parse_args()


# 解析命令行参数
args = parse_args()

# 加载配置文件
yaml_config = load_config(args.config)

# 构建最终配置（命令行参数优先）
small_model = args.small_model if args.small_model else yaml_config["models"]["small_model"]
large_model = args.large_model if args.large_model else yaml_config["models"]["large_model"]
threshold = args.threshold if args.threshold is not None else yaml_config["models"]["threshold"]
api_key_path = args.api_key if args.api_key else yaml_config["api"]["key_path"]
api_base = yaml_config["api"]["base_url"]
prompt_path = yaml_config["system"]["prompt_path"]
workers = args.workers if args.workers is not None else yaml_config["system"]["workers"]

# 初始化模型配置
config = ModelConfig(
    small_model=small_model,
    large_model=large_model,
    threshold=threshold,
    api_key_path=api_key_path,
    prompt_path=prompt_path,
    api_base=api_base
)

# 设置查询
query = args.query if args.query else yaml_config["query"]

# 用于存储解析后的任务数据
tasks = defaultdict(dict)
current_step = None
xml_buffer = ""

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
    # 根据难度选择模型
    model = model_config.select_model_by_difficulty(difficulty)
    
    # 获取客户端
    client = model_config.get_client()
    
    # 调用API
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        # 如果有统计跟踪器，更新token使用统计
        if stats_tracker and hasattr(response, 'usage'):
            model_type = "small_model" if model == model_config.small_model else "large_model"
            stats_tracker.update_token_usage(
                model_type,
                response.usage.prompt_tokens,
                response.usage.completion_tokens
            )
        
        return response.choices[0].message.content
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

import concurrent.futures

# 全局变量
# Track completed steps
completed_steps = set()
# Create a thread pool executor - 使用配置设置线程数
executor = concurrent.futures.ThreadPoolExecutor(max_workers=workers)
# Store futures for each step
futures = {}

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

def router(tasks, model_config, query, stats_tracker=None):
    """调度任务并行执行
    
    参数:
        tasks: 任务字典
        model_config: 模型配置对象
        query: 原始查询
        stats_tracker: 性能统计跟踪器
    """
    has_new_tasks = False
    
    # 检查可以开始的新任务
    for step_id in tasks:
        if step_id not in futures and step_id not in completed_steps:
            if is_step_ready(step_id, tasks):
                print(f"调度步骤 {step_id}: {tasks[step_id].get('Task', '未知任务')}")
                # 传递模型配置和性能统计器
                future = executor.submit(process_step, step_id, tasks, query, model_config, stats_tracker)
                futures[step_id] = future
                has_new_tasks = True
    
    # 检查完成的任务
    completed_future_ids = [step_id for step_id, f in list(futures.items()) if f.done()]
    for step_id in completed_future_ids:
        try:
            f = futures[step_id]
            f.result()  # 获取结果，如果有异常会抛出
            del futures[step_id]
            # 当一个任务完成后，立即重新检查依赖项，可能会启动新任务
            has_new_tasks = True
        except Exception as e:
            print(f"任务 {step_id} 执行错误: {e}")
            # 处理错误的任务也应该从队列中移除
            del futures[step_id]
    
    # 如果有正在运行的任务，继续路由
    if futures:
        # time.sleep(0.1)  # 小延迟防止CPU过载
        return True  # 继续路由
    
    # 如果有新任务被添加但没有正在运行的任务，也继续路由
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
    
    # 可选：打印详细任务信息的代码，默认注释掉
    '''
    print("\n\n解析的任务详情:")
    for step_id, attrs in sorted(tasks.items(), key=lambda x: int(x[0])):
        print(f"步骤 {step_id}:")
        for k, v in attrs.items():
            if k != 'Result':  # 不打印详细结果，避免输出过多
                print(f"  {k}: {v}")
        print()
    '''
    
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
        # time.sleep(1)  # 短暂等待以确保所有任务完成
    
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
    prompt = """All subtasks have been completed. Based on the results of all steps below, please provide the final answer. Be concise and clear in your response without additional explanation or clarification.

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
    except Exception as e:
        print(f"获取最终答案时出错: {e}")
        # 如果失败，回退到使用最后一个步骤的结果
        if sorted_tasks:
            last_step_id, last_step = sorted_tasks[-1]
            final_result += f"## 最终答案\n"
            if 'Result' in last_step and last_step['Result']:
                final_result += f"{last_step['Result']}\n"
            else:
                final_result += "（未能获得最终答案）\n"
    
    return final_result

class PerformanceTracker:
    """性能跟踪器类，用于跟踪模型使用情况和成本"""
    
    def __init__(self):
        """初始化性能跟踪器"""
        self.start_time = time.time()
        self.end_time = None
        
        # Token使用统计
        self.token_usage = {
            "small_model": {
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0
            },
            "large_model": {
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0
            },
            "total": {
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0
            }
        }
        
        # 成本估算 (美元/1K tokens)
        self.cost_rates = {
            "small_model": {
                "prompt": 0.0,
                "completion": 0.0
            },
            # $2.50/M input tokens $10/M output tokens
            "large_model": {
                "prompt": 0.0025,  # $2.50 per 1M input tokens
                "completion": 0.0100  # $10 per 1M output tokens
            }
        }
    
    def update_token_usage(self, model_type, prompt_tokens, completion_tokens):
        """更新token使用情况
        
        参数:
            model_type: 模型类型 ("small_model" 或 "large_model")
            prompt_tokens: 输入token数量
            completion_tokens: 输出token数量
        """
        # 更新指定模型的统计
        self.token_usage[model_type]["prompt_tokens"] += prompt_tokens
        self.token_usage[model_type]["completion_tokens"] += completion_tokens
        self.token_usage[model_type]["total_tokens"] += prompt_tokens + completion_tokens
        
        # 更新总统计
        self.token_usage["total"]["prompt_tokens"] += prompt_tokens
        self.token_usage["total"]["completion_tokens"] += completion_tokens
        self.token_usage["total"]["total_tokens"] += prompt_tokens + completion_tokens
    
    def stop_tracking(self):
        """停止性能跟踪"""
        self.end_time = time.time()
    
    def calculate_cost(self):
        """计算总成本
        
        返回:
            总成本（美元）
        """
        small_model_cost = (
            (self.token_usage["small_model"]["prompt_tokens"] / 1000) * self.cost_rates["small_model"]["prompt"] +
            (self.token_usage["small_model"]["completion_tokens"] / 1000) * self.cost_rates["small_model"]["completion"]
        )
        
        large_model_cost = (
            (self.token_usage["large_model"]["prompt_tokens"] / 1000) * self.cost_rates["large_model"]["prompt"] +
            (self.token_usage["large_model"]["completion_tokens"] / 1000) * self.cost_rates["large_model"]["completion"]
        )
        
        return {
            "small_model": small_model_cost,
            "large_model": large_model_cost,
            "total": small_model_cost + large_model_cost
        }
    
    def get_elapsed_time(self):
        """获取总耗时
        
        返回:
            耗时（秒）
        """
        end = self.end_time if self.end_time else time.time()
        return end - self.start_time
    
    def format_performance_report(self):
        """格式化性能报告
        
        返回:
            性能报告文本
        """
        costs = self.calculate_cost()
        elapsed_time = self.get_elapsed_time()
        
        report = "# 性能统计报告\n\n"
        report += f"## 总执行时间\n{elapsed_time:.2f} 秒\n\n"
        
        report += "## Token 使用情况\n\n"
        report += "### 小模型\n"
        report += f"- 输入 Tokens: {self.token_usage['small_model']['prompt_tokens']}\n"
        report += f"- 输出 Tokens: {self.token_usage['small_model']['completion_tokens']}\n"
        report += f"- 总 Tokens: {self.token_usage['small_model']['total_tokens']}\n\n"
        
        report += "### 大模型\n"
        report += f"- 输入 Tokens: {self.token_usage['large_model']['prompt_tokens']}\n"
        report += f"- 输出 Tokens: {self.token_usage['large_model']['completion_tokens']}\n"
        report += f"- 总 Tokens: {self.token_usage['large_model']['total_tokens']}\n\n"
        
        report += "### 总计\n"
        report += f"- 输入 Tokens: {self.token_usage['total']['prompt_tokens']}\n"
        report += f"- 输出 Tokens: {self.token_usage['total']['completion_tokens']}\n"
        report += f"- 总 Tokens: {self.token_usage['total']['total_tokens']}\n\n"
        
        report += "## 成本估算\n\n"
        report += f"- 小模型成本: ${costs['small_model']:.4f}\n"
        report += f"- 大模型成本: ${costs['large_model']:.4f}\n"
        report += f"- 总成本: ${costs['total']:.4f}\n"
        
        return report


def calculate_performance_metrics(stats_tracker):
    """计算性能指标
    
    参数:
        stats_tracker: 性能统计跟踪器
    
    返回:
        性能报告文本
    """
    stats_tracker.stop_tracking()
    return stats_tracker.format_performance_report()


def run_parallel_execution(query, config):
    """运行并行执行流程
    
    参数:
        query: 要解决的问题
        config: 模型配置对象
    """
    global xml_buffer, tasks, completed_steps, futures
    
    # 创建性能统计跟踪器
    stats_tracker = PerformanceTracker()
    
    # 重置全局状态
    xml_buffer = ""
    tasks = defaultdict(dict)
    completed_steps = set()
    futures = {}
    
    # 初始化变量跟踪解析进度
    task_count = 0
    print("开始处理问题：", query)
    print("正在获取解决方案计划...")
    
    # 设置请求参数
    url = f"{config.api_base}/chat/completions"
    headers = config.get_headers()
    payload = config.get_payload(query)
    
    # 设置请求参数
    url = f"{config.api_base}/chat/completions"
    headers = config.get_headers()
    payload = config.get_payload(query)
    
    # 流式处理
    try:
        with requests.post(url, headers=headers, json=payload, stream=True) as r:
            r.raise_for_status()  # 检查HTTP错误
            for chunk in r.iter_content(chunk_size=1024, decode_unicode=True):
                if not chunk:
                    continue
                    
                # 处理SSE格式
                for line in chunk.splitlines():
                    line = line.strip()
                    if not line or line == "data: [DONE]":
                        continue
                        
                    if line.startswith('data: '):
                        try:
                            data_obj = json.loads(line[6:])
                            content = data_obj["choices"][0]["delta"].get("content", "")
                            print(content, end="", flush=True)  # 实时输出
                            
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
                                router(tasks, config, query)
    
                        except json.JSONDecodeError:
                            pass  # 忽略解析错误，继续处理
                        except Exception as e:
                            print(f"\n处理响应时出错: {e}")
    except requests.RequestException as e:
        print(f"\n请求错误: {e}")
    except Exception as e:
        print(f"\n未知错误: {e}")
    
    print(f"\n计划生成完成，共解析 {task_count} 个任务")
    
    # 继续处理可能的剩余XML标签
    while process_xml_buffer():
        pass
    
    # 处理所有剩余任务直到全部完成
    print("\n\n开始执行所有任务...")
    while tasks and any(step_id not in completed_steps for step_id in tasks):
        if not router(tasks, config, query, stats_tracker):
            break
    
    # 关闭线程池
    executor.shutdown()
    
    # 停止性能跟踪
    stats_tracker.stop_tracking()
    
    return tasks, stats_tracker


# 执行主流程
if __name__ == "__main__":
    print("启动程序...")
    print(f"配置文件: {args.config}")
    print(f"使用小模型: {config.small_model}")
    print(f"使用大模型: {config.large_model}")
    print(f"难度阈值: {config.threshold}")
    print(f"工作线程数: {workers}")
    print(f"当前查询: {query}")
    
    # 运行并行执行流程
    tasks, stats_tracker = run_parallel_execution(query, config)
    
    # 结果处理在main函数内完成
    print("\n\n所有任务已完成！")
    
    # 打印结果
    print_results(tasks)
    
    # 获取最终结果
    final_result = wait_for_completion_and_get_final_result(tasks, query, config, stats_tracker)
    print("\n最终合并结果:")
    print(final_result)
    
    # 计算并打印性能指标
    performance_report = calculate_performance_metrics(stats_tracker)
    print("\n性能统计:")
    print(performance_report)
    
    # 可选：将最终结果保存到文件
    try:
        output_dir = "results"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(output_dir, f"result_{timestamp}.md")
        
        # 将性能报告添加到最终结果中
        final_result_with_stats = final_result + "\n\n" + performance_report
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(final_result_with_stats)
        print(f"结果已保存至: {output_file}")
    except Exception as e:
        print(f"保存结果时出错: {e}")