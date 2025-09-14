# 问题 19 的理论性能分析报告

## 问题描述

When 49 g of KClO3 decomposes, the resulting O2 reacts with 10.8 g of impure metal (20% purity) to form metal oxide. Calculate the amount of carbon needed to convert the metal oxide back to pure metal. The metal is amphoteric in nature and is one of the most abundant metals in earth crust.

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
| 规划阶段总时间 (Planner) | 5.374 | 100% |
| 规划过程中启动的任务数 | 7 / 9 | 77.8% |
| 规划与执行重叠的任务数 | 7 / 9 | 77.8% |
| 第一个任务规划完成时间 | 1.020 | - |
| 最后一个任务规划完成时间 | 5.331 | - |
| 最后一个任务执行完成时间 | 7.710 | - |
| 任务总执行时间(累计) | 10.239 | - |
| 流水线加速比 | 3.03x | - |
| 并行效率 | 132.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 9 | 10.239 | - |
| 规划模型 | 1 | 13.140 | - |
| 顺序总时间 | - | 23.380 | - |
| 并行总时间 | - | 7.710 | 3.03x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the balanced chemical equation for the decomposition of KClO3? | 大模型 | 1.020 | 2.175 | 1.155 | 2 |
| 2 | How many grams of pure KClO3 decompose if 49 g of impure KClO3 decompose? | 大模型 | 1.596 | 2.673 | 1.077 | 3 |
| 3 | How many moles of O2 are produced from the decomposition of pure KClO3? | 大模型 | 2.673 | 3.828 | 1.155 | 4 |
| 4 | What is the balanced chemical equation for the reaction between metal and O2 to form metal oxide? | 大模型 | 2.705 | 3.937 | 1.232 | 5 |
| 5 | How many grams of pure metal are produced from 10.8 g of impure metal (20% purity)? | 大模型 | 3.323 | 4.400 | 1.077 | 6 |
| 6 | What is the balanced chemical equation for the reduction of metal oxide with carbon? | 大模型 | 3.815 | 5.047 | 1.232 | 7 |
| 7 | How many moles of metal oxide are produced from the impure metal? | 大模型 | 4.400 | 5.555 | 1.155 | 8 |
| 8 | How many grams of carbon are needed to reduce the metal oxide to pure metal? | 大模型 | 5.555 | 6.710 | 1.155 | 9 |
| 9 | What is the final answer in grams of carbon needed? | 大模型 | 6.710 | 7.710 | 1.000 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            6.69s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 1.02s - 2.17s
步骤 2 |     #########                                              | 1.60s - 2.67s
步骤 3 |              ###########                                   | 2.67s - 3.83s
步骤 4 |               ###########                                  | 2.71s - 3.94s
步骤 5 |                    ##########                              | 3.32s - 4.40s
步骤 6 |                         ###########                        | 3.81s - 5.05s
步骤 7 |                              ##########                    | 4.40s - 5.56s
步骤 8 |                                        ###########         | 5.56s - 6.71s
步骤 9 |                                                   #########| 6.71s - 7.71s
```

