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
| 规划阶段总时间 (Planner) | 4.433 | 100% |
| 规划过程中启动的任务数 | 7 / 8 | 87.5% |
| 规划与执行重叠的任务数 | 7 / 8 | 87.5% |
| 第一个任务规划完成时间 | 1.090 | - |
| 最后一个任务规划完成时间 | 4.390 | - |
| 最后一个任务执行完成时间 | 6.298 | - |
| 任务总执行时间(累计) | 7.604 | - |
| 流水线加速比 | 3.07x | - |
| 并行效率 | 120.7% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 1.845 | - |
| 大模型任务 | 6 | 5.759 | - |
| 规划模型 | 1 | 11.736 | - |
| 顺序总时间 | - | 19.340 | - |
| 并行总时间 | - | 6.298 | 3.07x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the relationship between points A, D, H, and G lying on a circle? | 大模型 | 1.090 | 2.033 | 0.943 | 2 |
| 2 | How can we use the collinearity of points D, E, C, and F to establish relationships between segments? | 大模型 | 1.708 | 2.685 | 0.977 | 3 |
| 3 | What is the length of DC using the given dimensions? | 大模型 | 2.143 | 3.017 | 0.873 | 4 |
| 4 | Can we establish a proportion using the circle and collinearity constraints? | 大模型 | 2.685 | 3.697 | 1.012 | 5 |
| 5 | What is the length of EF? | 小模型 | 3.042 | 3.965 | 0.922 | 6 |
| 6 | What is the length of FG? | 小模型 | 3.421 | 4.344 | 0.922 | 7 |
| 7 | Using the proportion and given values, what is the value of CE? | 大模型 | 4.344 | 5.390 | 1.046 | 8 |
| 8 | What is the length of CE? | 大模型 | 5.390 | 6.298 | 0.908 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            5.21s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 1.09s - 2.03s
步骤 2 |       ###########                                          | 1.71s - 2.69s
步骤 3 |            ##########                                      | 2.14s - 3.02s
步骤 4 |                  ############                              | 2.69s - 3.70s
步骤 5 |                      ###########                           | 3.04s - 3.96s
步骤 6 |                          ###########                       | 3.42s - 4.34s
步骤 7 |                                     ############           | 4.34s - 5.39s
步骤 8 |                                                 ###########| 5.39s - 6.30s
```

