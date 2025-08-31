# 问题 7 的理论性能分析报告

## 问题描述

Triangle $ABC$ has three different integer side lengths. Side $AC$ is the longest side and side $AB$ is the shortest side. If the perimeter of $ABC$ is 384 units, what is the greatest possible difference $AC - AB$?

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (meta-llama/llama-3-8b-instruct) | 0.554 | 2069.56 |
| 大模型 (openai/gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 4.924 | 100% |
| 规划过程中启动的任务数 | 8 / 9 | 88.9% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 0.992 | - |
| 最后一个任务规划完成时间 | 4.882 | - |
| 最后一个任务执行完成时间 | 6.741 | - |
| 任务总执行时间(累计) | 8.380 | - |
| 流水线加速比 | 3.19x | - |
| 并行效率 | 124.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 9 | 8.380 | - |
| 规划模型 | 1 | 13.140 | - |
| 顺序总时间 | - | 21.520 | - |
| 并行总时间 | - | 6.741 | 3.19x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What are the constraints on the side lengths of triangle ABC? | 大模型 | 0.992 | 1.865 | 0.873 | 2 |
| 2 | What is the relationship between the sides of a valid triangle? | 大模型 | 1.865 | 2.773 | 0.908 | 3 |
| 3 | What are the possible values for side AB? | 大模型 | 2.773 | 3.716 | 0.943 | 4 |
| 4 | What are the possible values for side BC? | 大模型 | 2.773 | 3.716 | 0.943 | 5 |
| 5 | What is the relationship between AC, AB, and BC? | 大模型 | 2.803 | 3.711 | 0.908 | 6 |
| 6 | For each possible value of AB, what is the maximum possible value of AC? | 大模型 | 3.716 | 4.693 | 0.977 | 7 |
| 7 | What is the sum of AB + BC + AC for each valid combination? | 大模型 | 3.913 | 4.856 | 0.943 | 8 |
| 8 | Which combination of side lengths satisfies the perimeter constraint of 384 units? | 大模型 | 4.856 | 5.833 | 0.977 | 9 |
| 9 | What is the greatest possible value of AC - AB? | 大模型 | 5.833 | 6.741 | 0.908 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            5.75s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 0.99s - 1.86s
步骤 2 |         #########                                          | 1.86s - 2.77s
步骤 3 |                  ##########                                | 2.77s - 3.72s
步骤 4 |                  ##########                                | 2.77s - 3.72s
步骤 5 |                  ##########                                | 2.80s - 3.71s
步骤 6 |                            ##########                      | 3.72s - 4.69s
步骤 7 |                              ##########                    | 3.91s - 4.86s
步骤 8 |                                        ##########          | 4.86s - 5.83s
步骤 9 |                                                  ##########| 5.83s - 6.74s
```

