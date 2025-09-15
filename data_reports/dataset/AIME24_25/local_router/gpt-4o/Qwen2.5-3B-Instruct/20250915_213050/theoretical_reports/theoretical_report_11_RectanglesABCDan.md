# 问题 11 的理论性能分析报告

## 问题描述

Rectangles $ABCD$ and $EFGH$ are drawn such that $D,E,C,F$ are collinear. Also, $A,D,H,G$ all lie on a circle. If $BC=16$,$AB=107$,$FG=17$, and $EF=184$, what is the length of $CE$?

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
| 规划阶段总时间 (Planner) | 3.941 | 100% |
| 规划过程中启动的任务数 | 5 / 6 | 83.3% |
| 规划与执行重叠的任务数 | 5 / 6 | 83.3% |
| 第一个任务规划完成时间 | 1.090 | - |
| 最后一个任务规划完成时间 | 3.899 | - |
| 最后一个任务执行完成时间 | 5.708 | - |
| 任务总执行时间(累计) | 5.621 | - |
| 流水线加速比 | 2.55x | - |
| 并行效率 | 98.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 6 | 5.621 | - |
| 规划模型 | 1 | 8.927 | - |
| 顺序总时间 | - | 14.548 | - |
| 并行总时间 | - | 5.708 | 2.55x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the relationship between points A, D, H, and G lying on a circle? | 大模型 | 1.090 | 2.033 | 0.943 | 2 |
| 2 | How can we express the coordinates of points B, C, and D given BC=16 and AB=107? | 大模型 | 1.694 | 2.602 | 0.908 | 3 |
| 3 | How can we express the coordinates of points E, F, and G given FG=17 and EF=184? | 大模型 | 2.298 | 3.206 | 0.908 | 4 |
| 4 | What constraints does the collinearity of points D, E, C, and F impose? | 大模型 | 2.846 | 3.788 | 0.943 | 5 |
| 5 | How can we use the circle relationship to establish a mathematical equation involving CE? | 大模型 | 3.788 | 4.765 | 0.977 | 6 |
| 6 | What is the length of CE based on the established equations? | 大模型 | 4.765 | 5.708 | 0.943 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            4.62s
+------------------------------------------------------------+
步骤 1 |############                                                | 1.09s - 2.03s
步骤 2 |       ############                                         | 1.69s - 2.60s
步骤 3 |               ############                                 | 2.30s - 3.21s
步骤 4 |                      #############                         | 2.85s - 3.79s
步骤 5 |                                   ############             | 3.79s - 4.77s
步骤 6 |                                               ############ | 4.77s - 5.71s
```

