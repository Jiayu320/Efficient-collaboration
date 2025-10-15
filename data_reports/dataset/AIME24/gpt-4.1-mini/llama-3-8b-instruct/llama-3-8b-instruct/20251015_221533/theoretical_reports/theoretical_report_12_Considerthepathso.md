# 问题 12 的理论性能分析报告

## 问题描述

Consider the paths of length $16$ that follow the lines from the lower left corner to the upper right corner on an $8\times 8$ grid. Find the number of such paths that change direction exactly four times, as in the examples shown below.

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (meta-llama/llama-3-8b-instruct) | 0.645 | 86.95 |
| 大模型 (meta-llama/llama-3-8b-instruct) | 0.645 | 86.95 |
| 路由模型 (gpt-4.1-mini) | 0.700 | 69.59 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 8.474 | 100% |
| 规划过程中启动的任务数 | 6 / 7 | 85.7% |
| 规划与执行重叠的任务数 | 6 / 7 | 85.7% |
| 第一个任务规划完成时间 | 1.878 | - |
| 最后一个任务规划完成时间 | 8.431 | - |
| 最后一个任务执行完成时间 | 9.979 | - |
| 任务总执行时间(累计) | 7.160 | - |
| 流水线加速比 | 1.57x | - |
| 并行效率 | 71.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 6 | 5.940 | - |
| 大模型任务 | 1 | 1.220 | - |
| 规划模型 | 1 | 8.488 | - |
| 顺序总时间 | - | 15.649 | - |
| 并行总时间 | - | 9.979 | 1.57x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Represent each path from the lower left to the upper right corner on an 8x8 grid as a sequence of 16 moves, each move being either right (R) or up (U), with exactly 8 Rs and 8 Us. What is the total number of such sequences? | 小模型 | 1.878 | 2.868 | 0.990 | 2 |
| 2 | Define a direction change as a change from R to U or from U to R in the sequence. Given that a path changes direction exactly 4 times, how many runs (maximal consecutive segments of the same direction) are there in the 16-move sequence? (Hint: Number of runs = direction changes + 1) | 小模型 | 3.143 | 4.133 | 0.990 | 3 |
| 3 | Since there are 4 direction changes, the path has 5 runs alternating between R and U. List the two possible patterns of run directions starting with R or U. | 小模型 | 4.133 | 5.123 | 0.990 | 4 |
| 4 | Let the lengths of the 5 runs be (r1, r2, r3, r4, r5) where runs alternate directions (e.g., R,U,R,U,R) or (U,R,U,R,U). Each run length is a positive integer. Using the condition that the total number of Rs is 8 and the total number of Us is 8, write the system of equations for run lengths for each pattern. | 小模型 | 5.514 | 6.619 | 1.105 | 5 |
| 5 | For each pattern, calculate the number of positive integer solutions to the system where sum of R-run lengths = 8 and sum of U-run lengths = 8. Use the formula for compositions: number of positive integer solutions to x1 + x2 + ... + xk = n is C(n-1, k-1). What are these numbers for each pattern? | 大模型 | 6.893 | 8.113 | 1.220 | 6 |
| 6 | For each solution (run length distribution), the corresponding path sequences are uniquely determined. Calculate the total number of such sequences by summing the counts from each pattern. | 小模型 | 8.113 | 9.104 | 0.990 | 7 |
| 7 | Output the total number of paths of length 16 with exactly 4 direction changes from the lower left corner to the upper right corner on the 8x8 grid. | 小模型 | 9.104 | 9.979 | 0.875 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            8.10s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 1.88s - 2.87s
步骤 2 |         #######                                            | 3.14s - 4.13s
步骤 3 |                ########                                    | 4.13s - 5.12s
步骤 4 |                          #########                         | 5.51s - 6.62s
步骤 5 |                                     #########              | 6.89s - 8.11s
步骤 6 |                                              #######       | 8.11s - 9.10s
步骤 7 |                                                     ###### | 9.10s - 9.98s
```

