# 数据集处理报告

## 模型配置

- 小模型: meta-llama/llama-3-8b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/original_data/math200.json
- 问题总数: 10
- 正确数量: 2
- 准确率: 20.00%
- 平均执行时间: 17.58 秒
- 平均成本: $0.0016

## 任务规划指标

- 平均任务步骤数: 7.60
- 平均压缩比例: 81.19%
- 平均每步骤Token限制: 27.03 tokens

## 理论性能指标

- 平均理论执行时间: 10.977 秒
- 平均顺序执行时间: 18.168 秒
- 平均并行加速比: 1.66x
- 理论与实际执行时间比例: 0.62x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.233 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 11.554 秒

### 生成速度
- 小模型平均每秒生成token数: 0.13 tokens/s
- 大模型平均每秒生成token数: 3.02 tokens/s
- 路由模型平均每秒生成token数: 7.05 tokens/s
- 总平均每秒生成token数: 10.20 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Three semicircles of radius 1 are constructed o... | ✓ | 16.75 | 0.0012 | 5 | 80.00% | 23.0 |
| 2 | What is the distance between the two intersecti... | ✗ | 16.31 | 0.0014 | 9 | 55.56% | 24.4 |
| 3 | By joining alternate vertices of a regular hexa... | ✗ | 21.42 | 0.0017 | 9 | 88.89% | 27.2 |
| 4 | Two parallel chords in a circle have lengths 10... | ✓ | 16.24 | 0.0023 | 7 | 100.00% | 20.0 |
| 5 | Find all solutions to \[\sin \left( \tan^{-1} (... | ✓ | 18.51 | 0.0014 | 6 | 100.00% | 45.0 |
| 6 | There exists a polynomial $P$ of degree 5 with ... | ✗ | 19.50 | 0.0017 | 8 | 75.00% | 33.8 |
| 7 | Triangle $ABC$ has three different integer side... | ✓ | 17.73 | 0.0022 | 8 | 75.00% | 28.8 |
| 8 | Let $x,$ $y,$ and $z$ be positive real numbers ... | ✓ | 19.75 | 0.0026 | 8 | 87.50% | 27.5 |
| 9 | Simplify: $\frac{\sqrt{2.5^2-0.7^2}}{2.7-2.5}$. | ✓ | 14.16 | 0.0007 | 8 | 75.00% | 16.2 |
| 10 | Four points, $A$, $B$, $C$, and $D$, are chosen... | ✓ | 15.47 | 0.0010 | 8 | 75.00% | 24.4 |
