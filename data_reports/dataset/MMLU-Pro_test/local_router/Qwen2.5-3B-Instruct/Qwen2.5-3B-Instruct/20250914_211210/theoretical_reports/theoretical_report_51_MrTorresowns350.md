# 问题 51 的理论性能分析报告

## 问题描述

Mr. Torres owns 350 shares of Krescostock paying a quarterly dividend of $1.20 per share, with an extra year-end dividend of $.30 per share. What was his total income from the stock for the year?

A. $1,920
B. $1,710
C. $1,470
D. $1,680
E. $1,595
F. $1,260
G. $1,890
H. $1,785
I. $2,000
J. $1,650

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
| 规划阶段总时间 (Planner) | 3.225 | 100% |
| 规划过程中启动的任务数 | 4 / 6 | 66.7% |
| 规划与执行重叠的任务数 | 4 / 6 | 66.7% |
| 第一个任务规划完成时间 | 0.935 | - |
| 最后一个任务规划完成时间 | 3.183 | - |
| 最后一个任务执行完成时间 | 5.328 | - |
| 任务总执行时间(累计) | 5.922 | - |
| 流水线加速比 | 2.79x | - |
| 并行效率 | 111.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 1.845 | - |
| 大模型任务 | 4 | 4.077 | - |
| 规划模型 | 1 | 8.927 | - |
| 顺序总时间 | - | 14.849 | - |
| 并行总时间 | - | 5.328 | 2.79x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the quarterly dividend per share? | 小模型 | 0.935 | 1.858 | 0.922 | 2 |
| 2 | How many quarters are in a year? | 小模型 | 1.329 | 2.251 | 0.922 | 3 |
| 3 | What is the total quarterly income from dividends? | 大模型 | 2.251 | 3.251 | 1.000 | 4 |
| 4 | What is the total income from the extra year-end dividend? | 大模型 | 2.228 | 3.227 | 1.000 | 5 |
| 5 | What is Mr. Torres's total income from the stock for the year? | 大模型 | 3.251 | 4.328 | 1.077 | 6 |
| 6 | Which answer choice matches our calculated total income? | 大模型 | 4.328 | 5.328 | 1.000 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            4.39s
+------------------------------------------------------------+
步骤 1 |############                                                | 0.94s - 1.86s
步骤 2 |     ############                                           | 1.33s - 2.25s
步骤 4 |                 ##############                             | 2.23s - 3.23s
步骤 3 |                 ##############                             | 2.25s - 3.25s
步骤 5 |                               ###############              | 3.25s - 4.33s
步骤 6 |                                              ##############| 4.33s - 5.33s
```

