# 问题 81 的理论性能分析报告

## 问题描述

In triangle $ABC$, $\angle BAC = 72^\circ$.  The incircle of triangle $ABC$ touches sides $BC$, $AC$, and $AB$ at $D$, $E$, and $F$, respectively.  Find $\angle EDF$, in degrees.

[asy]
import geometry;

unitsize(2 cm);

pair A, B, C, D, E, F, I;

A = (1,2);
B = (0,0);
C = (3,0);
I = incenter(A,B,C);
D = (I + reflect(B,C)*(I))/2;
E = (I + reflect(C,A)*(I))/2;
F = (I + reflect(A,B)*(I))/2;

draw(A--B--C--cycle);
draw(incircle(A,B,C));
draw(F--D--E);

label("$A$", A, N);
label("$B$", B, SW);
label("$C$", C, SE);
label("$D$", D, S);
label("$E$", E, NE);
label("$F$", F, NW);
[/asy]

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
| 规划阶段总时间 (Planner) | 2.846 | 100% |
| 规划过程中启动的任务数 | 2 / 5 | 40.0% |
| 规划与执行重叠的任务数 | 2 / 5 | 40.0% |
| 第一个任务规划完成时间 | 1.034 | - |
| 最后一个任务规划完成时间 | 2.803 | - |
| 最后一个任务执行完成时间 | 5.747 | - |
| 任务总执行时间(累计) | 4.713 | - |
| 流水线加速比 | 2.13x | - |
| 并行效率 | 82.0% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 5 | 4.713 | - |
| 规划模型 | 1 | 7.522 | - |
| 顺序总时间 | - | 12.236 | - |
| 并行总时间 | - | 5.747 | 2.13x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the relationship between the incenter and the points of tangency? | 大模型 | 1.034 | 1.976 | 0.943 | 2 |
| 2 | What are the angles ∠ABF and ∠ACF? | 大模型 | 1.976 | 2.954 | 0.977 | 3 |
| 3 | What is the measure of angle ∠BFC? | 大模型 | 2.954 | 3.896 | 0.943 | 4 |
| 4 | What is the measure of angle ∠DFE? | 大模型 | 3.896 | 4.839 | 0.943 | 5 |
| 5 | What is the measure of angle ∠EDF? | 大模型 | 4.839 | 5.747 | 0.908 | 6 |

## 理论执行甘特图

```
时间轴:
0                                                            4.71s
+------------------------------------------------------------+
步骤 1 |############                                                | 1.03s - 1.98s
步骤 2 |            ############                                    | 1.98s - 2.95s
步骤 3 |                        ############                        | 2.95s - 3.90s
步骤 4 |                                    ############            | 3.90s - 4.84s
步骤 5 |                                                ############| 4.84s - 5.75s
```

