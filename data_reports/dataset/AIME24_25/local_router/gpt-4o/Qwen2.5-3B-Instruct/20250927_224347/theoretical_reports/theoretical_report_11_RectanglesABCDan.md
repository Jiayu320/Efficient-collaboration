# 问题 11 的理论性能分析报告

## 问题描述

Rectangles $ABCD$ and $EFGH$ are drawn such that $D,E,C,F$ are collinear. Also, $A,D,H,G$ all lie on a circle. If $BC=16$,$AB=107$,$FG=17$, and $EF=184$, what is the length of $CE$?

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-4B-Thinking/full/ep3) | 0.690 | 184.10 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 2.444 | 100% |
| 规划过程中启动的任务数 | 2 / 6 | 33.3% |
| 规划与执行重叠的任务数 | 2 / 6 | 33.3% |
| 第一个任务规划完成时间 | 1.010 | - |
| 最后一个任务规划完成时间 | 2.428 | - |
| 最后一个任务执行完成时间 | 7.852 | - |
| 任务总执行时间(累计) | 6.841 | - |
| 流水线加速比 | 1.84x | - |
| 并行效率 | 87.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 2.310 | - |
| 大模型任务 | 4 | 4.532 | - |
| 规划模型 | 1 | 7.594 | - |
| 顺序总时间 | - | 14.435 | - |
| 并行总时间 | - | 7.852 | 1.84x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What are the coordinates of points A, B, C, D for rectangle ABCD with D at (0, 0), BC = 16, and AB = 107? | 小模型 | 1.010 | 2.320 | 1.310 | 2 |
| 2 | Given D, E, C are collinear, what is the y-coordinate of E, and what is the general form of E's coordinates? | 小模型 | 2.320 | 3.320 | 1.000 | 3 |
| 3 | Using FG = 17 and EF = 184, what are the coordinates of H and G in terms of E's x-coordinate x? | 大模型 | 3.320 | 4.401 | 1.081 | 4 |
| 4 | What is the slope of AH, and what condition must x satisfy for AH to be perpendicular to DG? | 大模型 | 4.401 | 5.552 | 1.150 | 5 |
| 5 | Using the circle equation through A, D, H, G, what simplified linear equation in x is derived from expanding (x - 107)² + x² = 107² + (x - 17)²? | 大模型 | 5.552 | 6.771 | 1.219 | 6 |
| 6 | Solve the linear equation from Step 5 for x, then compute CE = |x - 16|. What is the final value of CE? | 大模型 | 6.771 | 7.852 | 1.081 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            6.84s
+------------------------------------------------------------+
步骤 1 |###########                                                 | 1.01s - 2.32s
步骤 2 |           #########                                        | 2.32s - 3.32s
步骤 3 |                    #########                               | 3.32s - 4.40s
步骤 4 |                             ##########                     | 4.40s - 5.55s
步骤 5 |                                       ###########          | 5.55s - 6.77s
步骤 6 |                                                  ##########| 6.77s - 7.85s
```

