# 问题 21 的理论性能分析报告

## 问题描述

Why does the hydroboration reaction between a conjugated diene and Ipc2BH form a single product, even at different temperatures?


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
| 规划阶段总时间 (Planner) | 3.014 | 100% |
| 规划过程中启动的任务数 | 2 / 5 | 40.0% |
| 规划与执行重叠的任务数 | 2 / 5 | 40.0% |
| 第一个任务规划完成时间 | 1.006 | - |
| 最后一个任务规划完成时间 | 2.972 | - |
| 最后一个任务执行完成时间 | 4.249 | - |
| 任务总执行时间(累计) | 5.371 | - |
| 流水线加速比 | 3.03x | - |
| 并行效率 | 126.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 5 | 5.371 | - |
| 规划模型 | 1 | 7.522 | - |
| 顺序总时间 | - | 12.893 | - |
| 并行总时间 | - | 4.249 | 3.03x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the mechanism of hydroboration of conjugated dienes? | 大模型 | 1.006 | 2.087 | 1.081 | 2 |
| 2 | How does Ipc2BH act as a borane reagent in this reaction? | 大模型 | 2.087 | 3.098 | 1.012 | 3 |
| 3 | Why does the reaction proceed with a single product despite different temperatures? | 大模型 | 3.098 | 4.249 | 1.150 | 4 |
| 4 | What determines the stereochemistry of the product? | 大模型 | 3.098 | 4.179 | 1.081 | 5 |
| 5 | How does the conjugated diene's structure influence the outcome? | 大模型 | 3.098 | 4.145 | 1.046 | 6 |

## 理论执行甘特图

```
时间轴:
0                                                            3.24s
+------------------------------------------------------------+
步骤 1 |###################                                         | 1.01s - 2.09s
步骤 2 |                   ###################                      | 2.09s - 3.10s
步骤 3 |                                      ######################| 3.10s - 4.25s
步骤 4 |                                      ####################  | 3.10s - 4.18s
步骤 5 |                                      ####################  | 3.10s - 4.14s
```

