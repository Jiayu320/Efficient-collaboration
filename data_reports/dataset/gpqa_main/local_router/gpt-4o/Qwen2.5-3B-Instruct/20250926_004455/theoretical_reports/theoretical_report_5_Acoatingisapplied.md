# 问题 5 的理论性能分析报告

## 问题描述

A coating is applied to a substrate resulting in a perfectly smooth surface. The measured contact angles of this smooth coating are 132° and 102° for water and hexadecane respectively. The coating formulation is then modified and when now applied to the same type of substrate, a rough surface is produced. When a droplet of water or oil sits on the rough surface, the wettability of the surface can now be described by the Cassie-Baxter state. The water contact angle on the rough surface is now 148°. What would be the best estimate of the contact angle of a droplet of octane on the rough surface? 

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Thinking/full/train_2025-09-25-23-33-09) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 4.784 | 100% |
| 规划过程中启动的任务数 | 4 / 4 | 100.0% |
| 规划与执行重叠的任务数 | 3 / 4 | 75.0% |
| 第一个任务规划完成时间 | 1.567 | - |
| 最后一个任务规划完成时间 | 4.742 | - |
| 最后一个任务执行完成时间 | 5.892 | - |
| 任务总执行时间(累计) | 4.606 | - |
| 流水线加速比 | 4.46x | - |
| 并行效率 | 78.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.155 | - |
| 大模型任务 | 3 | 3.451 | - |
| 规划模型 | 1 | 21.652 | - |
| 顺序总时间 | - | 26.257 | - |
| 并行总时间 | - | 5.892 | 4.46x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Using θₐ₁ = 148° (water on rough surface) and θₖ₁ = 132° (water on smooth surface), what is θₜ = θₖ₁ - θₐ₁ via Cassie-Baxter formula? | 大模型 | 1.567 | 2.718 | 1.150 | 2 |
| 2 | Using θₖ₁ = 132° (water on smooth surface) and θₐ₂ = 102° (hexadecane on smooth surface), what is θₖ₂ = θₖ₁ - θₐ₂ via Young's equation for two liquids? | 大模型 | 2.649 | 3.799 | 1.150 | 3 |
| 3 | Sum θₖ₁ (Step 2) and θₖ₂ (Step 2) to verify θₖ₁ + θₖ₂ equals 234°, the sum of known smooth-surface contact angles. What is this sum? | 小模型 | 3.799 | 4.954 | 1.155 | 4 |
| 4 | Using θₖ₁ = 132° (Step 2) and θₐ₁ = 148° (Step 1), what is θₖ₃ = θₖ₁ - θₐ₁ via Cassie-Baxter formula for octane? | 大模型 | 4.742 | 5.892 | 1.150 | 5 |

## 理论执行甘特图

```
时间轴:
0                                                            4.32s
+------------------------------------------------------------+
步骤 1 |###############                                             | 1.57s - 2.72s
步骤 2 |               ###############                              | 2.65s - 3.80s
步骤 3 |                              ################              | 3.80s - 4.95s
步骤 4 |                                            ################| 4.74s - 5.89s
```

