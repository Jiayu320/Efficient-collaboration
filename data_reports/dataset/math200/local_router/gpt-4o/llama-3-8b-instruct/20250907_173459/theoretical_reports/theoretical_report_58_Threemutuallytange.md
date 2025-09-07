# 问题 58 的理论性能分析报告

## 问题描述

Three mutually tangent spheres of radius 1 rest on a horizontal plane.  A sphere of radius 2 rests on them.  What is the distance from the plane to the top of the larger sphere?

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
| 规划阶段总时间 (Planner) | 2.719 | 100% |
| 规划过程中启动的任务数 | 2 / 4 | 50.0% |
| 规划与执行重叠的任务数 | 2 / 4 | 50.0% |
| 第一个任务规划完成时间 | 1.062 | - |
| 最后一个任务规划完成时间 | 2.677 | - |
| 最后一个任务执行完成时间 | 4.901 | - |
| 任务总执行时间(累计) | 3.840 | - |
| 流水线加速比 | 2.03x | - |
| 并行效率 | 78.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 4 | 3.840 | - |
| 规划模型 | 1 | 6.118 | - |
| 顺序总时间 | - | 9.958 | - |
| 并行总时间 | - | 4.901 | 2.03x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the vertical distance from the plane to the centers of the three smaller spheres? | 大模型 | 1.062 | 2.004 | 0.943 | 2 |
| 2 | What is the relationship between the centers of the three small spheres and the larger sphere? | 大模型 | 2.004 | 3.016 | 1.012 | 3 |
| 3 | What is the vertical distance from the plane to the center of the larger sphere? | 大模型 | 3.016 | 3.993 | 0.977 | 4 |
| 4 | What is the vertical distance from the center of the larger sphere to its top point? | 大模型 | 3.993 | 4.901 | 0.908 | 5 |

## 理论执行甘特图

```
时间轴:
0                                                            3.84s
+------------------------------------------------------------+
步骤 1 |##############                                              | 1.06s - 2.00s
步骤 2 |              ################                              | 2.00s - 3.02s
步骤 3 |                              ###############               | 3.02s - 3.99s
步骤 4 |                                             ############## | 3.99s - 4.90s
```

