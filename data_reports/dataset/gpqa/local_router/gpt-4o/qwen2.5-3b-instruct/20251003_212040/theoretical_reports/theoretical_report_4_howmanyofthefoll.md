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

A. 5
B. 3
C. 6
D. 4

Please select the correct answer and provide the final option letter and its corresponding content.

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
| 规划阶段总时间 (Planner) | 2.640 | 100% |
| 规划过程中启动的任务数 | 1 / 7 | 14.3% |
| 规划与执行重叠的任务数 | 1 / 7 | 14.3% |
| 第一个任务规划完成时间 | 0.967 | - |
| 最后一个任务规划完成时间 | 2.624 | - |
| 最后一个任务执行完成时间 | 23.933 | - |
| 任务总执行时间(累计) | 53.588 | - |
| 流水线加速比 | 2.51x | - |
| 并行效率 | 223.9% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 7 | 53.588 | - |
| 规划模型 | 1 | 6.388 | - |
| 顺序总时间 | - | 59.976 | - |
| 并行总时间 | - | 23.933 | 2.51x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Which compounds contain a non-planar, sp-hybridized carbon center with four distinct substituents, as required for optical isomerism? | 大模型 | 0.967 | 8.622 | 7.655 | 2 |
| 2 | Does 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene have a chiral carbon center with four distinct groups? | 大模型 | 8.622 | 16.278 | 7.655 | 3 |
| 3 | Is 2,3,3,3-tetrafluoroprop-1-ene planar and incapable of chirality due to sp² hybridization? | 大模型 | 8.622 | 16.278 | 7.655 | 4 |
| 4 | Does di(cyclohex-2-en-1-ylidene)methane exhibit planar allene geometry with no chiral centers? | 大模型 | 8.622 | 16.278 | 7.655 | 5 |
| 5 | Can 5-(5-methylhexan-2-en-1-ylidene)cyclopenta-1,3-diene form a non-planar, chiral system? | 大模型 | 8.622 | 16.278 | 7.655 | 6 |
| 6 | Why do compounds like [1,1'-biphenyl]-3,3'-diol lack optical activity despite having multiple double bonds? | 大模型 | 8.622 | 16.278 | 7.655 | 7 |
| 7 | How many compounds from the list satisfy the criteria for optical isomerism based on Steps 2-6? | 大模型 | 16.278 | 23.933 | 7.655 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            22.97s
+------------------------------------------------------------+
步骤 1 |####################                                        | 0.97s - 8.62s
步骤 2 |                    ####################                    | 8.62s - 16.28s
步骤 3 |                    ####################                    | 8.62s - 16.28s
步骤 4 |                    ####################                    | 8.62s - 16.28s
步骤 5 |                    ####################                    | 8.62s - 16.28s
步骤 6 |                    ####################                    | 8.62s - 16.28s
步骤 7 |                                        ####################| 16.28s - 23.93s
```

