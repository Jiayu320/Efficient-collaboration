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
| 路由模型 (saves/Qwen3-1.7B-Thinking/full/train_2025-09-25-23-33-09) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 7.775 | 100% |
| 规划过程中启动的任务数 | 8 / 9 | 88.9% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 1.455 | - |
| 最后一个任务规划完成时间 | 7.733 | - |
| 最后一个任务执行完成时间 | 9.267 | - |
| 任务总执行时间(累计) | 10.218 | - |
| 流水线加速比 | 3.51x | - |
| 并行效率 | 110.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.155 | - |
| 大模型任务 | 8 | 9.063 | - |
| 规划模型 | 1 | 22.326 | - |
| 顺序总时间 | - | 32.544 | - |
| 并行总时间 | - | 9.267 | 3.51x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Is the ring in 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene chiral? What substituents are bonded to the cyclohexene ring's carbon with the methyl group? | 大模型 | 1.455 | 2.605 | 1.150 | 2 |
| 2 | For 2,3,3,3-tetrafluoroprop-1-ene, does the chiral carbon at position 2 have four different substituents? List the substituents. | 大模型 | 2.256 | 3.337 | 1.081 | 3 |
| 3 | Is the ring in di(cyclohex-2-en-1-ylidene)methane chiral? Are the two cyclohexene groups bonded to the central carbon identical? | 大模型 | 3.042 | 4.192 | 1.150 | 4 |
| 4 | For 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene, does the chiral carbon in the cyclopentane ring have four different substituents? List them. | 大模型 | 3.927 | 5.077 | 1.150 | 5 |
| 5 | Is the ring in 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene chiral? Are the substituents at the chiral center distinct? | 大模型 | 4.742 | 5.892 | 1.150 | 6 |
| 6 | For [1,1'-biphenyl]-3,3'-diol, are the two phenyl rings asymmetric? Does the presence of two identical substituents negate chirality? | 大模型 | 5.542 | 6.692 | 1.150 | 7 |
| 7 | Is the ring in 8,8-dichlorobicyclo[4.2.0]octan-7-one chiral? Are the substituents at the cyclohexene ring's carbon distinct? | 大模型 | 6.413 | 7.563 | 1.150 | 8 |
| 8 | For cyclopent-2-en-1-one, is the double bond symmetric? Does this symmetry affect chirality? | 大模型 | 7.031 | 8.112 | 1.081 | 9 |
| 9 | Summing all compounds with chiral centers, how many total exhibit optical activity? | 小模型 | 8.112 | 9.267 | 1.155 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            7.81s
+------------------------------------------------------------+
步骤 1 |########                                                    | 1.46s - 2.61s
步骤 2 |      ########                                              | 2.26s - 3.34s
步骤 3 |            #########                                       | 3.04s - 4.19s
步骤 4 |                  #########                                 | 3.93s - 5.08s
步骤 5 |                         #########                          | 4.74s - 5.89s
步骤 6 |                               #########                    | 5.54s - 6.69s
步骤 7 |                                      ########              | 6.41s - 7.56s
步骤 8 |                                          #########         | 7.03s - 8.11s
步骤 9 |                                                   ######## | 8.11s - 9.27s
```

