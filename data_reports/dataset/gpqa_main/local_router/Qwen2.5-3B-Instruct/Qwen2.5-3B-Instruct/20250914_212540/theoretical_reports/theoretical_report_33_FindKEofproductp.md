# 问题 33 的理论性能分析报告

## 问题描述

Find KE of product particles in,
Pi(+) = mu(+) + nu
here Pi(+) is stationary.
Rest mass of Pi(+) &  mu(+) is 139.6 MeV & 105.7 MeV respectively.

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
| 规划阶段总时间 (Planner) | 4.320 | 100% |
| 规划过程中启动的任务数 | 5 / 8 | 62.5% |
| 规划与执行重叠的任务数 | 5 / 8 | 62.5% |
| 第一个任务规划完成时间 | 1.034 | - |
| 最后一个任务规划完成时间 | 4.278 | - |
| 最后一个任务执行完成时间 | 8.559 | - |
| 任务总执行时间(累计) | 8.852 | - |
| 流水线加速比 | 2.41x | - |
| 并行效率 | 103.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 8 | 8.852 | - |
| 规划模型 | 1 | 11.736 | - |
| 顺序总时间 | - | 20.588 | - |
| 并行总时间 | - | 8.559 | 2.41x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the total energy-momentum of the stationary Pi(+) particle? | 大模型 | 1.034 | 2.189 | 1.155 | 2 |
| 2 | What is the momentum of the mu(+) particle? | 大模型 | 1.455 | 2.455 | 1.000 | 3 |
| 3 | What is the momentum of the nu particle? | 大模型 | 1.862 | 2.862 | 1.000 | 4 |
| 4 | What is the total momentum of the system? | 大模型 | 2.862 | 3.940 | 1.077 | 5 |
| 5 | How do we apply conservation of momentum to find the unknown momentum of nu? | 大模型 | 3.940 | 5.172 | 1.232 | 6 |
| 6 | How do we apply conservation of energy to find the unknown energy of nu? | 大模型 | 5.172 | 6.404 | 1.232 | 7 |
| 7 | What is the total energy of the product particles? | 大模型 | 6.404 | 7.482 | 1.077 | 8 |
| 8 | What is the kinetic energy of the product particles? | 大模型 | 7.482 | 8.559 | 1.077 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            7.53s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 1.03s - 2.19s
步骤 2 |   ########                                                 | 1.46s - 2.45s
步骤 3 |      ########                                              | 1.86s - 2.86s
步骤 4 |              #########                                     | 2.86s - 3.94s
步骤 5 |                       #########                            | 3.94s - 5.17s
步骤 6 |                                ##########                  | 5.17s - 6.40s
步骤 7 |                                          #########         | 6.40s - 7.48s
步骤 8 |                                                   #########| 7.48s - 8.56s
```

