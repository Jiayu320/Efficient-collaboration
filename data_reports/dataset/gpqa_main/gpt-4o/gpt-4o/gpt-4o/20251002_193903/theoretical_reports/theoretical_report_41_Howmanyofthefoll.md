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
| 规划阶段总时间 (Planner) | 3.116 | 100% |
| 规划过程中启动的任务数 | 1 / 7 | 14.3% |
| 规划与执行重叠的任务数 | 1 / 7 | 14.3% |
| 第一个任务规划完成时间 | 1.026 | - |
| 最后一个任务规划完成时间 | 3.095 | - |
| 最后一个任务执行完成时间 | 54.614 | - |
| 任务总执行时间(累计) | 53.588 | - |
| 流水线加速比 | 1.05x | - |
| 并行效率 | 98.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 7 | 53.588 | - |
| 规划模型 | 1 | 3.995 | - |
| 顺序总时间 | - | 57.582 | - |
| 并行总时间 | - | 54.614 | 1.05x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Does (Z)-1-chloro-2-methylbut-1-ene exhibit optical activity? | 大模型 | 1.026 | 8.681 | 7.655 | 2 |
| 2 | Does (3aR,7aS,E)-8-(chloromethylene)hexahydro-4,7-methanoisobenzofuran-1,3-dione exhibit optical activity? | 大模型 | 8.681 | 16.336 | 7.655 | 3 |
| 3 | Does (2R,3S)-2,3-dimethylsuccinic acid exhibit optical activity? | 大模型 | 16.336 | 23.992 | 7.655 | 4 |
| 4 | Does (2R,3R)-2,3-dimethylsuccinic acid exhibit optical activity? | 大模型 | 23.992 | 31.647 | 7.655 | 5 |
| 5 | Does (R)-cyclohex-3-en-1-ol exhibit optical activity? | 大模型 | 31.647 | 39.303 | 7.655 | 6 |
| 6 | Does (1s,3s,5s)-cyclohexane-1,3,5-triol exhibit optical activity? | 大模型 | 39.303 | 46.958 | 7.655 | 7 |
| 7 | Does 1-cyclopentyl-3-methylbutan-1-one exhibit optical activity? | 大模型 | 46.958 | 54.614 | 7.655 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            53.59s
+------------------------------------------------------------+
步骤 1 |########                                                    | 1.03s - 8.68s
步骤 2 |        #########                                           | 8.68s - 16.34s
步骤 3 |                 ########                                   | 16.34s - 23.99s
步骤 4 |                         #########                          | 23.99s - 31.65s
步骤 5 |                                  ########                  | 31.65s - 39.30s
步骤 6 |                                          #########         | 39.30s - 46.96s
步骤 7 |                                                   #########| 46.96s - 54.61s
```

