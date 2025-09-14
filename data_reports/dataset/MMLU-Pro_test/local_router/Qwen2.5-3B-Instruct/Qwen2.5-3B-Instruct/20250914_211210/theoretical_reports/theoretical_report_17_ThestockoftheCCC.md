# 问题 17 的理论性能分析报告

## 问题描述

The stock of the CCC Corporation is currently valued at $12 and is assumed to possess all the properties of geometric Brownian motion. It has an expected annual return of 15%, an annual volatility of 20%, and the annual risk-free is 10%. Using a binomial lattice, determine the price of a call option on CCC stock maturing in 10 monthes time with a strike price of $14 (Let the distance between nodes on your tree be 1 month in length).

A. 50.0
B. 60.0
C. 55.0
D. 44.0
E. 48.0
F. 53.0
G. 42.0
H. 46.0
I. 51.0
J. 45.0

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 大模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 4.531 | 100% |
| 规划过程中启动的任务数 | 5 / 8 | 62.5% |
| 规划与执行重叠的任务数 | 5 / 8 | 62.5% |
| 第一个任务规划完成时间 | 0.978 | - |
| 最后一个任务规划完成时间 | 4.489 | - |
| 最后一个任务执行完成时间 | 8.551 | - |
| 任务总执行时间(累计) | 9.472 | - |
| 流水线加速比 | 2.48x | - |
| 并行效率 | 110.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 8 | 9.472 | - |
| 规划模型 | 1 | 11.736 | - |
| 顺序总时间 | - | 21.208 | - |
| 并行总时间 | - | 8.551 | 2.48x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the risk-neutral probability for a binomial model? | 大模型 | 0.978 | 2.132 | 1.155 | 2 |
| 2 | How many nodes are needed for a 10-month time period with 1-month intervals? | 大模型 | 1.511 | 2.589 | 1.077 | 3 |
| 3 | What is the up factor for the stock price in the binomial model? | 大模型 | 1.989 | 3.144 | 1.155 | 4 |
| 4 | What is the down factor for the stock price in the binomial model? | 大模型 | 2.466 | 3.621 | 1.155 | 5 |
| 5 | What is the price of the stock at each node in the binomial lattice? | 大模型 | 3.621 | 4.931 | 1.310 | 6 |
| 6 | What is the payoff of the call option at each node in the binomial lattice? | 大模型 | 4.931 | 6.163 | 1.232 | 7 |
| 7 | How do we work backwards to find the option price at the initial node? | 大模型 | 6.163 | 7.473 | 1.310 | 8 |
| 8 | What is the final price of the call option? | 大模型 | 7.473 | 8.551 | 1.077 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            7.57s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 0.98s - 2.13s
步骤 2 |    ########                                                | 1.51s - 2.59s
步骤 3 |        #########                                           | 1.99s - 3.14s
步骤 4 |           #########                                        | 2.47s - 3.62s
步骤 5 |                    ###########                             | 3.62s - 4.93s
步骤 6 |                               ##########                   | 4.93s - 6.16s
步骤 7 |                                         ##########         | 6.16s - 7.47s
步骤 8 |                                                   ######## | 7.47s - 8.55s
```

