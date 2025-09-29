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
| 规划阶段总时间 (Planner) | 2.265 | 100% |
| 规划过程中启动的任务数 | 2 / 4 | 50.0% |
| 规划与执行重叠的任务数 | 2 / 4 | 50.0% |
| 第一个任务规划完成时间 | 1.119 | - |
| 最后一个任务规划完成时间 | 2.249 | - |
| 最后一个任务执行完成时间 | 5.815 | - |
| 任务总执行时间(累计) | 5.591 | - |
| 流水线加速比 | 2.09x | - |
| 并行效率 | 96.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.310 | - |
| 大模型任务 | 3 | 4.281 | - |
| 规划模型 | 1 | 6.540 | - |
| 顺序总时间 | - | 12.131 | - |
| 并行总时间 | - | 5.815 | 2.09x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the tree-level mass squared $m_H^2$ given by $-\frac{1}{2} y_i^2 \left(2m_{N_{iR}}^2 + m_S^2\right)$ for the scalar doublet $S$? | 大模型 | 1.119 | 2.546 | 1.427 | 2 |
| 2 | For each $i$, what is the contribution to $\delta m_H^2$ from $\frac{1}{4} g_{i\alpha}^2 m_{N_{iR}}^2 \left(1 - \frac{2m_{N_{iR}}^2}{2m_{N_{iR}}^2 + m_S^2}\right)$? | 大模型 | 1.651 | 3.217 | 1.565 | 3 |
| 3 | Summing $m_H^2$ from Step 1 and $\delta m_H^2$ from Step 2, what is the total mass squared $m_{H_2}^2$? | 大模型 | 3.217 | 4.506 | 1.289 | 4 |
| 4 | What is the approximation for $m_{H_2}$ given by $\sqrt{m_{H_2}^2}$? | 小模型 | 4.506 | 5.815 | 1.310 | 5 |

## 理论执行甘特图

```
时间轴:
0                                                            4.70s
+------------------------------------------------------------+
步骤 1 |##################                                          | 1.12s - 2.55s
步骤 2 |      ####################                                  | 1.65s - 3.22s
步骤 3 |                          #################                 | 3.22s - 4.51s
步骤 4 |                                           #################| 4.51s - 5.82s
```

