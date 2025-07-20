# 数据集处理报告

## 模型配置

- 小模型: qwen/qwen-2.5-7b-instruct
- 大模型: openai/gpt-4o
- 路由模型: anthropic/claude-3.5-sonnet
- 难度阈值: 3
- 工作线程数: 10

## 概述

- 数据集: dataset/original_data/math200.json
- 问题总数: 10
- 正确数量: 5
- 准确率: 50.00%
- 平均执行时间: 20.69 秒
- 平均成本: $0.0044

## 任务规划指标

- 平均任务步骤数: 7.33
- 平均压缩比例: 85.22%
- 平均每步骤Token限制: 20.31 tokens

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.400 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 13.432 秒

### 生成速度
- 小模型平均每秒生成token数: 5.69 tokens/s
- 大模型平均每秒生成token数: 2.01 tokens/s
- 路由模型平均每秒生成token数: 8.11 tokens/s
- 总平均每秒生成token数: 15.81 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Three semicircles of radius 1 are constructed o... | ✓ | 17.09 | 0.0045 | 7 | 85.71% | 13.6 |
| 2 | What is the distance between the two intersecti... | ✓ | 26.11 | 0.0034 | 6 | 100.00% | 16.7 |
| 3 | By joining alternate vertices of a regular hexa... | ✗ | 20.19 | 0.0037 | 6 | 83.33% | 22.5 |
| 4 | Two parallel chords in a circle have lengths 10... | ✗ | 21.22 | 0.0066 | 9 | 77.78% | 18.3 |
| 5 | Find all solutions to \[\sin \left( \tan^{-1} (... | ✓ | 12.04 | 0.0000 | - | - | - |
| 6 | There exists a polynomial $P$ of degree 5 with ... | ✗ | 28.10 | 0.0074 | 10 | 90.00% | 23.0 |
| 7 | Triangle $ABC$ has three different integer side... | ✗ | 27.08 | 0.0077 | 9 | 77.78% | 25.0 |
| 8 | Let $x,$ $y,$ and $z$ be positive real numbers ... | ✓ | 23.26 | 0.0045 | 7 | 85.71% | 27.9 |
| 9 | Simplify: $\frac{\sqrt{2.5^2-0.7^2}}{2.7-2.5}$. | ✓ | 14.03 | 0.0031 | 6 | 83.33% | 10.8 |
| 10 | Four points, $A$, $B$, $C$, and $D$, are chosen... | ✗ | 17.76 | 0.0035 | 6 | 83.33% | 25.0 |
