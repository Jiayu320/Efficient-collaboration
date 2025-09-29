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
| 规划阶段总时间 (Planner) | 3.743 | 100% |
| 规划过程中启动的任务数 | 8 / 9 | 88.9% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 1.021 | - |
| 最后一个任务规划完成时间 | 3.726 | - |
| 最后一个任务执行完成时间 | 5.670 | - |
| 任务总执行时间(累计) | 10.560 | - |
| 流水线加速比 | 3.37x | - |
| 并行效率 | 186.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 9 | 10.560 | - |
| 规划模型 | 1 | 8.528 | - |
| 顺序总时间 | - | 19.088 | - |
| 并行总时间 | - | 5.670 | 3.37x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene, how many stereocenters (C with four distinct groups) are present? | 大模型 | 1.021 | 2.241 | 1.219 | 2 |
| 2 | Does 2,3,3,3-tetrafluoroprop-1-ene contain an unsymmetrical sp²-hybridized carbon (e.g., enol ether or enediol) that exhibits planar chirality? | 大模型 | 1.391 | 2.541 | 1.150 | 3 |
| 3 | For di(cyclohex-2-en-1-ylidene)methane, does its planar structure lack a plane of symmetry, making it non-superimposable on its mirror image? | 大模型 | 1.717 | 2.936 | 1.219 | 4 |
| 4 | Does 5-(5-methylhexan-2-en-1-ylidene)cyclopenta-1,3-diene have an asymmetrical allylic quaternary carbon (e.g., sp²-carbon with distinct substituents)? | 大模型 | 2.081 | 3.231 | 1.150 | 5 |
| 5 | For 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene, how many stereocenters are present, and are they non-superimposable on their mirror images? | 大模型 | 2.434 | 3.653 | 1.219 | 6 |
| 6 | Does [1,1'-biphenyl]-3,3'-diol have two enolic hydroxyl groups with asymmetrical substitution, leading to optical activity? | 大模型 | 2.716 | 3.866 | 1.150 | 7 |
| 7 | For 8,8-dichlorobicyclo[4.2.0]octan-7-one, is the allylic quaternary carbon sp²-hybridized and unsymmetrical, or does it lack chirality due to symmetry? | 大模型 | 3.113 | 4.332 | 1.219 | 8 |
| 8 | Does cyclopent-2-en-1-one contain an unsymmetrical sp²-hybridized carbon (e.g., enol ether) that acts as a planar stereocenter? | 大模型 | 3.439 | 4.589 | 1.150 | 9 |
| 9 | Summing the results from Steps 1-8, how many compounds exhibit optical activity? | 大模型 | 4.589 | 5.670 | 1.081 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            4.65s
+------------------------------------------------------------+
步骤 1 |###############                                             | 1.02s - 2.24s
步骤 2 |    ###############                                         | 1.39s - 2.54s
步骤 3 |        ################                                    | 1.72s - 2.94s
步骤 4 |             ###############                                | 2.08s - 3.23s
步骤 5 |                  ###############                           | 2.43s - 3.65s
步骤 6 |                     ###############                        | 2.72s - 3.87s
步骤 7 |                          ################                  | 3.11s - 4.33s
步骤 8 |                               ###############              | 3.44s - 4.59s
步骤 9 |                                              ##############| 4.59s - 5.67s
```

