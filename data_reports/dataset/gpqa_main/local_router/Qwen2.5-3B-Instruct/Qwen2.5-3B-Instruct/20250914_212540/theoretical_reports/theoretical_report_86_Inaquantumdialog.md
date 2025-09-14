# 问题 86 的理论性能分析报告

## 问题描述

In a quantum dialog protocol a 4-mode continuous variable GHZ state is distributed among 3-parties, and a bell measurement is performed on these states, what would be the measurement output if the three parties encode in the following way using a displacement operator D(alpha): 
P1: (xa,pa) 
P2: (xb,pb)
P3: (xc,pc)
Here, (x,p) correspond to the amplitude and phase, such that 
alpha= x +ip, is the argument of displacement operator.
In the scheme, the 2nd and 3rd mode are encoded by P2. The 1st and 4th mode are encoded by P1 and P3.

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 大模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 4.559 | 100% |
| 规划过程中启动的任务数 | 4 / 8 | 50.0% |
| 规划与执行重叠的任务数 | 4 / 8 | 50.0% |
| 第一个任务规划完成时间 | 1.048 | - |
| 最后一个任务规划完成时间 | 4.517 | - |
| 最后一个任务执行完成时间 | 10.651 | - |
| 任务总执行时间(累计) | 11.719 | - |
| 流水线加速比 | 2.20x | - |
| 并行效率 | 110.0% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 8 | 11.719 | - |
| 规划模型 | 1 | 11.736 | - |
| 顺序总时间 | - | 23.455 | - |
| 并行总时间 | - | 10.651 | 2.20x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the mathematical form of a 4-mode continuous variable GHZ state? | 大模型 | 1.048 | 2.513 | 1.465 | 2 |
| 2 | How does a bell measurement work on continuous variable quantum systems? | 大模型 | 2.513 | 4.132 | 1.620 | 3 |
| 3 | What is the displacement operator D(alpha) in terms of amplitude and phase? | 大模型 | 2.017 | 3.327 | 1.310 | 4 |
| 4 | What are the encoded states for P1, P2, and P3 based on the given encoding scheme? | 大模型 | 3.327 | 4.792 | 1.465 | 5 |
| 5 | How do we apply the displacement operator to each party's encoded state? | 大模型 | 4.792 | 6.256 | 1.465 | 6 |
| 6 | What is the mathematical expression for the bell measurement output? | 大模型 | 6.256 | 7.876 | 1.620 | 7 |
| 7 | How do we simplify the expression for the measurement output? | 大模型 | 7.876 | 9.341 | 1.465 | 8 |
| 8 | What is the final measurement output for the three parties? | 大模型 | 9.341 | 10.651 | 1.310 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            9.60s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 1.05s - 2.51s
步骤 3 |      ########                                              | 2.02s - 3.33s
步骤 2 |         ##########                                         | 2.51s - 4.13s
步骤 4 |              #########                                     | 3.33s - 4.79s
步骤 5 |                       #########                            | 4.79s - 6.26s
步骤 6 |                                ##########                  | 6.26s - 7.88s
步骤 7 |                                          #########         | 7.88s - 9.34s
步骤 8 |                                                   #########| 9.34s - 10.65s
```

