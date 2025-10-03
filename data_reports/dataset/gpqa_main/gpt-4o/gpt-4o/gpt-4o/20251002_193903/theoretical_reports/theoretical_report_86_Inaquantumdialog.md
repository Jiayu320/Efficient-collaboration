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
| 小模型 (gpt-4o) | 0.735 | 144.50 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (gpt-4o) | 0.735 | 144.50 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 2.133 | 100% |
| 规划过程中启动的任务数 | 1 / 4 | 25.0% |
| 规划与执行重叠的任务数 | 1 / 4 | 25.0% |
| 第一个任务规划完成时间 | 1.012 | - |
| 最后一个任务规划完成时间 | 2.112 | - |
| 最后一个任务执行完成时间 | 31.633 | - |
| 任务总执行时间(累计) | 30.622 | - |
| 流水线加速比 | 1.05x | - |
| 并行效率 | 96.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 4 | 30.622 | - |
| 规划模型 | 1 | 2.610 | - |
| 顺序总时间 | - | 33.232 | - |
| 并行总时间 | - | 31.633 | 1.05x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Determine the initial parameters and setup of the 4-mode continuous variable GHZ state. | 大模型 | 1.012 | 8.667 | 7.655 | 2 |
| 2 | Understand how the displacement operator D(alpha) affects the state when encoded with parameters (xa, pa) by P1, (xb, pb) by P2 on the 2nd and 3rd mode, and (xc, pc) by P3 on the 4th mode. | 大模型 | 8.667 | 16.323 | 7.655 | 3 |
| 3 | Analyze how the Bell measurement is performed on the displaced GHZ state. | 大模型 | 16.323 | 23.978 | 7.655 | 4 |
| 4 | Calculate the resulting measurement output after the Bell measurement, considering the encoded displacements. | 大模型 | 23.978 | 31.633 | 7.655 | 5 |

## 理论执行甘特图

```
时间轴:
0                                                            30.62s
+------------------------------------------------------------+
步骤 1 |###############                                             | 1.01s - 8.67s
步骤 2 |               ###############                              | 8.67s - 16.32s
步骤 3 |                              ###############               | 16.32s - 23.98s
步骤 4 |                                             ###############| 23.98s - 31.63s
```

