# 问题 42 的理论性能分析报告

## 问题描述

"Consider the following compounds:
1: 7,7-difluorobicyclo[2.2.1]heptane
2: 7-methoxybicyclo[2.2.1]heptane
3: 7-(propan-2-ylidene)bicyclo[2.2.1]heptane
4: 7-fluorobicyclo[2.2.1]heptane

which of these compounds contains the most electronically deshielded hydrogen nucleus?"


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
| 规划阶段总时间 (Planner) | 4.461 | 100% |
| 规划过程中启动的任务数 | 6 / 8 | 75.0% |
| 规划与执行重叠的任务数 | 6 / 8 | 75.0% |
| 第一个任务规划完成时间 | 0.963 | - |
| 最后一个任务规划完成时间 | 4.419 | - |
| 最后一个任务执行完成时间 | 7.048 | - |
| 任务总执行时间(累计) | 9.472 | - |
| 流水线加速比 | 3.01x | - |
| 并行效率 | 134.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 8 | 9.472 | - |
| 规划模型 | 1 | 11.736 | - |
| 顺序总时间 | - | 21.208 | - |
| 并行总时间 | - | 7.048 | 3.01x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What defines a deshielded hydrogen nucleus? | 大模型 | 0.963 | 2.118 | 1.155 | 2 |
| 2 | What functional groups typically deshield hydrogen atoms? | 大模型 | 2.118 | 3.351 | 1.232 | 3 |
| 3 | How does fluorination affect hydrogen deshielding? | 大模型 | 3.351 | 4.506 | 1.155 | 4 |
| 4 | How does methoxy (-OCH₃) typically affect hydrogen deshielding? | 大模型 | 3.351 | 4.583 | 1.232 | 5 |
| 5 | How does a carbonyl group (like propan-2-ylidene) typically affect hydrogen deshielding? | 大模型 | 3.351 | 4.583 | 1.232 | 6 |
| 6 | Which compound has the most fluorine atoms? | 大模型 | 3.365 | 4.365 | 1.000 | 7 |
| 7 | Which compound has the most electron-withdrawing groups? | 大模型 | 4.583 | 5.738 | 1.155 | 8 |
| 8 | Which compound contains the most deshielded hydrogen nuclei? | 大模型 | 5.738 | 7.048 | 1.310 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            6.08s
+------------------------------------------------------------+
步骤 1 |###########                                                 | 0.96s - 2.12s
步骤 2 |           ############                                     | 2.12s - 3.35s
步骤 3 |                       ###########                          | 3.35s - 4.51s
步骤 4 |                       ############                         | 3.35s - 4.58s
步骤 5 |                       ############                         | 3.35s - 4.58s
步骤 6 |                       ##########                           | 3.37s - 4.37s
步骤 7 |                                   ############             | 4.58s - 5.74s
步骤 8 |                                               #############| 5.74s - 7.05s
```

