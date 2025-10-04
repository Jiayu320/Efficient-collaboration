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
| 路由模型 (saves/Qwen3-1.7B-Thinking/full/train_2025-09-25-23-33-09) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 5.612 | 100% |
| 规划过程中启动的任务数 | 8 / 8 | 100.0% |
| 规划与执行重叠的任务数 | 7 / 8 | 87.5% |
| 第一个任务规划完成时间 | 1.216 | - |
| 最后一个任务规划完成时间 | 5.570 | - |
| 最后一个任务执行完成时间 | 6.651 | - |
| 任务总执行时间(累计) | 8.648 | - |
| 流水线加速比 | 2.35x | - |
| 并行效率 | 130.0% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 8 | 8.648 | - |
| 规划模型 | 1 | 6.989 | - |
| 顺序总时间 | - | 15.637 | - |
| 并行总时间 | - | 6.651 | 2.35x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the molecular formula of 1-methyl-4-(prop-1-en-2-yl)cyclohex-1-ene? | 大模型 | 1.216 | 2.297 | 1.081 | 2 |
| 2 | What is the molecular formula of 2,3,3,3-tetrafluoroprop-1-ene? | 大模型 | 1.820 | 2.901 | 1.081 | 3 |
| 3 | What is the molecular formula of di(cyclohex-2-en-1-ylidene)methane? | 大模型 | 2.424 | 3.505 | 1.081 | 4 |
| 4 | What is the molecular formula of 5-(5-methylhexan-2-ylidene)cyclopenta-1,3-diene? | 大模型 | 3.098 | 4.179 | 1.081 | 5 |
| 5 | What is the molecular formula of 3-(2-methylbut-1-en-1-ylidene)cyclohex-1-ene? | 大模型 | 3.787 | 4.868 | 1.081 | 6 |
| 6 | What is the molecular formula of [1,1'-biphenyl]-3,3'-diol? | 大模型 | 4.376 | 5.457 | 1.081 | 7 |
| 7 | What is the molecular formula of 8,8-dichlorobicyclo[4.2.0]octan-7-one? | 大模型 | 5.065 | 6.146 | 1.081 | 8 |
| 8 | What is the molecular formula of cyclopent-2-en-1-one? | 大模型 | 5.570 | 6.651 | 1.081 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            5.43s
+------------------------------------------------------------+
步骤 1 |###########                                                 | 1.22s - 2.30s
步骤 2 |      ############                                          | 1.82s - 2.90s
步骤 3 |             ############                                   | 2.42s - 3.51s
步骤 4 |                    ############                            | 3.10s - 4.18s
步骤 5 |                            ############                    | 3.79s - 4.87s
步骤 6 |                                  ############              | 4.38s - 5.46s
步骤 7 |                                          ############      | 5.06s - 6.15s
步骤 8 |                                                ############| 5.57s - 6.65s
```

