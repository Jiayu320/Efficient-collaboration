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
| 规划阶段总时间 (Planner) | 29.482 | 100% |
| 规划过程中启动的任务数 | 9 / 16 | 56.2% |
| 规划与执行重叠的任务数 | 9 / 16 | 56.2% |
| 第一个任务规划完成时间 | 7.593 | - |
| 最后一个任务规划完成时间 | 29.423 | - |
| 最后一个任务执行完成时间 | 55.277 | - |
| 任务总执行时间(累计) | 139.549 | - |
| 流水线加速比 | 3.14x | - |
| 并行效率 | 252.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 32.373 | - |
| 大模型任务 | 14 | 107.176 | - |
| 规划模型 | 1 | 33.773 | - |
| 顺序总时间 | - | 173.322 | - |
| 并行总时间 | - | 55.277 | 3.14x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the definition of optical activity in small organic molecules, and what symmetry conditions (absence of mirror plane, inversion center, improper rotation) are required for a molecule to be chiral? | 小模型 | 7.593 | 23.780 | 16.187 | 2 |
| 2 | What stereogenic elements can cause optical activity in organic molecules (point chirality at sp3 carbons, axial chirality in allenes/cumulenes, atropisomerism in biaryls, planar or helical chirality), and what are the typical structural prerequisites for each? | 大模型 | 9.135 | 16.791 | 7.655 | 3 |
| 3 | What are the CIP priority rules and the method to determine whether an sp3 ring carbon is a stereogenic center by comparing the two ring paths (i.e., when the two paths from that carbon are constitutionally or stereochemically non-equivalent)? | 大模型 | 23.780 | 31.435 | 7.655 | 4 |
| 4 | What criteria determine axial chirality in allenes and related cumulenes, particularly the requirement for different substituent sets on both terminal double-bond carbons, and how is the presence or absence of symmetry assessed? | 大模型 | 23.780 | 31.435 | 7.655 | 5 |
| 5 | What structural features and rotational barrier thresholds are required for atropisomerism in biphenyls, and how do substitution patterns (e.g., ortho vs meta) affect both chirality and barrier to racemization at room temperature? | 大模型 | 23.780 | 31.435 | 7.655 | 6 |
| 6 | What dynamic processes (e.g., rapid rotation about single bonds, ring inversions, pyramidal inversion) can lead to racemization, and how should these be considered when deciding if optical activity will be observed under standard conditions? | 大模型 | 23.780 | 31.435 | 7.655 | 7 |
| 7 | For each of the eight IUPAC names provided, draw or otherwise specify the correct unambiguous 2D skeletal structures, ensuring correct placement of double bonds, ring connectivity, and substituent positions. | 大模型 | 15.819 | 23.474 | 7.655 | 8 |
| 8 | For 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene, does the molecule possess any stereogenic element(s) leading to optical activity at room temperature? Analyze point chirality at relevant ring carbons using CIP rules and ring-path inequivalence, and assess symmetry. | 大模型 | 31.435 | 39.091 | 7.655 | 9 |
| 9 | For 2,3,3,3-tetrafluoroprop-1-ene, does the molecule possess any stereogenic element(s) leading to optical activity? Evaluate possibilities for point chirality, E/Z isomerism, axial chirality, and overall symmetry. | 大模型 | 23.474 | 31.130 | 7.655 | 10 |
| 10 | For di(cyclohex-2-en-1-ylidene)methane, is the central system an allene/cumulene, and if so, does it meet the criteria for axial chirality? Assess substituent sets at both terminal carbons, symmetry, and potential optical activity. | 大模型 | 31.435 | 39.091 | 7.655 | 1 |
| 11 | For 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene, does the molecule exhibit optical activity? Evaluate point chirality at ring carbons, possible planar or axial chirality due to the exocyclic double bond, and the presence or absence of symmetry. | 大模型 | 31.435 | 39.091 | 7.655 | 2 |
| 12 | For 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene, does the molecule exhibit optical activity? Analyze point chirality at the substituted ring carbon using ring-path inequivalence, and check for symmetry elements. | 大模型 | 31.435 | 39.091 | 7.655 | 3 |
| 13 | For [1,1'-biphenyl]-3,3'-diol, does the substitution pattern lead to atropisomeric chirality with a sufficient rotational barrier for observable optical activity? Evaluate symmetry and rotation about the biaryl bond. | 大模型 | 31.435 | 39.091 | 7.655 | 4 |
| 14 | For 8,8-dichlorobicyclo[4.2.0]octan-7-one, does the framework possess point or topological chirality leading to optical activity? Examine potential stereocenters (considering identical geminal substituents), overall symmetry, and any inherent chirality in the bicyclic system. | 大模型 | 31.435 | 39.091 | 7.655 | 5 |
| 15 | For cyclopent-2-en-1-one, does the molecule exhibit any stereogenic elements or lack of symmetry that would result in optical activity? | 大模型 | 28.197 | 35.852 | 7.655 | 6 |
| 16 | Based on the conclusions for each compound in Steps 8–15, how many of the eight compounds exhibit optical activity under standard conditions? | 小模型 | 39.091 | 55.277 | 16.187 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            47.68s
+------------------------------------------------------------+
步骤 1 |####################                                        | 7.59s - 23.78s
步骤 2 | ##########                                                 | 9.14s - 16.79s
步骤 7 |          #########                                         | 15.82s - 23.47s
步骤 9 |                   ##########                               | 23.47s - 31.13s
步骤 3 |                    ##########                              | 23.78s - 31.44s
步骤 4 |                    ##########                              | 23.78s - 31.44s
步骤 5 |                    ##########                              | 23.78s - 31.44s
步骤 6 |                    ##########                              | 23.78s - 31.44s
步骤 15 |                         ##########                         | 28.20s - 35.85s
步骤 8 |                              #########                     | 31.44s - 39.09s
步骤 10 |                              #########                     | 31.44s - 39.09s
步骤 11 |                              #########                     | 31.44s - 39.09s
步骤 12 |                              #########                     | 31.44s - 39.09s
步骤 13 |                              #########                     | 31.44s - 39.09s
步骤 14 |                              #########                     | 31.44s - 39.09s
步骤 16 |                                       #####################| 39.09s - 55.28s
```

