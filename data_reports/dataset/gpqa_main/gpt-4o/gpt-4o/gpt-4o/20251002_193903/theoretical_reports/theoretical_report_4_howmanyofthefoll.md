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
| 规划阶段总时间 (Planner) | 3.939 | 100% |
| 规划过程中启动的任务数 | 1 / 9 | 11.1% |
| 规划与执行重叠的任务数 | 1 / 9 | 11.1% |
| 第一个任务规划完成时间 | 1.088 | - |
| 最后一个任务规划完成时间 | 3.918 | - |
| 最后一个任务执行完成时间 | 69.987 | - |
| 任务总执行时间(累计) | 68.899 | - |
| 流水线加速比 | 1.03x | - |
| 并行效率 | 98.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 9 | 68.899 | - |
| 规划模型 | 1 | 3.482 | - |
| 顺序总时间 | - | 72.381 | - |
| 并行总时间 | - | 69.987 | 1.03x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Determine if 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene has a chiral center. | 大模型 | 1.088 | 8.743 | 7.655 | 2 |
| 2 | Determine if 2,3,3,3-tetrafluoroprop-1-ene has a chiral center. | 大模型 | 8.743 | 16.399 | 7.655 | 3 |
| 3 | Determine if di(cyclohex-2-en-1-ylidene)methane has a chiral center. | 大模型 | 16.399 | 24.054 | 7.655 | 4 |
| 4 | Determine if 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene has a chiral center. | 大模型 | 24.054 | 31.710 | 7.655 | 5 |
| 5 | Determine if 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene has a chiral center. | 大模型 | 31.710 | 39.365 | 7.655 | 6 |
| 6 | Determine if [1,1'-biphenyl]-3,3'-diol exhibits axial chirality. | 大模型 | 39.365 | 47.020 | 7.655 | 7 |
| 7 | Determine if 8,8-dichlorobicyclo[4.2.0]octan-7-one has a chiral center. | 大模型 | 47.020 | 54.676 | 7.655 | 8 |
| 8 | Determine if cyclopent-2-en-1-one has a chiral center. | 大模型 | 54.676 | 62.331 | 7.655 | 9 |
| 9 | Conclude which compounds with chiral centers or axial chirality exhibit optical activity. | 大模型 | 62.331 | 69.987 | 7.655 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            68.90s
+------------------------------------------------------------+
步骤 1 |######                                                      | 1.09s - 8.74s
步骤 2 |      #######                                               | 8.74s - 16.40s
步骤 3 |             #######                                        | 16.40s - 24.05s
步骤 4 |                    ######                                  | 24.05s - 31.71s
步骤 5 |                          #######                           | 31.71s - 39.37s
步骤 6 |                                 #######                    | 39.37s - 47.02s
步骤 7 |                                        ######              | 47.02s - 54.68s
步骤 8 |                                              #######       | 54.68s - 62.33s
步骤 9 |                                                     #######| 62.33s - 69.99s
```

