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
- 平均执行时间: 152.28 秒
- 平均成本: $0.0245

## 任务规划指标

- 平均任务步骤数: 6.20
- 平均压缩比例: 65.62%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 55.159 秒
- 平均顺序执行时间: 84.168 秒
- 平均并行加速比: 1.56x
- 理论与实际执行时间比例: 0.36x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 5.155 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 110.075 秒

### 生成速度
- 小模型平均每秒生成token数: 9.95 tokens/s
- 大模型平均每秒生成token数: 7.12 tokens/s
- 路由模型平均每秒生成token数: 2.91 tokens/s
- 总平均每秒生成token数: 19.98 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Given a rational number, write it as a fraction... | ✓ | 77.15 | 0.0220 | 6 | 83.33% | 0.0 |
| 2 | Let  $ \mathcal{H}$  be an infinite-dimensional... | ✗ | 213.60 | 0.0276 | 5 | 100.00% | 0.0 |
| 3 | Find the remainder when $9 \times 99 \times 999... | ✓ | 151.76 | 0.0135 | 7 | 57.14% | 0.0 |
| 4 | Compute the mean molecular speed v in the heavy... | ✗ | 86.62 | 0.0087 | 6 | 50.00% | 0.0 |
| 5 | Two capacitors with capacitance values $C_{1}=2... | ✗ | 182.46 | 0.0220 | 6 | 66.67% | 0.0 |
| 6 | One base of a trapezoid is $100$ units longer t... | ✗ | 148.27 | 0.0163 | 5 | 80.00% | 0.0 |
| 7 | Let's say a language  $L \subseteq \{0,1\}^*$  ... | ✗ | 163.49 | 0.0530 | 6 | 33.33% | 0.0 |
| 8 | In a mathematics test number of participants is... | ✗ | 235.38 | 0.0518 | 7 | 57.14% | 0.0 |
| 9 | Kathy has $5$ red cards and $5$ green cards. Sh... | ✗ | 140.54 | 0.0127 | 7 | 57.14% | 0.0 |
| 10 | Square $AIME$ has sides of length $10$ units.  ... | ✗ | 123.49 | 0.0176 | 7 | 71.43% | 0.0 |
