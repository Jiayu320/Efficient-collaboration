# 数据集处理报告

## 模型配置

- 小模型: gpt-4.1-mini
- 大模型: gpt-4.1-mini
- 路由模型: qwen3-4b
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/MMLU-Pro_test.json
- 问题总数: 50
- 正确数量: 35
- 准确率: 70.00%
- 平均执行时间: 18.82 秒
- 平均成本: $0.0016

## 任务规划指标

- 平均任务步骤数: 4.18
- 平均压缩比例: 93.23%
- 平均每步骤Token限制: 40.33 tokens

## 理论性能指标

- 平均理论执行时间: 5.906 秒
- 平均顺序执行时间: 7.109 秒
- 平均并行加速比: 1.21x
- 理论与实际执行时间比例: 0.31x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 2.066 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 5.955 秒

### 生成速度
- 小模型平均每秒生成token数: 23.39 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 11.03 tokens/s
- 总平均每秒生成token数: 34.41 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Bob writes down a number between 1 and 1,000. M... | ✓ | 12.12 | 0.0009 | 3 | 100.00% | 30.0 |
| 2 | A supplier of ink for printers sent the followi... | ✓ | 14.33 | 0.0012 | 3 | 100.00% | 46.7 |
| 3 | Peter bought a typewriter for $125, less a 5% d... | ✓ | 23.09 | 0.0011 | 5 | 80.00% | 30.0 |
| 4 | Using the tables of standard electrode potentia... | ✓ | 17.67 | 0.0016 | 4 | 100.00% | 45.0 |
| 5 | The gypsy moth produces a natural attractant, C... | ✓ | 28.54 | 0.0030 | 5 | 100.00% | 34.0 |
| 6 | Liquid nitrogen is an excellent bath for keepin... | ✓ | 20.87 | 0.0019 | 4 | 100.00% | 35.0 |
| 7 | A student has recently completed a dissertation... | ✓ | 11.17 | 0.0008 | 3 | 100.00% | 40.0 |
| 8 | On May 2, a woman mailed the following letter t... | ✗ | 13.03 | 0.0017 | 5 | 60.00% | 38.0 |
| 9 | A certain load to be driven at 1750 r/min requi... | ✓ | 13.95 | 0.0008 | 4 | 100.00% | 33.8 |
| 10 | The difference between dc and ac in electric ci... | ✗ | 8.05 | 0.0004 | 3 | 100.00% | 43.3 |
| 11 | At 10:00p. m. onNovember 14, a driver was opera... | ✗ | 13.61 | 0.0013 | 4 | 100.00% | 55.0 |
| 12 | When focused on a star, the distance of the eye... | ✓ | 31.13 | 0.0033 | 6 | 83.33% | 33.3 |
| 13 | What do we mean when we say that the farm probl... | ✓ | 15.80 | 0.0009 | 4 | 75.00% | 47.5 |
| 14 | Using the table below , find the federal income... | ✓ | 26.55 | 0.0018 | 5 | 100.00% | 38.0 |
| 15 | AlforsMotors is purchasing some new European ca... | ✓ | 19.70 | 0.0013 | 4 | 100.00% | 37.5 |
| 16 | A company created a new brand of pies. However,... | ✗ | 18.29 | 0.0011 | 4 | 100.00% | 52.5 |
| 17 | TheRydberg- Ritz equation governing the spectra... | ✗ | 19.38 | 0.0027 | 4 | 75.00% | 45.0 |
| 18 | Glucose-1-phosphate, essential to the metabolis... | ✓ | 19.08 | 0.0016 | 4 | 100.00% | 27.5 |
| 19 | A group of hikers climbed from Salt Flats (elev... | ✓ | 10.96 | 0.0007 | 4 | 100.00% | 27.5 |
| 20 | The speed of sound is slightly greater on a  A.... | ✓ | 12.85 | 0.0010 | 5 | 80.00% | 48.0 |
| 21 | Company A is currently trading at $150 per shar... | ✓ | 12.86 | 0.0008 | 4 | 100.00% | 26.2 |
| 22 | What is the impedance of a 1-henry inductor at ... | ✗ | 20.61 | 0.0013 | 4 | 100.00% | 35.0 |
| 23 | In a hypothetical environment, fishes called pi... | ✓ | 17.77 | 0.0016 | 5 | 80.00% | 44.0 |
| 24 | Air entering a tube of diameter 5.08cm (2 in.) ... | ✗ | 43.89 | 0.0043 | 6 | 83.33% | 40.0 |
| 25 |  Select the best English interpretation of the ... | ✓ | 19.76 | 0.0023 | 5 | 80.00% | 42.0 |
| 26 | A 360° journal bearing 3 in.long,carries a 4 in... | ✗ | 54.02 | 0.0077 | 5 | 100.00% | 48.0 |
| 27 | A heavy rock and a light rock in free fall (zer... | ✓ | 14.86 | 0.0010 | 4 | 100.00% | 40.0 |
| 28 | Marginal cost (MC) is equal to average variable... | ✓ | 10.82 | 0.0007 | 3 | 100.00% | 43.3 |
| 29 | Assume all gases are perfect unless stated othe... | ✓ | 19.20 | 0.0012 | 4 | 100.00% | 35.0 |
| 30 | Suppose an American firm sells a large piece of... | ✓ | 21.22 | 0.0008 | 4 | 100.00% | 22.5 |
| 31 | Assume the half-life of the proton is 10^33 yea... | ✓ | 22.69 | 0.0021 | 5 | 80.00% | 36.0 |
| 32 | This question refers to the following informati... | ✗ | 27.77 | 0.0009 | 4 | 100.00% | 40.0 |
| 33 | John Wilson retired at age 62 with average year... | ✗ | 25.26 | 0.0024 | 4 | 100.00% | 47.5 |
| 34 | One's ability to make inferences about the beha... | ✓ | 10.80 | 0.0005 | 3 | 100.00% | 50.0 |
| 35 | Air inside a chamber is heated from an initial ... | ✓ | 25.20 | 0.0024 | 4 | 100.00% | 40.0 |
| 36 | Why is it that in the United States, labor cons... | ✗ | 14.17 | 0.0009 | 4 | 75.00% | 57.5 |
| 37 | A 2008 survey showed that what percentage of th... | ✓ | 9.28 | 0.0004 | 3 | 100.00% | 36.7 |
| 38 | This question refers to the following informati... | ✗ | 11.36 | 0.0010 | 4 | 100.00% | 52.5 |
| 39 | While driving to school, Elise hears about a co... | ✓ | 12.48 | 0.0005 | 4 | 100.00% | 30.0 |
| 40 | Two narrow slits separated by $0.10 \mathrm{~mm... | ✓ | 19.80 | 0.0022 | 6 | 83.33% | 30.0 |
| 41 | What is the 'security dilemma' that faces weak ... | ✓ | 17.36 | 0.0009 | 3 | 100.00% | 60.0 |
| 42 | A farmer owned a 40-acre tract of farmland loca... | ✓ | 11.77 | 0.0016 | 3 | 66.67% | 50.0 |
| 43 | A condominium development consists of two build... | ✗ | 12.16 | 0.0012 | 4 | 100.00% | 45.0 |
| 44 | A deficiency of which vitamin has been associat... | ✓ | 10.00 | 0.0006 | 4 | 100.00% | 37.5 |
| 45 | An appliance store was using part of a public a... | ✗ | 19.76 | 0.0019 | 5 | 60.00% | 44.0 |
| 46 | A 25-year-old man is brought to the emergency d... | ✗ | 22.87 | 0.0013 | 5 | 100.00% | 50.0 |
| 47 | The dominant course for foreign policy througho... | ✓ | 15.54 | 0.0009 | 4 | 100.00% | 37.5 |
| 48 | What is the percentage of angular magnification... | ✓ | 17.32 | 0.0016 | 4 | 100.00% | 42.5 |
| 49 | An equilibrium solution of the complex ion Ag(N... | ✓ | 38.63 | 0.0043 | 5 | 100.00% | 40.0 |
| 50 | Good-day Tire Company wishes to find out its co... | ✓ | 11.61 | 0.0006 | 4 | 100.00% | 26.2 |
