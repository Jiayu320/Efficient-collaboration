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
| 路由模型 (gemini-2.5-pro) | 2.510 | 93.75 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 4.579 | 100% |
| 规划过程中启动的任务数 | 1 / 3 | 33.3% |
| 规划与执行重叠的任务数 | 1 / 3 | 33.3% |
| 第一个任务规划完成时间 | 3.310 | - |
| 最后一个任务规划完成时间 | 4.547 | - |
| 最后一个任务执行完成时间 | 9.240 | - |
| 任务总执行时间(累计) | 5.930 | - |
| 流水线加速比 | 1.84x | - |
| 并行效率 | 64.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.000 | - |
| 大模型任务 | 2 | 4.930 | - |
| 规划模型 | 1 | 11.064 | - |
| 顺序总时间 | - | 16.995 | - |
| 并行总时间 | - | 9.240 | 1.84x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What are the definitive structural criteria for a molecule to be chiral and thus exhibit optical activity? Your answer should include the role of stereocenters, planes of symmetry, centers of inversion, and specific cases like atropisomerism in substituted biphenyls. | 大模型 | 3.310 | 4.737 | 1.427 | 2 |
| 2 | For each of the 8 compounds provided, analyze its structure based on the criteria from Step 1. Determine whether each compound is chiral or achiral. Provide a list of only the compounds that are determined to be chiral (optically active). | 大模型 | 4.737 | 8.240 | 3.503 | 3 |
| 3 | Based on the list of chiral compounds from Step 2, what is the total number of compounds that exhibit optical activity? | 小模型 | 8.240 | 9.240 | 1.000 | 4 |

## 理论执行甘特图

```
时间轴:
0                                                            5.93s
+------------------------------------------------------------+
步骤 1 |##############                                              | 3.31s - 4.74s
步骤 2 |              ###################################           | 4.74s - 8.24s
步骤 3 |                                                 ###########| 8.24s - 9.24s
```

