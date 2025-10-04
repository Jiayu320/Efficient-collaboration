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

A. 5
B. 3
C. 6
D. 4

Please select the correct answer and provide the final option letter and its corresponding content.

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (gpt-4o) | 0.735 | 144.50 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 3.448 | 100% |
| 规划过程中启动的任务数 | 9 / 9 | 100.0% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 1.074 | - |
| 最后一个任务规划完成时间 | 3.427 | - |
| 最后一个任务执行完成时间 | 19.614 | - |
| 任务总执行时间(累计) | 77.430 | - |
| 流水线加速比 | 4.20x | - |
| 并行效率 | 394.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 16.187 | - |
| 大模型任务 | 8 | 61.243 | - |
| 规划模型 | 1 | 5.012 | - |
| 顺序总时间 | - | 82.442 | - |
| 并行总时间 | - | 19.614 | 4.20x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Does 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene exhibit optical activity? | 大模型 | 1.074 | 8.730 | 7.655 | 2 |
| 2 | Does 2,3,3,3-tetrafluoroprop-1-ene exhibit optical activity? | 大模型 | 1.358 | 9.013 | 7.655 | 3 |
| 3 | Does di(cyclohex-2-en-1-ylidene)methane exhibit optical activity? | 大模型 | 1.642 | 9.297 | 7.655 | 4 |
| 4 | Does 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene exhibit optical activity? | 大模型 | 1.960 | 9.615 | 7.655 | 5 |
| 5 | Does 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene exhibit optical activity? | 大模型 | 2.285 | 9.941 | 7.655 | 6 |
| 6 | Does [1,1'-biphenyl]-3,3'-diol exhibit optical activity? | 大模型 | 2.562 | 10.217 | 7.655 | 7 |
| 7 | Does 8,8-dichlorobicyclo[4.2.0]octan-7-one exhibit optical activity? | 大模型 | 2.887 | 10.543 | 7.655 | 8 |
| 8 | Does cyclopent-2-en-1-one exhibit optical activity? | 大模型 | 3.123 | 10.778 | 7.655 | 9 |
| 9 | How many of the compounds are optically active? | 小模型 | 3.427 | 19.614 | 16.187 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            18.54s
+------------------------------------------------------------+
步骤 1 |########################                                    | 1.07s - 8.73s
步骤 2 |#########################                                   | 1.36s - 9.01s
步骤 3 | #########################                                  | 1.64s - 9.30s
步骤 4 |  #########################                                 | 1.96s - 9.62s
步骤 5 |   #########################                                | 2.29s - 9.94s
步骤 6 |    #########################                               | 2.56s - 10.22s
步骤 7 |     #########################                              | 2.89s - 10.54s
步骤 8 |      #########################                             | 3.12s - 10.78s
步骤 9 |       #####################################################| 3.43s - 19.61s
```

