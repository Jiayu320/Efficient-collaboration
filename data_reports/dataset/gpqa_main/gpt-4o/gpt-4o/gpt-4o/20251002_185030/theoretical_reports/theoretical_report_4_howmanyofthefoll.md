# 问题 4 的理论性能分析报告

## 问题描述

how many of the following compounds exhibit optical activity?
1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene
2,3,3,3-tetrafluoroprop-1-ene
di(cyclohex-2-en-1-ylidene)methane
5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene
3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene
[1,1'-biphenyl]-3,3'-diol
8,8-dichlorobicyclo[4.2.0]octan-7-one
cyclopent-2-en-1-one

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
| 规划阶段总时间 (Planner) | 3.538 | 100% |
| 规划过程中启动的任务数 | 1 / 8 | 12.5% |
| 规划与执行重叠的任务数 | 1 / 8 | 12.5% |
| 第一个任务规划完成时间 | 1.081 | - |
| 最后一个任务规划完成时间 | 3.517 | - |
| 最后一个任务执行完成时间 | 62.324 | - |
| 任务总执行时间(累计) | 61.243 | - |
| 流水线加速比 | 1.05x | - |
| 并行效率 | 98.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 8 | 61.243 | - |
| 规划模型 | 1 | 4.396 | - |
| 顺序总时间 | - | 65.639 | - |
| 并行总时间 | - | 62.324 | 1.05x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Determine if 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene exhibits optical activity | 大模型 | 1.081 | 8.736 | 7.655 | 2 |
| 2 | Determine if 2,3,3,3-tetrafluoroprop-1-ene exhibits optical activity | 大模型 | 8.736 | 16.392 | 7.655 | 3 |
| 3 | Determine if di(cyclohex-2-en-1-ylidene)methane exhibits optical activity | 大模型 | 16.392 | 24.047 | 7.655 | 4 |
| 4 | Determine if 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene exhibits optical activity | 大模型 | 24.047 | 31.703 | 7.655 | 5 |
| 5 | Determine if 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene exhibits optical activity | 大模型 | 31.703 | 39.358 | 7.655 | 6 |
| 6 | Determine if [1,1'-biphenyl]-3,3'-diol exhibits optical activity | 大模型 | 39.358 | 47.014 | 7.655 | 7 |
| 7 | Determine if 8,8-dichlorobicyclo[4.2.0]octan-7-one exhibits optical activity | 大模型 | 47.014 | 54.669 | 7.655 | 8 |
| 8 | Determine if cyclopent-2-en-1-one exhibits optical activity | 大模型 | 54.669 | 62.324 | 7.655 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            61.24s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 1.08s - 8.74s
步骤 2 |       #######                                              | 8.74s - 16.39s
步骤 3 |              ########                                      | 16.39s - 24.05s
步骤 4 |                      #######                               | 24.05s - 31.70s
步骤 5 |                             ########                       | 31.70s - 39.36s
步骤 6 |                                     #######                | 39.36s - 47.01s
步骤 7 |                                            ########        | 47.01s - 54.67s
步骤 8 |                                                    ####### | 54.67s - 62.32s
```

