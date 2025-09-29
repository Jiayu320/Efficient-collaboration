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
| 规划阶段总时间 (Planner) | 1.445 | 100% |
| 规划过程中启动的任务数 | 2 / 2 | 100.0% |
| 规划与执行重叠的任务数 | 1 / 2 | 50.0% |
| 第一个任务规划完成时间 | 1.038 | - |
| 最后一个任务规划完成时间 | 1.429 | - |
| 最后一个任务执行完成时间 | 2.510 | - |
| 任务总执行时间(累计) | 2.391 | - |
| 流水线加速比 | 2.99x | - |
| 并行效率 | 95.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.310 | - |
| 大模型任务 | 1 | 1.081 | - |
| 规划模型 | 1 | 5.122 | - |
| 顺序总时间 | - | 7.513 | - |
| 并行总时间 | - | 2.510 | 2.99x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Using the bolometric luminosity of 1.5e46 erg/s and a bolometric correction of 5, what is the UV range luminosity calculated as L_UV = L_bol / BC? | 小模型 | 1.038 | 2.348 | 1.310 | 2 |
| 2 | Applying the Barvainis model formula R = 0.1 * sqrt(L_bol / 1e44) where L_bol is 1.5e46 erg/s, what is the inner radius of the torus in parsecs? | 大模型 | 1.429 | 2.510 | 1.081 | 3 |

## 理论执行甘特图

```
时间轴:
0                                                            1.47s
+------------------------------------------------------------+
步骤 1 |#####################################################       | 1.04s - 2.35s
步骤 2 |               #############################################| 1.43s - 2.51s
```

