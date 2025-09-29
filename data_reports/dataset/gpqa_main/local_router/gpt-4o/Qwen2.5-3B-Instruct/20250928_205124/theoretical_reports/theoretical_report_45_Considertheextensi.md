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
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (saves/Qwen3-4B-Thinking/full/ep5) | 0.690 | 184.10 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 1.961 | 100% |
| 规划过程中启动的任务数 | 2 / 4 | 50.0% |
| 规划与执行重叠的任务数 | 2 / 4 | 50.0% |
| 第一个任务规划完成时间 | 1.038 | - |
| 最后一个任务规划完成时间 | 1.945 | - |
| 最后一个任务执行完成时间 | 4.573 | - |
| 任务总执行时间(累计) | 4.451 | - |
| 流水线加速比 | 2.38x | - |
| 并行效率 | 97.3% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.000 | - |
| 大模型任务 | 3 | 3.451 | - |
| 规划模型 | 1 | 6.453 | - |
| 顺序总时间 | - | 10.904 | - |
| 并行总时间 | - | 4.573 | 2.38x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the self-coupling constant λ of the scalar doublet S, determined from the quadratic term in V(ϕ,S,H) as λ(S†S − x² − υ²)²? | 大模型 | 1.038 | 2.257 | 1.219 | 2 |
| 2 | Given ⟨ϕ⟩² = x² + υ² with ⟨ϕ⟩ = x and ⟨h⟩ = υ, what is the explicit value of x in terms of υ? | 小模型 | 1.342 | 2.342 | 1.000 | 3 |
| 3 | Using the Goldstone equivalence theorem, what is the tree-level mass formula for the pseudo-Goldstone boson H₂ as 2λx²? | 大模型 | 2.342 | 3.492 | 1.150 | 4 |
| 4 | Since x ≪ υ, radiative corrections to H₂'s mass are negligible. Using the formula from Step 3, what is the final approximation for m_{H₂}? | 大模型 | 3.492 | 4.573 | 1.081 | 5 |

## 理论执行甘特图

```
时间轴:
0                                                            3.54s
+------------------------------------------------------------+
步骤 1 |####################                                        | 1.04s - 2.26s
步骤 2 |     #################                                      | 1.34s - 2.34s
步骤 3 |                      ###################                   | 2.34s - 3.49s
步骤 4 |                                         ###################| 3.49s - 4.57s
```

