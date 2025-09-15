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
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 6.989 | 100% |
| 规划过程中启动的任务数 | 9 / 10 | 90.0% |
| 规划与执行重叠的任务数 | 9 / 10 | 90.0% |
| 第一个任务规划完成时间 | 0.949 | - |
| 最后一个任务规划完成时间 | 6.947 | - |
| 最后一个任务执行完成时间 | 8.096 | - |
| 任务总执行时间(累计) | 9.184 | - |
| 流水线加速比 | 2.93x | - |
| 并行效率 | 113.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 10 | 9.184 | - |
| 规划模型 | 1 | 14.545 | - |
| 顺序总时间 | - | 23.729 | - |
| 并行总时间 | - | 8.096 | 2.93x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What determines if a compound exhibits optical activity? | 大模型 | 0.949 | 1.892 | 0.943 | 2 |
| 2 | What is the condition for a compound to have a plane of symmetry? | 大模型 | 1.892 | 2.800 | 0.908 | 3 |
| 3 | How many stereocenters does (Z)-1-chloro-2-methylbut-1-ene have? | 大模型 | 2.031 | 2.904 | 0.873 | 4 |
| 4 | What is the configuration at each stereocenter in (3aR,7aS,E)-8-(chloromethylene)hexahydro-4,7-methanoisobenzofuran-1,3-dione? | 大模型 | 2.958 | 3.935 | 0.977 | 5 |
| 5 | How does the configuration at each stereocenter in (2R,3S)-2,3-dimethylsuccinic acid affect optical activity? | 大模型 | 3.646 | 4.589 | 0.943 | 6 |
| 6 | How does the configuration at each stereocenter in (2R,3R)-2,3-dimethylsuccinic acid affect optical activity? | 大模型 | 4.334 | 5.277 | 0.943 | 7 |
| 7 | What is the configuration at each stereocenter in (R)-cyclohex-3-en-1-ol? | 大模型 | 4.938 | 5.846 | 0.908 | 8 |
| 8 | What is the configuration at each stereocenter in (1s,3s,5s)-cyclohexane-1,3,5-triol? | 大模型 | 5.683 | 6.591 | 0.908 | 9 |
| 9 | What is the configuration at each stereocenter in 1-cyclopentyl-3-methylbutan-1-one? | 大模型 | 6.315 | 7.223 | 0.908 | 10 |
| 10 | How many compounds meet the criteria for optical activity? | 大模型 | 7.223 | 8.096 | 0.873 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            7.15s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 0.95s - 1.89s
步骤 2 |       ########                                             | 1.89s - 2.80s
步骤 3 |         #######                                            | 2.03s - 2.90s
步骤 4 |                #########                                   | 2.96s - 3.94s
步骤 5 |                      ########                              | 3.65s - 4.59s
步骤 6 |                            ########                        | 4.33s - 5.28s
步骤 7 |                                 ########                   | 4.94s - 5.85s
步骤 8 |                                       ########             | 5.68s - 6.59s
步骤 9 |                                             #######        | 6.31s - 7.22s
步骤 10 |                                                    ########| 7.22s - 8.10s
```

