# 问题 5 的理论性能分析报告

## 问题描述

 Some of key differences between Islamic finance and conventional finance include - prohibition of charging and paying _______, prohibition on ______ and ______ transactions, prohibition of sinful investment and requirement for all financial products to be backed by __________.

A. Interest, Certain, Assured, Both tangible and intangible assets
B. Interest, Uncertain, Assured, Both tangible and intangible assets
C. Interest, Uncertain, Speculative, Intangible assets
D. Interest, Certain, Assured, Tangible assets
E. Interest, Uncertain, Assured, Intangible assets
F. Profit, Uncertain, Speculative, Tangible assets
G. Interest, Uncertain, Speculative, Tangible assets
H. Interest, Certain, Speculative, Intangible assets
I. Profit, Certain, Assured, Tangible assets
J. Interest, Certain, Speculative, Both tangible and intangible assets

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
| 规划阶段总时间 (Planner) | 1.988 | 100% |
| 规划过程中启动的任务数 | 3 / 4 | 75.0% |
| 规划与执行重叠的任务数 | 3 / 4 | 75.0% |
| 第一个任务规划完成时间 | 0.956 | - |
| 最后一个任务规划完成时间 | 1.972 | - |
| 最后一个任务执行完成时间 | 3.827 | - |
| 任务总执行时间(累计) | 4.761 | - |
| 流水线加速比 | 2.83x | - |
| 并行效率 | 124.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.310 | - |
| 大模型任务 | 3 | 3.451 | - |
| 规划模型 | 1 | 6.062 | - |
| 顺序总时间 | - | 10.823 | - |
| 并行总时间 | - | 3.827 | 2.83x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the prohibited charge in Islamic finance that includes interest and is explicitly forbidden by Quranic verses 2:275-276? | 小模型 | 0.956 | 2.266 | 1.310 | 2 |
| 2 | Which two transaction types are prohibited in Islamic finance: uncertain (maysir) or speculative (gharar), and which term correctly describes the prohibited nature of these transactions? | 大模型 | 1.255 | 2.405 | 1.150 | 3 |
| 3 | What must all financial products in Islamic finance be backed by to ensure they are asset-linked (fisabila), specifically requiring both tangible and intangible assets? | 大模型 | 1.527 | 2.608 | 1.081 | 4 |
| 4 | Using the answers from Steps 1 (prohibited charge), 2 (prohibited transaction type), and 3 (asset-backing requirement), which option (C, E, or J) correctly matches: Interest, Uncertain, Speculative, Both tangible and intangible assets? | 大模型 | 2.608 | 3.827 | 1.219 | 5 |

## 理论执行甘特图

```
时间轴:
0                                                            2.87s
+------------------------------------------------------------+
步骤 1 |###########################                                 | 0.96s - 2.27s
步骤 2 |      ########################                              | 1.25s - 2.41s
步骤 3 |           #######################                          | 1.53s - 2.61s
步骤 4 |                                  ##########################| 2.61s - 3.83s
```

