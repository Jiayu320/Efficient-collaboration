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
| 规划阶段总时间 (Planner) | 5.360 | 100% |
| 规划过程中启动的任务数 | 8 / 10 | 80.0% |
| 规划与执行重叠的任务数 | 8 / 10 | 80.0% |
| 第一个任务规划完成时间 | 1.020 | - |
| 最后一个任务规划完成时间 | 5.317 | - |
| 最后一个任务执行完成时间 | 7.851 | - |
| 任务总执行时间(累计) | 10.929 | - |
| 流水线加速比 | 3.24x | - |
| 并行效率 | 139.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 10 | 10.929 | - |
| 规划模型 | 1 | 14.545 | - |
| 顺序总时间 | - | 25.474 | - |
| 并行总时间 | - | 7.851 | 3.24x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the balanced chemical equation for the decomposition of KClO3? | 大模型 | 1.020 | 2.175 | 1.155 | 2 |
| 2 | How many grams of pure KClO3 decompose if 49 g of impure KClO3 decompose? | 大模型 | 1.596 | 2.673 | 1.077 | 3 |
| 3 | What is the molar mass of KClO3? | 大模型 | 2.017 | 3.017 | 1.000 | 4 |
| 4 | What is the molar mass of O2? | 大模型 | 2.424 | 3.424 | 1.000 | 5 |
| 5 | How many moles of O2 are produced from the decomposition reaction? | 大模型 | 3.424 | 4.579 | 1.155 | 6 |
| 6 | What is the molar mass of the impure metal (20% purity)? | 大模型 | 3.463 | 4.541 | 1.077 | 7 |
| 7 | How many grams of pure metal are produced from the impure metal? | 大模型 | 4.541 | 5.618 | 1.077 | 8 |
| 8 | What is the molar mass of the metal oxide? | 大模型 | 4.376 | 5.531 | 1.155 | 9 |
| 9 | How many moles of metal oxide are produced? | 大模型 | 5.618 | 6.696 | 1.077 | 10 |
| 10 | How much carbon is needed to convert the metal oxide to pure metal? | 大模型 | 6.696 | 7.851 | 1.155 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            6.83s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 1.02s - 2.17s
步骤 2 |     #########                                              | 1.60s - 2.67s
步骤 3 |        #########                                           | 2.02s - 3.02s
步骤 4 |            #########                                       | 2.42s - 3.42s
步骤 5 |                     ##########                             | 3.42s - 4.58s
步骤 6 |                     #########                              | 3.46s - 4.54s
步骤 8 |                             ##########                     | 4.38s - 5.53s
步骤 7 |                              ##########                    | 4.54s - 5.62s
步骤 9 |                                        #########           | 5.62s - 6.70s
步骤 10 |                                                 ###########| 6.70s - 7.85s
```

