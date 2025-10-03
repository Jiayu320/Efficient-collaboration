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
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (gpt-4o) | 0.735 | 144.50 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 4.147 | 100% |
| 规划过程中启动的任务数 | 8 / 10 | 80.0% |
| 规划与执行重叠的任务数 | 8 / 10 | 80.0% |
| 第一个任务规划完成时间 | 1.116 | - |
| 最后一个任务规划完成时间 | 4.126 | - |
| 最后一个任务执行完成时间 | 43.483 | - |
| 任务总执行时间(累计) | 153.335 | - |
| 流水线加速比 | 3.63x | - |
| 并行效率 | 352.6% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 9 | 145.680 | - |
| 大模型任务 | 1 | 7.655 | - |
| 规划模型 | 1 | 4.555 | - |
| 顺序总时间 | - | 157.890 | - |
| 并行总时间 | - | 43.483 | 3.63x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Determine if the compound 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene has a chiral center or axis. | 小模型 | 1.116 | 17.302 | 16.187 | 2 |
| 2 | Determine if the compound 2,3,3,3-tetrafluoroprop-1-ene has a chiral center or axis. | 小模型 | 1.441 | 17.628 | 16.187 | 3 |
| 3 | Determine if the compound di(cyclohex-2-en-1-ylidene)methane has a chiral center or axis. | 小模型 | 1.766 | 17.953 | 16.187 | 4 |
| 4 | Determine if the compound 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene has a chiral center or axis. | 小模型 | 2.126 | 18.313 | 16.187 | 5 |
| 5 | Determine if the compound 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene has a chiral center or axis. | 小模型 | 2.493 | 18.679 | 16.187 | 6 |
| 6 | Determine if the compound [1,1'-biphenyl]-3,3'-diol has a chiral center or axis. | 小模型 | 2.811 | 18.998 | 16.187 | 7 |
| 7 | Determine if the compound 8,8-dichlorobicyclo[4.2.0]octan-7-one has a chiral center or axis. | 小模型 | 3.178 | 19.365 | 16.187 | 8 |
| 8 | Determine if the compound cyclopent-2-en-1-one has a chiral center or axis. | 小模型 | 3.455 | 19.641 | 16.187 | 9 |
| 9 | For each compound from Steps 1-8, assess if the presence of a chiral center or axis leads to optical activity. | 大模型 | 19.641 | 27.297 | 7.655 | 10 |
| 10 | Count how many compounds exhibit optical activity based on the assessments from Step 9. | 小模型 | 27.297 | 43.483 | 16.187 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            42.37s
+------------------------------------------------------------+
步骤 1 |######################                                      | 1.12s - 17.30s
步骤 2 |#######################                                     | 1.44s - 17.63s
步骤 3 |#######################                                     | 1.77s - 17.95s
步骤 4 | #######################                                    | 2.13s - 18.31s
步骤 5 | #######################                                    | 2.49s - 18.68s
步骤 6 |  #######################                                   | 2.81s - 19.00s
步骤 7 |  #######################                                   | 3.18s - 19.36s
步骤 8 |   #######################                                  | 3.45s - 19.64s
步骤 9 |                          ###########                       | 19.64s - 27.30s
步骤 10 |                                     #######################| 27.30s - 43.48s
```

