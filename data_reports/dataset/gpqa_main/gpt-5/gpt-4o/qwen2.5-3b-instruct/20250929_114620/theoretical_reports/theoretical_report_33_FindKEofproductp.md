# 问题 33 的理论性能分析报告

## 问题描述

Find KE of product particles in,
Pi(+) = mu(+) + nu
here Pi(+) is stationary.
Rest mass of Pi(+) &  mu(+) is 139.6 MeV & 105.7 MeV respectively.

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (gpt-5) | 6.407 | 50.57 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 13.169 | 100% |
| 规划过程中启动的任务数 | 4 / 4 | 100.0% |
| 规划与执行重叠的任务数 | 3 / 4 | 75.0% |
| 第一个任务规划完成时间 | 7.870 | - |
| 最后一个任务规划完成时间 | 13.110 | - |
| 最后一个任务执行完成时间 | 14.675 | - |
| 任务总执行时间(累计) | 6.039 | - |
| 流水线加速比 | 1.91x | - |
| 并行效率 | 41.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.620 | - |
| 大模型任务 | 3 | 4.420 | - |
| 规划模型 | 1 | 22.008 | - |
| 顺序总时间 | - | 28.047 | - |
| 并行总时间 | - | 14.675 | 1.91x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For a two-body decay of a stationary parent particle (mass M) into two daughters (masses m1 and m2), what are the energy–momentum conservation equations, and what constraints do they impose on the daughters’ energies and momenta? | 大模型 | 7.870 | 9.159 | 1.289 | 2 |
| 2 | Using the relations from Step 1 and the invariant mass method, what are the general symbolic expressions for the daughters’ total energies E1 and E2 and their common momentum magnitude p in terms of M, m1, and m2 (with c = 1)? | 大模型 | 9.373 | 10.938 | 1.565 | 3 |
| 3 | For the specific decay π+ → μ+ + ν with the parent at rest, what numerical values should be used for M and m1 (π+ and μ+ masses are given), what value or assumption should be adopted for the neutrino mass m2 (e.g., treat as approximately 0), and what unit convention (e.g., c = 1) will be used? | 小模型 | 11.330 | 12.950 | 1.620 | 4 |
| 4 | Applying the formulas from Step 2 with the values and assumption from Step 3, what are the numerical total energies Eμ and Eν, and the kinetic energies Kμ = Eμ − mμ and Kν = Eν − mν? Do the results satisfy energy conservation (Eμ + Eν = M)? | 大模型 | 13.110 | 14.675 | 1.565 | 5 |

## 理论执行甘特图

```
时间轴:
0                                                            6.81s
+------------------------------------------------------------+
步骤 1 |###########                                                 | 7.87s - 9.16s
步骤 2 |             ##############                                 | 9.37s - 10.94s
步骤 3 |                              ##############                | 11.33s - 12.95s
步骤 4 |                                              ##############| 13.11s - 14.68s
```

