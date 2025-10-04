# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: gpt-4o
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa.json
- 问题总数: 20
- 正确数量: 7
- 准确率: 35.00%
- 平均执行时间: 62.03 秒
- 平均成本: $0.0154

## 任务规划指标

- 平均任务步骤数: 6.95
- 平均压缩比例: 68.67%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 51.424 秒
- 平均顺序执行时间: 84.077 秒
- 平均并行加速比: 1.70x
- 理论与实际执行时间比例: 0.83x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.716 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 46.852 秒

### 生成速度
- 小模型平均每秒生成token数: 10.83 tokens/s
- 大模型平均每秒生成token数: 18.44 tokens/s
- 路由模型平均每秒生成token数: 6.38 tokens/s
- 总平均每秒生成token数: 35.66 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✓ | 38.84 | 0.0094 | 5 | 40.00% | 0.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 67.23 | 0.0053 | 4 | 100.00% | 0.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 39.24 | 0.0151 | 6 | 100.00% | 0.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 82.14 | 0.0075 | 11 | 36.36% | 0.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 30.10 | 0.0151 | 5 | 80.00% | 0.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✓ | 31.83 | 0.0197 | 5 | 100.00% | 0.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✓ | 26.73 | 0.0196 | 5 | 100.00% | 0.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 84.33 | 0.0205 | 7 | 57.14% | 0.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 68.18 | 0.0174 | 8 | 50.00% | 0.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 27.34 | 0.0106 | 4 | 75.00% | 0.0 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 43.60 | 0.0269 | 10 | 40.00% | 0.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 116.36 | 0.0188 | 8 | 62.50% | 0.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✗ | 111.20 | 0.0142 | 5 | 100.00% | 0.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 85.42 | 0.0277 | 7 | 85.71% | 0.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 47.17 | 0.0129 | 6 | 66.67% | 0.0 |
| 16 | Which of the following statements is a correct ... | ✓ | 13.68 | 0.0135 | 7 | 42.86% | 0.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 24.23 | 0.0142 | 4 | 100.00% | 0.0 |
| 18 | You perform a high-throughput experiment on whi... | ✓ | 45.85 | 0.0235 | 15 | 20.00% | 0.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✓ | 194.72 | 0.0106 | 10 | 60.00% | 0.0 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 62.47 | 0.0063 | 7 | 57.14% | 0.0 |
