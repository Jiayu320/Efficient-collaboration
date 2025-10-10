# 单模型数据集处理报告

## 模型信息

- 模型: Qwen/Qwen2.5-3B-Instruct
- 延迟 (TTFT): 0.690 秒
- 吞吐量: 64.53 tokens/s

## 概述

- 数据集: dataset/TestData/AIME24_25.json
- 问题总数: 60
- 正确数量: 11
- 准确率: 18.33%
- 平均执行时间: 19.98 秒
- 平均理论时间: 12.53 秒
- 实际/理论时间比率: 1.59x
- 平均成本: $0.0000

## 性能指标

- 平均首个令牌响应时间 (TTFT): 0.120 秒
- 平均每秒生成token数: 38.79 tokens/s
- 理论每秒生成token数: 64.53 tokens/s
- 实际/理论吞吐量比率: 0.60x

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 理论时间(秒) | 成本($) |
| --- | --- | --- | --- | --- | --- |
| 1 | Every morning Aya goes for a $9$-kilometer-long... | ✓ | 22.95 | 14.17 | 0.0000 |
| 2 | Let $ABC$ be a triangle inscribed in circle $\o... | ✗ | 21.00 | 13.32 | 0.0000 |
| 3 | Each vertex of a regular octagon is independent... | ✗ | 13.16 | 7.97 | 0.0000 |
| 4 | Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| ... | ✗ | 20.30 | 14.59 | 0.0000 |
| 5 | Let $p$ be the least prime number for which the... | ✓ | 21.68 | 15.16 | 0.0000 |
| 6 | Let $ABCD$ be a tetrahedron such that $AB=CD= \... | ✓ | 22.43 | 14.45 | 0.0000 |
| 7 | Let $\mathcal{B}$ be the set of rectangular box... | ✗ | 20.80 | 14.19 | 0.0000 |
| 8 | There exist real numbers $x$ and $y$, both grea... | ✓ | 10.69 | 6.27 | 0.0000 |
| 9 | Alice and Bob play the following game. A stack ... | ✗ | 20.11 | 12.67 | 0.0000 |
| 10 | Jen enters a lottery by picking $4$ distinct nu... | ✓ | 15.16 | 10.79 | 0.0000 |
| 11 | Rectangles $ABCD$ and $EFGH$ are drawn such tha... | ✗ | 18.94 | 12.51 | 0.0000 |
| 12 | Consider the paths of length $16$ that follow t... | ✗ | 8.97 | 5.62 | 0.0000 |
| 13 | Find the largest possible real part of \[(75+11... | ✗ | 22.39 | 12.34 | 0.0000 |
| 14 | Eight circles of radius $34$ are sequentially t... | ✗ | 21.87 | 14.45 | 0.0000 |
| 15 | Let $A$, $B$, $C$, and $D$ be point on the hype... | ✓ | 22.92 | 15.49 | 0.0000 |
| 16 | Among the 900 residents of Aimeville, there are... | ✓ | 23.23 | 15.74 | 0.0000 |
| 17 | Let $\triangle ABC$ have circumcenter $O$ and i... | ✗ | 15.89 | 9.14 | 0.0000 |
| 18 | Find the number of triples of nonnegative integ... | ✗ | 23.30 | 11.62 | 0.0000 |
| 19 | Let \(O=(0,0)\), \(A=\left(\tfrac{1}{2},0\right... | ✗ | 22.83 | 14.40 | 0.0000 |
| 20 | Let $\omega\neq 1$ be a 13th root of unity. Fin... | ✗ | 21.89 | 14.50 | 0.0000 |
| 21 | Let \(b\ge 2\) be an integer. Call a positive i... | ✗ | 16.93 | 11.86 | 0.0000 |
| 22 | Find the number of rectangles that can be forme... | ✗ | 15.98 | 10.28 | 0.0000 |
| 23 | A list of positive integers has the following p... | ✗ | 17.25 | 11.68 | 0.0000 |
| 24 | Find the number of ways to place a digit in eac... | ✗ | 22.98 | 13.91 | 0.0000 |
| 25 | Let $x,y$ and $z$ be positive real numbers that... | ✓ | 21.55 | 15.57 | 0.0000 |
| 26 | Let ABCDEF be a convex equilateral hexagon in w... | ✗ | 10.43 | 6.49 | 0.0000 |
| 27 | Alice chooses a set $A$ of positive integers. T... | ✓ | 23.37 | 14.85 | 0.0000 |
| 28 | Let $N$ be the greatest four-digit positive int... | ✓ | 22.02 | 15.35 | 0.0000 |
| 29 | Torus $T$ is the surface produced by revolving ... | ✗ | 18.51 | 13.01 | 0.0000 |
| 30 | There is a collection of $25$ indistinguishable... | ✗ | 12.25 | 8.21 | 0.0000 |
| 31 | Find the sum of all integer bases $b>9$ for whi... | ✗ | 22.10 | 15.44 | 0.0000 |
| 32 | On $\triangle ABC$ points $A,D,E$, and $B$ lie ... | ✗ | 23.24 | 15.18 | 0.0000 |
| 33 | The 9 members of a baseball team went to an ice... | ✗ | 18.37 | 12.59 | 0.0000 |
| 34 | Find the number of ordered pairs $(x,y)$, where... | ✗ | 22.15 | 11.96 | 0.0000 |
| 35 | There are $8!=40320$ eight-digit positive integ... | ✗ | 22.32 | 16.08 | 0.0000 |
| 36 | An isosceles trapezoid has an inscribed circle ... | ✗ | 55.16 | 13.75 | 0.0000 |
| 37 | The twelve letters $A,B,C,D,E,F,G,H,I,J,K$, and... | ✗ | 23.28 | 11.09 | 0.0000 |
| 38 | Let $k$ be real numbers such that the system $|... | ✗ | 21.80 | 15.66 | 0.0000 |
| 39 | The parabola with equation $y=x^{2}-4$ is rotat... | ✗ | 22.27 | 15.63 | 0.0000 |
| 40 | The 27 cells of a $3\times9$ grid are filled in... | ✓ | 20.78 | 13.91 | 0.0000 |
| 41 | A piecewise linear periodic function is defined... | ✗ | 22.97 | 14.87 | 0.0000 |
| 42 | The set of points in 3-dimensional coordinate s... | ✗ | 19.28 | 12.62 | 0.0000 |
| 43 | Alex divides a disk into four quadrants with tw... | ✗ | 11.68 | 7.32 | 0.0000 |
| 44 | Let $ABCDE$ be a convex pentagon with $AB=14, B... | ✗ | 15.95 | 10.92 | 0.0000 |
| 45 | Let $N$ denote the number of ordered triples of... | ✗ | 18.16 | 12.19 | 0.0000 |
| 46 | Six points $ A, B, C, D, E, $ and $ F $ lie in ... | ✗ | 23.35 | 14.19 | 0.0000 |
| 47 | Find the sum of all positive integers $ n $ suc... | ✗ | 21.57 | 15.35 | 0.0000 |
| 48 | Four unit squares form a $2 \times 2$ grid. Eac... | ✗ | 17.69 | 10.73 | 0.0000 |
| 49 | The product $ \prod_{k=4}^{63} \frac{\log_k(5^{... | ✗ | 16.32 | 10.92 | 0.0000 |
| 50 | Suppose $ \triangle ABC $ has angles $ \angle B... | ✗ | 15.53 | 7.11 | 0.0000 |
| 51 | Circle $\omega_1$ with radius 6 centered at poi... | ✗ | 19.35 | 12.82 | 0.0000 |
| 52 | Let $ A $ be the set of positive integer diviso... | ✗ | 19.30 | 12.75 | 0.0000 |
| 53 | From an unlimited supply of 1-cent coins, 10-ce... | ✗ | 19.59 | 13.10 | 0.0000 |
| 54 | There are $ n $ values of $ x $ in the interval... | ✗ | 18.45 | 12.79 | 0.0000 |
| 55 | Sixteen chairs are arranged in a row. Eight peo... | ✗ | 17.86 | 11.04 | 0.0000 |
| 56 | Let $ S $ be the set of vertices of a regular 2... | ✗ | 12.61 | 7.71 | 0.0000 |
| 57 | Let $ A_1A_2 \ldots A_{11} $ be an 11-sided non... | ✗ | 23.08 | 14.62 | 0.0000 |
| 58 | Let the sequence of rationals $ x_1, x_2, \ldot... | ✗ | 22.80 | 13.20 | 0.0000 |
| 59 | Let $ \triangle ABC $ be a right triangle with ... | ✗ | 16.28 | 10.75 | 0.0000 |
| 60 | There are exactly three positive real numbers $... | ✗ | 23.95 | 15.02 | 0.0000 |
