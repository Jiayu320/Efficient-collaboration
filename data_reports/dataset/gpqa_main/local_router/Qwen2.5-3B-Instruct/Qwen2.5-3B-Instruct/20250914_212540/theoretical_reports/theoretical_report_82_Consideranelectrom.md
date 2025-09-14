# 问题 82 的理论性能分析报告

## 问题描述

Consider an electromagnetic wave incident on an interface from a medium#1 with refractive index n1 = 1.75 to another medium#2 of refractive index n2 = 1.26. The wave is plane-polarized parallel to the interface.  If the angle of incidence 'i' is more than the critical angle of refraction 'i_0', then it is expected that there will be a lateral displacement of the beam while getting reflected. If the wavelength of the wave in the medium#1 is \lambda = 400 nm and i = 80 degree, then, find the value of the lateral displacement.

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
| 规划阶段总时间 (Planner) | 4.545 | 100% |
| 规划过程中启动的任务数 | 7 / 8 | 87.5% |
| 规划与执行重叠的任务数 | 7 / 8 | 87.5% |
| 第一个任务规划完成时间 | 1.006 | - |
| 最后一个任务规划完成时间 | 4.503 | - |
| 最后一个任务执行完成时间 | 6.568 | - |
| 任务总执行时间(累计) | 8.619 | - |
| 流水线加速比 | 3.10x | - |
| 并行效率 | 131.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 3 | 2.690 | - |
| 大模型任务 | 5 | 5.929 | - |
| 规划模型 | 1 | 11.736 | - |
| 顺序总时间 | - | 20.355 | - |
| 并行总时间 | - | 6.568 | 3.10x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the critical angle i_0 for total internal reflection? | 大模型 | 1.006 | 2.161 | 1.155 | 2 |
| 2 | Is the angle of incidence i = 80° greater than the critical angle i_0? | 小模型 | 2.161 | 3.083 | 0.922 | 3 |
| 3 | What is the refractive index n1 and n2 given in the problem? | 小模型 | 2.059 | 2.904 | 0.845 | 4 |
| 4 | What is the wavelength of the wave in medium#2? | 大模型 | 2.904 | 3.981 | 1.077 | 5 |
| 5 | What is the angle of refraction r in medium#2? | 大模型 | 3.981 | 5.136 | 1.155 | 6 |
| 6 | What is the angle between the incident wave and the normal to the interface? | 小模型 | 3.534 | 4.456 | 0.922 | 7 |
| 7 | What is the lateral displacement formula for plane-polarized light at an angle? | 大模型 | 4.025 | 5.258 | 1.232 | 8 |
| 8 | What is the value of the lateral displacement? | 大模型 | 5.258 | 6.568 | 1.310 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            5.56s
+------------------------------------------------------------+
步骤 1 |############                                                | 1.01s - 2.16s
步骤 3 |           #########                                        | 2.06s - 2.90s
步骤 2 |            ##########                                      | 2.16s - 3.08s
步骤 4 |                    ############                            | 2.90s - 3.98s
步骤 6 |                           ##########                       | 3.53s - 4.46s
步骤 5 |                                ############                | 3.98s - 5.14s
步骤 7 |                                #############               | 4.03s - 5.26s
步骤 8 |                                             ###############| 5.26s - 6.57s
```

