# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: gemini-2.5-pro
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 10
- 正确数量: 0
- 准确率: 0.00%
- 平均执行时间: 61.34 秒
- 平均成本: $0.0282

## 任务规划指标

- 平均任务步骤数: 3.80
- 平均压缩比例: 88.00%
- 平均每步骤Token限制: 140.38 tokens

## 理论性能指标

- 平均理论执行时间: 9.261 秒
- 平均顺序执行时间: 20.172 秒
- 平均并行加速比: 2.18x
- 理论与实际执行时间比例: 0.15x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 6.008 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 26.887 秒

### 生成速度
- 小模型平均每秒生成token数: 3.69 tokens/s
- 大模型平均每秒生成token数: 14.15 tokens/s
- 路由模型平均每秒生成token数: 17.83 tokens/s
- 总平均每秒生成token数: 35.66 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 43.74 | 0.0212 | 2 | 100.00% | 250.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 39.74 | 0.0264 | 4 | 75.00% | 72.5 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 60.65 | 0.0159 | 3 | 100.00% | 120.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 61.59 | 0.0217 | 3 | 100.00% | 173.3 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 61.93 | 0.0507 | 5 | 80.00% | 180.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 85.37 | 0.0341 | 5 | 100.00% | 88.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 44.42 | 0.0279 | 4 | 100.00% | 130.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 60.44 | 0.0255 | 4 | 75.00% | 95.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 60.07 | 0.0297 | 4 | 75.00% | 145.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 95.50 | 0.0293 | 4 | 75.00% | 150.0 |
