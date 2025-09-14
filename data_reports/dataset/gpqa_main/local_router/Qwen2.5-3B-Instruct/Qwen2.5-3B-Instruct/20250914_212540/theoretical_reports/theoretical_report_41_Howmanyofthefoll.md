# 问题 41 的理论性能分析报告

## 问题描述

How many of the following compounds will exhibit optical activity?

(Z)-1-chloro-2-methylbut-1-ene
(3aR,7aS,E)-8-(chloromethylene)hexahydro-4,7-methanoisobenzofuran-1,3-dione
(2R,3S)-2,3-dimethylsuccinic acid
(2R,3R)-2,3-dimethylsuccinic acid
(R)-cyclohex-3-en-1-ol
(1s,3s,5s)-cyclohexane-1,3,5-triol
1-cyclopentyl-3-methylbutan-1-one

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
| 规划阶段总时间 (Planner) | 6.511 | 100% |
| 规划过程中启动的任务数 | 9 / 10 | 90.0% |
| 规划与执行重叠的任务数 | 9 / 10 | 90.0% |
| 第一个任务规划完成时间 | 0.949 | - |
| 最后一个任务规划完成时间 | 6.469 | - |
| 最后一个任务执行完成时间 | 8.852 | - |
| 任务总执行时间(累计) | 11.472 | - |
| 流水线加速比 | 2.94x | - |
| 并行效率 | 129.6% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 10 | 11.472 | - |
| 规划模型 | 1 | 14.545 | - |
| 顺序总时间 | - | 26.016 | - |
| 并行总时间 | - | 8.852 | 2.94x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What determines if a compound exhibits optical activity? | 大模型 | 0.949 | 2.104 | 1.155 | 2 |
| 2 | How many chiral centers does (Z)-1-chloro-2-methylbut-1-ene have? | 大模型 | 1.525 | 2.603 | 1.077 | 3 |
| 3 | How many chiral centers does (3aR,7aS,E)-8-(chloromethylene)hexahydro-4,7-methanoisobenzofuran-1,3-dione have? | 大模型 | 2.396 | 3.628 | 1.232 | 4 |
| 4 | How many chiral centers does (2R,3S)-2,3-dimethylsuccinic acid have? | 大模型 | 2.986 | 4.141 | 1.155 | 5 |
| 5 | How many chiral centers does (2R,3R)-2,3-dimethylsuccinic acid have? | 大模型 | 3.576 | 4.731 | 1.155 | 6 |
| 6 | How many chiral centers does (R)-cyclohex-3-en-1-ol have? | 大模型 | 4.124 | 5.201 | 1.077 | 7 |
| 7 | How many chiral centers does (1s,3s,5s)-cyclohexane-1,3,5-triol have? | 大模型 | 4.812 | 5.967 | 1.155 | 8 |
| 8 | How many chiral centers does 1-cyclopentyl-3-methylbutan-1-one have? | 大模型 | 5.388 | 6.465 | 1.077 | 9 |
| 9 | Which of the compounds have at least one chiral center? | 大模型 | 6.465 | 7.697 | 1.232 | 10 |
| 10 | How many of the compounds will exhibit optical activity? | 大模型 | 7.697 | 8.852 | 1.155 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            7.90s
+------------------------------------------------------------+
步骤 1 |########                                                    | 0.95s - 2.10s
步骤 2 |    ########                                                | 1.53s - 2.60s
步骤 3 |          ##########                                        | 2.40s - 3.63s
步骤 4 |               #########                                    | 2.99s - 4.14s
步骤 5 |                   #########                                | 3.58s - 4.73s
步骤 6 |                        ########                            | 4.12s - 5.20s
步骤 7 |                             #########                      | 4.81s - 5.97s
步骤 8 |                                 ########                   | 5.39s - 6.47s
步骤 9 |                                         ##########         | 6.47s - 7.70s
步骤 10 |                                                   #########| 7.70s - 8.85s
```

