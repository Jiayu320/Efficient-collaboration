# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: gpt-5
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/AIME24_25.json
- 问题总数: 10
- 正确数量: 2
- 准确率: 20.00%
- 平均执行时间: 143.01 秒
- 平均成本: $0.0246

## 任务规划指标

- 平均任务步骤数: 3.40
- 平均压缩比例: 86.00%
- 平均每步骤Token限制: 94.30 tokens

## 理论性能指标

- 平均理论执行时间: 13.524 秒
- 平均顺序执行时间: 24.388 秒
- 平均并行加速比: 1.74x
- 理论与实际执行时间比例: 0.09x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 16.460 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 45.732 秒

### 生成速度
- 小模型平均每秒生成token数: 1.29 tokens/s
- 大模型平均每秒生成token数: 6.75 tokens/s
- 路由模型平均每秒生成token数: 5.24 tokens/s
- 总平均每秒生成token数: 13.28 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Every morning Aya goes for a $9$-kilometer-long... | ✗ | 137.15 | 0.0244 | 3 | 100.00% | 90.0 |
| 2 | Let $ABC$ be a triangle inscribed in circle $\o... | ✗ | 177.92 | 0.0029 | 0 | 0.00% | 0.0 |
| 3 | Each vertex of a regular octagon is independent... | ✗ | 179.53 | 0.0193 | 3 | 100.00% | 133.3 |
| 4 | Define $f(x)=|| x|-\tfrac{1}{2}|$ and $g(x)=|| ... | ✗ | 205.50 | 0.0494 | 5 | 100.00% | 144.0 |
| 5 | Let $p$ be the least prime number for which the... | ✗ | 188.98 | 0.0349 | 5 | 60.00% | 98.0 |
| 6 | Let $ABCD$ be a tetrahedron such that $AB=CD= \... | ✗ | 228.51 | 0.0359 | 5 | 100.00% | 96.0 |
| 7 | Let $\mathcal{B}$ be the set of rectangular box... | ✗ | 105.36 | 0.0218 | 3 | 100.00% | 113.3 |
| 8 | There exist real numbers $x$ and $y$, both grea... | ✓ | 69.10 | 0.0153 | 3 | 100.00% | 80.0 |
| 9 | Alice and Bob play the following game. A stack ... | ✗ | 74.66 | 0.0211 | 3 | 100.00% | 103.3 |
| 10 | Jen enters a lottery by picking $4$ distinct nu... | ✓ | 63.33 | 0.0207 | 4 | 100.00% | 85.0 |
