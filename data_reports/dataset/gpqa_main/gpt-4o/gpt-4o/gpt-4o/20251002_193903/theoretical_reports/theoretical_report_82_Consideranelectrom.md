# 问题 82 的理论性能分析报告

## 问题描述

Consider an electromagnetic wave incident on an interface from a medium#1 with refractive index n1 = 1.75 to another medium#2 of refractive index n2 = 1.26. The wave is plane-polarized parallel to the interface.  If the angle of incidence 'i' is more than the critical angle of refraction 'i_0', then it is expected that there will be a lateral displacement of the beam while getting reflected. If the wavelength of the wave in the medium#1 is \lambda = 400 nm and i = 80 degree, then, find the value of the lateral displacement.

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
| 规划阶段总时间 (Planner) | 1.642 | 100% |
| 规划过程中启动的任务数 | 1 / 3 | 33.3% |
| 规划与执行重叠的任务数 | 1 / 3 | 33.3% |
| 第一个任务规划完成时间 | 1.039 | - |
| 最后一个任务规划完成时间 | 1.621 | - |
| 最后一个任务执行完成时间 | 24.006 | - |
| 任务总执行时间(累计) | 22.966 | - |
| 流水线加速比 | 1.04x | - |
| 并行效率 | 95.7% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 3 | 22.966 | - |
| 规划模型 | 1 | 1.932 | - |
| 顺序总时间 | - | 24.898 | - |
| 并行总时间 | - | 24.006 | 1.04x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Calculate the critical angle of refraction 'i_0' using the refractive indices n1 and n2. | 大模型 | 1.039 | 8.695 | 7.655 | 2 |
| 2 | Verify if the angle of incidence 'i' is greater than the critical angle 'i_0'. | 大模型 | 8.695 | 16.350 | 7.655 | 3 |
| 3 | Determine the lateral displacement of the beam when the angle of incidence is greater than the critical angle. | 大模型 | 16.350 | 24.006 | 7.655 | 4 |

## 理论执行甘特图

```
时间轴:
0                                                            22.97s
+------------------------------------------------------------+
步骤 1 |###################                                         | 1.04s - 8.69s
步骤 2 |                   ####################                     | 8.69s - 16.35s
步骤 3 |                                       #####################| 16.35s - 24.01s
```

