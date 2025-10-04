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
| 规划阶段总时间 (Planner) | 2.045 | 100% |
| 规划过程中启动的任务数 | 2 / 3 | 66.7% |
| 规划与执行重叠的任务数 | 1 / 3 | 33.3% |
| 第一个任务规划完成时间 | 0.963 | - |
| 最后一个任务规划完成时间 | 2.003 | - |
| 最后一个任务执行完成时间 | 4.574 | - |
| 任务总执行时间(累计) | 3.610 | - |
| 流水线加速比 | 1.41x | - |
| 并行效率 | 78.9% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.310 | - |
| 大模型任务 | 2 | 2.300 | - |
| 规划模型 | 1 | 2.846 | - |
| 顺序总时间 | - | 6.456 | - |
| 并行总时间 | - | 4.574 | 1.41x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What are the structural formulas of all compounds listed? | 大模型 | 0.963 | 2.045 | 1.081 | 2 |
| 2 | For each compound, identify whether it contains chiral centers (carbon atoms with four different substituents). | 大模型 | 2.045 | 3.264 | 1.219 | 3 |
| 3 | Count the number of compounds with at least one chiral center. | 小模型 | 3.264 | 4.574 | 1.310 | 4 |

## 理论执行甘特图

```
时间轴:
0                                                            3.61s
+------------------------------------------------------------+
步骤 1 |#################                                           | 0.96s - 2.04s
步骤 2 |                 #####################                      | 2.04s - 3.26s
步骤 3 |                                      ######################| 3.26s - 4.57s
```

