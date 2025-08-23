"""
测试本地模型作为路由器(router)时的性能指标
包括延迟(latency)和吞吐量(throughput)
通过五次测试取平均值
"""
import time
import statistics
import argparse
from config import ModelConfig, load_config
from execution import initialize_clients
import json

def test_router_performance(config, test_queries, num_tests=5):
    """
    测试路由模型的性能
    
    参数:
        config: 模型配置对象
        test_queries: 测试用的查询列表
        num_tests: 测试次数，默认为5
        
    返回:
        包含性能测试结果的字典
    """
    # 确保初始化客户端
    from execution import router_model_client
    if router_model_client is None:
        initialize_clients(config)
    
    print(f"使用{'本地' if config.use_local_router else '远程'}路由模型: {config.local_router_model if config.use_local_router else config.router_model}")
    
    # 用于存储测试结果
    latency_results = []
    throughput_results = []
    token_counts = []
    
    # 定义测试提示
    difficulty_prompt_template = """Please determine the difficulty of the following math problem. 
    Difficulty scale:
    1-10 (1=simplest, 10=hardest)
    Problem: {question}
    Please output only the difficulty level as a number. No other explanations or details are needed.
    """
    
    for test_num in range(1, num_tests + 1):
        print(f"\n执行测试 {test_num}/{num_tests}...")
        
        # 为每个查询测试性能
        test_latencies = []
        test_throughputs = []
        
        for i, query in enumerate(test_queries):
            print(f"  测试查询 {i+1}/{len(test_queries)}: {query[:30]}...")
            
            prompt = difficulty_prompt_template.format(question=query)
            
            # 开始时间
            start_time = time.time()
            
            try:
                if config.use_local_router:
                    # 使用本地路由模型
                    response = router_model_client.chat.completions.create(
                        model=config.local_router_model,
                        messages=[{"role": "user", "content": prompt}],
                        stream=False
                    )
                else:
                    # 使用远程路由模型
                    response = router_model_client.chat.completions.create(
                        model=config.router_model,
                        messages=[{"role": "user", "content": prompt}],
                        stream=False
                    )
                
                # 结束时间
                end_time = time.time()
                
                # 获取结果
                difficulty = response.choices[0].message.content.strip()
                
                # 计算指标
                latency = end_time - start_time  # 延迟，单位秒
                
                # 获取token数量
                prompt_tokens = response.usage.prompt_tokens
                completion_tokens = response.usage.completion_tokens
                total_tokens = response.usage.total_tokens
                
                # 计算吞吐量 (tokens per second)
                throughput = total_tokens / latency if latency > 0 else 0
                
                # 保存结果
                test_latencies.append(latency)
                test_throughputs.append(throughput)
                
                print(f"    难度评估: {difficulty}")
                print(f"    延迟: {latency:.4f}s, 吞吐量: {throughput:.2f} tokens/s")
                print(f"    Token使用: 提示={prompt_tokens}, 完成={completion_tokens}, 总计={total_tokens}")
                
            except Exception as e:
                print(f"    测试出错: {e}")
                # 如果出错，添加一个空值，不影响其他测试
                test_latencies.append(None)
                test_throughputs.append(None)
        
        # 过滤掉失败的测试
        valid_latencies = [lat for lat in test_latencies if lat is not None]
        valid_throughputs = [tpt for tpt in test_throughputs if tpt is not None]
        
        if valid_latencies and valid_throughputs:
            # 计算本次测试的平均值
            avg_latency = statistics.mean(valid_latencies)
            avg_throughput = statistics.mean(valid_throughputs)
            
            latency_results.append(avg_latency)
            throughput_results.append(avg_throughput)
            
            print(f"  测试 {test_num} 平均延迟: {avg_latency:.4f}s")
            print(f"  测试 {test_num} 平均吞吐量: {avg_throughput:.2f} tokens/s")
        else:
            print(f"  测试 {test_num} 未获得有效结果")
    
    # 计算所有测试的平均值和标准差
    if latency_results and throughput_results:
        avg_latency_all = statistics.mean(latency_results)
        avg_throughput_all = statistics.mean(throughput_results)
        
        if len(latency_results) > 1:
            stdev_latency = statistics.stdev(latency_results)
            stdev_throughput = statistics.stdev(throughput_results)
        else:
            stdev_latency = 0
            stdev_throughput = 0
        
        return {
            "model": config.local_router_model if config.use_local_router else config.router_model,
            "is_local": config.use_local_router,
            "num_tests": num_tests,
            "latency": {
                "mean": avg_latency_all,
                "stdev": stdev_latency,
                "values": latency_results
            },
            "throughput": {
                "mean": avg_throughput_all,
                "stdev": stdev_throughput,
                "values": throughput_results
            }
        }
    else:
        return {
            "error": "所有测试均未获得有效结果"
        }

def save_test_results(results, output_file=None):
    """保存测试结果到文件"""
    if output_file is None:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        model_name = results["model"].split("/")[-1] if "/" in results["model"] else results["model"]
        model_type = "local" if results.get("is_local", False) else "remote"
        output_file = f"router_performance_{model_type}_{model_name}_{timestamp}.json"
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    return output_file

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="测试本地路由模型的性能")
    parser.add_argument("--config", default="config.yaml", help="配置文件路径")
    parser.add_argument("--tests", type=int, default=5, help="测试次数")
    parser.add_argument("--output", help="输出文件路径")
    args = parser.parse_args()
    
    # 加载配置
    yaml_config = load_config(args.config)
    
    # 获取本地路由模型配置
    use_local_router = yaml_config["models"].get("use_local_router", False)
    local_router_model = yaml_config["models"].get("local_router_model", "saves/Qwen3-1.7B-Instruct/full/sft")
    
    small_model = yaml_config["models"]["small_model"]
    large_model = yaml_config["models"]["large_model"]
    router_model = yaml_config["models"].get("router_model", small_model)
    
    small_key_path = yaml_config["api"]["small_key_path"]
    large_key_path = yaml_config["api"]["large_key_path"]
    router_key_path = yaml_config["api"]["router_key_path"]
    
    api_base = yaml_config["api"]["base_url"]
    small_api_base = yaml_config["api"].get("small_api_base_url", api_base)
    large_api_base = yaml_config["api"].get("large_api_base_url", api_base)
    router_api_base = yaml_config["api"].get("router_api_base_url", api_base)
    local_router_base = yaml_config["api"].get("local_router_base_url", "http://127.0.0.1:8000/v1")
    
    # 创建模型配置
    config = ModelConfig(
        small_model=small_model,
        large_model=large_model,
        router_model=router_model,
        threshold=yaml_config["models"].get("threshold", 2),
        small_key_path=small_key_path,
        large_key_path=large_key_path,
        router_key_path=router_key_path,
        prompt_path=yaml_config["system"].get("prompt_path", "prompt/generate_prompt.txt"),
        api_base=api_base,
        small_api_base=small_api_base,
        large_api_base=large_api_base,
        router_api_base=router_api_base,
        use_local_router=use_local_router,
        local_router_base=local_router_base,
        local_router_model=local_router_model
    )
    
    # 初始化客户端
    initialize_clients(config)
    
    # 测试查询
    test_queries = [
        "What is the result of 1+1?",
        "If a triangle has sides of length 3, 4, and 5, what is its area?",
        "Solve the equation: 2x + 5 = 13",
        "A circle has radius 5. What is its circumference?",
        "Find all the roots of the equation x^3 - 4x^2 + 5x - 2 = 0"
    ]
    
    print(f"开始测试路由模型性能...")
    print(f"将执行 {args.tests} 次测试")
    
    # 执行测试
    results = test_router_performance(config, test_queries, args.tests)
    
    # 打印结果
    print("\n测试结果摘要:")
    print(f"模型: {results['model']} ({'本地' if results.get('is_local', False) else '远程'})")
    print(f"平均延迟: {results['latency']['mean']:.4f}s ± {results['latency']['stdev']:.4f}")
    print(f"平均吞吐量: {results['throughput']['mean']:.2f} tokens/s ± {results['throughput']['stdev']:.2f}")
    
    # 保存结果
    output_file = save_test_results(results, args.output)
    print(f"结果已保存到: {output_file}")
    
    # 更新output_performance.py中的模型性能数据
    print("\n提示: 如果需要更新output_performance.py中的模型性能数据，请使用以下值:")
    print(f"本地路由模型 '{local_router_model}' 的性能:")
    print(f"    'latency': {results['latency']['mean']:.2f}")
    print(f"    'throughput': {results['throughput']['mean']:.2f}")

if __name__ == "__main__":
    main()

'''
# 使用默认配置运行5次测试
python test_local_router_performance.py

# 自定义测试次数
python test_local_router_performance.py --tests 10

# 指定配置文件
python test_local_router_performance.py --config custom_config.yaml

# 自定义输出文件
python test_local_router_performance.py --output my_test_results.json
'''