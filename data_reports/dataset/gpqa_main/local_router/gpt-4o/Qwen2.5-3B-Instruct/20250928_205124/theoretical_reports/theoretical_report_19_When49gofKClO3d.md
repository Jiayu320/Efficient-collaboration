# 问题 19 的理论性能分析报告

## 问题描述

When 49 g of KClO3 decomposes, the resulting O2 reacts with 10.8 g of impure metal (20% purity) to form metal oxide. Calculate the amount of carbon needed to convert the metal oxide back to pure metal. The metal is amphoteric in nature and is one of the most abundant metals in earth crust.

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
| 规划阶段总时间 (Planner) | 2.722 | 100% |
| 规划过程中启动的任务数 | 3 / 7 | 42.9% |
| 规划与执行重叠的任务数 | 3 / 7 | 42.9% |
| 第一个任务规划完成时间 | 0.886 | - |
| 最后一个任务规划完成时间 | 2.705 | - |
| 最后一个任务执行完成时间 | 6.296 | - |
| 任务总执行时间(累计) | 7.708 | - |
| 流水线加速比 | 2.49x | - |
| 并行效率 | 122.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 4 | 4.465 | - |
| 大模型任务 | 3 | 3.243 | - |
| 规划模型 | 1 | 7.974 | - |
| 顺序总时间 | - | 15.682 | - |
| 并行总时间 | - | 6.296 | 2.49x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the molar mass of KClO3 in g/mol? | 小模型 | 0.886 | 1.885 | 1.000 | 2 |
| 2 | Using the formula moles = mass / molar mass, what are the moles of KClO3 from 49 g? | 小模型 | 1.885 | 3.040 | 1.155 | 3 |
| 3 | According to the decomposition reaction 2KClO3 → 2KCl + 3O2, what is the mole ratio of O2 to KClO3? Using this ratio, what are the moles of O2 produced? | 大模型 | 3.040 | 4.052 | 1.012 | 4 |
| 4 | Given the impure metal has 20% purity, what is the mass of pure metal in 10.8 g of sample? | 小模型 | 1.755 | 2.910 | 1.155 | 5 |
| 5 | Using the molar mass of aluminum (26.98 g/mol), what are the moles of pure aluminum in the mass calculated in Step 4? | 小模型 | 2.910 | 4.064 | 1.155 | 6 |
| 6 | For the reduction reaction 2Al2O3 + 3C → 4Al + 3CO2, what is the mole ratio of carbon to aluminum? Using this ratio, what is the moles of carbon required for the aluminum moles from Step 5? | 大模型 | 4.064 | 5.215 | 1.150 | 7 |
| 7 | Using the molar mass of carbon (12 g/mol), what is the final mass of carbon needed to convert the metal oxide back to pure metal? | 大模型 | 5.215 | 6.296 | 1.081 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            5.41s
+------------------------------------------------------------+
步骤 1 |###########                                                 | 0.89s - 1.89s
步骤 4 |         #############                                      | 1.75s - 2.91s
步骤 2 |           ############                                     | 1.89s - 3.04s
步骤 5 |                      #############                         | 2.91s - 4.06s
步骤 3 |                       ############                         | 3.04s - 4.05s
步骤 6 |                                   #############            | 4.06s - 5.21s
步骤 7 |                                                ############| 5.21s - 6.30s
```

