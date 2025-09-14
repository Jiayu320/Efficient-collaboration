# 问题 7 的理论性能分析报告

## 问题描述

aniline is heated with sulfuric acid, forming product 1.

1 is treated with sodium bicarbonate, followed by sodium nitrite and HCl, forming product 2.

2 is allowed to react with 2-napthol, forming final product 3.

how many distinct nonexchaning hydrogen signals are there in the 1H nmr spectrum of 3?


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
| 规划阶段总时间 (Planner) | 3.815 | 100% |
| 规划过程中启动的任务数 | 4 / 6 | 66.7% |
| 规划与执行重叠的任务数 | 4 / 6 | 66.7% |
| 第一个任务规划完成时间 | 1.048 | - |
| 最后一个任务规划完成时间 | 3.772 | - |
| 最后一个任务执行完成时间 | 7.055 | - |
| 任务总执行时间(累计) | 7.084 | - |
| 流水线加速比 | 2.27x | - |
| 并行效率 | 100.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 6 | 7.084 | - |
| 规划模型 | 1 | 8.927 | - |
| 顺序总时间 | - | 16.011 | - |
| 并行总时间 | - | 7.055 | 2.27x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the structure of product 1 formed from aniline and sulfuric acid? | 大模型 | 1.048 | 2.203 | 1.155 | 2 |
| 2 | What is the structure of product 2 formed from sodium bicarbonate, sodium nitrite, and HCl treatment? | 大模型 | 2.203 | 3.358 | 1.155 | 3 |
| 3 | What is the structure of product 3 formed from 2-napthol? | 大模型 | 3.358 | 4.435 | 1.077 | 4 |
| 4 | How does 2-napthol affect the hydrogenation of product 2? | 大模型 | 3.358 | 4.590 | 1.232 | 5 |
| 5 | What are the distinct hydrogen environments in product 3? | 大模型 | 4.590 | 5.900 | 1.310 | 6 |
| 6 | How many non-exchanging hydrogen signals are present in the 1H NMR of product 3? | 大模型 | 5.900 | 7.055 | 1.155 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            6.01s
+------------------------------------------------------------+
步骤 1 |###########                                                 | 1.05s - 2.20s
步骤 2 |           ############                                     | 2.20s - 3.36s
步骤 3 |                       ##########                           | 3.36s - 4.43s
步骤 4 |                       ############                         | 3.36s - 4.59s
步骤 5 |                                   #############            | 4.59s - 5.90s
步骤 6 |                                                ############| 5.90s - 7.05s
```

