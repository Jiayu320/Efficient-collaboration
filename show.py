import time
import threading
import random
from queue import Queue
from rich import print
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

# ===== 系统配置 =====
PLAN_XML = """
<Plan>
<Step ID="1" Task="Identify key characteristics of the L-shaped tile and 2x5 rectangle" Difficulty="1" Token="30" Rely=""/>
<Step ID="2" Task="Determine possible rotations of the L-shaped tile (0°, 90°, 180°, 270°)" Difficulty="2" Token="40" Rely="1"/>
<Step ID="3" Task="Establish valid placement rules (tile must fit within rectangle boundaries)" Difficulty="2" Token="35" Rely="1"/>
<Step ID="4" Task="Map potential horizontal L-tile positions (original and 180° rotation)" Difficulty="3" Token="50" Rely="2,3"/>
<Step ID="5" Task="Map potential vertical L-tile positions (90° and 270° rotations)" Difficulty="3" Token="50" Rely="2,3"/>
<Step ID="6" Task="Combine all valid orientations and positions to form complete solution set" Difficulty="4" Token="60" Rely="4,5"/>
</Plan>
"""

SOLUTIONS = {
    1: "The L-shaped tile consists of 3 unit squares. The 2x5 rectangle contains 10 unit squares.",
    2: "The L-shaped tile can be rotated into four orientations:\n1. 0°: L-shape upright\n2. 90°: L-shape rotated clockwise\n3. 180°: L-shape upside down\n4. 270°: L-shape rotated counterclockwise",
    3: "Each of the L-shaped tile orientations must wholly fit within the 2x5 rectangle's boundaries.",
    4: "For horizontal placements:\n- Original (0°) at positions: top row columns 1-3, bottom row columns 1-2; ...\n- 180° rotation at positions: bottom row columns 1-3, top row columns 1-2; ...",
    5: "For vertical placements:\n- 90° rotation: Place the 2x2 part vertically with the arm extending to the side\n- 270° rotation: Same as 90° but flipped horizontally",
    6: "All valid placements:\n- Horizontal: 0°, 180° positions\n- Vertical: 90°, 270° positions\nTotal placements: 16"
}

# ===== 模型执行器类 =====
class ModelExecutor:
    def __init__(self, model_type):
        self.model_type = model_type
        self.work_queue = Queue()
        self.result_queue = Queue()
        self.worker = threading.Thread(target=self._process_queue, daemon=True)
        self.worker.start()
    
    def _process_queue(self):
        while True:
            step_id, task, difficulty = self.work_queue.get()
            # 模拟不同难度的处理时间
            process_time = 0.5 + difficulty * 0.3 + random.uniform(0, 0.5)
            
            # 创建进度条
            progress = Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True
            )
            task_id = progress.add_task(f"[cyan]Executing Step {step_id}...", total=100)
            
            # 模拟处理过程
            with progress:
                for i in range(100):
                    time.sleep(process_time / 100)
                    progress.update(task_id, advance=1)
            
            # 获取结果
            result = SOLUTIONS[step_id]
            self.result_queue.put((step_id, result))
            self.work_queue.task_done()

    def execute_step(self, step_id, task, difficulty):
        self.work_queue.put((step_id, task, difficulty))
        return f"Step {step_id} queued for {self.model_type} model"

# ===== 计划解析器 =====
def parse_plan(xml_string):
    steps = []
    lines = xml_string.strip().split("\n")[1:-1]  # 去掉首尾的<Plan>标签
    
    for line in lines:
        line = line.strip()
        if not line.startswith("<Step"):
            continue
            
        # 提取属性
        attrs = {}
        parts = line.split('"')
        for i in range(0, len(parts)-1, 2):
            key = parts[i].split()[-1].rstrip('=')
            value = parts[i+1].split()[0].rstrip('/>').rstrip('"')
            attrs[key] = value
        
        steps.append({
            "id": int(attrs["ID"]),
            "task": attrs["Task"],
            "difficulty": int(attrs["Difficulty"]),
            "token": int(attrs["Token"]),
            "rely": attrs.get("Rely", "").split(",") if "Rely" in attrs else []
        })
    
    return steps

# ===== 主演示函数 =====
def main_demo():
    console = Console()
    layout = Layout()
    
    # 创建布局分区
    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=7)
    )
    
    layout["main"].split_row(
        Layout(name="plan", ratio=2),
        Layout(name="execution", ratio=3)
    )
    
    # 初始化模型
    local_model = ModelExecutor("Local (Small)")
    cloud_model = ModelExecutor("Cloud (Large)")
    
    # 解析计划
    steps = parse_plan(PLAN_XML)
    
    # 准备显示内容
    plan_content = Text("", justify="left")
    execution_content = Text("", justify="left")
    completed_steps = set()
    results = {}
    
    # 创建状态表格
    status_table = Table(show_header=True, header_style="bold magenta")
    status_table.add_column("Step", width=6)
    status_table.add_column("Status", width=12)
    status_table.add_column("Model", width=12)
    status_table.add_column("Time", width=8)
    
    with Live(layout, refresh_per_second=10, screen=True):
        # 显示初始界面
        layout["header"].update(Panel("Plan-Driven Collaborative Execution System", 
                                     style="bold blue"))
        layout["plan"].update(Panel(plan_content, title="Execution Plan", 
                                  subtitle="XML Format", border_style="green"))
        layout["execution"].update(Panel(execution_content, title="Step Execution", 
                                       subtitle="Real-time Results", border_style="yellow"))
        layout["footer"].update(Panel(status_table, title="Execution Status", 
                                    border_style="cyan"))
        
        # 逐步显示计划
        for step in steps:
            # 添加当前步骤到计划显示
            step_xml = f'<Step ID="{step["id"]}" Task="{step["task"]}" Difficulty="{step["difficulty"]}" Token="{step["token"]}"'
            if step["rely"]:
                step_xml += f' Rely="{",".join(step["rely"])}"'
            step_xml += "/>"
            
            plan_content.append(step_xml + "\n", style="bold green")
            layout["plan"].update(Panel(plan_content, title="Execution Plan"))
            
            # 添加到状态表格
            status_table.add_row(
                str(step["id"]), 
                "[yellow]Queued", 
                "[cyan]Pending", 
                "0.0s"
            )
            layout["footer"].update(Panel(status_table, title="Execution Status"))
            
            # 根据难度选择模型
            if step["difficulty"] <= 2:
                model = local_model
                model_name = "Local"
                model_style = "green"
            else:
                model = cloud_model
                model_name = "Cloud"
                model_style = "blue"
            
            # 执行步骤
            model.execute_step(step["id"], step["task"], step["difficulty"])
            status_table.rows[step["id"]-1].cells[2] = f"[{model_style}]{model_name}"
            
            # 随机延迟，模拟流式效果
            time.sleep(0.8 + random.uniform(0, 0.5))
        
        # 监控执行进度
        start_times = {step["id"]: time.time() for step in steps}
        all_completed = False
        
        while not all_completed:
            # 检查本地模型结果
            while not local_model.result_queue.empty():
                step_id, result = local_model.result_queue.get()
                elapsed = time.time() - start_times[step_id]
                results[step_id] = result
                completed_steps.add(step_id)
                
                # 更新状态
                status_table.rows[step_id-1].cells[1] = "[green]Completed"
                status_table.rows[step_id-1].cells[3] = f"{elapsed:.1f}s"
                
                # 添加执行结果
                execution_content.append(f"\n[bold]Step {step_id} Result (Local Model):[/bold]\n", style="green")
                execution_content.append(result + "\n")
                layout["execution"].update(Panel(execution_content, title="Step Execution"))
            
            # 检查云端模型结果
            while not cloud_model.result_queue.empty():
                step_id, result = cloud_model.result_queue.get()
                elapsed = time.time() - start_times[step_id]
                results[step_id] = result
                completed_steps.add(step_id)
                
                # 更新状态
                status_table.rows[step_id-1].cells[1] = "[green]Completed"
                status_table.rows[step_id-1].cells[3] = f"{elapsed:.1f}s"
                
                # 添加执行结果
                execution_content.append(f"\n[bold]Step {step_id} Result (Cloud Model):[/bold]\n", style="blue")
                execution_content.append(result + "\n")
                layout["execution"].update(Panel(execution_content, title="Step Execution"))
            
            # 更新进行中的状态
            for i, row in enumerate(status_table.rows):
                step_id = i + 1
                if step_id not in completed_steps and status_table.rows[i].cells[1] == "[yellow]Queued":
                    elapsed = time.time() - start_times[step_id]
                    status_table.rows[i].cells[1] = "[cyan]Executing"
                    status_table.rows[i].cells[3] = f"{elapsed:.1f}s"
            
            layout["footer"].update(Panel(status_table, title="Execution Status"))
            
            # 检查是否全部完成
            all_completed = len(completed_steps) == len(steps)
            time.sleep(0.1)
        
        # 显示最终结果
        layout["header"].update(Panel("[bold green]✓ ALL STEPS COMPLETED SUCCESSFULLY", 
                                     style="bold green"))
        execution_content.append("\n[bold yellow]Final Answer:[/bold yellow] 16", style="bold yellow")
        layout["execution"].update(Panel(execution_content, title="Step Execution"))
        time.sleep(3)

# ===== 运行演示 =====
if __name__ == "__main__":
    main_demo()