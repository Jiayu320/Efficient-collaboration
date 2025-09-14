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
| 规划阶段总时间 (Planner) | 3.604 | 100% |
| 规划过程中启动的任务数 | 4 / 6 | 66.7% |
| 规划与执行重叠的任务数 | 4 / 6 | 66.7% |
| 第一个任务规划完成时间 | 0.963 | - |
| 最后一个任务规划完成时间 | 3.562 | - |
| 最后一个任务执行完成时间 | 6.001 | - |
| 任务总执行时间(累计) | 6.774 | - |
| 流水线加速比 | 2.62x | - |
| 并行效率 | 112.9% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 6 | 6.774 | - |
| 规划模型 | 1 | 8.927 | - |
| 顺序总时间 | - | 15.701 | - |
| 并行总时间 | - | 6.001 | 2.62x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What defines a deshielded hydrogen nucleus? | 大模型 | 0.963 | 2.118 | 1.155 | 2 |
| 2 | How does fluorine affect the electron density around adjacent hydrogens? | 大模型 | 2.118 | 3.196 | 1.077 | 3 |
| 3 | How does methoxy (-OCH₃) affect electron density around adjacent hydrogens? | 大模型 | 2.118 | 3.196 | 1.077 | 4 |
| 4 | How does a carbonyl group (like propan-2-ylidene) affect electron density? | 大模型 | 2.537 | 3.614 | 1.077 | 5 |
| 5 | Which compound has the highest number of deshielded hydrogens? | 大模型 | 3.614 | 4.846 | 1.232 | 6 |
| 6 | Which compound contains the most electronically deshielded hydrogen nucleus? | 大模型 | 4.846 | 6.001 | 1.155 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            5.04s
+------------------------------------------------------------+
步骤 1 |#############                                               | 0.96s - 2.12s
步骤 2 |             #############                                  | 2.12s - 3.20s
步骤 3 |             #############                                  | 2.12s - 3.20s
步骤 4 |                  #############                             | 2.54s - 3.61s
步骤 5 |                               ###############              | 3.61s - 4.85s
步骤 6 |                                              ##############| 4.85s - 6.00s
```

