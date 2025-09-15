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
| 规划阶段总时间 (Planner) | 2.888 | 100% |
| 规划过程中启动的任务数 | 3 / 4 | 75.0% |
| 规划与执行重叠的任务数 | 3 / 4 | 75.0% |
| 第一个任务规划完成时间 | 1.146 | - |
| 最后一个任务规划完成时间 | 2.846 | - |
| 最后一个任务执行完成时间 | 4.232 | - |
| 任务总执行时间(累计) | 3.940 | - |
| 流水线加速比 | 2.38x | - |
| 并行效率 | 93.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.077 | - |
| 大模型任务 | 3 | 2.862 | - |
| 规划模型 | 1 | 6.118 | - |
| 顺序总时间 | - | 10.058 | - |
| 并行总时间 | - | 4.232 | 2.38x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the relationship between bolometric luminosity, dust grain sublimation temperature, and inner radius of the torus? | 大模型 | 1.146 | 2.089 | 0.943 | 2 |
| 2 | How does the bolometric correction of 5 affect the UV luminosity to obtain the total bolometric luminosity? | 小模型 | 1.722 | 2.799 | 1.077 | 3 |
| 3 | What is the formula to calculate the inner radius of the torus using the sublimation temperature and luminosity? | 大模型 | 2.312 | 3.254 | 0.943 | 4 |
| 4 | What is the calculated inner radius using the given values and the derived formula? | 大模型 | 3.254 | 4.232 | 0.977 | 5 |

## 理论执行甘特图

```
时间轴:
0                                                            3.09s
+------------------------------------------------------------+
步骤 1 |##################                                          | 1.15s - 2.09s
步骤 2 |           #####################                            | 1.72s - 2.80s
步骤 3 |                      ##################                    | 2.31s - 3.25s
步骤 4 |                                        ################### | 3.25s - 4.23s
```

