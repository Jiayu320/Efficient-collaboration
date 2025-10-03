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
| 路由模型 (gpt-4o) | 0.735 | 144.50 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 3.877 | 100% |
| 规划过程中启动的任务数 | 7 / 10 | 70.0% |
| 规划与执行重叠的任务数 | 7 / 10 | 70.0% |
| 第一个任务规划完成时间 | 1.039 | - |
| 最后一个任务规划完成时间 | 3.856 | - |
| 最后一个任务执行完成时间 | 33.564 | - |
| 任务总执行时间(累计) | 76.554 | - |
| 流水线加速比 | 2.41x | - |
| 并行效率 | 228.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 9 | 68.899 | - |
| 大模型任务 | 1 | 7.655 | - |
| 规划模型 | 1 | 4.257 | - |
| 顺序总时间 | - | 80.812 | - |
| 并行总时间 | - | 33.564 | 2.41x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Determine if (Z)-1-chloro-2-methylbut-1-ene has a chiral center. | 小模型 | 1.039 | 8.695 | 7.655 | 2 |
| 2 | Determine if (3aR,7aS,E)-8-(chloromethylene)hexahydro-4,7-methanoisobenzofuran-1,3-dione has a chiral center. | 小模型 | 1.469 | 9.124 | 7.655 | 3 |
| 3 | Determine if (2R,3S)-2,3-dimethylsuccinic acid has a chiral center. | 小模型 | 1.759 | 9.415 | 7.655 | 4 |
| 4 | Determine if (2R,3R)-2,3-dimethylsuccinic acid has a chiral center. | 小模型 | 2.050 | 9.705 | 7.655 | 5 |
| 5 | Determine if (R)-cyclohex-3-en-1-ol has a chiral center. | 小模型 | 2.320 | 9.975 | 7.655 | 6 |
| 6 | Determine if (1s,3s,5s)-cyclohexane-1,3,5-triol has a chiral center. | 小模型 | 2.659 | 10.314 | 7.655 | 7 |
| 7 | Determine if 1-cyclopentyl-3-methylbutan-1-one has a chiral center. | 小模型 | 2.943 | 10.598 | 7.655 | 8 |
| 8 | For each compound with a chiral center, check if it lacks a plane of symmetry. | 小模型 | 10.598 | 18.253 | 7.655 | 9 |
| 9 | For each compound with a chiral center and no plane of symmetry, check if it can exist as non-superimposable mirror images. | 大模型 | 18.253 | 25.909 | 7.655 | 10 |
| 10 | Count the number of compounds that meet all criteria for optical activity. | 小模型 | 25.909 | 33.564 | 7.655 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            32.52s
+------------------------------------------------------------+
步骤 1 |##############                                              | 1.04s - 8.69s
步骤 2 |##############                                              | 1.47s - 9.12s
步骤 3 | ##############                                             | 1.76s - 9.41s
步骤 4 | ##############                                             | 2.05s - 9.71s
步骤 5 |  ##############                                            | 2.32s - 9.98s
步骤 6 |  ###############                                           | 2.66s - 10.31s
步骤 7 |   ##############                                           | 2.94s - 10.60s
步骤 8 |                 ##############                             | 10.60s - 18.25s
步骤 9 |                               ##############               | 18.25s - 25.91s
步骤 10 |                                             ###############| 25.91s - 33.56s
```

