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
| 规划阶段总时间 (Planner) | 6.722 | 100% |
| 规划过程中启动的任务数 | 5 / 10 | 50.0% |
| 规划与执行重叠的任务数 | 5 / 10 | 50.0% |
| 第一个任务规划完成时间 | 1.146 | - |
| 最后一个任务规划完成时间 | 6.680 | - |
| 最后一个任务执行完成时间 | 13.351 | - |
| 任务总执行时间(累计) | 12.205 | - |
| 流水线加速比 | 2.00x | - |
| 并行效率 | 91.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 5 | 6.627 | - |
| 大模型任务 | 5 | 5.578 | - |
| 规划模型 | 1 | 14.545 | - |
| 顺序总时间 | - | 26.750 | - |
| 并行总时间 | - | 13.351 | 2.00x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the definition and properties of the pseudo-Goldstone boson $H_2$ in this model? | 小模型 | 1.146 | 2.611 | 1.465 | 2 |
| 2 | How does the vacuum expectation value $\langle \phi \rangle^2 = (x^2 + \upsilon^2)$ affect the symmetry breaking of the Standard Model? | 小模型 | 2.611 | 3.921 | 1.310 | 3 |
| 3 | What are the relevant Feynman diagrams for calculating radiative corrections to the mass of $H_2$? | 大模型 | 3.921 | 5.071 | 1.150 | 4 |
| 4 | How does the coupling $g_{i\alpha} \bar{N}_{iR} L_\alpha S$ contribute to the mass of $H_2$? | 大模型 | 5.071 | 6.152 | 1.081 | 5 |
| 5 | What is the role of the scalar doublet $S$ in the radiative correction process? | 小模型 | 6.152 | 7.539 | 1.387 | 6 |
| 6 | How do the vacuum expectation values and symmetry-breaking parameters influence the radiative correction terms? | 大模型 | 7.539 | 8.655 | 1.116 | 7 |
| 7 | What is the mathematical approach to evaluate the radiative correction to the mass of $H_2$? | 大模型 | 8.655 | 9.805 | 1.150 | 8 |
| 8 | How do the contributions from different Feynman diagrams combine to give the final approximation for the mass of $H_2$? | 大模型 | 9.805 | 10.886 | 1.081 | 9 |
| 9 | What simplifications or approximations are made to make the calculation feasible? | 小模型 | 10.886 | 12.041 | 1.155 | 10 |
| 10 | What is the resulting approximation for the mass of the pseudo-Goldstone boson $H_2$? | 小模型 | 12.041 | 13.351 | 1.310 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            12.20s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 1.15s - 2.61s
步骤 2 |       ######                                               | 2.61s - 3.92s
步骤 3 |             ######                                         | 3.92s - 5.07s
步骤 4 |                   #####                                    | 5.07s - 6.15s
步骤 5 |                        #######                             | 6.15s - 7.54s
步骤 6 |                               #####                        | 7.54s - 8.65s
步骤 7 |                                    ######                  | 8.65s - 9.81s
步骤 8 |                                          #####             | 9.81s - 10.89s
步骤 9 |                                               ######       | 10.89s - 12.04s
步骤 10 |                                                     #######| 12.04s - 13.35s
```

