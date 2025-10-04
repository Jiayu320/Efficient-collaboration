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
- 平均执行时间: 45.41 秒
- 平均成本: $0.0154

## 任务规划指标

- 平均任务步骤数: 4.10
- 平均压缩比例: 75.11%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 31.334 秒
- 平均顺序执行时间: 46.701 秒
- 平均并行加速比: 1.63x
- 理论与实际执行时间比例: 0.69x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.910 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 33.867 秒

### 生成速度
- 小模型平均每秒生成token数: 5.24 tokens/s
- 大模型平均每秒生成token数: 19.26 tokens/s
- 路由模型平均每秒生成token数: 16.74 tokens/s
- 总平均每秒生成token数: 41.24 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 28.62 | 0.0144 | 5 | 40.00% | 0.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 60.70 | 0.0121 | 3 | 66.67% | 0.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✓ | 133.69 | 0.0134 | 5 | 100.00% | 0.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 22.91 | 0.0216 | 9 | 22.22% | 0.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 27.71 | 0.0132 | 3 | 100.00% | 0.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✓ | 19.60 | 0.0173 | 3 | 100.00% | 0.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 22.43 | 0.0179 | 4 | 100.00% | 0.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✓ | 73.58 | 0.0180 | 6 | 66.67% | 0.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 23.92 | 0.0094 | 2 | 100.00% | 0.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 15.63 | 0.0121 | 3 | 66.67% | 0.0 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 22.35 | 0.0156 | 5 | 40.00% | 0.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 99.69 | 0.0111 | 4 | 75.00% | 0.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 82.03 | 0.0186 | 4 | 100.00% | 0.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✓ | 43.07 | 0.0166 | 3 | 100.00% | 0.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 12.60 | 0.0086 | 1 | 100.00% | 0.0 |
| 16 | Which of the following statements is a correct ... | ✗ | 16.30 | 0.0170 | 6 | 33.33% | 0.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✓ | 51.02 | 0.0164 | 3 | 100.00% | 0.0 |
| 18 | You perform a high-throughput experiment on whi... | ✓ | 47.01 | 0.0154 | 3 | 66.67% | 0.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 82.61 | 0.0139 | 4 | 75.00% | 0.0 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 22.80 | 0.0257 | 6 | 50.00% | 0.0 |
