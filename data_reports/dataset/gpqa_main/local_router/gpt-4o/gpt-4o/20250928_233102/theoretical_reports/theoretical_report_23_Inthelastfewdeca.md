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
| 路由模型 (saves/Qwen3-4B-Thinking/full/ep5) | 0.690 | 184.10 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 1.787 | 100% |
| 规划过程中启动的任务数 | 2 / 3 | 66.7% |
| 规划与执行重叠的任务数 | 2 / 3 | 66.7% |
| 第一个任务规划完成时间 | 1.081 | - |
| 最后一个任务规划完成时间 | 1.771 | - |
| 最后一个任务执行完成时间 | 3.589 | - |
| 任务总执行时间(累计) | 3.451 | - |
| 流水线加速比 | 2.67x | - |
| 并行效率 | 96.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 0.943 | - |
| 大模型任务 | 2 | 2.508 | - |
| 规划模型 | 1 | 6.133 | - |
| 顺序总时间 | - | 9.583 | - |
| 并行总时间 | - | 3.589 | 2.67x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the explicit formula for the inner torus radius (R_sub) according to the Barvainis model, expressed in terms of bolometric luminosity (L), dust sublimation temperature (T), and bolometric correction (BC)? | 大模型 | 1.081 | 2.370 | 1.289 | 2 |
| 2 | What is the value of the Stefan-Boltzmann constant (σ) in units of erg/s/cm²/K⁴? | 小模型 | 1.326 | 2.268 | 0.943 | 3 |
| 3 | Using the formula from Step 1, the Stefan-Boltzmann constant from Step 2, and the given values (L = 1.5e46 erg/s, T = 900 K, BC = 5), what is the calculated inner radius of the torus in centimeters? | 大模型 | 2.370 | 3.589 | 1.219 | 4 |

## 理论执行甘特图

```
时间轴:
0                                                            2.51s
+------------------------------------------------------------+
步骤 1 |##############################                              | 1.08s - 2.37s
步骤 2 |     #######################                                | 1.33s - 2.27s
步骤 3 |                              ##############################| 2.37s - 3.59s
```

