# 问题 15 的理论性能分析报告

## 问题描述

Let $A$, $B$, $C$, and $D$ be point on the hyperbola $\frac{x^2}{20}- \frac{y^2}{24} = 1$ such that $ABCD$ is a rhombus whose diagonals intersect at the origin. Find the greatest real number that is less than $BD^2$ for all such rhombi.

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 4.517 | 100% |
| 规划过程中启动的任务数 | 6 / 8 | 75.0% |
| 规划与执行重叠的任务数 | 6 / 8 | 75.0% |
| 第一个任务规划完成时间 | 1.020 | - |
| 最后一个任务规划完成时间 | 4.475 | - |
| 最后一个任务执行完成时间 | 7.783 | - |
| 任务总执行时间(累计) | 8.775 | - |
| 流水线加速比 | 2.64x | - |
| 并行效率 | 112.7% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.000 | - |
| 大模型任务 | 7 | 7.775 | - |
| 规划模型 | 1 | 11.736 | - |
| 顺序总时间 | - | 20.511 | - |
| 并行总时间 | - | 7.783 | 2.64x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What are the coordinates of points A and B on the hyperbola? | 大模型 | 1.020 | 2.101 | 1.081 | 2 |
| 2 | What are the coordinates of points C and D on the hyperbola? | 大模型 | 2.101 | 3.182 | 1.081 | 3 |
| 3 | What is the equation of the hyperbola in terms of x and y? | 小模型 | 2.003 | 3.003 | 1.000 | 4 |
| 4 | How do the diagonals of the rhombus relate to the hyperbola? | 大模型 | 3.182 | 4.332 | 1.150 | 5 |
| 5 | What is the formula for BD² in terms of the coordinates? | 大模型 | 3.182 | 4.194 | 1.012 | 6 |
| 6 | How can we express BD² in terms of a parameter? | 大模型 | 4.332 | 5.551 | 1.219 | 7 |
| 7 | What is the maximum value of BD²? | 大模型 | 5.551 | 6.702 | 1.150 | 8 |
| 8 | What is the greatest real number less than BD² for all such rhombi? | 大模型 | 6.702 | 7.783 | 1.081 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            6.76s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 1.02s - 2.10s
步骤 3 |        #########                                           | 2.00s - 3.00s
步骤 2 |         ##########                                         | 2.10s - 3.18s
步骤 4 |                   ##########                               | 3.18s - 4.33s
步骤 5 |                   #########                                | 3.18s - 4.19s
步骤 6 |                             ###########                    | 4.33s - 5.55s
步骤 7 |                                        ##########          | 5.55s - 6.70s
步骤 8 |                                                  ##########| 6.70s - 7.78s
```

