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
| 小模型 (gpt-4o) | 0.735 | 144.50 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (gpt-4o) | 0.735 | 144.50 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 1.995 | 100% |
| 规划过程中启动的任务数 | 1 / 4 | 25.0% |
| 规划与执行重叠的任务数 | 1 / 4 | 25.0% |
| 第一个任务规划完成时间 | 1.067 | - |
| 最后一个任务规划完成时间 | 1.974 | - |
| 最后一个任务执行完成时间 | 31.689 | - |
| 任务总执行时间(累计) | 30.622 | - |
| 流水线加速比 | 1.06x | - |
| 并行效率 | 96.6% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 4 | 30.622 | - |
| 规划模型 | 1 | 2.915 | - |
| 顺序总时间 | - | 33.537 | - |
| 并行总时间 | - | 31.689 | 1.06x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Determine the type of cycloaddition reaction between (E)-penta-1,3-diene and acrylonitrile. | 大模型 | 1.067 | 8.723 | 7.655 | 2 |
| 2 | Identify the cycloaddition product of (E)-penta-1,3-diene and acrylonitrile. | 大模型 | 8.723 | 16.378 | 7.655 | 3 |
| 3 | Determine the type of cycloaddition reaction between cyclopentadiene and methyl acrylate under thermal conditions. | 大模型 | 16.378 | 24.033 | 7.655 | 4 |
| 4 | Identify the cycloaddition product of cyclopentadiene and methyl acrylate. | 大模型 | 24.033 | 31.689 | 7.655 | 5 |

## 理论执行甘特图

```
时间轴:
0                                                            30.62s
+------------------------------------------------------------+
步骤 1 |##############                                              | 1.07s - 8.72s
步骤 2 |              ###############                               | 8.72s - 16.38s
步骤 3 |                             ###############                | 16.38s - 24.03s
步骤 4 |                                            ############### | 24.03s - 31.69s
```

