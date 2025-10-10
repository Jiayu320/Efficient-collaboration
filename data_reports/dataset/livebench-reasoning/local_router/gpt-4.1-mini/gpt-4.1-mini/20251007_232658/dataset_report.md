# 数据集处理报告

## 模型配置

- 小模型: gpt-4.1-mini
- 大模型: gpt-4.1-mini
- 路由模型: saves/Llama-3.2-1B-Instruct/full/Llama-3-2-1B_ep5
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/livebench-reasoning.json
- 问题总数: 50
- 正确数量: 14
- 准确率: 28.00%
- 平均执行时间: 45.40 秒
- 平均成本: $0.0204

## 任务规划指标

- 平均任务步骤数: 6.40
- 平均压缩比例: 64.73%
- 平均每步骤Token限制: 66.68 tokens

## 理论性能指标

- 平均理论执行时间: 7.586 秒
- 平均顺序执行时间: 14.019 秒
- 平均并行加速比: 1.97x
- 理论与实际执行时间比例: 0.17x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 2.306 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 25.742 秒

### 生成速度
- 小模型平均每秒生成token数: 91.21 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 16.18 tokens/s
- 总平均每秒生成token数: 107.38 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | There are 2 people standing in a line. From lef... | ✓ | 22.38 | 0.0113 | 6 | 66.67% | 33.3 |
| 2 | There are 2 people standing in a line. From lef... | ✓ | 29.06 | 0.0139 | 7 | 100.00% | 58.6 |
| 3 | There are 2 people standing in a line. From lef... | ✗ | 6.57 | 0.0089 | 4 | 100.00% | 40.0 |
| 4 | There are 2 people standing in a line. From lef... | ✓ | 19.84 | 0.0148 | 6 | 50.00% | 33.3 |
| 5 | There are 2 people standing in a line. From lef... | ✓ | 49.49 | 0.0113 | 6 | 50.00% | 41.7 |
| 6 | There are 2 people standing in a line. From lef... | ✓ | 42.32 | 0.0118 | 6 | 50.00% | 38.3 |
| 7 | There are 2 people standing in a line. From lef... | ✗ | 111.76 | 0.0142 | 7 | 57.14% | 28.6 |
| 8 | There are 3 people standing in a line. From lef... | ✓ | 30.62 | 0.0126 | 4 | 100.00% | 62.5 |
| 9 | There are 3 people standing in a line. From lef... | ✗ | 26.27 | 0.0167 | 6 | 66.67% | 46.7 |
| 10 | There are 3 people standing in a line. From lef... | ✗ | 17.15 | 0.0162 | 6 | 50.00% | 31.7 |
| 11 | There are 3 people standing in a line. From lef... | ✗ | 47.11 | 0.0200 | 7 | 100.00% | 31.4 |
| 12 | There are 3 people standing in a line. From lef... | ✗ | 38.55 | 0.0161 | 6 | 83.33% | 45.0 |
| 13 | There are 3 people standing in a line. From lef... | ✓ | 23.95 | 0.0170 | 6 | 50.00% | 46.7 |
| 14 | There are 3 people standing in a line. From lef... | ✓ | 20.76 | 0.0147 | 6 | 50.00% | 51.7 |
| 15 | There are 3 people standing in a line. From lef... | ✓ | 30.93 | 0.0133 | 6 | 100.00% | 38.3 |
| 16 | There are 3 people standing in a line. From lef... | ✓ | 27.81 | 0.0131 | 4 | 100.00% | 95.0 |
| 17 | There are 3 people standing in a line. From lef... | ✗ | 28.67 | 0.0163 | 6 | 50.00% | 51.7 |
| 18 | There are 3 people standing in a line. From lef... | ✗ | 5.57 | 0.0062 | 1 | 100.00% | 100.0 |
| 19 | There are 3 people standing in a line. From lef... | ✗ | 36.19 | 0.0162 | 6 | 100.00% | 90.0 |
| 20 | There are 3 people standing in a line. From lef... | ✗ | 30.46 | 0.0194 | 6 | 50.00% | 106.7 |
| 21 | There are 3 people standing in a line. From lef... | ✗ | 27.30 | 0.0155 | 6 | 50.00% | 51.7 |
| 22 | There are 3 people standing in a line. From lef... | ✓ | 23.68 | 0.0159 | 6 | 66.67% | 100.0 |
| 23 | There are 3 people standing in a line. From lef... | ✗ | 49.20 | 0.0305 | 10 | 40.00% | 38.0 |
| 24 | There are 3 people standing in a line. From lef... | ✗ | 21.10 | 0.0282 | 12 | 25.00% | 94.2 |
| 25 | There are 3 people standing in a line. From lef... | ✓ | 30.92 | 0.0152 | 6 | 100.00% | 100.0 |
| 26 | There are 3 people standing in a line. From lef... | ✗ | 30.62 | 0.0207 | 7 | 57.14% | 100.0 |
| 27 | There are 3 people standing in a line. From lef... | ✗ | 58.67 | 0.0211 | 7 | 100.00% | 68.6 |
| 28 | There are 3 people standing in a line. From lef... | ✓ | 25.74 | 0.0292 | 13 | 15.38% | 53.8 |
| 29 | There are 3 people standing in a line. From lef... | ✗ | 51.42 | 0.0233 | 7 | 57.14% | 112.9 |
| 30 | There are 4 people standing in a line. From lef... | ✗ | 33.91 | 0.0201 | 6 | 50.00% | 70.0 |
| 31 | There are 4 people standing in a line. From lef... | ✗ | 21.69 | 0.0183 | 6 | 50.00% | 85.0 |
| 32 | There are 4 people standing in a line. From lef... | ✗ | 62.70 | 0.0315 | 7 | 57.14% | 112.9 |
| 33 | There are 4 people standing in a line. From lef... | ✗ | 70.30 | 0.0214 | 6 | 100.00% | 75.0 |
| 34 | There are 4 people standing in a line. From lef... | ✗ | 6.84 | 0.0062 | 1 | 100.00% | 100.0 |
| 35 | There are 4 people standing in a line. From lef... | ✗ | 40.23 | 0.0202 | 6 | 50.00% | 83.3 |
| 36 | There are 4 people standing in a line. From lef... | ✗ | 531.88 | 0.0937 | 7 | 42.86% | 44.3 |
| 37 | There are 4 people standing in a line. From lef... | ✗ | 39.89 | 0.0224 | 6 | 50.00% | 76.7 |
| 38 | There are 4 people standing in a line. From lef... | ✗ | 24.91 | 0.0205 | 6 | 50.00% | 83.3 |
| 39 | There are 4 people standing in a line. From lef... | ✗ | 52.09 | 0.0229 | 5 | 100.00% | 44.0 |
| 40 | There are 4 people standing in a line. From lef... | ✓ | 36.22 | 0.0178 | 5 | 60.00% | 84.0 |
| 41 | There are 4 people standing in a line. From lef... | ✗ | 43.59 | 0.0269 | 7 | 42.86% | 68.6 |
| 42 | There are 4 people standing in a line. From lef... | ✗ | 27.79 | 0.0187 | 7 | 57.14% | 77.1 |
| 43 | There are 4 people standing in a line. From lef... | ✗ | 24.98 | 0.0230 | 8 | 37.50% | 93.8 |
| 44 | There are 5 people standing in a line. From lef... | ✗ | 23.18 | 0.0199 | 6 | 50.00% | 75.0 |
| 45 | There are 5 people standing in a line. From lef... | ✗ | 42.76 | 0.0202 | 7 | 100.00% | 62.9 |
| 46 | There are 5 people standing in a line. From lef... | ✗ | 20.90 | 0.0280 | 11 | 18.18% | 30.9 |
| 47 | There are 5 people standing in a line. From lef... | ✗ | 41.99 | 0.0277 | 6 | 50.00% | 58.3 |
| 48 | There are 5 people standing in a line. From lef... | ✗ | 55.42 | 0.0232 | 7 | 100.00% | 107.1 |
| 49 | There are 5 people standing in a line. From lef... | ✗ | 28.09 | 0.0194 | 7 | 42.86% | 58.6 |
| 50 | There are 5 people standing in a line. From lef... | ✗ | 76.33 | 0.0352 | 7 | 42.86% | 52.9 |
