import requests
import json
import os
import time
import argparse
import yaml
import pathlib
from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, Any, List, Union
from openai import OpenAI

# 导入理论性能计算模块
from output_performance import get_model_performance, calculate_theoretical_time


class ModelConfig:
    """模型配置类，用于管理API和模型设置"""
    
    def __init__(self, 
                 model="qwen/qwen3-235b-a22b", 
                 api_key_path="usage/openrouter",
                 prompt_path="prompt/direct_solve_prompt.txt",
                 api_base="https://openrouter.ai/api/v1"):
        """
        初始化模型配置
        
        参数:
            model: 要使用的模型名称
            api_key_path: API密钥文件路径
            prompt_path: 提示词文件路径
            api_base: API基础URL
        """
        self.model = model
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
    
    def get_payload(self, query):
        """获取API请求载荷"""
        return {
            "model": self.model,
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
                "large_model": "qwen/qwen3-235b-a22b"
            },
            "api": {
                "key_path": "usage/openrouter",
                "base_url": "https://openrouter.ai/api/v1"
            },
            "system": {
                "prompt_path": "prompt/direct_solve_prompt.txt"
            },
            "query": "What is the result of 1+1?"
        }


def get_api_key(file_path="together_ai"):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            api_key = f.read().strip()
    else:
        raise FileNotFoundError(f"Credentials file '{file_path}' not found.")
    return api_key


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='单模型求解系统')
    parser.add_argument('--config', type=str, default="config.yaml",
                      help='配置文件路径')
    parser.add_argument('--query', type=str,
                      help='要解决的问题')
    parser.add_argument('--dataset', type=str,
                      help='数据集文件路径')
    parser.add_argument('--limit', type=int,
                      help='处理数据集的最大问题数')
    parser.add_argument('--model', type=str,
                      help='指定要使用的模型名称')
    return parser.parse_args()


def build_output_path(model_name):
    """构建输出路径
    
    参数:
        model_name: 模型名称
    
    返回:
        输出目录路径
    """
    # 清理模型名称以用于文件路径
    def clean_name(name):
        if name is None:
            return "unknown"
        # 提取模型名称的核心部分
        if "/" in name:
            name = name.split("/")[-1]
        # 移除可能导致路径问题的字符
        return ''.join(c for c in name if c.isalnum() or c in '_-.')
    
    # 构建基本路径
    base_path = os.path.join("data_reports", "single_model_results")
    
    # 添加模型名称子目录
    model_dir = clean_name(model_name)
    full_path = os.path.join(base_path, model_dir)
    
    # 确保目录存在
    os.makedirs(full_path, exist_ok=True)
    
    return full_path


class SingleModelDatasetRunner:
    """单模型数据集处理器，用于批量处理数据集并生成统计报告"""
    
    def __init__(self, config, dataset_path, limit=None):
        """初始化数据集处理器
        
        参数:
            config: 模型配置对象
            dataset_path: 数据集文件路径
            limit: 处理的最大问题数量，None表示处理所有问题
        """
        self.config = config
        self.dataset_path = dataset_path
        self.limit = limit
        self.results = []
        
        # 加载数据集
        self.dataset = self._load_dataset()
        
    def _load_dataset(self):
        """加载数据集
        
        返回:
            数据集列表
        """
        try:
            with open(self.dataset_path, 'r', encoding='utf-8') as f:
                dataset = json.load(f)
            
            # 如果设置了限制，则只取前N个问题
            if self.limit is not None:
                dataset = dataset[:self.limit]
            
            return dataset
        except Exception as e:
            print(f"加载数据集时出错: {e}")
            return []
    
    def process_dataset(self):
        """处理整个数据集
        
        返回:
            处理结果列表
        """
        if not self.dataset:
            print("数据集为空，无法处理")
            return []
        
        print(f"开始使用模型 {self.config.model} 处理数据集，共 {len(self.dataset)} 个问题...")
        
        # 使用tqdm显示进度
        for i, problem_data in enumerate(tqdm(self.dataset, desc="处理数据集")):
            problem = problem_data.get("problem", "")
            solution = problem_data.get("solution", "")
            
            # 每个问题的性能统计
            result = self.process_single_problem(problem, solution)
            self.results.append(result)
            
            # 打印当前进度
            print(f"完成进度: {i+1}/{len(self.dataset)}")
            
        return self.results
    
    def process_single_problem(self, problem, solution):
        """处理单个问题
        
        参数:
            problem: 问题文本
            solution: 标准答案
            
        返回:
            处理结果字典
        """
        print(f"\n处理问题: {problem[:100]}...")
        
        # 初始化结果字典
        result = {
            "problem": problem,
            "gold_solution": solution,
            "model_solution": "",
            "is_correct": False,
            "judge_result": "",
            "stats": None,
            "execution_time": 0,
            "theoretical_time": None  # 添加理论时间字段
        }
        
        start_time = time.time()
        
        try:
            # 创建性能统计跟踪器
            stats_tracker = PerformanceTracker(self.config.model)
            
            # 使用模型处理问题
            model_solution = solve_problem_with_model(problem, self.config, stats_tracker)
            result["model_solution"] = model_solution
            
            # 判断结果正确性（使用LLM进行判断）
            is_correct, judge_result = self._judge_answer(problem, solution, model_solution)
            result["is_correct"] = is_correct
            result["judge_result"] = judge_result
            
            # 记录性能统计
            stats_tracker.stop_tracking()
            result["stats"] = stats_tracker
            
            # 计算理论时间
            completion_tokens = stats_tracker.token_usage["completion_tokens"]
            theoretical_time = calculate_theoretical_time(self.config.model, completion_tokens)
            result["theoretical_time"] = theoretical_time
            
        except Exception as e:
            print(f"处理问题时出错: {e}")
            result["error"] = str(e)
        
        # 计算总执行时间
        result["execution_time"] = time.time() - start_time
        
        return result
    
    def _judge_answer(self, problem, gold_solution, model_solution):
        """判断答案是否正确
        
        参数:
            problem: 问题文本
            gold_solution: 标准答案
            model_solution: 模型生成的答案
            
        返回:
            (是否正确的布尔值, 判断结果文本)
        """
        prompt = f"""Here is a math problem with a standard answer and a student's solution. Please help me determine if the student's solution is correct. If the numerical value are same, then it is correct.
                               
                Problem: {problem}

                Standard answer: {gold_solution}

                Answer: {model_solution}

                If the student's answer is correct, just output True; otherwise, just output False.
                No explanation is required.
        """
        
        # 使用客户端调用API
        client = OpenAI(
            base_url="https://api.bianxie.ai/v1",
            api_key=get_api_key("usage/bianxie"),
            )
        try:
            response = client.chat.completions.create(
                # model="openai/gpt-4o",
                model="gpt-4o", # 使用bianxie api
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,  # 低温度以获得更确定的回答
                max_tokens=10      # 只需要简短回答
            )
            judge_result = response.choices[0].message.content.strip().lower()
            is_correct = "true" in judge_result
            
            return is_correct, judge_result
        except Exception as e:
            print(f"判断答案时出错: {e}")
            return False, f"错误: {str(e)}"
    
    def generate_report(self):
        """生成数据集处理报告
        
        返回:
            处理报告文本
        """
        if not self.results:
            return "没有处理结果，无法生成报告"
        
        # 获取模型性能指标
        model_performance = get_model_performance(self.config.model)
        
        # 统计正确率
        correct_count = sum(1 for r in self.results if r.get("is_correct", False))
        accuracy = correct_count / len(self.results) if self.results else 0
        
        # 统计平均执行时间
        avg_time = sum(r.get("execution_time", 0) for r in self.results) / len(self.results) if self.results else 0
        
        # 统计平均理论时间
        theoretical_times = [r.get("theoretical_time", {}).get("total_time", 0) for r in self.results if r.get("theoretical_time")]
        avg_theoretical_time = sum(theoretical_times) / len(theoretical_times) if theoretical_times else 0
        
        # 统计平均成本
        total_cost = sum(r.get("stats").calculate_cost() if r.get("stats") else 0 for r in self.results)
        avg_cost = total_cost / len(self.results) if self.results else 0
        
        # 计算实际时间与理论时间的比率
        time_ratio = avg_time / avg_theoretical_time if avg_theoretical_time > 0 else "N/A"
        if isinstance(time_ratio, float):
            time_ratio = f"{time_ratio:.2f}x"
        
        # 生成报告
        report = "# 单模型数据集处理报告\n\n"
        report += f"## 模型信息\n\n"
        report += f"- 模型: {self.config.model}\n"
        report += f"- 延迟 (TTFT): {model_performance['latency']:.3f} 秒\n"
        report += f"- 吞吐量: {model_performance['throughput']:.2f} tokens/s\n\n"
        
        report += f"## 概述\n\n"
        report += f"- 数据集: {self.dataset_path}\n"
        report += f"- 问题总数: {len(self.results)}\n"
        report += f"- 正确数量: {correct_count}\n"
        report += f"- 准确率: {accuracy:.2%}\n"
        report += f"- 平均执行时间: {avg_time:.2f} 秒\n"
        report += f"- 平均理论时间: {avg_theoretical_time:.2f} 秒\n"
        report += f"- 实际/理论时间比率: {time_ratio}\n"
        report += f"- 平均成本: ${avg_cost:.4f}\n\n"
        
        # 添加TTFT和生成速度统计
        ttft_metrics = []
        tokens_per_second = []
        for result in self.results:
            if result.get("stats") and result.get("stats").ttft_metrics:
                ttft_list = result.get("stats").ttft_metrics
                if ttft_list:
                    avg_ttft = sum(ttft_list) / len(ttft_list)
                    ttft_metrics.append(avg_ttft)
            
            # 计算每秒生成token数
            if result.get("stats"):
                tokens = result.get("stats").token_usage.get("completion_tokens", 0)
                exec_time = result.get("execution_time", 0)
                if exec_time > 0:
                    tokens_per_second.append(tokens / exec_time)
        
        avg_ttft = sum(ttft_metrics) / len(ttft_metrics) if ttft_metrics else 0
        avg_tokens_per_second = sum(tokens_per_second) / len(tokens_per_second) if tokens_per_second else 0
        
        report += f"## 性能指标\n\n"
        report += f"- 平均首个令牌响应时间 (TTFT): {avg_ttft:.3f} 秒\n"
        report += f"- 平均每秒生成token数: {avg_tokens_per_second:.2f} tokens/s\n"
        report += f"- 理论每秒生成token数: {model_performance['throughput']:.2f} tokens/s\n"
        report += f"- 实际/理论吞吐量比率: {(avg_tokens_per_second/model_performance['throughput']):.2f}x\n\n"
        
        # 生成详细结果表格
        report += f"## 详细结果\n\n"
        report += "| # | 问题 | 正确? | 执行时间(秒) | 理论时间(秒) | 成本($) |\n"
        report += "| --- | --- | --- | --- | --- | --- |\n"
        
        for i, result in enumerate(self.results):
            is_correct = "✓" if result.get("is_correct", False) else "✗"
            problem = result.get("problem", "")
            # 截断问题以适合表格
            if len(problem) > 50:
                problem = problem[:47] + "..."
            problem = problem.replace("\n", " ")
            
            exec_time = result.get("execution_time", 0)
            theoretical_time = result.get("theoretical_time", {}).get("total_time", 0)
            cost = result.get("stats").calculate_cost() if result.get("stats") else 0
            
            report += f"| {i+1} | {problem} | {is_correct} | {exec_time:.2f} | {theoretical_time:.2f} | {cost:.4f} |\n"
        
        return report
    
    def save_results(self, timestamp=None):
        """保存处理结果到文件
        
        参数:
            timestamp: 时间戳，如果为None则自动生成
            
        返回:
            报告文件路径
        """
        if timestamp is None:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            
        # 构建输出目录
        output_dir = build_output_path(self.config.model)
        run_dir = os.path.join(output_dir, timestamp)
        os.makedirs(run_dir, exist_ok=True)
        
        # 保存报告
        report = self.generate_report()
        report_file = os.path.join(run_dir, "report.md")
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"报告已保存至: {report_file}")
        
        # 保存详细结果为JSON
        results_json = []
        for result in self.results:
            # 创建可序列化的结果对象
            serializable_result = {
                "problem": result.get("problem", ""),
                "gold_solution": result.get("gold_solution", ""),
                "model_solution": result.get("model_solution", ""),
                "is_correct": result.get("is_correct", False),
                "judge_result": result.get("judge_result", ""),
                "execution_time": result.get("execution_time", 0),
                "theoretical_time": result.get("theoretical_time", {}),
                "token_usage": result.get("stats").token_usage if result.get("stats") else {},
                "cost": result.get("stats").calculate_cost() if result.get("stats") else 0
            }
            results_json.append(serializable_result)
            
        json_file = os.path.join(run_dir, "results.json")
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(results_json, f, indent=2, ensure_ascii=False)
        print(f"详细结果已保存至: {json_file}")
        
        return report_file


class PerformanceTracker:
    """性能跟踪器类，用于跟踪模型使用情况和成本"""
    
    def __init__(self, model_name="gpt-4o"):
        """初始化性能跟踪器
        
        参数:
            model_name: 模型名称，用于获取价格费率
        """
        from api_pricing import get_model_pricing
        
        self.start_time = time.time()
        self.end_time = None
        self.model_name = model_name
        
        # 首个令牌响应时间统计
        self.ttft_metrics = []
        
        # Token使用统计
        self.token_usage = {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0
        }
        
        # 成本估算 (美元/1M tokens) - 从API价格管理模块获取
        self.cost_rates = get_model_pricing(model_name)

    def update_token_usage(self, prompt_tokens, completion_tokens):
        """更新token使用情况
        
        参数:
            prompt_tokens: 输入token数量
            completion_tokens: 输出token数量
        """
        self.token_usage["prompt_tokens"] += prompt_tokens
        self.token_usage["completion_tokens"] += completion_tokens
        self.token_usage["total_tokens"] += prompt_tokens + completion_tokens
        
    def update_ttft(self, ttft):
        """更新首个令牌响应时间 (Time to First Token)
        
        参数:
            ttft: 首个令牌响应时间（秒）
        """
        if ttft is not None:
            self.ttft_metrics.append(ttft)
    
    def stop_tracking(self):
        """停止性能跟踪"""
        self.end_time = time.time()
    
    def calculate_cost(self):
        """计算总成本
        
        返回:
            总成本（美元）
        """
        # API价格通常以美元/百万tokens为单位，因此需要除以1,000,000
        return (
            (self.token_usage["prompt_tokens"] / 1000000) * self.cost_rates["prompt"] +
            (self.token_usage["completion_tokens"] / 1000000) * self.cost_rates["completion"]
        )
    
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
            每秒生成的token数量
        """
        elapsed_time = self.get_elapsed_time()
        if elapsed_time <= 0:
            return 0
        
        return self.token_usage["completion_tokens"] / elapsed_time
    
    def format_performance_report(self):
        """格式化性能报告
        
        返回:
            性能报告文本
        """
        cost = self.calculate_cost()
        elapsed_time = self.get_elapsed_time()
        tokens_per_second = self.calculate_tokens_per_second()
        
        report = "# 性能统计报告\n\n"
        report += f"## 总执行时间\n{elapsed_time:.2f} 秒\n\n"
        
        # 首个令牌响应时间报告
        report += "## 首个令牌响应时间 (TTFT)\n\n"
        
        # 计算平均TTFT
        def calc_avg_ttft(ttft_list):
            return sum(ttft_list) / len(ttft_list) if ttft_list else 0
        
        if self.ttft_metrics:
            report += f"- 平均首个令牌响应时间: {calc_avg_ttft(self.ttft_metrics):.3f} 秒\n"
            report += f"- 最短响应时间: {min(self.ttft_metrics):.3f} 秒\n"
            report += f"- 最长响应时间: {max(self.ttft_metrics):.3f} 秒\n"
            report += f"- 响应次数: {len(self.ttft_metrics)}\n\n"
            report += f"## 去除ttft的总执行时间\n{elapsed_time - calc_avg_ttft(self.ttft_metrics):.3f} 秒\n\n"
        else:
            report += "- 无数据\n\n"
        
        # 理论性能
        theoretical_time = calculate_theoretical_time(self.model_name, self.token_usage["completion_tokens"])
        report += "## 理论性能\n\n"
        report += f"- 延迟 (TTFT): {theoretical_time['latency']:.3f} 秒\n"
        report += f"- 生成时间: {theoretical_time['generation_time']:.3f} 秒\n"
        report += f"- 总理论时间: {theoretical_time['total_time']:.3f} 秒\n"
        report += f"- 实际/理论时间比率: {elapsed_time / theoretical_time['total_time']:.2f}x\n\n"
        
        report += "## Token 使用情况\n\n"
        report += f"- 输入 Tokens: {self.token_usage['prompt_tokens']}\n"
        report += f"- 输出 Tokens: {self.token_usage['completion_tokens']}\n"
        report += f"- 总 Tokens: {self.token_usage['total_tokens']}\n\n"
        
        report += "## 生成速度\n\n"
        report += f"- 每秒生成token数: {tokens_per_second:.2f} tokens/s\n\n"
        
        report += "## 成本估算\n\n"
        report += f"- 总成本: ${cost:.4f}\n"
        
        return report


def solve_problem_with_model(query, config, stats_tracker):
    """使用模型解决问题
    
    参数:
        query: 问题
        config: 模型配置
        stats_tracker: 性能统计跟踪器
        
    返回:
        解决方案
    """
    print(f"开始使用模型 {config.model} 解决问题...\n")
    print(f"问题: {query}\n")
    
    # 获取客户端
    client = config.get_client()
    
    # 开始计时
    start_time = time.time()
    first_token_time = None
    
    try:
        # 使用流式API
        response_stream = client.chat.completions.create(
            model=config.model,
            messages=[
                {"role": "system", "content": config.system_prompt},
                {"role": "user", "content": query}
            ],
            stream=True
        )
        
        # 收集完整响应
        collected_content = ""
        for chunk in response_stream:
            if first_token_time is None:
                first_token_time = time.time()
                
            # 从每个块中提取内容并累加
            if hasattr(chunk.choices[0], 'delta') and hasattr(chunk.choices[0].delta, 'content'):
                content = chunk.choices[0].delta.content
                if content:
                    collected_content += content
                    print(content, end="", flush=True)
        
        print("\n\n")
        
        # 计算首个令牌响应时间
        ttft = first_token_time - start_time if first_token_time else None
        
        # 估算token数量
        prompt_words = len(query.split())
        prompt_chinese_chars = sum(1 for c in query if '\u4e00' <= c <= '\u9fff')
        content_words = len(collected_content.split())
        content_chinese_chars = sum(1 for c in collected_content if '\u4e00' <= c <= '\u9fff')
        
        estimated_prompt_tokens = int((prompt_words * 1.3) + (prompt_chinese_chars * 1.5))
        estimated_completion_tokens = int((content_words * 1.3) + (content_chinese_chars * 1.5))
        
        if estimated_prompt_tokens < 1:
            estimated_prompt_tokens = 1
        if estimated_completion_tokens < 1:
            estimated_completion_tokens = 1
        
        # 更新性能统计
        stats_tracker.update_token_usage(estimated_prompt_tokens, estimated_completion_tokens)
        if ttft is not None:
            stats_tracker.update_ttft(ttft)
        
        # 计算总时间
        total_time = time.time() - start_time
        print(f"问题解决完成，总用时: {total_time:.2f} 秒")
        if ttft:
            print(f"首个令牌响应时间: {ttft:.3f} 秒")
        
        return collected_content
        
    except Exception as e:
        print(f"API调用失败: {e}")
        return f"错误: {str(e)}"


def save_single_result(query, result, performance_report, theoretical_time, model_config):
    """保存单个问题的处理结果
    
    参数:
        query: 问题
        result: 解决方案
        performance_report: 性能报告
        theoretical_time: 理论时间计算结果
        model_config: 模型配置
        
    返回:
        输出文件路径
    """
    try:
        # 创建输出目录
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        output_dir = build_output_path(model_config.model)
        run_dir = os.path.join(output_dir, timestamp)
        os.makedirs(run_dir, exist_ok=True)
        
        # 构建报告内容
        model_info = f"# 单模型求解结果\n\n使用模型: {model_config.model}\n\n"
        
        # 理论性能部分
        theory_section = "## 理论性能\n\n"
        theory_section += f"- 延迟 (TTFT): {theoretical_time['latency']:.3f} 秒\n"
        theory_section += f"- 生成时间: {theoretical_time['generation_time']:.3f} 秒\n"
        theory_section += f"- 总理论时间: {theoretical_time['total_time']:.3f} 秒\n\n"
        
        # 写入文件
        output_file = os.path.join(run_dir, "result.md")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(model_info + "## 问题\n\n" + query + "\n\n## 解决方案\n\n" + result + "\n\n" + theory_section + performance_report)
        
        print(f"结果已保存至: {output_file}")
        return output_file
    except Exception as e:
        print(f"保存结果时出错: {e}")
        return None


if __name__ == "__main__":
    # 解析命令行参数
    args = parse_args()
    
    # 加载配置
    yaml_config = load_config(args.config)
    
    # 确定使用的模型
    model_name = args.model
    if not model_name:
        model_name = yaml_config["models"].get("large_model", "qwen/qwen3-235b-a22b")
    
    # 确定API配置
    api_key_path = yaml_config["api"]["large_key_path"]
    api_base = yaml_config["api"]["large_api_base_url"]
    
    # 构建模型配置
    model_config = ModelConfig(
        model=model_name,
        api_key_path=api_key_path,
        prompt_path="prompt/direct_solve_prompt.txt",
        api_base=api_base
    )
    
    print(f"使用模型: {model_config.model}")
    print(f"API基础URL: {model_config.api_base}")
    
    # 检查是否进行数据集处理
    enabled_dataset_processing = yaml_config.get("dataset", {}).get("enabled", False)
    dataset_path = args.dataset or yaml_config.get("dataset", {}).get("path", None)
    dataset_limit = args.limit or yaml_config.get("dataset", {}).get("limit", None)
    
    if enabled_dataset_processing and dataset_path:
        print("启动单模型数据集处理程序...")
        print(f"数据集路径: {dataset_path}")
        if dataset_limit:
            print(f"处理问题数量限制: {dataset_limit}")
        
        # 创建数据集运行器
        dataset_runner = SingleModelDatasetRunner(model_config, dataset_path, limit=dataset_limit)
        
        # 处理数据集
        dataset_runner.process_dataset()
        
        # 保存结果并生成报告
        report_file = dataset_runner.save_results()
        print(f"数据集处理完成，报告已保存到 {report_file}")
    else:
        # 单个问题处理模式
        # 获取查询
        query = args.query if args.query else yaml_config["query"]
        print("启动单模型单独求解程序...")
        print(f"当前查询: {query}")
        
        # 创建性能跟踪器
        stats_tracker = PerformanceTracker(model_config.model)
        
        # 解决问题
        result = solve_problem_with_model(query, model_config, stats_tracker)
        
        # 停止性能跟踪
        stats_tracker.stop_tracking()
        
        # 计算理论时间
        theoretical_time = calculate_theoretical_time(
            model_config.model, 
            stats_tracker.token_usage["completion_tokens"]
        )
        
        # 生成性能报告
        performance_report = stats_tracker.format_performance_report()
        print("\n性能统计:")
        print(performance_report)
        
        # 保存结果到文件
        output_file = save_single_result(query, result, performance_report, theoretical_time, model_config)
        print(f"执行完成")

'''
单个问题：
python single_model_only.py --query "你的问题" --model "gpt-4o"
数据集处理：
python single_model_only.py --dataset "dataset/your_dataset.json" --limit 5 --model "claude-3-5-sonnet"
从配置文件处理：
python single_model_only.py --config "config.yaml"
'''