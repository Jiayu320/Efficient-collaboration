# 数据集处理报告

## 模型配置

- 小模型: gpt-4.1-mini
- 大模型: gpt-4.1-mini
- 路由模型: gpt-4.1-mini
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/livebench-reasoning-10.json
- 问题总数: 10
- 正确数量: 0
- 准确率: 0.00%
- 平均执行时间: 100.11 秒
- 平均成本: $0.0000

## 任务规划指标

- 平均任务步骤数: 7.50
- 平均压缩比例: 68.42%
- 平均每步骤Token限制: 88.57 tokens

## 理论性能指标

- 平均理论执行时间: 13.260 秒
- 平均顺序执行时间: 20.706 秒
- 平均并行加速比: 1.56x
- 理论与实际执行时间比例: 0.13x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 0.000 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 0.000 秒

### 生成速度
- 小模型平均每秒生成token数: 0.00 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 0.00 tokens/s
- 总平均每秒生成token数: 0.00 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | There are 4 people standing in a line. From lef... | ✗ | 100.45 | 0.0000 | 5 | 100.00% | 110.0 |
| 2 | There are 4 people standing in a line. From lef... | ✗ | 85.63 | 0.0000 | 8 | 62.50% | 65.0 |
| 3 | There are 4 people standing in a line. From lef... | ✗ | 95.48 | 0.0000 | 8 | 62.50% | 98.8 |
| 4 | There are 4 people standing in a line. From lef... | ✗ | 81.39 | 0.0000 | 8 | 62.50% | 70.0 |
| 5 | There are 5 people standing in a line. From lef... | ✗ | 127.14 | 0.0000 | 8 | 62.50% | 72.5 |
| 6 | There are 5 people standing in a line. From lef... | ✗ | 86.40 | 0.0000 | 8 | 62.50% | 70.0 |
| 7 | There are 5 people standing in a line. From lef... | ✗ | 158.24 | 0.0000 | 8 | 62.50% | 90.0 |
| 8 | There are 5 people standing in a line. From lef... | ✗ | 31.01 | 0.0000 | 9 | 66.67% | 82.2 |
| 9 | There are 5 people standing in a line. From lef... | ✗ | 130.38 | 0.0000 | 5 | 80.00% | 136.0 |
| 10 | There are 5 people standing in a line. From lef... | ✗ | 104.98 | 0.0000 | 8 | 62.50% | 91.2 |
