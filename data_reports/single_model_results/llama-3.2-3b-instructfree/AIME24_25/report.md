# 单模型数据集处理报告

## 模型信息

- 模型: meta-llama/llama-3.2-3b-instruct:free
- 延迟 (TTFT): 0.710 秒
- 吞吐量: 165.00 tokens/s

## 概述

- 数据集: dataset/TestData/AIME24_25.json
- 问题总数: 60
- 超时问题数: 0 (0.00%)
- 有效问题数: 60
- 正确数量: 12
- 准确率(有效问题): 20.00%
- 平均执行时间(有效问题): 46.60 秒
- 平均理论时间(有效问题): 10.23 秒
- 实际/理论时间比率: 4.55x
- 平均成本(有效问题): $0.0000

## 性能指标

- 平均首个令牌响应时间 (TTFT): 2.780 秒
- 平均每秒生成token数: 57.76 tokens/s
- 理论每秒生成token数: 165.00 tokens/s
- 实际/理论吞吐量比率: 0.35x

## 详细结果

| # | 问题 | 状态 | 执行时间(秒) | 理论时间(秒) | 成本($) |
| --- | --- | --- | --- | --- | --- |
| 1 | Every morning Aya goes for a $9$-kilometer-long... | ✗ | 19.60 | 7.49 | 0.0000 |
| 2 | Let $ABC$ be a triangle inscribed in circle $\o... | ✓ | 12.10 | 2.70 | 0.0000 |
| 3 | Each vertex of a regular octagon is independent... | ✗ | 14.38 | 6.17 | 0.0000 |
| 4 | Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| ... | ✗ | 20.60 | 7.78 | 0.0000 |
| 5 | Let $p$ be the least prime number for which the... | ✗ | 12.58 | 5.52 | 0.0000 |
| 6 | Let $ABCD$ be a tetrahedron such that $AB=CD= \... | ✓ | 12.42 | 3.96 | 0.0000 |
| 7 | Let $\mathcal{B}$ be the set of rectangular box... | ✗ | 13.60 | 6.81 | 0.0000 |
| 8 | There exist real numbers $x$ and $y$, both grea... | ✗ | 15.15 | 3.45 | 0.0000 |
| 9 | Alice and Bob play the following game. A stack ... | ✗ | 11.18 | 3.25 | 0.0000 |
| 10 | Jen enters a lottery by picking $4$ distinct nu... | ✓ | 991.55 | 0.72 | 0.0000 |
| 11 | Rectangles $ABCD$ and $EFGH$ are drawn such tha... | ✓ | 383.98 | 0.72 | 0.0000 |
| 12 | Consider the paths of length $16$ that follow t... | ✗ | 11.31 | 2.94 | 0.0000 |
| 13 | Find the largest possible real part of \[(75+11... | ✗ | 13.82 | 5.88 | 0.0000 |
| 14 | Eight circles of radius $34$ are sequentially t... | ✓ | 64.72 | 37.41 | 0.0000 |
| 15 | Let $A$, $B$, $C$, and $D$ be point on the hype... | ✗ | 17.07 | 7.67 | 0.0000 |
| 16 | Among the 900 residents of Aimeville, there are... | ✓ | 57.06 | 43.52 | 0.0000 |
| 17 | Let $\triangle ABC$ have circumcenter $O$ and i... | ✓ | 52.15 | 38.36 | 0.0000 |
| 18 | Find the number of triples of nonnegative integ... | ✓ | 11.32 | 3.58 | 0.0000 |
| 19 | Let \(O=(0,0)\), \(A=\left(\tfrac{1}{2},0\right... | ✓ | 39.72 | 29.81 | 0.0000 |
| 20 | Let $\omega\neq 1$ be a 13th root of unity. Fin... | ✗ | 12.78 | 5.07 | 0.0000 |
| 21 | Let \(b\ge 2\) be an integer. Call a positive i... | ✗ | 13.27 | 4.06 | 0.0000 |
| 22 | Find the number of rectangles that can be forme... | ✗ | 8.44 | 2.72 | 0.0000 |
| 23 | A list of positive integers has the following p... | ✗ | 9.04 | 2.63 | 0.0000 |
| 24 | Find the number of ways to place a digit in eac... | ✗ | 11.98 | 3.71 | 0.0000 |
| 25 | Let $x,y$ and $z$ be positive real numbers that... | ✗ | 23.34 | 6.84 | 0.0000 |
| 26 | Let ABCDEF be a convex equilateral hexagon in w... | ✗ | 11.16 | 2.83 | 0.0000 |
| 27 | Alice chooses a set $A$ of positive integers. T... | ✓ | 61.68 | 40.76 | 0.0000 |
| 28 | Let $N$ be the greatest four-digit positive int... | ✓ | 11.91 | 3.49 | 0.0000 |
| 29 | Torus $T$ is the surface produced by revolving ... | ✓ | 239.86 | 0.71 | 0.0000 |
| 30 | There is a collection of $25$ indistinguishable... | ✗ | 14.18 | 1.80 | 0.0000 |
| 31 | Find the sum of all integer bases $b>9$ for whi... | ✗ | 17.66 | 5.13 | 0.0000 |
| 32 | On $\triangle ABC$ points $A,D,E$, and $B$ lie ... | ✗ | 18.12 | 2.73 | 0.0000 |
| 33 | The 9 members of a baseball team went to an ice... | ✗ | 14.57 | 4.13 | 0.0000 |
| 34 | Find the number of ordered pairs $(x,y)$, where... | ✗ | 11.80 | 5.27 | 0.0000 |
| 35 | There are $8!=40320$ eight-digit positive integ... | ✗ | 13.15 | 5.16 | 0.0000 |
| 36 | An isosceles trapezoid has an inscribed circle ... | ✗ | 74.52 | 56.16 | 0.0000 |
| 37 | The twelve letters $A,B,C,D,E,F,G,H,I,J,K$, and... | ✗ | 9.58 | 3.33 | 0.0000 |
| 38 | Let $k$ be real numbers such that the system $|... | ✗ | 10.30 | 4.35 | 0.0000 |
| 39 | The parabola with equation $y=x^{2}-4$ is rotat... | ✗ | 11.56 | 5.43 | 0.0000 |
| 40 | The 27 cells of a $3\times9$ grid are filled in... | ✗ | 18.86 | 7.93 | 0.0000 |
| 41 | A piecewise linear periodic function is defined... | ✗ | 13.01 | 4.07 | 0.0000 |
| 42 | The set of points in 3-dimensional coordinate s... | ✗ | 11.16 | 4.95 | 0.0000 |
| 43 | Alex divides a disk into four quadrants with tw... | ✗ | 85.00 | 61.43 | 0.0000 |
| 44 | Let $ABCDE$ be a convex pentagon with $AB=14, B... | ✗ | 14.13 | 7.12 | 0.0000 |
| 45 | Let $N$ denote the number of ordered triples of... | ✗ | 10.93 | 5.53 | 0.0000 |
| 46 | Six points $ A, B, C, D, E, $ and $ F $ lie in ... | ✗ | 57.19 | 44.65 | 0.0000 |
| 47 | Find the sum of all positive integers $ n $ suc... | ✗ | 14.99 | 7.27 | 0.0000 |
| 48 | Four unit squares form a $2 \times 2$ grid. Eac... | ✗ | 26.89 | 18.12 | 0.0000 |
| 49 | The product $ \prod_{k=4}^{63} \frac{\log_k(5^{... | ✗ | 10.74 | 4.28 | 0.0000 |
| 50 | Suppose $ \triangle ABC $ has angles $ \angle B... | ✗ | 12.06 | 3.15 | 0.0000 |
| 51 | Circle $\omega_1$ with radius 6 centered at poi... | ✗ | 11.81 | 5.62 | 0.0000 |
| 52 | Let $ A $ be the set of positive integer diviso... | ✗ | 13.28 | 5.54 | 0.0000 |
| 53 | From an unlimited supply of 1-cent coins, 10-ce... | ✗ | 11.60 | 5.38 | 0.0000 |
| 54 | There are $ n $ values of $ x $ in the interval... | ✗ | 10.56 | 3.98 | 0.0000 |
| 55 | Sixteen chairs are arranged in a row. Eight peo... | ✗ | 10.11 | 1.92 | 0.0000 |
| 56 | Let $ S $ be the set of vertices of a regular 2... | ✗ | 12.03 | 3.49 | 0.0000 |
| 57 | Let $ A_1A_2 \ldots A_{11} $ be an 11-sided non... | ✗ | 12.88 | 5.64 | 0.0000 |
| 58 | Let the sequence of rationals $ x_1, x_2, \ldot... | ✗ | 13.48 | 5.35 | 0.0000 |
| 59 | Let $ \triangle ABC $ be a right triangle with ... | ✗ | 24.55 | 7.11 | 0.0000 |
| 60 | There are exactly three positive real numbers $... | ✗ | 27.28 | 17.30 | 0.0000 |
