# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Thinking/full/train_2025-09-25-23-33-09
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa.json
- 问题总数: 20
- 正确数量: 6
- 准确率: 30.00%
- 平均执行时间: 29.35 秒
- 平均成本: $0.0144

## 任务规划指标

- 平均任务步骤数: 5.10
- 平均压缩比例: 67.65%
- 平均每步骤Token限制: 72.77 tokens

## 理论性能指标

- 平均理论执行时间: 6.300 秒
- 平均顺序执行时间: 11.733 秒
- 平均并行加速比: 1.84x
- 理论与实际执行时间比例: 0.21x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.304 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 20.102 秒

### 生成速度
- 小模型平均每秒生成token数: 4.91 tokens/s
- 大模型平均每秒生成token数: 31.63 tokens/s
- 路由模型平均每秒生成token数: 15.12 tokens/s
- 总平均每秒生成token数: 51.66 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 13.95 | 0.0076 | 3 | 100.00% | 30.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 7.08 | 0.0048 | 1 | 100.00% | 50.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 54.07 | 0.0188 | 9 | 33.33% | 88.9 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 11.13 | 0.0104 | 8 | 12.50% | 50.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 18.28 | 0.0172 | 4 | 50.00% | 27.5 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✓ | 29.17 | 0.0092 | 2 | 100.00% | 60.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 15.22 | 0.0144 | 4 | 100.00% | 72.5 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 16.44 | 0.0203 | 3 | 66.67% | 50.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 13.45 | 0.0130 | 4 | 75.00% | 125.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 16.95 | 0.0156 | 6 | 33.33% | 66.7 |
| 11 | To investigate the causes of a complex genetic ... | ✓ | 35.50 | 0.0140 | 6 | 50.00% | 55.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 121.06 | 0.0084 | 5 | 100.00% | 44.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 40.80 | 0.0212 | 6 | 66.67% | 40.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 16.33 | 0.0194 | 6 | 100.00% | 233.3 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✗ | 9.97 | 0.0071 | 2 | 100.00% | 45.0 |
| 16 | Which of the following statements is a correct ... | ✓ | 18.01 | 0.0191 | 5 | 80.00% | 220.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✓ | 21.37 | 0.0232 | 8 | 75.00% | 60.0 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 23.53 | 0.0142 | 5 | 40.00% | 48.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 48.48 | 0.0258 | 11 | 45.45% | 54.5 |
| 20 | which of the following molecules has c3h symmet... | ✓ | 56.19 | 0.0048 | 4 | 25.00% | 35.0 |
