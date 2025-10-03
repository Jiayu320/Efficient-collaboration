# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: gpt-4o
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 10
- 正确数量: 0
- 准确率: 0.00%
- 平均执行时间: 131.10 秒
- 平均成本: $0.0099

## 任务规划指标

- 平均任务步骤数: 4.80
- 平均压缩比例: 85.67%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 55.138 秒
- 平均顺序执行时间: 72.871 秒
- 平均并行加速比: 1.40x
- 理论与实际执行时间比例: 0.42x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.382 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 121.365 秒

### 生成速度
- 小模型平均每秒生成token数: 13.55 tokens/s
- 大模型平均每秒生成token数: 2.96 tokens/s
- 路由模型平均每秒生成token数: 2.67 tokens/s
- 总平均每秒生成token数: 19.19 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 93.27 | 0.0061 | 4 | 100.00% | 0.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 147.42 | 0.0089 | 3 | 100.00% | 0.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 186.65 | 0.0046 | 7 | 100.00% | 0.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 71.28 | 0.0186 | 10 | 30.00% | 0.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 78.51 | 0.0079 | 3 | 100.00% | 0.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 131.68 | 0.0159 | 4 | 100.00% | 0.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 124.56 | 0.0106 | 4 | 100.00% | 0.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 150.98 | 0.0151 | 5 | 80.00% | 0.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 151.02 | 0.0080 | 5 | 80.00% | 0.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 175.59 | 0.0035 | 3 | 66.67% | 0.0 |
