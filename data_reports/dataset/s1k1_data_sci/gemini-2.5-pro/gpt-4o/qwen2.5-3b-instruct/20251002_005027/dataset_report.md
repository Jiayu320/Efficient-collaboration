# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: gemini-2.5-pro
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k1_data_sci.json
- 问题总数: 10
- 正确数量: 1
- 准确率: 10.00%
- 平均执行时间: 117.29 秒
- 平均成本: $0.0183

## 任务规划指标

- 平均任务步骤数: 6.50
- 平均压缩比例: 62.76%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 57.742 秒
- 平均顺序执行时间: 87.391 秒
- 平均并行加速比: 1.56x
- 理论与实际执行时间比例: 0.49x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 4.621 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 82.374 秒

### 生成速度
- 小模型平均每秒生成token数: 9.57 tokens/s
- 大模型平均每秒生成token数: 8.64 tokens/s
- 路由模型平均每秒生成token数: 4.95 tokens/s
- 总平均每秒生成token数: 23.17 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Imagine a radioactive nuclei X(Z,A) can decay i... | ✗ | 206.08 | 0.0154 | 7 | 57.14% | 0.0 |
| 2 | 2 mol of $\mathrm{Hg}(g)$ is combusted in a fix... | ✗ | 175.69 | 0.0218 | 7 | 57.14% | 0.0 |
| 3 | Identify the final product produced when cyclob... | ✓ | 72.28 | 0.0176 | 6 | 100.00% | 0.0 |
| 4 | There is a C-NOT gate where the condition is th... | ✗ | 117.51 | 0.0105 | 5 | 60.00% | 0.0 |
| 5 | An ideal gas is expanded from $\left(\mathrm{p}... | ✗ | 64.56 | 0.0223 | 5 | 40.00% | 0.0 |
| 6 | Arrange the nucleophiles (1. 4-methylcyclohexan... | ✗ | 100.17 | 0.0410 | 10 | 50.00% | 0.0 |
| 7 | Solve the crossword puzzle. You are presented w... | ✗ | 175.50 | 0.0113 | 5 | 80.00% | 0.0 |
| 8 | Determine which set of states mentioned below a... | ✗ | 26.14 | 0.0093 | 7 | 57.14% | 0.0 |
| 9 | The decomposition reaction $2 \mathrm{~N}_{2} \... | ✗ | 147.50 | 0.0142 | 6 | 83.33% | 0.0 |
| 10 | The majority of stars in our Galaxy form and ev... | ✗ | 87.49 | 0.0198 | 7 | 42.86% | 0.0 |
