import os
import time
from config import ModelConfig, load_config, parse_args
from performance import PerformanceTracker, calculate_performance_metrics
from execution import (
    run_parallel_execution, print_results, wait_for_completion_and_get_final_result,
    judge_question_difficulty, call_small_model_directly, generate_task_dependency_report,
    judge_correct, LLM_judge, save_result_to_file
)

def main():
    """主程序入口"""
    print("启动程序...")
    
    # 解析命令行参数
    args = parse_args()
    print(f"配置文件: {args.config}")
    
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

    print(f"使用小模型: {config.small_model}")
    print(f"使用大模型: {config.large_model}")
    print(f"使用路由模型: {config.router_model}")
    print(f"难度阈值: {config.threshold}")
    print(f"工作线程数: {workers}")
    print(f"当前查询: {query}")

    try:
        # 判断问题难度
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
            tasks, stats_tracker = run_parallel_execution(query, config, workers)
            
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
        
        # 将最终结果保存到文件
        output_file = save_result_to_file(final_result, config, workers, correctness_report, performance_report, dependency_report)
        if output_file:
            print(f"结果已保存至: {output_file}")
            
    except Exception as e:
        print(f"处理过程中出错: {e}")

if __name__ == "__main__":
    main()
