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
- 正确数量: 6
- 准确率: 30.00%
- 平均执行时间: 48.30 秒
- 平均成本: $0.0210

## 任务规划指标

- 平均任务步骤数: 4.60
- 平均压缩比例: 79.80%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 35.717 秒
- 平均顺序执行时间: 52.174 秒
- 平均并行加速比: 1.55x
- 理论与实际执行时间比例: 0.74x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.247 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 40.142 秒

### 生成速度
- 小模型平均每秒生成token数: 3.35 tokens/s
- 大模型平均每秒生成token数: 17.84 tokens/s
- 路由模型平均每秒生成token数: 29.86 tokens/s
- 总平均每秒生成token数: 51.05 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 47.40 | 0.0180 | 5 | 40.00% | 0.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✓ | 27.90 | 0.0160 | 3 | 100.00% | 0.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 39.82 | 0.0189 | 5 | 100.00% | 0.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 27.94 | 0.0350 | 7 | 42.86% | 0.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 24.99 | 0.0263 | 4 | 75.00% | 0.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✓ | 44.32 | 0.0247 | 5 | 80.00% | 0.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 21.29 | 0.0183 | 3 | 100.00% | 0.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 187.45 | 0.0190 | 5 | 100.00% | 0.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 23.79 | 0.0192 | 4 | 100.00% | 0.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 26.89 | 0.0225 | 3 | 66.67% | 0.0 |
| 11 | To investigate the causes of a complex genetic ... | ✓ | 23.69 | 0.0144 | 3 | 100.00% | 0.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 64.24 | 0.0277 | 7 | 71.43% | 0.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 35.22 | 0.0201 | 3 | 100.00% | 0.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 33.26 | 0.0323 | 4 | 75.00% | 0.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 27.71 | 0.0205 | 4 | 100.00% | 0.0 |
| 16 | Which of the following statements is a correct ... | ✓ | 27.20 | 0.0203 | 4 | 75.00% | 0.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 151.84 | 0.0130 | 4 | 100.00% | 0.0 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 20.09 | 0.0129 | 4 | 100.00% | 0.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 77.61 | 0.0191 | 10 | 30.00% | 0.0 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 33.40 | 0.0219 | 5 | 40.00% | 0.0 |
