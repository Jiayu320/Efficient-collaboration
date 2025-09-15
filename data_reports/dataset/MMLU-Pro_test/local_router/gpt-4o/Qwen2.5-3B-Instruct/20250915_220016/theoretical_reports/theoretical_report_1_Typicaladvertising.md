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
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 2.930 | 100% |
| 规划过程中启动的任务数 | 3 / 5 | 60.0% |
| 规划与执行重叠的任务数 | 3 / 5 | 60.0% |
| 第一个任务规划完成时间 | 0.963 | - |
| 最后一个任务规划完成时间 | 2.888 | - |
| 最后一个任务执行完成时间 | 5.815 | - |
| 任务总执行时间(累计) | 4.851 | - |
| 流水线加速比 | 2.13x | - |
| 并行效率 | 83.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 5 | 4.851 | - |
| 规划模型 | 1 | 7.522 | - |
| 顺序总时间 | - | 12.374 | - |
| 并行总时间 | - | 5.815 | 2.13x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What are the key regulatory objectives for advertising content? | 大模型 | 0.963 | 1.906 | 0.943 | 2 |
| 2 | Which types of content are typically considered harmful or inappropriate in advertising? | 大模型 | 1.906 | 2.849 | 0.943 | 3 |
| 3 | Which options list elements that align with these harmful content categories? | 大模型 | 2.849 | 3.861 | 1.012 | 4 |
| 4 | Which options include 'Trivial' as a possible outcome for advertising content? | 大模型 | 3.861 | 4.803 | 0.943 | 5 |
| 5 | Which option best matches the regulatory goals with appropriate consequences? | 大模型 | 4.803 | 5.815 | 1.012 | 6 |

## 理论执行甘特图

```
时间轴:
0                                                            4.85s
+------------------------------------------------------------+
步骤 1 |###########                                                 | 0.96s - 1.91s
步骤 2 |           ############                                     | 1.91s - 2.85s
步骤 3 |                       ############                         | 2.85s - 3.86s
步骤 4 |                                   ############             | 3.86s - 4.80s
步骤 5 |                                               #############| 4.80s - 5.81s
```

