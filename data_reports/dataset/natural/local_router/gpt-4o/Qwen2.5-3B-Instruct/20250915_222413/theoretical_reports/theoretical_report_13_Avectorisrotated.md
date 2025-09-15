# 问题 13 的理论性能分析报告

## 问题描述

A vector is rotated by Euler angles $\alpha$, $\beta$, and $\gamma$ around the $x$, $y$, and $z$ axes, respectively. The resulting vector is $v$. Describe the steps to recover the original vector $v_0$ by applying inverse rotations. Provide the mathematical expression for the rotation matrices and the order in which they should be applied to $v$ to obtain $v_0$.

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
| 规划阶段总时间 (Planner) | 5.963 | 100% |
| 规划过程中启动的任务数 | 9 / 10 | 90.0% |
| 规划与执行重叠的任务数 | 9 / 10 | 90.0% |
| 第一个任务规划完成时间 | 1.062 | - |
| 最后一个任务规划完成时间 | 5.921 | - |
| 最后一个任务执行完成时间 | 7.591 | - |
| 任务总执行时间(累计) | 9.011 | - |
| 流水线加速比 | 3.10x | - |
| 并行效率 | 118.7% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 10 | 9.011 | - |
| 规划模型 | 1 | 14.545 | - |
| 顺序总时间 | - | 23.556 | - |
| 并行总时间 | - | 7.591 | 3.10x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the mathematical expression for the rotation matrix around the x-axis by angle α? | 大模型 | 1.062 | 1.935 | 0.873 | 2 |
| 2 | What is the mathematical expression for the rotation matrix around the y-axis by angle β? | 大模型 | 1.581 | 2.455 | 0.873 | 3 |
| 3 | What is the mathematical expression for the rotation matrix around the z-axis by angle γ? | 大模型 | 2.101 | 2.975 | 0.873 | 4 |
| 4 | In what order should the inverse rotation matrices be applied to v to obtain v₀? | 大模型 | 2.975 | 3.917 | 0.943 | 5 |
| 5 | How do we express the inverse of each individual rotation matrix? | 大模型 | 3.154 | 4.063 | 0.908 | 6 |
| 6 | What is the mathematical expression for the inverse rotation matrix around the z-axis by angle γ? | 大模型 | 4.063 | 4.936 | 0.873 | 7 |
| 7 | What is the mathematical expression for the inverse rotation matrix around the y-axis by angle β? | 大模型 | 4.250 | 5.123 | 0.873 | 8 |
| 8 | What is the mathematical expression for the inverse rotation matrix around the x-axis by angle α? | 大模型 | 4.798 | 5.671 | 0.873 | 9 |
| 9 | How do we combine these inverse rotation matrices in the correct order to get the overall inverse rotation transformation? | 大模型 | 5.671 | 6.648 | 0.977 | 10 |
| 10 | What is the final mathematical expression for recovering v₀ from v? | 大模型 | 6.648 | 7.591 | 0.943 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            6.53s
+------------------------------------------------------------+
步骤 1 |########                                                    | 1.06s - 1.94s
步骤 2 |    ########                                                | 1.58s - 2.45s
步骤 3 |         ########                                           | 2.10s - 2.97s
步骤 4 |                 #########                                  | 2.97s - 3.92s
步骤 5 |                   ########                                 | 3.15s - 4.06s
步骤 6 |                           ########                         | 4.06s - 4.94s
步骤 7 |                             ########                       | 4.25s - 5.12s
步骤 8 |                                  ########                  | 4.80s - 5.67s
步骤 9 |                                          #########         | 5.67s - 6.65s
步骤 10 |                                                   #########| 6.65s - 7.59s
```

