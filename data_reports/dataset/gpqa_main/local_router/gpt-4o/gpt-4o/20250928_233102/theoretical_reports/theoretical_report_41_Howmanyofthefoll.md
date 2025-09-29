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
| 规划阶段总时间 (Planner) | 3.047 | 100% |
| 规划过程中启动的任务数 | 7 / 8 | 87.5% |
| 规划与执行重叠的任务数 | 7 / 8 | 87.5% |
| 第一个任务规划完成时间 | 0.983 | - |
| 最后一个任务规划完成时间 | 3.031 | - |
| 最后一个任务执行完成时间 | 4.894 | - |
| 任务总执行时间(累计) | 9.133 | - |
| 流水线加速比 | 3.34x | - |
| 并行效率 | 186.6% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 8 | 9.133 | - |
| 规划模型 | 1 | 7.197 | - |
| 顺序总时间 | - | 16.330 | - |
| 并行总时间 | - | 4.894 | 3.34x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Does (Z)-1-chloro-2-methylbut-1-ene possess a plane of symmetry or rotational symmetry axis that makes it non-chiral? | 大模型 | 0.983 | 2.134 | 1.150 | 2 |
| 2 | For (3aR,7aS,E)-8-(chloromethylene)hexahydro-4,7-methanoisobenzofuran-1,3-dione, does the axial chloromethylene substituent create a symmetry axis or plane? | 大模型 | 1.374 | 2.594 | 1.219 | 3 |
| 3 | Does (2R,3S)-2,3-dimethylsuccinic acid have a plane of symmetry due to its substituent arrangement? | 大模型 | 1.635 | 2.785 | 1.150 | 4 |
| 4 | For (2R,3R)-2,3-dimethylsuccinic acid, does the stereocenter configuration eliminate all symmetry planes or axes? | 大模型 | 1.907 | 3.057 | 1.150 | 5 |
| 5 | Does (R)-cyclohex-3-en-1-ol have a plane of symmetry due to its cyclohexene ring substitution pattern? | 大模型 | 2.167 | 3.318 | 1.150 | 6 |
| 6 | For (1s,3s,5s)-cyclohexane-1,3,5-triol, does the equatorial substituent arrangement create a symmetry plane? | 大模型 | 2.466 | 3.616 | 1.150 | 7 |
| 7 | Does 1-cyclopentyl-3-methylbutan-1-one have a plane of symmetry due to its cyclopentyl substitution? | 大模型 | 2.732 | 3.813 | 1.081 | 8 |
| 8 | Based on Steps 1-7, how many compounds lack symmetry planes/axes and thus exhibit optical activity? | 大模型 | 3.813 | 4.894 | 1.081 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            3.91s
+------------------------------------------------------------+
步骤 1 |#################                                           | 0.98s - 2.13s
步骤 2 |     ###################                                    | 1.37s - 2.59s
步骤 3 |         ##################                                 | 1.64s - 2.79s
步骤 4 |              #################                             | 1.91s - 3.06s
步骤 5 |                  #################                         | 2.17s - 3.32s
步骤 6 |                      ##################                    | 2.47s - 3.62s
步骤 7 |                          #################                 | 2.73s - 3.81s
步骤 8 |                                           #################| 3.81s - 4.89s
```

