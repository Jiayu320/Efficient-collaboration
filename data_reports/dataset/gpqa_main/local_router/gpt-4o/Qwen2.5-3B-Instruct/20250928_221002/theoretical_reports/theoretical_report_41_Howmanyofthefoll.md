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
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-4B-Thinking/full/ep5) | 0.690 | 184.10 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 3.400 | 100% |
| 规划过程中启动的任务数 | 7 / 8 | 87.5% |
| 规划与执行重叠的任务数 | 7 / 8 | 87.5% |
| 第一个任务规划完成时间 | 1.021 | - |
| 最后一个任务规划完成时间 | 3.384 | - |
| 最后一个任务执行完成时间 | 5.359 | - |
| 任务总执行时间(累计) | 9.617 | - |
| 流水线加速比 | 3.38x | - |
| 并行效率 | 179.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 8 | 9.617 | - |
| 规划模型 | 1 | 8.474 | - |
| 顺序总时间 | - | 18.091 | - |
| 并行总时间 | - | 5.359 | 3.38x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Does (Z)-1-chloro-2-methylbut-1-ene have a plane of symmetry through C1-C2-C3, making it achiral despite having two chiral centers? | 大模型 | 1.021 | 2.241 | 1.219 | 2 |
| 2 | For (3aR,7aS,E)-8-(chloromethylene)hexahydro-4,7-methanoisobenzofuran-1,3-dione, are the chloromethylene group and two methyl groups symmetrically placed on a hemispherical surface of the fused ring system? | 大模型 | 1.461 | 2.750 | 1.289 | 3 |
| 3 | Does (2R,3S)-2,3-dimethylsuccinic acid have a plane of symmetry through the central C=C bond, making it superimposable on its mirror image? | 大模型 | 1.771 | 2.921 | 1.150 | 4 |
| 4 | For (2R,3R)-2,3-dimethylsuccinic acid, is the molecule symmetric with respect to a plane perpendicular to the C=C bond, causing it to lack optical activity? | 大模型 | 2.097 | 3.247 | 1.150 | 5 |
| 5 | Does (R)-cyclohex-3-en-1-ol have a plane of symmetry through C3 and the axial OH position, rendering it achiral? | 大模型 | 2.379 | 3.599 | 1.219 | 6 |
| 6 | For (1s,3s,5s)-cyclohexane-1,3,5-triol, are the hydroxyl groups symmetrically distributed on a hemispherical surface of the cyclohexane ring, causing it to lack optical activity? | 大模型 | 2.760 | 4.048 | 1.289 | 7 |
| 7 | Does 1-cyclopentyl-3-methylbutan-1-one possess any chiral centers, or is its asymmetry due to planar groups rather than three-dimensional chirality? | 大模型 | 3.058 | 4.278 | 1.219 | 8 |
| 8 | Based on Steps 1-7, how many compounds have neither planes of symmetry nor hemispherical symmetry, and thus exhibit optical activity? | 大模型 | 4.278 | 5.359 | 1.081 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            4.34s
+------------------------------------------------------------+
步骤 1 |################                                            | 1.02s - 2.24s
步骤 2 |      #################                                     | 1.46s - 2.75s
步骤 3 |          ################                                  | 1.77s - 2.92s
步骤 4 |              ################                              | 2.10s - 3.25s
步骤 5 |                  #################                         | 2.38s - 3.60s
步骤 6 |                        #################                   | 2.76s - 4.05s
步骤 7 |                            #################               | 3.06s - 4.28s
步骤 8 |                                             ###############| 4.28s - 5.36s
```

