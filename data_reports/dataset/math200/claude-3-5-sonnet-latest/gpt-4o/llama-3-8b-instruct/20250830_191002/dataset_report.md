# 数据集处理报告

## 模型配置

- 小模型: meta-llama/llama-3-8b-instruct
- 大模型: gpt-4o
- 路由模型: claude-3-5-sonnet-latest
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/original_data/math200.json
- 问题总数: 2
- 正确数量: 1
- 准确率: 50.00%
- 平均执行时间: 17.94 秒
- 平均成本: $0.0122

## 任务规划指标

- 平均任务步骤数: 5.00
- 平均压缩比例: 79.17%
- 平均每步骤Token限制: 26.67 tokens

## 理论性能指标

- 平均理论执行时间: 5.236 秒
- 平均顺序执行时间: 13.881 秒
- 平均并行加速比: 2.63x
- 理论与实际执行时间比例: 0.29x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 2.791 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 9.567 秒

### 生成速度
- 小模型平均每秒生成token数: 2.37 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 11.57 tokens/s
- 总平均每秒生成token数: 13.94 tokens/s

## 任务分配统计

- 总任务数: 10
- 小模型执行任务数: 6
- 大模型执行任务数: 4
- 小模型任务占比: 60.00%
- 大模型任务占比: 40.00%

### 任务分配详情

| 问题 | 任务ID | 任务描述 | 难度 | 分配模型 |
| --- | --- | --- | --- | --- |
| 1 | 1 | What is the area of the large semicircle of radius 2? | 1 | 小模型 |
| 1 | 2 | What is the area of each small semicircle of radius 1? | 1 | 小模型 |
| 1 | 3 | How many small semicircles are there and what is their total area? | 2 | 小模型 |
| 1 | 4 | What is the formula for finding the shaded area? | 5 | 大模型 |
| 1 | 5 | Calculate the shaded area using the formula? | 5 | 大模型 |
| 1 | 6 | Express the answer in terms of π in simplest radical form? | 5 | 大模型 |
| 2 | 1 | How do we find the points of intersection between y=x^2 and x+y=1? | 2 | 小模型 |
| 2 | 2 | Solve the system of equations to find the coordinates of intersection points? | 3 | 小模型 |
| 2 | 3 | What is the formula for distance between two points in a plane? | 1 | 小模型 |
| 2 | 4 | Calculate the distance between the two intersection points? | 3 | 小模型 |

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Three semicircles of radius 1 are constructed o... | ✓ | 20.50 | 0.0132 | 6 | 83.33% | 23.3 |
| 2 | What is the distance between the two intersecti... | ✗ | 15.38 | 0.0113 | 4 | 75.00% | 30.0 |
