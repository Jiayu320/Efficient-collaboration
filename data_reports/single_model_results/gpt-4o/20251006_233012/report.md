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
- 平均执行时间(有效问题): 4.89 秒
- 平均理论时间(有效问题): 2.12 秒
- 实际/理论时间比率: 2.31x
- 平均成本(有效问题): $0.0047

## 性能指标

- 平均首个令牌响应时间 (TTFT): 1.743 秒
- 平均每秒生成token数: 40.32 tokens/s
- 理论每秒生成token数: 144.50 tokens/s
- 实际/理论吞吐量比率: 0.28x

## 详细结果

| # | 问题 | 状态 | 执行时间(秒) | 理论时间(秒) | 成本($) |
| --- | --- | --- | --- | --- | --- |
| 1 | Your task is to generate python code to solve t... | ✓ | 5.89 | 2.23 | 0.0047 |
| 2 | Your task is to generate python code to solve t... | ✗ | 4.25 | 1.78 | 0.0037 |
| 3 | Your task is to generate python code to solve t... | ✗ | 5.03 | 2.23 | 0.0072 |
| 4 | Your task is to generate python code to solve t... | ✓ | 4.66 | 2.05 | 0.0048 |
| 5 | Your task is to generate python code to solve t... | ✓ | 4.18 | 1.63 | 0.0039 |
| 6 | Your task is to generate python code to solve t... | ✓ | 4.80 | 2.01 | 0.0031 |
| 7 | Your task is to generate python code to solve t... | ✗ | 5.81 | 2.54 | 0.0053 |
| 8 | Your task is to generate python code to solve t... | ✗ | 4.38 | 2.36 | 0.0045 |
| 9 | Your task is to generate python code to solve t... | ✗ | 6.11 | 2.88 | 0.0061 |
| 10 | Your task is to generate python code to solve t... | ✗ | 3.80 | 1.48 | 0.0035 |
