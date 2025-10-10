# 单模型数据集处理报告

## 模型信息

- 模型: gpt-4o
- 延迟 (TTFT): 0.735 秒
- 吞吐量: 144.50 tokens/s

## 概述

- 数据集: dataset/TestData/AIME24_25.json
- 问题总数: 60
- 超时问题数: 0 (0.00%)
- 有效问题数: 60
- 正确数量: 7
- 准确率(有效问题): 11.67%
- 平均执行时间(有效问题): 16.11 秒
- 平均理论时间(有效问题): 5.94 秒
- 实际/理论时间比率: 2.71x
- 平均成本(有效问题): $0.0078

## 性能指标

- 平均首个令牌响应时间 (TTFT): 3.431 秒
- 平均每秒生成token数: 46.59 tokens/s
- 理论每秒生成token数: 144.50 tokens/s
- 实际/理论吞吐量比率: 0.32x

## 详细结果

| # | 问题 | 状态 | 执行时间(秒) | 理论时间(秒) | 成本($) |
| --- | --- | --- | --- | --- | --- |
| 1 | Every morning Aya goes for a $9$-kilometer-long... | ✓ | 20.03 | 8.12 | 0.0110 |
| 2 | Let $ABC$ be a triangle inscribed in circle $\o... | ✓ | 17.65 | 5.24 | 0.0068 |
| 3 | Each vertex of a regular octagon is independent... | ✗ | 21.92 | 6.15 | 0.0080 |
| 4 | Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| ... | ✗ | 18.41 | 7.73 | 0.0103 |
| 5 | Let $p$ be the least prime number for which the... | ✗ | 16.48 | 6.57 | 0.0086 |
| 6 | Let $ABCD$ be a tetrahedron such that $AB=CD= \... | ✓ | 15.67 | 5.48 | 0.0072 |
| 7 | Let $\mathcal{B}$ be the set of rectangular box... | ✗ | 15.27 | 5.63 | 0.0073 |
| 8 | There exist real numbers $x$ and $y$, both grea... | ✓ | 15.99 | 5.02 | 0.0063 |
| 9 | Alice and Bob play the following game. A stack ... | ✗ | 21.19 | 7.10 | 0.0094 |
| 10 | Jen enters a lottery by picking $4$ distinct nu... | ✓ | 17.44 | 5.57 | 0.0073 |
| 11 | Rectangles $ABCD$ and $EFGH$ are drawn such tha... | ✗ | 12.91 | 3.70 | 0.0045 |
| 12 | Consider the paths of length $16$ that follow t... | ✗ | 12.39 | 5.45 | 0.0069 |
| 13 | Find the largest possible real part of \[(75+11... | ✗ | 17.84 | 5.82 | 0.0075 |
| 14 | Eight circles of radius $34$ are sequentially t... | ✗ | 16.43 | 6.31 | 0.0083 |
| 15 | Let $A$, $B$, $C$, and $D$ be point on the hype... | ✗ | 13.22 | 4.97 | 0.0063 |
| 16 | Among the 900 residents of Aimeville, there are... | ✗ | 14.41 | 6.57 | 0.0087 |
| 17 | Let $\triangle ABC$ have circumcenter $O$ and i... | ✓ | 16.94 | 5.71 | 0.0073 |
| 18 | Find the number of triples of nonnegative integ... | ✓ | 13.77 | 5.66 | 0.0073 |
| 19 | Let \(O=(0,0)\), \(A=\left(\tfrac{1}{2},0\right... | ✗ | 15.44 | 7.36 | 0.0100 |
| 20 | Let $\omega\neq 1$ be a 13th root of unity. Fin... | ✗ | 12.70 | 3.86 | 0.0046 |
| 21 | Let \(b\ge 2\) be an integer. Call a positive i... | ✗ | 17.20 | 6.46 | 0.0086 |
| 22 | Find the number of rectangles that can be forme... | ✗ | 12.34 | 3.97 | 0.0051 |
| 23 | A list of positive integers has the following p... | ✗ | 17.63 | 6.42 | 0.0084 |
| 24 | Find the number of ways to place a digit in eac... | ✗ | 15.69 | 5.70 | 0.0075 |
| 25 | Let $x,y$ and $z$ be positive real numbers that... | ✗ | 16.82 | 6.89 | 0.0092 |
| 26 | Let ABCDEF be a convex equilateral hexagon in w... | ✗ | 15.93 | 5.98 | 0.0077 |
| 27 | Alice chooses a set $A$ of positive integers. T... | ✗ | 15.77 | 5.62 | 0.0072 |
| 28 | Let $N$ be the greatest four-digit positive int... | ✗ | 18.99 | 8.44 | 0.0113 |
| 29 | Torus $T$ is the surface produced by revolving ... | ✗ | 16.20 | 5.21 | 0.0074 |
| 30 | There is a collection of $25$ indistinguishable... | ✗ | 16.96 | 4.22 | 0.0053 |
| 31 | Find the sum of all integer bases $b>9$ for whi... | ✗ | 17.32 | 6.02 | 0.0077 |
| 32 | On $\triangle ABC$ points $A,D,E$, and $B$ lie ... | ✗ | 17.41 | 5.84 | 0.0077 |
| 33 | The 9 members of a baseball team went to an ice... | ✗ | 15.92 | 5.78 | 0.0076 |
| 34 | Find the number of ordered pairs $(x,y)$, where... | ✗ | 16.41 | 6.20 | 0.0080 |
| 35 | There are $8!=40320$ eight-digit positive integ... | ✗ | 17.25 | 6.61 | 0.0087 |
| 36 | An isosceles trapezoid has an inscribed circle ... | ✗ | 13.66 | 4.90 | 0.0062 |
| 37 | The twelve letters $A,B,C,D,E,F,G,H,I,J,K$, and... | ✗ | 17.37 | 6.77 | 0.0090 |
| 38 | Let $k$ be real numbers such that the system $|... | ✗ | 22.49 | 7.26 | 0.0097 |
| 39 | The parabola with equation $y=x^{2}-4$ is rotat... | ✗ | 19.48 | 7.46 | 0.0099 |
| 40 | The 27 cells of a $3\times9$ grid are filled in... | ✗ | 16.98 | 5.88 | 0.0080 |
| 41 | A piecewise linear periodic function is defined... | ✗ | 19.80 | 8.90 | 0.0122 |
| 42 | The set of points in 3-dimensional coordinate s... | ✗ | 17.23 | 6.67 | 0.0088 |
| 43 | Alex divides a disk into four quadrants with tw... | ✗ | 12.60 | 4.53 | 0.0057 |
| 44 | Let $ABCDE$ be a convex pentagon with $AB=14, B... | ✗ | 13.76 | 4.96 | 0.0064 |
| 45 | Let $N$ denote the number of ordered triples of... | ✗ | 14.69 | 5.91 | 0.0076 |
| 46 | Six points $ A, B, C, D, E, $ and $ F $ lie in ... | ✗ | 15.54 | 6.17 | 0.0081 |
| 47 | Find the sum of all positive integers $ n $ suc... | ✗ | 13.38 | 4.72 | 0.0059 |
| 48 | Four unit squares form a $2 \times 2$ grid. Eac... | ✗ | 13.66 | 5.30 | 0.0067 |
| 49 | The product $ \prod_{k=4}^{63} \frac{\log_k(5^{... | ✗ | 19.10 | 6.32 | 0.0085 |
| 50 | Suppose $ \triangle ABC $ has angles $ \angle B... | ✗ | 14.67 | 5.54 | 0.0075 |
| 51 | Circle $\omega_1$ with radius 6 centered at poi... | ✗ | 14.82 | 5.61 | 0.0075 |
| 52 | Let $ A $ be the set of positive integer diviso... | ✗ | 17.11 | 7.41 | 0.0099 |
| 53 | From an unlimited supply of 1-cent coins, 10-ce... | ✗ | 12.47 | 4.62 | 0.0062 |
| 54 | There are $ n $ values of $ x $ in the interval... | ✗ | 17.99 | 7.08 | 0.0094 |
| 55 | Sixteen chairs are arranged in a row. Eight peo... | ✗ | 15.77 | 5.41 | 0.0069 |
| 56 | Let $ S $ be the set of vertices of a regular 2... | ✗ | 15.39 | 5.15 | 0.0065 |
| 57 | Let $ A_1A_2 \ldots A_{11} $ be an 11-sided non... | ✗ | 15.05 | 7.36 | 0.0101 |
| 58 | Let the sequence of rationals $ x_1, x_2, \ldot... | ✗ | 13.75 | 6.28 | 0.0083 |
| 59 | Let $ \triangle ABC $ be a right triangle with ... | ✗ | 11.38 | 3.36 | 0.0040 |
| 60 | There are exactly three positive real numbers $... | ✗ | 14.68 | 5.43 | 0.0070 |
