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
- 正确数量: 8
- 准确率: 40.00%
- 平均执行时间: 46.75 秒
- 平均成本: $0.0174

## 任务规划指标

- 平均任务步骤数: 4.30
- 平均压缩比例: 78.11%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 32.776 秒
- 平均顺序执行时间: 46.507 秒
- 平均并行加速比: 1.52x
- 理论与实际执行时间比例: 0.70x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.963 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 34.668 秒

### 生成速度
- 小模型平均每秒生成token数: 4.82 tokens/s
- 大模型平均每秒生成token数: 20.45 tokens/s
- 路由模型平均每秒生成token数: 18.63 tokens/s
- 总平均每秒生成token数: 43.90 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✓ | 18.30 | 0.0177 | 5 | 40.00% | 0.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 57.07 | 0.0092 | 5 | 40.00% | 0.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✓ | 74.25 | 0.0173 | 5 | 100.00% | 0.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 41.02 | 0.0188 | 10 | 30.00% | 0.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 26.79 | 0.0223 | 4 | 100.00% | 0.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✓ | 24.44 | 0.0176 | 3 | 100.00% | 0.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 58.47 | 0.0228 | 4 | 100.00% | 0.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✓ | 25.90 | 0.0258 | 5 | 80.00% | 0.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 17.23 | 0.0136 | 3 | 66.67% | 0.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 33.71 | 0.0107 | 3 | 66.67% | 0.0 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 18.22 | 0.0140 | 3 | 66.67% | 0.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 38.33 | 0.0224 | 5 | 100.00% | 0.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 222.67 | 0.0213 | 4 | 100.00% | 0.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 50.09 | 0.0201 | 4 | 100.00% | 0.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 15.84 | 0.0094 | 1 | 100.00% | 0.0 |
| 16 | Which of the following statements is a correct ... | ✗ | 46.46 | 0.0144 | 4 | 100.00% | 0.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✓ | 27.66 | 0.0120 | 2 | 100.00% | 0.0 |
| 18 | You perform a high-throughput experiment on whi... | ✓ | 22.00 | 0.0185 | 4 | 75.00% | 0.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 94.47 | 0.0212 | 7 | 57.14% | 0.0 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 22.10 | 0.0189 | 5 | 40.00% | 0.0 |
