# 问题 21 的理论性能分析报告

## 问题描述

Why does the hydroboration reaction between a conjugated diene and Ipc2BH form a single product, even at different temperatures?


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
| 规划阶段总时间 (Planner) | 4.419 | 100% |
| 规划过程中启动的任务数 | 5 / 8 | 62.5% |
| 规划与执行重叠的任务数 | 5 / 8 | 62.5% |
| 第一个任务规划完成时间 | 1.034 | - |
| 最后一个任务规划完成时间 | 4.376 | - |
| 最后一个任务执行完成时间 | 9.237 | - |
| 任务总执行时间(累计) | 10.324 | - |
| 流水线加速比 | 2.39x | - |
| 并行效率 | 111.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 8 | 10.324 | - |
| 规划模型 | 1 | 11.736 | - |
| 顺序总时间 | - | 22.060 | - |
| 并行总时间 | - | 9.237 | 2.39x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the structure of the conjugated diene and Ipc2BH? | 大模型 | 1.034 | 2.189 | 1.155 | 2 |
| 2 | What is the mechanism of hydroboration reaction? | 大模型 | 1.455 | 2.765 | 1.310 | 3 |
| 3 | How does the boron reagent Ipc2BH affect the reaction? | 大模型 | 2.765 | 3.997 | 1.232 | 4 |
| 4 | Why does the reaction form a single product despite different temperatures? | 大模型 | 3.997 | 5.385 | 1.387 | 5 |
| 5 | What factors stabilize the intermediate in the reaction? | 大模型 | 3.997 | 5.307 | 1.310 | 6 |
| 6 | How does the reaction proceed from the conjugated diene to the final product? | 大模型 | 5.307 | 6.695 | 1.387 | 7 |
| 7 | What makes the reaction insensitive to temperature variation? | 大模型 | 6.695 | 8.004 | 1.310 | 8 |
| 8 | Why does the hydroboration reaction form only one product? | 大模型 | 8.004 | 9.237 | 1.232 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            8.20s
+------------------------------------------------------------+
步骤 1 |########                                                    | 1.03s - 2.19s
步骤 2 |   #########                                                | 1.46s - 2.76s
步骤 3 |            #########                                       | 2.76s - 4.00s
步骤 4 |                     ##########                             | 4.00s - 5.38s
步骤 5 |                     ##########                             | 4.00s - 5.31s
步骤 6 |                               ##########                   | 5.31s - 6.69s
步骤 7 |                                         #########          | 6.69s - 8.00s
步骤 8 |                                                  ##########| 8.00s - 9.24s
```

