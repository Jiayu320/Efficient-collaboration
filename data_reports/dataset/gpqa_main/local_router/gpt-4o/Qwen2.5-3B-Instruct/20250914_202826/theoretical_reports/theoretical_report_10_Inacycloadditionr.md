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
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 5.360 | 100% |
| 规划过程中启动的任务数 | 10 / 10 | 100.0% |
| 规划与执行重叠的任务数 | 8 / 10 | 80.0% |
| 第一个任务规划完成时间 | 1.034 | - |
| 最后一个任务规划完成时间 | 5.317 | - |
| 最后一个任务执行完成时间 | 6.270 | - |
| 任务总执行时间(累计) | 9.392 | - |
| 流水线加速比 | 3.82x | - |
| 并行效率 | 149.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 10 | 9.392 | - |
| 规划模型 | 1 | 14.545 | - |
| 顺序总时间 | - | 23.936 | - |
| 并行总时间 | - | 6.270 | 3.82x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the general rule for cycloaddition reactions between two π systems? | 大模型 | 1.034 | 1.976 | 0.943 | 2 |
| 2 | What is the structure of (E)-penta-1,3-diene? | 大模型 | 1.553 | 2.461 | 0.908 | 3 |
| 3 | What is the structure of acrylonitrile? | 大模型 | 1.961 | 2.869 | 0.908 | 4 |
| 4 | How do we predict the product structure for reaction A based on the cycloaddition mechanism? | 大模型 | 2.869 | 3.881 | 1.012 | 5 |
| 5 | What is the structure of cyclopentadiene? | 大模型 | 3.000 | 3.908 | 0.908 | 6 |
| 6 | What is the structure of methyl acrylate? | 大模型 | 3.407 | 4.315 | 0.908 | 7 |
| 7 | How do we predict the product structure for reaction B based on the cycloaddition mechanism? | 大模型 | 4.315 | 5.327 | 1.012 | 8 |
| 8 | What is the final product structure for reaction A? | 大模型 | 4.447 | 5.389 | 0.943 | 9 |
| 9 | What is the final product structure for reaction B? | 大模型 | 5.327 | 6.270 | 0.943 | 10 |
| 10 | What are the cycloaddition products of these reactions? | 大模型 | 5.317 | 6.225 | 0.908 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            5.24s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 1.03s - 1.98s
步骤 2 |     ###########                                            | 1.55s - 2.46s
步骤 3 |          ###########                                       | 1.96s - 2.87s
步骤 4 |                     ###########                            | 2.87s - 3.88s
步骤 5 |                      ##########                            | 3.00s - 3.91s
步骤 6 |                           ##########                       | 3.41s - 4.32s
步骤 7 |                                     ############           | 4.32s - 5.33s
步骤 8 |                                       ##########           | 4.45s - 5.39s
步骤 10 |                                                 ########## | 5.32s - 6.23s
步骤 9 |                                                 ###########| 5.33s - 6.27s
```

