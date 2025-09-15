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
| 规划阶段总时间 (Planner) | 5.893 | 100% |
| 规划过程中启动的任务数 | 8 / 9 | 88.9% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 1.048 | - |
| 最后一个任务规划完成时间 | 5.851 | - |
| 最后一个任务执行完成时间 | 7.210 | - |
| 任务总执行时间(累计) | 8.449 | - |
| 流水线加速比 | 2.99x | - |
| 并行效率 | 117.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 9 | 8.449 | - |
| 规划模型 | 1 | 13.140 | - |
| 顺序总时间 | - | 21.589 | - |
| 并行总时间 | - | 7.210 | 2.99x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the general outcome of a cycloaddition reaction between two π systems? | 大模型 | 1.048 | 1.921 | 0.873 | 2 |
| 2 | How does the thermal condition affect the cycloaddition reaction compared to the photochemical condition? | 大模型 | 1.921 | 2.829 | 0.908 | 3 |
| 3 | What is the structure of (E)-penta-1,3-diene and how does it participate in the reaction? | 大模型 | 2.829 | 3.772 | 0.943 | 4 |
| 4 | What is the structure of acrylonitrile and how does it interact with (E)-penta-1,3-diene? | 大模型 | 3.772 | 4.749 | 0.977 | 5 |
| 5 | What is the structure of cyclopentadiene and how does it participate in the reaction? | 大模型 | 3.463 | 4.371 | 0.908 | 6 |
| 6 | What is the structure of methyl acrylate and how does it interact with cyclopentadiene? | 大模型 | 4.371 | 5.349 | 0.977 | 7 |
| 7 | What is the expected structure of product A based on the reaction between (E)-penta-1,3-diene and acrylonitrile? | 大模型 | 4.749 | 5.761 | 1.012 | 8 |
| 8 | What is the expected structure of product B based on the reaction between cyclopentadiene and methyl acrylate? | 大模型 | 5.360 | 6.371 | 1.012 | 9 |
| 9 | What is the final question regarding the cycloaddition products? | 大模型 | 6.371 | 7.210 | 0.839 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            6.16s
+------------------------------------------------------------+
步骤 1 |########                                                    | 1.05s - 1.92s
步骤 2 |        #########                                           | 1.92s - 2.83s
步骤 3 |                 #########                                  | 2.83s - 3.77s
步骤 5 |                       #########                            | 3.46s - 4.37s
步骤 4 |                          ##########                        | 3.77s - 4.75s
步骤 6 |                                #########                   | 4.37s - 5.35s
步骤 7 |                                    #########               | 4.75s - 5.76s
步骤 8 |                                         ##########         | 5.36s - 6.37s
步骤 9 |                                                   #########| 6.37s - 7.21s
```

