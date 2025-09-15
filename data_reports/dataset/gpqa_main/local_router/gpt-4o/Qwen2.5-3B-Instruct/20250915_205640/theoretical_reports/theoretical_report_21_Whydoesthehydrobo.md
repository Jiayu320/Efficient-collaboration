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
| 规划阶段总时间 (Planner) | 5.669 | 100% |
| 规划过程中启动的任务数 | 9 / 10 | 90.0% |
| 规划与执行重叠的任务数 | 8 / 10 | 80.0% |
| 第一个任务规划完成时间 | 1.076 | - |
| 最后一个任务规划完成时间 | 5.626 | - |
| 最后一个任务执行完成时间 | 7.285 | - |
| 任务总执行时间(累计) | 10.533 | - |
| 流水线加速比 | 3.44x | - |
| 并行效率 | 144.6% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 10 | 10.533 | - |
| 规划模型 | 1 | 14.545 | - |
| 顺序总时间 | - | 25.078 | - |
| 并行总时间 | - | 7.285 | 3.44x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the mechanism of hydroboration of conjugated dienes with Ipc2BH? | 大模型 | 1.076 | 2.157 | 1.081 | 2 |
| 2 | How does the structure of Ipc2BH influence the reaction pathway? | 大模型 | 2.157 | 3.169 | 1.012 | 3 |
| 3 | What role does the conjugated diene play in determining the reaction outcome? | 大模型 | 2.157 | 3.238 | 1.081 | 4 |
| 4 | How does temperature affect the stability of intermediate species in this reaction? | 大模型 | 3.169 | 4.180 | 1.012 | 5 |
| 5 | What factors ensure the reaction proceeds with a single product regardless of temperature? | 大模型 | 4.180 | 5.262 | 1.081 | 6 |
| 6 | What is the significance of the reaction forming a single product in organic synthesis? | 大模型 | 5.262 | 6.273 | 1.012 | 7 |
| 7 | How does the hydroboration reaction demonstrate stereoselectivity in organic chemistry? | 大模型 | 4.081 | 5.162 | 1.081 | 8 |
| 8 | What are the key differences between different hydroboration reactions at varying temperatures? | 大模型 | 4.587 | 5.668 | 1.081 | 9 |
| 9 | How do the reaction conditions (temperature) affect the stereochemistry of the final product? | 大模型 | 5.668 | 6.749 | 1.081 | 10 |
| 10 | Why is the single product formation important for practical organic synthesis applications? | 大模型 | 6.273 | 7.285 | 1.012 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            6.21s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 1.08s - 2.16s
步骤 2 |          ##########                                        | 2.16s - 3.17s
步骤 3 |          ##########                                        | 2.16s - 3.24s
步骤 4 |                    #########                               | 3.17s - 4.18s
步骤 7 |                             ##########                     | 4.08s - 5.16s
步骤 5 |                             ###########                    | 4.18s - 5.26s
步骤 8 |                                 ###########                | 4.59s - 5.67s
步骤 6 |                                        ##########          | 5.26s - 6.27s
步骤 9 |                                            ##########      | 5.67s - 6.75s
步骤 10 |                                                  ##########| 6.27s - 7.29s
```

