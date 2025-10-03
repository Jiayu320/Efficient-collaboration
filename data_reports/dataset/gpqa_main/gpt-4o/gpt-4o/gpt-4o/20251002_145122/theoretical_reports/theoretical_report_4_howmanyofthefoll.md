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
| 规划阶段总时间 (Planner) | 3.621 | 100% |
| 规划过程中启动的任务数 | 8 / 9 | 88.9% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 1.088 | - |
| 最后一个任务规划完成时间 | 3.600 | - |
| 最后一个任务执行完成时间 | 18.558 | - |
| 任务总执行时间(累计) | 68.899 | - |
| 流水线加速比 | 3.93x | - |
| 并行效率 | 371.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 8 | 61.243 | - |
| 大模型任务 | 1 | 7.655 | - |
| 规划模型 | 1 | 3.974 | - |
| 顺序总时间 | - | 72.872 | - |
| 并行总时间 | - | 18.558 | 3.93x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Determine if 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene has a chiral center. | 小模型 | 1.088 | 8.743 | 7.655 | 2 |
| 2 | Determine if 2,3,3,3-tetrafluoroprop-1-ene has a chiral center. | 小模型 | 1.386 | 9.041 | 7.655 | 3 |
| 3 | Determine if di(cyclohex-2-en-1-ylidene)methane has a chiral center. | 小模型 | 1.683 | 9.339 | 7.655 | 4 |
| 4 | Determine if 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene has a chiral center. | 小模型 | 2.015 | 9.671 | 7.655 | 5 |
| 5 | Determine if 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene has a chiral center. | 小模型 | 2.354 | 10.010 | 7.655 | 6 |
| 6 | Determine if [1,1'-biphenyl]-3,3'-diol has an axis of chirality. | 小模型 | 2.659 | 10.314 | 7.655 | 7 |
| 7 | Determine if 8,8-dichlorobicyclo[4.2.0]octan-7-one has a chiral center. | 小模型 | 2.998 | 10.653 | 7.655 | 8 |
| 8 | Determine if cyclopent-2-en-1-one has a chiral center. | 小模型 | 3.247 | 10.903 | 7.655 | 9 |
| 9 | Based on Steps 1-8, count how many compounds exhibit optical activity. | 大模型 | 10.903 | 18.558 | 7.655 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            17.47s
+------------------------------------------------------------+
步骤 1 |##########################                                  | 1.09s - 8.74s
步骤 2 | ##########################                                 | 1.39s - 9.04s
步骤 3 |  ##########################                                | 1.68s - 9.34s
步骤 4 |   ##########################                               | 2.02s - 9.67s
步骤 5 |    ##########################                              | 2.35s - 10.01s
步骤 6 |     ##########################                             | 2.66s - 10.31s
步骤 7 |      ##########################                            | 3.00s - 10.65s
步骤 8 |       ##########################                           | 3.25s - 10.90s
步骤 9 |                                 ###########################| 10.90s - 18.56s
```

