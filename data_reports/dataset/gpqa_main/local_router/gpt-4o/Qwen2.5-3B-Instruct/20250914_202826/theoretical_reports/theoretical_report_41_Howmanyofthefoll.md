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
| 规划阶段总时间 (Planner) | 6.244 | 100% |
| 规划过程中启动的任务数 | 8 / 9 | 88.9% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 0.949 | - |
| 最后一个任务规划完成时间 | 6.202 | - |
| 最后一个任务执行完成时间 | 7.539 | - |
| 任务总执行时间(累计) | 8.968 | - |
| 流水线加速比 | 2.93x | - |
| 并行效率 | 119.0% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 9 | 8.968 | - |
| 规划模型 | 1 | 13.140 | - |
| 顺序总时间 | - | 22.108 | - |
| 并行总时间 | - | 7.539 | 2.93x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What determines if a compound exhibits optical activity? | 大模型 | 0.949 | 1.892 | 0.943 | 2 |
| 2 | What is the plane of symmetry in (Z)-1-chloro-2-methylbut-1-ene? | 大模型 | 1.892 | 2.904 | 1.012 | 3 |
| 3 | What is the plane of symmetry in (3aR,7aS,E)-8-(chloromethylene)hexahydro-4,7-methanoisobenzofuran-1,3-dione? | 大模型 | 2.452 | 3.464 | 1.012 | 4 |
| 4 | What is the plane of symmetry in (2R,3S)-2,3-dimethylsuccinic acid? | 大模型 | 3.070 | 4.082 | 1.012 | 5 |
| 5 | What is the plane of symmetry in (2R,3R)-2,3-dimethylsuccinic acid? | 大模型 | 3.688 | 4.700 | 1.012 | 6 |
| 6 | What is the plane of symmetry in (R)-cyclohex-3-en-1-ol? | 大模型 | 4.264 | 5.276 | 1.012 | 7 |
| 7 | What is the plane of symmetry in (1s,3s,5s)-cyclohexane-1,3,5-triol? | 大模型 | 4.980 | 5.992 | 1.012 | 8 |
| 8 | What is the plane of symmetry in 1-cyclopentyl-3-methylbutan-1-one? | 大模型 | 5.584 | 6.596 | 1.012 | 9 |
| 9 | How many of the compounds have a plane of symmetry? | 大模型 | 6.596 | 7.539 | 0.943 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            6.59s
+------------------------------------------------------------+
步骤 1 |########                                                    | 0.95s - 1.89s
步骤 2 |        #########                                           | 1.89s - 2.90s
步骤 3 |             #########                                      | 2.45s - 3.46s
步骤 4 |                   #########                                | 3.07s - 4.08s
步骤 5 |                        ##########                          | 3.69s - 4.70s
步骤 6 |                              #########                     | 4.26s - 5.28s
步骤 7 |                                    #########               | 4.98s - 5.99s
步骤 8 |                                          #########         | 5.58s - 6.60s
步骤 9 |                                                   #########| 6.60s - 7.54s
```

