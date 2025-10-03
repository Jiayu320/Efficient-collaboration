# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: gpt-4o
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 15
- 正确数量: 4
- 准确率: 26.67%
- 平均执行时间: 39.26 秒
- 平均成本: $0.0213

## 任务规划指标

- 平均任务步骤数: 3.60
- 平均压缩比例: 100.00%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 28.579 秒
- 平均顺序执行时间: 29.813 秒
- 平均并行加速比: 1.04x
- 理论与实际执行时间比例: 0.73x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 4.836 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 12.820 秒

### 生成速度
- 小模型平均每秒生成token数: 26.11 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 5.41 tokens/s
- 总平均每秒生成token数: 31.52 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 39.11 | 0.0091 | 3 | 100.00% | 0.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 32.32 | 0.0145 | 3 | 100.00% | 0.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✓ | 40.41 | 0.0190 | 4 | 100.00% | 0.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 52.83 | 0.0556 | 8 | 100.00% | 0.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 36.39 | 0.0171 | 3 | 100.00% | 0.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 36.88 | 0.0222 | 3 | 100.00% | 0.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 42.46 | 0.0212 | 4 | 100.00% | 0.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 31.58 | 0.0127 | 3 | 100.00% | 0.0 |
| 9 | In a parallel universe where a magnet can have ... | ✓ | 31.69 | 0.0158 | 3 | 100.00% | 0.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 35.96 | 0.0133 | 3 | 100.00% | 0.0 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 43.72 | 0.0147 | 3 | 100.00% | 0.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 51.71 | 0.0386 | 5 | 100.00% | 0.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 40.69 | 0.0309 | 3 | 100.00% | 0.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 36.57 | 0.0202 | 3 | 100.00% | 0.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 36.56 | 0.0152 | 3 | 100.00% | 0.0 |
