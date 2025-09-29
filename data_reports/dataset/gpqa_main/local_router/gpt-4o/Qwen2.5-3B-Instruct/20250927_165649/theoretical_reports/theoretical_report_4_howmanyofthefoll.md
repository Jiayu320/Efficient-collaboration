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
| 路由模型 (saves/Qwen3-4B-Thinking/full/ep5) | 0.690 | 184.10 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 3.531 | 100% |
| 规划过程中启动的任务数 | 8 / 9 | 88.9% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 1.087 | - |
| 最后一个任务规划完成时间 | 3.515 | - |
| 最后一个任务执行完成时间 | 5.579 | - |
| 任务总执行时间(累计) | 10.634 | - |
| 流水线加速比 | 3.60x | - |
| 并行效率 | 190.6% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.155 | - |
| 大模型任务 | 8 | 9.479 | - |
| 规划模型 | 1 | 9.462 | - |
| 顺序总时间 | - | 20.096 | - |
| 并行总时间 | - | 5.579 | 3.60x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For compound 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene, does the sp²-planar cyclohexenylidene system and allylic substitution create non-superimposable mirror images? | 大模型 | 1.087 | 2.306 | 1.219 | 2 |
| 2 | For compound 2,3,3,3-tetrafluoroprop-1-ene, does the sp²-planar allene system exhibit inherent asymmetry leading to optical isomerism? | 大模型 | 1.396 | 2.546 | 1.150 | 3 |
| 3 | For di(cyclohex-2-en-1-ylidene)methane, does the bicyclic sp²-planar system produce non-superimposable mirror images? | 大模型 | 1.700 | 2.920 | 1.219 | 4 |
| 4 | For 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene, does the sp²-planar fused system generate optical isomers? | 大模型 | 1.999 | 3.219 | 1.219 | 5 |
| 5 | For 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene, does the sp²-planar substitution create planar asymmetry? | 大模型 | 2.298 | 3.517 | 1.219 | 6 |
| 6 | For [1,1'-biphenyl]-3,3'-diol, is the planar biphenyl structure symmetric and achiral? | 大模型 | 2.559 | 3.640 | 1.081 | 7 |
| 7 | For 8,8-dichlorobicyclo[4.2.0]octan-7-one, does the tertiary carbon with four distinct groups (Cl, CH₂Cl, cyclopropyl, and cyclobutyl) constitute a chiral center? | 大模型 | 2.950 | 4.100 | 1.150 | 8 |
| 8 | For cyclopent-2-en-1-one, does the sp²-planar ketone system lack symmetry and exhibit optical activity? | 大模型 | 3.205 | 4.424 | 1.219 | 9 |
| 9 | Count the number of compounds exhibiting optical activity from Steps 1 to 8. What is the final count? | 小模型 | 4.424 | 5.579 | 1.155 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            4.49s
+------------------------------------------------------------+
步骤 1 |################                                            | 1.09s - 2.31s
步骤 2 |    ###############                                         | 1.40s - 2.55s
步骤 3 |        ################                                    | 1.70s - 2.92s
步骤 4 |            ################                                | 2.00s - 3.22s
步骤 5 |                ################                            | 2.30s - 3.52s
步骤 6 |                   ###############                          | 2.56s - 3.64s
步骤 7 |                        ################                    | 2.95s - 4.10s
步骤 8 |                            ################                | 3.20s - 4.42s
步骤 9 |                                            ################| 4.42s - 5.58s
```

