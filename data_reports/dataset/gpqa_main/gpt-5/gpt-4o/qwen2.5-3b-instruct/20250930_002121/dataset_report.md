# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: gpt-5
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 10
- 正确数量: 2
- 准确率: 20.00%
- 平均执行时间: 128.42 秒
- 平均成本: $0.0362

## 任务规划指标

- 平均任务步骤数: 6.30
- 平均压缩比例: 76.36%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 56.996 秒
- 平均顺序执行时间: 83.660 秒
- 平均并行加速比: 1.48x
- 理论与实际执行时间比例: 0.44x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 8.239 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 55.610 秒

### 生成速度
- 小模型平均每秒生成token数: 4.54 tokens/s
- 大模型平均每秒生成token数: 12.48 tokens/s
- 路由模型平均每秒生成token数: 5.28 tokens/s
- 总平均每秒生成token数: 22.30 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 63.95 | 0.0409 | 6 | 83.33% | 0.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 104.31 | 0.0267 | 5 | 80.00% | 0.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 129.68 | 0.0236 | 6 | 83.33% | 0.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 229.91 | 0.0736 | 11 | 36.36% | 0.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 159.74 | 0.0394 | 6 | 66.67% | 0.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 124.00 | 0.0272 | 4 | 100.00% | 0.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✓ | 105.06 | 0.0415 | 7 | 71.43% | 0.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 124.06 | 0.0144 | 5 | 80.00% | 0.0 |
| 9 | In a parallel universe where a magnet can have ... | ✓ | 112.57 | 0.0283 | 5 | 100.00% | 0.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 130.89 | 0.0460 | 8 | 62.50% | 0.0 |
