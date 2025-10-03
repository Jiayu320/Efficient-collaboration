# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: gpt-4o
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 10
- 正确数量: 1
- 准确率: 10.00%
- 平均执行时间: 19.98 秒
- 平均成本: $0.0310

## 任务规划指标

- 平均任务步骤数: 5.30
- 平均压缩比例: 77.76%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 26.590 秒
- 平均顺序执行时间: 43.557 秒
- 平均并行加速比: 1.66x
- 理论与实际执行时间比例: 1.33x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.642 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 7.972 秒

### 生成速度
- 小模型平均每秒生成token数: 74.02 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 15.15 tokens/s
- 总平均每秒生成token数: 89.18 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 17.84 | 0.0145 | 3 | 100.00% | 0.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 18.23 | 0.0237 | 4 | 75.00% | 0.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 20.46 | 0.0198 | 5 | 100.00% | 0.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 25.86 | 0.1051 | 17 | 17.65% | 0.0 |
| 5 | A coating is applied to a substrate resulting i... | ✓ | 21.93 | 0.0280 | 4 | 75.00% | 0.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 19.56 | 0.0214 | 3 | 100.00% | 0.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 21.03 | 0.0198 | 4 | 100.00% | 0.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 18.21 | 0.0263 | 4 | 75.00% | 0.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 18.18 | 0.0215 | 4 | 75.00% | 0.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 18.50 | 0.0301 | 5 | 60.00% | 0.0 |
