# 问题 4 的理论性能分析报告

## 问题描述

Compute the mean molecular speed v in the heavy gas radon (Rn) in m/s

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 3.743 | 100% |
| 规划过程中启动的任务数 | 3 / 3 | 100.0% |
| 规划与执行重叠的任务数 | 2 / 3 | 66.7% |
| 第一个任务规划完成时间 | 1.449 | - |
| 最后一个任务规划完成时间 | 3.696 | - |
| 最后一个任务执行完成时间 | 4.777 | - |
| 任务总执行时间(累计) | 2.828 | - |
| 流水线加速比 | 2.26x | - |
| 并行效率 | 59.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 3 | 2.828 | - |
| 规划模型 | 1 | 7.989 | - |
| 顺序总时间 | - | 10.817 | - |
| 并行总时间 | - | 4.777 | 2.26x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Convert the molar mass of radon from g/mol to kg/mol. What is the molar mass of radon in kg/mol? | 大模型 | 1.449 | 2.323 | 0.873 | 2 |
| 2 | Ensure the temperature \( T \) is in Kelvin. If the temperature is given in Celsius, convert it to Kelvin by adding 273.15. What is the temperature in Kelvin? | 大模型 | 2.333 | 3.206 | 0.873 | 3 |
| 3 | Substitute the values \( R = 8.314 \, \text{J/(mol·K)} \), \( T \) in Kelvin, and \( M \) in kg/mol into the formula \( v = \sqrt{\frac{8RT}{\pi M}} \). What is the mean molecular speed \( v \) in m/s? | 大模型 | 3.696 | 4.777 | 1.081 | 4 |

## 理论执行甘特图

```
时间轴:
0                                                            3.33s
+------------------------------------------------------------+
步骤 1 |###############                                             | 1.45s - 2.32s
步骤 2 |               ################                             | 2.33s - 3.21s
步骤 3 |                                        ####################| 3.70s - 4.78s
```

