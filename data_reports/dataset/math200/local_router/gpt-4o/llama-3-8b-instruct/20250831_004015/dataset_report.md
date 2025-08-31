# 数据集处理报告

## 模型配置

- 小模型: meta-llama/llama-3-8b-instruct
- 大模型: openai/gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/original_data/math200.json
- 问题总数: 20
- 正确数量: 7
- 准确率: 35.00%
- 平均执行时间: 21.41 秒
- 平均成本: $0.0028

## 任务规划指标

- 平均任务步骤数: 7.55
- 平均压缩比例: 74.22%
- 平均每步骤Token限制: 25.96 tokens

## 理论性能指标

- 平均理论执行时间: 6.519 秒
- 平均顺序执行时间: 17.942 秒
- 平均并行加速比: 2.72x
- 理论与实际执行时间比例: 0.30x


## 任务分配统计

- 总任务数: 151
- 小模型执行任务数: 1
- 大模型执行任务数: 150
- 小模型任务占比: 0.66%
- 大模型任务占比: 99.34%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.099 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 15.144 秒

### 生成速度
- 小模型平均每秒生成token数: 0.30 tokens/s
- 大模型平均每秒生成token数: 5.62 tokens/s
- 路由模型平均每秒生成token数: 23.35 tokens/s
- 总平均每秒生成token数: 29.27 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Three semicircles of radius 1 are constructed o... | ✗ | 19.45 | 0.0045 | 9 | 66.67% | 20.0 |
| 2 | What is the distance between the two intersecti... | ✓ | 15.43 | 0.0022 | 6 | 66.67% | 27.5 |
| 3 | By joining alternate vertices of a regular hexa... | ✓ | 20.95 | 0.0037 | 9 | 66.67% | 35.0 |
| 4 | Two parallel chords in a circle have lengths 10... | ✓ | 22.38 | 0.0066 | 7 | 85.71% | 20.0 |
| 5 | Find all solutions to \[\sin \left( \tan^{-1} (... | ✗ | 30.20 | 0.0043 | 9 | 88.89% | 22.2 |
| 6 | There exists a polynomial $P$ of degree 5 with ... | ✗ | 20.99 | 0.0054 | 8 | 75.00% | 33.1 |
| 7 | Triangle $ABC$ has three different integer side... | ✓ | 18.94 | 0.0031 | 9 | 66.67% | 28.3 |
| 8 | Let $x,$ $y,$ and $z$ be positive real numbers ... | ✗ | 19.99 | 0.0038 | 6 | 66.67% | 35.0 |
| 9 | Simplify: $\frac{\sqrt{2.5^2-0.7^2}}{2.7-2.5}$. | ✓ | 20.14 | 0.0020 | 7 | 71.43% | 13.6 |
| 10 | Four points, $A$, $B$, $C$, and $D$, are chosen... | ✗ | 14.04 | 0.0009 | 4 | 75.00% | 27.5 |
| 11 | Determine the number of solutions in $x$ of the... | ✗ | 13.86 | 0.0012 | 5 | 80.00% | 27.0 |
| 12 | On the graph of $y=(x+2)^4-100$, how many point... | ✓ | 19.31 | 0.0038 | 6 | 100.00% | 26.7 |
| 13 | Convert $\frac{3}{16}$ to base 2. Express your ... | ✗ | 16.27 | 0.0015 | 9 | 77.78% | 15.6 |
| 14 | Let $S$ be the set of points $(a,b)$ with $0 \l... | ✗ | 17.48 | 0.0019 | 6 | 83.33% | 37.5 |
| 15 | What is the perimeter, in units, of a rhombus i... | ✗ | 14.39 | 0.0007 | 5 | 80.00% | 26.0 |
| 16 | Three schools have a chess tournament. Four pla... | ✓ | 14.26 | 0.0010 | 6 | 50.00% | 30.8 |
| 17 | Three distinct integers $a,$ $b,$ and $c$ have ... | ✗ | 74.29 | 0.0052 | 9 | 88.89% | 23.3 |
| 18 | Determine $w^2+x^2+y^2+z^2$ if \[\begin{aligned... | ✗ | 26.38 | 0.0019 | 17 | 11.76% | 15.9 |
| 19 | If $a$ and $b$ are positive integers such that ... | ✗ | 13.19 | 0.0000 | 8 | 100.00% | 22.5 |
| 20 | Find the maximum value of \[\frac{x - y}{x^4 + ... | ✗ | 16.31 | 0.0026 | 6 | 83.33% | 31.7 |
