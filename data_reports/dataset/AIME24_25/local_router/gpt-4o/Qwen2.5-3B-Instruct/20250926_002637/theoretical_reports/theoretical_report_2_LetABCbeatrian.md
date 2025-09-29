# 问题 2 的理论性能分析报告

## 问题描述

Let $ABC$ be a triangle inscribed in circle $\omega$. Let the tangents to $\omega$ at $B$ and $C$ intersect at point $D$, and let $\overline{AD}$ intersect $\omega$ at $P$. If $AB=5$, $BC=9$, and $AC=10$, $AP$ can be written as the form $\frac{m}{n}$, where $m$ and $n$ are relatively prime integers. Find $m + n$.

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
| 规划阶段总时间 (Planner) | 4.278 | 100% |
| 规划过程中启动的任务数 | 3 / 5 | 60.0% |
| 规划与执行重叠的任务数 | 3 / 5 | 60.0% |
| 第一个任务规划完成时间 | 1.371 | - |
| 最后一个任务规划完成时间 | 4.236 | - |
| 最后一个任务执行完成时间 | 6.721 | - |
| 任务总执行时间(累计) | 5.756 | - |
| 流水线加速比 | 2.97x | - |
| 并行效率 | 85.6% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.155 | - |
| 大模型任务 | 4 | 4.601 | - |
| 规划模型 | 1 | 14.236 | - |
| 顺序总时间 | - | 19.992 | - |
| 并行总时间 | - | 6.721 | 2.97x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Using the Law of Cosines, compute cos B and cos C for triangle ABC with sides AB=5, BC=9, and AC=10. What are cos B and cos C? | 大模型 | 1.371 | 2.521 | 1.150 | 2 |
| 2 | Calculate BP * PC using BP = 9 - 5 = 4 and PC = 9 + 5 = 14. What is BP * PC? | 小模型 | 2.115 | 3.270 | 1.155 | 3 |
| 3 | Solve the quadratic equation PD² - 13 PD - 32 = 0 for PD using BP * PC from Step 2. What is the positive root PD? | 大模型 | 3.270 | 4.489 | 1.219 | 4 |
| 4 | Compute AP = PD - AD where AD = 13 (from AB² + AC² = AD²). Using PD from Step 3, what is AP? | 大模型 | 4.489 | 5.571 | 1.081 | 5 |
| 5 | Simplify AP to the reduced fraction m/n where m and n are coprime. What is m + n? | 大模型 | 5.571 | 6.721 | 1.150 | 6 |

## 理论执行甘特图

```
时间轴:
0                                                            5.35s
+------------------------------------------------------------+
步骤 1 |############                                                | 1.37s - 2.52s
步骤 2 |        #############                                       | 2.12s - 3.27s
步骤 3 |                     #############                          | 3.27s - 4.49s
步骤 4 |                                  #############             | 4.49s - 5.57s
步骤 5 |                                               #############| 5.57s - 6.72s
```

