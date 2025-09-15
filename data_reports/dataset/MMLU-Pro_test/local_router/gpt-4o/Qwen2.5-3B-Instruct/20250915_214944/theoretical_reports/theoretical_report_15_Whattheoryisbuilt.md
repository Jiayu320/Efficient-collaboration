# 问题 15 的理论性能分析报告

## 问题描述

What theory is built around the principle that 'people make choices regarding how to behave based on values and beliefs'?

A. Social Learning
B. Contingency
C. Operant Conditioning
D. Evolutionary
E. Classical
F. Expectancy
G. Psychoanalytic
H. Instrumental
I. Cognitive Dissonance
J. Humanistic

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 4.180 | 100% |
| 规划过程中启动的任务数 | 4 / 7 | 57.1% |
| 规划与执行重叠的任务数 | 4 / 7 | 57.1% |
| 第一个任务规划完成时间 | 0.992 | - |
| 最后一个任务规划完成时间 | 4.138 | - |
| 最后一个任务执行完成时间 | 7.534 | - |
| 任务总执行时间(累计) | 7.619 | - |
| 流水线加速比 | 2.38x | - |
| 并行效率 | 101.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 7 | 7.619 | - |
| 大模型任务 | 0 | 0.000 | - |
| 规划模型 | 1 | 10.331 | - |
| 顺序总时间 | - | 17.951 | - |
| 并行总时间 | - | 7.534 | 2.38x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the core principle of the theory being asked about? | 小模型 | 0.992 | 1.992 | 1.000 | 2 |
| 2 | Which theories emphasize the role of internal values and beliefs in decision-making? | 小模型 | 1.992 | 3.146 | 1.155 | 3 |
| 3 | Which theory among the options explicitly focuses on values and beliefs as decision-making factors? | 小模型 | 3.146 | 4.224 | 1.077 | 4 |
| 4 | What theory is best described as focusing on human potential and self-determination? | 小模型 | 2.480 | 3.558 | 1.077 | 5 |
| 5 | Which theory aligns with the idea that behavior is shaped by conscious choices influenced by values? | 小模型 | 4.224 | 5.379 | 1.155 | 6 |
| 6 | Which theory among the options is most closely related to the principle of choice based on values? | 小模型 | 5.379 | 6.456 | 1.077 | 7 |
| 7 | What is the final theory that best matches the principle of choice based on values and beliefs? | 小模型 | 6.456 | 7.534 | 1.077 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            6.54s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 0.99s - 1.99s
步骤 2 |         ##########                                         | 1.99s - 3.15s
步骤 4 |             ##########                                     | 2.48s - 3.56s
步骤 3 |                   ##########                               | 3.15s - 4.22s
步骤 5 |                             ###########                    | 4.22s - 5.38s
步骤 6 |                                        ##########          | 5.38s - 6.46s
步骤 7 |                                                  ##########| 6.46s - 7.53s
```

