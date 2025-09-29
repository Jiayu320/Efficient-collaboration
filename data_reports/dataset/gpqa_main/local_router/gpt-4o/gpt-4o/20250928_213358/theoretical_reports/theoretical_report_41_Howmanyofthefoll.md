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
| 小模型 (gpt-4o) | 0.735 | 144.50 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-4B-Thinking/full/ep5) | 0.690 | 184.10 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 2.933 | 100% |
| 规划过程中启动的任务数 | 7 / 8 | 87.5% |
| 规划与执行重叠的任务数 | 7 / 8 | 87.5% |
| 第一个任务规划完成时间 | 0.956 | - |
| 最后一个任务规划完成时间 | 2.917 | - |
| 最后一个任务执行完成时间 | 4.775 | - |
| 任务总执行时间(累计) | 8.994 | - |
| 流水线加速比 | 3.35x | - |
| 并行效率 | 188.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.012 | - |
| 大模型任务 | 7 | 7.982 | - |
| 规划模型 | 1 | 6.985 | - |
| 顺序总时间 | - | 15.980 | - |
| 并行总时间 | - | 4.775 | 3.35x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Does (Z)-1-chloro-2-methylbut-1-ene contain any chiral centers and lack a plane of symmetry? | 大模型 | 0.956 | 2.106 | 1.150 | 2 |
| 2 | Does (3aR,7aS,E)-8-(chloromethylene)hexahydro-4,7-methanoisobenzofuran-1,3-dione contain any chiral centers and lack a plane of symmetry? | 大模型 | 1.320 | 2.540 | 1.219 | 3 |
| 3 | Does (2R,3S)-2,3-dimethylsuccinic acid contain any chiral centers and lack a plane of symmetry? | 大模型 | 1.575 | 2.656 | 1.081 | 4 |
| 4 | Does (2R,3R)-2,3-dimethylsuccinic acid contain any chiral centers and lack a plane of symmetry? | 大模型 | 1.831 | 2.912 | 1.081 | 5 |
| 5 | Does (R)-cyclohex-3-en-1-ol contain any chiral centers and lack a plane of symmetry? | 大模型 | 2.070 | 3.220 | 1.150 | 6 |
| 6 | Does (1s,3s,5s)-cyclohexane-1,3,5-triol contain any chiral centers and lack a plane of symmetry? | 大模型 | 2.363 | 3.513 | 1.150 | 7 |
| 7 | Does 1-cyclopentyl-3-methylbutan-1-one contain any chiral centers and lack a plane of symmetry? | 大模型 | 2.613 | 3.763 | 1.150 | 8 |
| 8 | Count the number of compounds identified as exhibiting optical activity in Steps 1-7. What is the final count? | 小模型 | 3.763 | 4.775 | 1.012 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            3.82s
+------------------------------------------------------------+
步骤 1 |##################                                          | 0.96s - 2.11s
步骤 2 |     ###################                                    | 1.32s - 2.54s
步骤 3 |         #################                                  | 1.58s - 2.66s
步骤 4 |             #################                              | 1.83s - 2.91s
步骤 5 |                 ##################                         | 2.07s - 3.22s
步骤 6 |                      ##################                    | 2.36s - 3.51s
步骤 7 |                          ##################                | 2.61s - 3.76s
步骤 8 |                                            ################| 3.76s - 4.77s
```

