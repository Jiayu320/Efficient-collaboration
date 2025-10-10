# 单模型数据集处理报告

## 模型信息

- 模型: qwen2.5-3b-instruct
- 延迟 (TTFT): 0.690 秒
- 吞吐量: 64.53 tokens/s

## 概述

- 数据集: dataset/TestData/gsmhardv2.json
- 问题总数: 50
- 超时问题数: 0 (0.00%)
- 有效问题数: 50
- 正确数量: 26
- 准确率(有效问题): 52.00%
- 平均执行时间(有效问题): 34.33 秒
- 平均理论时间(有效问题): 5.90 秒
- 实际/理论时间比率: 5.82x
- 平均成本(有效问题): $0.0000

## 性能指标

- 平均首个令牌响应时间 (TTFT): 1.589 秒
- 平均每秒生成token数: 10.39 tokens/s
- 理论每秒生成token数: 64.53 tokens/s
- 实际/理论吞吐量比率: 0.16x

## 详细结果

| # | 问题 | 状态 | 执行时间(秒) | 理论时间(秒) | 成本($) |
| --- | --- | --- | --- | --- | --- |
| 1 | Janet’s ducks lay 16 eggs per day. She eats thr... | ✗ | 27.26 | 4.04 | 0.0000 |
| 2 | A robe takes 2287720 bolts of blue fiber and ha... | ✓ | 17.75 | 3.73 | 0.0000 |
| 3 | James decides to run 1793815 sprints 1793815 ti... | ✗ | 30.33 | 4.08 | 0.0000 |
| 4 | Every day, Wendi feeds each of her chickens thr... | ✗ | 36.15 | 7.34 | 0.0000 |
| 5 | Kylar went to the store to buy glasses for his ... | ✗ | 36.44 | 6.36 | 0.0000 |
| 6 | Toulouse has twice as many sheep as Charleston.... | ✓ | 39.90 | 6.24 | 0.0000 |
| 7 | Eliza's rate per hour for the first 40 hours sh... | ✓ | 29.61 | 7.21 | 0.0000 |
| 8 | A new program had 531811 downloads in the first... | ✗ | 30.08 | 7.21 | 0.0000 |
| 9 | Toula went to the bakery and bought various typ... | ✗ | 28.41 | 5.87 | 0.0000 |
| 10 | Carlos is planting a lemon tree. The tree will ... | ✗ | 34.03 | 8.84 | 0.0000 |
| 11 | A merchant wants to make a choice of purchase b... | ✓ | 56.80 | 7.85 | 0.0000 |
| 12 | Jill gets paid $20 per hour to teach and $83697... | ✓ | 32.40 | 5.46 | 0.0000 |
| 13 | Claire makes a 6022727 egg omelet every morning... | ✗ | 24.31 | 4.22 | 0.0000 |
| 14 | I have 10 liters of orange drink that are two-t... | ✗ | 51.77 | 10.11 | 0.0000 |
| 15 | Billy sells DVDs. He has 8 customers on Tuesday... | ✗ | 59.37 | 8.35 | 0.0000 |
| 16 | A candle melts by 2 centimeters every hour that... | ✓ | 29.99 | 3.93 | 0.0000 |
| 17 | Marie ordered one chicken meal that costs $12, ... | ✗ | 67.78 | 9.66 | 0.0000 |
| 18 | Mishka bought 3 pairs of shorts, 3 pairs of pan... | ✗ | 29.44 | 6.30 | 0.0000 |
| 19 | Cynthia eats one serving of ice cream every nig... | ✓ | 29.16 | 4.98 | 0.0000 |
| 20 | Henry made two stops during his 60-mile bike tr... | ✓ | 31.42 | 4.21 | 0.0000 |
| 21 | Gloria is shoe shopping when she comes across a... | ✓ | 23.38 | 4.11 | 0.0000 |
| 22 | Darrell and Allen's ages are in the ratio of 7:... | ✓ | 59.72 | 8.70 | 0.0000 |
| 23 | Gunter is trying to count the jelly beans in a ... | ✗ | 48.58 | 6.76 | 0.0000 |
| 24 | John takes care of 1328372 dogs.  Each dog take... | ✓ | 38.14 | 4.29 | 0.0000 |
| 25 | Siobhan has 2 fewer jewels than Aaron. Aaron ha... | ✓ | 15.36 | 3.85 | 0.0000 |
| 26 | John runs 60 miles a week. He runs 3 days a wee... | ✓ | 28.59 | 5.29 | 0.0000 |
| 27 | Dana can run at a rate of speed four times fast... | ✓ | 33.51 | 6.72 | 0.0000 |
| 28 | Brandon's iPhone is four times as old as Ben's ... | ✓ | 16.57 | 3.99 | 0.0000 |
| 29 | Grandma Jones baked 5 apple pies for the firema... | ✓ | 27.78 | 4.60 | 0.0000 |
| 30 | According to its nutritional info, a bag of chi... | ✗ | 29.45 | 6.45 | 0.0000 |
| 31 | Charlie wants to sell beeswax candles.  For eve... | ✓ | 50.52 | 6.28 | 0.0000 |
| 32 | John buys twice as many red ties as blue ties. ... | ✗ | 60.41 | 7.52 | 0.0000 |
| 33 | Richard lives in an apartment building with 676... | ✓ | 14.84 | 6.80 | 0.0000 |
| 34 | Lloyd has an egg farm. His chickens produce 863... | ✗ | 44.39 | 5.59 | 0.0000 |
| 35 | Tom's ship can travel at 10 miles per hour.  He... | ✓ | 23.37 | 3.93 | 0.0000 |
| 36 | Uriah's book bag is getting too heavy for him. ... | ✗ | 54.74 | 11.54 | 0.0000 |
| 37 | The Doubtfire sisters are driving home with 581... | ✓ | 19.01 | 4.08 | 0.0000 |
| 38 | Jean has 30 lollipops. Jean eats 8714250 of the... | ✗ | 24.06 | 3.70 | 0.0000 |
| 39 | Peter plans to go to the movies this week. He a... | ✗ | 35.88 | 5.14 | 0.0000 |
| 40 | A wooden bridge can carry no more than 5000 pou... | ✓ | 33.98 | 5.77 | 0.0000 |
| 41 | Stephen placed an online order for groceries.  ... | ✗ | 19.67 | 3.43 | 0.0000 |
| 42 | A raspberry bush has 6 clusters of 7077300 frui... | ✓ | 22.51 | 3.57 | 0.0000 |
| 43 | A basket contains 6483292 oranges among which 1... | ✗ | 19.69 | 5.12 | 0.0000 |
| 44 | Janet buys a brooch for her daughter.  She pays... | ✗ | 50.92 | 6.13 | 0.0000 |
| 45 | Aleena subscribed to a streaming service that c... | ✓ | 56.62 | 8.00 | 0.0000 |
| 46 | Sophia is thinking of taking a road trip in her... | ✓ | 44.41 | 5.96 | 0.0000 |
| 47 | Jim spends 2 hours watching TV and then decides... | ✓ | 21.68 | 4.53 | 0.0000 |
| 48 | There are four schools competing at a basketbal... | ✗ | 30.06 | 4.98 | 0.0000 |
| 49 | A treasure hunter found a buried treasure chest... | ✓ | 20.76 | 6.38 | 0.0000 |
| 50 | There are twice as many boys as girls at Dr. We... | ✗ | 25.61 | 5.97 | 0.0000 |
