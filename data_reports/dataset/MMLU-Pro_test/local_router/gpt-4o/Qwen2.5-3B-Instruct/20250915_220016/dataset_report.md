# 数据集处理报告

## 模型配置

- 小模型: Qwen/Qwen2.5-3B-Instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-Pro_test.json
- 问题总数: 50
- 正确数量: 29
- 准确率: 58.00%
- 平均执行时间: 12.04 秒
- 平均成本: $0.0013

## 任务规划指标

- 平均任务步骤数: 6.19
- 平均压缩比例: 73.71%
- 平均每步骤Token限制: 24.09 tokens

## 理论性能指标

- 平均理论执行时间: 5.584 秒
- 平均顺序执行时间: 14.786 秒
- 平均并行加速比: 2.63x
- 理论与实际执行时间比例: 0.46x


## 任务分配统计

- 总任务数: 291
- 小模型执行任务数: 20
- 大模型执行任务数: 271
- 小模型任务占比: 6.87%
- 大模型任务占比: 93.13%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 0.623 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 9.641 秒

### 生成速度
- 小模型平均每秒生成token数: 2.90 tokens/s
- 大模型平均每秒生成token数: 2.69 tokens/s
- 路由模型平均每秒生成token数: 30.18 tokens/s
- 总平均每秒生成token数: 35.78 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Typical advertising regulatory bodies suggest, ... | ✗ | 12.99 | 0.0024 | 5 | 100.00% | 34.0 |
| 2 | Managers are entrusted to run the company in th... | ✓ | 10.68 | 0.0020 | 5 | 80.00% | 36.0 |
| 3 | There are two main issues associated with _____... | ✗ | 13.11 | 0.0010 | 8 | 50.00% | 38.8 |
| 4 | _______ locate morality beyond the sphere of ra... | ✓ | 10.12 | 0.0007 | 5 | 60.00% | 33.0 |
| 5 |  Some of key differences between Islamic financ... | ✓ | 11.77 | 0.0008 | 9 | 55.56% | 23.9 |
| 6 |  Which of the following are the three broad gro... | ✓ | 10.30 | 0.0008 | 5 | 80.00% | 28.0 |
| 7 |  Pine and Gilmore (1999) derive four distinct r... | ✓ | 11.92 | 0.0022 | 5 | 100.00% | 38.0 |
| 8 |  Which type of research methods are designed to... | ✓ | 9.22 | 0.0005 | 6 | 66.67% | 21.7 |
| 9 | Where the price is set low relative to the comp... | ✓ | 11.24 | 0.0012 | 5 | 100.00% | 22.0 |
| 10 | Once a train pulls out of a station, or an aero... | ✗ | 14.67 | 0.0021 | 7 | 100.00% | 27.1 |
| 11 | A marketing research firm contracts with client... | ✓ | 9.41 | 0.0007 | 5 | 60.00% | 27.0 |
| 12 | The six dimensions usually considered to consti... | ✗ | 9.07 | 0.0006 | 5 | 60.00% | 23.0 |
| 13 | What is the term for the 'rule of thumb' type o... | ✓ | 9.99 | 0.0013 | 4 | 100.00% | 25.0 |
| 14 | As what is ensuring that one individual does no... | ✗ | 9.31 | 0.0011 | 4 | 100.00% | 23.8 |
| 15 | What theory is built around the principle that ... | ✓ | 11.06 | 0.0020 | 5 | 100.00% | 37.0 |
| 16 | How does lateral communication in an organisati... | ✗ | 12.28 | 0.0013 | 8 | 50.00% | 25.6 |
| 17 | The stock of the CCC Corporation is currently v... | ✗ | 14.04 | 0.0032 | 6 | 83.33% | 34.2 |
| 18 | George is seen to place an even-money $100,000 ... | ✓ | 10.90 | 0.0023 | 5 | 80.00% | 27.0 |
| 19 | Boy Alcott and Jon Buxton are partners in a ste... | ✗ | 14.96 | 0.0013 | 10 | 60.00% | 16.0 |
| 20 | TheAlforsCompany had a beginning inventory of $... | ✓ | 10.07 | 0.0008 | 5 | 80.00% | 18.0 |
| 21 | (a) Given the two discount series of 30-10-2(1/... | ✓ | 24.01 | 0.0029 | 7 | 57.14% | 25.0 |
| 22 | On July 7, Magee Data stock sold at a high of 2... | ✓ | 10.98 | 0.0009 | 6 | 66.67% | 18.3 |
| 23 | During a riot, Mr. Winter's car was overturned ... | ✓ | 10.88 | 0.0014 | 7 | 71.43% | 17.9 |
| 24 | Janet Firestone purchased an option on a stock ... | ✓ | 11.74 | 0.0014 | 8 | 50.00% | 16.2 |
| 25 | Margaret Denault recently rented a truck to dri... | ✗ | 9.92 | 0.0007 | 6 | 50.00% | 17.5 |
| 26 | Where in the balance sheet does each of the fol... | ✗ | 10.55 | 0.0000 | 9 | 33.33% | 23.3 |
| 27 | Prepare a balance sheet for Silvertown Office S... | ✗ | 11.39 | 0.0009 | 7 | 42.86% | 30.0 |
| 28 | What is the net cost of a tape recorder whose l... | ✓ | 8.21 | 0.0006 | 3 | 100.00% | 20.0 |
| 29 | Mr. Frankel wants to borrow $2,000 from Novembe... | ✓ | 10.66 | 0.0000 | 7 | 57.14% | 15.0 |
| 30 | HarryHyppeis paid a straight wage of $2.89 (1/2... | ✗ | 8.72 | 0.0007 | 4 | 100.00% | 17.5 |
| 31 | Steven Moore purchased a new car for $3,462.20,... | ✓ | 9.30 | 0.0006 | 5 | 60.00% | 28.0 |
| 32 | A man sells novelty items for $1.25 each. His c... | ✓ | 12.29 | 0.0028 | 7 | 71.43% | 22.9 |
| 33 | Find the amount to be paid each month in order ... | ✗ | 13.05 | 0.0031 | 7 | 85.71% | 28.6 |
| 34 | Find the break-even point for the cost of produ... | ✗ | 13.45 | 0.0024 | 8 | 75.00% | 20.0 |
| 35 | The tax rate in the town of Centerville is 11(1... | ✓ | 11.65 | 0.0014 | 7 | 85.71% | 21.4 |
| 36 | A man buys a house and lot for $35,000, paying ... | ✗ | 13.72 | 0.0016 | 9 | 66.67% | 19.4 |
| 37 | The Five Star Hotel put down $3,000 worth of ca... | ✗ | 10.69 | 0.0008 | 6 | 66.67% | 22.5 |
| 38 | Mr. Williams owns a piece of property assessed ... | ✓ | 9.76 | 0.0007 | 5 | 80.00% | 15.0 |
| 39 | Joe Troy purchased a chain saw for $1,200 for h... | ✓ | 11.22 | 0.0000 | - | - | - |
| 40 | Mr. Castle will buy one of two 10-HP motors off... | ✗ | 15.58 | 0.0036 | 9 | 66.67% | 21.7 |
| 41 | Determine the number of men needed to build a b... | ✓ | 10.67 | 0.0015 | 4 | 100.00% | 17.5 |
| 42 | Given the above statement, find what would happ... | ✓ | 10.61 | 0.0014 | 5 | 100.00% | 19.0 |
| 43 | How much will it cost to cover a floor 13'6" × ... | ✗ | 11.84 | 0.0016 | 5 | 100.00% | 20.0 |
| 44 | Dermanand Klein are the sole stockholders of th... | ✗ | 9.67 | 0.0000 | 7 | 42.86% | 26.4 |
| 45 | Tom bought a new bicycle for $80. After 4 years... | ✓ | 11.18 | 0.0017 | 5 | 80.00% | 17.0 |
| 46 | A manufacturer can produce a saw for $13 in dir... | ✓ | 7.26 | 0.0000 | - | - | - |
| 47 | Which of the following would yield the greatest... | ✗ | 10.48 | 0.0017 | 5 | 80.00% | 34.0 |
| 48 | The list price of a book is $4.95. It sells in ... | ✓ | 6.68 | 0.0000 | - | - | - |
| 49 | A business started last year with an inventory ... | ✗ | 13.26 | 0.0014 | 7 | 42.86% | 20.7 |
| 50 | Paul Murphy wants to have $10,000 in his accoun... | ✓ | 45.66 | 0.0017 | 9 | 66.67% | 18.3 |
