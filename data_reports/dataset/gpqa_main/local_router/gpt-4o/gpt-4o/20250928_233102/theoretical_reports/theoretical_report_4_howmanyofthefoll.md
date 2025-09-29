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
| 路由模型 (saves/Qwen3-4B-Thinking/full/ep5) | 0.690 | 184.10 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 3.900 | 100% |
| 规划过程中启动的任务数 | 9 / 10 | 90.0% |
| 规划与执行重叠的任务数 | 9 / 10 | 90.0% |
| 第一个任务规划完成时间 | 0.951 | - |
| 最后一个任务规划完成时间 | 3.884 | - |
| 最后一个任务执行完成时间 | 5.719 | - |
| 任务总执行时间(累计) | 11.364 | - |
| 流水线加速比 | 3.94x | - |
| 并行效率 | 198.7% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 0.943 | - |
| 大模型任务 | 9 | 10.421 | - |
| 规划模型 | 1 | 11.184 | - |
| 顺序总时间 | - | 22.548 | - |
| 并行总时间 | - | 5.719 | 3.94x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the definition of a chiral center in organic chemistry, specifically the requirement for a carbon to have four distinct substituents? | 小模型 | 0.951 | 1.893 | 0.943 | 2 |
| 2 | Does 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene contain a carbon with four distinct substituents (including ring position and substituent identity) that would make it chiral? | 大模型 | 1.893 | 3.113 | 1.219 | 3 |
| 3 | Does 2,3,3,3-tetrafluoroprop-1-ene have a carbon with four distinct substituents due to fluorine substitution symmetry, making it chiral? | 大模型 | 1.893 | 3.044 | 1.150 | 4 |
| 4 | For di(cyclohex-2-en-1-ylidene)methane, does the sp²-carbon in the enolidene groups have asymmetric substituents that create a non-superimposable mirror image? | 大模型 | 1.966 | 3.186 | 1.219 | 5 |
| 5 | Does 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene exhibit chirality from asymmetric substituents on the enolidene carbon? | 大模型 | 2.276 | 3.496 | 1.219 | 6 |
| 6 | Does 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene have spatial asymmetry on the enolidene substituent that creates optical activity? | 大模型 | 2.597 | 3.816 | 1.219 | 7 |
| 7 | Is [1,1'-biphenyl]-3,3'-diol chiral due to the diol groups creating a carbon with four distinct substituents? | 大模型 | 2.884 | 3.896 | 1.012 | 8 |
| 8 | Does 8,8-dichlorobicyclo[4.2.0]octan-7-one contain a tertiary carbon with four distinct substituents (including chloride and ring groups) that would make it chiral? | 大模型 | 3.243 | 4.393 | 1.150 | 9 |
| 9 | Does cyclopent-2-en-1-one have asymmetric substituents on its sp²-carbon that create optical activity? | 大模型 | 3.487 | 4.638 | 1.150 | 10 |
| 10 | Summing the 'yes' responses from Steps 2, 4, 5, 6, 7, 8, and 9, how many compounds exhibit optical activity? | 大模型 | 4.638 | 5.719 | 1.081 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            4.77s
+------------------------------------------------------------+
步骤 1 |###########                                                 | 0.95s - 1.89s
步骤 2 |           ################                                 | 1.89s - 3.11s
步骤 3 |           ###############                                  | 1.89s - 3.04s
步骤 4 |            ################                                | 1.97s - 3.19s
步骤 5 |                ################                            | 2.28s - 3.50s
步骤 6 |                    ################                        | 2.60s - 3.82s
步骤 7 |                        #############                       | 2.88s - 3.90s
步骤 8 |                            ###############                 | 3.24s - 4.39s
步骤 9 |                               ###############              | 3.49s - 4.64s
步骤 10 |                                              ##############| 4.64s - 5.72s
```

