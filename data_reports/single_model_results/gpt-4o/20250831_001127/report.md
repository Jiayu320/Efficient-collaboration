# 单模型数据集处理报告

## 模型信息

- 模型: openai/gpt-4o
- 延迟 (TTFT): 0.735 秒
- 吞吐量: 144.50 tokens/s

## 概述

- 数据集: dataset/original_data/math200.json
- 问题总数: 2
- 正确数量: 1
- 准确率: 50.00%
- 平均执行时间: 10.06 秒
- 平均理论时间: 5.58 秒
- 实际/理论时间比率: 1.80x
- 平均成本: $0.0075

## 性能指标

- 平均首个令牌响应时间 (TTFT): 2.297 秒
- 平均每秒生成token数: 66.43 tokens/s
- 理论每秒生成token数: 144.50 tokens/s
- 实际/理论吞吐量比率: 0.46x

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 理论时间(秒) | 成本($) |
| --- | --- | --- | --- | --- | --- |
| 1 | Three semicircles of radius 1 are constructed o... | ✗ | 8.15 | 3.54 | 0.0050 |
| 2 | What is the distance between the two intersecti... | ✓ | 11.97 | 7.63 | 0.0100 |
