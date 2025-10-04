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
- 正确数量: 9
- 准确率: 45.00%
- 平均执行时间: 44.07 秒
- 平均成本: $0.0179

## 任务规划指标

- 平均任务步骤数: 4.70
- 平均压缩比例: 73.03%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 31.840 秒
- 平均顺序执行时间: 49.111 秒
- 平均并行加速比: 1.66x
- 理论与实际执行时间比例: 0.72x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.908 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 31.266 秒

### 生成速度
- 小模型平均每秒生成token数: 5.33 tokens/s
- 大模型平均每秒生成token数: 24.26 tokens/s
- 路由模型平均每秒生成token数: 18.51 tokens/s
- 总平均每秒生成token数: 48.11 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✓ | 20.22 | 0.0157 | 5 | 40.00% | 0.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 77.64 | 0.0174 | 5 | 60.00% | 0.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 83.50 | 0.0099 | 5 | 100.00% | 0.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 16.12 | 0.0298 | 9 | 22.22% | 0.0 |
| 5 | A coating is applied to a substrate resulting i... | ✓ | 28.53 | 0.0151 | 3 | 100.00% | 0.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 22.34 | 0.0208 | 3 | 100.00% | 0.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✓ | 27.08 | 0.0184 | 4 | 100.00% | 0.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 98.56 | 0.0194 | 5 | 80.00% | 0.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 52.57 | 0.0139 | 5 | 60.00% | 0.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✓ | 18.25 | 0.0198 | 4 | 75.00% | 0.0 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 35.03 | 0.0149 | 4 | 75.00% | 0.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 109.17 | 0.0149 | 4 | 100.00% | 0.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 23.22 | 0.0220 | 4 | 100.00% | 0.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✓ | 17.64 | 0.0157 | 3 | 100.00% | 0.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✗ | 56.26 | 0.0166 | 5 | 40.00% | 0.0 |
| 16 | Which of the following statements is a correct ... | ✓ | 16.58 | 0.0140 | 4 | 75.00% | 0.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✓ | 25.04 | 0.0141 | 3 | 100.00% | 0.0 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 73.31 | 0.0196 | 5 | 40.00% | 0.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 53.25 | 0.0190 | 5 | 60.00% | 0.0 |
| 20 | which of the following molecules has c3h symmet... | ✓ | 27.01 | 0.0268 | 9 | 33.33% | 0.0 |
