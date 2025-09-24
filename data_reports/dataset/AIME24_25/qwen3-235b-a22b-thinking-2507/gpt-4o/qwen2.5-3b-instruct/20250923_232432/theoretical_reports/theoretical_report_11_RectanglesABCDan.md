# 问题 11 的理论性能分析报告

## 问题描述

Rectangles $ABCD$ and $EFGH$ are drawn such that $D,E,C,F$ are collinear. Also, $A,D,H,G$ all lie on a circle. If $BC=16$,$AB=107$,$FG=17$, and $EF=184$, what is the length of $CE$?

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (qwen3-235b-a22b-thinking-2507) | 0.825 | 70.53 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 5.958 | 100% |
| 规划过程中启动的任务数 | 4 / 6 | 66.7% |
| 规划与执行重叠的任务数 | 4 / 6 | 66.7% |
| 第一个任务规划完成时间 | 1.888 | - |
| 最后一个任务规划完成时间 | 5.915 | - |
| 最后一个任务执行完成时间 | 8.474 | - |
| 任务总执行时间(累计) | 7.204 | - |
| 流水线加速比 | 2.59x | - |
| 并行效率 | 85.0% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 2.465 | - |
| 大模型任务 | 4 | 4.739 | - |
| 规划模型 | 1 | 14.777 | - |
| 顺序总时间 | - | 21.981 | - |
| 并行总时间 | - | 8.474 | 2.59x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Assign coordinates: Let D=(0,0), C=(107,0), A=(0,16), B=(107,16). What are the coordinates of E and F on the x-axis, given EF=184 and order D-E-C-F? | 小模型 | 1.888 | 3.198 | 1.310 | 2 |
| 2 | Assuming EFGH is oriented downward, what are the coordinates of G and H in terms of E=(e,0) and F=(f,0), given FG=17? | 大模型 | 3.198 | 4.279 | 1.081 | 3 |
| 3 | Using the circle equation x² + y² + Dx + Ey + F = 0, substitute D=(0,0) and A=(0,16) to find E=-16. What is the simplified circle equation? | 大模型 | 3.661 | 4.811 | 1.150 | 4 |
| 4 | Substitute H=(e,-17) and G=(f,-17) into the circle equation from Step 3. What equation relates e and f? | 大模型 | 4.811 | 6.030 | 1.219 | 5 |
| 5 | Given f = e + 184 (from EF=184) and ef = 561 (from Step 4), solve for e. What is the positive solution for e? | 大模型 | 6.030 | 7.319 | 1.289 | 6 |
| 6 | Compute CE = 107 - e using the value of e from Step 5. What is the final length of CE? | 小模型 | 7.319 | 8.474 | 1.155 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            6.59s
+------------------------------------------------------------+
步骤 1 |###########                                                 | 1.89s - 3.20s
步骤 2 |           ##########                                       | 3.20s - 4.28s
步骤 3 |                ##########                                  | 3.66s - 4.81s
步骤 4 |                          ###########                       | 4.81s - 6.03s
步骤 5 |                                     ############           | 6.03s - 7.32s
步骤 6 |                                                 ###########| 7.32s - 8.47s
```

