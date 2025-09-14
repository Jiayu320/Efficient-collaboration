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
| 大模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 4.376 | 100% |
| 规划过程中启动的任务数 | 6 / 8 | 75.0% |
| 规划与执行重叠的任务数 | 6 / 8 | 75.0% |
| 第一个任务规划完成时间 | 1.020 | - |
| 最后一个任务规划完成时间 | 4.334 | - |
| 最后一个任务执行完成时间 | 7.838 | - |
| 任务总执行时间(累计) | 10.014 | - |
| 流水线加速比 | 2.77x | - |
| 并行效率 | 127.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 8 | 10.014 | - |
| 规划模型 | 1 | 11.736 | - |
| 顺序总时间 | - | 21.750 | - |
| 并行总时间 | - | 7.838 | 2.77x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What does 'lateral communication' specifically refer to in organisational theory? | 大模型 | 1.020 | 2.330 | 1.310 | 2 |
| 2 | Which communication channels involve interaction between different departments or functions? | 大模型 | 2.330 | 3.562 | 1.232 | 3 |
| 3 | Which communication channels involve horizontal movement within the organisation? | 大模型 | 2.330 | 3.562 | 1.232 | 4 |
| 4 | Which communication channels involve information moving between different levels of hierarchy? | 大模型 | 2.368 | 3.600 | 1.232 | 5 |
| 5 | Which communication channels involve information moving from one department to another? | 大模型 | 2.831 | 4.064 | 1.232 | 6 |
| 6 | Which of the given options directly describe lateral communication channels? | 大模型 | 4.064 | 5.374 | 1.310 | 7 |
| 7 | Which of the remaining options are not part of lateral communication? | 大模型 | 5.374 | 6.684 | 1.310 | 8 |
| 8 | What is the correct answer to the original question about lateral communication? | 大模型 | 6.684 | 7.838 | 1.155 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            6.82s
+------------------------------------------------------------+
步骤 1 |###########                                                 | 1.02s - 2.33s
步骤 2 |           ###########                                      | 2.33s - 3.56s
步骤 3 |           ###########                                      | 2.33s - 3.56s
步骤 4 |           ###########                                      | 2.37s - 3.60s
步骤 5 |               ###########                                  | 2.83s - 4.06s
步骤 6 |                          ############                      | 4.06s - 5.37s
步骤 7 |                                      ###########           | 5.37s - 6.68s
步骤 8 |                                                 ###########| 6.68s - 7.84s
```

