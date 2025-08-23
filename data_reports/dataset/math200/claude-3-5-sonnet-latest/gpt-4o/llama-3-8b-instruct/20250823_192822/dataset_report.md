# 数据集处理报告

## 模型配置

- 小模型: meta-llama/llama-3-8b-instruct
- 大模型: gpt-4o
- 路由模型: claude-3-5-sonnet-latest
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/original_data/math200.json
- 问题总数: 2
- 正确数量: 0
- 准确率: 0.00%
- 平均执行时间: 27.63 秒
- 平均成本: $0.0000

## 任务规划指标

- 平均任务步骤数: 0.00
- 平均压缩比例: 0.00%
- 平均每步骤Token限制: 0.00 tokens

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
| 1 | Three semicircles of radius 1 are constructed o... | ✗ | 28.32 | 0.0000 | - | - | - |
| 2 | What is the distance between the two intersecti... | ✗ | 26.94 | 0.0000 | - | - | - |
