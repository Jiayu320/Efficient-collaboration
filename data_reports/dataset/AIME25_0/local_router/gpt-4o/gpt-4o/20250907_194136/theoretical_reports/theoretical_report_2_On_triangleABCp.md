# 问题 2 的理论性能分析报告

## 问题描述

On $\triangle ABC$ points $A,D,E$, and $B$ lie that order on side $\overline{AB}$ with $AD=4, DE=16$, and $EB=8$. Points $A,F,G$, and $C$ lie in that order on side $\overline{AC}$ with $AF=13, FG=52$, and $GC=26$. Let $M$ be the reflection of $D$ through $F$, and let $N$ be the reflection of $G$ through $E$. Quadrilateral $DEGF$ has area 288. Find the area of heptagon $AFNBCEM$.

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (gpt-4o) | 0.735 | 144.50 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 4.854 | 100% |
| 规划过程中启动的任务数 | 7 / 9 | 77.8% |
| 规划与执行重叠的任务数 | 7 / 9 | 77.8% |
| 第一个任务规划完成时间 | 0.935 | - |
| 最后一个任务规划完成时间 | 4.812 | - |
| 最后一个任务执行完成时间 | 6.007 | - |
| 任务总执行时间(累计) | 8.380 | - |
| 流水线加速比 | 3.58x | - |
| 并行效率 | 139.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 9 | 8.380 | - |
| 规划模型 | 1 | 13.140 | - |
| 顺序总时间 | - | 21.520 | - |
| 并行总时间 | - | 6.007 | 3.58x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the length of side AB? | 大模型 | 0.935 | 1.809 | 0.873 | 2 |
| 2 | What is the length of side AC? | 大模型 | 1.329 | 2.202 | 0.873 | 3 |
| 3 | What are the coordinates of points A, B, C? | 大模型 | 2.202 | 3.145 | 0.943 | 4 |
| 4 | What are the coordinates of points D, E? | 大模型 | 3.145 | 4.053 | 0.908 | 5 |
| 5 | What are the coordinates of points F, G? | 大模型 | 3.145 | 4.053 | 0.908 | 6 |
| 6 | What are the coordinates of point M (reflection of D through F)? | 大模型 | 4.053 | 4.995 | 0.943 | 7 |
| 7 | What are the coordinates of point N (reflection of G through E)? | 大模型 | 4.053 | 4.995 | 0.943 | 8 |
| 8 | What is the area of quadrilateral DEGF? | 大模型 | 4.995 | 5.973 | 0.977 | 9 |
| 9 | What is the area of the heptagon AFNBCEM? | 大模型 | 4.995 | 6.007 | 1.012 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            5.07s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 0.94s - 1.81s
步骤 2 |    ##########                                              | 1.33s - 2.20s
步骤 3 |              ############                                  | 2.20s - 3.14s
步骤 4 |                          ##########                        | 3.14s - 4.05s
步骤 5 |                          ##########                        | 3.14s - 4.05s
步骤 6 |                                    ############            | 4.05s - 5.00s
步骤 7 |                                    ############            | 4.05s - 5.00s
步骤 8 |                                                ########### | 5.00s - 5.97s
步骤 9 |                                                ############| 5.00s - 6.01s
```

