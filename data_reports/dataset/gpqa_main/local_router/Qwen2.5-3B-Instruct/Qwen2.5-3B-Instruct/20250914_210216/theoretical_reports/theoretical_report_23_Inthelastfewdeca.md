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
| 规划阶段总时间 (Planner) | 3.730 | 100% |
| 规划过程中启动的任务数 | 4 / 6 | 66.7% |
| 规划与执行重叠的任务数 | 4 / 6 | 66.7% |
| 第一个任务规划完成时间 | 1.076 | - |
| 最后一个任务规划完成时间 | 3.688 | - |
| 最后一个任务执行完成时间 | 6.722 | - |
| 任务总执行时间(累计) | 7.859 | - |
| 流水线加速比 | 2.50x | - |
| 并行效率 | 116.9% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 6 | 7.859 | - |
| 规划模型 | 1 | 8.927 | - |
| 顺序总时间 | - | 16.786 | - |
| 并行总时间 | - | 6.722 | 2.50x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the basic Barvainis model for the inner radius of the torus? | 大模型 | 1.076 | 2.541 | 1.465 | 2 |
| 2 | What are the given parameters: dust sublimation temperature, bolometric luminosity, and bolometric correction? | 大模型 | 1.638 | 2.793 | 1.155 | 3 |
| 3 | How does the bolometric correction affect the UV luminosity calculation? | 大模型 | 2.793 | 4.102 | 1.310 | 4 |
| 4 | What is the formula relating inner radius to luminosity in the Barvainis model? | 大模型 | 2.635 | 3.945 | 1.310 | 5 |
| 5 | Calculate the UV luminosity using the bolometric luminosity and correction factor? | 大模型 | 4.102 | 5.335 | 1.232 | 6 |
| 6 | Substitute values into the Barvainis formula to find the inner radius? | 大模型 | 5.335 | 6.722 | 1.387 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            5.65s
+------------------------------------------------------------+
步骤 1 |###############                                             | 1.08s - 2.54s
步骤 2 |     #############                                          | 1.64s - 2.79s
步骤 4 |                ##############                              | 2.63s - 3.94s
步骤 3 |                  ##############                            | 2.79s - 4.10s
步骤 5 |                                #############               | 4.10s - 5.33s
步骤 6 |                                             ###############| 5.33s - 6.72s
```

