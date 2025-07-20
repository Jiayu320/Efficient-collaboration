# 数据集处理报告

## 模型配置

- 小模型: qwen/qwen-2.5-7b-instruct
- 大模型: openai/gpt-4o
- 路由模型: qwen/qwen-2.5-7b-instruct
- 难度阈值: 3
- 工作线程数: 10

## 概述

- 数据集: dataset/original_data/math200.json
- 问题总数: 10
- 正确数量: 3
- 准确率: 30.00%
- 平均执行时间: 15.52 秒
- 平均成本: $0.0049

## 任务规划指标

- 平均任务步骤数: 4.56
- 平均压缩比例: 85.19%
- 平均每步骤Token限制: 1.75 tokens

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.118 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 11.484 秒

### 生成速度
- 小模型平均每秒生成token数: 4.83 tokens/s
- 大模型平均每秒生成token数: 6.86 tokens/s
- 路由模型平均每秒生成token数: 10.37 tokens/s
- 总平均每秒生成token数: 22.06 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Three semicircles of radius 1 are constructed o... | ✗ | 13.79 | 0.0026 | 4 | 50.00% | 1.0 |
| 2 | What is the distance between the two intersecti... | ✓ | 8.92 | 0.0018 | 2 | 100.00% | 2.0 |
| 3 | By joining alternate vertices of a regular hexa... | ✗ | 12.07 | 0.0036 | 4 | 100.00% | 2.2 |
| 4 | Two parallel chords in a circle have lengths 10... | ✗ | 9.61 | 0.0039 | 6 | 66.67% | 1.3 |
| 5 | Find all solutions to \[\sin \left( \tan^{-1} (... | ✗ | 7.55 | 0.0000 | - | - | - |
| 6 | There exists a polynomial $P$ of degree 5 with ... | ✗ | 32.18 | 0.0198 | 9 | 100.00% | 1.0 |
| 7 | Triangle $ABC$ has three different integer side... | ✓ | 16.36 | 0.0065 | 4 | 100.00% | 2.0 |
| 8 | Let $x,$ $y,$ and $z$ be positive real numbers ... | ✗ | 23.60 | 0.0048 | 3 | 100.00% | 1.7 |
| 9 | Simplify: $\frac{\sqrt{2.5^2-0.7^2}}{2.7-2.5}$. | ✓ | 16.27 | 0.0022 | 4 | 50.00% | 1.5 |
| 10 | Four points, $A$, $B$, $C$, and $D$, are chosen... | ✗ | 14.84 | 0.0035 | 5 | 100.00% | 3.0 |
