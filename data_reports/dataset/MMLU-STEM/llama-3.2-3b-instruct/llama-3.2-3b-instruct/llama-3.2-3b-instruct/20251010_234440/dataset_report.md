# 数据集处理报告

## 模型配置

- 小模型: meta-llama/llama-3.2-3b-instruct
- 大模型: meta-llama/llama-3.2-3b-instruct
- 路由模型: meta-llama/llama-3.2-3b-instruct
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-STEM.json
- 问题总数: 5
- 正确数量: 2
- 准确率: 40.00%
- 平均执行时间: 24.97 秒
- 平均成本: $0.0000

## 任务规划指标

- 平均任务步骤数: 5.40
- 平均压缩比例: 100.00%
- 平均每步骤Token限制: 32.33 tokens

## 理论性能指标

- 平均理论执行时间: 6.209 秒
- 平均顺序执行时间: 9.203 秒
- 平均并行加速比: 1.54x
- 理论与实际执行时间比例: 0.25x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.807 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 10.908 秒

### 生成速度
- 小模型平均每秒生成token数: 16.97 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 17.95 tokens/s
- 总平均每秒生成token数: 34.92 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Which of these vowels does NOT have a vertical ... | ✗ | 22.62 | 0.0000 | 5 | 100.00% | 15.0 |
| 2 | A species of goose nests on both cliffs and bea... | ✓ | 29.59 | 0.0000 | 5 | 100.00% | 36.0 |
| 3 | Which of the following best describes the struc... | ✓ | 30.27 | 0.0000 | 6 | 100.00% | 20.0 |
| 4 | A drug company will conduct a randomized contro... | ✗ | 20.40 | 0.0000 | 5 | 100.00% | 44.0 |
| 5 | Most of the radiation in Earth’s biosphere is  ... | ✗ | 21.99 | 0.0000 | 6 | 100.00% | 46.7 |
