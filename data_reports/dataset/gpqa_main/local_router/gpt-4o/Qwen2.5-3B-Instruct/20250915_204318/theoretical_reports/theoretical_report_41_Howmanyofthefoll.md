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
| 规划阶段总时间 (Planner) | 4.419 | 100% |
| 规划过程中启动的任务数 | 4 / 8 | 50.0% |
| 规划与执行重叠的任务数 | 4 / 8 | 50.0% |
| 第一个任务规划完成时间 | 0.949 | - |
| 最后一个任务规划完成时间 | 4.376 | - |
| 最后一个任务执行完成时间 | 9.428 | - |
| 任务总执行时间(累计) | 8.479 | - |
| 流水线加速比 | 2.14x | - |
| 并行效率 | 89.9% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 4 | 4.155 | - |
| 大模型任务 | 4 | 4.324 | - |
| 规划模型 | 1 | 11.736 | - |
| 顺序总时间 | - | 20.215 | - |
| 并行总时间 | - | 9.428 | 2.14x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What determines if a compound exhibits optical activity? | 小模型 | 0.949 | 1.949 | 1.000 | 2 |
| 2 | What is the requirement for a compound to have a plane of symmetry? | 小模型 | 1.949 | 3.027 | 1.077 | 3 |
| 3 | How do we determine if a compound has a chiral center? | 小模型 | 3.027 | 4.182 | 1.155 | 4 |
| 4 | For each compound, check if it has any chiral centers? | 大模型 | 4.182 | 5.263 | 1.081 | 5 |
| 5 | For compounds with chiral centers, do the centers have equal or opposite configuration? | 大模型 | 5.263 | 6.344 | 1.081 | 6 |
| 6 | What determines if a compound with chiral centers is optically active? | 大模型 | 6.344 | 7.356 | 1.012 | 7 |
| 7 | How many of the given compounds have chiral centers with non-superimposable mirror images? | 大模型 | 7.356 | 8.506 | 1.150 | 8 |
| 8 | What is the final question regarding the number of compounds exhibiting optical activity? | 小模型 | 8.506 | 9.428 | 0.922 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            8.48s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 0.95s - 1.95s
步骤 2 |       #######                                              | 1.95s - 3.03s
步骤 3 |              ########                                      | 3.03s - 4.18s
步骤 4 |                      ########                              | 4.18s - 5.26s
步骤 5 |                              ########                      | 5.26s - 6.34s
步骤 6 |                                      #######               | 6.34s - 7.36s
步骤 7 |                                             ########       | 7.36s - 8.51s
步骤 8 |                                                     #######| 8.51s - 9.43s
```

