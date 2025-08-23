# 问题 2 的理论性能分析报告

## 问题描述

What is the distance between the two intersections of $y=x^2$ and $x+y=1$?

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (meta-llama/llama-3-8b-instruct) | 0.440 | 3422.00 |
| 大模型 (gpt-4o) | 0.610 | 58.71 |
| 路由模型 (claude-3-5-sonnet-latest) | 1.060 | 57.07 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 11.573 | 100% |
| 规划过程中启动的任务数 | 6 / 6 | 100.0% |
| 规划与执行重叠的任务数 | 5 / 6 | 83.3% |
| 第一个任务规划完成时间 | 2.911 | - |
| 最后一个任务规划完成时间 | 10.130 | - |
| 最后一个任务执行完成时间 | 11.336 | - |
| 任务总执行时间(累计) | 6.051 | - |
| 流水线加速比 | 1.55x | - |
| 并行效率 | 53.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 0.446 | - |
| 大模型任务 | 5 | 5.605 | - |
| 规划模型 | 1 | 11.573 | - |
| 顺序总时间 | - | 17.624 | - |
| 并行总时间 | - | 11.336 | 1.55x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | How do we find the points of intersection between y=x^2 and x+y=1? | 大模型 | 2.911 | 4.032 | 1.121 | 1 |
| 2 | Solve the system of equations by substitution to find the x-coordinates? | 大模型 | 4.355 | 5.561 | 1.206 | 1 |
| 3 | Calculate the y-coordinates of the intersection points? | 大模型 | 5.799 | 6.834 | 1.036 | 1 |
| 4 | What are the two intersection points in (x,y) form? | 小模型 | 7.242 | 7.688 | 0.446 | 1 |
| 5 | How do we calculate the distance between two points in a plane? | 大模型 | 8.686 | 9.722 | 1.036 | 1 |
| 6 | Apply the distance formula to find the distance between the intersection points? | 大模型 | 10.130 | 11.336 | 1.206 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            8.42s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 2.91s - 4.03s
步骤 2 |          ########                                          | 4.35s - 5.56s
步骤 3 |                    #######                                 | 5.80s - 6.83s
步骤 4 |                              ####                          | 7.24s - 7.69s
步骤 5 |                                         #######            | 8.69s - 9.72s
步骤 6 |                                                   #########| 10.13s - 11.34s
```

## 关键路径分析

关键路径是决定总执行时间的最长任务链。以下是本次执行的关键路径：

| 步骤 | 任务描述 | 执行时间 (秒) |
| --- | --- | --- |
| 6 | Apply the distance formula to find the distance between the intersection points? | 1.206 |

关键路径总时间: 1.206 秒
