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
| 小模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 4.728 | 100% |
| 规划过程中启动的任务数 | 8 / 9 | 88.9% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 0.992 | - |
| 最后一个任务规划完成时间 | 4.685 | - |
| 最后一个任务执行完成时间 | 6.462 | - |
| 任务总执行时间(累计) | 8.103 | - |
| 流水线加速比 | 3.29x | - |
| 并行效率 | 125.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 9 | 8.103 | - |
| 规划模型 | 1 | 13.140 | - |
| 顺序总时间 | - | 21.243 | - |
| 并行总时间 | - | 6.462 | 3.29x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What are the key differences between Islamic finance and conventional finance? | 大模型 | 0.992 | 1.934 | 0.943 | 2 |
| 2 | What is prohibited in terms of interest-related activities in Islamic finance? | 大模型 | 1.934 | 2.808 | 0.873 | 3 |
| 3 | What types of transactions are prohibited in Islamic finance? | 大模型 | 1.934 | 2.842 | 0.908 | 4 |
| 4 | What is required for all financial products in Islamic finance? | 大模型 | 2.354 | 3.227 | 0.873 | 5 |
| 5 | Which answer choices contain the correct terms for prohibited interest-related activities? | 大模型 | 2.860 | 3.768 | 0.908 | 6 |
| 6 | Which answer choices contain the correct terms for prohibited transactions? | 大模型 | 3.309 | 4.217 | 0.908 | 7 |
| 7 | Which answer choices contain the correct terms for required asset types? | 大模型 | 3.772 | 4.680 | 0.908 | 8 |
| 8 | Which answer choice matches all three identified criteria? | 大模型 | 4.680 | 5.623 | 0.943 | 9 |
| 9 | What is the correct answer among the options provided? | 大模型 | 5.623 | 6.462 | 0.839 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            5.47s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 0.99s - 1.93s
步骤 2 |          #########                                         | 1.93s - 2.81s
步骤 3 |          ##########                                        | 1.93s - 2.84s
步骤 4 |              ##########                                    | 2.35s - 3.23s
步骤 5 |                    ##########                              | 2.86s - 3.77s
步骤 6 |                         ##########                         | 3.31s - 4.22s
步骤 7 |                              ##########                    | 3.77s - 4.68s
步骤 8 |                                        ##########          | 4.68s - 5.62s
步骤 9 |                                                  ##########| 5.62s - 6.46s
```

