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
| 规划阶段总时间 (Planner) | 24.361 | 100% |
| 规划过程中启动的任务数 | 2 / 11 | 18.2% |
| 规划与执行重叠的任务数 | 2 / 11 | 18.2% |
| 第一个任务规划完成时间 | 7.613 | - |
| 最后一个任务规划完成时间 | 24.301 | - |
| 最后一个任务执行完成时间 | 55.297 | - |
| 任务总执行时间(累计) | 101.272 | - |
| 流水线加速比 | 2.34x | - |
| 并行效率 | 183.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 32.373 | - |
| 大模型任务 | 9 | 68.899 | - |
| 规划模型 | 1 | 28.058 | - |
| 顺序总时间 | - | 129.330 | - |
| 并行总时间 | - | 55.297 | 2.34x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What does it mean for a molecule to exhibit optical activity, and what stereochemical criteria must be satisfied (chirality, absence of improper symmetry elements, and configurational stability)? | 小模型 | 7.613 | 23.800 | 16.187 | 2 |
| 2 | What practical diagnostic rules determine chirality for the stereogenic elements likely to appear here: (a) point chirality at sp3 carbons, (b) axial chirality in allenes/cumulenes (substituent rules at terminal carbons), (c) atropisomerism in biaryls (ortho substitution and rotational barrier), and (d) planar/ring chirality in constrained ring systems? | 大模型 | 23.800 | 31.455 | 7.655 | 3 |
| 3 | Does 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene contain any stereogenic element (e.g., an sp3 stereocenter on the ring with four different substituents) and thus exhibit optical activity? Identify the specific stereogenic element if present and justify. | 大模型 | 31.455 | 39.110 | 7.655 | 4 |
| 4 | Does 2,3,3,3-tetrafluoroprop-1-ene contain any stereogenic element (sp3 stereocenter, E/Z-defined chiral alkene, axial chirality), or is it achiral given the CH2 terminus on the double bond? | 大模型 | 31.455 | 39.110 | 7.655 | 5 |
| 5 | Treat di(cyclohex-2-en-1-ylidene)methane as an allene/cumulene: do both terminal cumulenic carbons bear two different substituents (R1 ≠ R2 at one end and R3 ≠ R4 at the other) so as to create axial chirality, or are the ends symmetrically substituted making it achiral? | 大模型 | 31.455 | 39.110 | 7.655 | 6 |
| 6 | For 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene, does the structure contain any sp3 stereocenter (in the side chain or ring) with four different substituents, or any axial/planar chirality arising from the exocyclic double bond and conjugated diene? | 大模型 | 31.455 | 39.110 | 7.655 | 7 |
| 7 | For 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene, does the molecule possess any stereogenic element (e.g., a ring sp3 stereocenter with four different substituents, or chirality in the side chain), or is it overall achiral? | 大模型 | 31.455 | 39.110 | 7.655 | 8 |
| 8 | Does [1,1'-biphenyl]-3,3'-diol exhibit axial chirality (atropisomerism)? Evaluate whether there is sufficient ortho substitution to hinder rotation about the biaryl bond and remove symmetry, or whether free rotation renders it achiral. | 大模型 | 31.455 | 39.110 | 7.655 | 9 |
| 9 | For 8,8-dichlorobicyclo[4.2.0]octan-7-one, analyze the bicyclic skeleton for inherent chirality: is there any mirror plane, inversion center, or improper axis preserved by the gem-dichloro and carbonyl placement, or does the substitution pattern remove all such symmetry to yield a chiral, optically active system? | 大模型 | 31.455 | 39.110 | 7.655 | 10 |
| 10 | Does cyclopent-2-en-1-one have any stereogenic element (point/axial/planar chirality), or is it planar and achiral? | 大模型 | 31.455 | 39.110 | 7.655 | 1 |
| 11 | Based on the yes/no determinations from Steps 3–10, how many of the eight compounds are optically active, and which ones are they? | 小模型 | 39.110 | 55.297 | 16.187 | 2 |

## 理论执行甘特图

```
时间轴:
0                                                            47.68s
+------------------------------------------------------------+
步骤 1 |####################                                        | 7.61s - 23.80s
步骤 2 |                    ##########                              | 23.80s - 31.45s
步骤 3 |                              #########                     | 31.45s - 39.11s
步骤 4 |                              #########                     | 31.45s - 39.11s
步骤 5 |                              #########                     | 31.45s - 39.11s
步骤 6 |                              #########                     | 31.45s - 39.11s
步骤 7 |                              #########                     | 31.45s - 39.11s
步骤 8 |                              #########                     | 31.45s - 39.11s
步骤 9 |                              #########                     | 31.45s - 39.11s
步骤 10 |                              #########                     | 31.45s - 39.11s
步骤 11 |                                       #####################| 39.11s - 55.30s
```

