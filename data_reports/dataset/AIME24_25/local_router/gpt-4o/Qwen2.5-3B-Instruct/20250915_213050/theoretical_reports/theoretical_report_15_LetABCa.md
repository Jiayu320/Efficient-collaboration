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
| 规划阶段总时间 (Planner) | 3.787 | 100% |
| 规划过程中启动的任务数 | 3 / 6 | 50.0% |
| 规划与执行重叠的任务数 | 3 / 6 | 50.0% |
| 第一个任务规划完成时间 | 1.076 | - |
| 最后一个任务规划完成时间 | 3.744 | - |
| 最后一个任务执行完成时间 | 7.629 | - |
| 任务总执行时间(累计) | 6.553 | - |
| 流水线加速比 | 2.03x | - |
| 并行效率 | 85.9% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 3 | 3.310 | - |
| 大模型任务 | 3 | 3.243 | - |
| 规划模型 | 1 | 8.927 | - |
| 顺序总时间 | - | 15.480 | - |
| 并行总时间 | - | 7.629 | 2.03x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What are the coordinates of points A and B given that they lie on the hyperbola? | 小模型 | 1.076 | 2.231 | 1.155 | 2 |
| 2 | What are the coordinates of points C and D given that they lie on the hyperbola and form a rhombus with A and B? | 大模型 | 2.231 | 3.243 | 1.012 | 3 |
| 3 | What is the formula for the length squared of diagonal BD in terms of coordinates? | 小模型 | 3.243 | 4.242 | 1.000 | 4 |
| 4 | How can we express BD² in terms of a parameter? | 大模型 | 4.242 | 5.324 | 1.081 | 5 |
| 5 | What is the maximum value of BD² for all possible rhombuses? | 大模型 | 5.324 | 6.474 | 1.150 | 6 |
| 6 | What is the greatest real number less than BD² for all such rhombi? | 小模型 | 6.474 | 7.629 | 1.155 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            6.55s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 1.08s - 2.23s
步骤 2 |          #########                                         | 2.23s - 3.24s
步骤 3 |                   #########                                | 3.24s - 4.24s
步骤 4 |                            ##########                      | 4.24s - 5.32s
步骤 5 |                                      ###########           | 5.32s - 6.47s
步骤 6 |                                                 ###########| 6.47s - 7.63s
```

