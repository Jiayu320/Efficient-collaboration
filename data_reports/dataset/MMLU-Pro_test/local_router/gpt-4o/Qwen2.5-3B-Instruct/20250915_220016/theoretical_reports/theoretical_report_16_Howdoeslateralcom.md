# 问题 16 的理论性能分析报告

## 问题描述

How does lateral communication in an organisation occur?

A. Information is shared only during official meetings.
B. Information is restricted within a single department.
C. Information is transferred through external stakeholders.
D. Information is transferred only through the head of the organisation.
E. Information is disseminated through public announcements.
F. Information passes upwards.
G. Information passes downwards.
H. Information is a two-way process.
I. Information passes diagonally between different levels of hierarchy.
J. Information passes between different departments and functions.

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
| 规划阶段总时间 (Planner) | 4.292 | 100% |
| 规划过程中启动的任务数 | 6 / 8 | 75.0% |
| 规划与执行重叠的任务数 | 6 / 8 | 75.0% |
| 第一个任务规划完成时间 | 0.935 | - |
| 最后一个任务规划完成时间 | 4.250 | - |
| 最后一个任务执行完成时间 | 6.434 | - |
| 任务总执行时间(累计) | 7.299 | - |
| 流水线加速比 | 2.96x | - |
| 并行效率 | 113.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 8 | 7.299 | - |
| 规划模型 | 1 | 11.736 | - |
| 顺序总时间 | - | 19.035 | - |
| 并行总时间 | - | 6.434 | 2.96x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What defines lateral communication in an organisation? | 大模型 | 0.935 | 1.809 | 0.873 | 2 |
| 2 | Which options suggest information is shared between different departments or functions? | 大模型 | 1.385 | 2.293 | 0.908 | 3 |
| 3 | Which options suggest information flows within the same department or function? | 大模型 | 1.834 | 2.742 | 0.908 | 4 |
| 4 | Which options suggest information moves between different levels of the hierarchy? | 大模型 | 2.284 | 3.192 | 0.908 | 5 |
| 5 | Which options suggest information is shared without formal approval or channels? | 大模型 | 2.733 | 3.641 | 0.908 | 6 |
| 6 | Which options describe the characteristics of effective lateral communication? | 大模型 | 3.641 | 4.584 | 0.943 | 7 |
| 7 | Which options are most commonly used to describe lateral communication in organisational studies? | 大模型 | 4.584 | 5.526 | 0.943 | 8 |
| 8 | Which option best describes the mechanism of lateral communication in an organisation? | 大模型 | 5.526 | 6.434 | 0.908 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            5.50s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 0.94s - 1.81s
步骤 2 |    ##########                                              | 1.38s - 2.29s
步骤 3 |         ##########                                         | 1.83s - 2.74s
步骤 4 |              ##########                                    | 2.28s - 3.19s
步骤 5 |                   ##########                               | 2.73s - 3.64s
步骤 6 |                             ##########                     | 3.64s - 4.58s
步骤 7 |                                       ###########          | 4.58s - 5.53s
步骤 8 |                                                  ##########| 5.53s - 6.43s
```

