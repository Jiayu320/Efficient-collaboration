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
| 规划阶段总时间 (Planner) | 6.680 | 100% |
| 规划过程中启动的任务数 | 8 / 17 | 47.1% |
| 规划与执行重叠的任务数 | 8 / 17 | 47.1% |
| 第一个任务规划完成时间 | 1.136 | - |
| 最后一个任务规划完成时间 | 6.659 | - |
| 最后一个任务执行完成时间 | 26.587 | - |
| 任务总执行时间(累计) | 130.142 | - |
| 流水线加速比 | 5.16x | - |
| 并行效率 | 489.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 17 | 130.142 | - |
| 大模型任务 | 0 | 0.000 | - |
| 规划模型 | 1 | 6.950 | - |
| 顺序总时间 | - | 137.092 | - |
| 并行总时间 | - | 26.587 | 5.16x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Examine the structure of 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene to determine if it has a chiral center. | 小模型 | 1.136 | 8.792 | 7.655 | 2 |
| 2 | Examine the structure of 2,3,3,3-tetrafluoroprop-1-ene to determine if it has a chiral center. | 小模型 | 1.482 | 9.138 | 7.655 | 3 |
| 3 | Examine the structure of di(cyclohex-2-en-1-ylidene)methane to determine if it has a chiral center. | 小模型 | 1.828 | 9.484 | 7.655 | 4 |
| 4 | Examine the structure of 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene to determine if it has a chiral center. | 小模型 | 2.209 | 9.864 | 7.655 | 5 |
| 5 | Examine the structure of 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene to determine if it has a chiral center. | 小模型 | 2.597 | 10.252 | 7.655 | 6 |
| 6 | Examine the structure of [1,1'-biphenyl]-3,3'-diol to determine if it has a chiral center. | 小模型 | 2.936 | 10.591 | 7.655 | 7 |
| 7 | Examine the structure of 8,8-dichlorobicyclo[4.2.0]octan-7-one to determine if it has a chiral center. | 小模型 | 3.323 | 10.979 | 7.655 | 8 |
| 8 | Examine the structure of cyclopent-2-en-1-one to determine if it has a chiral center. | 小模型 | 3.621 | 11.276 | 7.655 | 9 |
| 9 | Assess the symmetry of 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene to determine optical activity. | 小模型 | 8.792 | 16.447 | 7.655 | 10 |
| 10 | Assess the symmetry of 2,3,3,3-tetrafluoroprop-1-ene to determine optical activity. | 小模型 | 9.138 | 16.793 | 7.655 | 1 |
| 11 | Assess the symmetry of di(cyclohex-2-en-1-ylidene)methane to determine optical activity. | 小模型 | 9.484 | 17.139 | 7.655 | 2 |
| 12 | Assess the symmetry of 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene to determine optical activity. | 小模型 | 9.864 | 17.520 | 7.655 | 3 |
| 13 | Assess the symmetry of 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene to determine optical activity. | 小模型 | 10.252 | 17.907 | 7.655 | 4 |
| 14 | Assess the symmetry of [1,1'-biphenyl]-3,3'-diol to determine optical activity. | 小模型 | 10.591 | 18.247 | 7.655 | 5 |
| 15 | Assess the symmetry of 8,8-dichlorobicyclo[4.2.0]octan-7-one to determine optical activity. | 小模型 | 10.979 | 18.634 | 7.655 | 6 |
| 16 | Assess the symmetry of cyclopent-2-en-1-one to determine optical activity. | 小模型 | 11.276 | 18.932 | 7.655 | 7 |
| 17 | Count the number of compounds that are optically active based on symmetry assessments. | 小模型 | 18.932 | 26.587 | 7.655 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            25.45s
+------------------------------------------------------------+
步骤 1 |##################                                          | 1.14s - 8.79s
步骤 2 |##################                                          | 1.48s - 9.14s
步骤 3 | ##################                                         | 1.83s - 9.48s
步骤 4 |  ##################                                        | 2.21s - 9.86s
步骤 5 |   ##################                                       | 2.60s - 10.25s
步骤 6 |    ##################                                      | 2.94s - 10.59s
步骤 7 |     ##################                                     | 3.32s - 10.98s
步骤 8 |     ##################                                     | 3.62s - 11.28s
步骤 9 |                  ##################                        | 8.79s - 16.45s
步骤 10 |                  ##################                        | 9.14s - 16.79s
步骤 11 |                   ##################                       | 9.48s - 17.14s
步骤 12 |                    ##################                      | 9.86s - 17.52s
步骤 13 |                     ##################                     | 10.25s - 17.91s
步骤 14 |                      ##################                    | 10.59s - 18.25s
步骤 15 |                       ##################                   | 10.98s - 18.63s
步骤 16 |                       ##################                   | 11.28s - 18.93s
步骤 17 |                                         ###################| 18.93s - 26.59s
```

