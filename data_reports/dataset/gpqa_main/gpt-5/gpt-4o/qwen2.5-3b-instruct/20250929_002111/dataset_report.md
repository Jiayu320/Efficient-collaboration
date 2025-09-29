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
- 正确数量: 3
- 准确率: 30.00%
- 平均执行时间: 110.07 秒
- 平均成本: $0.0299

## 任务规划指标

- 平均任务步骤数: 4.40
- 平均压缩比例: 87.33%
- 平均每步骤Token限制: 95.18 tokens

## 理论性能指标

- 平均理论执行时间: 14.847 秒
- 平均顺序执行时间: 30.264 秒
- 平均并行加速比: 2.03x
- 理论与实际执行时间比例: 0.13x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 12.377 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 31.798 秒

### 生成速度
- 小模型平均每秒生成token数: 1.15 tokens/s
- 大模型平均每秒生成token数: 9.29 tokens/s
- 路由模型平均每秒生成token数: 8.32 tokens/s
- 总平均每秒生成token数: 18.77 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 75.98 | 0.0211 | 5 | 80.00% | 82.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 112.84 | 0.0289 | 5 | 100.00% | 74.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✓ | 137.27 | 0.0232 | 5 | 100.00% | 84.0 |
| 4 | how many of the following compounds exhibit opt... | ✓ | 179.50 | 0.0330 | 4 | 75.00% | 150.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 108.48 | 0.0573 | 6 | 83.33% | 100.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✓ | 115.13 | 0.0243 | 5 | 60.00% | 46.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 111.96 | 0.0263 | 3 | 100.00% | 146.7 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 96.15 | 0.0243 | 4 | 75.00% | 57.5 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 59.71 | 0.0245 | 3 | 100.00% | 66.7 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 103.69 | 0.0357 | 4 | 100.00% | 145.0 |
