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
| 大模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 4.433 | 100% |
| 规划过程中启动的任务数 | 6 / 7 | 85.7% |
| 规划与执行重叠的任务数 | 6 / 7 | 85.7% |
| 第一个任务规划完成时间 | 1.104 | - |
| 最后一个任务规划完成时间 | 4.390 | - |
| 最后一个任务执行完成时间 | 6.005 | - |
| 任务总执行时间(累计) | 7.619 | - |
| 流水线加速比 | 2.99x | - |
| 并行效率 | 126.9% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 0.922 | - |
| 大模型任务 | 6 | 6.697 | - |
| 规划模型 | 1 | 10.331 | - |
| 顺序总时间 | - | 17.951 | - |
| 并行总时间 | - | 6.005 | 2.99x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the formula for the inner radius of the torus in the Barvainis model? | 大模型 | 1.104 | 2.259 | 1.155 | 2 |
| 2 | What is the UV luminosity of the AGN given its bolometric luminosity and the bolometric correction? | 大模型 | 1.666 | 2.743 | 1.077 | 3 |
| 3 | What are the known values for the dust sublimation temperature and AGN luminosity? | 小模型 | 2.171 | 3.094 | 0.922 | 4 |
| 4 | What is the value of the Planck constant in appropriate units? | 大模型 | 2.621 | 3.621 | 1.000 | 5 |
| 5 | What is the radius of a dust grain at the sublimation temperature of 900 K? | 大模型 | 3.621 | 4.853 | 1.232 | 6 |
| 6 | How does the inner radius of the torus relate to the dust grain radius and the UV luminosity? | 大模型 | 3.772 | 4.927 | 1.155 | 7 |
| 7 | What is the inner radius of the torus based on the Barvainis model calculation? | 大模型 | 4.927 | 6.005 | 1.077 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            4.90s
+------------------------------------------------------------+
步骤 1 |##############                                              | 1.10s - 2.26s
步骤 2 |      ##############                                        | 1.67s - 2.74s
步骤 3 |             ###########                                    | 2.17s - 3.09s
步骤 4 |                  ############                              | 2.62s - 3.62s
步骤 5 |                              ###############               | 3.62s - 4.85s
步骤 6 |                                ##############              | 3.77s - 4.93s
步骤 7 |                                              ##############| 4.93s - 6.00s
```

