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
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Thinking/full/train_2025-09-25-23-33-09) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 3.520 | 100% |
| 规划过程中启动的任务数 | 2 / 4 | 50.0% |
| 规划与执行重叠的任务数 | 2 / 4 | 50.0% |
| 第一个任务规划完成时间 | 1.230 | - |
| 最后一个任务规划完成时间 | 3.478 | - |
| 最后一个任务执行完成时间 | 5.762 | - |
| 任务总执行时间(累计) | 4.532 | - |
| 流水线加速比 | 3.40x | - |
| 并行效率 | 78.6% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 4 | 4.532 | - |
| 规划模型 | 1 | 15.037 | - |
| 顺序总时间 | - | 19.568 | - |
| 并行总时间 | - | 5.762 | 3.40x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Which negative emotional states are typically prohibited by 'encourage' in advertising regulations, such as 'distress' or 'jealousy'? | 大模型 | 1.230 | 2.381 | 1.150 | 2 |
| 2 | Which negative emotional states are typically prohibited by 'cause' in advertising regulations, such as 'distress' or 'fear'? | 大模型 | 2.381 | 3.531 | 1.150 | 3 |
| 3 | Which severity level of offense is typically prohibited by 'offence' in advertising regulations, such as 'trivial' or 'serious'? | 大模型 | 3.531 | 4.681 | 1.150 | 4 |
| 4 | Which option lists the prohibited elements as: [negative behavior] for 'encourage', [negative state] for 'cause', and [offense severity] for 'offence'? | 大模型 | 4.681 | 5.762 | 1.081 | 5 |

## 理论执行甘特图

```
时间轴:
0                                                            4.53s
+------------------------------------------------------------+
步骤 1 |###############                                             | 1.23s - 2.38s
步骤 2 |               ###############                              | 2.38s - 3.53s
步骤 3 |                              ###############               | 3.53s - 4.68s
步骤 4 |                                             ###############| 4.68s - 5.76s
```

