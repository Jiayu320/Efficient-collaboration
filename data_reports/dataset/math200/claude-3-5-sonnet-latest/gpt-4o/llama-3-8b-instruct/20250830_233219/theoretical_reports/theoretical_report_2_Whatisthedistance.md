# 问题 2 的理论性能分析报告

## 问题描述

What is the distance between the two intersections of $y=x^2$ and $x+y=1$?

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (meta-llama/llama-3-8b-instruct) | 0.554 | 2069.56 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (claude-3-5-sonnet-latest) | 1.338 | 51.49 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 5.630 | 100% |
| 规划过程中启动的任务数 | 6 / 6 | 100.0% |
| 规划与执行重叠的任务数 | 5 / 6 | 83.3% |
| 第一个任务规划完成时间 | 2.154 | - |
| 最后一个任务规划完成时间 | 5.572 | - |
| 最后一个任务执行完成时间 | 6.549 | - |
| 任务总执行时间(累计) | 4.253 | - |
| 流水线加速比 | 2.63x | - |
| 并行效率 | 64.9% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 4 | 2.264 | - |
| 大模型任务 | 2 | 1.989 | - |
| 规划模型 | 1 | 12.990 | - |
| 顺序总时间 | - | 17.244 | - |
| 并行总时间 | - | 6.549 | 2.63x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | How do we find the points of intersection between y=x^2 and x+y=1? | 小模型 | 2.154 | 2.722 | 0.568 | 2 |
| 2 | Solve the system of equations by substitution to find the x-coordinates of the intersection points? | 大模型 | 2.911 | 3.923 | 1.012 | 3 |
| 3 | Calculate the y-coordinates of the intersection points? | 小模型 | 3.923 | 4.489 | 0.566 | 4 |
| 4 | What are the two intersection points in (x,y) form? | 小模型 | 4.489 | 5.053 | 0.564 | 5 |
| 5 | How do we find the distance between two points in a coordinate plane? | 小模型 | 4.873 | 5.439 | 0.566 | 6 |
| 6 | Calculate the distance between the two intersection points using the distance formula? | 大模型 | 5.572 | 6.549 | 0.977 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            4.40s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 2.15s - 2.72s
步骤 2 |          ##############                                    | 2.91s - 3.92s
步骤 3 |                        #######                             | 3.92s - 4.49s
步骤 4 |                               ########                     | 4.49s - 5.05s
步骤 5 |                                     #######                | 4.87s - 5.44s
步骤 6 |                                              ##############| 5.57s - 6.55s
```

