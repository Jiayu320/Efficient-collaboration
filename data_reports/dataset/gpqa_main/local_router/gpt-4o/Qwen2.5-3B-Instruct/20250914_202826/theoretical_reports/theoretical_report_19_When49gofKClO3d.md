# 问题 19 的理论性能分析报告

## 问题描述

When 49 g of KClO3 decomposes, the resulting O2 reacts with 10.8 g of impure metal (20% purity) to form metal oxide. Calculate the amount of carbon needed to convert the metal oxide back to pure metal. The metal is amphoteric in nature and is one of the most abundant metals in earth crust.

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
| 规划阶段总时间 (Planner) | 4.376 | 100% |
| 规划过程中启动的任务数 | 6 / 8 | 75.0% |
| 规划与执行重叠的任务数 | 6 / 8 | 75.0% |
| 第一个任务规划完成时间 | 1.020 | - |
| 最后一个任务规划完成时间 | 4.334 | - |
| 最后一个任务执行完成时间 | 6.759 | - |
| 任务总执行时间(累计) | 7.625 | - |
| 流水线加速比 | 2.86x | - |
| 并行效率 | 112.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 0.922 | - |
| 大模型任务 | 7 | 6.702 | - |
| 规划模型 | 1 | 11.736 | - |
| 顺序总时间 | - | 19.360 | - |
| 并行总时间 | - | 6.759 | 2.86x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the balanced chemical equation for the decomposition of KClO3? | 大模型 | 1.020 | 1.962 | 0.943 | 2 |
| 2 | How many grams of pure KClO3 decomposed? | 大模型 | 1.441 | 2.314 | 0.873 | 3 |
| 3 | What is the balanced chemical equation for the reaction between KClO3 and metal? | 大模型 | 1.962 | 2.974 | 1.012 | 4 |
| 4 | What is the balanced chemical equation for the reaction between metal oxide and carbon? | 大模型 | 2.452 | 3.464 | 1.012 | 5 |
| 5 | How many moles of metal oxide were formed? | 大模型 | 2.974 | 3.951 | 0.977 | 6 |
| 6 | How many moles of carbon are needed to convert the metal oxide to pure metal? | 大模型 | 3.951 | 4.929 | 0.977 | 7 |
| 7 | What is the mass of carbon needed? | 大模型 | 4.929 | 5.837 | 0.908 | 8 |
| 8 | What is the final question to determine the amount of carbon needed? | 小模型 | 5.837 | 6.759 | 0.922 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            5.74s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 1.02s - 1.96s
步骤 2 |    #########                                               | 1.44s - 2.31s
步骤 3 |         ###########                                        | 1.96s - 2.97s
步骤 4 |              ###########                                   | 2.45s - 3.46s
步骤 5 |                    ##########                              | 2.97s - 3.95s
步骤 6 |                              ##########                    | 3.95s - 4.93s
步骤 7 |                                        ##########          | 4.93s - 5.84s
步骤 8 |                                                  ##########| 5.84s - 6.76s
```

