'''
包含性能跟踪和统计相关的代码
'''
import time

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
        report += f"## 总执行时间\n{elapsed_time:.3f} 秒\n\n"
        
        # 计算平均TTFT
        def calc_avg_ttft(ttft_list):
            return sum(ttft_list) / len(ttft_list) if ttft_list else 0
            
        small_ttft = self.ttft_metrics["small_model"]
        large_ttft = self.ttft_metrics["large_model"]
        all_ttft = self.ttft_metrics["total"]

        def calc_total_ttft(ttft_list):
            return sum(ttft_list) if ttft_list else 0
        
        report += f"## 去除ttft的总执行时间\n{elapsed_time - calc_total_ttft(all_ttft):.3f} 秒\n\n"
        
        # 首个令牌响应时间报告
        report += "## 首个令牌响应时间 (TTFT)\n\n"

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
