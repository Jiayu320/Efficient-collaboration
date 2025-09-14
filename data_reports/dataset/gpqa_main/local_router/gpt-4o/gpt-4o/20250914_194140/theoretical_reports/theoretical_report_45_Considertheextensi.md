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
| 小模型 (gpt-4o) | 0.735 | 144.50 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 5.458 | 100% |
| 规划过程中启动的任务数 | 7 / 9 | 77.8% |
| 规划与执行重叠的任务数 | 7 / 9 | 77.8% |
| 第一个任务规划完成时间 | 1.076 | - |
| 最后一个任务规划完成时间 | 5.416 | - |
| 最后一个任务执行完成时间 | 7.641 | - |
| 任务总执行时间(累计) | 8.622 | - |
| 流水线加速比 | 2.85x | - |
| 并行效率 | 112.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 9 | 8.622 | - |
| 规划模型 | 1 | 13.140 | - |
| 顺序总时间 | - | 21.762 | - |
| 并行总时间 | - | 7.641 | 2.85x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the definition of the pseudo-Goldstone boson H₂ in this model? | 大模型 | 1.076 | 1.984 | 0.908 | 2 |
| 2 | How does the vacuum expectation value ⟨φ⟩² = (x² + υ²) affect the symmetry breaking in the Lagrangian? | 大模型 | 1.722 | 2.665 | 0.943 | 3 |
| 3 | What is the role of the coupling term y_iφ⟨N_iR⟩² in generating masses? | 大模型 | 2.665 | 3.642 | 0.977 | 4 |
| 4 | How do radiative corrections modify the mass generation mechanism in the Standard Model? | 大模型 | 2.789 | 3.697 | 0.908 | 5 |
| 5 | What are the relevant Feynman diagrams for calculating radiative corrections to H₂ mass? | 大模型 | 3.697 | 4.675 | 0.977 | 6 |
| 6 | How does the vacuum expectation value affect the loop diagrams for radiative corrections? | 大模型 | 4.675 | 5.686 | 1.012 | 7 |
| 7 | What is the leading-order mass of H₂ without radiative corrections? | 大模型 | 4.348 | 5.291 | 0.943 | 8 |
| 8 | What is the next-order correction to H₂ mass due to radiative effects? | 大模型 | 5.686 | 6.698 | 1.012 | 9 |
| 9 | What is the total approximation for the mass of H₂ through radiative corrections? | 大模型 | 6.698 | 7.641 | 0.943 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            6.56s
+------------------------------------------------------------+
步骤 1 |########                                                    | 1.08s - 1.98s
步骤 2 |     #########                                              | 1.72s - 2.66s
步骤 3 |              #########                                     | 2.66s - 3.64s
步骤 4 |               ########                                     | 2.79s - 3.70s
步骤 5 |                       #########                            | 3.70s - 4.67s
步骤 7 |                             #########                      | 4.35s - 5.29s
步骤 6 |                                ##########                  | 4.67s - 5.69s
步骤 8 |                                          #########         | 5.69s - 6.70s
步骤 9 |                                                   #########| 6.70s - 7.64s
```

