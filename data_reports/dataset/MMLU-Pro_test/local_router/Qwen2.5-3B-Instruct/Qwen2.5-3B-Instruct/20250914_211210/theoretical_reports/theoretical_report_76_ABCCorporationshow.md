# 问题 76 的理论性能分析报告

## 问题描述

ABC Corporation shows total assets of $75,000 and total liabilitiesof $52,000. If the Corporation has only 500 shares ofstock outstanding, what is the book value per share?

A. $65 per share
B. $50 per share
C. $30 per share
D. $35 per share
E. $40 per share
F. $60 per share
G. $25 per share
H. $46 per share
I. $42 per share
J. $55 per share

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
| 规划阶段总时间 (Planner) | 2.747 | 100% |
| 规划过程中启动的任务数 | 4 / 5 | 80.0% |
| 规划与执行重叠的任务数 | 4 / 5 | 80.0% |
| 第一个任务规划完成时间 | 0.949 | - |
| 最后一个任务规划完成时间 | 2.705 | - |
| 最后一个任务执行完成时间 | 4.277 | - |
| 任务总执行时间(累计) | 5.155 | - |
| 流水线加速比 | 2.96x | - |
| 并行效率 | 120.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 0.922 | - |
| 大模型任务 | 4 | 4.232 | - |
| 规划模型 | 1 | 7.522 | - |
| 顺序总时间 | - | 12.677 | - |
| 并行总时间 | - | 4.277 | 2.96x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the total equity of ABC Corporation? | 大模型 | 0.949 | 1.949 | 1.000 | 2 |
| 2 | What is the book value of the corporation? | 大模型 | 1.949 | 2.949 | 1.000 | 3 |
| 3 | What is the formula for calculating book value per share? | 大模型 | 1.806 | 2.884 | 1.077 | 4 |
| 4 | What is the number of shares outstanding? | 小模型 | 2.199 | 3.122 | 0.922 | 5 |
| 5 | What is the book value per share using the formula? | 大模型 | 3.122 | 4.277 | 1.155 | 6 |

## 理论执行甘特图

```
时间轴:
0                                                            3.33s
+------------------------------------------------------------+
步骤 1 |##################                                          | 0.95s - 1.95s
步骤 3 |               ###################                          | 1.81s - 2.88s
步骤 2 |                  ##################                        | 1.95s - 2.95s
步骤 4 |                      #################                     | 2.20s - 3.12s
步骤 5 |                                       #####################| 3.12s - 4.28s
```

