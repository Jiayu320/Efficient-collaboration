# 问题 7 的理论性能分析报告

## 问题描述

Triangle $ABC$ has three different integer side lengths. Side $AC$ is the longest side and side $AB$ is the shortest side. If the perimeter of $ABC$ is 384 units, what is the greatest possible difference $AC - AB$?

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (meta-llama/llama-3-8b-instruct) | 0.440 | 3422.00 |
| 大模型 (gpt-4o) | 0.610 | 58.71 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段 (Planner) | 10.331 | 70.9% |
| 任务执行阶段 | 4.246 | 29.1% |
| 总执行时间 | 14.577 | 100% |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 0.443 | - |
| 大模型任务 | 6 | 5.534 | - |
| 规划模型 | 1 | 10.331 | - |
| 顺序总时间 | - | 16.308 | - |
| 并行总时间 | - | 14.577 | 1.12x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the relationship between sides AB, BC, and AC? | 大模型 | 10.331 | 11.282 | 0.951 | 1 |
| 2 | What are the constraints on the possible integer values for AB, BC, and AC? | 大模型 | 11.282 | 12.318 | 1.036 | 1 |
| 3 | What is the minimum possible value for AB? | 大模型 | 12.318 | 13.183 | 0.865 | 1 |
| 4 | What is the maximum possible value for BC? | 大模型 | 12.318 | 13.183 | 0.865 | 2 |
| 5 | What is the maximum possible value for AC? | 大模型 | 12.318 | 13.183 | 0.865 | 3 |
| 6 | What is the sum of AB + BC + AC? | 小模型 | 13.183 | 13.626 | 0.443 | 1 |
| 7 | What is the maximum value of AC - AB? | 大模型 | 13.626 | 14.577 | 0.951 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            4.25s
+------------------------------------------------------------+
步骤 1 |#############                                               | 10.33s - 11.28s
步骤 2 |             ###############                                | 11.28s - 12.32s
步骤 3 |                            ############                    | 12.32s - 13.18s
步骤 4 |                            ############                    | 12.32s - 13.18s
步骤 5 |                            ############                    | 12.32s - 13.18s
步骤 6 |                                        ######              | 13.18s - 13.63s
步骤 7 |                                              ############# | 13.63s - 14.58s
```

## 关键路径分析

关键路径是决定总执行时间的最长任务链。以下是本次执行的关键路径：

| 步骤 | 任务描述 | 执行时间 (秒) |
| --- | --- | --- |
| 7 | What is the maximum value of AC - AB? | 0.951 |

关键路径总时间: 0.951 秒
