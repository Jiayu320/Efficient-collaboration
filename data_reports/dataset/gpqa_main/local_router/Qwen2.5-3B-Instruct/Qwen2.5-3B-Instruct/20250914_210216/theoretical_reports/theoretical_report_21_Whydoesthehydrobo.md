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
| 规划阶段总时间 (Planner) | 3.435 | 100% |
| 规划过程中启动的任务数 | 5 / 6 | 83.3% |
| 规划与执行重叠的任务数 | 5 / 6 | 83.3% |
| 第一个任务规划完成时间 | 1.034 | - |
| 最后一个任务规划完成时间 | 3.393 | - |
| 最后一个任务执行完成时间 | 5.425 | - |
| 任务总执行时间(累计) | 6.697 | - |
| 流水线加速比 | 2.88x | - |
| 并行效率 | 123.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 6 | 6.697 | - |
| 规划模型 | 1 | 8.927 | - |
| 顺序总时间 | - | 15.624 | - |
| 并行总时间 | - | 5.425 | 2.88x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the structure of the conjugated diene and Ipc2BH? | 大模型 | 1.034 | 2.189 | 1.155 | 2 |
| 2 | What is the expected outcome of hydroboration at higher temperatures? | 大模型 | 1.497 | 2.575 | 1.077 | 3 |
| 3 | What is the expected outcome of hydroboration at lower temperatures? | 大模型 | 1.961 | 3.038 | 1.077 | 4 |
| 4 | How does the reaction mechanism differ between these two temperatures? | 大模型 | 3.038 | 4.270 | 1.232 | 5 |
| 5 | What role does Ipc2BH play in the reaction? | 大模型 | 2.902 | 3.902 | 1.000 | 6 |
| 6 | Why does the reaction form a single product despite temperature differences? | 大模型 | 4.270 | 5.425 | 1.155 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            4.39s
+------------------------------------------------------------+
步骤 1 |###############                                             | 1.03s - 2.19s
步骤 2 |      ###############                                       | 1.50s - 2.57s
步骤 3 |            ###############                                 | 1.96s - 3.04s
步骤 5 |                         ##############                     | 2.90s - 3.90s
步骤 4 |                           #################                | 3.04s - 4.27s
步骤 6 |                                            ############### | 4.27s - 5.43s
```

