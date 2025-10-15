# 问题 20 的理论性能分析报告

## 问题描述

Let $\omega\neq 1$ be a 13th root of unity. Find the remainder when
\[\prod_{k=0}^{12}(2-2\omega^k+\omega^{2k})\]
is divided by 1000.

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (meta-llama/llama-3-8b-instruct) | 0.645 | 86.95 |
| 大模型 (meta-llama/llama-3-8b-instruct) | 0.645 | 86.95 |
| 路由模型 (gpt-4.1-mini) | 0.700 | 69.59 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 7.181 | 100% |
| 规划过程中启动的任务数 | 3 / 4 | 75.0% |
| 规划与执行重叠的任务数 | 3 / 4 | 75.0% |
| 第一个任务规划完成时间 | 2.252 | - |
| 最后一个任务规划完成时间 | 7.138 | - |
| 最后一个任务执行完成时间 | 8.974 | - |
| 任务总执行时间(累计) | 4.995 | - |
| 流水线加速比 | 1.44x | - |
| 并行效率 | 55.7% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 1.980 | - |
| 大模型任务 | 2 | 3.015 | - |
| 规划模型 | 1 | 7.914 | - |
| 顺序总时间 | - | 12.909 | - |
| 并行总时间 | - | 8.974 | 1.44x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Express the product as \(\prod_{k=0}^{12} (2 - 2\omega^k + \omega^{2k})\) and rewrite each factor using the substitution \(x = \omega^k\), so each factor is \(2 - 2x + x^2\). What polynomial \(P(x)\) satisfies \(P(\omega^k) = 2 - 2\omega^k + \omega^{2k}\)? | 小模型 | 2.252 | 3.357 | 1.105 | 2 |
| 2 | Recognize that the product over \(k=0\) to \(12\) of \(P(\omega^k)\) is the product of the values of \(P(x)\) evaluated at the 13th roots of unity \(\omega^k\). Use the formula \(\prod_{k=0}^{n-1} P(\omega^k) = \frac{\text{Res}(\Phi_n(x), P(x))}{a^{n}}\), or equivalently the formula \(\prod_{\omega^k \text{ root of } x^n-1} P(\omega^k) = \prod_{P(\zeta) = 0} \zeta^n - 1\), to express the product in terms of resultant or values of cyclotomic polynomials? (Difficulty=6) | 大模型 | 4.724 | 6.174 | 1.450 | 3 |
| 3 | Calculate the value \(Q = \prod_{k=0}^{12} P(\omega^k)\) by recognizing it as the value at 1 of the polynomial \(R(x) = \prod_{P(\zeta) = 0} (x - \zeta^{13})\), or alternatively find the polynomial with roots \(\omega^k\) for \(k=0,\ldots,12\) and evaluate the product of \(P(\omega^k)\) as \(N\). What is the explicit numeric value of this product \(N\)? | 大模型 | 6.534 | 8.099 | 1.565 | 4 |
| 4 | Find \(N \mod 1000\), the remainder when the product is divided by 1000. | 小模型 | 8.099 | 8.974 | 0.875 | 5 |

## 理论执行甘特图

```
时间轴:
0                                                            6.72s
+------------------------------------------------------------+
步骤 1 |#########                                                   | 2.25s - 3.36s
步骤 2 |                      #############                         | 4.72s - 6.17s
步骤 3 |                                      ##############        | 6.53s - 8.10s
步骤 4 |                                                    ########| 8.10s - 8.97s
```

