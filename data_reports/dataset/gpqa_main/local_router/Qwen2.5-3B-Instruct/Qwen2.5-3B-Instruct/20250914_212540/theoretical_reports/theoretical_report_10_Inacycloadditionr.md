# 问题 10 的理论性能分析报告

## 问题描述

In a cycloaddition reaction, two π systems combine to form a single-ring structure. These reactions can occur under two conditions including thermal and photochemical. These reactions follow the general mechanism given below.
Ethene + ethene (Heat) ----- cyclobutane
Mention the cycloaddition products of the following reactions.
(E)-penta-1,3-diene + acrylonitrile  ---> A
cyclopentadiene + methyl acrylate (Heat) ---> B

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
| 规划阶段总时间 (Planner) | 4.713 | 100% |
| 规划过程中启动的任务数 | 7 / 9 | 77.8% |
| 规划与执行重叠的任务数 | 7 / 9 | 77.8% |
| 第一个任务规划完成时间 | 0.978 | - |
| 最后一个任务规划完成时间 | 4.671 | - |
| 最后一个任务执行完成时间 | 6.677 | - |
| 任务总执行时间(累计) | 11.479 | - |
| 流水线加速比 | 3.69x | - |
| 并行效率 | 171.9% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 9 | 11.479 | - |
| 规划模型 | 1 | 13.140 | - |
| 顺序总时间 | - | 24.619 | - |
| 并行总时间 | - | 6.677 | 3.69x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the general mechanism of cycloaddition reactions? | 大模型 | 0.978 | 2.287 | 1.310 | 2 |
| 2 | What is the structure of (E)-penta-1,3-diene? | 大模型 | 1.497 | 2.652 | 1.155 | 3 |
| 3 | What is the structure of acrylonitrile? | 大模型 | 1.904 | 3.059 | 1.155 | 4 |
| 4 | What is the structure of cyclopentadiene? | 大模型 | 2.340 | 3.495 | 1.155 | 5 |
| 5 | What is the structure of methyl acrylate? | 大模型 | 2.747 | 3.902 | 1.155 | 6 |
| 6 | What is the expected product structure for reaction A? | 大模型 | 3.239 | 4.704 | 1.465 | 7 |
| 7 | What is the expected product structure for reaction B? | 大模型 | 3.902 | 5.367 | 1.465 | 8 |
| 8 | What are the key differences between the two reactions? | 大模型 | 5.367 | 6.677 | 1.310 | 9 |
| 9 | What are the cycloaddition products of these reactions? | 大模型 | 5.367 | 6.677 | 1.310 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            5.70s
+------------------------------------------------------------+
步骤 1 |#############                                               | 0.98s - 2.29s
步骤 2 |     ############                                           | 1.50s - 2.65s
步骤 3 |         ############                                       | 1.90s - 3.06s
步骤 4 |              ############                                  | 2.34s - 3.49s
步骤 5 |                  ############                              | 2.75s - 3.90s
步骤 6 |                       ################                     | 3.24s - 4.70s
步骤 7 |                              ################              | 3.90s - 5.37s
步骤 8 |                                              ##############| 5.37s - 6.68s
步骤 9 |                                              ##############| 5.37s - 6.68s
```

