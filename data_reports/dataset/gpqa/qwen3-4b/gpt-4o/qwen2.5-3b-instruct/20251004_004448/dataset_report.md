# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: qwen3-4b
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa.json
- 问题总数: 50
- 正确数量: 23
- 准确率: 46.00%
- 平均执行时间: 20.31 秒
- 平均成本: $0.0084

## 任务规划指标

- 平均任务步骤数: 5.02
- 平均压缩比例: 82.23%
- 平均每步骤Token限制: 166.16 tokens

## 理论性能指标

- 平均理论执行时间: 8.698 秒
- 平均顺序执行时间: 11.268 秒
- 平均并行加速比: 1.36x
- 理论与实际执行时间比例: 0.43x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.373 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 12.315 秒

### 生成速度
- 小模型平均每秒生成token数: 2.29 tokens/s
- 大模型平均每秒生成token数: 36.59 tokens/s
- 路由模型平均每秒生成token数: 15.05 tokens/s
- 总平均每秒生成token数: 53.93 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✓ | 10.43 | 0.0043 | 3 | 100.00% | 30.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 9.38 | 0.0012 | 3 | 100.00% | 300.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 7.05 | 0.0018 | 5 | 100.00% | 40.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 16.53 | 0.0160 | 4 | 100.00% | 237.5 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 21.91 | 0.0142 | 4 | 75.00% | 275.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 16.41 | 0.0061 | 5 | 80.00% | 300.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✓ | 14.89 | 0.0054 | 2 | 100.00% | 175.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 11.54 | 0.0029 | 4 | 100.00% | 162.5 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 12.61 | 0.0066 | 4 | 100.00% | 275.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 9.02 | 0.0016 | 5 | 60.00% | 240.0 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 32.49 | 0.0024 | 5 | 60.00% | 21.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 101.45 | 0.0158 | 9 | 55.56% | 123.3 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 21.73 | 0.0188 | 5 | 100.00% | 190.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 33.54 | 0.0105 | 6 | 100.00% | 28.3 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 20.12 | 0.0049 | 5 | 80.00% | 44.0 |
| 16 | Which of the following statements is a correct ... | ✓ | 14.07 | 0.0036 | 4 | 100.00% | 350.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✓ | 27.73 | 0.0114 | 5 | 80.00% | 124.0 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 10.12 | 0.0038 | 4 | 75.00% | 200.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✓ | 31.31 | 0.0064 | 7 | 100.00% | 250.0 |
| 20 | which of the following molecules has c3h symmet... | ✓ | 17.61 | 0.0143 | 6 | 50.00% | 350.0 |
| 21 | Why does the hydroboration reaction between a c... | ✓ | 4.61 | 0.0011 | 5 | 100.00% | 210.0 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✓ | 20.43 | 0.0249 | 7 | 57.14% | 50.0 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 70.99 | 0.0073 | 6 | 66.67% | 40.0 |
| 24 | A coating is applied to a substrate resulting i... | ✗ | 12.99 | 0.0070 | 5 | 100.00% | 320.0 |
| 25 | Astronomers are studying two binary star system... | ✓ | 20.67 | 0.0204 | 6 | 66.67% | 166.7 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 17.84 | 0.0089 | 5 | 100.00% | 320.0 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 8.37 | 0.0040 | 4 | 100.00% | 250.0 |
| 28 | In an industrial research lab, a scientist perf... | ✗ | 9.05 | 0.0088 | 6 | 50.00% | 171.7 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✓ | 7.65 | 0.0018 | 4 | 100.00% | 27.5 |
| 30 | Among the following exoplanets, which one has t... | ✗ | 22.53 | 0.0000 | 3 | 100.00% | 20.0 |
| 31 | All the following statements about the molecula... | ✗ | 18.74 | 0.0155 | 6 | 50.00% | 156.7 |
| 32 | You are interested in studying a rare type of b... | ✓ | 10.93 | 0.0099 | 7 | 57.14% | 25.0 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✓ | 69.30 | 0.0125 | 6 | 66.67% | 13.3 |
| 34 | Measuring stellar inclinations is fundamental i... | ✓ | 18.16 | 0.0123 | 4 | 100.00% | 225.0 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✓ | 22.97 | 0.0094 | 9 | 100.00% | 200.0 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✓ | 10.16 | 0.0030 | 5 | 80.00% | 200.0 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 16.60 | 0.0089 | 4 | 100.00% | 195.0 |
| 38 | Identify the final product produced when cyclob... | ✗ | 15.06 | 0.0075 | 4 | 75.00% | 195.0 |
| 39 | Researchers are attempting to detect transits o... | ✗ | 11.87 | 0.0087 | 6 | 66.67% | 53.3 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 9.49 | 0.0011 | 4 | 100.00% | 225.0 |
| 41 | How many of the following compounds will exhibi... | ✓ | 13.76 | 0.0161 | 5 | 80.00% | 220.0 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 5.71 | 0.0010 | 5 | 100.00% | 250.0 |
| 43 | A paper you are reading about the seesaw mechan... | ✓ | 6.98 | 0.0042 | 5 | 40.00% | 182.0 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 9.17 | 0.0039 | 4 | 100.00% | 262.5 |
| 45 | Consider the extension of the Standard Model gi... | ✓ | 13.83 | 0.0221 | 5 | 60.00% | 290.0 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 23.23 | 0.0153 | 5 | 80.00% | 72.0 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 14.93 | 0.0157 | 5 | 80.00% | 42.0 |
| 48 | Which of the following statements about enhance... | ✗ | 11.30 | 0.0104 | 5 | 60.00% | 22.0 |
| 49 | The Paranal Observatory is situated in Chile at... | ✓ | 11.02 | 0.0063 | 5 | 60.00% | 172.0 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✓ | 67.34 | 0.0000 | 6 | 100.00% | 15.8 |
