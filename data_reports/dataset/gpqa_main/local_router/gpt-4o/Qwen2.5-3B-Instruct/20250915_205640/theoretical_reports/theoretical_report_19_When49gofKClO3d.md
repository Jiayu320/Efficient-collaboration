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
| 规划阶段总时间 (Planner) | 5.598 | 100% |
| 规划过程中启动的任务数 | 8 / 10 | 80.0% |
| 规划与执行重叠的任务数 | 8 / 10 | 80.0% |
| 第一个任务规划完成时间 | 1.020 | - |
| 最后一个任务规划完成时间 | 5.556 | - |
| 最后一个任务执行完成时间 | 7.831 | - |
| 任务总执行时间(累计) | 9.490 | - |
| 流水线加速比 | 3.07x | - |
| 并行效率 | 121.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 1.845 | - |
| 大模型任务 | 8 | 7.645 | - |
| 规划模型 | 1 | 14.545 | - |
| 顺序总时间 | - | 24.035 | - |
| 并行总时间 | - | 7.831 | 3.07x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the balanced chemical equation for the decomposition of KClO3? | 大模型 | 1.020 | 1.962 | 0.943 | 2 |
| 2 | How many moles of KClO3 decompose to produce O2? | 大模型 | 1.962 | 2.870 | 0.908 | 3 |
| 3 | How many moles of O2 are produced from the decomposition of 49 g KClO3? | 大模型 | 2.870 | 3.848 | 0.977 | 4 |
| 4 | What is the mass of pure KClO3 in 49 g? | 小模型 | 2.537 | 3.459 | 0.922 | 5 |
| 5 | How many moles of O2 are produced from the pure KClO3? | 大模型 | 3.459 | 4.402 | 0.943 | 6 |
| 6 | How many moles of metal oxide are formed from the O2? | 大模型 | 4.402 | 5.379 | 0.977 | 7 |
| 7 | What is the mass of impure metal (20% purity) provided? | 小模型 | 4.011 | 4.934 | 0.922 | 8 |
| 8 | What is the mass of pure metal in the impure sample? | 大模型 | 4.934 | 5.807 | 0.873 | 9 |
| 9 | What is the balanced chemical equation for the reduction of metal oxide to pure metal using carbon? | 大模型 | 5.807 | 6.819 | 1.012 | 10 |
| 10 | How much carbon is needed to convert the metal oxide to pure metal? | 大模型 | 6.819 | 7.831 | 1.012 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            6.81s
+------------------------------------------------------------+
步骤 1 |########                                                    | 1.02s - 1.96s
步骤 2 |        ########                                            | 1.96s - 2.87s
步骤 4 |             ########                                       | 2.54s - 3.46s
步骤 3 |                ########                                    | 2.87s - 3.85s
步骤 5 |                     ########                               | 3.46s - 4.40s
步骤 7 |                          ########                          | 4.01s - 4.93s
步骤 6 |                             #########                      | 4.40s - 5.38s
步骤 8 |                                  ########                  | 4.93s - 5.81s
步骤 9 |                                          #########         | 5.81s - 6.82s
步骤 10 |                                                   #########| 6.82s - 7.83s
```

