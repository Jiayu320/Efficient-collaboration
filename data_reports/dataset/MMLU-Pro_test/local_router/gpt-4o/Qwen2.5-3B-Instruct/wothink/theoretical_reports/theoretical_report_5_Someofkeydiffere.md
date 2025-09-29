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
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 2.368 | 100% |
| 规划过程中启动的任务数 | 2 / 3 | 66.7% |
| 规划与执行重叠的任务数 | 2 / 3 | 66.7% |
| 第一个任务规划完成时间 | 1.090 | - |
| 最后一个任务规划完成时间 | 2.326 | - |
| 最后一个任务执行完成时间 | 4.402 | - |
| 任务总执行时间(累计) | 3.312 | - |
| 流水线加速比 | 1.49x | - |
| 并行效率 | 75.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 3 | 3.312 | - |
| 规划模型 | 1 | 3.253 | - |
| 顺序总时间 | - | 6.565 | - |
| 并行总时间 | - | 4.402 | 1.49x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the correct term for prohibited transactions in Islamic finance, as per the question's context? | 大模型 | 1.090 | 2.240 | 1.150 | 2 |
| 2 | Which option (A-J) lists the prohibited transaction types as 'Interest, Certain, Assured' for the first blank? | 大模型 | 2.240 | 3.321 | 1.081 | 3 |
| 3 | Which option (A-J) specifies 'Intangible assets' as the required backing for all financial products? | 大模型 | 3.321 | 4.402 | 1.081 | 4 |

## 理论执行甘特图

```
时间轴:
0                                                            3.31s
+------------------------------------------------------------+
步骤 1 |####################                                        | 1.09s - 2.24s
步骤 2 |                    ####################                    | 2.24s - 3.32s
步骤 3 |                                        ####################| 3.32s - 4.40s
```

