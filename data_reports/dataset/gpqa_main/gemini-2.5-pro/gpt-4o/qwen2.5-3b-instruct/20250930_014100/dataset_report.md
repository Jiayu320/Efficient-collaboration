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
- 平均执行时间: 281.69 秒
- 平均成本: $0.0231

## 任务规划指标

- 平均任务步骤数: 5.90
- 平均压缩比例: 65.83%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 50.011 秒
- 平均顺序执行时间: 73.041 秒
- 平均并行加速比: 1.40x
- 理论与实际执行时间比例: 0.18x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 20.696 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 134.009 秒

### 生成速度
- 小模型平均每秒生成token数: 5.40 tokens/s
- 大模型平均每秒生成token数: 8.05 tokens/s
- 路由模型平均每秒生成token数: 2.09 tokens/s
- 总平均每秒生成token数: 15.54 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 62.70 | 0.0287 | 7 | 71.43% | 0.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 137.57 | 0.0275 | 7 | 71.43% | 0.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 77.04 | 0.0205 | 5 | 100.00% | 0.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 888.07 | 0.0769 | 12 | 33.33% | 0.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 91.94 | 0.0000 | 0 | 0.00% | 0.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 896.82 | 0.0169 | 7 | 85.71% | 0.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 62.45 | 0.0155 | 4 | 100.00% | 0.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 330.51 | 0.0217 | 7 | 71.43% | 0.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 98.48 | 0.0177 | 6 | 50.00% | 0.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 171.34 | 0.0059 | 4 | 75.00% | 0.0 |
