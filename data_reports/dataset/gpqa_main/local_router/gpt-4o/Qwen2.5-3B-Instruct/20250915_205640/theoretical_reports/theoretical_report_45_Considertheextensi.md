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
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-1.7B-Instruct/full/sft) | 0.500 | 71.20 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 5.303 | 100% |
| 规划过程中启动的任务数 | 6 / 9 | 66.7% |
| 规划与执行重叠的任务数 | 6 / 9 | 66.7% |
| 第一个任务规划完成时间 | 1.062 | - |
| 最后一个任务规划完成时间 | 5.261 | - |
| 最后一个任务执行完成时间 | 8.714 | - |
| 任务总执行时间(累计) | 9.452 | - |
| 流水线加速比 | 2.59x | - |
| 并行效率 | 108.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 9 | 9.452 | - |
| 规划模型 | 1 | 13.140 | - |
| 顺序总时间 | - | 22.593 | - |
| 并行总时间 | - | 8.714 | 2.59x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the definition of pseudo-Goldstone boson H₂ in this context? | 大模型 | 1.062 | 2.004 | 0.943 | 2 |
| 2 | How does the ⟨φ⟩² = (x² + υ²) term affect the symmetry breaking of the Standard Model? | 大模型 | 2.004 | 3.016 | 1.012 | 3 |
| 3 | What are the relevant Feynman diagrams for radiative corrections to H₂ mass? | 大模型 | 2.228 | 3.309 | 1.081 | 4 |
| 4 | How does the interaction term with φ influence the H₂ mass through loop diagrams? | 大模型 | 3.309 | 4.459 | 1.150 | 5 |
| 5 | What is the effective potential for H₂ in the broken symmetry phase? | 大模型 | 4.459 | 5.540 | 1.081 | 6 |
| 6 | How do we compute the mass correction from the effective potential? | 大模型 | 5.540 | 6.690 | 1.150 | 7 |
| 7 | What is the leading order radiative correction to H₂ mass? | 大模型 | 4.222 | 5.234 | 1.012 | 8 |
| 8 | How do we combine the leading order correction with the vacuum expectation value effects? | 大模型 | 6.690 | 7.771 | 1.081 | 9 |
| 9 | What is the final approximation for the mass of H₂ through radiative corrections? | 大模型 | 7.771 | 8.714 | 0.943 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            7.65s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 1.06s - 2.00s
步骤 2 |       ########                                             | 2.00s - 3.02s
步骤 3 |         ########                                           | 2.23s - 3.31s
步骤 4 |                 #########                                  | 3.31s - 4.46s
步骤 7 |                        ########                            | 4.22s - 5.23s
步骤 5 |                          #########                         | 4.46s - 5.54s
步骤 6 |                                   #########                | 5.54s - 6.69s
步骤 8 |                                            ########        | 6.69s - 7.77s
步骤 9 |                                                    ########| 7.77s - 8.71s
```

