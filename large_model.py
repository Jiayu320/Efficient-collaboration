import requests
import json
import os
import time
import argparse
import yaml
from openai import OpenAI
from typing import Dict, Any
from reasoning import ModelConfig, load_config, parse_args, PerformanceTracker


def run_direct_execution(query, config):
    """使用单一大模型直接执行查询
    
    参数:
        query: 要解决的问题
        config: 模型配置对象
        
    返回:
        结果文本和性能统计跟踪器
    """
    # 创建性能统计跟踪器
    stats_tracker = PerformanceTracker()
    
    print("开始直接处理问题：", query)
    
    # 获取客户端
    client = config.get_client()
    
    # 使用大模型直接处理
    try:
        print("使用大模型处理中...")
        start_time = time.time()
        
        response = client.chat.completions.create(
            model=config.large_model,
            messages=[
                {"role": "user", "content": query}
            ]
        )
        
        result = response.choices[0].message.content
        
        # 更新token使用统计
        if hasattr(response, 'usage'):
            stats_tracker.update_token_usage(
                "large_model",
                response.usage.prompt_tokens,
                response.usage.completion_tokens
            )
        
        end_time = time.time()
        print(f"处理完成，耗时：{end_time - start_time:.2f}秒")
        
        return result, stats_tracker
        
    except Exception as e:
        print(f"处理出错: {e}")
        stats_tracker.stop_tracking()
        return f"错误: {str(e)}", stats_tracker


def format_comparison_report(direct_result, direct_stats, parallel_stats=None):
    """格式化对比报告
    
    参数:
        direct_result: 直接执行的结果
        direct_stats: 直接执行的性能统计
        parallel_stats: 并行执行的性能统计（可选）
        
    返回:
        对比报告文本
    """
    direct_stats.stop_tracking()
    direct_costs = direct_stats.calculate_cost()
    direct_time = direct_stats.get_elapsed_time()
    
    report = "# 大模型直接处理与并行处理对比报告\n\n"
    
    report += "## 直接使用大模型处理\n\n"
    report += f"### 执行时间\n{direct_time:.2f} 秒\n\n"
    
    report += "### Token 使用情况\n"
    report += f"- 输入 Tokens: {direct_stats.token_usage['large_model']['prompt_tokens']}\n"
    report += f"- 输出 Tokens: {direct_stats.token_usage['large_model']['completion_tokens']}\n"
    report += f"- 总 Tokens: {direct_stats.token_usage['large_model']['total_tokens']}\n\n"
    
    report += "### 成本估算\n"
    report += f"- 大模型成本: ${direct_costs['large_model']:.4f}\n\n"
    
    if parallel_stats:
        parallel_stats.stop_tracking()
        parallel_costs = parallel_stats.calculate_cost()
        parallel_time = parallel_stats.get_elapsed_time()
        
        report += "## 并行处理（小模型 + 大模型）\n\n"
        report += f"### 执行时间\n{parallel_time:.2f} 秒\n\n"
        
        report += "### Token 使用情况\n"
        report += "#### 小模型\n"
        report += f"- 输入 Tokens: {parallel_stats.token_usage['small_model']['prompt_tokens']}\n"
        report += f"- 输出 Tokens: {parallel_stats.token_usage['small_model']['completion_tokens']}\n"
        report += f"- 总 Tokens: {parallel_stats.token_usage['small_model']['total_tokens']}\n\n"
        
        report += "#### 大模型\n"
        report += f"- 输入 Tokens: {parallel_stats.token_usage['large_model']['prompt_tokens']}\n"
        report += f"- 输出 Tokens: {parallel_stats.token_usage['large_model']['completion_tokens']}\n"
        report += f"- 总 Tokens: {parallel_stats.token_usage['large_model']['total_tokens']}\n\n"
        
        report += "#### 总计\n"
        report += f"- 输入 Tokens: {parallel_stats.token_usage['total']['prompt_tokens']}\n"
        report += f"- 输出 Tokens: {parallel_stats.token_usage['total']['completion_tokens']}\n"
        report += f"- 总 Tokens: {parallel_stats.token_usage['total']['total_tokens']}\n\n"
        
        report += "### 成本估算\n"
        report += f"- 小模型成本: ${parallel_costs['small_model']:.4f}\n"
        report += f"- 大模型成本: ${parallel_costs['large_model']:.4f}\n"
        report += f"- 总成本: ${parallel_costs['total']:.4f}\n\n"
        
        # 计算效率对比
        time_ratio = direct_time / parallel_time if parallel_time > 0 else 0
        cost_ratio = direct_costs['large_model'] / parallel_costs['total'] if parallel_costs['total'] > 0 else 0
        
        report += "## 效率对比\n\n"
        report += f"- 时间比例 (直接/并行): {time_ratio:.2f}x\n"
        report += f"- 成本比例 (直接/并行): {cost_ratio:.2f}x\n"
        
        if time_ratio > 1:
            report += f"- 并行处理比直接处理快 **{time_ratio:.2f}倍**\n"
        elif time_ratio < 1:
            report += f"- 直接处理比并行处理快 **{1/time_ratio:.2f}倍**\n"
        
        if cost_ratio > 1:
            report += f"- 并行处理比直接处理节省 **{(1-1/cost_ratio)*100:.1f}%** 的成本\n"
        elif cost_ratio < 1:
            report += f"- 直接处理比并行处理节省 **{(1-cost_ratio)*100:.1f}%** 的成本\n"
        
    return report


def save_result(result, report, query):
    """保存结果到文件
    
    参数:
        result: 处理结果
        report: 性能报告
        query: 原始查询
    """
    try:
        output_dir = "comparison_results"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(output_dir, f"direct_result_{timestamp}.md")
        
        full_content = f"# 大模型直接处理结果\n\n"
        full_content += f"## 原始问题\n{query}\n\n"
        full_content += f"## 解决方案\n{result}\n\n"
        full_content += report
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(full_content)
        print(f"结果已保存至: {output_file}")
    except Exception as e:
        print(f"保存结果时出错: {e}")


def compare_with_parallel(query, config, parallel_stats):
    """与并行执行进行比较
    
    参数:
        query: 原始查询
        config: 模型配置
        parallel_stats: 并行执行的性能统计
    """
    # 直接使用大模型执行
    direct_result, direct_stats = run_direct_execution(query, config)
    
    # 生成对比报告
    comparison_report = format_comparison_report(direct_result, direct_stats, parallel_stats)
    
    # 保存结果和报告
    save_result(direct_result, comparison_report, query)
    
    # 打印报告
    print("\n对比报告:")
    print(comparison_report)
    
    return direct_result, direct_stats, comparison_report


# 独立执行模式
if __name__ == "__main__":
    print("启动直接对比程序...")
    
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
    
    print(f"配置文件: {args.config}")
    print(f"使用大模型: {config.large_model}")
    print(f"当前查询: {query}")
    
    # 直接使用大模型执行
    direct_result, direct_stats = run_direct_execution(query, config)
    
    # 生成简单报告(无并行对比)
    report = format_comparison_report(direct_result, direct_stats)
    
    # 保存结果和报告
    save_result(direct_result, report, query)
    
    # 打印报告
    print("\n性能报告:")
    print(report)