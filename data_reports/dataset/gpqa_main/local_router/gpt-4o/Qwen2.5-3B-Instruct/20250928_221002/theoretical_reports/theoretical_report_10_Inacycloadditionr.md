# 问题 10 的理论性能分析报告

## 问题描述

In a cycloaddition reaction, two π systems combine to form a single-ring structure. These reactions can occur under two conditions including thermal and photochemical. These reactions follow the general mechanism given below.
Ethene + ethene (Heat) ----- cyclobutane
Mention the cycloaddition products of the following reactions.
(E)-penta-1,3-diene + acrylonitrile  ---> A
cyclopentadiene + methyl acrylate (Heat) ---> B

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
| 规划阶段总时间 (Planner) | 2.216 | 100% |
| 规划过程中启动的任务数 | 3 / 6 | 50.0% |
| 规划与执行重叠的任务数 | 3 / 6 | 50.0% |
| 第一个任务规划完成时间 | 0.983 | - |
| 最后一个任务规划完成时间 | 2.200 | - |
| 最后一个任务执行完成时间 | 5.236 | - |
| 任务总执行时间(累计) | 7.040 | - |
| 流水线加速比 | 2.54x | - |
| 并行效率 | 134.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 6 | 7.040 | - |
| 规划模型 | 1 | 6.241 | - |
| 顺序总时间 | - | 13.281 | - |
| 并行总时间 | - | 5.236 | 2.54x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | How many π bonds does (E)-penta-1,3-diene have, and how many does acrylonitrile have? Are they equal? | 大模型 | 0.983 | 2.134 | 1.150 | 2 |
| 2 | Given the π bond counts from Step 1 and thermal conditions, what type of cycloaddition mechanism applies to reaction A? | 大模型 | 2.134 | 3.353 | 1.219 | 3 |
| 3 | Using the formula ring size = 2 × π bonds per reactant, what is the ring size of product A? | 大模型 | 3.353 | 4.503 | 1.150 | 4 |
| 4 | How many π bonds does cyclopentadiene have, and how many does methyl acrylate have? Are they equal? | 大模型 | 1.717 | 2.867 | 1.150 | 5 |
| 5 | Given the π bond counts from Step 4 and heat, what type of cycloaddition mechanism applies to reaction B? | 大模型 | 2.867 | 4.086 | 1.219 | 6 |
| 6 | Using the formula ring size = 2 × π bonds per reactant, what is the ring size of product B? | 大模型 | 4.086 | 5.236 | 1.150 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            4.25s
+------------------------------------------------------------+
步骤 1 |################                                            | 0.98s - 2.13s
步骤 4 |          ################                                  | 1.72s - 2.87s
步骤 2 |                #################                           | 2.13s - 3.35s
步骤 5 |                          #################                 | 2.87s - 4.09s
步骤 3 |                                 ################           | 3.35s - 4.50s
步骤 6 |                                           #################| 4.09s - 5.24s
```

