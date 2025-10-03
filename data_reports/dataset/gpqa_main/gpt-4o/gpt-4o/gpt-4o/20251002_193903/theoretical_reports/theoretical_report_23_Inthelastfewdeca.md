# 问题 23 的理论性能分析报告

## 问题描述

In the last few decades, reverberation mapping, interferometry and various other observations across the electromagnetic spectrum, have been used to probe the inner structure of AGNs.
Various semi-empirical relations between the inner radius of the torus and the luminosity of AGNs have emerged. They can differ to an extent based on accuracy of observation and underlining assumptions.
They are usually compered to the basic Barvainis model.
Assuming this model, and that the temperature of dust grain sublimation is 900 K, and bolometric luminosity of AGN is 1.5*10^46 erg/s; what is the inner radius of the torus?

(Assume bolometric correction of 5, for UV range luminosity)

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
| 规划阶段总时间 (Planner) | 1.524 | 100% |
| 规划过程中启动的任务数 | 1 / 3 | 33.3% |
| 规划与执行重叠的任务数 | 1 / 3 | 33.3% |
| 第一个任务规划完成时间 | 0.963 | - |
| 最后一个任务规划完成时间 | 1.503 | - |
| 最后一个任务执行完成时间 | 23.930 | - |
| 任务总执行时间(累计) | 22.966 | - |
| 流水线加速比 | 1.04x | - |
| 并行效率 | 96.0% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 3 | 22.966 | - |
| 规划模型 | 1 | 1.828 | - |
| 顺序总时间 | - | 24.795 | - |
| 并行总时间 | - | 23.930 | 1.04x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the UV luminosity of the AGN? | 大模型 | 0.963 | 8.619 | 7.655 | 2 |
| 2 | What is the effective temperature of the dust at the inner radius of the torus? | 大模型 | 8.619 | 16.274 | 7.655 | 3 |
| 3 | What is the inner radius of the torus according to Barvainis model? | 大模型 | 16.274 | 23.930 | 7.655 | 4 |

## 理论执行甘特图

```
时间轴:
0                                                            22.97s
+------------------------------------------------------------+
步骤 1 |####################                                        | 0.96s - 8.62s
步骤 2 |                    ####################                    | 8.62s - 16.27s
步骤 3 |                                        ####################| 16.27s - 23.93s
```

