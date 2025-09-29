# 问题 29 的理论性能分析报告

## 问题描述

Torus $T$ is the surface produced by revolving a circle with radius $3$ around an axis in the plane of the circle that is a distance $6$ from the center of the circle (so like a donut). Let $S$ be a sphere with a radius $11$. When $T$ rests on the outside of $S$, it is externally tangent to $S$ along a circle with radius $r_i$, and when $T$ rests on the outside of $S$, it is externally tangent to $S$ along a circle with radius $r_o$. The difference $r_i-r_o$ can be written as $\tfrac{m}{n}$, where $m$ and $n$ are relatively prime positive integers. Find $m+n$.
[asy] unitsize(0.3 inch); draw(ellipse((0,0), 3, 1.75)); draw((-1.2,0.1)..(-0.8,-0.03)..(-0.4,-0.11)..(0,-0.15)..(0.4,-0.11)..(0.8,-0.03)..(1.2,0.1)); draw((-1,0.04)..(-0.5,0.12)..(0,0.16)..(0.5,0.12)..(1,0.04)); draw((0,2.4)--(0,-0.15)); draw((0,-0.15)--(0,-1.75), dashed); draw((0,-1.75)--(0,-2.25)); draw(ellipse((2,0), 1, 0.9)); draw((2.03,-0.02)--(2.9,-0.4)); [/asy]

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-4B-Thinking/full/ep3) | 0.690 | 184.10 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 2.108 | 100% |
| 规划过程中启动的任务数 | 3 / 6 | 50.0% |
| 规划与执行重叠的任务数 | 3 / 6 | 50.0% |
| 第一个任务规划完成时间 | 0.880 | - |
| 最后一个任务规划完成时间 | 2.091 | - |
| 最后一个任务执行完成时间 | 5.476 | - |
| 任务总执行时间(累计) | 6.150 | - |
| 流水线加速比 | 2.70x | - |
| 并行效率 | 112.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 5 | 5.000 | - |
| 大模型任务 | 1 | 1.150 | - |
| 规划模型 | 1 | 8.631 | - |
| 顺序总时间 | - | 14.781 | - |
| 并行总时间 | - | 5.476 | 2.70x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the value of $11 - 3$? | 小模型 | 0.880 | 1.725 | 0.845 | 2 |
| 2 | Using the formula $r_i = \sqrt{11^2 - (11 - 3)^2}$, what is $r_i$? | 小模型 | 1.725 | 2.880 | 1.155 | 3 |
| 3 | What is the value of $11 + 3$? | 小模型 | 1.326 | 2.170 | 0.845 | 4 |
| 4 | Using the formula $r_o = \sqrt{11^2 - (11 + 3)^2}$, what is $r_o$? | 小模型 | 2.170 | 3.325 | 1.155 | 5 |
| 5 | What is the simplified form of $\sqrt{87} - \sqrt{200}$ as $\frac{m}{n}$ where $m$ and $n$ are coprime positive integers? | 大模型 | 3.325 | 4.476 | 1.150 | 6 |
| 6 | What is the sum $m + n$? | 小模型 | 4.476 | 5.476 | 1.000 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            4.60s
+------------------------------------------------------------+
步骤 1 |###########                                                 | 0.88s - 1.73s
步骤 3 |     ###########                                            | 1.33s - 2.17s
步骤 2 |           ###############                                  | 1.73s - 2.88s
步骤 4 |                ###############                             | 2.17s - 3.33s
步骤 5 |                               ###############              | 3.33s - 4.48s
步骤 6 |                                              ##############| 4.48s - 5.48s
```

