import os
import json
import time
from tqdm import tqdm
from datetime import datetime
import argparse

from config import ModelConfig, load_config, parse_args
from execution import (
    dataset_run_parallel_execution, wait_for_completion_and_get_final_result,
    judge_question_difficulty, judge_correct, run_parallel_execution
)
from task_metrics import calculate_task_metrics
from performance import PerformanceTracker

def generate_training_data(input_dataset_path, output_path, config, limit=100, workers=10):
    """
    生成训练数据集
    
    参数:
        input_dataset_path: 输入数据集路径
        output_path: 输出数据集路径
        config: 模型配置对象
        limit: 处理的最大问题数量，None表示处理所有问题
        workers: 并行工作线程数
    
    返回:
        生成的数据集
    """
    print(f"开始从 {input_dataset_path} 生成训练数据...")
    
    # 验证配置对象是否是ModelConfig类的实例
    if not isinstance(config, ModelConfig):
        raise TypeError("配置对象必须是ModelConfig类的实例")
    
    # 验证配置对象的必要属性
    required_attrs = [
        'small_model', 'large_model', 'router_model', 'threshold', 
        'use_local_router', 'local_router_model'
    ]
    
    for attr in required_attrs:
        if not hasattr(config, attr):
            raise AttributeError(f"配置对象缺少必要的属性: {attr}")
            
    print("配置验证成功，继续处理...")
    
    # 加载输入数据集
    with open(input_dataset_path, 'r', encoding='utf-8') as f:
        input_dataset = json.load(f)
    
    # 如果设置了限制，只处理前N个问题
    if limit:
        input_dataset = input_dataset[:limit]
    
    # 检查是否已有处理过的数据
    training_data = []
    processed_questions = set()
    
    if os.path.exists(output_path):
        try:
            with open(output_path, 'r', encoding='utf-8') as f:
                training_data = json.load(f)
                print(f"加载已有数据，已处理 {len(training_data)} 个问题")
                
                # 记录已处理过的问题
                for item in training_data:
                    processed_questions.add(item.get("question", ""))
        except Exception as e:
            print(f"读取已有数据出错: {str(e)}")
            training_data = []
    
    print(f"已有 {len(processed_questions)} 个问题被处理过，将跳过这些问题")
    
    # 计算需要处理的问题数量
    questions_to_process = []
    for item in input_dataset:
        question = item.get("problem") or item.get("question")
        answer = item.get("answer") or ""
        ori_solution = item.get("solution") or ""

        if not question or question in processed_questions:
            continue

        questions_to_process.append((question, answer, ori_solution))
    
    print(f"共有 {len(questions_to_process)} 个新问题需要处理")
    
    # 使用tqdm显示进度
    for i, (question, answer, ori_solution) in enumerate(tqdm(questions_to_process, desc="处理数据集")):
        if not question:
            print(f"跳过项目 {i+1}：没有找到问题")
            continue
        
        print(f"\n处理问题 {i+1}/{len(questions_to_process)}: {question[:100]}...")
        
        try:
            # 记录开始时间
            start_time = time.time()
            
            # 初始化性能跟踪器
            stats_tracker = PerformanceTracker(config)
            
            # 评估难度
            difficulty = judge_question_difficulty(question, config)
            print(f"问题难度评估: {difficulty}")
            
            # 运行并行执行流程，获取任务计划和结果
            # tasks, stats_tracker = dataset_run_parallel_execution(question, ori_solution, config, workers)
            tasks, stats_tracker = run_parallel_execution(question, config, workers)
            # 获取最终结果
            solution = wait_for_completion_and_get_final_result(tasks, question, config, stats_tracker)
            
            # 判断结果正确性
            is_correct, judge_result = judge_correct(question, answer, solution, config)

            # 停止性能跟踪
            stats_tracker.stop_tracking()
            execution_time = time.time() - start_time
            
            # 计算任务规划指标
            metrics = calculate_task_metrics(tasks)
            
            # 提取计划的XML格式
            plan_xml = "<Plan>"
            for step_id, attrs in sorted(tasks.items(), key=lambda x: int(x[0])):
                task = attrs.get('Task', '')
                difficulty_val = attrs.get('Difficulty', '1')
                token = attrs.get('Token', '10')
                rely = attrs.get('Rely', '')
                
                plan_xml += f'<Step ID="{step_id}" Task="{task}" Difficulty="{difficulty_val}" Token="{token}" Rely="{rely}"/>'
            plan_xml += "</Plan>"
            
            # 创建训练数据项
            data_item = {
                "question": question,
                "answer": answer,
                "solution": solution,
                "plan": plan_xml,
                "difficulty": difficulty,
                "correct": is_correct,
                "steps": metrics["total_tasks_num"],
                "token_predict": metrics["avg_task_plan_tokens"],
                "compression": metrics["compression_ratio"],
                "time_cost": execution_time,
                "api_cost": stats_tracker.calculate_cost()
            }
            
            training_data.append(data_item)
            
            # 在处理过程中保存进度
            if (i + 1) % 5 == 0 or (i + 1) == len(input_dataset):
                save_intermediate_data(training_data, output_path)
            
        except Exception as e:
            print(f"处理问题时出错: {str(e)}")
    
    # 最后保存完整数据集
    save_intermediate_data(training_data, output_path)
    
    print(f"训练数据生成完成，共有 {len(training_data)} 个问题的处理结果")
    return training_data

def save_intermediate_data(data, output_path):
    """
    保存中间数据到文件
    
    参数:
        data: 数据列表
        output_path: 输出路径
    """
    # 确保输出目录存在
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 保存数据
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"数据已保存到 {output_path}")

def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="生成训练数据集")
    parser.add_argument("--config", type=str, default="config.yaml", help="配置文件路径")
    parser.add_argument("--input", type=str, default="dataset\\generated_data\\s1k1_1_false_results.json", help="输入数据集路径")
    parser.add_argument("--output", type=str, default="dataset\\generated_data\\s1k1_1_training_0.json", help="输出数据集路径")
    parser.add_argument("--limit", type=int, default=None, help="处理的最大问题数量")
    parser.add_argument("--workers", type=int, default=4, help="并行工作线程数")
    
    args = parser.parse_args()
    
    # 加载配置
    config_args = parse_args()
    config_args.config = args.config
    config_dict = load_config(config_args.config)
    
    # 获取API配置
    api_config = config_dict.get("api", {})
    
    # 创建ModelConfig实例
    models_config = config_dict.get("models", {})
    system_config = config_dict.get("system", {})
    config = ModelConfig(
        small_model=models_config.get("small_model", "meta-llama/llama-3-8b-instruct"),
        large_model=models_config.get("large_model", "gpt-4o"),
        router_model=models_config.get("router_model", "claude-3-5-sonnet-latest"),
        threshold=models_config.get("threshold", 2),
        
        # API配置
        api_base=api_config.get("base_url", "https://api.bianxie.ai/v1"),
        small_api_base=api_config.get("small_api_base_url", "https://openrouter.ai/api/v1"),
        large_api_base=api_config.get("large_api_base_url", "https://api.bianxie.ai/v1"),
        router_api_base=api_config.get("router_api_base_url", "https://api.bianxie.ai/v1"),
        
        # API密钥路径
        small_key_path=api_config.get("small_key_path", "usage/openrouter"),
        large_key_path=api_config.get("large_key_path", "usage/bianxie"),
        router_key_path=api_config.get("router_key_path", "usage/bianxie"),

        # 提示词路径
        prompt_path=system_config.get("prompt_path", "prompt/generate_prompt.txt"),
        
        # 路由模型配置
        use_local_router=models_config.get("use_local_router", False),
        local_router_base=models_config.get("local_router_base", "http://127.0.0.1:8000/v1"),
        local_router_model=models_config.get("local_router_model", "saves/Qwen3-1.7B-Instruct/full/sft")
    )
    
    # 确保配置中不使用dataset.path，而是使用命令行参数中的--input路径
    print(f"使用输入数据集: {args.input} (忽略config.yaml中的dataset.path设置)")
    
    # 生成训练数据
    generate_training_data(args.input, args.output, config, args.limit, args.workers)

if __name__ == "__main__":
    main()
