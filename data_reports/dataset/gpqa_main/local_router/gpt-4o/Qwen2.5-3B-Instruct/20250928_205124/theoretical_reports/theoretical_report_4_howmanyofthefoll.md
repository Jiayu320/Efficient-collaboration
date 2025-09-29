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
| 规划阶段总时间 (Planner) | 3.547 | 100% |
| 规划过程中启动的任务数 | 8 / 9 | 88.9% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 1.114 | - |
| 最后一个任务规划完成时间 | 3.531 | - |
| 最后一个任务执行完成时间 | 5.632 | - |
| 任务总执行时间(累计) | 10.650 | - |
| 流水线加速比 | 3.34x | - |
| 并行效率 | 189.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.310 | - |
| 大模型任务 | 8 | 9.340 | - |
| 规划模型 | 1 | 8.142 | - |
| 顺序总时间 | - | 18.793 | - |
| 并行总时间 | - | 5.632 | 3.34x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For compound 1, does any carbon have four distinct groups (e.g., -CH(CH₃), -C(CH₂CH₃), -C(CH₂CH₂CH₃), -C₆H₄)? What is the chirality status? | 大模型 | 1.114 | 2.333 | 1.219 | 2 |
| 2 | For compound 2, is the molecule symmetric such that mirror-image isomers are identical (e.g., identical substituents on sp² carbons)? Does symmetry eliminate optical activity? | 大模型 | 1.412 | 2.563 | 1.150 | 3 |
| 3 | For compound 3, are both cyclohexenylidene groups identical and symmetrically equivalent, preventing superimposable mirror images? What is the optical activity status? | 大模型 | 1.700 | 2.851 | 1.150 | 4 |
| 4 | For compound 4, does the diekström symmetry of cyclopenta-1,3-diene with a substituted side chain make the molecule superimposable on its mirror image? What is the result? | 大模型 | 2.032 | 3.251 | 1.219 | 5 |
| 5 | For compound 5, is the cyclohexene ring substituted in a way that creates a chiral center with four distinct groups? What is the chirality status? | 大模型 | 2.314 | 3.534 | 1.219 | 6 |
| 6 | For compound 6, does the diol configuration (1,2-diol) allow for a plane of symmetry, eliminating optical isomerism? What is the conclusion? | 大模型 | 2.607 | 3.688 | 1.081 | 7 |
| 7 | For compound 7, does the bicyclic structure with identical substituents possess a plane of symmetry, making it optically inactive? What is the result? | 大模型 | 2.879 | 4.029 | 1.150 | 8 |
| 8 | For compound 8, does the cyclopentenone ring have a plane of symmetry through the ketone and substituents, eliminating optical activity? What is the conclusion? | 大模型 | 3.172 | 4.323 | 1.150 | 9 |
| 9 | Sum the optical activity flags from Steps 1-8 (1 for active, 0 for inactive). What is the total count of optically active compounds? | 小模型 | 4.323 | 5.632 | 1.310 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            4.52s
+------------------------------------------------------------+
步骤 1 |################                                            | 1.11s - 2.33s
步骤 2 |   ################                                         | 1.41s - 2.56s
步骤 3 |       ################                                     | 1.70s - 2.85s
步骤 4 |            ################                                | 2.03s - 3.25s
步骤 5 |               #################                            | 2.31s - 3.53s
步骤 6 |                   ###############                          | 2.61s - 3.69s
步骤 7 |                       ###############                      | 2.88s - 4.03s
步骤 8 |                           ###############                  | 3.17s - 4.32s
步骤 9 |                                          ##################| 4.32s - 5.63s
```

