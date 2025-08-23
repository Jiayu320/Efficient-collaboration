from typing import Dict, Any, List, Tuple
import heapq

def get_model_performance(model_name: str) -> Dict[str, float]:
    """
    根据模型名称返回其性能指标（延迟和吞吐量）
    
    参数:
        model_name: 模型名称（字符串或包含模型名称的字符串）
    
    返回:
        包含输入和输出性能指标的字典 {'latency': float, 'throughput': float}
    """
    # 标准化模型名称为小写以便匹配
    model_name_lower = model_name.lower()
    
    # Claude模型性能
    if "claude-3-5" in model_name_lower or "claude-3.5" in model_name_lower or "claude-3-5-sonnet" in model_name_lower:
        return {"latency": 1.06, "throughput": 57.07}
    
    # OpenAI模型性能
    elif "gpt-4o" in model_name_lower:
        return {"latency": 0.61, "throughput": 58.71}
    
    # DeepSeek系列
    elif "deepseek-r1" in model_name_lower:
        return {"latency": 1.01, "throughput": 55.17}
    elif "deepseek-chat" in model_name_lower:
        return {"latency": 0.94, "throughput": 54.79}
    elif "deepseek-reasoner" in model_name_lower:
        return {"latency": 1.01, "throughput": 55.17}

    elif "llama3-8b" in model_name_lower or "llama-3-8b" in model_name_lower:
        return {"latency": 0.44, "throughput": 3422}
    # 本地模型
    elif "local" in model_name_lower:
        return {"latency": 0.5, "throughput": 100.0}

    # 默认性能（当无法识别模型时使用）
    else:
        print(f"警告: 未识别的模型 '{model_name}'，使用默认性能")
        return {"latency": 0.5, "throughput": 100.0}

def calculate_theoretical_time(model_name: str, tokens: int) -> Dict[str, float]:
    """
    根据模型性能指标和token数量计算理论时间
    
    参数:
        model_name: 模型名称
        tokens: 生成的token数量
    
    返回:
        包含各项时间指标的字典 {'latency': float, 'generation_time': float, 'total_time': float}
    """
    performance = get_model_performance(model_name)
    
    # 延迟时间（TTFT - Time To First Token）
    latency = performance["latency"]
    
    # 生成时间（根据吞吐量计算）
    generation_time = tokens / performance["throughput"] if tokens > 0 else 0
    
    # 总时间 = 延迟 + 生成时间
    total_time = latency + generation_time
    
    return {
        "latency": latency,
        "generation_time": generation_time,
        "total_time": total_time
    }

def generate_theoretical_performance_report(tasks, config, planner_output=None):
    """
    生成基于理论性能指标的报告
    
    参数:
        tasks: 任务字典
        config: 模型配置对象
        planner_output: planner实际输出的规划结果，包含token数量等信息，默认为None
    
    返回:
        理论性能报告文本
    """
    # 收集任务执行情况
    small_model_tasks = []
    large_model_tasks = []
    
    # 按执行顺序整理任务
    sorted_tasks = sorted(tasks.items(), key=lambda x: int(x[0]))
    
    # 遍历每个任务，根据难度分配到对应模型
    for step_id, task in sorted_tasks:
        # 提取token数量，默认为1000
        token_str = task.get('Token', '1000')
        try:
            tokens = int(token_str)
        except ValueError:
            tokens = 1000  # 默认值
            
        # 提取难度，根据难度选择模型
        difficulty = task.get('Difficulty', '0')
        
        # 创建任务信息
        task_info = {
            'step_id': step_id,
            'task': task.get('Task', f'步骤 {step_id}'),
            'tokens': tokens,
            'rely': task.get('Rely', '').split(',') if task.get('Rely', '') else []
        }
        
        # 根据难度判断使用哪个模型
        if int(difficulty) >= config.threshold:
            # 大模型任务
            large_model_tasks.append(task_info)
        else:
            # 小模型任务
            small_model_tasks.append(task_info)
    
    # 构建完整的任务依赖图
    dependency_graph = {}
    for step_id, task in sorted_tasks:
        rely_str = task.get('Rely', '')
        dependencies = [dep for dep in rely_str.split(',') if dep]  # 过滤空依赖
        dependency_graph[step_id] = dependencies
    
    # 获取模型名称
    small_model_name = config.small_model
    large_model_name = config.large_model
    router_model_name = config.router_model if not config.use_local_router else config.local_router_model
    
    # 计算规划阶段（Planner）的理论时间
    router_performance = get_model_performance(router_model_name)
    planner_latency = router_performance['latency']
    
    # 使用实际的planner输出token数量计算生成时间
    if planner_output and isinstance(planner_output, dict):
        # 如果提供了planner输出信息，使用实际的token计数
        plan_tokens = planner_output.get('completion_tokens', 0)
        if 'ttft' in planner_output and planner_output['ttft'] is not None:
            # 如果提供了实际的TTFT，直接使用
            planner_latency = planner_output['ttft']
            print(f"使用实际测量的planner延迟: {planner_latency:.3f}秒")
        
        print(f"使用实际的planner输出token数: {plan_tokens}")
    else:
        # 如果没有提供planner输出信息，基于任务数估算
        plan_tokens = len(tasks) * 100  # 每个任务约需100个token
        print(f"使用估算的planner输出token数: {plan_tokens}")
    
    # 计算路由模型的理论时间（初始化 + 生成计划）
    planner_generation_time = plan_tokens / router_performance['throughput']
    planner_total_time = planner_latency + planner_generation_time
    
    # 模拟任务执行的理论时间，考虑依赖关系和并行执行
    # 每个任务的开始时间和结束时间
    earliest_start_times = {}
    earliest_finish_times = {}
    
    # 任务的执行时间映射
    task_execution_times = {}
    for step_id, task in sorted_tasks:
        token_str = task.get('Token', '1000')
        try:
            tokens = int(token_str)
        except ValueError:
            tokens = 1000
            
        difficulty = task.get('Difficulty', '0')
        
        # 根据难度选择模型
        if int(difficulty) >= config.threshold:
            model_name = large_model_name
        else:
            model_name = small_model_name
            
        # 计算任务执行时间
        time_data = calculate_theoretical_time(model_name, tokens)
        task_execution_times[step_id] = time_data['total_time']
    
    # 计算任务的最早开始和完成时间，模拟真实调度过程
    max_workers = 4  # 默认并行工作线程数，可以从config中获取
    
    # 模拟任务执行过程
    simulation_result = simulate_task_execution(
        sorted_tasks, 
        dependency_graph, 
        task_execution_times, 
        max_workers, 
        planner_total_time
    )
    
    total_execution_time = simulation_result['total_time']
    task_timelines = simulation_result['task_timelines']
    worker_allocation = simulation_result['worker_allocation']
    
    # 计算各模型的理论时间总和（不考虑并行）
    small_model_theoretical_time = sum(
        task_execution_times[task['step_id']] for task in small_model_tasks
    )
    
    large_model_theoretical_time = sum(
        task_execution_times[task['step_id']] for task in large_model_tasks
    )
    
    # 构建报告
    report = "# 理论性能模型分析\n\n"
    
    # 添加模型性能参数
    small_perf = get_model_performance(small_model_name)
    large_perf = get_model_performance(large_model_name)
    router_perf = get_model_performance(router_model_name)
    
    report += "## 模型性能参数\n\n"
    report += "| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |\n"
    report += "| --- | --- | --- |\n"
    report += f"| 小模型 ({small_model_name}) | {small_perf['latency']:.3f} | {small_perf['throughput']:.2f} |\n"
    report += f"| 大模型 ({large_model_name}) | {large_perf['latency']:.3f} | {large_perf['throughput']:.2f} |\n"
    report += f"| 路由模型 ({router_model_name}) | {router_perf['latency']:.3f} | {router_perf['throughput']:.2f} |\n\n"
    
    # 添加执行流程理论时间
    report += "## 执行流程理论时间\n\n"
    report += "| 阶段 | 理论时间 (秒) | 百分比 |\n"
    report += "| --- | --- | --- |\n"
    report += f"| 规划阶段 (Planner) | {planner_total_time:.3f} | {(planner_total_time/total_execution_time)*100:.1f}% |\n"
    report += f"| 任务执行阶段 | {total_execution_time - planner_total_time:.3f} | {((total_execution_time - planner_total_time)/total_execution_time)*100:.1f}% |\n"
    report += f"| 总执行时间 | {total_execution_time:.3f} | 100% |\n\n"
    
    # 添加任务类型理论时间
    report += "## 任务类型理论时间\n\n"
    report += "| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |\n"
    report += "| --- | --- | --- | --- |\n"
    
    # 计算并行加速比
    sequential_time = planner_total_time + small_model_theoretical_time + large_model_theoretical_time
    parallel_speedup = sequential_time / total_execution_time if total_execution_time > 0 else 1.0
    
    report += f"| 小模型任务 | {len(small_model_tasks)} | {small_model_theoretical_time:.3f} | - |\n"
    report += f"| 大模型任务 | {len(large_model_tasks)} | {large_model_theoretical_time:.3f} | - |\n"
    report += f"| 规划模型 | 1 | {planner_total_time:.3f} | - |\n"
    report += f"| 顺序总时间 | - | {sequential_time:.3f} | - |\n"
    report += f"| 并行总时间 | - | {total_execution_time:.3f} | {parallel_speedup:.2f}x |\n\n"
    
    # 添加任务明细
    report += "## 任务执行明细\n\n"
    report += "| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |\n"
    report += "| --- | --- | --- | --- | --- | --- | --- |\n"
    
    for step_id, task in sorted_tasks:
        task_desc = task.get('Task', f'步骤 {step_id}')
        difficulty = task.get('Difficulty', '0')
        
        # 根据难度判断使用哪个模型
        if int(difficulty) >= config.threshold:
            model_type = "大模型"
        else:
            model_type = "小模型"
            
        start_time = task_timelines[step_id]['start_time']
        end_time = task_timelines[step_id]['end_time']
        duration = end_time - start_time
        worker_id = worker_allocation.get(step_id, "N/A")
        
        report += f"| {step_id} | {task_desc} | {model_type} | {start_time:.3f} | {end_time:.3f} | {duration:.3f} | {worker_id} |\n"
    
    # 添加理论执行甘特图描述
    report += "\n## 理论执行甘特图\n\n"
    report += "```\n"
    report += generate_gantt_chart(task_timelines, max_workers)
    report += "```\n\n"
    
    # 添加关键路径分析
    critical_path = find_critical_path(sorted_tasks, dependency_graph, task_execution_times)
    
    report += "## 关键路径分析\n\n"
    report += "关键路径是决定总执行时间的最长任务链。以下是本次执行的关键路径：\n\n"
    
    if critical_path:
        report += "| 步骤 | 任务描述 | 执行时间 (秒) |\n"
        report += "| --- | --- | --- |\n"
        
        for step_id in critical_path:
            for original_step_id, task in sorted_tasks:
                if original_step_id == step_id:
                    task_desc = task.get('Task', f'步骤 {step_id}')
                    report += f"| {step_id} | {task_desc} | {task_execution_times[step_id]:.3f} |\n"
                    break
                    
        report += f"\n关键路径总时间: {sum(task_execution_times[step_id] for step_id in critical_path):.3f} 秒\n"
    else:
        report += "无法确定关键路径。\n"
        
    return report

def simulate_task_execution(sorted_tasks, dependency_graph, task_execution_times, max_workers, planner_time):
    """
    模拟并行任务执行，考虑依赖关系和工作线程数限制
    
    参数:
        sorted_tasks: 按ID排序的任务
        dependency_graph: 任务依赖关系图
        task_execution_times: 每个任务的执行时间
        max_workers: 最大并行工作线程数
        planner_time: 规划阶段的时间
        
    返回:
        包含总执行时间和任务时间线的字典
    """
    # 待处理任务队列
    pending_tasks = set([step_id for step_id, _ in sorted_tasks])
    
    # 正在执行的任务
    running_tasks = {}  # step_id -> (start_time, end_time)
    
    # 已完成任务
    completed_tasks = set()
    
    # 记录每个任务的开始时间和结束时间
    task_timelines = {}
    
    # 工作线程分配情况
    worker_allocation = {}  # step_id -> worker_id
    
    # 当前时间（从规划结束时开始）
    current_time = planner_time
    
    # 工作线程状态，初始全部空闲
    workers = [{"id": i+1, "busy_until": 0} for i in range(max_workers)]
    
    # 模拟执行过程
    while pending_tasks or running_tasks:
        # 1. 检查已完成的任务
        newly_completed = []
        for step_id, (start_time, end_time) in list(running_tasks.items()):
            if end_time <= current_time:
                completed_tasks.add(step_id)
                newly_completed.append(step_id)
                del running_tasks[step_id]
        
        # 2. 找出可以开始的任务
        ready_tasks = []
        for step_id in pending_tasks:
            dependencies = dependency_graph.get(step_id, [])
            if all(dep in completed_tasks for dep in dependencies if dep):
                # 计算任务优先级（依赖数量越少优先级越高）
                priority = (len(dependencies), int(step_id))
                ready_tasks.append((priority, step_id))
        
        # 按优先级排序
        ready_tasks.sort()
        
        # 3. 分配任务到空闲的工作线程
        available_workers = [w for w in workers if w["busy_until"] <= current_time]
        
        tasks_to_start = min(len(ready_tasks), len(available_workers))
        
        if tasks_to_start > 0:
            for i in range(tasks_to_start):
                _, step_id = ready_tasks[i]
                worker = available_workers[i]
                
                # 获取任务执行时间
                execution_time = task_execution_times[step_id]
                
                # 更新工作线程状态
                worker["busy_until"] = current_time + execution_time
                
                # 记录任务时间线
                task_timelines[step_id] = {
                    "start_time": current_time,
                    "end_time": current_time + execution_time
                }
                
                # 记录任务与工作线程的分配关系
                worker_allocation[step_id] = worker["id"]
                
                # 将任务从待处理移到正在执行
                pending_tasks.remove(step_id)
                running_tasks[step_id] = (current_time, current_time + execution_time)
        
        # 4. 如果没有任务可以开始或没有空闲工作线程，向前推进时间
        if not pending_tasks or not running_tasks:
            # 所有任务已完成
            if not running_tasks:
                break
                
            # 向前推进到下一个任务完成的时间
            next_completion_time = min(end_time for _, end_time in running_tasks.values())
            current_time = next_completion_time
        else:
            # 有任务在运行，找出下一个可能的事件时间点
            next_event_times = []
            
            # 下一个任务完成的时间
            if running_tasks:
                next_event_times.append(min(end_time for _, end_time in running_tasks.values()))
                
            # 下一个工作线程空闲的时间
            if len(ready_tasks) > len(available_workers):  # 还有等待分配的任务
                busy_workers = [w for w in workers if w["busy_until"] > current_time]
                if busy_workers:
                    next_event_times.append(min(w["busy_until"] for w in busy_workers))
            
            # 移动到下一个事件时间点
            if next_event_times:
                current_time = min(next_event_times)
            else:
                # 如果没有下一个事件点，说明所有任务都在等待依赖完成
                # 这种情况通常表示存在循环依赖，但为了避免死锁，我们稍微推进时间
                current_time += 0.001
    
    # 总执行时间
    total_time = max(timeline["end_time"] for timeline in task_timelines.values()) if task_timelines else planner_time
    
    return {
        "total_time": total_time,
        "task_timelines": task_timelines,
        "worker_allocation": worker_allocation
    }

def generate_gantt_chart(task_timelines, max_workers, width=80):
    """
    生成简单的ASCII甘特图
    
    参数:
        task_timelines: 任务时间线
        max_workers: 最大工作线程数
        width: 图表宽度
        
    返回:
        ASCII甘特图文本
    """
    if not task_timelines:
        return "没有任务执行数据可供显示。"
    
    # 确定时间范围
    start_time = min(data["start_time"] for data in task_timelines.values())
    end_time = max(data["end_time"] for data in task_timelines.values())
    time_range = end_time - start_time
    
    # 每个字符表示的时间
    time_per_char = time_range / (width - 20)
    
    # 生成时间轴
    gantt = "时间轴:\n"
    gantt += "0" + " " * (width - 20) + f"{time_range:.2f}s\n"
    gantt += "+" + "-" * (width - 20) + "+\n"
    
    # 生成任务条
    sorted_tasks = sorted(task_timelines.items(), key=lambda x: x[1]["start_time"])
    
    for step_id, data in sorted_tasks:
        rel_start = data["start_time"] - start_time
        rel_end = data["end_time"] - start_time
        
        start_pos = int(rel_start / time_per_char)
        end_pos = int(rel_end / time_per_char)
        
        # 确保每个任务至少显示一个字符
        if start_pos == end_pos:
            end_pos = start_pos + 1
            
        # 限制在图表范围内
        end_pos = min(end_pos, width - 20)
        
        # 构建任务条
        task_bar = " " * start_pos + "#" * (end_pos - start_pos)
        
        # 确保任务条不超过图表宽度
        task_bar = task_bar.ljust(width - 20)
        
        # 添加任务信息
        gantt += f"步骤 {step_id} |{task_bar}| {data['start_time']:.2f}s - {data['end_time']:.2f}s\n"
    
    return gantt

def find_critical_path(sorted_tasks, dependency_graph, task_execution_times):
    """
    找出任务依赖图中的关键路径
    
    参数:
        sorted_tasks: 按ID排序的任务
        dependency_graph: 任务依赖关系图
        task_execution_times: 每个任务的执行时间
        
    返回:
        关键路径上的任务ID列表
    """
    # 拓扑排序
    topo_order = []
    visited = set()
    temp_visited = set()
    
    def dfs(node):
        if node in temp_visited:
            # 检测到循环依赖
            return False
        if node in visited:
            return True
        
        temp_visited.add(node)
        
        # 访问所有依赖
        dependencies = dependency_graph.get(node, [])
        for dep in dependencies:
            if dep and not dfs(dep):
                return False
                
        temp_visited.remove(node)
        visited.add(node)
        topo_order.append(node)
        return True
    
    # 对每个任务执行DFS
    for step_id, _ in sorted_tasks:
        if step_id not in visited:
            if not dfs(step_id):
                # 存在循环依赖，无法确定关键路径
                return []
    
    # 反转拓扑序，从源节点开始
    topo_order.reverse()
    
    # 计算每个节点的最早完成时间和前驱节点
    earliest_finish = {}
    predecessor = {}
    
    for node in topo_order:
        # 获取所有前驱节点的最早完成时间
        max_finish_time = 0
        max_predecessor = None
        
        dependencies = dependency_graph.get(node, [])
        for dep in dependencies:
            if dep and dep in earliest_finish:
                finish_time = earliest_finish[dep]
                if finish_time > max_finish_time:
                    max_finish_time = finish_time
                    max_predecessor = dep
        
        # 计算当前节点的最早完成时间
        earliest_finish[node] = max_finish_time + task_execution_times.get(node, 0)
        predecessor[node] = max_predecessor
    
    # 找出最晚完成的节点
    end_nodes = [node for node in topo_order if not any(node in dependency_graph.get(next_node, []) for next_node, _ in sorted_tasks)]
    
    if not end_nodes:
        # 如果没有终止节点，取所有节点中完成时间最晚的
        max_finish_node = max(earliest_finish.items(), key=lambda x: x[1])[0]
    else:
        # 在终止节点中找出完成时间最晚的
        max_finish_node = max(end_nodes, key=lambda x: earliest_finish.get(x, 0))
    
    # 回溯构建关键路径
    critical_path = []
    current = max_finish_node
    
    while current:
        critical_path.append(current)
        current = predecessor.get(current)
    
    # 反转路径，从开始到结束
    critical_path.reverse()
    
    return critical_path

def calculate_critical_path_time(sorted_tasks, dependency_graph, small_model_name, large_model_name, config):
    """
    计算任务依赖图中的关键路径时间
    
    参数:
        sorted_tasks: 按ID排序的任务
        dependency_graph: 任务依赖关系图
        small_model_name: 小模型名称
        large_model_name: 大模型名称
        config: 模型配置
    
    返回:
        关键路径的理论时间
    """
    # 计算每个任务的最早完成时间
    earliest_finish_time = {}
    
    # 按拓扑顺序遍历任务
    for step_id, task in sorted_tasks:
        # 提取token数量
        token_str = task.get('Token', '1000')
        try:
            tokens = int(token_str)
        except ValueError:
            tokens = 1000
            
        # 判断使用哪个模型
        difficulty = task.get('Difficulty', '0')
        model_name = large_model_name if int(difficulty) >= config.threshold else small_model_name
        
        # 计算该任务的理论时间
        time_data = calculate_theoretical_time(model_name, tokens)
        task_time = time_data['total_time']
        
        # 计算该任务的最早开始时间（取决于其所有依赖任务的完成时间）
        dependencies = dependency_graph[step_id]
        earliest_start = 0
        if dependencies and dependencies != ['']:
            earliest_start = max([earliest_finish_time.get(dep, 0) for dep in dependencies if dep])
        
        # 该任务的最早完成时间 = 最早开始时间 + 任务时间
        earliest_finish_time[step_id] = earliest_start + task_time
    
    # 关键路径时间是所有任务中的最晚完成时间
    if earliest_finish_time:
        return max(earliest_finish_time.values())
    else:
        return 0