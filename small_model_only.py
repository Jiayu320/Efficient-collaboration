import requests
import json
import os
import time
import argparse
import yaml
from typing import Dict, Any
from openai import OpenAI


class ModelConfig:
    """模型配置类，用于管理API和模型设置"""
    
    def __init__(self, 
                 model="qwen/qwen3-14b:free", 
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
                "small_model": "qwen/qwen3-14b:free"
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
    parser = argparse.ArgumentParser(description='小模型单独求解系统')
    parser.add_argument('--config', type=str, default="config.yaml",
                      help='配置文件路径')
    parser.add_argument('--query', type=str,
                      help='要解决的问题')
    return parser.parse_args()


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
        
        # 成本估算 (美元/1K tokens) - 小模型通常是免费的，但为了对比可以设置一个很小的值
        self.cost_rates = {
            "prompt": 0.0,  # 免费模型
            "completion": 0.0  # 免费模型
        }
    
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


def solve_problem_with_small_model(query, config, stats_tracker):
    """使用小模型解决问题
    
    参数:
        query: 问题
        config: 模型配置
        stats_tracker: 性能统计跟踪器
        
    返回:
        解决方案
    """
    print(f"开始使用小模型 {config.model} 解决问题...\n")
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
    
    # 获取查询
    query = args.query if args.query else yaml_config["query"]
    
    # 构建模型配置
    model_config = ModelConfig(
        model=yaml_config["models"]["small_model"],
        api_key_path=yaml_config["api"]["key_path"],
        prompt_path=yaml_config["system"]["compare_prompt_path"],
        api_base=yaml_config["api"]["base_url"]
    )
    
    # 创建性能跟踪器
    stats_tracker = PerformanceTracker()
    
    print("启动小模型单独求解程序...")
    print(f"使用模型: {model_config.model}")
    print(f"当前查询: {query}")
    
    # 解决问题
    result = solve_problem_with_small_model(query, model_config, stats_tracker)
    
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
        output_file = os.path.join(output_dir, f"small_model_result_{timestamp}.md")
        model_info = f"# 小模型单独求解结果\n\n使用模型: {model_config.model}\n\n"
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(model_info + "## 问题\n\n" + query + "\n\n## 解决方案\n\n" + result + "\n\n" + performance_report)
        print(f"结果已保存至: {output_file}")
    except Exception as e:
        print(f"保存结果时出错: {e}")
