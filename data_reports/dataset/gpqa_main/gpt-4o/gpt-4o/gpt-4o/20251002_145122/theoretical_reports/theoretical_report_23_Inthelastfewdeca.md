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
| 规划阶段总时间 (Planner) | 1.469 | 100% |
| 规划过程中启动的任务数 | 1 / 2 | 50.0% |
| 规划与执行重叠的任务数 | 1 / 2 | 50.0% |
| 第一个任务规划完成时间 | 1.039 | - |
| 最后一个任务规划完成时间 | 1.448 | - |
| 最后一个任务执行完成时间 | 16.350 | - |
| 任务总执行时间(累计) | 15.311 | - |
| 流水线加速比 | 1.06x | - |
| 并行效率 | 93.6% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 15.311 | - |
| 大模型任务 | 0 | 0.000 | - |
| 规划模型 | 1 | 1.974 | - |
| 顺序总时间 | - | 17.285 | - |
| 并行总时间 | - | 16.350 | 1.06x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Calculate the UV range luminosity of the AGN using the given bolometric luminosity and bolometric correction factor. | 小模型 | 1.039 | 8.695 | 7.655 | 2 |
| 2 | Using the Barvainis model, determine the inner radius of the torus based on the UV range luminosity from Step 1 and the dust grain sublimation temperature of 900 K. | 小模型 | 8.695 | 16.350 | 7.655 | 3 |

## 理论执行甘特图

```
时间轴:
0                                                            15.31s
+------------------------------------------------------------+
步骤 1 |#############################                               | 1.04s - 8.69s
步骤 2 |                             ############################## | 8.69s - 16.35s
```

