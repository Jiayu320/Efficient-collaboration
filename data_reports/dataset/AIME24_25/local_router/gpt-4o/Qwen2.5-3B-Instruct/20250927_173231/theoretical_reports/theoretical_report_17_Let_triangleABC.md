# 问题 17 的理论性能分析报告

## 问题描述

Let $\triangle ABC$ have circumcenter $O$ and incenter $I$ with $\overline{IA}\perp\overline{OI}$, circumradius $13$, and inradius $6$. Find $AB\cdot AC$.

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
| 规划阶段总时间 (Planner) | 1.559 | 100% |
| 规划过程中启动的任务数 | 1 / 3 | 33.3% |
| 规划与执行重叠的任务数 | 1 / 3 | 33.3% |
| 第一个任务规划完成时间 | 1.021 | - |
| 最后一个任务规划完成时间 | 1.543 | - |
| 最后一个任务执行完成时间 | 4.477 | - |
| 任务总执行时间(累计) | 3.455 | - |
| 流水线加速比 | 2.23x | - |
| 并行效率 | 77.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.155 | - |
| 大模型任务 | 2 | 2.300 | - |
| 规划模型 | 1 | 6.507 | - |
| 顺序总时间 | - | 9.963 | - |
| 并行总时间 | - | 4.477 | 2.23x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Given IA ⊥ OI, what trigonometric relationship between the inradius r=6, circumradius R=13, and angle A at vertex A is derived from vector dot product properties? | 大模型 | 1.021 | 2.241 | 1.219 | 2 |
| 2 | Using the derived relationship in Step 1, what is the value of cos A? | 小模型 | 2.241 | 3.396 | 1.155 | 3 |
| 3 | Given AB · AC = r² + R² for triangles satisfying IA ⊥ OI, what is the numerical value of AB · AC when r=6 and R=13? | 大模型 | 3.396 | 4.477 | 1.081 | 4 |

## 理论执行甘特图

```
时间轴:
0                                                            3.46s
+------------------------------------------------------------+
步骤 1 |#####################                                       | 1.02s - 2.24s
步骤 2 |                     ####################                   | 2.24s - 3.40s
步骤 3 |                                         ###################| 3.40s - 4.48s
```

