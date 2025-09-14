# 问题 90 的理论性能分析报告

## 问题描述

The Last National Bank has just approved a loan at an interest rate of 6% for 90 days. If the interest charge on the loan is $36, how much is the principal of the loan?

A. $3000
B. $2600
C. $2200
D. $2800
E. $3200
F. $2000
G. $2100
H. $1800
I. $2500
J. $2400

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
| 规划阶段总时间 (Planner) | 3.056 | 100% |
| 规划过程中启动的任务数 | 4 / 5 | 80.0% |
| 规划与执行重叠的任务数 | 4 / 5 | 80.0% |
| 第一个任务规划完成时间 | 1.048 | - |
| 最后一个任务规划完成时间 | 3.014 | - |
| 最后一个任务执行完成时间 | 5.023 | - |
| 任务总执行时间(累计) | 5.775 | - |
| 流水线加速比 | 2.65x | - |
| 并行效率 | 115.0% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 5 | 5.775 | - |
| 规划模型 | 1 | 7.522 | - |
| 顺序总时间 | - | 13.297 | - |
| 并行总时间 | - | 5.023 | 2.65x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the formula to calculate interest based on principal, rate, and time? | 大模型 | 1.048 | 2.203 | 1.155 | 2 |
| 2 | What is the time period in years for 90 days? | 大模型 | 1.497 | 2.575 | 1.077 | 3 |
| 3 | What is the interest rate in a decimal form (6% ÷ 100)? | 大模型 | 2.017 | 3.017 | 1.000 | 4 |
| 4 | How can we rearrange the interest formula to solve for principal? | 大模型 | 2.480 | 3.713 | 1.232 | 5 |
| 5 | What is the principal amount using the given interest, rate, and time? | 大模型 | 3.713 | 5.023 | 1.310 | 6 |

## 理论执行甘特图

```
时间轴:
0                                                            3.97s
+------------------------------------------------------------+
步骤 1 |#################                                           | 1.05s - 2.20s
步骤 2 |      #################                                     | 1.50s - 2.57s
步骤 3 |              ###############                               | 2.02s - 3.02s
步骤 4 |                     ###################                    | 2.48s - 3.71s
步骤 5 |                                        ####################| 3.71s - 5.02s
```

