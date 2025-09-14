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
| 小模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 大模型 (Qwen/Qwen2.5-3B-Instruct) | 0.690 | 64.53 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 4.320 | 100% |
| 规划过程中启动的任务数 | 5 / 7 | 71.4% |
| 规划与执行重叠的任务数 | 5 / 7 | 71.4% |
| 第一个任务规划完成时间 | 1.062 | - |
| 最后一个任务规划完成时间 | 4.278 | - |
| 最后一个任务执行完成时间 | 7.563 | - |
| 任务总执行时间(累计) | 10.099 | - |
| 流水线加速比 | 2.70x | - |
| 并行效率 | 133.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 7 | 10.099 | - |
| 规划模型 | 1 | 10.331 | - |
| 顺序总时间 | - | 20.430 | - |
| 并行总时间 | - | 7.563 | 2.70x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the density matrix rho for the non-Gaussian Schrödinger cat state? | 大模型 | 1.062 | 2.527 | 1.465 | 2 |
| 2 | What is the density matrix tau for the reference Gaussian state? | 大模型 | 1.511 | 2.976 | 1.465 | 3 |
| 3 | What is the value of N at phi =-pi /4 and alpha= 0.5? | 大模型 | 2.073 | 3.228 | 1.155 | 4 |
| 4 | What is the trace of rho*ln(rho) for the non-Gaussian state? | 大模型 | 2.635 | 4.255 | 1.620 | 5 |
| 5 | What is the trace of tau*ln(tau) for the reference Gaussian state? | 大模型 | 3.169 | 4.788 | 1.620 | 6 |
| 6 | What is the relative entropy del_b for the non-Gaussian state? | 大模型 | 4.788 | 6.253 | 1.465 | 7 |
| 7 | What is the value of nG for phi =-pi /4 and alpha= 0.5? | 大模型 | 6.253 | 7.563 | 1.310 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            6.50s
+------------------------------------------------------------+
步骤 1 |#############                                               | 1.06s - 2.53s
步骤 2 |    #############                                           | 1.51s - 2.98s
步骤 3 |         ##########                                         | 2.07s - 3.23s
步骤 4 |              ###############                               | 2.63s - 4.25s
步骤 5 |                   ###############                          | 3.17s - 4.79s
步骤 6 |                                  #############             | 4.79s - 6.25s
步骤 7 |                                               #############| 6.25s - 7.56s
```

