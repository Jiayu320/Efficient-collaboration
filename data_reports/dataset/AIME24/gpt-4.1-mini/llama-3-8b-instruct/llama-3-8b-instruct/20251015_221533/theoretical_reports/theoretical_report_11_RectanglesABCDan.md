# 问题 11 的理论性能分析报告

## 问题描述

Rectangles $ABCD$ and $EFGH$ are drawn such that $D,E,C,F$ are collinear. Also, $A,D,H,G$ all lie on a circle. If $BC=16$,$AB=107$,$FG=17$, and $EF=184$, what is the length of $CE$?

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (meta-llama/llama-3-8b-instruct) | 0.645 | 86.95 |
| 大模型 (meta-llama/llama-3-8b-instruct) | 0.645 | 86.95 |
| 路由模型 (gpt-4.1-mini) | 0.700 | 69.59 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 6.103 | 100% |
| 规划过程中启动的任务数 | 4 / 5 | 80.0% |
| 规划与执行重叠的任务数 | 4 / 5 | 80.0% |
| 第一个任务规划完成时间 | 1.936 | - |
| 最后一个任务规划完成时间 | 6.060 | - |
| 最后一个任务执行完成时间 | 8.598 | - |
| 任务总执行时间(累计) | 6.560 | - |
| 流水线加速比 | 1.49x | - |
| 并行效率 | 76.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 2.210 | - |
| 大模型任务 | 3 | 4.350 | - |
| 规划模型 | 1 | 6.232 | - |
| 顺序总时间 | - | 12.793 | - |
| 并行总时间 | - | 8.598 | 1.49x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Identify the properties of rectangles ABCD and EFGH: all angles are right angles, opposite sides are equal, and order of vertices matters. Confirm that BC=AD=16 and AB=DC=107 for ABCD, and FG=EH=17 and EF=GH=184 for EFGH. Is this consistent? | 小模型 | 1.936 | 3.041 | 1.105 | 2 |
| 2 | Use the collinearity condition D, E, C, F. Since D and C are vertices of ABCD, and E and F of EFGH, find expressions or parameterizations for points D, E, C, F along a line. Can their coordinates be set with respect to a suitable origin or frame? | 大模型 | 3.143 | 4.478 | 1.335 | 3 |
| 3 | Since A, D, H, G lie on a circle, use the cyclic quadrilateral condition. Express coordinates of A, D from ABCD, and H, G from EFGH in terms of the unknown location of E and F, consistent with step 2. What is the equation of the circle passing through these points? | 大模型 | 4.478 | 6.043 | 1.565 | 4 |
| 4 | Apply the rectangle properties: AB ⟂ BC and EF ⟂ FG, to find coordinate relations and angles for the rectangles. Use these relations to write coordinates of all relevant points, especially C and E, in terms of known lengths and variables from prior steps. | 大模型 | 6.043 | 7.493 | 1.450 | 5 |
| 5 | Using the coordinates from step 4, compute the length CE by distance formula. What is the explicit value of CE? | 小模型 | 7.493 | 8.598 | 1.105 | 6 |

## 理论执行甘特图

```
时间轴:
0                                                            6.66s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 1.94s - 3.04s
步骤 2 |          ############                                      | 3.14s - 4.48s
步骤 3 |                      ##############                        | 4.48s - 6.04s
步骤 4 |                                    ##############          | 6.04s - 7.49s
步骤 5 |                                                  ##########| 7.49s - 8.60s
```

