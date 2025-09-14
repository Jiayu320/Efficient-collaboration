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
| 规划阶段总时间 (Planner) | 4.910 | 100% |
| 规划过程中启动的任务数 | 6 / 8 | 75.0% |
| 规划与执行重叠的任务数 | 6 / 8 | 75.0% |
| 第一个任务规划完成时间 | 1.090 | - |
| 最后一个任务规划完成时间 | 4.868 | - |
| 最后一个任务执行完成时间 | 7.790 | - |
| 任务总执行时间(累计) | 8.193 | - |
| 流水线加速比 | 2.56x | - |
| 并行效率 | 105.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 1.845 | - |
| 大模型任务 | 6 | 6.348 | - |
| 规划模型 | 1 | 11.736 | - |
| 顺序总时间 | - | 19.929 | - |
| 并行总时间 | - | 7.790 | 2.56x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the relationship between points A, D, H, and G lying on a circle? | 大模型 | 1.090 | 2.171 | 1.081 | 2 |
| 2 | How can we use the collinearity of points D, E, C, and F to establish a geometric relationship? | 大模型 | 1.708 | 2.789 | 1.081 | 3 |
| 3 | What are the dimensions of rectangle $ABCD$ given $BC=16$ and $AB=107$? | 小模型 | 2.298 | 3.220 | 0.922 | 4 |
| 4 | What are the dimensions of rectangle $EFGH$ given $FG=17$ and $EF=184$? | 小模型 | 2.902 | 3.824 | 0.922 | 5 |
| 5 | How can we use the collinearity of points D, E, C, and F to find the length of $CE$? | 大模型 | 3.604 | 4.754 | 1.150 | 6 |
| 6 | What is the length of $CE$? | 大模型 | 4.754 | 5.766 | 1.012 | 7 |
| 7 | What is the length of $CE$? | 大模型 | 5.766 | 6.778 | 1.012 | 8 |
| 8 | What is the length of $CE$? | 大模型 | 6.778 | 7.790 | 1.012 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            6.70s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 1.09s - 2.17s
步骤 2 |     ##########                                             | 1.71s - 2.79s
步骤 3 |          #########                                         | 2.30s - 3.22s
步骤 4 |                ########                                    | 2.90s - 3.82s
步骤 5 |                      ##########                            | 3.60s - 4.75s
步骤 6 |                                #########                   | 4.75s - 5.77s
步骤 7 |                                         #########          | 5.77s - 6.78s
步骤 8 |                                                  ##########| 6.78s - 7.79s
```

