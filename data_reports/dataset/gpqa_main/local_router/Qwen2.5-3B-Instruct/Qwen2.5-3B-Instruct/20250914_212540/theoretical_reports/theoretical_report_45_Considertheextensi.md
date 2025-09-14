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
| 规划阶段总时间 (Planner) | 5.079 | 100% |
| 规划过程中启动的任务数 | 6 / 9 | 66.7% |
| 规划与执行重叠的任务数 | 6 / 9 | 66.7% |
| 第一个任务规划完成时间 | 1.062 | - |
| 最后一个任务规划完成时间 | 5.037 | - |
| 最后一个任务执行完成时间 | 9.861 | - |
| 任务总执行时间(累计) | 12.719 | - |
| 流水线加速比 | 2.62x | - |
| 并行效率 | 129.0% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 9 | 12.719 | - |
| 规划模型 | 1 | 13.140 | - |
| 顺序总时间 | - | 25.859 | - |
| 并行总时间 | - | 9.861 | 2.62x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the definition of pseudo-Goldstone boson H2 in this model? | 大模型 | 1.062 | 2.217 | 1.155 | 2 |
| 2 | How does the vacuum expectation value of φ affect the symmetry breaking pattern? | 大模型 | 1.539 | 2.849 | 1.310 | 3 |
| 3 | What is the effective potential for the Higgs fields in this model? | 大模型 | 2.849 | 4.314 | 1.465 | 4 |
| 4 | What are the relevant Feynman diagrams for radiative corrections to H2 mass? | 大模型 | 2.537 | 3.924 | 1.387 | 5 |
| 5 | How do we compute the tree-level mass of H2 from the effective potential? | 大模型 | 4.314 | 5.779 | 1.465 | 6 |
| 6 | What is the leading-order correction to the H2 mass from loop diagrams? | 大模型 | 3.924 | 5.544 | 1.620 | 7 |
| 7 | How do we evaluate the loop correction to the H2 mass? | 大模型 | 5.544 | 7.318 | 1.775 | 8 |
| 8 | What is the total mass of H2 including both tree and radiative corrections? | 大模型 | 7.318 | 8.628 | 1.310 | 9 |
| 9 | What is the approximation of H2 mass through radiative corrections? | 大模型 | 8.628 | 9.861 | 1.232 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            8.80s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 1.06s - 2.22s
步骤 2 |   #########                                                | 1.54s - 2.85s
步骤 4 |          #########                                         | 2.54s - 3.92s
步骤 3 |            ##########                                      | 2.85s - 4.31s
步骤 6 |                   ###########                              | 3.92s - 5.54s
步骤 5 |                      ##########                            | 4.31s - 5.78s
步骤 7 |                              ############                  | 5.54s - 7.32s
步骤 8 |                                          #########         | 7.32s - 8.63s
步骤 9 |                                                   ######## | 8.63s - 9.86s
```

