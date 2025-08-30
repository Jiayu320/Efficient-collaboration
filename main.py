import os
import time
import json
from config import ModelConfig, load_config, parse_args
from performance import PerformanceTracker, calculate_performance_metrics
from output_performance import generate_theoretical_performance_report
from execution import (
    run_parallel_execution, print_results, wait_for_completion_and_get_final_result,
    judge_question_difficulty, call_small_model_directly, generate_task_dependency_report,
    judge_correct, LLM_judge, save_result_to_file
)
# 导入数据集处理模块
from dataset_runner import run_dataset_evaluation

def main():
    """主程序入口"""
    print("启动程序...")
    
    # 解析命令行参数
    args = parse_args()
    print(f"配置文件: {args.config}")
    
    # 加载配置文件
    yaml_config = load_config(args.config)

    # 构建最终配置
    small_model = yaml_config["models"]["small_model"]
    large_model = yaml_config["models"]["large_model"]
    router_model = yaml_config["models"].get("router_model", small_model)  # 如果未设置，默认使用小模型
    # 获取本地路由模型配置
    use_local_router = yaml_config["models"].get("use_local_router", False)
    local_router_model = yaml_config["models"].get("local_router_model", "saves/Qwen3-1.7B-Instruct/full/sft")

    small_key_path = yaml_config["api"]["small_key_path"]
    large_key_path = yaml_config["api"]["large_key_path"]
    router_key_path = yaml_config["api"]["router_key_path"]
    api_base = yaml_config["api"]["base_url"]
    # 获取各个模型的API基础URL（如果配置中有的话）
    small_api_base = yaml_config["api"].get("small_api_base_url", api_base)  # 注意配置中使用了 small_api_base_url
    large_api_base = yaml_config["api"].get("large_api_base_url", api_base)
    router_api_base = yaml_config["api"].get("router_api_base_url", api_base)
    local_router_base = yaml_config["api"].get("local_router_base_url", "http://127.0.0.1:8000/v1")
    prompt_path = yaml_config["system"]["prompt_path"]
    workers = yaml_config["system"]["workers"]

    # 获取判断相关配置
    enable_judge = yaml_config["system"].get("enable_judge", False)
    gold_answer = yaml_config["system"].get("gold_answer", "")
    enable_threshold = yaml_config["system"].get("enable_threshold", False)
    if use_local_router:
        prompt_path = "prompt/generate_prompt.txt"
        threshold = yaml_config["models"]["threshold"]
    else:
        prompt_path = "prompt/generate_prompt_ori.txt"
        threshold = yaml_config["models"]["threshold"]

    # 初始化模型配置
    config = ModelConfig(
        small_model=small_model,
        large_model=large_model,
        router_model=router_model,
        threshold=threshold,
        small_key_path=small_key_path,
        large_key_path=large_key_path,
        router_key_path=router_key_path,
        prompt_path=prompt_path,
        api_base=api_base,
        small_api_base=small_api_base,
        large_api_base=large_api_base,
        router_api_base=router_api_base,
        use_local_router=use_local_router,
        local_router_base=local_router_base,
        local_router_model=local_router_model
    )
    # 检查是否为数据集处理模式
    # 优先使用命令行参数，其次使用配置文件
    dataset_enabled = args.dataset or yaml_config.get("dataset", {}).get("enabled", False)
    dataset_path = args.dataset_path or yaml_config.get("dataset", {}).get("path", "")
    dataset_limit = args.dataset_limit or yaml_config.get("dataset", {}).get("limit", None)

    if dataset_enabled and dataset_path:
        print("===== 数据集处理模式 =====")
        print(f"使用小模型: {config.small_model}")
        print(f"使用大模型: {config.large_model}")
        if config.use_local_router:
            print(f"使用本地路由模型: {config.local_router_model}")
        else:
            print(f"使用远程路由模型: {config.router_model}")
        print(f"难度阈值: {config.threshold}")
        print(f"工作线程数: {workers}")
        print(f"数据集路径: {dataset_path}")
        if dataset_limit:
            print(f"数据集限制: {dataset_limit} 条")
        
        try:
            # 运行数据集评估
            report_file = run_dataset_evaluation(config, dataset_path, dataset_limit, workers)
            
            # 添加任务分配统计
            print("正在生成任务分配统计...")
            # 获取对应的 dataset_results.json 文件路径
            results_dir = os.path.dirname(report_file)
            results_file = os.path.join(results_dir, "dataset_results.json")
            
            if os.path.exists(results_file):
                try:
                    # 读取 JSON 文件
                    with open(results_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    # 初始化计数器
                    total_tasks = 0
                    small_model_tasks = 0
                    large_model_tasks = 0
                    
                    # 遍历所有问题
                    for problem in data:
                        tasks = problem.get('tasks', {})
                        
                        # 遍历每个问题的任务
                        for task_id, task_info in tasks.items():
                            total_tasks += 1
                            
                            # 获取任务难度（如果不存在，假设为0）
                            difficulty = int(task_info.get('Difficulty', 0))
                            
                            # 根据难度阈值判断使用哪个模型
                            if difficulty < config.threshold:
                                small_model_tasks += 1
                            else:
                                large_model_tasks += 1
                    
                    # 计算百分比
                    small_model_percentage = (small_model_tasks / total_tasks * 100) if total_tasks > 0 else 0
                    large_model_percentage = (large_model_tasks / total_tasks * 100) if total_tasks > 0 else 0
                    
                    # 生成统计文本
                    stats_text = "\n## 任务分配统计\n\n"
                    stats_text += f"- 总任务数: {total_tasks}\n"
                    stats_text += f"- 小模型执行任务数: {small_model_tasks}\n"
                    stats_text += f"- 大模型执行任务数: {large_model_tasks}\n"
                    stats_text += f"- 小模型任务占比: {small_model_percentage:.2f}%\n"
                    stats_text += f"- 大模型任务占比: {large_model_percentage:.2f}%\n"
                    
                    # 将统计信息添加到报告文件中
                    with open(report_file, 'r', encoding='utf-8') as f:
                        report_content = f.read()
                    
                    # 在"性能指标"部分之前插入任务分配统计
                    performance_section_index = report_content.find("## 性能指标")
                    if performance_section_index != -1:
                        new_report_content = report_content[:performance_section_index] + stats_text + "\n" + report_content[performance_section_index:]
                    else:
                        # 如果找不到性能指标部分，则添加到文件末尾
                        new_report_content = report_content + stats_text
                    
                    # 写回报告文件
                    with open(report_file, 'w', encoding='utf-8') as f:
                        f.write(new_report_content)
                    
                    print("任务分配统计已添加到报告中")
                except Exception as e:
                    print(f"生成任务分配统计时出错: {e}")
            else:
                print(f"未找到对应的结果文件: {results_file}")
            
            print(f"数据集评估完成，报告已保存至: {report_file}")
            return
        except Exception as e:
            print(f"数据集处理过程中出错: {e}")
            import traceback
            traceback.print_exc()
            return
    
    # 单问题处理模式
    print("===== 单问题处理模式 =====")
    # 设置查询
    query = yaml_config["query"]
    print(f"使用小模型: {config.small_model}")
    print(f"使用大模型: {config.large_model}")
    if config.use_local_router:
        print(f"使用本地路由模型: {config.local_router_model}")
    else:
        print(f"使用远程路由模型: {config.router_model}")
    print(f"难度阈值: {config.threshold}")
    print(f"工作线程数: {workers}")
    print(f"当前查询: {query}")

    try:
        # 初始化模型客户端
        from execution import initialize_clients, warmup_models
        initialize_clients(config)
        warmup_models(config)
        
        # 判断问题难度
        difficulty = judge_question_difficulty(query, config)
        
        # 创建性能统计跟踪器（无论使用哪种方法都需要）
        stats_tracker = PerformanceTracker(config)
        
        if enable_threshold and int(difficulty) < config.threshold:
            print(f"问题难度 {difficulty} 低于阈值 {config.threshold}，使用小模型处理")

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
        
        # 计算并打印实际性能指标
        performance_report = calculate_performance_metrics(stats_tracker)
        print("\n实际性能统计:")
        print(performance_report)
        
        # 生成基于理论模型的性能报告
        theoretical_report = generate_theoretical_performance_report(tasks, config, stats_tracker.planner_output)
        print("\n理论性能模型分析:")
        print(theoretical_report)
        
        # 生成任务依赖关系报告
        dependency_report = generate_task_dependency_report(tasks)
        print("\n任务规划依赖关系:")
        print(dependency_report)
        
        # 将最终结果保存到文件
        output_file = save_result_to_file(final_result, config, workers, correctness_report, performance_report, dependency_report, theoretical_report)
        if output_file:
            print(f"结果已保存至: {output_file}")
            
    except Exception as e:
        print(f"处理过程中出错: {e}")

if __name__ == "__main__":
    main()
