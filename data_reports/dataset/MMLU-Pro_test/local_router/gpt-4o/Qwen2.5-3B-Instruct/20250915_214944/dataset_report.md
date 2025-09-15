# 数据集处理报告

## 模型配置

- 小模型: Qwen/Qwen2.5-3B-Instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-Pro_test.json
- 问题总数: 50
- 正确数量: 25
- 准确率: 50.00%
- 平均执行时间: 11.37 秒
- 平均成本: $0.0002

## 任务规划指标

- 平均任务步骤数: 7.24
- 平均压缩比例: 69.09%
- 平均每步骤Token限制: 26.70 tokens

## 理论性能指标

- 平均理论执行时间: 6.896 秒
- 平均顺序执行时间: 18.145 秒
- 平均并行加速比: 2.65x
- 理论与实际执行时间比例: 0.61x


## 任务分配统计

- 总任务数: 123
- 小模型执行任务数: 87
- 大模型执行任务数: 36
- 小模型任务占比: 70.73%
- 大模型任务占比: 29.27%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 0.177 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 10.732 秒

### 生成速度
- 小模型平均每秒生成token数: 25.14 tokens/s
- 大模型平均每秒生成token数: 0.41 tokens/s
- 路由模型平均每秒生成token数: 11.82 tokens/s
- 总平均每秒生成token数: 37.37 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Typical advertising regulatory bodies suggest, ... | ✗ | 2.19 | 0.0000 | - | - | - |
| 2 | Managers are entrusted to run the company in th... | ✗ | 1.36 | 0.0000 | - | - | - |
| 3 | There are two main issues associated with _____... | ✗ | 12.68 | 0.0010 | 6 | 33.33% | 21.7 |
| 4 | _______ locate morality beyond the sphere of ra... | ✓ | 13.09 | 0.0006 | 9 | 55.56% | 27.8 |
| 5 |  Some of key differences between Islamic financ... | ✗ | 12.24 | 0.0000 | 6 | 50.00% | 31.7 |
| 6 |  Which of the following are the three broad gro... | ✗ | 15.01 | 0.0000 | - | - | - |
| 7 |  Pine and Gilmore (1999) derive four distinct r... | ✗ | 13.14 | 0.0020 | 6 | 100.00% | 31.7 |
| 8 |  Which type of research methods are designed to... | ✓ | 11.59 | 0.0000 | - | - | - |
| 9 | Where the price is set low relative to the comp... | ✓ | 9.11 | 0.0000 | - | - | - |
| 10 | Once a train pulls out of a station, or an aero... | ✗ | 11.82 | 0.0000 | - | - | - |
| 11 | A marketing research firm contracts with client... | ✓ | 9.79 | 0.0000 | - | - | - |
| 12 | The six dimensions usually considered to consti... | ✓ | 9.01 | 0.0000 | - | - | - |
| 13 | What is the term for the 'rule of thumb' type o... | ✓ | 12.66 | 0.0000 | - | - | - |
| 14 | As what is ensuring that one individual does no... | ✓ | 7.80 | 0.0000 | 5 | 100.00% | 25.0 |
| 15 | What theory is built around the principle that ... | ✗ | 9.68 | 0.0000 | 7 | 85.71% | 25.7 |
| 16 | How does lateral communication in an organisati... | ✓ | 11.92 | 0.0000 | - | - | - |
| 17 | The stock of the CCC Corporation is currently v... | ✗ | 14.89 | 0.0018 | 9 | 66.67% | 29.4 |
| 18 | George is seen to place an even-money $100,000 ... | ✗ | 16.71 | 0.0021 | 6 | 66.67% | 29.2 |
| 19 | Boy Alcott and Jon Buxton are partners in a ste... | ✗ | 22.49 | 0.0000 | 8 | 62.50% | 28.1 |
| 20 | TheAlforsCompany had a beginning inventory of $... | ✓ | 7.69 | 0.0000 | - | - | - |
| 21 | (a) Given the two discount series of 30-10-2(1/... | ✗ | 13.20 | 0.0000 | 9 | 55.56% | 25.6 |
| 22 | On July 7, Magee Data stock sold at a high of 2... | ✓ | 18.67 | 0.0000 | - | - | - |
| 23 | During a riot, Mr. Winter's car was overturned ... | ✓ | 7.12 | 0.0000 | - | - | - |
| 24 | Janet Firestone purchased an option on a stock ... | ✓ | 9.89 | 0.0000 | - | - | - |
| 25 | Margaret Denault recently rented a truck to dri... | ✗ | 12.83 | 0.0000 | - | - | - |
| 26 | Where in the balance sheet does each of the fol... | ✗ | 9.49 | 0.0000 | - | - | - |
| 27 | Prepare a balance sheet for Silvertown Office S... | ✓ | 12.50 | 0.0000 | - | - | - |
| 28 | What is the net cost of a tape recorder whose l... | ✓ | 7.58 | 0.0000 | - | - | - |
| 29 | Mr. Frankel wants to borrow $2,000 from Novembe... | ✗ | 17.50 | 0.0000 | - | - | - |
| 30 | HarryHyppeis paid a straight wage of $2.89 (1/2... | ✗ | 11.83 | 0.0000 | - | - | - |
| 31 | Steven Moore purchased a new car for $3,462.20,... | ✓ | 7.10 | 0.0000 | - | - | - |
| 32 | A man sells novelty items for $1.25 each. His c... | ✓ | 10.69 | 0.0000 | - | - | - |
| 33 | Find the amount to be paid each month in order ... | ✗ | 20.95 | 0.0000 | 7 | 85.71% | 34.3 |
| 34 | Find the break-even point for the cost of produ... | ✓ | 17.94 | 0.0001 | - | - | - |
| 35 | The tax rate in the town of Centerville is 11(1... | ✓ | 11.96 | 0.0000 | - | - | - |
| 36 | A man buys a house and lot for $35,000, paying ... | ✗ | 13.57 | 0.0000 | 9 | 66.67% | 20.6 |
| 37 | The Five Star Hotel put down $3,000 worth of ca... | ✓ | 9.41 | 0.0000 | - | - | - |
| 38 | Mr. Williams owns a piece of property assessed ... | ✓ | 9.06 | 0.0000 | - | - | - |
| 39 | Joe Troy purchased a chain saw for $1,200 for h... | ✗ | 11.32 | 0.0000 | - | - | - |
| 40 | Mr. Castle will buy one of two 10-HP motors off... | ✗ | 11.81 | 0.0013 | 8 | 62.50% | 20.6 |
| 41 | Determine the number of men needed to build a b... | ✓ | 10.05 | 0.0000 | - | - | - |
| 42 | Given the above statement, find what would happ... | ✗ | 9.32 | 0.0000 | - | - | - |
| 43 | How much will it cost to cover a floor 13'6" × ... | ✗ | 10.04 | 0.0000 | 6 | 83.33% | 21.7 |
| 44 | Dermanand Klein are the sole stockholders of th... | ✗ | 14.98 | 0.0000 | 8 | 62.50% | 30.0 |
| 45 | Tom bought a new bicycle for $80. After 4 years... | ✓ | 9.37 | 0.0000 | - | - | - |
| 46 | A manufacturer can produce a saw for $13 in dir... | ✓ | 6.56 | 0.0000 | - | - | - |
| 47 | Which of the following would yield the greatest... | ✗ | 13.52 | 0.0019 | 9 | 77.78% | 25.0 |
| 48 | The list price of a book is $4.95. It sells in ... | ✓ | 6.03 | 0.0000 | - | - | - |
| 49 | A business started last year with an inventory ... | ✗ | 9.29 | 0.0000 | 5 | 60.00% | 26.0 |
| 50 | Paul Murphy wants to have $10,000 in his accoun... | ✓ | 10.01 | 0.0000 | - | - | - |
