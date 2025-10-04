# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: gpt-4o
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa.json
- 问题总数: 20
- 正确数量: 7
- 准确率: 35.00%
- 平均执行时间: 19.77 秒
- 平均成本: $0.0227

## 任务规划指标

- 平均任务步骤数: 4.60
- 平均压缩比例: 74.13%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 25.505 秒
- 平均顺序执行时间: 39.549 秒
- 平均并行加速比: 1.64x
- 理论与实际执行时间比例: 1.29x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.906 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 7.228 秒

### 生成速度
- 小模型平均每秒生成token数: 42.74 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 27.23 tokens/s
- 总平均每秒生成token数: 69.97 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 15.90 | 0.0160 | 5 | 40.00% | 0.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✓ | 15.90 | 0.0180 | 3 | 66.67% | 0.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✓ | 18.10 | 0.0204 | 5 | 100.00% | 0.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 18.04 | 0.0330 | 10 | 30.00% | 0.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 25.68 | 0.0242 | 3 | 100.00% | 0.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✓ | 27.32 | 0.0266 | 4 | 100.00% | 0.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 21.66 | 0.0219 | 4 | 100.00% | 0.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✓ | 22.66 | 0.0341 | 5 | 80.00% | 0.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 17.83 | 0.0197 | 4 | 75.00% | 0.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 16.31 | 0.0189 | 3 | 66.67% | 0.0 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 15.93 | 0.0167 | 5 | 40.00% | 0.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 26.18 | 0.0282 | 5 | 80.00% | 0.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 21.04 | 0.0253 | 4 | 100.00% | 0.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 19.18 | 0.0210 | 3 | 100.00% | 0.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 16.77 | 0.0143 | 3 | 100.00% | 0.0 |
| 16 | Which of the following statements is a correct ... | ✓ | 16.88 | 0.0140 | 4 | 50.00% | 0.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 24.21 | 0.0248 | 3 | 100.00% | 0.0 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 19.41 | 0.0299 | 7 | 42.86% | 0.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 22.68 | 0.0288 | 7 | 71.43% | 0.0 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 13.69 | 0.0179 | 5 | 40.00% | 0.0 |
