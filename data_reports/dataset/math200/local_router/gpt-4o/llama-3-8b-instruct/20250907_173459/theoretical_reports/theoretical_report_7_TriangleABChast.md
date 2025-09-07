# 问题 7 的理论性能分析报告

## 问题描述

Triangle $ABC$ has three different integer side lengths. Side $AC$ is the longest side and side $AB$ is the shortest side. If the perimeter of $ABC$ is 384 units, what is the greatest possible difference $AC - AB$?

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (meta-llama/llama-3-8b-instruct) | 0.554 | 2069.56 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 4.180 | 100% |
| 规划过程中启动的任务数 | 6 / 7 | 85.7% |
| 规划与执行重叠的任务数 | 6 / 7 | 85.7% |
| 第一个任务规划完成时间 | 1.048 | - |
| 最后一个任务规划完成时间 | 4.138 | - |
| 最后一个任务执行完成时间 | 5.823 | - |
| 任务总执行时间(累计) | 6.252 | - |
| 流水线加速比 | 2.85x | - |
| 并行效率 | 107.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 7 | 6.252 | - |
| 规划模型 | 1 | 10.331 | - |
| 顺序总时间 | - | 16.584 | - |
| 并行总时间 | - | 5.823 | 2.85x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the relationship between sides AB, BC, and AC in a triangle? | 大模型 | 1.048 | 1.921 | 0.873 | 2 |
| 2 | What constraints exist on the side lengths given they must form a valid triangle? | 大模型 | 1.921 | 2.829 | 0.908 | 3 |
| 3 | What are the possible integer values for AB, BC, and AC given their sum is 384? | 大模型 | 2.829 | 3.772 | 0.943 | 4 |
| 4 | What is the constraint on AC - AB given that AC is the longest side? | 大模型 | 2.829 | 3.703 | 0.873 | 5 |
| 5 | What is the constraint on AB + BC given that AC is the longest side? | 大模型 | 3.169 | 4.042 | 0.873 | 6 |
| 6 | How can we maximize AC - AB while satisfying all constraints? | 大模型 | 4.042 | 4.950 | 0.908 | 7 |
| 7 | What is the maximum possible value of AC - AB? | 大模型 | 4.950 | 5.823 | 0.873 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            4.78s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 1.05s - 1.92s
步骤 2 |          ############                                      | 1.92s - 2.83s
步骤 3 |                      ############                          | 2.83s - 3.77s
步骤 4 |                      ###########                           | 2.83s - 3.70s
步骤 5 |                          ###########                       | 3.17s - 4.04s
步骤 6 |                                     ############           | 4.04s - 4.95s
步骤 7 |                                                 ###########| 4.95s - 5.82s
```

