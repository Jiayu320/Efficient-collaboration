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
| 路由模型 (gpt-5) | 6.407 | 50.57 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 13.090 | 100% |
| 规划过程中启动的任务数 | 3 / 4 | 75.0% |
| 规划与执行重叠的任务数 | 3 / 4 | 75.0% |
| 第一个任务规划完成时间 | 8.641 | - |
| 最后一个任务规划完成时间 | 13.031 | - |
| 最后一个任务执行完成时间 | 16.034 | - |
| 任务总执行时间(累计) | 7.219 | - |
| 流水线加速比 | 2.08x | - |
| 并行效率 | 45.0% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.000 | - |
| 大模型任务 | 3 | 6.219 | - |
| 规划模型 | 1 | 26.180 | - |
| 顺序总时间 | - | 33.399 | - |
| 并行总时间 | - | 16.034 | 2.08x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What are the complete, formal criteria for a molecule to exhibit optical activity, including definitions and diagnostic rules for point chirality, axial chirality (atropisomerism with rotational barrier requirements), planar and helical chirality, allenes/cumulenes, and the symmetry elements (mirror plane, inversion center, improper axis) that render a molecule achiral, as well as the role of dynamic interconversion on the measurement timescale? | 大模型 | 8.641 | 10.345 | 1.704 | 2 |
| 2 | For each of the eight IUPAC names provided, what is the unambiguous structural depiction (skeletal structures with ring connectivity, positions of double bonds including exocyclic/endocyclic, substitution patterns such as ortho/meta/para on biaryls, presence of allenic/cumulenic fragments, and any obvious symmetry elements) needed to evaluate chirality? | 大模型 | 10.520 | 12.777 | 2.257 | 3 |
| 3 | Applying the criteria from Step 1 to the structural depictions from Step 2, which of the eight compounds are chiral (identifying the operative stereogenic element) and remain configurationally stable against racemization at ambient conditions, and which are achiral due to symmetry or rapid interconversion? | 大模型 | 12.777 | 15.034 | 2.257 | 4 |
| 4 | Based on the chiral compound list from Step 3, what is the total number of compounds that will exhibit optical activity? | 小模型 | 15.034 | 16.034 | 1.000 | 5 |

## 理论执行甘特图

```
时间轴:
0                                                            7.39s
+------------------------------------------------------------+
步骤 1 |#############                                               | 8.64s - 10.34s
步骤 2 |               ##################                           | 10.52s - 12.78s
步骤 3 |                                 ##################         | 12.78s - 15.03s
步骤 4 |                                                   #########| 15.03s - 16.03s
```

