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
| 规划阶段总时间 (Planner) | 3.096 | 100% |
| 规划过程中启动的任务数 | 4 / 7 | 57.1% |
| 规划与执行重叠的任务数 | 4 / 7 | 57.1% |
| 第一个任务规划完成时间 | 1.038 | - |
| 最后一个任务规划完成时间 | 3.080 | - |
| 最后一个任务执行完成时间 | 7.135 | - |
| 任务总执行时间(累计) | 8.052 | - |
| 流水线加速比 | 2.53x | - |
| 并行效率 | 112.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 0.943 | - |
| 大模型任务 | 6 | 7.109 | - |
| 规划模型 | 1 | 9.984 | - |
| 顺序总时间 | - | 18.035 | - |
| 并行总时间 | - | 7.135 | 2.53x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the explicit form of the scalar potential $ V(\phi, S, H) $ that defines the mass $ m_H $ of the pseudo-Goldstone boson $ H_2 $? | 大模型 | 1.038 | 2.326 | 1.289 | 2 |
| 2 | From $ V(\phi, S, H) $ in Step 1, what is the quartic coupling constant $ \lambda $ that governs the Higgs self-interaction? | 大模型 | 2.326 | 3.546 | 1.219 | 3 |
| 3 | What is the mass of the $ W $-boson $ m_W $ in the Standard Model? | 小模型 | 1.559 | 2.502 | 0.943 | 4 |
| 4 | What is the formula for the mass $ m_{H_2} $ of the pseudo-Goldstone boson in terms of $ m_H $ and $ m_W $ before radiative corrections? | 大模型 | 2.502 | 3.514 | 1.012 | 5 |
| 5 | Using $ \lambda $ from Step 2 and $ m_H $ from Step 1, what is the radiative correction $ \delta m_H^2 \approx -\frac{\lambda m_H^2}{8\pi^2} $ to the Higgs mass? | 大模型 | 3.546 | 4.834 | 1.289 | 6 |
| 6 | What is the corrected Higgs mass $ m_H' = m_H + \delta m_H $ after applying the radiative correction from Step 5? | 大模型 | 4.834 | 5.985 | 1.150 | 7 |
| 7 | Using the corrected Higgs mass $ m_H' $ from Step 6 and the $ W $-boson mass $ m_W $ from Step 3, what is the final approximation $ m_{H_2} \approx \frac{(m_H')^2}{2m_W} $ for the pseudo-Goldstone boson mass? | 大模型 | 5.985 | 7.135 | 1.150 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            6.10s
+------------------------------------------------------------+
步骤 1 |############                                                | 1.04s - 2.33s
步骤 3 |     #########                                              | 1.56s - 2.50s
步骤 2 |            ############                                    | 2.33s - 3.55s
步骤 4 |              ##########                                    | 2.50s - 3.51s
步骤 5 |                        #############                       | 3.55s - 4.83s
步骤 6 |                                     ###########            | 4.83s - 5.98s
步骤 7 |                                                ############| 5.98s - 7.13s
```

