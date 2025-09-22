# 问题 3 的理论性能分析报告

## 问题描述

Find the remainder when $9 \times 99 \times 999 \times \cdots \times \underbrace{99\cdots9}_{\text{999 9's}}$ is divided by $1000$ .

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (claude-3-5-sonnet-latest) | 1.338 | 51.49 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 8.854 | 100% |
| 规划过程中启动的任务数 | 8 / 9 | 88.9% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 2.445 | - |
| 最后一个任务规划完成时间 | 8.795 | - |
| 最后一个任务执行完成时间 | 9.898 | - |
| 任务总执行时间(累计) | 9.092 | - |
| 流水线加速比 | 2.72x | - |
| 并行效率 | 91.9% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 7 | 7.000 | - |
| 大模型任务 | 2 | 2.093 | - |
| 规划模型 | 1 | 17.865 | - |
| 顺序总时间 | - | 26.957 | - |
| 并行总时间 | - | 9.898 | 2.72x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Express the numbers 9, 99, 999, etc. in the form 10^n - 1. What are the first few terms in this sequence? | 小模型 | 2.445 | 3.600 | 1.155 | 2 |
| 2 | What is the remainder when 9 is divided by 1000? | 小模型 | 3.105 | 3.950 | 0.845 | 3 |
| 3 | What is the remainder when 99 is divided by 1000? | 小模型 | 3.766 | 4.611 | 0.845 | 4 |
| 4 | What is the remainder when 999 is divided by 1000? | 小模型 | 4.426 | 5.271 | 0.845 | 5 |
| 5 | What is the remainder when 9999 (and any number with 4 or more 9's) is divided by 1000? | 小模型 | 5.377 | 6.532 | 1.155 | 6 |
| 6 | How many terms in our product have a remainder of 999 when divided by 1000? | 小模型 | 6.532 | 7.687 | 1.155 | 7 |
| 7 | Calculate (9 × 99) mod 1000. What is this value? | 小模型 | 6.970 | 7.970 | 1.000 | 8 |
| 8 | Calculate (999^997) mod 1000 using modular exponentiation. What is this value? | 大模型 | 7.805 | 8.886 | 1.081 | 9 |
| 9 | Compute the final answer by calculating [(9 × 99) × (999^997)] mod 1000. What is the remainder? | 大模型 | 8.886 | 9.898 | 1.012 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            7.45s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 2.44s - 3.60s
步骤 2 |     #######                                                | 3.11s - 3.95s
步骤 3 |          #######                                           | 3.77s - 4.61s
步骤 4 |               #######                                      | 4.43s - 5.27s
步骤 5 |                       #########                            | 5.38s - 6.53s
步骤 6 |                                ##########                  | 6.53s - 7.69s
步骤 7 |                                    ########                | 6.97s - 7.97s
步骤 8 |                                           ########         | 7.81s - 8.89s
步骤 9 |                                                   #########| 8.89s - 9.90s
```

