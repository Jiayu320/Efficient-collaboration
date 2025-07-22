import requests
import json
import os
import time
import argparse
import yaml
from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, Any, List, Union
from openai import OpenAI


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


def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='大模型单独求解系统')
    parser.add_argument('--config', type=str, default="config.yaml",
                      help='配置文件路径')
    parser.add_argument('--query', type=str,
                      help='要解决的问题')
    parser.add_argument('--dataset', type=str,
                      help='数据集文件路径')
    parser.add_argument('--limit', type=int,
                      help='处理数据集的最大问题数')
    return parser.parse_args()


class LargeModelDatasetRunner:
    """大模型数据集处理器，用于批量处理数据集并生成统计报告"""
    
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
        
        print(f"开始使用大模型处理数据集，共 {len(self.dataset)} 个问题...")
        
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
            "execution_time": 0
        }
        
        start_time = time.time()
        
        try:
            # 创建性能统计跟踪器
            stats_tracker = PerformanceTracker()
            
            # 使用大模型处理问题
            model_solution = solve_problem_with_large_model(problem, self.config, stats_tracker)
            result["model_solution"] = model_solution
            
            # 判断结果正确性（使用LLM进行判断）
            is_correct, judge_result = self._judge_answer(problem, solution, model_solution)
            result["is_correct"] = is_correct
            result["judge_result"] = judge_result
            
            # 记录性能统计
            stats_tracker.stop_tracking()
            result["stats"] = stats_tracker
            
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
        client = self.config.get_client()
        
        try:
            response = client.chat.completions.create(
                model="openai/gpt-4o",
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
        
        # 统计正确率
        correct_count = sum(1 for r in self.results if r.get("is_correct", False))
        accuracy = correct_count / len(self.results) if self.results else 0
        
        # 统计平均执行时间
        avg_time = sum(r.get("execution_time", 0) for r in self.results) / len(self.results) if self.results else 0
        
        # 统计平均成本
        total_cost = sum(r.get("stats").calculate_cost() if r.get("stats") else 0 for r in self.results)
        avg_cost = total_cost / len(self.results) if self.results else 0
        
        # 生成报告
        report = "# 大模型数据集处理报告\n\n"
        report += f"模型型号: {self.config.model}\n\n"
        report += f"## 概述\n\n"
        report += f"- 数据集: {self.dataset_path}\n"
        report += f"- 问题总数: {len(self.results)}\n"
        report += f"- 正确数量: {correct_count}\n"
        report += f"- 准确率: {accuracy:.2%}\n"
        report += f"- 平均执行时间: {avg_time:.2f} 秒\n"
        report += f"- 平均成本: ${avg_cost:.4f}\n\n"
        
        # 生成详细结果表格
        report += f"## 详细结果\n\n"
        report += "| # | 问题 | 正确? | 执行时间(秒) | 成本($) |\n"
        report += "| --- | --- | --- | --- | --- |\n"
        
        for i, result in enumerate(self.results):
            is_correct = "✓" if result.get("is_correct", False) else "✗"
            problem = result.get("problem", "")
            # 截断问题以适合表格
            if len(problem) > 50:
                problem = problem[:47] + "..."
            problem = problem.replace("\n", " ")
            
            exec_time = result.get("execution_time", 0)
            cost = result.get("stats").calculate_cost() if result.get("stats") else 0
            
            report += f"| {i+1} | {problem} | {is_correct} | {exec_time:.2f} | {cost:.4f} |\n"
        
        return report
    
    def visualize_results(self, output_dir="dataset_reports"):
        """可视化数据集处理结果
        
        参数:
            output_dir: 输出目录
        """
        if not self.results:
            print("没有处理结果，无法生成可视化")
            return
        
        # 确保输出目录存在
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        
        # 准备数据
        data = []
        for result in self.results:
            item = {
                "问题": result.get("problem", "")[:50],
                "正确": result.get("is_correct", False),
                "执行时间": result.get("execution_time", 0),
                "成本": result.get("stats").calculate_cost() if result.get("stats") else 0
            }
            data.append(item)
        
        df = pd.DataFrame(data)
        
        # 准确率
        plt.figure(figsize=(10, 6))
        correct_count = sum(1 for r in self.results if r.get("is_correct", False))
        labels = ['正确', '错误']
        sizes = [correct_count, len(self.results) - correct_count]
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#4CAF50', '#F44336'])
        plt.title('问题解答准确率')
        plt.savefig(f"{output_dir}/accuracy_{timestamp}.png")
        
        # 执行时间分布
        plt.figure(figsize=(10, 6))
        plt.hist(df['执行时间'], bins=10, color='#2196F3')
        plt.xlabel('执行时间 (秒)')
        plt.ylabel('问题数量')
        plt.title('执行时间分布')
        plt.grid(True, alpha=0.3)
        plt.savefig(f"{output_dir}/time_distribution_{timestamp}.png")
        
        # 成本分布
        plt.figure(figsize=(10, 6))
        plt.hist(df['成本'], bins=10, color='#FF9800')
        plt.xlabel('成本 (美元)')
        plt.ylabel('问题数量')
        plt.title('成本分布')
        plt.grid(True, alpha=0.3)
        plt.savefig(f"{output_dir}/cost_distribution_{timestamp}.png")
        
        # 生成完整报告
        report = self.generate_report()
        with open(f"{output_dir}/dataset_report_{timestamp}.md", "w", encoding="utf-8") as f:
            f.write(report)
        
        print(f"可视化和报告已保存到 {output_dir} 目录")


class PerformanceTracker:
    """性能跟踪器类，用于跟踪模型使用情况和成本"""
    
    def __init__(self):
        """初始化性能跟踪器"""
        self.start_time = time.time()
        self.end_time = None
        
        # 首个令牌响应时间统计
        self.ttft_metrics = []
        
        # Token使用统计
        self.token_usage = {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0
        }
        
        # 成本估算 (美元/1K tokens) - 使用大模型费率
        # GPT-4o 费率:
        self.cost_rates = {
            "prompt": 0.0025,  # $2.50 per 1M input tokens
            "completion": 0.0100  # $10 per 1M output tokens
        }
        '''
        self.cost_rates = {
            "prompt": 0.003,  # $3.00 per 1M input tokens
            "completion": 0.015
        }
        
        # $0.272/M input tokens $0.272/M output tokens
        self.cost_rates = {
            "prompt": 0.000272,  # $0.272 per 1M input tokens
            "completion": 0.000272  # $0.272 per 1M output tokens
        }
        '''

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
        return (
            (self.token_usage["prompt_tokens"] / 1000) * self.cost_rates["prompt"] +
            (self.token_usage["completion_tokens"] / 1000) * self.cost_rates["completion"]
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
        else:
            report += "- 无数据\n\n"
        
        report += "## Token 使用情况\n\n"
        report += f"- 输入 Tokens: {self.token_usage['prompt_tokens']}\n"
        report += f"- 输出 Tokens: {self.token_usage['completion_tokens']}\n"
        report += f"- 总 Tokens: {self.token_usage['total_tokens']}\n\n"
        
        report += "## 生成速度\n\n"
        report += f"- 每秒生成token数: {tokens_per_second:.2f} tokens/s\n\n"
        
        report += "## 成本估算\n\n"
        report += f"- 总成本: ${cost:.4f}\n"
        
        return report


def solve_problem_with_large_model(query, config, stats_tracker):
    """使用大模型解决问题
    
    参数:
        query: 问题
        config: 模型配置
        stats_tracker: 性能统计跟踪器
        
    返回:
        解决方案
    """
    print(f"开始使用大模型 {config.model} 解决问题...\n")
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


if __name__ == "__main__":
    # 解析命令行参数
    args = parse_args()
    
    # 加载配置
    yaml_config = load_config(args.config)
    
    # 构建模型配置
    model_config = ModelConfig(
        model=yaml_config["models"]["large_model"],
        api_key_path=yaml_config["api"]["key_path"],
        prompt_path="prompt/direct_solve_prompt.txt",
        api_base=yaml_config["api"]["base_url"]
    )
    
    # 检查是否进行数据集处理
    enabled_dataset_processing = yaml_config.get("dataset", {}).get("enabled", False)
    dataset_path = args.dataset or yaml_config.get("dataset", {}).get("path", None)
    dataset_limit = args.limit or yaml_config.get("dataset", {}).get("limit", None)
    
    if enabled_dataset_processing:
        print("启动大模型数据集处理程序...")
        print(f"使用模型: {model_config.model}")
        print(f"数据集路径: {dataset_path}")
        if dataset_limit:
            print(f"处理问题数量限制: {dataset_limit}")
        
        # 创建数据集运行器
        dataset_runner = LargeModelDatasetRunner(model_config, dataset_path, limit=dataset_limit)
        
        # 处理数据集
        dataset_runner.process_dataset()
        
        # 生成报告和可视化
        report = dataset_runner.generate_report()
        print("\n数据集处理报告:")
        print(report)
        
        # 保存报告和生成可视化
        try:
            output_dir = "dataset_reports"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            # 保存报告到文件
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            output_file = os.path.join(output_dir, f"large_model_dataset_result_{timestamp}.md")
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(report)
            
            # 生成可视化
            # dataset_runner.visualize_results(output_dir)
            
            print(f"数据集处理完成，报告已保存到 {output_file}")
        except Exception as e:
            print(f"保存报告时出错: {e}")
    else:
        # 获取查询
        query = args.query if args.query else yaml_config["query"]
        
        # 创建性能跟踪器
        stats_tracker = PerformanceTracker()
        
        print("启动大模型单独求解程序...")
        print(f"使用模型: {model_config.model}")
        print(f"当前查询: {query}")
        
        # 解决问题
        result = solve_problem_with_large_model(query, model_config, stats_tracker)
        
        # 停止性能跟踪
        stats_tracker.stop_tracking()
        
        # 生成性能报告
        performance_report = stats_tracker.format_performance_report()
        print("\n性能统计:")
        print(performance_report)
        
        # 保存结果到文件
        try:
            output_dir = "comparison_results"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            output_file = os.path.join(output_dir, f"large_model_result_{timestamp}.md")
            model_info = f"# 大模型单独求解结果\n\n使用模型: {model_config.model}\n\n"
            
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(model_info + "## 问题\n\n" + query + "\n\n## 解决方案\n\n" + result + "\n\n" + performance_report)
            print(f"结果已保存至: {output_file}")
        except Exception as e:
            print(f"保存结果时出错: {e}")
