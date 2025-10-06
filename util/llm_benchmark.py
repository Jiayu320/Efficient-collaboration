import threading
import time
import argparse
import statistics
from openai import OpenAI
from typing import List, Dict, Any

# --- 配置区 ---

# 默认测试的提示语列表
DEFAULT_PROMPTS = [
    "请介绍一下北京的历史。",
    "写一个关于旅行的短故事。",
    "解释什么是黑洞。",
    "如何用 Python 编写一个简单的 web 服务器？",
    "给我五个关于健康生活的建议。",
]

# 默认测试的模型配置 (模型名称 -> API 地址)
# 您可以为不同的模型指定不同的 URL
DEFAULT_MODEL_CONFIGS = {
    "saves/Qwen3-1.7B-Instruct/full/sft": "http://127.0.0.1:8000/v1",
    "saves/Qwen3-4B-Thinking/full/ep5": "http://127.0.0.1:8001/v1", # 示例：不同的端口
}


# --- 脚本核心代码 ---

def test_model_performance(model_name: str, base_url: str, prompt: str, extra_body: dict) -> Dict[str, Any]:
    """
    对单个模型和提示进行流式调用，并测量性能指标。

    Args:
        model_name (str): 要测试的模型名称。
        base_url (str): 该模型对应的 API 地址。
        prompt (str): 发送给模型的提示语。
        extra_body (dict): 传递给 API 的额外参数。

    Returns:
        dict: 包含性能指标的字典。
    """
    metrics = {
        "success": False,
        "error": None,
        "ttft": 0.0,
        "throughput": 0.0,
        "output_tokens": 0,
        "total_duration": 0.0,
    }

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]

    try:
        # 在函数内部为每个请求创建客户端实例，以支持不同的 base_url
        client = OpenAI(api_key="0", base_url=base_url)
        request_start_time = time.perf_counter()
        
        stream = client.chat.completions.create(
            model=model_name,
            messages=messages,
            stream=True,
            temperature=0.6,
            extra_body=extra_body,
        )

        first_token_time = None
        output_tokens = 0
        
        for chunk in stream:
            # 仅在接收到有效内容时处理
            if chunk.choices[0].delta and chunk.choices[0].delta.content:
                if first_token_time is None:
                    first_token_time = time.perf_counter()
                # 简单地将每个有内容的 chunk 计为一个 token
                output_tokens += 1
        
        request_end_time = time.perf_counter()

        # 如果没有收到任何 token，则标记为失败
        if first_token_time is None:
            metrics["error"] = "No content generated from the model."
            return metrics

        # --- 计算指标 ---
        # 首字时间 (Time To First Token)
        ttft = first_token_time - request_start_time
        
        # 生成过程耗时 (从收到第一个 token 到最后一个 token)
        generation_duration = request_end_time - first_token_time
        
        # 吞吐量 (Tokens per Second)
        # 避免除以零错误
        throughput = output_tokens / generation_duration if generation_duration > 0 else 0
        
        # --- 更新结果 ---
        metrics.update({
            "success": True,
            "ttft": ttft,
            "throughput": throughput,
            "output_tokens": output_tokens,
            "total_duration": request_end_time - request_start_time,
        })

    except Exception as e:
        metrics["error"] = str(e)

    return metrics

def print_summary(title: str, values: List[float]):
    """打印一组数据的统计摘要。"""
    if not values:
        print(f"  {title}: N/A (No successful runs)")
        return
    
    avg = statistics.mean(values)
    stdev = statistics.stdev(values) if len(values) > 1 else 0
    mini = min(values)
    maxi = max(values)
    
    print(f"  {title}:")
    print(f"    - 平均值: {avg:.4f}")
    print(f"    - 标准差: {stdev:.4f}")
    print(f"    - 最小值: {mini:.4f}")
    print(f"    - 最大值: {maxi:.4f}")

def main():
    """主函数，用于解析参数和编排测试。"""
    parser = argparse.ArgumentParser(description="本地大语言模型性能测试工具")
    parser.add_argument(
        "-m", "--models", nargs="+", default=None,
        help="要测试的模型和URL对，格式为 'model_name@http://base_url'。如果不提供，将使用脚本中的默认配置。"
    )
    parser.add_argument(
        "-c", "--concurrency", type=int, default=5,
        help="每个模型的并发请求数。默认为: 5"
    )
    parser.add_argument(
        "--prompts", nargs="+", default=DEFAULT_PROMPTS,
        help="用于测试的提示语列表。"
    )
    parser.add_argument(
        "--enable-thinking", action="store_true",
        help="如果指定，将 'enable_thinking: True' 添加到请求中。"
    )

    args = parser.parse_args()
    
    model_configs = {}
    if args.models:
        for model_arg in args.models:
            parts = model_arg.split('@')
            if len(parts) != 2 or not parts[1].startswith(('http://', 'https://')):
                print(f"错误：模型参数格式不正确 '{model_arg}'。请使用 'model_name@http://base_url' 格式。")
                return
            model_configs[parts[0]] = parts[1]
    else:
        model_configs = DEFAULT_MODEL_CONFIGS


    extra_body = {"enable_thinking": True} if args.enable_thinking else {}

    print("--- 开始性能测试 ---")
    print(f"并发数: {args.concurrency}")
    if extra_body:
        print(f"额外参数: {extra_body}")
    print("-" * 25)

    for model, base_url in model_configs.items():
        print(f"\n[测试模型]: {model}")
        print(f"  - API URL: {base_url}")
        
        results = []
        threads = []
        
        # 使用一个线程安全的列表来收集结果
        def worker(prompt):
            result = test_model_performance(model, base_url, prompt, extra_body)
            results.append(result)

        overall_start_time = time.perf_counter()

        for i in range(args.concurrency):
            # 循环使用提示语，以防并发数大于提示语数量
            prompt = args.prompts[i % len(args.prompts)]
            thread = threading.Thread(target=worker, args=(prompt,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()

        overall_end_time = time.perf_counter()
        
        # --- 结果分析与展示 ---
        successful_runs = [r for r in results if r["success"]]
        failed_runs = len(results) - len(successful_runs)

        print(f"\n测试完成。总耗时: {overall_end_time - overall_start_time:.2f} 秒")
        print(f"成功请求: {len(successful_runs)}, 失败请求: {failed_runs}")

        if not successful_runs:
            print("所有请求均失败，无法计算性能指标。")
            # 打印一些失败原因以供调试
            for i, res in enumerate(results[:3]): # 最多打印3个错误
                print(f"  - 失败示例 {i+1}: {res['error']}")
            continue

        ttfts = [r["ttft"] for r in successful_runs]
        throughputs = [r["throughput"] for r in successful_runs]
        output_tokens = [r["output_tokens"] for r in successful_runs]
        
        print("\n--- 性能指标统计 ---")
        print_summary("首字时间 (TTFT) (秒)", ttfts)
        print_summary("吞吐量 (Tokens/秒)", throughputs)
        
        total_output_tokens = sum(output_tokens)
        total_time_lapsed = overall_end_time - overall_start_time
        overall_throughput = total_output_tokens / total_time_lapsed if total_time_lapsed > 0 else 0
        
        print("\n--- 总体性能 ---")
        print(f"  - 所有并发请求总耗时: {total_time_lapsed:.4f} 秒")
        print(f"  - 总计生成 Tokens: {total_output_tokens}")
        print(f"  - 整体吞吐量: {overall_throughput:.4f} Tokens/秒")
        print("-" * 25)

if __name__ == "__main__":
    main()

