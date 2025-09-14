# 问题 29 的理论性能分析报告

## 问题描述

Torus $T$ is the surface produced by revolving a circle with radius $3$ around an axis in the plane of the circle that is a distance $6$ from the center of the circle (so like a donut). Let $S$ be a sphere with a radius $11$. When $T$ rests on the outside of $S$, it is externally tangent to $S$ along a circle with radius $r_i$, and when $T$ rests on the outside of $S$, it is externally tangent to $S$ along a circle with radius $r_o$. The difference $r_i-r_o$ can be written as $\tfrac{m}{n}$, where $m$ and $n$ are relatively prime positive integers. Find $m+n$.
[asy] unitsize(0.3 inch); draw(ellipse((0,0), 3, 1.75)); draw((-1.2,0.1)..(-0.8,-0.03)..(-0.4,-0.11)..(0,-0.15)..(0.4,-0.11)..(0.8,-0.03)..(1.2,0.1)); draw((-1,0.04)..(-0.5,0.12)..(0,0.16)..(0.5,0.12)..(1,0.04)); draw((0,2.4)--(0,-0.15)); draw((0,-0.15)--(0,-1.75), dashed); draw((0,-1.75)--(0,-2.25)); draw(ellipse((2,0), 1, 0.9)); draw((2.03,-0.02)--(2.9,-0.4)); [/asy]

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
| 规划阶段总时间 (Planner) | 4.236 | 100% |
| 规划过程中启动的任务数 | 5 / 7 | 71.4% |
| 规划与执行重叠的任务数 | 5 / 7 | 71.4% |
| 第一个任务规划完成时间 | 1.020 | - |
| 最后一个任务规划完成时间 | 4.194 | - |
| 最后一个任务执行完成时间 | 6.517 | - |
| 任务总执行时间(累计) | 6.440 | - |
| 流水线加速比 | 2.57x | - |
| 并行效率 | 98.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 0.922 | - |
| 大模型任务 | 6 | 5.517 | - |
| 规划模型 | 1 | 10.331 | - |
| 顺序总时间 | - | 16.771 | - |
| 并行总时间 | - | 6.517 | 2.57x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the distance between the centers of the torus and sphere? | 大模型 | 1.020 | 1.893 | 0.873 | 2 |
| 2 | What is the formula for the radius of the circle of intersection between a torus and sphere? | 大模型 | 1.893 | 2.836 | 0.943 | 3 |
| 3 | What is the radius r_i of the circle of intersection when the torus is externally tangent? | 大模型 | 2.836 | 3.778 | 0.943 | 4 |
| 4 | What is the radius r_o of the circle of intersection when the torus is externally tangent? | 大模型 | 2.836 | 3.778 | 0.943 | 5 |
| 5 | What is the difference r_i - r_o as a fraction? | 大模型 | 3.778 | 4.686 | 0.908 | 6 |
| 6 | What are the relatively prime positive integers m and n in the fraction m/n? | 大模型 | 4.686 | 5.594 | 0.908 | 7 |
| 7 | What is the sum m + n? | 小模型 | 5.594 | 6.517 | 0.922 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            5.50s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 1.02s - 1.89s
步骤 2 |         ##########                                         | 1.89s - 2.84s
步骤 3 |                   ###########                              | 2.84s - 3.78s
步骤 4 |                   ###########                              | 2.84s - 3.78s
步骤 5 |                              ##########                    | 3.78s - 4.69s
步骤 6 |                                        #########           | 4.69s - 5.59s
步骤 7 |                                                 ###########| 5.59s - 6.52s
```

