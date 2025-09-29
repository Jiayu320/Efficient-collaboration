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
| 规划阶段总时间 (Planner) | 4.194 | 100% |
| 规划过程中启动的任务数 | 8 / 9 | 88.9% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 1.146 | - |
| 最后一个任务规划完成时间 | 4.177 | - |
| 最后一个任务执行完成时间 | 5.948 | - |
| 任务总执行时间(累计) | 10.560 | - |
| 流水线加速比 | 3.37x | - |
| 并行效率 | 177.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 0.943 | - |
| 大模型任务 | 8 | 9.617 | - |
| 规划模型 | 1 | 9.506 | - |
| 顺序总时间 | - | 20.065 | - |
| 并行总时间 | - | 5.948 | 3.37x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Does 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene have a carbon bonded to four distinct groups (e.g., R1, R2, R3, R4)? Using molecular structure rules, what is the chirality status of this compound? | 大模型 | 1.146 | 2.366 | 1.219 | 2 |
| 2 | For 2,3,3,3-tetrafluoroprop-1-ene, are the substituents on the double bond asymmetric (e.g., R-CHF=CHF-R vs. symmetric)? Does this enable enantiomeric pairs? What is the optical activity conclusion? | 大模型 | 1.559 | 2.709 | 1.150 | 3 |
| 3 | In di(cyclohex-2-en-1-ylidene)methane, are the two cyclohex-2-en-1-yl groups symmetrically or asymmetrically substituted? Does this create a planar system with no symmetry plane? What is the optical activity conclusion? | 大模型 | 1.966 | 3.186 | 1.219 | 4 |
| 4 | For 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene, is the cyclopenta-1,3-diene system planar and asymmetric? Does the substituent on the double bond break symmetry? What is the optical activity conclusion? | 大模型 | 2.385 | 3.604 | 1.219 | 5 |
| 5 | Does 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene have a planar asymmetric system where mirror images cannot superimpose? Using double bond substitution rules, what is the optical activity conclusion? | 大模型 | 2.754 | 3.974 | 1.219 | 6 |
| 6 | Does [1,1'-biphenyl]-3,3'-diol have a plane of symmetry or chiral centers? Using diol symmetry principles, what is the optical activity conclusion? | 大模型 | 3.069 | 4.219 | 1.150 | 7 |
| 7 | For 8,8-dichlorobicyclo[4.2.0]octan-7-one, are there four distinct groups on any carbon (e.g., chloro, oxygen, cycloalkyl, methyl)? Using bicyclic stereochemistry rules, what is the chirality conclusion? | 大模型 | 3.498 | 4.718 | 1.219 | 8 |
| 8 | Does cyclopent-2-en-1-one have a planar asymmetric system with enantiomers? Using diene substitution symmetry rules, what is the optical activity conclusion? | 大模型 | 3.786 | 5.006 | 1.219 | 9 |
| 9 | Count the number of compounds from Steps 1-8 that exhibit optical isomerism. Using the formula N = sum of Step results, what is the final count of optically active compounds? | 小模型 | 5.006 | 5.948 | 0.943 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            4.80s
+------------------------------------------------------------+
步骤 1 |###############                                             | 1.15s - 2.37s
步骤 2 |     ##############                                         | 1.56s - 2.71s
步骤 3 |          ###############                                   | 1.97s - 3.19s
步骤 4 |               ###############                              | 2.38s - 3.60s
步骤 5 |                    ###############                         | 2.75s - 3.97s
步骤 6 |                        ##############                      | 3.07s - 4.22s
步骤 7 |                             ###############                | 3.50s - 4.72s
步骤 8 |                                ################            | 3.79s - 5.01s
步骤 9 |                                                ############| 5.01s - 5.95s
```

