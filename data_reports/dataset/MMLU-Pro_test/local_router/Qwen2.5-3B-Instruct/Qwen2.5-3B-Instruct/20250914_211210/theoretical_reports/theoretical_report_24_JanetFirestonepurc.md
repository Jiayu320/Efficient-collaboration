# 问题 24 的理论性能分析报告

## 问题描述

Janet Firestone purchased an option on a stock for $175 giving her the right to buy 100 shares at 14(1/2) within 90 days. One month later, she exercised her option and then sold the stock on the same day for 17. What was her profit on the stock?

A. $200
B. $50
C. $250
D. $65
E. $125
F. $95
G. $150
H. $75
I. $85
J. $100

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
| 规划阶段总时间 (Planner) | 4.587 | 100% |
| 规划过程中启动的任务数 | 7 / 9 | 77.8% |
| 规划与执行重叠的任务数 | 7 / 9 | 77.8% |
| 第一个任务规划完成时间 | 0.963 | - |
| 最后一个任务规划完成时间 | 4.545 | - |
| 最后一个任务执行完成时间 | 6.906 | - |
| 任务总执行时间(累计) | 9.232 | - |
| 流水线加速比 | 3.24x | - |
| 并行效率 | 133.7% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 1.845 | - |
| 大模型任务 | 7 | 7.387 | - |
| 规划模型 | 1 | 13.140 | - |
| 顺序总时间 | - | 22.372 | - |
| 并行总时间 | - | 6.906 | 3.24x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the strike price of the stock option? | 大模型 | 0.963 | 1.963 | 1.000 | 2 |
| 2 | How many shares did Janet purchase under the option? | 小模型 | 1.385 | 2.307 | 0.922 | 3 |
| 3 | What was the purchase price per share for Janet? | 大模型 | 2.307 | 3.385 | 1.077 | 4 |
| 4 | What was the selling price per share on the open market? | 大模型 | 2.298 | 3.298 | 1.000 | 5 |
| 5 | How many shares did Janet sell on the open market? | 小模型 | 2.747 | 3.670 | 0.922 | 6 |
| 6 | What was Janet's total cost for the option purchase? | 大模型 | 3.385 | 4.462 | 1.077 | 7 |
| 7 | What was Janet's total revenue from selling the stock? | 大模型 | 3.674 | 4.752 | 1.077 | 8 |
| 8 | What was Janet's profit on the stock transaction? | 大模型 | 4.752 | 5.906 | 1.155 | 9 |
| 9 | Which answer choice matches Janet's profit? | 大模型 | 5.906 | 6.906 | 1.000 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            5.94s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 0.96s - 1.96s
步骤 2 |    #########                                               | 1.38s - 2.31s
步骤 4 |             ##########                                     | 2.30s - 3.30s
步骤 3 |             ###########                                    | 2.31s - 3.38s
步骤 5 |                  #########                                 | 2.75s - 3.67s
步骤 6 |                        ###########                         | 3.38s - 4.46s
步骤 7 |                           ###########                      | 3.67s - 4.75s
步骤 8 |                                      ###########           | 4.75s - 5.91s
步骤 9 |                                                 ###########| 5.91s - 6.91s
```

