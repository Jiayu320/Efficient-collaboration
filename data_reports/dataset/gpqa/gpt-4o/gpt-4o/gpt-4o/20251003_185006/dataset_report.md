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
- 正确数量: 11
- 准确率: 55.00%
- 平均执行时间: 19.58 秒
- 平均成本: $0.0262

## 任务规划指标

- 平均任务步骤数: 7.20
- 平均压缩比例: 61.97%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 32.817 秒
- 平均顺序执行时间: 57.870 秒
- 平均并行加速比: 1.90x
- 理论与实际执行时间比例: 1.68x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.938 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 2.624 秒

### 生成速度
- 小模型平均每秒生成token数: 60.44 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 16.23 tokens/s
- 总平均每秒生成token数: 76.67 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✓ | 12.58 | 0.0117 | 5 | 40.00% | 0.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✓ | 16.89 | 0.0165 | 4 | 100.00% | 0.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 23.97 | 0.0260 | 9 | 66.67% | 0.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 19.33 | 0.0464 | 11 | 36.36% | 0.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 8.80 | 0.0085 | 7 | 57.14% | 0.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✓ | 24.23 | 0.0261 | 6 | 100.00% | 0.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✓ | 29.74 | 0.0212 | 5 | 100.00% | 0.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✓ | 20.80 | 0.0308 | 8 | 50.00% | 0.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 18.43 | 0.0374 | 11 | 36.36% | 0.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 15.93 | 0.0184 | 4 | 75.00% | 0.0 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 9.28 | 0.0087 | 6 | 50.00% | 0.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 25.00 | 0.0414 | 9 | 55.56% | 0.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 24.48 | 0.0376 | 7 | 71.43% | 0.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✓ | 38.88 | 0.0422 | 9 | 88.89% | 0.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 15.58 | 0.0188 | 5 | 60.00% | 0.0 |
| 16 | Which of the following statements is a correct ... | ✓ | 15.31 | 0.0164 | 7 | 42.86% | 0.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✓ | 15.62 | 0.0168 | 5 | 80.00% | 0.0 |
| 18 | You perform a high-throughput experiment on whi... | ✓ | 20.89 | 0.0380 | 11 | 36.36% | 0.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 22.77 | 0.0357 | 8 | 50.00% | 0.0 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 13.02 | 0.0247 | 7 | 42.86% | 0.0 |
