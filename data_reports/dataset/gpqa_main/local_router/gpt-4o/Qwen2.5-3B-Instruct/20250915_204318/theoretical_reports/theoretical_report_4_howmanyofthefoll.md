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
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 6.778 | 100% |
| 规划过程中启动的任务数 | 10 / 11 | 90.9% |
| 规划与执行重叠的任务数 | 10 / 11 | 90.9% |
| 第一个任务规划完成时间 | 0.949 | - |
| 最后一个任务规划完成时间 | 6.736 | - |
| 最后一个任务执行完成时间 | 8.201 | - |
| 任务总执行时间(累计) | 10.984 | - |
| 流水线加速比 | 3.28x | - |
| 并行效率 | 133.9% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 2.155 | - |
| 大模型任务 | 9 | 8.830 | - |
| 规划模型 | 1 | 15.949 | - |
| 顺序总时间 | - | 26.934 | - |
| 并行总时间 | - | 8.201 | 3.28x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What determines if a compound exhibits optical activity? | 大模型 | 0.949 | 1.892 | 0.943 | 2 |
| 2 | What is the condition for a compound to have a plane of symmetry? | 小模型 | 1.892 | 2.969 | 1.077 | 3 |
| 3 | How do functional groups affect the plane of symmetry in a compound? | 大模型 | 2.969 | 3.947 | 0.977 | 4 |
| 4 | Is 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene chiral? | 大模型 | 3.947 | 4.958 | 1.012 | 5 |
| 5 | Is 2,3,3,3-tetrafluoroprop-1-ene chiral? | 大模型 | 3.947 | 4.889 | 0.943 | 6 |
| 6 | Is di(cyclohex-2-en-1-ylidene)methane chiral? | 大模型 | 3.947 | 4.924 | 0.977 | 7 |
| 7 | Is 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene chiral? | 大模型 | 4.306 | 5.318 | 1.012 | 8 |
| 8 | Is 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene chiral? | 大模型 | 4.952 | 5.964 | 1.012 | 9 |
| 9 | Is [1,1'-biphenyl]-3,3'-diol chiral? | 大模型 | 5.500 | 6.477 | 0.977 | 10 |
| 10 | Is 8,8-dichlorobicyclo[4.2.0]octan-7-one chiral? | 大模型 | 6.146 | 7.123 | 0.977 | 1 |
| 11 | How many of the analyzed compounds are chiral? | 小模型 | 7.123 | 8.201 | 1.077 | 2 |

## 理论执行甘特图

```
时间轴:
0                                                            7.25s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 0.95s - 1.89s
步骤 2 |       #########                                            | 1.89s - 2.97s
步骤 3 |                ########                                    | 2.97s - 3.95s
步骤 4 |                        #########                           | 3.95s - 4.96s
步骤 5 |                        ########                            | 3.95s - 4.89s
步骤 6 |                        ########                            | 3.95s - 4.92s
步骤 7 |                           #########                        | 4.31s - 5.32s
步骤 8 |                                 ########                   | 4.95s - 5.96s
步骤 9 |                                     ########               | 5.50s - 6.48s
步骤 10 |                                          #########         | 6.15s - 7.12s
步骤 11 |                                                   #########| 7.12s - 8.20s
```

