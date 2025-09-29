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
| 路由模型 (saves/Qwen3-4B-Thinking/full/ep5) | 0.690 | 184.10 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 1.956 | 100% |
| 规划过程中启动的任务数 | 4 / 5 | 80.0% |
| 规划与执行重叠的任务数 | 4 / 5 | 80.0% |
| 第一个任务规划完成时间 | 0.924 | - |
| 最后一个任务规划完成时间 | 1.939 | - |
| 最后一个任务执行完成时间 | 3.758 | - |
| 任务总执行时间(累计) | 5.777 | - |
| 流水线加速比 | 3.09x | - |
| 并行效率 | 153.7% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 2.465 | - |
| 大模型任务 | 3 | 3.312 | - |
| 规划模型 | 1 | 5.850 | - |
| 顺序总时间 | - | 11.627 | - |
| 并行总时间 | - | 3.758 | 3.09x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the primary public health risk that advertising regulations prohibit by forbidding 'unsafe practices'? | 小模型 | 0.924 | 2.233 | 1.310 | 2 |
| 2 | Which psychological state is explicitly prohibited by advertising standards as a result of misleading or harmful content? | 小模型 | 1.130 | 2.285 | 1.155 | 3 |
| 3 | Which secondary emotional response is commonly associated with social comparison in regulated advertising content? | 大模型 | 1.320 | 2.401 | 1.081 | 4 |
| 4 | What threshold for offense is considered acceptable under advertising regulatory frameworks, excluding trivial or serious harm? | 大模型 | 1.527 | 2.608 | 1.081 | 5 |
| 5 | Given the answers to Steps 1 (unsafe practices), 2 (distress), 3 (jealousy), and 4 (trivial), which option (B, F, or H) correctly matches these terms in order? | 大模型 | 2.608 | 3.758 | 1.150 | 6 |

## 理论执行甘特图

```
时间轴:
0                                                            2.83s
+------------------------------------------------------------+
步骤 1 |###########################                                 | 0.92s - 2.23s
步骤 2 |    ########################                                | 1.13s - 2.28s
步骤 3 |        #######################                             | 1.32s - 2.40s
步骤 4 |            #######################                         | 1.53s - 2.61s
步骤 5 |                                   #########################| 2.61s - 3.76s
```

