# 数据集处理报告

## 模型配置

- 小模型: meta-llama/llama-3-8b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/original_data/math200.json
- 问题总数: 2
- 正确数量: 1
- 准确率: 50.00%
- 平均执行时间: 15.91 秒
- 平均成本: $0.0009

## 任务规划指标

- 平均任务步骤数: 5.00
- 平均压缩比例: 79.17%
- 平均每步骤Token限制: 25.42 tokens

## 理论性能指标

- 平均理论执行时间: 7.325 秒
- 平均顺序执行时间: 12.080 秒
- 平均并行加速比: 1.65x
- 理论与实际执行时间比例: 0.46x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.149 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 11.846 秒

### 生成速度
- 小模型平均每秒生成token数: 0.08 tokens/s
- 大模型平均每秒生成token数: 1.20 tokens/s
- 路由模型平均每秒生成token数: 5.68 tokens/s
- 总平均每秒生成token数: 6.96 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Three semicircles of radius 1 are constructed o... | ✗ | 19.38 | 0.0012 | 6 | 83.33% | 25.8 |
| 2 | What is the distance between the two intersecti... | ✓ | 12.44 | 0.0006 | 4 | 75.00% | 25.0 |
