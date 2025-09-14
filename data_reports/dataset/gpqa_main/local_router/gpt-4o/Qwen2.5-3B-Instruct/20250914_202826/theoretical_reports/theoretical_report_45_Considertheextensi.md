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
| 规划阶段总时间 (Planner) | 5.149 | 100% |
| 规划过程中启动的任务数 | 8 / 9 | 88.9% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 1.076 | - |
| 最后一个任务规划完成时间 | 5.107 | - |
| 最后一个任务执行完成时间 | 6.730 | - |
| 任务总执行时间(累计) | 9.106 | - |
| 流水线加速比 | 3.31x | - |
| 并行效率 | 135.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 9 | 9.106 | - |
| 规划模型 | 1 | 13.140 | - |
| 顺序总时间 | - | 22.247 | - |
| 并行总时间 | - | 6.730 | 3.31x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the definition of the pseudo-Goldstone boson H₂ in this model? | 大模型 | 1.076 | 2.018 | 0.943 | 2 |
| 2 | How does the vacuum expectation value ⟨φ⟩ = x affect the Lagrangian? | 大模型 | 1.567 | 2.579 | 1.012 | 3 |
| 3 | What is the effective potential V(φ, S, H) after considering vacuum expectation values? | 大模型 | 2.579 | 3.660 | 1.081 | 4 |
| 4 | How does the Higgs mechanism generate masses in this model? | 大模型 | 2.565 | 3.542 | 0.977 | 5 |
| 5 | What is the mass of the Higgs boson H₁ before radiative corrections? | 大模型 | 3.056 | 4.068 | 1.012 | 6 |
| 6 | How do radiative corrections modify the mass of the Higgs boson? | 大模型 | 3.660 | 4.707 | 1.046 | 7 |
| 7 | What is the relationship between the masses of H₁ and H₂ through symmetry breaking? | 大模型 | 4.096 | 5.107 | 1.012 | 8 |
| 8 | What is the leading-order mass of H₂? | 大模型 | 4.707 | 5.684 | 0.977 | 9 |
| 9 | What is the approximation for the radiative correction to H₂'s mass? | 大模型 | 5.684 | 6.730 | 1.046 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            5.65s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 1.08s - 2.02s
步骤 2 |     ##########                                             | 1.57s - 2.58s
步骤 4 |               ###########                                  | 2.56s - 3.54s
步骤 3 |               ############                                 | 2.58s - 3.66s
步骤 5 |                     ##########                             | 3.06s - 4.07s
步骤 6 |                           ###########                      | 3.66s - 4.71s
步骤 7 |                                ##########                  | 4.10s - 5.11s
步骤 8 |                                      ##########            | 4.71s - 5.68s
步骤 9 |                                                ############| 5.68s - 6.73s
```

