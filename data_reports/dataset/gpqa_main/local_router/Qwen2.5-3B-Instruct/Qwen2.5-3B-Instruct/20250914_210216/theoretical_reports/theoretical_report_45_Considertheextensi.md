# 问题 45 的理论性能分析报告

## 问题描述

Consider the extension of the Standard Model given by the following Lagrangian

\mathcal{L}\subset i\bar{N}_{R}\gamma^{\mu}\partial_{\mu}N_{R}+\frac{1}{2}\left(\partial^{\mu}\phi\right)^{2}+\left|D^{\mu}S\right|^{2}-\frac{y_{i}}{2}\phi\bar{N}_{iR}^{c}N_{iR}^{c}-g_{i\alpha}\bar{N}_{iR}L_{\alpha}S-V\left(\phi,S,H\right)
with singlet fermions,$N{iR}\sim\left(1,1,0\right)$, scalar-doublet $S\sim\left(1,2,1\right)$, and singlet scalar $\phi\sim\left(1,1,0\right)$. We give $\left\langle \phi\right\rangle ^{2}=\left(x^{2}+\upsilon^{2}\right)$, where $\left\langle \phi\right\rangle =x$ and $\left\langle h\right\rangle =v$.

What is the approximation of the mass of the pseudo-Goldostone boson $H_{2}$ through radiative corrections? 

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
| 规划阶段总时间 (Planner) | 4.615 | 100% |
| 规划过程中启动的任务数 | 5 / 8 | 62.5% |
| 规划与执行重叠的任务数 | 5 / 8 | 62.5% |
| 第一个任务规划完成时间 | 1.062 | - |
| 最后一个任务规划完成时间 | 4.573 | - |
| 最后一个任务执行完成时间 | 8.698 | - |
| 任务总执行时间(累计) | 9.859 | - |
| 流水线加速比 | 2.48x | - |
| 并行效率 | 113.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 8 | 9.859 | - |
| 规划模型 | 1 | 11.736 | - |
| 顺序总时间 | - | 21.595 | - |
| 并行总时间 | - | 8.698 | 2.48x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the definition of pseudo-Goldstone boson H2 in this model? | 大模型 | 1.062 | 2.217 | 1.155 | 2 |
| 2 | What is the effective potential V(φ,S,H) in the broken symmetry phase? | 大模型 | 1.581 | 2.891 | 1.310 | 3 |
| 3 | What are the relevant Feynman diagrams for radiative corrections to H2 mass? | 大模型 | 2.217 | 3.449 | 1.232 | 4 |
| 4 | How do we calculate the vacuum expectation value of φ? | 大模型 | 2.537 | 3.614 | 1.077 | 5 |
| 5 | What is the contribution from the φ-φ coupling to the effective potential? | 大模型 | 3.614 | 4.924 | 1.310 | 6 |
| 6 | How do we compute the mass of H2 using the corrected potential? | 大模型 | 4.924 | 6.311 | 1.387 | 7 |
| 7 | What is the leading radiative correction to H2 mass? | 大模型 | 6.311 | 7.544 | 1.232 | 8 |
| 8 | What is the approximation for H2 mass including all radiative corrections? | 大模型 | 7.544 | 8.698 | 1.155 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            7.64s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 1.06s - 2.22s
步骤 2 |    ##########                                              | 1.58s - 2.89s
步骤 3 |         #########                                          | 2.22s - 3.45s
步骤 4 |           #########                                        | 2.54s - 3.61s
步骤 5 |                    ##########                              | 3.61s - 4.92s
步骤 6 |                              ###########                   | 4.92s - 6.31s
步骤 7 |                                         #########          | 6.31s - 7.54s
步骤 8 |                                                  ##########| 7.54s - 8.70s
```

