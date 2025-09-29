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
| 规划阶段总时间 (Planner) | 1.793 | 100% |
| 规划过程中启动的任务数 | 2 / 3 | 66.7% |
| 规划与执行重叠的任务数 | 2 / 3 | 66.7% |
| 第一个任务规划完成时间 | 1.059 | - |
| 最后一个任务规划完成时间 | 1.776 | - |
| 最后一个任务执行完成时间 | 3.664 | - |
| 任务总执行时间(累计) | 3.520 | - |
| 流水线加速比 | 2.64x | - |
| 并行效率 | 96.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 3 | 3.520 | - |
| 规划模型 | 1 | 6.154 | - |
| 顺序总时间 | - | 9.674 | - |
| 并行总时间 | - | 3.664 | 2.64x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the formula for the tree-level mass squared of the pseudo-Goldstone boson $H_2$ in terms of the scalar vacuum expectation value $\langle \phi \rangle$ and couplings $y_i$? | 大模型 | 1.059 | 2.279 | 1.219 | 2 |
| 2 | What is the formula for the effective coupling constant squared $g_{\text{eff}}^2$ in terms of the couplings $g_i$ and $g_{\alpha}$? | 大模型 | 1.364 | 2.514 | 1.150 | 3 |
| 3 | Using the formula from Step 1 for the tree-level mass squared and the formula from Step 2 for $g_{\text{eff}}^2$, what is the approximation for the radiatively corrected mass squared $m_{H_2}^2$? | 大模型 | 2.514 | 3.664 | 1.150 | 4 |

## 理论执行甘特图

```
时间轴:
0                                                            2.60s
+------------------------------------------------------------+
步骤 1 |############################                                | 1.06s - 2.28s
步骤 2 |       ##########################                           | 1.36s - 2.51s
步骤 3 |                                 ###########################| 2.51s - 3.66s
```

