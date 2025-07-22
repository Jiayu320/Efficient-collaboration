"""
处理数据集的模块，用于批量处理类似math200.json这样的数据集
"""
import os
import json
import time
from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt

from config import ModelConfig
from performance import PerformanceTracker
from execution import (
    run_parallel_execution, wait_for_completion_and_get_final_result,
    judge_question_difficulty, call_small_model_directly, LLM_judge
)


class DatasetRunner:
    """数据集处理器，用于批量处理数据集并生成统计报告"""
    
    def __init__(self, config, dataset_path, limit=None, workers=4):
        """初始化数据集处理器
        
        参数:
            config: 模型配置对象
            dataset_path: 数据集文件路径
            limit: 处理的最大问题数量，None表示处理所有问题
            workers: 并行工作线程数
        """
        self.config = config
        self.dataset_path = dataset_path
        self.limit = limit
        self.workers = workers
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
        
        print(f"开始处理数据集，共 {len(self.dataset)} 个问题...")
        
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
            "difficulty": 0,
            "is_correct": False,
            "judge_result": "",
            "stats": None,
            "execution_time": 0
        }
        
        start_time = time.time()
        
        try:
            # 判断问题难度
            difficulty = judge_question_difficulty(problem, self.config)
            result["difficulty"] = difficulty
            
            # 创建性能统计跟踪器
            stats_tracker = PerformanceTracker()
            
            if int(difficulty) < self.config.threshold:
                print(f"问题难度 {difficulty} 低于阈值 {self.config.threshold}，使用小模型处理")
                
                # 直接调用小模型处理
                model_solution = call_small_model_directly(problem, self.config, stats_tracker)
                
                result["model_solution"] = model_solution
            else:
                # 运行并行执行流程
                tasks, stats_tracker = run_parallel_execution(problem, self.config, self.workers)
                
                # 获取最终结果
                model_solution = wait_for_completion_and_get_final_result(tasks, problem, self.config, stats_tracker)
                
                result["model_solution"] = model_solution
                
                # 保存任务计划和执行结果
                result["tasks"] = tasks
                
                # 计算任务规划指标
                from task_metrics import calculate_task_metrics
                task_metrics = calculate_task_metrics(tasks)
                
                # 添加任务规划指标到结果中
                result["total_tasks_num"] = task_metrics["total_tasks_num"]
                result["compression_ratio"] = task_metrics["compression_ratio"]
                result["avg_task_plan_tokens"] = task_metrics["avg_task_plan_tokens"]
            
            # 判断结果正确性（使用LLM进行判断）
            is_correct, judge_result = LLM_judge(problem, model_solution, self.config)
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
        
        # 统计按难度的正确率
        difficulty_stats = {}
        for result in self.results:
            diff = result.get("difficulty", "未知")
            if diff not in difficulty_stats:
                difficulty_stats[diff] = {"total": 0, "correct": 0}
            
            difficulty_stats[diff]["total"] += 1
            if result.get("is_correct", False):
                difficulty_stats[diff]["correct"] += 1
        
        # 统计平均执行时间
        avg_time = sum(r.get("execution_time", 0) for r in self.results) / len(self.results) if self.results else 0
        
        # 统计平均成本
        total_cost = 0
        
        # TTFT 统计和生成速度统计
        total_avg_ttft = 0
        total_time_without_ttft = 0
        total_tokens_per_second = {"small_model": 0, "large_model": 0, "router_model": 0, "total": 0}
        
        for result in self.results:
            stats = result.get("stats")
            if stats:
                costs = stats.calculate_cost()
                total_cost += costs["total"]
                
                # 计算平均TTFT
                def calc_avg_ttft(ttft_list):
                    return sum(ttft_list) / len(ttft_list) if ttft_list else 0
                
                all_ttft = stats.ttft_metrics["total"]
                if all_ttft:
                    total_avg_ttft += calc_avg_ttft(all_ttft)
                    
                # 计算去除TTFT的时间
                def calc_total_ttft(ttft_list):
                    return sum(ttft_list) if ttft_list else 0
                    
                exec_time = result.get("execution_time", 0)
                time_without_ttft = exec_time - calc_total_ttft(all_ttft)
                total_time_without_ttft += time_without_ttft
                
                # 累加每秒生成token数
                tokens_per_second = stats.calculate_tokens_per_second()
                for model_type in total_tokens_per_second.keys():
                    total_tokens_per_second[model_type] += tokens_per_second[model_type]
        
        # 计算任务规划指标的平均值
        total_tasks_count = 0
        total_compression_ratio = 0.0
        total_plan_tokens = 0.0
        task_planning_results_count = 0
        
        for result in self.results:
            if "total_tasks_num" in result and "compression_ratio" in result and "avg_task_plan_tokens" in result:
                total_tasks_count += result["total_tasks_num"]
                total_compression_ratio += result["compression_ratio"]
                total_plan_tokens += result["avg_task_plan_tokens"]
                task_planning_results_count += 1
                
        avg_tasks_num = total_tasks_count / task_planning_results_count if task_planning_results_count > 0 else 0
        avg_compression_ratio = total_compression_ratio / task_planning_results_count if task_planning_results_count > 0 else 0
        avg_plan_tokens = total_plan_tokens / task_planning_results_count if task_planning_results_count > 0 else 0
        
        # 计算平均值
        avg_cost = total_cost / len(self.results) if self.results else 0
        avg_ttft = total_avg_ttft / len(self.results) if self.results else 0
        avg_time_without_ttft = total_time_without_ttft / len(self.results) if self.results else 0
        
        # 计算平均每秒生成token数
        avg_tokens_per_second = {model_type: val / len(self.results) if self.results else 0 
                                for model_type, val in total_tokens_per_second.items()}
        
        # 生成报告
        report = "# 数据集处理报告\n\n"
        report += f"## 模型配置\n\n"
        report += f"- 小模型: {self.config.small_model}\n"
        report += f"- 大模型: {self.config.large_model}\n"
        if self.config.use_local_router:
            report += f"- 路由模型: {self.config.local_router_model}\n"
        else:
            report += f"- 路由模型: {self.config.router_model}\n"
        report += f"- 难度阈值: {self.config.threshold}\n"
        report += f"- 工作线程数: {self.workers}\n\n"
        report += f"## 概述\n\n"
        report += f"- 数据集: {self.dataset_path}\n"
        report += f"- 问题总数: {len(self.results)}\n"
        report += f"- 正确数量: {correct_count}\n"
        report += f"- 准确率: {accuracy:.2%}\n"
        report += f"- 平均执行时间: {avg_time:.2f} 秒\n"
        report += f"- 平均成本: ${avg_cost:.4f}\n\n"
        
        # 添加任务规划指标
        report += f"## 任务规划指标\n\n"
        report += f"- 平均任务步骤数: {avg_tasks_num:.2f}\n"
        report += f"- 平均压缩比例: {avg_compression_ratio:.2%}\n"
        report += f"- 平均每步骤Token限制: {avg_plan_tokens:.2f} tokens\n\n"
        
        # 添加TTFT和生成速度统计
        report += f"## 性能指标\n\n"
        report += f"### 首个令牌响应时间 (TTFT)\n"
        report += f"- 平均首个令牌响应时间: {avg_ttft:.3f} 秒\n\n"
        
        report += f"### 去除TTFT的执行时间\n"
        report += f"- 平均去除TTFT的执行时间: {avg_time_without_ttft:.3f} 秒\n\n"
        
        report += f"### 生成速度\n"
        report += f"- 小模型平均每秒生成token数: {avg_tokens_per_second['small_model']:.2f} tokens/s\n"
        report += f"- 大模型平均每秒生成token数: {avg_tokens_per_second['large_model']:.2f} tokens/s\n"
        report += f"- 路由模型平均每秒生成token数: {avg_tokens_per_second['router_model']:.2f} tokens/s\n"
        report += f"- 总平均每秒生成token数: {avg_tokens_per_second['total']:.2f} tokens/s\n\n"
        
        # 生成详细结果表格
        report += f"## 详细结果\n\n"
        report += "| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |\n"
        report += "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
        
        for i, result in enumerate(self.results):
            is_correct = "✓" if result.get("is_correct", False) else "✗"
            problem = result.get("problem", "")
            # 截断问题以适合表格
            if len(problem) > 50:
                problem = problem[:47] + "..."
            problem = problem.replace("\n", " ")
            
            exec_time = result.get("execution_time", 0)
            cost_data = result.get("stats").calculate_cost() if result.get("stats") else {"total": 0}
            total_cost = cost_data["total"] if isinstance(cost_data, dict) else 0
            
            # 获取任务规划指标
            tasks_num = result.get("total_tasks_num", "-")
            compression = result.get("compression_ratio", "-")
            if compression != "-":
                compression = f"{compression:.2%}"
            plan_tokens = result.get("avg_task_plan_tokens", "-")
            if plan_tokens != "-":
                plan_tokens = f"{plan_tokens:.1f}"
            
            report += f"| {i+1} | {problem} | {is_correct} | {exec_time:.2f} | {total_cost:.4f} | {tasks_num} | {compression} | {plan_tokens} |\n"
        
        return report
    
    def save_report(self, output_dir="dataset_reports"):
        """保存处理报告到文件
        
        参数:
            output_dir: 输出目录
            
        返回:
            报告文件路径
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        report_file = os.path.join(output_dir, f"dataset_report_{timestamp}.md")
        
        # 生成报告
        report = self.generate_report()
        
        # 保存到文件
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"报告已保存至: {report_file}")
        
        # 生成可视化图表
        # self.generate_visualizations(output_dir, timestamp)
        
        # 保存JSON结果
        json_file = self.save_results_json("dataset_results", timestamp)
        print(f"JSON结果已保存至: {json_file}")
        
        return report_file
    
    def save_results_json(self, output_dir="dataset_results", timestamp=None):
        """将处理结果保存为JSON格式
        
        参数:
            output_dir: 输出目录
            timestamp: 时间戳，如果为None则自动生成
            
        返回:
            JSON文件路径
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        if timestamp is None:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            
        json_file = os.path.join(output_dir, f"dataset_results_{timestamp}.json")
        
        # 准备JSON数据
        json_results = []
        
        for result in self.results:
            # 创建一个可序列化的结果对象
            serializable_result = {
                "problem": result.get("problem", ""),
                "gold_solution": result.get("gold_solution", ""),
                "model_solution": result.get("model_solution", ""),
                "difficulty": result.get("difficulty", 0),
                "is_correct": result.get("is_correct", False),
                "judge_result": result.get("judge_result", ""),
                "execution_time": result.get("execution_time", 0),
                "total_tasks_num": result.get("total_tasks_num", 0),
                "compression_ratio": result.get("compression_ratio", 0),
                "avg_task_plan_tokens": result.get("avg_task_plan_tokens", 0)
            }
            
            # 添加任务计划和步骤结果（如果存在）
            if "tasks" in result:
                # 将tasks字典转换为可序列化的对象
                serializable_tasks = {}
                for task_id, task_info in result["tasks"].items():
                    serializable_task = {}
                    for key, value in task_info.items():
                        # 确保所有值都是可序列化的
                        if key in ["Task", "Rely", "Token", "Difficulty", "Result"]:
                            serializable_task[key] = value
                    serializable_tasks[task_id] = serializable_task
                
                serializable_result["tasks"] = serializable_tasks
            
            # 添加性能统计数据
            if result.get("stats"):
                stats = result["stats"]
                costs = stats.calculate_cost()
                tokens_per_second = stats.calculate_tokens_per_second()
                
                serializable_result["stats"] = {
                    "costs": costs,
                    "tokens_per_second": tokens_per_second,
                    "token_usage": stats.token_usage,
                    "ttft_metrics": stats.ttft_metrics
                }
            
            json_results.append(serializable_result)
        
        # 保存到JSON文件
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_results, f, ensure_ascii=False, indent=2)
        
        print(f"JSON结果已保存至: {json_file}")
        
        return json_file
    
    def generate_visualizations(self, output_dir, timestamp):
        """生成可视化图表
        
        参数:
            output_dir: 输出目录
            timestamp: 时间戳
        """
        try:
            # 收集数据
            data = []
            for result in self.results:
                stats = result.get("stats")
                if not stats:
                    continue
                
                # 计算成本
                costs = stats.calculate_cost()
                
                data.append({
                    "difficulty": result.get("difficulty", 0),
                    "is_correct": result.get("is_correct", False),
                    "execution_time": result.get("execution_time", 0),
                    "cost": costs["total"],
                    "small_model_tokens": stats.token_usage["small_model"]["total_tokens"],
                    "large_model_tokens": stats.token_usage["large_model"]["total_tokens"]
                })
            
            if not data:
                return
            
            # 创建数据框
            df = pd.DataFrame(data)
            
            # Difficulty distribution
            plt.figure(figsize=(10, 6))
            difficulty_counts = df["difficulty"].value_counts().sort_index()
            difficulty_counts.plot(kind='bar')
            plt.title("Difficulty Distribution")
            plt.xlabel("Difficulty")
            plt.ylabel("Number of Problems")
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, f"difficulty_distribution_{timestamp}.png"))
            plt.close()
            
            # Accuracy vs Difficulty
            plt.figure(figsize=(10, 6))
            accuracy_by_difficulty = df.groupby("difficulty")["is_correct"].mean()
            accuracy_by_difficulty.plot(kind='bar')
            plt.title("Accuracy by Difficulty")
            plt.xlabel("Difficulty")
            plt.ylabel("Accuracy")
            plt.ylim(0, 1)
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, f"accuracy_by_difficulty_{timestamp}.png"))
            plt.close()
            
            # Execution Time vs Difficulty
            plt.figure(figsize=(10, 6))
            time_by_difficulty = df.groupby("difficulty")["execution_time"].mean()
            time_by_difficulty.plot(kind='bar')
            plt.title("Average Execution Time by Difficulty")
            plt.xlabel("Difficulty")
            plt.ylabel("Execution Time (seconds)")
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, f"time_by_difficulty_{timestamp}.png"))
            plt.close()
            
            # Cost vs Difficulty
            plt.figure(figsize=(10, 6))
            cost_by_difficulty = df.groupby("difficulty")["cost"].mean()
            cost_by_difficulty.plot(kind='bar')
            plt.title("Average Cost by Difficulty")
            plt.xlabel("Difficulty")
            plt.ylabel("Cost (USD)")
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, f"cost_by_difficulty_{timestamp}.png"))
            plt.close()
            
        except Exception as e:
            print(f"生成可视化图表时出错: {e}")


def run_dataset_evaluation(config, dataset_path, limit=None, workers=4):
    """运行数据集评估
    
    参数:
        config: 模型配置对象
        dataset_path: 数据集文件路径
        limit: 处理的最大问题数量
        workers: 并行工作线程数
        
    返回:
        元组: (报告文件路径, JSON结果文件路径)
    """
    print(f"开始数据集评估: {dataset_path}")
    
    # 创建数据集处理器
    runner = DatasetRunner(config, dataset_path, limit, workers)
    
    # 处理数据集
    runner.process_dataset()
    
    # 保存报告
    report_file = runner.save_report()
    
    # 获取JSON文件路径
    timestamp = report_file.split("_")[-1].replace(".md", "")
    json_file = os.path.join("dataset_results", f"dataset_results_{timestamp}.json")
    
    return report_file, json_file
