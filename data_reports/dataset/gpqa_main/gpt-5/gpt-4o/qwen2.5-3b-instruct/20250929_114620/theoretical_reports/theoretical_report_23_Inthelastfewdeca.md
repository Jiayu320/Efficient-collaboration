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
| 路由模型 (gpt-5) | 6.407 | 50.57 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 11.647 | 100% |
| 规划过程中启动的任务数 | 3 / 3 | 100.0% |
| 规划与执行重叠的任务数 | 2 / 3 | 66.7% |
| 第一个任务规划完成时间 | 8.364 | - |
| 最后一个任务规划完成时间 | 11.587 | - |
| 最后一个任务执行完成时间 | 12.737 | - |
| 任务总执行时间(累计) | 4.026 | - |
| 流水线加速比 | 1.79x | - |
| 并行效率 | 31.6% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.310 | - |
| 大模型任务 | 2 | 2.716 | - |
| 规划模型 | 1 | 18.765 | - |
| 顺序总时间 | - | 22.790 | - |
| 并行总时间 | - | 12.737 | 1.79x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the Barvainis (1987) dust sublimation radius relation r_sub as a function of UV luminosity (L_UV), dust sublimation temperature (T_sub), and grain size (a), including the numerical coefficient, exponents, normalization (e.g., L_46, T_1500, a_0.05), and the assumed grain composition? | 大模型 | 8.364 | 9.930 | 1.565 | 2 |
| 2 | Given L_bol = 1.5 × 10^46 erg/s and a bolometric correction of 5 for the UV range, what is the UV luminosity L_UV and its normalized value L_46 to be used in the Barvainis relation? | 小模型 | 9.847 | 11.157 | 1.310 | 3 |
| 3 | Using the Barvainis relation from Step 1, with T_sub = 900 K and the standard grain size assumption from Step 1, and the L_UV (L_46) from Step 2, what is the inner (sublimation) radius r_sub of the torus in parsecs? | 大模型 | 11.587 | 12.737 | 1.150 | 4 |

## 理论执行甘特图

```
时间轴:
0                                                            4.37s
+------------------------------------------------------------+
步骤 1 |#####################                                       | 8.36s - 9.93s
步骤 2 |                    ##################                      | 9.85s - 11.16s
步骤 3 |                                            ################| 11.59s - 12.74s
```

