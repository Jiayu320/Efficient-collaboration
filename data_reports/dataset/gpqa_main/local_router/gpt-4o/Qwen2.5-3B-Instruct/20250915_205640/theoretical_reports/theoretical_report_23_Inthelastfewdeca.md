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
| 规划阶段总时间 (Planner) | 3.351 | 100% |
| 规划过程中启动的任务数 | 3 / 5 | 60.0% |
| 规划与执行重叠的任务数 | 3 / 5 | 60.0% |
| 第一个任务规划完成时间 | 1.160 | - |
| 最后一个任务规划完成时间 | 3.309 | - |
| 最后一个任务执行完成时间 | 5.700 | - |
| 任务总执行时间(累计) | 4.540 | - |
| 流水线加速比 | 2.12x | - |
| 并行效率 | 79.6% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 5 | 4.540 | - |
| 规划模型 | 1 | 7.522 | - |
| 顺序总时间 | - | 12.063 | - |
| 并行总时间 | - | 5.700 | 2.12x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the relationship between bolometric luminosity, temperature of dust grain sublimation, and inner radius of the torus? | 大模型 | 1.160 | 2.103 | 0.943 | 2 |
| 2 | How does the bolometric correction of 5 affect the UV luminosity from the bolometric luminosity? | 大模型 | 2.103 | 2.976 | 0.873 | 3 |
| 3 | What is the effective luminosity available for calculating the inner radius of the torus? | 大模型 | 2.976 | 3.884 | 0.908 | 4 |
| 4 | How do we apply the semi-empirical relation to calculate the inner radius given the effective luminosity? | 大模型 | 3.884 | 4.827 | 0.943 | 5 |
| 5 | What is the final value for the inner radius of the torus? | 大模型 | 4.827 | 5.700 | 0.873 | 6 |

## 理论执行甘特图

```
时间轴:
0                                                            4.54s
+------------------------------------------------------------+
步骤 1 |############                                                | 1.16s - 2.10s
步骤 2 |            ###########                                     | 2.10s - 2.98s
步骤 3 |                       #############                        | 2.98s - 3.88s
步骤 4 |                                    ############            | 3.88s - 4.83s
步骤 5 |                                                ############| 4.83s - 5.70s
```

