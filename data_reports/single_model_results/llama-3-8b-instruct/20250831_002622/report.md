# 单模型数据集处理报告

## 模型信息

- 模型: meta-llama/llama-3-8b-instruct
- 延迟 (TTFT): 0.554 秒
- 吞吐量: 2069.56 tokens/s

## 概述

- 数据集: dataset/original_data/math200.json
- 问题总数: 20
- 正确数量: 1
- 准确率: 5.00%
- 平均执行时间: 12.12 秒
- 平均理论时间: 0.83 秒
- 实际/理论时间比率: 14.63x
- 平均成本: $0.0000

## 性能指标

- 平均首个令牌响应时间 (TTFT): 2.182 秒
- 平均每秒生成token数: 49.78 tokens/s
- 理论每秒生成token数: 2069.56 tokens/s
- 实际/理论吞吐量比率: 0.02x

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 理论时间(秒) | 成本($) |
| --- | --- | --- | --- | --- | --- |
| 1 | Three semicircles of radius 1 are constructed o... | ✗ | 8.65 | 0.63 | 0.0000 |
| 2 | What is the distance between the two intersecti... | ✗ | 9.30 | 0.71 | 0.0000 |
| 3 | By joining alternate vertices of a regular hexa... | ✗ | 12.92 | 0.65 | 0.0000 |
| 4 | Two parallel chords in a circle have lengths 10... | ✗ | 14.99 | 0.76 | 0.0000 |
| 5 | Find all solutions to \[\sin \left( \tan^{-1} (... | ✗ | 6.39 | 0.90 | 0.0000 |
| 6 | There exists a polynomial $P$ of degree 5 with ... | ✗ | 33.60 | 1.56 | 0.0001 |
| 7 | Triangle $ABC$ has three different integer side... | ✗ | 12.57 | 0.79 | 0.0000 |
| 8 | Let $x,$ $y,$ and $z$ be positive real numbers ... | ✗ | 9.56 | 0.72 | 0.0000 |
| 9 | Simplify: $\frac{\sqrt{2.5^2-0.7^2}}{2.7-2.5}$. | ✓ | 10.23 | 0.64 | 0.0000 |
| 10 | Four points, $A$, $B$, $C$, and $D$, are chosen... | ✗ | 11.17 | 0.76 | 0.0000 |
| 11 | Determine the number of solutions in $x$ of the... | ✗ | 8.04 | 0.69 | 0.0000 |
| 12 | On the graph of $y=(x+2)^4-100$, how many point... | ✗ | 8.56 | 0.74 | 0.0000 |
| 13 | Convert $\frac{3}{16}$ to base 2. Express your ... | ✗ | 13.89 | 0.80 | 0.0000 |
| 14 | Let $S$ be the set of points $(a,b)$ with $0 \l... | ✗ | 14.15 | 0.97 | 0.0001 |
| 15 | What is the perimeter, in units, of a rhombus i... | ✗ | 11.25 | 0.81 | 0.0000 |
| 16 | Three schools have a chess tournament. Four pla... | ✗ | 8.58 | 0.69 | 0.0000 |
| 17 | Three distinct integers $a,$ $b,$ and $c$ have ... | ✗ | 26.01 | 1.19 | 0.0001 |
| 18 | Determine $w^2+x^2+y^2+z^2$ if \[\begin{aligned... | ✗ | 5.50 | 0.91 | 0.0001 |
| 19 | If $a$ and $b$ are positive integers such that ... | ✗ | 6.10 | 0.90 | 0.0000 |
| 20 | Find the maximum value of \[\frac{x - y}{x^4 + ... | ✗ | 10.87 | 0.77 | 0.0000 |
