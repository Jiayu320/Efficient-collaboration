# 问题 97 的理论性能分析报告

## 问题描述

Which of the following data sets corresponds to an optically active saturated hydrocarbon?

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
| 规划阶段总时间 (Planner) | 3.787 | 100% |
| 规划过程中启动的任务数 | 5 / 7 | 71.4% |
| 规划与执行重叠的任务数 | 5 / 7 | 71.4% |
| 第一个任务规划完成时间 | 0.921 | - |
| 最后一个任务规划完成时间 | 3.744 | - |
| 最后一个任务执行完成时间 | 6.960 | - |
| 任务总执行时间(累计) | 8.239 | - |
| 流水线加速比 | 2.67x | - |
| 并行效率 | 118.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 7 | 8.239 | - |
| 规划模型 | 1 | 10.331 | - |
| 顺序总时间 | - | 18.571 | - |
| 并行总时间 | - | 6.960 | 2.67x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What defines an optically active molecule? | 大模型 | 0.921 | 2.076 | 1.155 | 2 |
| 2 | What structural features make a hydrocarbon optically active? | 大模型 | 2.076 | 3.309 | 1.232 | 3 |
| 3 | What is the general formula for saturated hydrocarbons? | 大模型 | 1.750 | 2.827 | 1.077 | 4 |
| 4 | Which of the given data sets contains only carbon atoms? | 大模型 | 2.185 | 3.340 | 1.155 | 5 |
| 5 | Which of the remaining data sets has a molecular formula that matches the general formula for saturated hydrocarbons? | 大模型 | 3.340 | 4.573 | 1.232 | 6 |
| 6 | Is the hydrocarbon in the selected data set chiral? | 大模型 | 4.573 | 5.883 | 1.310 | 7 |
| 7 | Which of the data sets corresponds to an optically active saturated hydrocarbon? | 大模型 | 5.883 | 6.960 | 1.077 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            6.04s
+------------------------------------------------------------+
步骤 1 |###########                                                 | 0.92s - 2.08s
步骤 3 |        ##########                                          | 1.75s - 2.83s
步骤 2 |           ############                                     | 2.08s - 3.31s
步骤 4 |            ############                                    | 2.19s - 3.34s
步骤 5 |                        ############                        | 3.34s - 4.57s
步骤 6 |                                    #############           | 4.57s - 5.88s
步骤 7 |                                                 ###########| 5.88s - 6.96s
```

