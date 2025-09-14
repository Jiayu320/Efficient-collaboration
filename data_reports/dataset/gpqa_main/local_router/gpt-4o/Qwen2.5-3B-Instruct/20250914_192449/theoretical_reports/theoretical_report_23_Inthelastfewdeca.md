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
| 小模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 4.278 | 100% |
| 规划过程中启动的任务数 | 6 / 7 | 85.7% |
| 规划与执行重叠的任务数 | 6 / 7 | 85.7% |
| 第一个任务规划完成时间 | 1.118 | - |
| 最后一个任务规划完成时间 | 4.236 | - |
| 最后一个任务执行完成时间 | 6.190 | - |
| 任务总执行时间(累计) | 6.690 | - |
| 流水线加速比 | 2.75x | - |
| 并行效率 | 108.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 7 | 6.690 | - |
| 大模型任务 | 0 | 0.000 | - |
| 规划模型 | 1 | 10.331 | - |
| 顺序总时间 | - | 17.021 | - |
| 并行总时间 | - | 6.190 | 2.75x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the formula for the inner radius of the torus according to the Barvainis model? | 小模型 | 1.118 | 2.118 | 1.000 | 2 |
| 2 | What is the UV luminosity of the AGN given its bolometric luminosity and the bolometric correction? | 小模型 | 1.680 | 2.602 | 0.922 | 3 |
| 3 | What is the sublimation temperature of dust grains in K? | 小模型 | 2.129 | 2.897 | 0.767 | 4 |
| 4 | How do we convert the sublimation temperature to a wavelength in the UV range? | 小模型 | 2.897 | 3.819 | 0.922 | 5 |
| 5 | What is the Planck's constant in appropriate units for this calculation? | 小模型 | 3.112 | 3.957 | 0.845 | 6 |
| 6 | What is the formula for the inner radius using the UV luminosity, sublimation temperature, and Planck's constant? | 小模型 | 3.957 | 5.035 | 1.077 | 7 |
| 7 | What is the inner radius of the torus? | 小模型 | 5.035 | 6.190 | 1.155 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            5.07s
+------------------------------------------------------------+
步骤 1 |###########                                                 | 1.12s - 2.12s
步骤 2 |      ###########                                           | 1.68s - 2.60s
步骤 3 |           ##########                                       | 2.13s - 2.90s
步骤 4 |                     ##########                             | 2.90s - 3.82s
步骤 5 |                       ##########                           | 3.11s - 3.96s
步骤 6 |                                 #############              | 3.96s - 5.03s
步骤 7 |                                              ############# | 5.03s - 6.19s
```

