# 数据集处理报告

## 模型配置

- 小模型: gpt-4.1-mini
- 大模型: gpt-4.1-mini
- 路由模型: qwen3-4b
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/livebench-reasoning.json
- 问题总数: 50
- 正确数量: 21
- 准确率: 42.00%
- 平均执行时间: 51.39 秒
- 平均成本: $0.0085

## 任务规划指标

- 平均任务步骤数: 5.42
- 平均压缩比例: 71.18%
- 平均每步骤Token限制: 88.32 tokens

## 理论性能指标

- 平均理论执行时间: 8.527 秒
- 平均顺序执行时间: 12.760 秒
- 平均并行加速比: 1.60x
- 理论与实际执行时间比例: 0.17x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.823 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 37.742 秒

### 生成速度
- 小模型平均每秒生成token数: 67.13 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 6.19 tokens/s
- 总平均每秒生成token数: 73.32 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | There are 2 people standing in a line. From lef... | ✓ | 27.65 | 0.0020 | 4 | 100.00% | 52.5 |
| 2 | There are 2 people standing in a line. From lef... | ✓ | 25.69 | 0.0045 | 4 | 75.00% | 42.5 |
| 3 | There are 2 people standing in a line. From lef... | ✓ | 15.84 | 0.0028 | 6 | 33.33% | 40.0 |
| 4 | There are 2 people standing in a line. From lef... | ✓ | 35.01 | 0.0050 | 4 | 75.00% | 42.5 |
| 5 | There are 2 people standing in a line. From lef... | ✓ | 14.91 | 0.0014 | 4 | 100.00% | 57.5 |
| 6 | There are 2 people standing in a line. From lef... | ✓ | 25.47 | 0.0027 | 5 | 100.00% | 52.0 |
| 7 | There are 2 people standing in a line. From lef... | ✓ | 24.09 | 0.0032 | 6 | 83.33% | 58.3 |
| 8 | There are 3 people standing in a line. From lef... | ✓ | 43.13 | 0.0080 | 6 | 50.00% | 38.3 |
| 9 | There are 3 people standing in a line. From lef... | ✓ | 32.92 | 0.0057 | 6 | 50.00% | 58.3 |
| 10 | There are 3 people standing in a line. From lef... | ✓ | 36.64 | 0.0095 | 5 | 80.00% | 52.0 |
| 11 | There are 3 people standing in a line. From lef... | ✓ | 21.64 | 0.0034 | 4 | 75.00% | 41.2 |
| 12 | There are 3 people standing in a line. From lef... | ✗ | 50.47 | 0.0084 | 5 | 100.00% | 130.0 |
| 13 | There are 3 people standing in a line. From lef... | ✓ | 28.70 | 0.0040 | 6 | 50.00% | 70.0 |
| 14 | There are 3 people standing in a line. From lef... | ✓ | 23.54 | 0.0056 | 5 | 40.00% | 52.0 |
| 15 | There are 3 people standing in a line. From lef... | ✗ | 45.07 | 0.0081 | 5 | 100.00% | 134.0 |
| 16 | There are 3 people standing in a line. From lef... | ✓ | 28.78 | 0.0037 | 5 | 100.00% | 46.0 |
| 17 | There are 3 people standing in a line. From lef... | ✓ | 93.99 | 0.0085 | 5 | 100.00% | 74.0 |
| 18 | There are 3 people standing in a line. From lef... | ✓ | 35.43 | 0.0035 | 5 | 60.00% | 50.0 |
| 19 | There are 3 people standing in a line. From lef... | ✗ | 53.94 | 0.0087 | 4 | 100.00% | 120.0 |
| 20 | There are 3 people standing in a line. From lef... | ✗ | 123.77 | 0.0126 | 5 | 80.00% | 96.0 |
| 21 | There are 3 people standing in a line. From lef... | ✗ | 42.29 | 0.0083 | 6 | 50.00% | 36.7 |
| 22 | There are 3 people standing in a line. From lef... | ✗ | 37.98 | 0.0079 | 7 | 57.14% | 164.3 |
| 23 | There are 3 people standing in a line. From lef... | ✗ | 104.71 | 0.0136 | 10 | 30.00% | 41.0 |
| 24 | There are 3 people standing in a line. From lef... | ✗ | 106.41 | 0.0121 | 5 | 80.00% | 130.0 |
| 25 | There are 3 people standing in a line. From lef... | ✓ | 61.54 | 0.0088 | 6 | 66.67% | 121.7 |
| 26 | There are 3 people standing in a line. From lef... | ✗ | 58.63 | 0.0070 | 5 | 100.00% | 74.0 |
| 27 | There are 3 people standing in a line. From lef... | ✗ | 95.03 | 0.0155 | 7 | 57.14% | 64.3 |
| 28 | There are 3 people standing in a line. From lef... | ✓ | 26.27 | 0.0054 | 6 | 50.00% | 133.3 |
| 29 | There are 3 people standing in a line. From lef... | ✗ | 49.29 | 0.0087 | 6 | 50.00% | 128.3 |
| 30 | There are 4 people standing in a line. From lef... | ✗ | 70.24 | 0.0147 | 6 | 50.00% | 60.0 |
| 31 | There are 4 people standing in a line. From lef... | ✗ | 47.27 | 0.0072 | 4 | 75.00% | 97.5 |
| 32 | There are 4 people standing in a line. From lef... | ✗ | 36.99 | 0.0088 | 5 | 100.00% | 160.0 |
| 33 | There are 4 people standing in a line. From lef... | ✗ | 16.79 | 0.0057 | 5 | 40.00% | 60.0 |
| 34 | There are 4 people standing in a line. From lef... | ✓ | 46.76 | 0.0088 | 5 | 40.00% | 140.0 |
| 35 | There are 4 people standing in a line. From lef... | ✓ | 49.88 | 0.0076 | 6 | 50.00% | 66.7 |
| 36 | There are 4 people standing in a line. From lef... | ✓ | 34.31 | 0.0065 | 5 | 60.00% | 62.0 |
| 37 | There are 4 people standing in a line. From lef... | ✗ | 50.45 | 0.0100 | 5 | 100.00% | 68.0 |
| 38 | There are 4 people standing in a line. From lef... | ✗ | 46.15 | 0.0193 | 6 | 50.00% | 141.7 |
| 39 | There are 4 people standing in a line. From lef... | ✗ | 67.98 | 0.0148 | 5 | 40.00% | 140.0 |
| 40 | There are 4 people standing in a line. From lef... | ✗ | 39.65 | 0.0058 | 5 | 100.00% | 140.0 |
| 41 | There are 4 people standing in a line. From lef... | ✗ | 65.07 | 0.0089 | 6 | 100.00% | 100.0 |
| 42 | There are 4 people standing in a line. From lef... | ✗ | 52.33 | 0.0179 | 6 | 50.00% | 150.0 |
| 43 | There are 4 people standing in a line. From lef... | ✗ | 197.25 | 0.0149 | 5 | 80.00% | 112.0 |
| 44 | There are 5 people standing in a line. From lef... | ✗ | 43.01 | 0.0068 | 6 | 100.00% | 53.3 |
| 45 | There are 5 people standing in a line. From lef... | ✗ | 84.12 | 0.0151 | 5 | 80.00% | 140.0 |
| 46 | There are 5 people standing in a line. From lef... | ✗ | 34.02 | 0.0122 | 6 | 50.00% | 75.0 |
| 47 | There are 5 people standing in a line. From lef... | ✗ | 69.50 | 0.0124 | 5 | 100.00% | 134.0 |
| 48 | There are 5 people standing in a line. From lef... | ✗ | 33.65 | 0.0073 | 6 | 50.00% | 131.7 |
| 49 | There are 5 people standing in a line. From lef... | ✗ | 70.50 | 0.0118 | 5 | 80.00% | 62.0 |
| 50 | There are 5 people standing in a line. From lef... | ✗ | 44.74 | 0.0111 | 7 | 71.43% | 121.4 |
