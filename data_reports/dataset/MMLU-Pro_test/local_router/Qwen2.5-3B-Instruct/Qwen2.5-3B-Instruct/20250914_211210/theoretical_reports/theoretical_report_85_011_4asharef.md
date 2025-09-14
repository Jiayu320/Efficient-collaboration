# 问题 85 的理论性能分析报告

## 问题描述

$ .01(1/4) a share for stocks under $5 a share par value $ .02(1/2) a share for stocks from $5-$10 a share par value $ .03(3/4) a share for stocks from $10-$20 a share par value $ .05 a share for stocks over $20 a share par value Mr. Carr sold 300 shares of stock having a par value of $50 per share. What was the New York State transfer tax?

A. $50
B. $20
C. $40
D. $15
E. $30
F. $10
G. $25
H. $35
I. $5
J. $12.50

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
| 规划阶段总时间 (Planner) | 3.393 | 100% |
| 规划过程中启动的任务数 | 4 / 6 | 66.7% |
| 规划与执行重叠的任务数 | 4 / 6 | 66.7% |
| 第一个任务规划完成时间 | 1.076 | - |
| 最后一个任务规划完成时间 | 3.351 | - |
| 最后一个任务执行完成时间 | 6.076 | - |
| 任务总执行时间(累计) | 5.922 | - |
| 流水线加速比 | 2.44x | - |
| 并行效率 | 97.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 6 | 5.922 | - |
| 规划模型 | 1 | 8.927 | - |
| 顺序总时间 | - | 14.849 | - |
| 并行总时间 | - | 6.076 | 2.44x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What type of stock did Mr. Carr sell based on the par value ($50)? | 大模型 | 1.076 | 2.076 | 1.000 | 2 |
| 2 | What is the applicable share price for the stock type determined in Step 1? | 大模型 | 2.076 | 3.153 | 1.077 | 3 |
| 3 | What is the total value of the stock transaction before tax? | 大模型 | 3.153 | 4.153 | 1.000 | 4 |
| 4 | What is the tax rate applied to the stock transaction? | 大模型 | 2.494 | 3.417 | 0.922 | 5 |
| 5 | What is the calculated transfer tax amount? | 大模型 | 4.153 | 5.153 | 1.000 | 6 |
| 6 | Which answer choice matches our calculated transfer tax? | 大模型 | 5.153 | 6.076 | 0.922 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            5.00s
+------------------------------------------------------------+
步骤 1 |############                                                | 1.08s - 2.08s
步骤 2 |            ############                                    | 2.08s - 3.15s
步骤 4 |                 ###########                                | 2.49s - 3.42s
步骤 3 |                        ############                        | 3.15s - 4.15s
步骤 5 |                                    ############            | 4.15s - 5.15s
步骤 6 |                                                ############| 5.15s - 6.08s
```

