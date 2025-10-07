# 数据集处理报告

## 模型配置

- 小模型: meta-llama/llama-3.2-3b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Llama-3.2-1B-Instruct/full/llama_1b_ep1_5e5
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-STEM.json
- 问题总数: 20
- 正确数量: 6
- 准确率: 30.00%
- 平均执行时间: 24.73 秒
- 平均成本: $0.0049

## 任务规划指标

- 平均任务步骤数: 5.55
- 平均压缩比例: 77.68%
- 平均每步骤Token限制: 36.90 tokens

## 理论性能指标

- 平均理论执行时间: 4.590 秒
- 平均顺序执行时间: 8.029 秒
- 平均并行加速比: 1.77x
- 理论与实际执行时间比例: 0.19x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.341 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 14.587 秒

### 生成速度
- 小模型平均每秒生成token数: 25.95 tokens/s
- 大模型平均每秒生成token数: 10.53 tokens/s
- 路由模型平均每秒生成token数: 22.37 tokens/s
- 总平均每秒生成token数: 58.85 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Find the degree for the given field extension Q... | ✗ | 30.07 | 0.0021 | 4 | 100.00% | 40.0 |
| 2 | Let p = (1, 2, 5, 4)(2, 3) in S_5 . Find the in... | ✗ | 7.84 | 0.0000 | 1 | 100.00% | 10.0 |
| 3 | Find all zeros in the indicated finite field of... | ✓ | 33.24 | 0.0009 | 9 | 55.56% | 38.9 |
| 4 | Statement 1 | A factor group of a non-Abelian g... | ✗ | 12.40 | 0.0000 | 3 | 66.67% | 40.0 |
| 5 | Find the product of the given polynomials in th... | ✓ | 95.94 | 0.0233 | 13 | 100.00% | 38.5 |
| 6 | Statement 1 | If a group has an element of orde... | ✗ | 27.53 | 0.0000 | 11 | 45.45% | 25.5 |
| 7 | Statement 1 | Every homomorphic image of a grou... | ✗ | 17.30 | 0.0000 | 3 | 66.67% | 40.0 |
| 8 | Statement 1 | A ring homomorphism is one to one... | ✗ | 17.27 | 0.0016 | 5 | 60.00% | 36.0 |
| 9 | Find the degree for the given field extension Q... | ✗ | 26.44 | 0.0000 | 3 | 100.00% | 26.7 |
| 10 | Find all zeros in the indicated finite field of... | ✓ | 23.97 | 0.0000 | 3 | 100.00% | 30.0 |
| 11 | Statement 1 | If H is a subgroup of G and a bel... | ✗ | 13.02 | 0.0027 | 4 | 100.00% | 37.5 |
| 12 | If A = {1, 2, 3} then relation S = {(1, 1), (2,... | ✗ | 16.90 | 0.0153 | 6 | 66.67% | 65.0 |
| 13 | Find the order of the factor group (Z_11 x Z_15... | ✗ | 19.02 | 0.0000 | 4 | 100.00% | 30.0 |
| 14 | The polynomial x^3 + 2x^2 + 2x + 1 can be facto... | ✗ | 22.18 | 0.0023 | 3 | 100.00% | 46.7 |
| 15 | Find the maximum possible order for an element ... | ✗ | 10.56 | 0.0000 | 3 | 100.00% | 23.3 |
| 16 | Statement 1 | R is a splitting field of some po... | ✗ | 20.97 | 0.0229 | 12 | 25.00% | 45.0 |
| 17 | The inverse of -i in the multiplicative group, ... | ✓ | 26.53 | 0.0000 | 7 | 85.71% | 37.1 |
| 18 | Compute the product in the given ring. (2,3)(3,... | ✓ | 53.70 | 0.0275 | 11 | 81.82% | 55.5 |
| 19 | The set of all real numbers under the usual mul... | ✓ | 14.86 | 0.0000 | 4 | 50.00% | 32.5 |
| 20 | Statement 1| Every group of order p^2 where p i... | ✗ | 4.88 | 0.0000 | 2 | 50.00% | 40.0 |
