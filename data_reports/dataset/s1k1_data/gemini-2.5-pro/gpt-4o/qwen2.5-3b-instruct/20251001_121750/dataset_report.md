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
- 正确数量: 2
- 准确率: 20.00%
- 平均执行时间: 163.15 秒
- 平均成本: $0.0165

## 任务规划指标

- 平均任务步骤数: 6.30
- 平均压缩比例: 62.59%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 54.263 秒
- 平均顺序执行时间: 92.794 秒
- 平均并行加速比: 1.78x
- 理论与实际执行时间比例: 0.33x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 4.787 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 124.328 秒

### 生成速度
- 小模型平均每秒生成token数: 11.73 tokens/s
- 大模型平均每秒生成token数: 5.23 tokens/s
- 路由模型平均每秒生成token数: 0.74 tokens/s
- 总平均每秒生成token数: 17.69 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 137.91 | 0.0125 | 6 | 83.33% | 0.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 216.62 | 0.0145 | 6 | 83.33% | 0.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✓ | 140.90 | 0.0035 | 7 | 71.43% | 0.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 92.83 | 0.0000 | 6 | 50.00% | 0.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 233.39 | 0.0078 | 4 | 50.00% | 0.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 172.48 | 0.0109 | 5 | 80.00% | 0.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 189.20 | 0.0775 | 9 | 44.44% | 0.0 |
| 8 | In a mathematics test number of participants is... | ✗ | 104.38 | 0.0243 | 6 | 50.00% | 0.0 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 181.17 | 0.0065 | 9 | 33.33% | 0.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 162.60 | 0.0074 | 5 | 80.00% | 0.0 |
