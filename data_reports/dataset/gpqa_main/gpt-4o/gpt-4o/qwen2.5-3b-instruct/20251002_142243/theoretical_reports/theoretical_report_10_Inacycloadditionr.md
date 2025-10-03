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
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (gpt-4o) | 0.735 | 144.50 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 1.766 | 100% |
| 规划过程中启动的任务数 | 1 / 3 | 33.3% |
| 规划与执行重叠的任务数 | 1 / 3 | 33.3% |
| 第一个任务规划完成时间 | 1.088 | - |
| 最后一个任务规划完成时间 | 1.745 | - |
| 最后一个任务执行完成时间 | 33.461 | - |
| 任务总执行时间(累计) | 48.560 | - |
| 流水线加速比 | 1.52x | - |
| 并行效率 | 145.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 3 | 48.560 | - |
| 大模型任务 | 0 | 0.000 | - |
| 规划模型 | 1 | 2.417 | - |
| 顺序总时间 | - | 50.977 | - |
| 并行总时间 | - | 33.461 | 1.52x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Understand the mechanism of cycloaddition reactions, specifically the Diels-Alder reaction, which involves a diene and a dienophile. | 小模型 | 1.088 | 17.275 | 16.187 | 2 |
| 2 | Apply the cycloaddition mechanism to (E)-penta-1,3-diene and acrylonitrile to determine the product A. | 小模型 | 17.275 | 33.461 | 16.187 | 3 |
| 3 | Apply the cycloaddition mechanism to cyclopentadiene and methyl acrylate under thermal conditions to determine the product B. | 小模型 | 17.275 | 33.461 | 16.187 | 4 |

## 理论执行甘特图

```
时间轴:
0                                                            32.37s
+------------------------------------------------------------+
步骤 1 |#############################                               | 1.09s - 17.27s
步骤 2 |                             ############################## | 17.27s - 33.46s
步骤 3 |                             ############################## | 17.27s - 33.46s
```

