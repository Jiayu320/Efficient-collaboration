# 问题 11 的理论性能分析报告

## 问题描述

Rectangles $ABCD$ and $EFGH$ are drawn such that $D,E,C,F$ are collinear. Also, $A,D,H,G$ all lie on a circle. If $BC=16$,$AB=107$,$FG=17$, and $EF=184$, what is the length of $CE$?

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-4B-Thinking/full/ep5) | 0.690 | 184.10 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 2.135 | 100% |
| 规划过程中启动的任务数 | 1 / 5 | 20.0% |
| 规划与执行重叠的任务数 | 1 / 5 | 20.0% |
| 第一个任务规划完成时间 | 0.983 | - |
| 最后一个任务规划完成时间 | 2.119 | - |
| 最后一个任务执行完成时间 | 5.813 | - |
| 任务总执行时间(累计) | 5.980 | - |
| 流水线加速比 | 2.34x | - |
| 并行效率 | 102.9% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.310 | - |
| 大模型任务 | 4 | 4.670 | - |
| 规划模型 | 1 | 7.599 | - |
| 顺序总时间 | - | 13.579 | - |
| 并行总时间 | - | 5.813 | 2.34x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What are the coordinates of points D, E, C, F on a horizontal line, expressed in terms of parameters d, e, c, f? | 小模型 | 0.983 | 2.293 | 1.310 | 2 |
| 2 | Using the circle equation through A, D, H, G, what are the expressions for x_H and y_H in terms of c and d? | 大模型 | 2.293 | 3.443 | 1.150 | 3 |
| 3 | Applying the Pythagorean theorem to rectangle ABCD, what is the equation relating c, d, e from AH² = AB² + BH²? | 大模型 | 3.443 | 4.594 | 1.150 | 4 |
| 4 | Applying the Pythagorean theorem to rectangle EFGH, what is the equation relating c, d, e from GH² = FG² + BG²? | 大模型 | 3.443 | 4.594 | 1.150 | 5 |
| 5 | Subtracting the equations from Steps 3 and 4, solving for c, and using the result from Step 3, what is the value of CE = c - e? | 大模型 | 4.594 | 5.813 | 1.219 | 6 |

## 理论执行甘特图

```
时间轴:
0                                                            4.83s
+------------------------------------------------------------+
步骤 1 |################                                            | 0.98s - 2.29s
步骤 2 |                ##############                              | 2.29s - 3.44s
步骤 3 |                              ##############                | 3.44s - 4.59s
步骤 4 |                              ##############                | 3.44s - 4.59s
步骤 5 |                                            ################| 4.59s - 5.81s
```

