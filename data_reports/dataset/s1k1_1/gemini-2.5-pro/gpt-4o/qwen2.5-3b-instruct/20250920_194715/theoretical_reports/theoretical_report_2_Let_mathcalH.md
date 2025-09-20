# 问题 2 的理论性能分析报告

## 问题描述

Let  $ \mathcal{H}$  be an infinite-dimensional Hilbert space, let  $ d>0$ , and suppose that  $ S$  is a set of points (not necessarily countable) in  $ \mathcal{H}$  such that the distance between any two distinct points in  $ S$  is equal to  $ d$ . Show that there is a point  $ y\in\mathcal{H}$  such that 
\[ \left\{\frac{\sqrt{2}}{d}(x\minus{}y): \ x\in S\right\}\]
is an orthonormal system of vectors in  $ \mathcal{H}$ .

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (gemini-2.5-pro) | 2.510 | 93.75 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 11.459 | 100% |
| 规划过程中启动的任务数 | 6 / 8 | 75.0% |
| 规划与执行重叠的任务数 | 6 / 8 | 75.0% |
| 第一个任务规划完成时间 | 3.481 | - |
| 最后一个任务规划完成时间 | 11.427 | - |
| 最后一个任务执行完成时间 | 14.323 | - |
| 任务总执行时间(累计) | 10.655 | - |
| 流水线加速比 | 1.51x | - |
| 并行效率 | 74.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 8 | 10.655 | - |
| 规划模型 | 1 | 11.043 | - |
| 顺序总时间 | - | 21.698 | - |
| 并行总时间 | - | 14.323 | 1.51x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Let the proposed orthonormal system be $v_x = \frac{\sqrt{2}}{d}(x-y)$. What are the two conditions on the norms and inner products of the vectors $\{x-y\}$ that are equivalent to the set $\{v_x\}_{x \in S}$ being an orthonormal system? | 大模型 | 3.481 | 4.562 | 1.081 | 2 |
| 2 | Fix an arbitrary point $x_0 \in S$. Define a new set of vectors $z_x = x - x_0$ for all $x \in S$. Using the given condition that $\|x_1 - x_2\| = d$ for distinct $x_1, x_2 \in S$, what are the values of $\|z_x\|^2$ for $x \neq x_0$ and $\langle z_{x_1}, z_{x_2} \rangle$ for distinct $x_1, x_2 \in S \setminus \{x_0\}$? | 大模型 | 5.081 | 6.369 | 1.289 | 3 |
| 3 | Let $y' = y - x_0$. Rewrite the two conditions from Step 1 in terms of $y'$ and the vectors $\{z_x\}_{x \in S}$. What specific conditions must $y'$ satisfy with respect to the set $\{z_x\}_{x \in S \setminus \{x_0\}}$ and the zero vector $z_{x_0}$? | 大模型 | 6.369 | 7.727 | 1.358 | 4 |
| 4 | Let $M_0$ be the linear span of the set of vectors $Z' = \{z_x : x \in S \setminus \{x_0\}\}$. Define a linear functional $f$ on $M_0$ by its action on the basis vectors: $f(z_x) = d^2/2$. Show that this functional is well-defined by proving that the set $Z'$ is linearly independent. | 大模型 | 7.395 | 8.961 | 1.565 | 5 |
| 5 | Prove that the linear functional $f$ defined in Step 4 is bounded on $M_0$. What is an upper bound for the norm of $f$? | 大模型 | 8.961 | 10.388 | 1.427 | 6 |
| 6 | By the Riesz Representation Theorem, the bounded linear functional $f$ from Step 5 can be extended to the closed linear span $M = \overline{M_0}$ and there exists a unique vector $y' \in M$ representing it. What equation relates $y'$, $z_x$, and $d^2/2$ for all $x \in S \setminus \{x_0\}$? | 大模型 | 10.388 | 11.676 | 1.289 | 7 |
| 7 | Using the vector $y'$ whose existence was established in Step 6, and the conditions derived in Step 3, show that the orthogonality condition $\langle z_{x_1}-y', z_{x_2}-y' \rangle = 0$ for distinct $x_1, x_2 \in S \setminus \{x_0\}$ implies that $\|y'\|^2 = d^2/2$. | 大模型 | 11.676 | 13.034 | 1.358 | 8 |
| 8 | Having established the existence of a vector $y'$ satisfying all necessary properties, define the point $y$ in terms of $y'$ and $x_0$. Verify that this choice of $y$ makes the original set $\{\frac{\sqrt{2}}{d}(x-y): x\in S\}$ an orthonormal system. | 大模型 | 13.034 | 14.323 | 1.289 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            10.84s
+------------------------------------------------------------+
步骤 1 |#####                                                       | 3.48s - 4.56s
步骤 2 |        #######                                             | 5.08s - 6.37s
步骤 3 |               ########                                     | 6.37s - 7.73s
步骤 4 |                     #########                              | 7.40s - 8.96s
步骤 5 |                              ########                      | 8.96s - 10.39s
步骤 6 |                                      #######               | 10.39s - 11.68s
步骤 7 |                                             #######        | 11.68s - 13.03s
步骤 8 |                                                    ########| 13.03s - 14.32s
```

