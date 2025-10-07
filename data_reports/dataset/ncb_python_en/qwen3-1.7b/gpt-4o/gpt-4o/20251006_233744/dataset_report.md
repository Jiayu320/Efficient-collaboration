# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: qwen3-1.7b
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/ncb_python_en.json
- 问题总数: 10
- 正确数量: 1
- 准确率: 10.00%
- 平均执行时间: 15.81 秒
- 平均成本: $0.0193

## 任务规划指标

- 平均任务步骤数: 4.20
- 平均压缩比例: 100.00%
- 平均每步骤Token限制: 63.83 tokens

## 理论性能指标

- 平均理论执行时间: 5.887 秒
- 平均顺序执行时间: 6.621 秒
- 平均并行加速比: 1.12x
- 理论与实际执行时间比例: 0.37x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.335 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 7.585 秒

### 生成速度
- 小模型平均每秒生成token数: 61.73 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 11.76 tokens/s
- 总平均每秒生成token数: 73.49 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Your task is to generate python code to solve t... | ✗ | 20.13 | 0.0126 | 3 | 100.00% | 76.7 |
| 2 | Your task is to generate python code to solve t... | ✗ | 13.17 | 0.0165 | 4 | 100.00% | 40.0 |
| 3 | Your task is to generate python code to solve t... | ✗ | 22.58 | 0.0340 | 6 | 100.00% | 63.3 |
| 4 | Your task is to generate python code to solve t... | ✓ | 11.24 | 0.0140 | 3 | 100.00% | 50.0 |
| 5 | Your task is to generate python code to solve t... | ✗ | 10.53 | 0.0103 | 3 | 100.00% | 86.7 |
| 6 | Your task is to generate python code to solve t... | ✗ | 11.42 | 0.0099 | 4 | 100.00% | 50.0 |
| 7 | Your task is to generate python code to solve t... | ✗ | 12.27 | 0.0147 | 3 | 100.00% | 70.0 |
| 8 | Your task is to generate python code to solve t... | ✗ | 21.24 | 0.0294 | 6 | 100.00% | 28.3 |
| 9 | Your task is to generate python code to solve t... | ✗ | 26.52 | 0.0427 | 7 | 100.00% | 90.0 |
| 10 | Your task is to generate python code to solve t... | ✗ | 9.05 | 0.0088 | 3 | 100.00% | 83.3 |
