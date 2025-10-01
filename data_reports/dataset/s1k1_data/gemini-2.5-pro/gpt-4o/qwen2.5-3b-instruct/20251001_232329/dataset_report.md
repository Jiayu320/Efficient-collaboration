# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: gemini-2.5-pro
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/s1k1_data.json
- 问题总数: 10
- 正确数量: 3
- 准确率: 30.00%
- 平均执行时间: 145.19 秒
- 平均成本: $0.0216

## 任务规划指标

- 平均任务步骤数: 6.50
- 平均压缩比例: 71.39%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 60.613 秒
- 平均顺序执行时间: 87.230 秒
- 平均并行加速比: 1.48x
- 理论与实际执行时间比例: 0.42x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 4.591 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 106.257 秒

### 生成速度
- 小模型平均每秒生成token数: 9.45 tokens/s
- 大模型平均每秒生成token数: 7.36 tokens/s
- 路由模型平均每秒生成token数: 3.22 tokens/s
- 总平均每秒生成token数: 20.03 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 53.60 | 0.0193 | 6 | 83.33% | 0.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 165.39 | 0.0168 | 5 | 100.00% | 0.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✓ | 118.09 | 0.0103 | 7 | 71.43% | 0.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✓ | 78.97 | 0.0076 | 6 | 50.00% | 0.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 161.88 | 0.0179 | 8 | 62.50% | 0.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 213.04 | 0.0185 | 5 | 80.00% | 0.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 193.18 | 0.0473 | 8 | 37.50% | 0.0 |
| 8 | In a mathematics test number of participants is... | ✗ | 119.13 | 0.0454 | 6 | 66.67% | 0.0 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 153.27 | 0.0184 | 8 | 62.50% | 0.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 195.32 | 0.0149 | 6 | 100.00% | 0.0 |
