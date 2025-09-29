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
| 规划阶段总时间 (Planner) | 2.461 | 100% |
| 规划过程中启动的任务数 | 4 / 5 | 80.0% |
| 规划与执行重叠的任务数 | 4 / 5 | 80.0% |
| 第一个任务规划完成时间 | 1.130 | - |
| 最后一个任务规划完成时间 | 2.444 | - |
| 最后一个任务执行完成时间 | 4.809 | - |
| 任务总执行时间(累计) | 5.675 | - |
| 流水线加速比 | 2.72x | - |
| 并行效率 | 118.0% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 2.155 | - |
| 大模型任务 | 3 | 3.520 | - |
| 规划模型 | 1 | 7.425 | - |
| 顺序总时间 | - | 13.100 | - |
| 并行总时间 | - | 4.809 | 2.72x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the formula for the dust sublimation radius according to the Barvainis model, expressed as R = 0.05 × L^0.25 × T^-0.5, where L is bolometric luminosity in erg/s and T is sublimation temperature in Kelvin? | 大模型 | 1.130 | 2.349 | 1.219 | 2 |
| 2 | What is the bolometric luminosity L given as 1.5e46 erg/s, and what is the sublimation temperature T given as 900 K? | 小模型 | 1.412 | 2.257 | 0.845 | 3 |
| 3 | Using the formula from Step 1 and the values from Step 2, what is the value of L^0.25 for L = 1.5e46 erg/s? | 大模型 | 2.349 | 3.500 | 1.150 | 4 |
| 4 | Using the formula from Step 1 and the values from Step 2, what is the value of T^0.5 for T = 900 K? | 小模型 | 2.349 | 3.659 | 1.310 | 5 |
| 5 | Using the values of L^0.25 from Step 3 and T^0.5 from Step 4, what is the inner radius R = 0.05 × (L^0.25) / (T^0.5)? | 大模型 | 3.659 | 4.809 | 1.150 | 6 |

## 理论执行甘特图

```
时间轴:
0                                                            3.68s
+------------------------------------------------------------+
步骤 1 |###################                                         | 1.13s - 2.35s
步骤 2 |    ##############                                          | 1.41s - 2.26s
步骤 3 |                   ###################                      | 2.35s - 3.50s
步骤 4 |                   ######################                   | 2.35s - 3.66s
步骤 5 |                                         ###################| 3.66s - 4.81s
```

