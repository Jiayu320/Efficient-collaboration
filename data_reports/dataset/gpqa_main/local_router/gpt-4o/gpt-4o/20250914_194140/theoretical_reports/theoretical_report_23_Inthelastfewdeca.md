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
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 4.194 | 100% |
| 规划过程中启动的任务数 | 5 / 7 | 71.4% |
| 规划与执行重叠的任务数 | 5 / 7 | 71.4% |
| 第一个任务规划完成时间 | 1.104 | - |
| 最后一个任务规划完成时间 | 4.152 | - |
| 最后一个任务执行完成时间 | 5.989 | - |
| 任务总执行时间(累计) | 5.906 | - |
| 流水线加速比 | 2.71x | - |
| 并行效率 | 98.6% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 0.770 | - |
| 大模型任务 | 6 | 5.137 | - |
| 规划模型 | 1 | 10.331 | - |
| 顺序总时间 | - | 16.238 | - |
| 并行总时间 | - | 5.989 | 2.71x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the formula for the inner radius of the torus in the Barvainis model? | 大模型 | 1.104 | 1.977 | 0.873 | 2 |
| 2 | What is the sublimation temperature of dust grains given in the problem? | 小模型 | 1.581 | 2.351 | 0.770 | 3 |
| 3 | What is the UV luminosity of the AGN after applying the bolometric correction? | 大模型 | 2.087 | 2.926 | 0.839 | 4 |
| 4 | How do we convert erg/s to a more standard unit of luminosity? | 大模型 | 2.565 | 3.369 | 0.804 | 5 |
| 5 | What value should we substitute for the luminosity of the AGN in the formula? | 大模型 | 3.369 | 4.277 | 0.908 | 6 |
| 6 | How do we calculate the inner radius using the known values and formula? | 大模型 | 4.277 | 5.150 | 0.873 | 7 |
| 7 | What is the final value for the inner radius of the torus? | 大模型 | 5.150 | 5.989 | 0.839 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            4.89s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 1.10s - 1.98s
步骤 2 |     ##########                                             | 1.58s - 2.35s
步骤 3 |            ##########                                      | 2.09s - 2.93s
步骤 4 |                 ##########                                 | 2.56s - 3.37s
步骤 5 |                           ###########                      | 3.37s - 4.28s
步骤 6 |                                      ###########           | 4.28s - 5.15s
步骤 7 |                                                 ###########| 5.15s - 5.99s
```

