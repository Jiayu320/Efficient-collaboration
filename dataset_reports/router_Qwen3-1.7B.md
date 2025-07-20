# 数据集处理报告

## 模型配置

- 小模型: qwen/qwen-2.5-7b-instruct
- 大模型: openai/gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/original_data/math200.json
- 问题总数: 10
- 正确数量: 5
- 准确率: 50.00%
- 平均执行时间: 22.87 秒
- 平均成本: $0.0004

## 任务规划指标

- 平均任务步骤数: 8.62
- 平均压缩比例: 79.66%
- 平均每步骤Token限制: 58.76 tokens

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 0.792 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 19.685 秒

### 生成速度
- 小模型平均每秒生成token数: 9.87 tokens/s
- 大模型平均每秒生成token数: 0.91 tokens/s
- 路由模型平均每秒生成token数: 4.85 tokens/s
- 总平均每秒生成token数: 15.63 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Three semicircles of radius 1 are constructed o... | ✗ | 18.66 | 0.0000 | 8 | 62.50% | 31.2 |
| 2 | What is the distance between the two intersecti... | ✓ | 23.65 | 0.0000 | 6 | 100.00% | 45.0 |
| 3 | By joining alternate vertices of a regular hexa... | ✗ | 26.73 | 0.0028 | 7 | 71.43% | 84.3 |
| 4 | Two parallel chords in a circle have lengths 10... | ✗ | 40.56 | 0.0000 | 10 | 90.00% | 71.0 |
| 5 | Find all solutions to \[\sin \left( \tan^{-1} (... | ✓ | 8.85 | 0.0000 | - | - | - |
| 6 | There exists a polynomial $P$ of degree 5 with ... | ✗ | 30.37 | 0.0016 | 9 | 66.67% | 67.8 |
| 7 | Triangle $ABC$ has three different integer side... | ✗ | 28.18 | 0.0000 | 10 | 100.00% | 56.0 |
| 8 | Let $x,$ $y,$ and $z$ be positive real numbers ... | ✓ | 24.35 | 0.0000 | 9 | 66.67% | 77.8 |
| 9 | Simplify: $\frac{\sqrt{2.5^2-0.7^2}}{2.7-2.5}$. | ✓ | 8.14 | 0.0000 | - | - | - |
| 10 | Four points, $A$, $B$, $C$, and $D$, are chosen... | ✓ | 19.19 | 0.0000 | 10 | 80.00% | 37.0 |
