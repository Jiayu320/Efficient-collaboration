"""
测试output_performance.py中的理论性能模型计算函数

此文件创建一个简单的任务结构和配置对象，用于测试generate_theoretical_performance_report函数。
"""
import os
import sys
from typing import Dict, Any

# 添加当前目录到模块搜索路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 导入需要测试的函数
from output_performance import (
    get_model_performance, 
    calculate_theoretical_time, 
    generate_theoretical_performance_report,
    simulate_task_execution,
    find_critical_path
)

# 创建一个模拟的ModelConfig类
class MockModelConfig:
    """模拟的模型配置类，仅用于测试"""
    
    def __init__(self, small_model="gpt-3.5-turbo", large_model="gpt-4o", router_model="gpt-3.5-turbo", threshold=3):
        self.small_model = small_model
        self.large_model = large_model
        self.router_model = router_model
        self.threshold = threshold
        self.use_local_router = False


def create_mock_tasks() -> Dict[str, Dict[str, Any]]:
    """创建模拟的任务结构"""
    return {
        "1": {
            "ID": "1",
            "Task": "解析问题并确定所需的数学概念?",
            "Difficulty": "2",
            "Token": "300",
            "Rely": "",
            "Result": "问题要求我们计算几何图形的面积和周长..."
        },
        "2": {
            "ID": "2",
            "Task": "计算三角形的面积?",
            "Difficulty": "3",
            "Token": "500",
            "Rely": "1",
            "Result": "使用三角形面积公式: S = (1/2) * b * h..."
        },
        "3": {
            "ID": "3",
            "Task": "计算圆的面积?",
            "Difficulty": "2",
            "Token": "400",
            "Rely": "1",
            "Result": "圆的面积公式是 S = πr²..."
        },
        "4": {
            "ID": "4",
            "Task": "计算总面积?",
            "Difficulty": "4",
            "Token": "600",
            "Rely": "2,3",
            "Result": "总面积是三角形面积加上圆的面积..."
        }
    }


def create_mock_planner_output() -> Dict[str, Any]:
    """创建模拟的planner输出信息"""
    return {
        'prompt_tokens': 200,
        'completion_tokens': 400,
        'ttft': 0.8,
        'total_tokens': 600
    }


def test_get_model_performance():
    """测试get_model_performance函数"""
    models = ["gpt-4o", "claude-3-5-sonnet", "llama3-8b", "deepseek-r1", "unknown-model"]
    
    print("\n=== 测试 get_model_performance 函数 ===")
    for model in models:
        perf = get_model_performance(model)
        print(f"模型: {model}, 延迟: {perf['latency']:.3f}秒, 吞吐量: {perf['throughput']:.2f} tokens/s")
    
    # 预期结果:
    # 模型: gpt-4o, 延迟: 0.610秒, 吞吐量: 58.71 tokens/s
    # 模型: claude-3-5-sonnet, 延迟: 1.060秒, 吞吐量: 57.07 tokens/s
    # 模型: llama3-8b, 延迟: 0.440秒, 吞吐量: 3422.00 tokens/s
    # 模型: deepseek-r1, 延迟: 1.010秒, 吞吐量: 55.17 tokens/s
    # 模型: unknown-model, 延迟: 0.500秒, 吞吐量: 100.00 tokens/s


def test_calculate_theoretical_time():
    """测试calculate_theoretical_time函数"""
    test_cases = [
        ("gpt-4o", 500),
        ("claude-3-5-sonnet", 1000),
        ("llama3-8b", 2000),
        ("deepseek-r1", 750),
        ("unknown-model", 500)
    ]
    
    print("\n=== 测试 calculate_theoretical_time 函数 ===")
    for model, tokens in test_cases:
        result = calculate_theoretical_time(model, tokens)
        print(f"模型: {model}, Tokens: {tokens}")
        print(f"  延迟: {result['latency']:.3f}秒")
        print(f"  生成时间: {result['generation_time']:.3f}秒")
        print(f"  总时间: {result['total_time']:.3f}秒")
    
    # 预期结果:
    # 模型: gpt-4o, Tokens: 500
    #   延迟: 0.610秒
    #   生成时间: 8.517秒 (500 / 58.71)
    #   总时间: 9.127秒
    
    # 模型: claude-3-5-sonnet, Tokens: 1000
    #   延迟: 1.060秒
    #   生成时间: 17.522秒 (1000 / 57.07)
    #   总时间: 18.582秒
    
    # 模型: llama3-8b, Tokens: 2000
    #   延迟: 0.440秒
    #   生成时间: 0.585秒 (2000 / 3422)
    #   总时间: 1.025秒
    
    # 模型: deepseek-r1, Tokens: 750
    #   延迟: 1.010秒
    #   生成时间: 13.594秒 (750 / 55.17)
    #   总时间: 14.604秒
    
    # 模型: unknown-model, Tokens: 500
    #   延迟: 0.500秒
    #   生成时间: 5.000秒 (500 / 100)
    #   总时间: 5.500秒


def test_simulate_task_execution():
    """测试simulate_task_execution函数"""
    tasks = create_mock_tasks()
    sorted_tasks = sorted(tasks.items(), key=lambda x: int(x[0]))
    
    # 构建依赖图
    dependency_graph = {}
    for step_id, task in sorted_tasks:
        rely_str = task.get('Rely', '')
        dependencies = [dep for dep in rely_str.split(',') if dep]
        dependency_graph[step_id] = dependencies
    
    # 模拟执行时间
    task_execution_times = {
        "1": 2.5,  # 小模型, 300 tokens
        "2": 10.0, # 大模型, 500 tokens
        "3": 3.0,  # 小模型, 400 tokens
        "4": 11.0  # 大模型, 600 tokens
    }
    
    max_workers = 2
    planner_time = 4.0
    
    print("\n=== 测试 simulate_task_execution 函数 ===")
    # 创建模拟配置对象
    class MockConfig:
        def __init__(self):
            self.router_model = "claude-3-5-sonnet-latest"
            self.small_model = "deepseek-chat"
            self.large_model = "gpt-4o"
            self.use_local_router = False
            self.local_router_model = "llama3-8b"
            self.threshold = 3
            
    mock_config = MockConfig()
    result = simulate_task_execution(sorted_tasks, dependency_graph, task_execution_times, max_workers, planner_time, mock_config)
    
    print(f"总执行时间: {result['total_time']:.3f}秒")
    print("任务时间线:")
    for step_id, timeline in result['task_timelines'].items():
        print(f"  步骤 {step_id}: 开始={timeline['start_time']:.3f}秒, 结束={timeline['end_time']:.3f}秒")
    
    print("工作线程分配:")
    for step_id, worker_id in result['worker_allocation'].items():
        print(f"  步骤 {step_id} 分配给工作线程 {worker_id}")
    
    # 预期结果:
    # 总执行时间: ~27.5秒
    # 任务时间线:
    #   步骤 1: 开始=4.000秒, 结束=6.500秒
    #   步骤 2: 开始=6.500秒, 结束=16.500秒 
    #   步骤 3: 开始=6.500秒, 结束=9.500秒  (与步骤2并行执行)
    #   步骤 4: 开始=16.500秒, 结束=27.500秒 (需等待步骤2和3都完成)
    # 
    # 工作线程分配:
    #   步骤 1 分配给工作线程 1
    #   步骤 2 分配给工作线程 1
    #   步骤 3 分配给工作线程 2
    #   步骤 4 分配给工作线程 1


def test_find_critical_path():
    """测试find_critical_path函数"""
    tasks = create_mock_tasks()
    sorted_tasks = sorted(tasks.items(), key=lambda x: int(x[0]))
    
    # 构建依赖图
    dependency_graph = {}
    for step_id, task in sorted_tasks:
        rely_str = task.get('Rely', '')
        dependencies = [dep for dep in rely_str.split(',') if dep]
        dependency_graph[step_id] = dependencies
    
    # 设置执行时间
    task_execution_times = {
        "1": 2.5,
        "2": 10.0,
        "3": 3.0,
        "4": 11.0
    }
    
    print("\n=== 测试 find_critical_path 函数 ===")
    critical_path = find_critical_path(sorted_tasks, dependency_graph, task_execution_times)
    
    print("关键路径:")
    print(" -> ".join(critical_path))
    print(f"关键路径总时间: {sum(task_execution_times[step_id] for step_id in critical_path):.3f}秒")
    
    # 预期结果:
    # 关键路径: 1 -> 2 -> 4
    # 关键路径总时间: 23.500秒
    # (因为步骤1 -> 步骤2 -> 步骤4是最长的执行路径)


def test_generate_theoretical_performance_report():
    """测试generate_theoretical_performance_report函数"""
    # 创建模拟数据
    tasks = create_mock_tasks()
    config = MockModelConfig()
    planner_output = create_mock_planner_output()
    
    print("\n=== 测试 generate_theoretical_performance_report 函数 ===")
    
    # 生成报告
    report = generate_theoretical_performance_report(tasks, config, planner_output)
    
    # 打印报告内容
    print(report)
    
    # 预期结果是一个包含多个部分的报告，包括:
    # - 模型性能参数
    # - 执行流程理论时间
    # - 任务类型理论时间
    # - 任务执行明细
    # - 理论执行甘特图
    # - 关键路径分析


def main():
    """运行所有测试"""
    test_get_model_performance()
    test_calculate_theoretical_time()
    test_simulate_task_execution()
    test_find_critical_path()
    test_generate_theoretical_performance_report()


if __name__ == "__main__":
    main()
