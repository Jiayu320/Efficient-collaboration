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
| 规划阶段总时间 (Planner) | 3.660 | 100% |
| 规划过程中启动的任务数 | 6 / 6 | 100.0% |
| 规划与执行重叠的任务数 | 5 / 6 | 83.3% |
| 第一个任务规划完成时间 | 1.020 | - |
| 最后一个任务规划完成时间 | 3.618 | - |
| 最后一个任务执行完成时间 | 4.773 | - |
| 任务总执行时间(累计) | 6.701 | - |
| 流水线加速比 | 3.27x | - |
| 并行效率 | 140.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 5 | 5.620 | - |
| 大模型任务 | 1 | 1.081 | - |
| 规划模型 | 1 | 8.927 | - |
| 顺序总时间 | - | 15.628 | - |
| 并行总时间 | - | 4.773 | 3.27x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What are the core principles of Islamic finance that differ from conventional finance? | 大模型 | 1.020 | 2.101 | 1.081 | 2 |
| 2 | Which of the options lists the prohibited types of transactions in Islamic finance? | 小模型 | 2.101 | 3.256 | 1.155 | 3 |
| 3 | Which option correctly identifies the prohibited transaction type related to interest (Haraam)? | 小模型 | 3.256 | 4.333 | 1.077 | 4 |
| 4 | Which option correctly identifies the prohibition on certain types of transactions (e.g., speculative or uncertain)? | 小模型 | 3.256 | 4.410 | 1.155 | 5 |
| 5 | Which option correctly identifies the prohibition on assured transactions? | 小模型 | 3.256 | 4.333 | 1.077 | 6 |
| 6 | Which option correctly identifies the requirement for all financial products to be backed by tangible or intangible assets? | 小模型 | 3.618 | 4.773 | 1.155 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            3.75s
+------------------------------------------------------------+
步骤 1 |#################                                           | 1.02s - 2.10s
步骤 2 |                 ##################                         | 2.10s - 3.26s
步骤 3 |                                   #################        | 3.26s - 4.33s
步骤 4 |                                   ###################      | 3.26s - 4.41s
步骤 5 |                                   #################        | 3.26s - 4.33s
步骤 6 |                                         ################## | 3.62s - 4.77s
```

