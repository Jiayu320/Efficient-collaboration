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
| 大模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 3.590 | 100% |
| 规划过程中启动的任务数 | 5 / 6 | 83.3% |
| 规划与执行重叠的任务数 | 5 / 6 | 83.3% |
| 第一个任务规划完成时间 | 1.034 | - |
| 最后一个任务规划完成时间 | 3.548 | - |
| 最后一个任务执行完成时间 | 5.902 | - |
| 任务总执行时间(累计) | 8.169 | - |
| 流水线加速比 | 2.90x | - |
| 并行效率 | 138.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 6 | 8.169 | - |
| 规划模型 | 1 | 8.927 | - |
| 顺序总时间 | - | 17.096 | - |
| 并行总时间 | - | 5.902 | 2.90x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What are the three main prohibitions in Islamic finance compared to conventional finance? | 大模型 | 1.034 | 2.499 | 1.465 | 2 |
| 2 | What is the definition of 'interest' in financial terms? | 大模型 | 1.483 | 2.638 | 1.155 | 3 |
| 3 | What are the three main types of transactions prohibited in Islamic finance? | 大模型 | 2.499 | 3.808 | 1.310 | 4 |
| 4 | What does 'sinful investment' mean in the context of Islamic finance? | 大模型 | 2.452 | 3.762 | 1.310 | 5 |
| 5 | What does 'backed by both tangible and intangible assets' mean in financial terms? | 大模型 | 2.972 | 4.282 | 1.310 | 6 |
| 6 | Which answer choice correctly identifies all three prohibitions and the asset requirement? | 大模型 | 4.282 | 5.902 | 1.620 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            4.87s
+------------------------------------------------------------+
步骤 1 |##################                                          | 1.03s - 2.50s
步骤 2 |     ##############                                         | 1.48s - 2.64s
步骤 4 |                 ################                           | 2.45s - 3.76s
步骤 3 |                  ################                          | 2.50s - 3.81s
步骤 5 |                       #################                    | 2.97s - 4.28s
步骤 6 |                                        ####################| 4.28s - 5.90s
```

