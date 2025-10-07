# 单模型数据集处理报告

## 模型信息

- 模型: gpt-4o
- 延迟 (TTFT): 0.735 秒
- 吞吐量: 144.50 tokens/s

## 概述

- 数据集: dataset/TestData/ncb_python_en.json
- 问题总数: 10
- 超时问题数: 0 (0.00%)
- 有效问题数: 10
- 正确数量: 4
- 准确率(有效问题): 40.00%
- 平均执行时间(有效问题): 5.34 秒
- 平均理论时间(有效问题): 2.17 秒
- 实际/理论时间比率: 2.46x
- 平均成本(有效问题): $0.0047

## 性能指标

- 平均首个令牌响应时间 (TTFT): 1.780 秒
- 平均每秒生成token数: 39.37 tokens/s
- 理论每秒生成token数: 144.50 tokens/s
- 实际/理论吞吐量比率: 0.27x

## 详细结果

| # | 问题 | 状态 | 执行时间(秒) | 理论时间(秒) | 成本($) |
| --- | --- | --- | --- | --- | --- |
| 1 | Your task is to generate python code to solve t... | ✓ | 8.21 | 2.11 | 0.0046 |
| 2 | Your task is to generate python code to solve t... | ✓ | 4.55 | 1.72 | 0.0036 |
| 3 | Your task is to generate python code to solve t... | ✗ | 4.67 | 2.76 | 0.0080 |
| 4 | Your task is to generate python code to solve t... | ✓ | 5.19 | 1.87 | 0.0045 |
| 5 | Your task is to generate python code to solve t... | ✗ | 3.96 | 1.34 | 0.0035 |
| 6 | Your task is to generate python code to solve t... | ✓ | 3.85 | 1.65 | 0.0026 |
| 7 | Your task is to generate python code to solve t... | ✗ | 6.37 | 2.32 | 0.0049 |
| 8 | Your task is to generate python code to solve t... | ✗ | 4.97 | 2.66 | 0.0049 |
| 9 | Your task is to generate python code to solve t... | ✗ | 6.58 | 2.78 | 0.0059 |
| 10 | Your task is to generate python code to solve t... | ✗ | 5.09 | 2.53 | 0.0050 |
