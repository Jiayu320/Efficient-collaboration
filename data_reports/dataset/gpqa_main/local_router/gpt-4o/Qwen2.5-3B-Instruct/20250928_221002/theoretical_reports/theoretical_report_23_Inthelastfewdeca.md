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
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-4B-Thinking/full/ep5) | 0.690 | 184.10 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 1.336 | 100% |
| 规划过程中启动的任务数 | 1 / 2 | 50.0% |
| 规划与执行重叠的任务数 | 1 / 2 | 50.0% |
| 第一个任务规划完成时间 | 0.940 | - |
| 最后一个任务规划完成时间 | 1.320 | - |
| 最后一个任务执行完成时间 | 3.677 | - |
| 任务总执行时间(累计) | 2.737 | - |
| 流水线加速比 | 2.18x | - |
| 并行效率 | 74.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.310 | - |
| 大模型任务 | 1 | 1.427 | - |
| 规划模型 | 1 | 5.285 | - |
| 顺序总时间 | - | 8.022 | - |
| 并行总时间 | - | 3.677 | 2.18x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the given bolometric luminosity L in erg/s, and what is the sublimation temperature T in Kelvin? | 小模型 | 0.940 | 2.250 | 1.310 | 2 |
| 2 | Using the formula R = sqrt(L / (4 * π * σ * T^4)), where σ = 5.67e-12 erg s² K⁻⁴ cm⁻², what is the value of R in centimeters? | 大模型 | 2.250 | 3.677 | 1.427 | 3 |

## 理论执行甘特图

```
时间轴:
0                                                            2.74s
+------------------------------------------------------------+
步骤 1 |############################                                | 0.94s - 2.25s
步骤 2 |                            ############################### | 2.25s - 3.68s
```

