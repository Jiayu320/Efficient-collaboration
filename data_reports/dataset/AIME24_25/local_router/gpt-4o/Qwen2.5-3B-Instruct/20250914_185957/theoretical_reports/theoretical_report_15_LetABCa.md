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
| 规划过程中启动的任务数 | 5 / 7 | 71.4% |
| 规划与执行重叠的任务数 | 5 / 7 | 71.4% |
| 第一个任务规划完成时间 | 1.090 | - |
| 最后一个任务规划完成时间 | 4.475 | - |
| 最后一个任务执行完成时间 | 7.811 | - |
| 任务总执行时间(累计) | 7.798 | - |
| 流水线加速比 | 2.32x | - |
| 并行效率 | 99.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 5 | 5.775 | - |
| 大模型任务 | 2 | 2.024 | - |
| 规划模型 | 1 | 10.331 | - |
| 顺序总时间 | - | 18.130 | - |
| 并行总时间 | - | 7.811 | 2.32x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What are the coordinates of points A, B, C, and D on the hyperbola? | 小模型 | 1.090 | 2.555 | 1.465 | 2 |
| 2 | How do the coordinates of a rhombus relate to its diagonals intersecting at the origin? | 大模型 | 2.555 | 3.497 | 0.943 | 3 |
| 3 | What is the equation of the hyperbola and how does it constrain the coordinates of points on the hyperbola? | 小模型 | 2.228 | 3.305 | 1.077 | 4 |
| 4 | How can we express the length of diagonal BD in terms of the coordinates of points B and D? | 小模型 | 3.497 | 4.420 | 0.922 | 5 |
| 5 | How do we express BD² in terms of the hyperbola's parameters and the coordinates of B and D? | 小模型 | 4.420 | 5.730 | 1.310 | 6 |
| 6 | What is the maximum value of BD² given the constraint of the hyperbola? | 大模型 | 5.730 | 6.811 | 1.081 | 7 |
| 7 | What is the greatest real number less than BD² for all such rhombi? | 小模型 | 6.811 | 7.811 | 1.000 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            6.72s
+------------------------------------------------------------+
步骤 1 |#############                                               | 1.09s - 2.55s
步骤 3 |          #########                                         | 2.23s - 3.30s
步骤 2 |             ########                                       | 2.55s - 3.50s
步骤 4 |                     ########                               | 3.50s - 4.42s
步骤 5 |                             ############                   | 4.42s - 5.73s
步骤 6 |                                         ##########         | 5.73s - 6.81s
步骤 7 |                                                   #########| 6.81s - 7.81s
```

