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
| 路由模型 (saves/Qwen3-4B-Thinking/full/ep5) | 0.690 | 184.10 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 1.983 | 100% |
| 规划过程中启动的任务数 | 2 / 5 | 40.0% |
| 规划与执行重叠的任务数 | 2 / 5 | 40.0% |
| 第一个任务规划完成时间 | 0.934 | - |
| 最后一个任务规划完成时间 | 1.966 | - |
| 最后一个任务执行完成时间 | 5.541 | - |
| 任务总执行时间(累计) | 5.544 | - |
| 流水线加速比 | 2.42x | - |
| 并行效率 | 100.0% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 0.943 | - |
| 大模型任务 | 4 | 4.601 | - |
| 规划模型 | 1 | 7.876 | - |
| 顺序总时间 | - | 13.420 | - |
| 并行总时间 | - | 5.541 | 2.42x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the symmetry group broken by the scalar fields to produce the pseudo-Goldstone boson H2? | 大模型 | 0.934 | 2.154 | 1.219 | 2 |
| 2 | What are the vacuum expectation values ⟨φ⟩ and ⟨H⟩ given by ⟨φ⟩² = x² + υ² and ⟨H⟩ = υ? | 小模型 | 1.217 | 2.160 | 0.943 | 3 |
| 3 | What is the effective potential V_eff for H after eliminating φ and S using their VEVs? | 大模型 | 2.160 | 3.310 | 1.150 | 4 |
| 4 | What is the second derivative of V_eff with respect to H evaluated at the minimum, contributing to the radiative correction? | 大模型 | 3.310 | 4.460 | 1.150 | 5 |
| 5 | Combining the tree-level mass squared m_H² and the radiative correction from Step 4, what is the approximation for the mass of H2? | 大模型 | 4.460 | 5.541 | 1.081 | 6 |

## 理论执行甘特图

```
时间轴:
0                                                            4.61s
+------------------------------------------------------------+
步骤 1 |###############                                             | 0.93s - 2.15s
步骤 2 |   ############                                             | 1.22s - 2.16s
步骤 3 |               ###############                              | 2.16s - 3.31s
步骤 4 |                              ###############               | 3.31s - 4.46s
步骤 5 |                                             ###############| 4.46s - 5.54s
```

