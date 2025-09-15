# 数据集处理报告

## 模型配置

- 小模型: meta-llama/llama-3-8b-instruct
- 大模型: openai/gpt-4o
- 路由模型: anthropic/claude-3.5-sonnet
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/original_data/math200.json
- 问题总数: 20
- 正确数量: 3
- 准确率: 15.00%
- 平均执行时间: 22.19 秒
- 平均成本: $0.0173

## 任务规划指标

- 平均任务步骤数: 6.60
- 平均压缩比例: 81.64%
- 平均每步骤Token限制: 33.65 tokens

## 理论性能指标

- 平均理论执行时间: 7.758 秒
- 平均顺序执行时间: 20.489 秒
- 平均并行加速比: 2.64x
- 理论与实际执行时间比例: 0.35x


## 任务分配统计

- 总任务数: 132
- 小模型执行任务数: 5
- 大模型执行任务数: 127
- 小模型任务占比: 3.79%
- 大模型任务占比: 96.21%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.428 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 13.838 秒

### 生成速度
- 小模型平均每秒生成token数: 0.72 tokens/s
- 大模型平均每秒生成token数: 9.46 tokens/s
- 路由模型平均每秒生成token数: 12.68 tokens/s
- 总平均每秒生成token数: 22.86 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Three semicircles of radius 1 are constructed o... | ✓ | 25.12 | 0.0199 | 7 | 71.43% | 26.4 |
| 2 | What is the distance between the two intersecti... | ✓ | 25.28 | 0.0165 | 5 | 100.00% | 25.0 |
| 3 | By joining alternate vertices of a regular hexa... | ✗ | 24.68 | 0.0163 | 7 | 57.14% | 35.7 |
| 4 | Two parallel chords in a circle have lengths 10... | ✗ | 21.08 | 0.0195 | 8 | 75.00% | 34.4 |
| 5 | Find all solutions to \[\sin \left( \tan^{-1} (... | ✗ | 23.53 | 0.0183 | 7 | 71.43% | 33.6 |
| 6 | There exists a polynomial $P$ of degree 5 with ... | ✗ | 25.81 | 0.0182 | 6 | 100.00% | 42.5 |
| 7 | Triangle $ABC$ has three different integer side... | ✗ | 20.70 | 0.0164 | 7 | 85.71% | 35.0 |
| 8 | Let $x,$ $y,$ and $z$ be positive real numbers ... | ✗ | 24.40 | 0.0234 | 8 | 87.50% | 40.0 |
| 9 | Simplify: $\frac{\sqrt{2.5^2-0.7^2}}{2.7-2.5}$. | ✓ | 15.13 | 0.0134 | 6 | 66.67% | 22.5 |
| 10 | Four points, $A$, $B$, $C$, and $D$, are chosen... | ✗ | 25.01 | 0.0157 | 7 | 71.43% | 34.3 |
| 11 | Determine the number of solutions in $x$ of the... | ✗ | 17.53 | 0.0161 | 6 | 83.33% | 32.5 |
| 12 | On the graph of $y=(x+2)^4-100$, how many point... | ✓ | 23.01 | 0.0161 | 6 | 66.67% | 30.8 |
| 13 | Convert $\frac{3}{16}$ to base 2. Express your ... | ✓ | 21.47 | 0.0141 | 5 | 100.00% | 25.0 |
| 14 | Let $S$ be the set of points $(a,b)$ with $0 \l... | ✗ | 18.28 | 0.0176 | 7 | 100.00% | 45.0 |
| 15 | What is the perimeter, in units, of a rhombus i... | ✗ | 15.45 | 0.0136 | 5 | 100.00% | 28.0 |
| 16 | Three schools have a chess tournament. Four pla... | ✓ | 26.30 | 0.0151 | 6 | 66.67% | 30.8 |
| 17 | Three distinct integers $a,$ $b,$ and $c$ have ... | ✗ | 23.32 | 0.0197 | 8 | 87.50% | 36.9 |
| 18 | Determine $w^2+x^2+y^2+z^2$ if \[\begin{aligned... | ✗ | 22.91 | 0.0202 | 6 | 83.33% | 39.2 |
| 19 | If $a$ and $b$ are positive integers such that ... | ✓ | 25.95 | 0.0199 | 8 | 87.50% | 32.5 |
| 20 | Find the maximum value of \[\frac{x - y}{x^4 + ... | ✗ | 18.81 | 0.0167 | 7 | 71.43% | 42.9 |
