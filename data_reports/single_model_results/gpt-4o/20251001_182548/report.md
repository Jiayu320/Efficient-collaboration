# 单模型数据集处理报告

## 模型信息

- 模型: gpt-4o
- 延迟 (TTFT): 0.735 秒
- 吞吐量: 144.50 tokens/s

## 概述

- 数据集: dataset/TestData/s1k1_data.json
- 问题总数: 10
- 超时问题数: 0 (0.00%)
- 有效问题数: 10
- 正确数量: 3
- 准确率(有效问题): 30.00%
- 平均执行时间(有效问题): 18.60 秒
- 平均理论时间(有效问题): 5.87 秒
- 实际/理论时间比率: 3.17x
- 平均成本(有效问题): $0.0078

## 性能指标

- 平均首个令牌响应时间 (TTFT): 2.002 秒
- 平均每秒生成token数: 40.77 tokens/s
- 理论每秒生成token数: 144.50 tokens/s
- 实际/理论吞吐量比率: 0.28x

## 详细结果

| # | 问题 | 状态 | 执行时间(秒) | 理论时间(秒) | 成本($) |
| --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✗ | 24.06 | 5.68 | 0.0073 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 13.38 | 5.88 | 0.0078 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✓ | 13.92 | 4.69 | 0.0058 |
| 4 | Compute the mean molecular speed v in the heavy... | ✓ | 12.44 | 4.76 | 0.0059 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✓ | 26.98 | 7.40 | 0.0098 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 17.88 | 7.31 | 0.0097 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 24.89 | 7.87 | 0.0123 |
| 8 | In a mathematics test number of participants is... | ✗ | 23.58 | 6.87 | 0.0093 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 15.67 | 5.29 | 0.0069 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 13.22 | 2.99 | 0.0034 |
