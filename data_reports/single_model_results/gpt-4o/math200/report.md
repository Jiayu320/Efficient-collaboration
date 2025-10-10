# 单模型数据集处理报告

## 模型信息

- 模型: openai/gpt-4o
- 延迟 (TTFT): 0.735 秒
- 吞吐量: 144.50 tokens/s

## 概述

- 数据集: dataset/original_data/math200.json
- 问题总数: 20
- 正确数量: 10
- 准确率: 50.00%
- 平均执行时间: 15.70 秒
- 平均理论时间: 5.29 秒
- 实际/理论时间比率: 2.97x
- 平均成本: $0.0068

## 性能指标

- 平均首个令牌响应时间 (TTFT): 2.479 秒
- 平均每秒生成token数: 44.44 tokens/s
- 理论每秒生成token数: 144.50 tokens/s
- 实际/理论吞吐量比率: 0.31x

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 理论时间(秒) | 成本($) |
| --- | --- | --- | --- | --- | --- |
| 1 | Three semicircles of radius 1 are constructed o... | ✗ | 8.72 | 3.41 | 0.0048 |
| 2 | What is the distance between the two intersecti... | ✓ | 12.96 | 7.03 | 0.0092 |
| 3 | By joining alternate vertices of a regular hexa... | ✗ | 11.09 | 4.17 | 0.0054 |
| 4 | Two parallel chords in a circle have lengths 10... | ✓ | 23.18 | 6.24 | 0.0084 |
| 5 | Find all solutions to \[\sin \left( \tan^{-1} (... | ✗ | 21.08 | 4.92 | 0.0062 |
| 6 | There exists a polynomial $P$ of degree 5 with ... | ✗ | 28.57 | 6.18 | 0.0080 |
| 7 | Triangle $ABC$ has three different integer side... | ✗ | 13.39 | 5.38 | 0.0068 |
| 8 | Let $x,$ $y,$ and $z$ be positive real numbers ... | ✗ | 17.43 | 5.21 | 0.0067 |
| 9 | Simplify: $\frac{\sqrt{2.5^2-0.7^2}}{2.7-2.5}$. | ✓ | 7.73 | 3.15 | 0.0036 |
| 10 | Four points, $A$, $B$, $C$, and $D$, are chosen... | ✓ | 16.16 | 4.29 | 0.0052 |
| 11 | Determine the number of solutions in $x$ of the... | ✓ | 15.81 | 5.03 | 0.0063 |
| 12 | On the graph of $y=(x+2)^4-100$, how many point... | ✓ | 10.46 | 5.92 | 0.0076 |
| 13 | Convert $\frac{3}{16}$ to base 2. Express your ... | ✓ | 9.39 | 3.86 | 0.0046 |
| 14 | Let $S$ be the set of points $(a,b)$ with $0 \l... | ✗ | 23.96 | 5.80 | 0.0075 |
| 15 | What is the perimeter, in units, of a rhombus i... | ✓ | 12.48 | 4.31 | 0.0052 |
| 16 | Three schools have a chess tournament. Four pla... | ✓ | 11.90 | 3.68 | 0.0044 |
| 17 | Three distinct integers $a,$ $b,$ and $c$ have ... | ✓ | 14.75 | 6.95 | 0.0092 |
| 18 | Determine $w^2+x^2+y^2+z^2$ if \[\begin{aligned... | ✗ | 25.46 | 8.16 | 0.0113 |
| 19 | If $a$ and $b$ are positive integers such that ... | ✗ | 16.17 | 6.02 | 0.0078 |
| 20 | Find the maximum value of \[\frac{x - y}{x^4 + ... | ✗ | 13.22 | 6.02 | 0.0077 |
