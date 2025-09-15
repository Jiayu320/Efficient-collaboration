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
| 规划阶段总时间 (Planner) | 4.376 | 100% |
| 规划过程中启动的任务数 | 6 / 7 | 85.7% |
| 规划与执行重叠的任务数 | 6 / 7 | 85.7% |
| 第一个任务规划完成时间 | 1.062 | - |
| 最后一个任务规划完成时间 | 4.334 | - |
| 最后一个任务执行完成时间 | 6.138 | - |
| 任务总执行时间(累计) | 6.994 | - |
| 流水线加速比 | 2.82x | - |
| 并行效率 | 114.0% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 3 | 3.155 | - |
| 大模型任务 | 4 | 3.840 | - |
| 规划模型 | 1 | 10.331 | - |
| 顺序总时间 | - | 17.326 | - |
| 并行总时间 | - | 6.138 | 2.82x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the definition of pseudo-Goldstone boson H₂ in this model? | 小模型 | 1.062 | 2.062 | 1.000 | 2 |
| 2 | How does the vacuum expectation value ⟨φ⟩ = x affect the symmetry breaking in this model? | 小模型 | 2.062 | 3.139 | 1.077 | 3 |
| 3 | What is the effective potential V(φ, S, H) after considering the vacuum expectation values? | 大模型 | 3.139 | 4.082 | 0.943 | 4 |
| 4 | How do radiative corrections modify the mass generating functional in this model? | 大模型 | 2.663 | 3.640 | 0.977 | 5 |
| 5 | What is the leading order mass term for H₂ in the Lagrangian? | 小模型 | 3.140 | 4.218 | 1.077 | 6 |
| 6 | How do the parameters y_i and g_iα influence the radiative corrections to H₂'s mass? | 大模型 | 4.218 | 5.160 | 0.943 | 7 |
| 7 | What is the approximation for the mass of H₂ when the vacuum expectation values are non-zero? | 大模型 | 5.160 | 6.138 | 0.977 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            5.08s
+------------------------------------------------------------+
步骤 1 |###########                                                 | 1.06s - 2.06s
步骤 2 |           #############                                    | 2.06s - 3.14s
步骤 4 |                  ############                              | 2.66s - 3.64s
步骤 3 |                        ###########                         | 3.14s - 4.08s
步骤 5 |                        #############                       | 3.14s - 4.22s
步骤 6 |                                     ###########            | 4.22s - 5.16s
步骤 7 |                                                ############| 5.16s - 6.14s
```

