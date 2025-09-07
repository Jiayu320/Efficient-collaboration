# 问题 2 的理论性能分析报告

## 问题描述

On $\triangle ABC$ points $A,D,E$, and $B$ lie that order on side $\overline{AB}$ with $AD=4, DE=16$, and $EB=8$. Points $A,F,G$, and $C$ lie in that order on side $\overline{AC}$ with $AF=13, FG=52$, and $GC=26$. Let $M$ be the reflection of $D$ through $F$, and let $N$ be the reflection of $G$ through $E$. Quadrilateral $DEGF$ has area 288. Find the area of heptagon $AFNBCEM$.

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (meta-llama/llama-3-8b-instruct) | 0.554 | 2069.56 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 4.545 | 100% |
| 规划过程中启动的任务数 | 7 / 8 | 87.5% |
| 规划与执行重叠的任务数 | 7 / 8 | 87.5% |
| 第一个任务规划完成时间 | 0.935 | - |
| 最后一个任务规划完成时间 | 4.503 | - |
| 最后一个任务执行完成时间 | 6.111 | - |
| 任务总执行时间(累计) | 7.506 | - |
| 流水线加速比 | 3.15x | - |
| 并行效率 | 122.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 8 | 7.506 | - |
| 规划模型 | 1 | 11.736 | - |
| 顺序总时间 | - | 19.242 | - |
| 并行总时间 | - | 6.111 | 3.15x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the length of side AB? | 大模型 | 0.935 | 1.809 | 0.873 | 2 |
| 2 | What is the length of side AC? | 大模型 | 1.329 | 2.202 | 0.873 | 3 |
| 3 | What are the coordinates of points A, B, C, D, E, F, and G? | 大模型 | 2.202 | 3.283 | 1.081 | 4 |
| 4 | What are the coordinates of point M (reflection of D through F)? | 大模型 | 3.283 | 4.191 | 0.908 | 5 |
| 5 | What are the coordinates of point N (reflection of G through E)? | 大模型 | 3.283 | 4.191 | 0.908 | 6 |
| 6 | What is the area of quadrilateral DEGF? | 大模型 | 4.191 | 5.134 | 0.943 | 7 |
| 7 | What is the area of triangle ABC? | 大模型 | 3.927 | 4.870 | 0.943 | 8 |
| 8 | What is the area of the heptagon AFNBCEM? | 大模型 | 5.134 | 6.111 | 0.977 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            5.18s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 0.94s - 1.81s
步骤 2 |    ##########                                              | 1.33s - 2.20s
步骤 3 |              #############                                 | 2.20s - 3.28s
步骤 4 |                           ##########                       | 3.28s - 4.19s
步骤 5 |                           ##########                       | 3.28s - 4.19s
步骤 7 |                                  ###########               | 3.93s - 4.87s
步骤 6 |                                     ###########            | 4.19s - 5.13s
步骤 8 |                                                ########### | 5.13s - 6.11s
```

