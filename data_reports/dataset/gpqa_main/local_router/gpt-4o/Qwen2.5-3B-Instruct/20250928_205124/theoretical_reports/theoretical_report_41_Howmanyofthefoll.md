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
| 规划阶段总时间 (Planner) | 3.210 | 100% |
| 规划过程中启动的任务数 | 7 / 8 | 87.5% |
| 规划与执行重叠的任务数 | 7 / 8 | 87.5% |
| 第一个任务规划完成时间 | 1.016 | - |
| 最后一个任务规划完成时间 | 3.194 | - |
| 最后一个任务执行完成时间 | 5.408 | - |
| 任务总执行时间(累计) | 9.915 | - |
| 流水线加速比 | 3.39x | - |
| 并行效率 | 183.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.310 | - |
| 大模型任务 | 7 | 8.605 | - |
| 规划模型 | 1 | 8.425 | - |
| 顺序总时间 | - | 18.340 | - |
| 并行总时间 | - | 5.408 | 3.39x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Does (Z)-1-chloro-2-methylbut-1-ene have a plane of symmetry through the double bond, making it optically inactive despite the chloro group on C1? | 大模型 | 1.016 | 2.235 | 1.219 | 2 |
| 2 | For (3aR,7aS,E)-8-(chloromethylene)hexahydro-4,7-methanoisobenzofuran-1,3-dione, does the internal plane of symmetry through C3a/C7a atoms make it optically inactive? | 大模型 | 1.429 | 2.717 | 1.289 | 3 |
| 3 | Is (2R,3S)-2,3-dimethylsuccinic acid chiral and symmetric enough to be optically inactive as a meso compound? | 大模型 | 1.700 | 2.920 | 1.219 | 4 |
| 4 | Does (2R,3R)-2,3-dimethylsuccinic acid have a plane of symmetry through the carboxylic acid groups, making it optically inactive? | 大模型 | 1.983 | 3.202 | 1.219 | 5 |
| 5 | Does (R)-cyclohex-3-en-1-ol lack a plane of symmetry due to asymmetric substitution on the cyclohexene ring? | 大模型 | 2.249 | 3.468 | 1.219 | 6 |
| 6 | Does (1s,3s,5s)-cyclohexane-1,3,5-triol have a plane of symmetry through C1/C3/C5, making it optically inactive? | 大模型 | 2.580 | 3.800 | 1.219 | 7 |
| 7 | Does 1-cyclopentyl-3-methylbutan-1-one have a plane of symmetry through the cyclopentyl and methyl groups, making it optically inactive? | 大模型 | 2.879 | 4.098 | 1.219 | 8 |
| 8 | Count the number of compounds without symmetry planes from Steps 1-7. What is the final count of optically active compounds? | 小模型 | 4.098 | 5.408 | 1.310 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            4.39s
+------------------------------------------------------------+
步骤 1 |################                                            | 1.02s - 2.24s
步骤 2 |     ##################                                     | 1.43s - 2.72s
步骤 3 |         #################                                  | 1.70s - 2.92s
步骤 4 |             ################                               | 1.98s - 3.20s
步骤 5 |                #################                           | 2.25s - 3.47s
步骤 6 |                     #################                      | 2.58s - 3.80s
步骤 7 |                         #################                  | 2.88s - 4.10s
步骤 8 |                                          ##################| 4.10s - 5.41s
```

