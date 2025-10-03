# 问题 55 的理论性能分析报告

## 问题描述

Calculate the amount of non-Gaussianity(nG) in the Schrödinger cat state using relative entropy measure. The state is defined as,
|psi> =( cos(phi)|alpha> + sin(phi)|-alpha> )/ N;
Here, alpha is the amplitude, phi is the phase and N is the normalisation constant.
N = sqrt(1+ sin(2*phi)*exp(-2*alpha^2)).
The relative entropy measure is given as,
del_b = [trace(rho* ln(rho))-trace(tau* ln(tau))]
where tau is the density matrix of a reference Gaussian state and rho is the density matrix of the above non-Gaussian state.
Calculate the nG for phi =-pi /4 and alpha= 0.5.

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (gpt-4o) | 0.735 | 144.50 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (gpt-4o) | 0.735 | 144.50 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 2.735 | 100% |
| 规划过程中启动的任务数 | 1 / 7 | 14.3% |
| 规划与执行重叠的任务数 | 1 / 7 | 14.3% |
| 第一个任务规划完成时间 | 0.977 | - |
| 最后一个任务规划完成时间 | 2.714 | - |
| 最后一个任务执行完成时间 | 54.565 | - |
| 任务总执行时间(累计) | 53.588 | - |
| 流水线加速比 | 1.04x | - |
| 并行效率 | 98.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 7 | 53.588 | - |
| 规划模型 | 1 | 3.240 | - |
| 顺序总时间 | - | 56.828 | - |
| 并行总时间 | - | 54.565 | 1.04x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Compute the normalization constant N for the given phi and alpha | 大模型 | 0.977 | 8.633 | 7.655 | 2 |
| 2 | Determine the density matrix rho of the non-Gaussian state using the computed N, phi, and alpha | 大模型 | 8.633 | 16.288 | 7.655 | 3 |
| 3 | Identify the density matrix tau of a reference Gaussian state | 大模型 | 16.288 | 23.943 | 7.655 | 4 |
| 4 | Calculate the trace of rho*ln(rho) | 大模型 | 23.943 | 31.599 | 7.655 | 5 |
| 5 | Calculate the trace of tau*ln(tau) | 大模型 | 31.599 | 39.254 | 7.655 | 6 |
| 6 | Subtract the result from Step 5 from Step 4 to find the relative entropy measure del_b | 大模型 | 39.254 | 46.910 | 7.655 | 7 |
| 7 | Calculate the amount of non-Gaussianity (nG) from the result in Step 6 | 大模型 | 46.910 | 54.565 | 7.655 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            53.59s
+------------------------------------------------------------+
步骤 1 |########                                                    | 0.98s - 8.63s
步骤 2 |        #########                                           | 8.63s - 16.29s
步骤 3 |                 ########                                   | 16.29s - 23.94s
步骤 4 |                         #########                          | 23.94s - 31.60s
步骤 5 |                                  ########                  | 31.60s - 39.25s
步骤 6 |                                          #########         | 39.25s - 46.91s
步骤 7 |                                                   #########| 46.91s - 54.57s
```

