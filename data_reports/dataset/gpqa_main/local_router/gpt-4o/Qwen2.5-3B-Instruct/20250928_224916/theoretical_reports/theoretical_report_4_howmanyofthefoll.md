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
| 规划阶段总时间 (Planner) | 3.368 | 100% |
| 规划过程中启动的任务数 | 8 / 9 | 88.9% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 1.016 | - |
| 最后一个任务规划完成时间 | 3.352 | - |
| 最后一个任务执行完成时间 | 5.353 | - |
| 任务总执行时间(累计) | 10.495 | - |
| 流水线加速比 | 3.11x | - |
| 并行效率 | 196.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.155 | - |
| 大模型任务 | 8 | 9.340 | - |
| 规划模型 | 1 | 6.149 | - |
| 顺序总时间 | - | 16.644 | - |
| 并行总时间 | - | 5.353 | 3.11x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Does 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene possess a plane of symmetry, and if so, what is its orientation? | 大模型 | 1.016 | 2.235 | 1.219 | 2 |
| 2 | Does 2,3,3,3-tetrafluoroprop-1-ene exhibit symmetry across the double bond plane, and does it contain any chirality centers? | 大模型 | 1.309 | 2.459 | 1.150 | 3 |
| 3 | Is di(cyclohex-2-en-1-ylidene)methane symmetric with respect to any plane, including those through double bonds? | 大模型 | 1.581 | 2.800 | 1.219 | 4 |
| 4 | Does 5-(5-methylhexan-2-en-1-ylidene)cyclopenta-1,3-diene lack a plane of symmetry, and are its substituents asymmetrically arranged? | 大模型 | 1.907 | 3.126 | 1.219 | 5 |
| 5 | Does 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene have a symmetry plane, and are its double bond substituents enantiomeric? | 大模型 | 2.222 | 3.441 | 1.219 | 6 |
| 6 | Does [1,1'-biphenyl]-3,3'-diol possess a plane of symmetry through its central carbon-carbon bond? | 大模型 | 2.483 | 3.494 | 1.012 | 7 |
| 7 | Is 8,8-dichlorobicyclo[4.2.0]octan-7-one symmetric with respect to any plane, including through its exocyclic double bond? | 大模型 | 2.803 | 3.953 | 1.150 | 8 |
| 8 | Does cyclopent-2-en-1-one lack a plane of symmetry, and are its substituents asymmetrically arranged? | 大模型 | 3.047 | 4.198 | 1.150 | 9 |
| 9 | Count the compounds from Steps 1-8 that lack any plane of symmetry. What is this count? | 小模型 | 4.198 | 5.353 | 1.155 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            4.34s
+------------------------------------------------------------+
步骤 1 |################                                            | 1.02s - 2.24s
步骤 2 |    ###############                                         | 1.31s - 2.46s
步骤 3 |       #################                                    | 1.58s - 2.80s
步骤 4 |            #################                               | 1.91s - 3.13s
步骤 5 |                #################                           | 2.22s - 3.44s
步骤 6 |                    ##############                          | 2.48s - 3.49s
步骤 7 |                        ################                    | 2.80s - 3.95s
步骤 8 |                            ################                | 3.05s - 4.20s
步骤 9 |                                            ################| 4.20s - 5.35s
```

