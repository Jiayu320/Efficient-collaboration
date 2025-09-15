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
| 规划阶段总时间 (Planner) | 6.427 | 100% |
| 规划过程中启动的任务数 | 10 / 10 | 100.0% |
| 规划与执行重叠的任务数 | 9 / 10 | 90.0% |
| 第一个任务规划完成时间 | 1.048 | - |
| 最后一个任务规划完成时间 | 6.385 | - |
| 最后一个任务执行完成时间 | 7.540 | - |
| 任务总执行时间(累计) | 10.540 | - |
| 流水线加速比 | 3.33x | - |
| 并行效率 | 139.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 5 | 5.620 | - |
| 大模型任务 | 5 | 4.921 | - |
| 规划模型 | 1 | 14.545 | - |
| 顺序总时间 | - | 25.085 | - |
| 并行总时间 | - | 7.540 | 3.33x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the general outcome of a cycloaddition reaction between two π systems? | 小模型 | 1.048 | 2.125 | 1.077 | 2 |
| 2 | What is the structure of (E)-penta-1,3-diene and how does it participate in a cycloaddition? | 大模型 | 2.125 | 3.068 | 0.943 | 3 |
| 3 | What is the structure of acrylonitrile and how does it interact with (E)-penta-1,3-diene in a cycloaddition? | 大模型 | 3.068 | 4.045 | 0.977 | 4 |
| 4 | What is the structure of cyclopentadiene and how does it participate in a cycloaddition? | 小模型 | 3.042 | 4.197 | 1.155 | 5 |
| 5 | What is the structure of methyl acrylate and how does it interact with cyclopentadiene in a cycloaddition? | 大模型 | 4.197 | 5.174 | 0.977 | 6 |
| 6 | What is the predicted product structure for reaction A based on the cycloaddition mechanism? | 大模型 | 4.222 | 5.234 | 1.012 | 7 |
| 7 | What is the predicted product structure for reaction B based on the cycloaddition mechanism? | 大模型 | 5.174 | 6.186 | 1.012 | 8 |
| 8 | What conditions are typically required for thermal versus photochemical cycloaddition reactions? | 小模型 | 5.261 | 6.339 | 1.077 | 9 |
| 9 | Does reaction A occur under thermal or photochemical conditions, and how does this affect the product? | 小模型 | 6.339 | 7.494 | 1.155 | 10 |
| 10 | Does reaction B occur under thermal or photochemical conditions, and how does this affect the product? | 小模型 | 6.385 | 7.540 | 1.155 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            6.49s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 1.05s - 2.13s
步骤 2 |         #########                                          | 2.13s - 3.07s
步骤 4 |                  ###########                               | 3.04s - 4.20s
步骤 3 |                  #########                                 | 3.07s - 4.04s
步骤 5 |                             #########                      | 4.20s - 5.17s
步骤 6 |                             #########                      | 4.22s - 5.23s
步骤 7 |                                      #########             | 5.17s - 6.19s
步骤 8 |                                      ##########            | 5.26s - 6.34s
步骤 9 |                                                ########### | 6.34s - 7.49s
步骤 10 |                                                 ###########| 6.38s - 7.54s
```

