# 单模型数据集处理报告

## 模型信息

- 模型: gpt-4.1-mini
- 延迟 (TTFT): 0.700 秒
- 吞吐量: 69.59 tokens/s

## 概述

- 数据集: dataset/TestData/livebench-reasoning.json
- 问题总数: 50
- 超时问题数: 1 (2.00%)
- 有效问题数: 49
- 正确数量: 28
- 准确率(有效问题): 57.14%
- 平均执行时间(有效问题): 90.69 秒
- 平均理论时间(有效问题): 59.00 秒
- 实际/理论时间比率: 1.54x
- 平均成本(有效问题): $0.0067

## 性能指标

- 平均首个令牌响应时间 (TTFT): 3.232 秒
- 平均每秒生成token数: 52.59 tokens/s
- 理论每秒生成token数: 69.59 tokens/s
- 实际/理论吞吐量比率: 0.76x

## 详细结果

| # | 问题 | 状态 | 执行时间(秒) | 理论时间(秒) | 成本($) |
| --- | --- | --- | --- | --- | --- |
| 1 | There are 2 people standing in a line. From lef... | ✓ | 13.31 | 8.56 | 0.0010 |
| 2 | There are 2 people standing in a line. From lef... | ✓ | 12.62 | 13.03 | 0.0015 |
| 3 | There are 2 people standing in a line. From lef... | ✓ | 8.31 | 8.24 | 0.0009 |
| 4 | There are 2 people standing in a line. From lef... | ✓ | 18.70 | 18.76 | 0.0021 |
| 5 | There are 2 people standing in a line. From lef... | ✓ | 8.76 | 6.75 | 0.0008 |
| 6 | There are 2 people standing in a line. From lef... | ✓ | 9.65 | 11.05 | 0.0013 |
| 7 | There are 2 people standing in a line. From lef... | ✓ | 8.90 | 7.77 | 0.0009 |
| 8 | There are 3 people standing in a line. From lef... | ✓ | 27.15 | 23.71 | 0.0027 |
| 9 | There are 3 people standing in a line. From lef... | ✓ | 28.42 | 45.95 | 0.0052 |
| 10 | There are 3 people standing in a line. From lef... | ✗ | 75.94 | 59.65 | 0.0067 |
| 11 | There are 3 people standing in a line. From lef... | ✓ | 31.52 | 21.21 | 0.0024 |
| 12 | There are 3 people standing in a line. From lef... | ✓ | 29.69 | 27.05 | 0.0031 |
| 13 | There are 3 people standing in a line. From lef... | ✓ | 41.70 | 20.57 | 0.0024 |
| 14 | There are 3 people standing in a line. From lef... | ✓ | 39.55 | 31.28 | 0.0036 |
| 15 | There are 3 people standing in a line. From lef... | ✓ | 84.58 | 34.44 | 0.0039 |
| 16 | There are 3 people standing in a line. From lef... | ✓ | 47.75 | 21.09 | 0.0024 |
| 17 | There are 3 people standing in a line. From lef... | ✓ | 24.94 | 24.37 | 0.0028 |
| 18 | There are 3 people standing in a line. From lef... | ✓ | 51.54 | 21.48 | 0.0025 |
| 19 | There are 3 people standing in a line. From lef... | ✓ | 144.45 | 50.76 | 0.0058 |
| 20 | There are 3 people standing in a line. From lef... | ✓ | 30.39 | 37.73 | 0.0043 |
| 21 | There are 3 people standing in a line. From lef... | ✓ | 161.80 | 70.22 | 0.0079 |
| 22 | There are 3 people standing in a line. From lef... | ✓ | 33.33 | 38.16 | 0.0044 |
| 23 | There are 3 people standing in a line. From lef... | ✗ | 123.47 | 112.21 | 0.0126 |
| 24 | There are 3 people standing in a line. From lef... | ✓ | 42.92 | 44.11 | 0.0050 |
| 25 | There are 3 people standing in a line. From lef... | ✗ | 82.02 | 121.11 | 0.0136 |
| 26 | There are 3 people standing in a line. From lef... | ✗ | 225.64 | 94.54 | 0.0107 |
| 27 | There are 3 people standing in a line. From lef... | ✓ | 59.95 | 66.23 | 0.0075 |
| 28 | There are 3 people standing in a line. From lef... | ✓ | 79.39 | 29.09 | 0.0033 |
| 29 | There are 3 people standing in a line. From lef... | ✗ | 54.85 | 61.00 | 0.0069 |
| 30 | There are 4 people standing in a line. From lef... | ✗ | 226.85 | 96.04 | 0.0108 |
| 31 | There are 4 people standing in a line. From lef... | ✗ | 161.96 | 63.60 | 0.0073 |
| 32 | There are 4 people standing in a line. From lef... | ✓ | 222.82 | 71.51 | 0.0081 |
| 33 | There are 4 people standing in a line. From lef... | ✗ | 275.46 | 122.41 | 0.0138 |
| 34 | There are 4 people standing in a line. From lef... | ✗ | 224.47 | 65.19 | 0.0074 |
| 35 | There are 4 people standing in a line. From lef... | ⏱️ 超时 | 302.24 | 0.70 | 0.0000 |
| 36 | There are 4 people standing in a line. From lef... | ✓ | 99.37 | 39.34 | 0.0045 |
| 37 | There are 4 people standing in a line. From lef... | ✓ | 132.90 | 62.79 | 0.0072 |
| 38 | There are 4 people standing in a line. From lef... | ✗ | 68.68 | 67.78 | 0.0077 |
| 39 | There are 4 people standing in a line. From lef... | ✗ | 181.62 | 128.46 | 0.0145 |
| 40 | There are 4 people standing in a line. From lef... | ✓ | 50.00 | 42.06 | 0.0048 |
| 41 | There are 4 people standing in a line. From lef... | ✗ | 81.67 | 101.86 | 0.0116 |
| 42 | There are 4 people standing in a line. From lef... | ✗ | 74.47 | 91.68 | 0.0104 |
| 43 | There are 4 people standing in a line. From lef... | ✗ | 113.45 | 77.88 | 0.0088 |
| 44 | There are 5 people standing in a line. From lef... | ✗ | 128.62 | 75.71 | 0.0087 |
| 45 | There are 5 people standing in a line. From lef... | ✗ | 205.02 | 124.17 | 0.0141 |
| 46 | There are 5 people standing in a line. From lef... | ✗ | 104.70 | 95.14 | 0.0108 |
| 47 | There are 5 people standing in a line. From lef... | ✗ | 118.15 | 100.41 | 0.0116 |
| 48 | There are 5 people standing in a line. From lef... | ✗ | 168.54 | 108.93 | 0.0124 |
| 49 | There are 5 people standing in a line. From lef... | ✗ | 101.73 | 96.81 | 0.0110 |
| 50 | There are 5 people standing in a line. From lef... | ✗ | 101.99 | 129.17 | 0.0146 |
