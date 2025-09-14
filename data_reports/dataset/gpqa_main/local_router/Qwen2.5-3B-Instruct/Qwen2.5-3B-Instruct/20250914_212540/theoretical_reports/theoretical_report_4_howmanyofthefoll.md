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
| 小模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 大模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 6.301 | 100% |
| 规划过程中启动的任务数 | 9 / 10 | 90.0% |
| 规划与执行重叠的任务数 | 9 / 10 | 90.0% |
| 第一个任务规划完成时间 | 0.949 | - |
| 最后一个任务规划完成时间 | 6.258 | - |
| 最后一个任务执行完成时间 | 7.718 | - |
| 任务总执行时间(累计) | 10.774 | - |
| 流水线加速比 | 3.28x | - |
| 并行效率 | 139.6% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 10 | 10.774 | - |
| 规划模型 | 1 | 14.545 | - |
| 顺序总时间 | - | 25.319 | - |
| 并行总时间 | - | 7.718 | 3.28x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What determines if a compound exhibits optical activity? | 大模型 | 0.949 | 2.104 | 1.155 | 2 |
| 2 | Is 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene chiral? | 大模型 | 2.104 | 3.182 | 1.077 | 3 |
| 3 | Is 2,3,3,3-tetrafluoroprop-1-ene chiral? | 大模型 | 2.143 | 3.221 | 1.077 | 4 |
| 4 | Is di(cyclohex-2-en-1-ylidene)methane chiral? | 大模型 | 2.705 | 3.782 | 1.077 | 5 |
| 5 | Is 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene chiral? | 大模型 | 3.337 | 4.414 | 1.077 | 6 |
| 6 | Is 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene chiral? | 大模型 | 3.983 | 5.061 | 1.077 | 7 |
| 7 | Is [1,1'-biphenyl]-3,3'-diol chiral? | 大模型 | 4.531 | 5.608 | 1.077 | 8 |
| 8 | Is 8,8-dichlorobicyclo[4.2.0]octan-7-one chiral? | 大模型 | 5.177 | 6.254 | 1.077 | 9 |
| 9 | Is cyclopent-2-en-1-one chiral? | 大模型 | 5.640 | 6.718 | 1.077 | 10 |
| 10 | How many of these compounds exhibit optical activity? | 大模型 | 6.718 | 7.718 | 1.000 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            6.77s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 0.95s - 2.10s
步骤 2 |          #########                                         | 2.10s - 3.18s
步骤 3 |          ##########                                        | 2.14s - 3.22s
步骤 4 |               ##########                                   | 2.71s - 3.78s
步骤 5 |                     #########                              | 3.34s - 4.41s
步骤 6 |                          ##########                        | 3.98s - 5.06s
步骤 7 |                               ##########                   | 4.53s - 5.61s
步骤 8 |                                     ##########             | 5.18s - 6.25s
步骤 9 |                                         ##########         | 5.64s - 6.72s
步骤 10 |                                                   #########| 6.72s - 7.72s
```

