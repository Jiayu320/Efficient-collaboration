# 问题 1 的理论性能分析报告

## 问题描述

Typical advertising regulatory bodies suggest, for example that adverts must not: encourage _________, cause unnecessary ________ or _____, and must not cause _______ offence.

A. Safe practices, Fear, Jealousy, Trivial
B. Unsafe practices, Distress, Joy, Trivial
C. Safe practices, Wants, Jealousy, Trivial
D. Safe practices, Distress, Fear, Trivial
E. Unsafe practices, Wants, Jealousy, Serious
F. Safe practices, Distress, Jealousy, Serious
G. Safe practices, Wants, Fear, Serious
H. Unsafe practices, Wants, Fear, Trivial
I. Unsafe practices, Distress, Fear, Serious

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
| 规划阶段总时间 (Planner) | 2.944 | 100% |
| 规划过程中启动的任务数 | 3 / 5 | 60.0% |
| 规划与执行重叠的任务数 | 3 / 5 | 60.0% |
| 第一个任务规划完成时间 | 1.006 | - |
| 最后一个任务规划完成时间 | 2.902 | - |
| 最后一个任务执行完成时间 | 5.858 | - |
| 任务总执行时间(累计) | 6.007 | - |
| 流水线加速比 | 2.31x | - |
| 并行效率 | 102.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 5 | 6.007 | - |
| 规划模型 | 1 | 7.522 | - |
| 顺序总时间 | - | 13.529 | - |
| 并行总时间 | - | 5.858 | 2.31x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What are the key regulatory concerns for advertisements according to the question? | 大模型 | 1.006 | 2.161 | 1.155 | 2 |
| 2 | What are the three negative impacts that advertisements must not encourage? | 大模型 | 2.161 | 3.315 | 1.155 | 3 |
| 3 | What are the three negative impacts that advertisements must not cause? | 大模型 | 2.161 | 3.315 | 1.155 | 4 |
| 4 | Which answer choice contains the correct pattern of negative impacts? | 大模型 | 3.315 | 4.625 | 1.310 | 5 |
| 5 | Does the selected answer choice have the correct word choices for each blank? | 大模型 | 4.625 | 5.858 | 1.232 | 6 |

## 理论执行甘特图

```
时间轴:
0                                                            4.85s
+------------------------------------------------------------+
步骤 1 |##############                                              | 1.01s - 2.16s
步骤 2 |              ##############                                | 2.16s - 3.32s
步骤 3 |              ##############                                | 2.16s - 3.32s
步骤 4 |                            ################                | 3.32s - 4.63s
步骤 5 |                                            ################| 4.63s - 5.86s
```

