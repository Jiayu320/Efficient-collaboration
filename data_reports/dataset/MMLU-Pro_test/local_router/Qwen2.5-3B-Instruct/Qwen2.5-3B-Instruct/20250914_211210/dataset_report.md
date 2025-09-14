# 数据集处理报告

## 模型配置

- 小模型: Qwen/Qwen2.5-3B-Instruct
- 大模型: Qwen/Qwen2.5-3B-Instruct
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-Pro_test.json
- 问题总数: 100
- 正确数量: 20
- 准确率: 20.00%
- 平均执行时间: 7.08 秒
- 平均成本: $0.0000

## 任务规划指标

- 平均任务步骤数: 6.67
- 平均压缩比例: 65.05%
- 平均每步骤Token限制: 27.28 tokens

## 理论性能指标

- 平均理论执行时间: 6.366 秒
- 平均顺序执行时间: 17.304 秒
- 平均并行加速比: 2.70x
- 理论与实际执行时间比例: 0.90x


## 任务分配统计

- 总任务数: 554
- 小模型执行任务数: 50
- 大模型执行任务数: 504
- 小模型任务占比: 9.03%
- 大模型任务占比: 90.97%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 0.095 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 6.760 秒

### 生成速度
- 小模型平均每秒生成token数: 4.06 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 38.09 tokens/s
- 总平均每秒生成token数: 42.14 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Typical advertising regulatory bodies suggest, ... | ✗ | 6.75 | 0.0000 | 5 | 80.00% | 33.0 |
| 2 | Managers are entrusted to run the company in th... | ✗ | 9.18 | 0.0000 | 9 | 44.44% | 32.8 |
| 3 | There are two main issues associated with _____... | ✗ | 0.55 | 0.0000 | - | - | - |
| 4 | _______ locate morality beyond the sphere of ra... | ✗ | 0.54 | 0.0000 | - | - | - |
| 5 |  Some of key differences between Islamic financ... | ✗ | 6.29 | 0.0000 | 6 | 50.00% | 43.3 |
| 6 |  Which of the following are the three broad gro... | ✓ | 7.79 | 0.0000 | - | - | - |
| 7 |  Pine and Gilmore (1999) derive four distinct r... | ✗ | 4.92 | 0.0000 | 4 | 75.00% | 35.0 |
| 8 |  Which type of research methods are designed to... | ✗ | 0.46 | 0.0000 | - | - | - |
| 9 | Where the price is set low relative to the comp... | ✗ | 0.39 | 0.0000 | - | - | - |
| 10 | Once a train pulls out of a station, or an aero... | ✗ | 0.42 | 0.0000 | - | - | - |
| 11 | A marketing research firm contracts with client... | ✗ | 7.56 | 0.0000 | 7 | 57.14% | 27.1 |
| 12 | The six dimensions usually considered to consti... | ✗ | 8.34 | 0.0000 | 10 | 30.00% | 35.0 |
| 13 | What is the term for the 'rule of thumb' type o... | ✗ | 0.39 | 0.0000 | - | - | - |
| 14 | As what is ensuring that one individual does no... | ✓ | 7.92 | 0.0000 | 9 | 88.89% | 34.4 |
| 15 | What theory is built around the principle that ... | ✗ | 0.34 | 0.0000 | - | - | - |
| 16 | How does lateral communication in an organisati... | ✗ | 7.11 | 0.0000 | 8 | 62.50% | 36.2 |
| 17 | The stock of the CCC Corporation is currently v... | ✗ | 11.17 | 0.0000 | 8 | 62.50% | 31.9 |
| 18 | George is seen to place an even-money $100,000 ... | ✗ | 11.50 | 0.0000 | 7 | 71.43% | 42.1 |
| 19 | Boy Alcott and Jon Buxton are partners in a ste... | ✗ | 6.93 | 0.0000 | 6 | 66.67% | 32.5 |
| 20 | TheAlforsCompany had a beginning inventory of $... | ✗ | 10.88 | 0.0000 | 9 | 66.67% | 28.3 |
| 21 | (a) Given the two discount series of 30-10-2(1/... | ✗ | 8.43 | 0.0000 | 7 | 42.86% | 25.7 |
| 22 | On July 7, Magee Data stock sold at a high of 2... | ✗ | 7.23 | 0.0000 | 6 | 66.67% | 21.7 |
| 23 | During a riot, Mr. Winter's car was overturned ... | ✓ | 7.19 | 0.0000 | 8 | 62.50% | 21.9 |
| 24 | Janet Firestone purchased an option on a stock ... | ✗ | 46.83 | 0.0000 | 9 | 55.56% | 21.7 |
| 25 | Margaret Denault recently rented a truck to dri... | ✗ | 10.60 | 0.0000 | 8 | 50.00% | 21.9 |
| 26 | Where in the balance sheet does each of the fol... | ✗ | 8.07 | 0.0000 | 8 | 50.00% | 27.5 |
| 27 | Prepare a balance sheet for Silvertown Office S... | ✗ | 0.40 | 0.0000 | - | - | - |
| 28 | What is the net cost of a tape recorder whose l... | ✓ | 4.22 | 0.0000 | 3 | 100.00% | 20.0 |
| 29 | Mr. Frankel wants to borrow $2,000 from Novembe... | ✗ | 7.71 | 0.0000 | 7 | 57.14% | 30.0 |
| 30 | HarryHyppeis paid a straight wage of $2.89 (1/2... | ✓ | 5.83 | 0.0000 | 6 | 100.00% | 20.8 |
| 31 | Steven Moore purchased a new car for $3,462.20,... | ✓ | 7.00 | 0.0000 | 8 | 50.00% | 21.2 |
| 32 | A man sells novelty items for $1.25 each. His c... | ✗ | 10.47 | 0.0000 | 7 | 71.43% | 29.3 |
| 33 | Find the amount to be paid each month in order ... | ✗ | 10.49 | 0.0000 | 5 | 80.00% | 35.0 |
| 34 | Find the break-even point for the cost of produ... | ✗ | 10.90 | 0.0000 | 9 | 33.33% | 31.1 |
| 35 | The tax rate in the town of Centerville is 11(1... | ✓ | 11.64 | 0.0000 | 6 | 66.67% | 34.2 |
| 36 | A man buys a house and lot for $35,000, paying ... | ✗ | 13.15 | 0.0000 | 9 | 66.67% | 28.9 |
| 37 | The Five Star Hotel put down $3,000 worth of ca... | ✗ | 6.70 | 0.0000 | 4 | 75.00% | 22.5 |
| 38 | Mr. Williams owns a piece of property assessed ... | ✓ | 5.38 | 0.0000 | 3 | 100.00% | 21.7 |
| 39 | Joe Troy purchased a chain saw for $1,200 for h... | ✗ | 7.25 | 0.0000 | 4 | 75.00% | 27.5 |
| 40 | Mr. Castle will buy one of two 10-HP motors off... | ✗ | 9.89 | 0.0000 | 8 | 50.00% | 27.5 |
| 41 | Determine the number of men needed to build a b... | ✗ | 8.29 | 0.0000 | 7 | 71.43% | 23.6 |
| 42 | Given the above statement, find what would happ... | ✗ | 5.50 | 0.0000 | 4 | 50.00% | 26.2 |
| 43 | How much will it cost to cover a floor 13'6" × ... | ✗ | 9.73 | 0.0000 | 8 | 75.00% | 28.1 |
| 44 | Dermanand Klein are the sole stockholders of th... | ✗ | 8.84 | 0.0000 | 9 | 66.67% | 32.8 |
| 45 | Tom bought a new bicycle for $80. After 4 years... | ✗ | 5.59 | 0.0000 | 6 | 66.67% | 19.2 |
| 46 | A manufacturer can produce a saw for $13 in dir... | ✗ | 4.62 | 0.0000 | 4 | 100.00% | 22.5 |
| 47 | Which of the following would yield the greatest... | ✗ | 8.16 | 0.0000 | 9 | 55.56% | 28.9 |
| 48 | The list price of a book is $4.95. It sells in ... | ✗ | 7.70 | 0.0000 | 7 | 71.43% | 20.7 |
| 49 | A business started last year with an inventory ... | ✗ | 0.43 | 0.0000 | - | - | - |
| 50 | Paul Murphy wants to have $10,000 in his accoun... | ✓ | 6.53 | 0.0000 | 7 | 57.14% | 24.3 |
| 51 | Mr. Torres owns 350 shares of Krescostock payin... | ✓ | 5.60 | 0.0000 | 6 | 66.67% | 19.2 |
| 52 | Assume the following model (from the preceding ... | ✗ | 8.59 | 0.0000 | 7 | 57.14% | 30.0 |
| 53 | The average salary of the Bedford Manufacturing... | ✗ | 6.96 | 0.0000 | 5 | 80.00% | 21.0 |
| 54 | _______ such as bitcoin are becoming increasing... | ✗ | 10.16 | 0.0000 | - | - | - |
| 55 | _______ economy is the term used to describe in... | ✗ | 0.37 | 0.0000 | - | - | - |
| 56 |  The ________ perspective on sustainability res... | ✗ | 7.78 | 0.0000 | 8 | 50.00% | 33.1 |
| 57 | In a business to business context, conflicts of... | ✗ | 5.48 | 0.0000 | 5 | 80.00% | 32.0 |
| 58 | This is a hierarchy of effects or sequential mo... | ✗ | 8.20 | 0.0000 | 10 | 10.00% | 20.0 |
| 59 | The extent to which a service envelops a produc... | ✗ | 8.53 | 0.0000 | 10 | 40.00% | 34.0 |
| 60 | An important characteristic of services is that... | ✓ | 6.79 | 0.0000 | 7 | 57.14% | 32.9 |
| 61 | This is the sharing of meaning created through ... | ✗ | 6.86 | 0.0000 | 7 | 57.14% | 24.3 |
| 62 | Which one is not an element in the primary acti... | ✗ | 5.04 | 0.0000 | 5 | 60.00% | 33.0 |
| 63 | What are characteristics of a programmed decisi... | ✗ | 5.13 | 0.0000 | 5 | 80.00% | 42.0 |
| 64 | Workers' acceptance of change is characteristic... | ✗ | 0.39 | 0.0000 | - | - | - |
| 65 | For a two-period binomial model for stock price... | ✗ | 0.44 | 0.0000 | - | - | - |
| 66 | Let's assume that the 10-year annual return for... | ✓ | 5.43 | 0.0000 | 5 | 60.00% | 24.0 |
| 67 | CheckMate forecasts that its dividend will grow... | ✗ | 9.87 | 0.0000 | 7 | 85.71% | 22.9 |
| 68 | If at the beginning of each month a deposit of ... | ✗ | 5.94 | 0.0000 | 6 | 66.67% | 29.2 |
| 69 | Suppose the demand curve for oPads is given by ... | ✗ | 0.38 | 0.0000 | - | - | - |
| 70 | Suppose a monopoly market has a demand function... | ✗ | 8.38 | 0.0000 | 6 | 83.33% | 28.3 |
| 71 | Mr. Norman Schwartz, age 30, wants to take out ... | ✓ | 7.82 | 0.0000 | 6 | 50.00% | 31.7 |
| 72 | lf 10% and 20% discounts are both given on the"... | ✗ | 6.78 | 0.0000 | 7 | 71.43% | 22.1 |
| 73 | What percent of .65% is .42%?  A. 500% B. 700% ... | ✗ | 0.46 | 0.0000 | - | - | - |
| 74 | A wholesaler was going out of business so he so... | ✗ | 7.08 | 0.0000 | 5 | 100.00% | 26.0 |
| 75 | Pauline DiLorenzo wishes to purchase a store va... | ✗ | 7.67 | 0.0000 | 8 | 50.00% | 23.1 |
| 76 | ABC Corporation shows total assets of $75,000 a... | ✓ | 5.56 | 0.0000 | 5 | 60.00% | 22.0 |
| 77 | Martha Michael spends $360 on her monthly telep... | ✓ | 7.09 | 0.0000 | 5 | 80.00% | 28.0 |
| 78 | a frame house, located in a Class A town, insur... | ✗ | 13.39 | 0.0000 | 7 | 71.43% | 20.7 |
| 79 | George put $500 into an account that bears inte... | ✗ | 6.76 | 0.0000 | 6 | 66.67% | 25.0 |
| 80 | What percent is 131 of 42?  A. 125% B. 294.4% C... | ✗ | 4.21 | 0.0000 | 3 | 100.00% | 35.0 |
| 81 | Ike Waterman and Sean Cole invested $20,000 and... | ✗ | 12.29 | 0.0000 | 9 | 77.78% | 25.0 |
| 82 | An invoice dated March 2 in the amount of $416.... | ✗ | 9.13 | 0.0000 | 9 | 55.56% | 24.4 |
| 83 | Paul Reilly deposited a $5,000 check in his sav... | ✓ | 8.21 | 0.0000 | 9 | 55.56% | 22.2 |
| 84 | With the invoice amount of $190.55, and a disco... | ✗ | 6.22 | 0.0000 | 5 | 80.00% | 22.0 |
| 85 | $ .01(1/4) a share for stocks under $5 a share ... | ✗ | 7.36 | 0.0000 | 6 | 83.33% | 19.2 |
| 86 | New City has an annual budget of $4,221,890.49.... | ✓ | 8.80 | 0.0000 | 8 | 62.50% | 30.6 |
| 87 | A furniture manufacturer wants to find out how ... | ✓ | 6.78 | 0.0000 | 6 | 50.00% | 21.7 |
| 88 | A television sells for $180. It costs the retai... | ✓ | 5.58 | 0.0000 | 5 | 60.00% | 25.0 |
| 89 | Find the total earnings of an employee who earn... | ✗ | 8.09 | 0.0000 | 8 | 75.00% | 23.1 |
| 90 | The Last National Bank has just approved a loan... | ✗ | 5.49 | 0.0000 | 5 | 60.00% | 30.0 |
| 91 | What is the future value obtained When $5,000 i... | ✓ | 6.99 | 0.0000 | 6 | 50.00% | 25.8 |
| 92 | On September 1, Mr. Blake received a statement ... | ✗ | 10.24 | 0.0000 | 9 | 55.56% | 21.7 |
| 93 | Ringling Brothers Circus recently purchased a n... | ✗ | 8.12 | 0.0000 | 7 | 85.71% | 24.3 |
| 94 | The assessed valuation of the taxable property ... | ✗ | 9.07 | 0.0000 | 5 | 60.00% | 28.0 |
| 95 | Florsheimand Co. accepted a 90-day sight draft ... | ✗ | 8.27 | 0.0000 | 9 | 55.56% | 20.6 |
| 96 | TencerInc. has estimated its revenue function t... | ✗ | 5.54 | 0.0000 | 4 | 75.00% | 25.0 |
| 97 | A draft for $800, due in 3 months and bearing i... | ✗ | 8.35 | 0.0000 | 6 | 50.00% | 24.2 |
| 98 | A water bed sells for $330 cash or $40 down and... | ✗ | 8.26 | 0.0000 | 5 | 40.00% | 36.0 |
| 99 | A tomato cannery has 5000 pounds of grade A tom... | ✗ | 0.40 | 0.0000 | - | - | - |
| 100 | In one year Juan earned $30,000. and Don earned... | ✗ | 7.95 | 0.0000 | 8 | 62.50% | 28.1 |
