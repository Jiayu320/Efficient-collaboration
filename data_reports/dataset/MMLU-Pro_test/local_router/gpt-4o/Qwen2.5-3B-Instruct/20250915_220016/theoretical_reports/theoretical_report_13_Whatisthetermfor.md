# 问题 13 的理论性能分析报告

## 问题描述

What is the term for the 'rule of thumb' type of bias in decision making?

A. Framing bias
B. Availability bias
C. Representativeness bias
D. Self-serving bias
E. Hindsight bias
F. Over-confidence bias
G. Confirmation bias
H. Optimism bias
I. Anchoring bias
J. Heuristics

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
| 规划阶段总时间 (Planner) | 2.466 | 100% |
| 规划过程中启动的任务数 | 2 / 4 | 50.0% |
| 规划与执行重叠的任务数 | 2 / 4 | 50.0% |
| 第一个任务规划完成时间 | 0.978 | - |
| 最后一个任务规划完成时间 | 2.424 | - |
| 最后一个任务执行完成时间 | 4.610 | - |
| 任务总执行时间(累计) | 3.632 | - |
| 流水线加速比 | 2.12x | - |
| 并行效率 | 78.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 4 | 3.632 | - |
| 规划模型 | 1 | 6.118 | - |
| 顺序总时间 | - | 9.750 | - |
| 并行总时间 | - | 4.610 | 2.12x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What are common types of cognitive biases in decision making? | 大模型 | 0.978 | 1.920 | 0.943 | 2 |
| 2 | Which biases are related to using mental shortcuts or heuristics? | 大模型 | 1.920 | 2.828 | 0.908 | 3 |
| 3 | Which of the listed options specifically refers to a heuristic or rule-of-thumb approach? | 大模型 | 2.828 | 3.702 | 0.873 | 4 |
| 4 | How does this identified bias differ from other listed options? | 大模型 | 3.702 | 4.610 | 0.908 | 5 |

## 理论执行甘特图

```
时间轴:
0                                                            3.63s
+------------------------------------------------------------+
步骤 1 |###############                                             | 0.98s - 1.92s
步骤 2 |               ###############                              | 1.92s - 2.83s
步骤 3 |                              ###############               | 2.83s - 3.70s
步骤 4 |                                             ###############| 3.70s - 4.61s
```

