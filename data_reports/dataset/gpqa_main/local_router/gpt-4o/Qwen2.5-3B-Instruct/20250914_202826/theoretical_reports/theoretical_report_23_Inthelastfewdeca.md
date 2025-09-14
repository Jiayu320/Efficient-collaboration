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
| 规划阶段总时间 (Planner) | 3.520 | 100% |
| 规划过程中启动的任务数 | 3 / 5 | 60.0% |
| 规划与执行重叠的任务数 | 3 / 5 | 60.0% |
| 第一个任务规划完成时间 | 1.118 | - |
| 最后一个任务规划完成时间 | 3.478 | - |
| 最后一个任务执行完成时间 | 5.592 | - |
| 任务总执行时间(累计) | 4.644 | - |
| 流水线加速比 | 2.18x | - |
| 并行效率 | 83.0% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 5 | 4.644 | - |
| 规划模型 | 1 | 7.522 | - |
| 顺序总时间 | - | 12.166 | - |
| 并行总时间 | - | 5.592 | 2.18x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the formula for the inner radius of the torus based on the Barvainis model? | 大模型 | 1.118 | 2.061 | 0.943 | 2 |
| 2 | What are the known values: sublimation temperature (900 K), bolometric luminosity (1.5×10^46 erg/s), and bolometric correction (5)? | 大模型 | 1.890 | 2.798 | 0.908 | 3 |
| 3 | How do we convert the bolometric luminosity to UV luminosity using the bolometric correction? | 大模型 | 2.798 | 3.741 | 0.943 | 4 |
| 4 | What is the effective luminosity in the UV range needed for the calculation? | 大模型 | 3.741 | 4.649 | 0.908 | 5 |
| 5 | How do we calculate the inner radius using the formula and the UV luminosity? | 大模型 | 4.649 | 5.592 | 0.943 | 6 |

## 理论执行甘特图

```
时间轴:
0                                                            4.47s
+------------------------------------------------------------+
步骤 1 |############                                                | 1.12s - 2.06s
步骤 2 |          ############                                      | 1.89s - 2.80s
步骤 3 |                      #############                         | 2.80s - 3.74s
步骤 4 |                                   ############             | 3.74s - 4.65s
步骤 5 |                                               #############| 4.65s - 5.59s
```

