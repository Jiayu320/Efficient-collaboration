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
                 router_model=None,
                 threshold=2,
                 api_key_path="usage/openrouter",
                 prompt_path="prompt/generate_prompt.txt",
                 api_base="https://openrouter.ai/api/v1"):
        """
        初始化模型配置
        
        参数:
            small_model: 小模型的名称
            large_model: 大模型的名称
            router_model: 路由模型的名称，用于生成任务计划，如果为None则使用small_model
            threshold: 使用大模型的难度阈值
            api_key_path: API密钥文件路径
            prompt_path: 提示词文件路径
            api_base: API基础URL
        """
        self.small_model = small_model
        self.large_model = large_model
        self.router_model = router_model if router_model else small_model
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
                "router_model": "qwen/qwen-2.5-7b-instruct",
                "threshold": 2
            },
            "api": {
                "key_path": "usage/openrouter",
                "base_url": "https://openrouter.ai/api/v1"
            },
            "system": {
                "prompt_path": "prompt/generate_prompt.txt",
                "workers": 4,
                "enable_judge": False,
                "gold_answer": ""
            },
            "query": "What is the result of 1+1?"
        }

def parse_args():
    """解析命令行参数，可覆盖配置文件中的设置"""
    parser = argparse.ArgumentParser(description='并行任务处理系统')
    parser.add_argument('--config', type=str, default="config.yaml",
                      help='配置文件路径')
    return parser.parse_args()

# 解析命令行参数
args = parse_args()

# 加载配置文件
yaml_config = load_config(args.config)

# 构建最终配置（命令行参数优先）
small_model = yaml_config["models"]["small_model"]
large_model = yaml_config["models"]["large_model"]
router_model = yaml_config["models"].get("router_model", small_model)  # 如果未设置，默认使用小模型
threshold = yaml_config["models"]["threshold"]
api_key_path = yaml_config["api"]["key_path"]
api_base = yaml_config["api"]["base_url"]
prompt_path = yaml_config["system"]["prompt_path"]
workers = yaml_config["system"]["workers"]

# 获取判断相关配置
enable_judge = yaml_config["system"].get("enable_judge", False)
gold_answer = yaml_config["system"].get("gold_answer", "")

# 初始化模型配置
config = ModelConfig(
    small_model=small_model,
    large_model=large_model,
    router_model=router_model,
    threshold=threshold,
    api_key_path=api_key_path,
    prompt_path=prompt_path,
    api_base=api_base
)

# 设置查询
query = yaml_config["query"]

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

class PerformanceTracker:
    """性能跟踪器类，用于跟踪模型使用情况和成本"""
    
    def __init__(self):
        """初始化性能跟踪器"""
        self.start_time = time.time()
        self.end_time = None
        
        # 首个令牌响应时间统计
        self.ttft_metrics = {
            "small_model": [],
            "large_model": [],
            "total": []
        }
        
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
            },  # 小模型免费
            # $2.50/M input tokens $10/M output tokens
            "large_model": {
                "prompt": 0.0025,  # $2.50 per 1M input tokens
                "completion": 0.0100  # $10 per 1M output tokens
            }
        }
        '''
        self.cost_rates = {
            "small_model": {
                "prompt": 0.0025,
                "completion": 0.0100
            },
            # $2.50/M input tokens $10/M output tokens
            "large_model": {
                "prompt": 0.0025,  # $2.50 per 1M input tokens
                "completion": 0.0100  # $10 per 1M output tokens
            }
        }
        '''
    
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
        
    def update_ttft(self, model_type, ttft):
        """更新首个令牌响应时间 (Time to First Token)
        
        参数:
            model_type: 模型类型 ("small_model" 或 "large_model")
            ttft: 首个令牌响应时间（秒）
        """
        if ttft is not None:
            # 更新指定模型的统计
            self.ttft_metrics[model_type].append(ttft)
            # 更新总统计
            self.ttft_metrics["total"].append(ttft)
    
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
    
    def calculate_tokens_per_second(self):
        """计算每秒生成的token数量
        
        返回:
            每秒生成的token数量字典
        """
        elapsed_time = self.get_elapsed_time()
        if elapsed_time <= 0:
            return {
                "small_model": 0,
                "large_model": 0,
                "total": 0
            }
        
        small_tps = self.token_usage["small_model"]["completion_tokens"] / elapsed_time
        large_tps = self.token_usage["large_model"]["completion_tokens"] / elapsed_time
        total_tps = self.token_usage["total"]["completion_tokens"] / elapsed_time
        
        return {
            "small_model": small_tps,
            "large_model": large_tps,
            "total": total_tps
        }
    
    def format_performance_report(self):
        """格式化性能报告
        
        返回:
            性能报告文本
        """
        costs = self.calculate_cost()
        elapsed_time = self.get_elapsed_time()
        tokens_per_second = self.calculate_tokens_per_second()
        
        report = "# 性能统计报告\n\n"
        report += f"## 总执行时间\n{elapsed_time:.2f} 秒\n\n"
        
        # 首个令牌响应时间报告
        report += "## 首个令牌响应时间 (TTFT)\n\n"
        
        # 计算平均TTFT
        def calc_avg_ttft(ttft_list):
            return sum(ttft_list) / len(ttft_list) if ttft_list else 0
            
        small_ttft = self.ttft_metrics["small_model"]
        large_ttft = self.ttft_metrics["large_model"]
        all_ttft = self.ttft_metrics["total"]
        
        report += "### 小模型\n"
        if small_ttft:
            report += f"- 平均首个令牌响应时间: {calc_avg_ttft(small_ttft):.3f} 秒\n"
            report += f"- 最短响应时间: {min(small_ttft):.3f} 秒\n"
            report += f"- 最长响应时间: {max(small_ttft):.3f} 秒\n"
            report += f"- 响应次数: {len(small_ttft)}\n\n"
        else:
            report += "- 无数据\n\n"
            
        report += "### 大模型\n"
        if large_ttft:
            report += f"- 平均首个令牌响应时间: {calc_avg_ttft(large_ttft):.3f} 秒\n"
            report += f"- 最短响应时间: {min(large_ttft):.3f} 秒\n"
            report += f"- 最长响应时间: {max(large_ttft):.3f} 秒\n"
            report += f"- 响应次数: {len(large_ttft)}\n\n"
        else:
            report += "- 无数据\n\n"
            
        report += "### 总计\n"
        if all_ttft:
            report += f"- 平均首个令牌响应时间: {calc_avg_ttft(all_ttft):.3f} 秒\n"
            report += f"- 最短响应时间: {min(all_ttft):.3f} 秒\n"
            report += f"- 最长响应时间: {max(all_ttft):.3f} 秒\n"
            report += f"- 响应总次数: {len(all_ttft)}\n\n"
        else:
            report += "- 无数据\n\n"
        
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
        
        report += "## 生成速度\n\n"
        report += f"- 小模型每秒生成token数: {tokens_per_second['small_model']:.2f} tokens/s\n"
        report += f"- 大模型每秒生成token数: {tokens_per_second['large_model']:.2f} tokens/s\n"
        report += f"- 平均每秒生成token数: {tokens_per_second['total']:.2f} tokens/s\n\n"
        
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
    # 使用router_model而不是默认的small_model
    payload = config.get_payload(query, model_override=config.router_model)
    
    print(f"使用路由模型: {config.router_model} 生成解决方案计划")
    
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
    
    return tasks, stats_tracker

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

# 执行主流程
if __name__ == "__main__":
    print("启动程序...")
    print(f"配置文件: {args.config}")
    print(f"使用小模型: {config.small_model}")
    print(f"使用大模型: {config.large_model}")
    print(f"使用路由模型: {config.router_model}")
    print(f"难度阈值: {config.threshold}")
    print(f"工作线程数: {workers}")
    print(f"当前查询: {query}")

    try:
        difficulty = judge_question_difficulty(query, config)
        # 创建性能统计跟踪器（无论使用哪种方法都需要）
        stats_tracker = PerformanceTracker()
        
        if int(difficulty) < 2:
            print(f"问题难度 {difficulty} 低于阈值 2，使用小模型处理")

            # 直接调用小模型处理，传入性能跟踪器
            model_result = call_small_model_directly(query, config, stats_tracker)
            
            # 创建一个只包含一个任务的任务字典，以便生成一致的报告
            tasks = {
                "1": {
                    "Task": "直接使用小模型解答问题",
                    "Difficulty": difficulty,
                    "Token": "1000",
                    "Rely": "",
                    "Result": model_result
                }
            }
            
            # 构建最终结果
            final_result = "# 问题求解最终结果\n\n"
            final_result += f"## 原始问题\n{query}\n\n"
            final_result += "## 解决步骤\n\n"
            final_result += f"### 步骤 1: 直接使用小模型解答问题\n{model_result}\n\n"
            final_result += f"## 最终答案\n{model_result}\n"
            
            # 停止跟踪性能
            stats_tracker.stop_tracking()
            
            print("\n最终结果:")
            print(final_result)
        else:
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
    
        # 判断结果正确性
        correctness_report = ""
        if enable_judge and gold_answer:
            print("\n判断答案正确性...")
            is_correct, judge_result = judge_correct(query, gold_answer, final_result, config)
            correctness_status = "正确" if is_correct else "不正确"
            print(f"判断结果: 答案{correctness_status}")
            print(f"模型返回: {judge_result}")
            
            correctness_report = f"## 答案正确性判断\n\n标准答案: {gold_answer}\n\n判断结果: 答案{correctness_status}\n\n模型反馈: {judge_result}\n\n"
        elif enable_judge:
            print("\n判断答案正确性...")
            is_correct, judge_result = LLM_judge(query, final_result, config)
            correctness_status = "正确" if is_correct else "不正确"
            print(f"判断结果: 答案{correctness_status}")
            print(f"模型返回: {judge_result}")
            
            correctness_report = f"## 答案正确性判断\n\n判断结果: 答案{correctness_status}\n\n模型反馈: {judge_result}\n\n"

        # 计算并打印性能指标
        performance_report = calculate_performance_metrics(stats_tracker)
        print("\n性能统计:")
        print(performance_report)
        
        # 生成任务依赖关系报告
        dependency_report = generate_task_dependency_report(tasks)
        print("\n任务规划依赖关系:")
        print(dependency_report)
        
        # 可选：将最终结果保存到文件
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
        except Exception as e:
            print(f"保存结果时出错: {e}")
            

    except Exception as e:
        print(f"判断问题难度时出错: {e}")