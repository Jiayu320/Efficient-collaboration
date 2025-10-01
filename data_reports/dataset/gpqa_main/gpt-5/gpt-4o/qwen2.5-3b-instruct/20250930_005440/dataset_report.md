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
- 正确数量: 1
- 准确率: 10.00%
- 平均执行时间: 228.23 秒
- 平均成本: $0.0339

## 任务规划指标

- 平均任务步骤数: 7.00
- 平均压缩比例: 69.88%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 58.321 秒
- 平均顺序执行时间: 92.057 秒
- 平均并行加速比: 1.62x
- 理论与实际执行时间比例: 0.26x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 16.772 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 85.140 秒

### 生成速度
- 小模型平均每秒生成token数: 5.61 tokens/s
- 大模型平均每秒生成token数: 8.42 tokens/s
- 路由模型平均每秒生成token数: 3.93 tokens/s
- 总平均每秒生成token数: 17.97 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 92.44 | 0.0249 | 7 | 57.14% | 0.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 199.33 | 0.0147 | 5 | 100.00% | 0.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✓ | 93.09 | 0.0197 | 6 | 66.67% | 0.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 190.83 | 0.1158 | 16 | 25.00% | 0.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 161.10 | 0.0486 | 6 | 66.67% | 0.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 198.61 | 0.0234 | 6 | 100.00% | 0.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 753.29 | 0.0260 | 6 | 83.33% | 0.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 173.06 | 0.0186 | 4 | 75.00% | 0.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 171.93 | 0.0136 | 6 | 50.00% | 0.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 248.64 | 0.0339 | 8 | 75.00% | 0.0 |
