# 问题 21 的理论性能分析报告

## 问题描述

Why does the hydroboration reaction between a conjugated diene and Ipc2BH form a single product, even at different temperatures?


# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 5.921 | 100% |
| 规划过程中启动的任务数 | 9 / 10 | 90.0% |
| 规划与执行重叠的任务数 | 9 / 10 | 90.0% |
| 第一个任务规划完成时间 | 1.076 | - |
| 最后一个任务规划完成时间 | 5.879 | - |
| 最后一个任务执行完成时间 | 7.379 | - |
| 任务总执行时间(累计) | 10.154 | - |
| 流水线加速比 | 3.35x | - |
| 并行效率 | 137.6% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 2.232 | - |
| 大模型任务 | 8 | 7.922 | - |
| 规划模型 | 1 | 14.545 | - |
| 顺序总时间 | - | 24.699 | - |
| 并行总时间 | - | 7.379 | 3.35x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the mechanism of hydroboration of conjugated dienes with Ipc2BH? | 大模型 | 1.076 | 2.157 | 1.081 | 2 |
| 2 | How does the electron density and reaction preference differ between different temperatures? | 大模型 | 2.157 | 3.099 | 0.943 | 3 |
| 3 | What role does the Ipc2BH act as in the reaction? | 小模型 | 2.157 | 3.234 | 1.077 | 4 |
| 4 | How does the formation of a single product relate to the stability of intermediates or transition states? | 大模型 | 3.234 | 4.246 | 1.012 | 5 |
| 5 | Why does the reaction not proceed with different stereochemistry at different temperatures? | 大模型 | 3.112 | 4.090 | 0.977 | 6 |
| 6 | What is the significance of conjugated diene in determining the reaction's outcome? | 大模型 | 3.618 | 4.595 | 0.977 | 7 |
| 7 | How does the hydroboration reaction's selectivity relate to the stability of the formed products? | 大模型 | 4.246 | 5.258 | 1.012 | 8 |
| 8 | What experimental evidence supports the formation of a single product in this reaction? | 大模型 | 4.685 | 5.628 | 0.943 | 9 |
| 9 | How do the reaction conditions (temperature) influence the stereochemistry of the final product? | 小模型 | 5.247 | 6.402 | 1.155 | 10 |
| 10 | What is the final conclusion regarding the selectivity of the hydroboration reaction with Ipc2BH? | 大模型 | 6.402 | 7.379 | 0.977 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            6.30s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 1.08s - 2.16s
步骤 2 |          #########                                         | 2.16s - 3.10s
步骤 3 |          ##########                                        | 2.16s - 3.23s
步骤 5 |                   #########                                | 3.11s - 4.09s
步骤 4 |                    ##########                              | 3.23s - 4.25s
步骤 6 |                        #########                           | 3.62s - 4.60s
步骤 7 |                              #########                     | 4.25s - 5.26s
步骤 8 |                                  #########                 | 4.69s - 5.63s
步骤 9 |                                       ###########          | 5.25s - 6.40s
步骤 10 |                                                  ##########| 6.40s - 7.38s
```

