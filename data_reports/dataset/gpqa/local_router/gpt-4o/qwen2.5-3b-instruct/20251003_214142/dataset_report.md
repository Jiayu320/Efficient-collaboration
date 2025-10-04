# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-4B-Thinking/full/ep5
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa.json
- 问题总数: 20
- 正确数量: 8
- 准确率: 40.00%
- 平均执行时间: 41.79 秒
- 平均成本: $0.0183

## 任务规划指标

- 平均任务步骤数: 5.55
- 平均压缩比例: 85.64%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 44.281 秒
- 平均顺序执行时间: 55.540 秒
- 平均并行加速比: 1.25x
- 理论与实际执行时间比例: 1.06x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.370 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 31.476 秒

### 生成速度
- 小模型平均每秒生成token数: 3.02 tokens/s
- 大模型平均每秒生成token数: 35.95 tokens/s
- 路由模型平均每秒生成token数: 14.88 tokens/s
- 总平均每秒生成token数: 53.86 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 18.63 | 0.0099 | 4 | 100.00% | 0.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✓ | 18.40 | 0.0126 | 3 | 100.00% | 0.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 23.01 | 0.0142 | 5 | 100.00% | 0.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 17.00 | 0.0260 | 4 | 50.00% | 0.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 27.69 | 0.0194 | 5 | 100.00% | 0.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 21.45 | 0.0233 | 5 | 100.00% | 0.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✓ | 17.10 | 0.0148 | 4 | 100.00% | 0.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✓ | 49.72 | 0.0117 | 5 | 80.00% | 0.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 18.75 | 0.0237 | 6 | 83.33% | 0.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 21.22 | 0.0212 | 5 | 80.00% | 0.0 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 41.22 | 0.0123 | 6 | 66.67% | 0.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 167.04 | 0.0196 | 9 | 77.78% | 0.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 56.26 | 0.0266 | 8 | 75.00% | 0.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 21.50 | 0.0249 | 5 | 100.00% | 0.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 20.65 | 0.0180 | 6 | 100.00% | 0.0 |
| 16 | Which of the following statements is a correct ... | ✓ | 13.18 | 0.0118 | 4 | 100.00% | 0.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 179.19 | 0.0096 | 6 | 83.33% | 0.0 |
| 18 | You perform a high-throughput experiment on whi... | ✓ | 16.46 | 0.0167 | 5 | 80.00% | 0.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 73.65 | 0.0296 | 10 | 70.00% | 0.0 |
| 20 | which of the following molecules has c3h symmet... | ✓ | 13.66 | 0.0196 | 6 | 66.67% | 0.0 |
