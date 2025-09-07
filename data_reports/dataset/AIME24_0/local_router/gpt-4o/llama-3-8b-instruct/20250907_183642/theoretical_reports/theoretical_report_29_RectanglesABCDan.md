# 问题 29 的理论性能分析报告

## 问题描述

Rectangles $ABCD$ and $EFGH$ are drawn such that $D,E,C,F$ are collinear. Also, $A,D,H,G$ all lie on a circle. If $BC=16$,$AB=107$,$FG=17$, and $EF=184$, what is the length of $CE$?

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
| 规划阶段总时间 (Planner) | 3.997 | 100% |
| 规划过程中启动的任务数 | 5 / 7 | 71.4% |
| 规划与执行重叠的任务数 | 5 / 7 | 71.4% |
| 第一个任务规划完成时间 | 1.062 | - |
| 最后一个任务规划完成时间 | 3.955 | - |
| 最后一个任务执行完成时间 | 6.329 | - |
| 任务总执行时间(累计) | 6.564 | - |
| 流水线加速比 | 2.67x | - |
| 并行效率 | 103.7% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 7 | 6.564 | - |
| 规划模型 | 1 | 10.331 | - |
| 顺序总时间 | - | 16.895 | - |
| 并行总时间 | - | 6.329 | 2.67x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What does it mean for points A,D,H,G to all lie on a circle? | 大模型 | 1.062 | 2.004 | 0.943 | 2 |
| 2 | What properties can we derive from the collinearity of points D,E,C,F? | 大模型 | 1.581 | 2.489 | 0.908 | 3 |
| 3 | Can we establish a relationship between the sides of the rectangles? | 大模型 | 2.489 | 3.467 | 0.977 | 4 |
| 4 | What is the length of AD using the circle property? | 大模型 | 3.467 | 4.479 | 1.012 | 5 |
| 5 | What is the length of DC using the rectangle property? | 大模型 | 3.467 | 4.340 | 0.873 | 6 |
| 6 | What is the length of EC using collinearity and the values given? | 大模型 | 4.479 | 5.456 | 0.977 | 7 |
| 7 | What is the length of CE? | 大模型 | 5.456 | 6.329 | 0.873 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            5.27s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 1.06s - 2.00s
步骤 2 |     ###########                                            | 1.58s - 2.49s
步骤 3 |                ###########                                 | 2.49s - 3.47s
步骤 4 |                           ###########                      | 3.47s - 4.48s
步骤 5 |                           ##########                       | 3.47s - 4.34s
步骤 6 |                                      ############          | 4.48s - 5.46s
步骤 7 |                                                  ##########| 5.46s - 6.33s
```

