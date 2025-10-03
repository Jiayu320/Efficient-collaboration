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
- 正确数量: 10
- 准确率: 50.00%
- 平均执行时间: 18.72 秒
- 平均成本: $0.0199

## 任务规划指标

- 平均任务步骤数: 3.75
- 平均压缩比例: 100.00%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 29.756 秒
- 平均顺序执行时间: 31.101 秒
- 平均并行加速比: 1.04x
- 理论与实际执行时间比例: 1.59x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.616 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 9.441 秒

### 生成速度
- 小模型平均每秒生成token数: 44.35 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 12.80 tokens/s
- 总平均每秒生成token数: 57.15 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 17.66 | 0.0125 | 3 | 100.00% | 0.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✓ | 15.58 | 0.0167 | 3 | 100.00% | 0.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 11.64 | 0.0096 | 3 | 100.00% | 0.0 |
| 4 | how many of the following compounds exhibit opt... | ✓ | 36.67 | 0.0558 | 8 | 100.00% | 0.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 19.33 | 0.0175 | 3 | 100.00% | 0.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✓ | 20.51 | 0.0209 | 4 | 100.00% | 0.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✓ | 20.68 | 0.0203 | 4 | 100.00% | 0.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✓ | 18.58 | 0.0249 | 4 | 100.00% | 0.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 18.32 | 0.0137 | 3 | 100.00% | 0.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 12.22 | 0.0131 | 3 | 100.00% | 0.0 |
| 11 | To investigate the causes of a complex genetic ... | ✓ | 12.66 | 0.0082 | 3 | 100.00% | 0.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 19.93 | 0.0242 | 4 | 100.00% | 0.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 24.31 | 0.0318 | 5 | 100.00% | 0.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 19.63 | 0.0231 | 4 | 100.00% | 0.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 13.96 | 0.0109 | 3 | 100.00% | 0.0 |
| 16 | Which of the following statements is a correct ... | ✓ | 12.20 | 0.0086 | 3 | 100.00% | 0.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 19.48 | 0.0190 | 3 | 100.00% | 0.0 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 17.64 | 0.0187 | 3 | 100.00% | 0.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 20.63 | 0.0188 | 3 | 100.00% | 0.0 |
| 20 | which of the following molecules has c3h symmet... | ✓ | 22.69 | 0.0299 | 6 | 100.00% | 0.0 |
