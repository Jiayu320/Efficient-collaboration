# 问题 2 的理论性能分析报告

## 问题描述

What is the distance between the two intersections of $y=x^2$ and $x+y=1$?

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (meta-llama/llama-3-8b-instruct) | 0.554 | 2069.56 |
| 大模型 (openai/gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 3.463 | 100% |
| 规划过程中启动的任务数 | 5 / 6 | 83.3% |
| 规划与执行重叠的任务数 | 4 / 6 | 66.7% |
| 第一个任务规划完成时间 | 1.118 | - |
| 最后一个任务规划完成时间 | 3.421 | - |
| 最后一个任务执行完成时间 | 5.275 | - |
| 任务总执行时间(累计) | 5.552 | - |
| 流水线加速比 | 2.74x | - |
| 并行效率 | 105.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 6 | 5.552 | - |
| 规划模型 | 1 | 8.927 | - |
| 顺序总时间 | - | 14.479 | - |
| 并行总时间 | - | 5.275 | 2.74x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What are the points of intersection between the parabola y=x^2 and the line x+y=1? | 大模型 | 1.118 | 2.061 | 0.943 | 2 |
| 2 | How can we solve the system of equations simultaneously? | 大模型 | 1.539 | 2.447 | 0.908 | 3 |
| 3 | What are the coordinates of the two intersection points? | 大模型 | 2.447 | 3.425 | 0.977 | 4 |
| 4 | What is the distance formula between two points in a coordinate plane? | 大模型 | 2.466 | 3.340 | 0.873 | 5 |
| 5 | What is the distance between the first and second intersection points? | 大模型 | 3.425 | 4.367 | 0.943 | 6 |
| 6 | What is the final answer for the distance between the intersections? | 大模型 | 4.367 | 5.275 | 0.908 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            4.16s
+------------------------------------------------------------+
步骤 1 |#############                                               | 1.12s - 2.06s
步骤 2 |      #############                                         | 1.54s - 2.45s
步骤 3 |                   ##############                           | 2.45s - 3.42s
步骤 4 |                   #############                            | 2.47s - 3.34s
步骤 5 |                                 #############              | 3.42s - 4.37s
步骤 6 |                                              ##############| 4.37s - 5.28s
```

