# 问题 14 的理论性能分析报告

## 问题描述

Joanie takes a $\$6,\!000$ loan to pay for her car.  The annual interest rate on the loan is $12\%$.  She makes no payments for 4 years, but has to pay back all the money she owes at the end of 4 years. How much more money will she owe if the interest compounds quarterly than if the interest compounds annually?  Express your answer as a dollar value to the nearest cent.

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (openai/gpt-5) | 6.407 | 50.57 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 11.330 | 100% |
| 规划过程中启动的任务数 | 3 / 4 | 75.0% |
| 规划与执行重叠的任务数 | 3 / 4 | 75.0% |
| 第一个任务规划完成时间 | 7.751 | - |
| 最后一个任务规划完成时间 | 11.271 | - |
| 最后一个任务执行完成时间 | 12.186 | - |
| 任务总执行时间(累计) | 3.799 | - |
| 流水线加速比 | 1.96x | - |
| 并行效率 | 31.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 1.845 | - |
| 大模型任务 | 2 | 1.954 | - |
| 规划模型 | 1 | 20.050 | - |
| 顺序总时间 | - | 23.850 | - |
| 并行总时间 | - | 12.186 | 1.96x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Using compound interest with annual compounding, compute A_annual = P·(1 + r)^t with P = 6000, r = 0.12, t = 4; what is A_annual? | 大模型 | 7.751 | 8.694 | 0.943 | 2 |
| 2 | Using compound interest with quarterly compounding, compute A_quarterly = P·(1 + r/m)^(m·t) with P = 6000, r = 0.12, m = 4, t = 4; what is A_quarterly? | 大模型 | 9.274 | 10.286 | 1.012 | 3 |
| 3 | Using the results from Steps 1 and 2, compute the unrounded difference Δ = A_quarterly − A_annual; what is Δ? | 小模型 | 10.342 | 11.341 | 1.000 | 4 |
| 4 | Round Δ from Step 3 to the nearest cent; how much more is owed under quarterly compounding than annual compounding, in dollars? | 小模型 | 11.341 | 12.186 | 0.845 | 5 |

## 理论执行甘特图

```
时间轴:
0                                                            4.44s
+------------------------------------------------------------+
步骤 1 |############                                                | 7.75s - 8.69s
步骤 2 |                    ##############                          | 9.27s - 10.29s
步骤 3 |                                   #############            | 10.34s - 11.34s
步骤 4 |                                                ############| 11.34s - 12.19s
```

