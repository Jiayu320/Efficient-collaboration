# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: saves/Llama-3.2-1B-Instruct/full/Llama-3-2-1B_ep5
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa.json
- 问题总数: 50
- 正确数量: 20
- 准确率: 40.00%
- 平均执行时间: 13.55 秒
- 平均成本: $0.0184

## 任务规划指标

- 平均任务步骤数: 4.27
- 平均压缩比例: 76.63%
- 平均每步骤Token限制: 50.79 tokens

## 理论性能指标

- 平均理论执行时间: 5.128 秒
- 平均顺序执行时间: 7.277 秒
- 平均并行加速比: 1.44x
- 理论与实际执行时间比例: 0.38x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.484 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 5.123 秒

### 生成速度
- 小模型平均每秒生成token数: 41.06 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 25.96 tokens/s
- 总平均每秒生成token数: 67.02 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✓ | 19.52 | 0.0161 | 4 | 100.00% | 40.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✓ | 24.77 | 0.0179 | 4 | 100.00% | 27.5 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 7.35 | 0.0087 | 3 | 33.33% | 43.3 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 15.80 | 0.0195 | 4 | 100.00% | 42.5 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 7.20 | 0.0097 | 4 | 25.00% | 45.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 0.00 | 0.0000 | - | - | - |
| 7 | aniline is heated with sulfuric acid, forming p... | ✓ | 23.78 | 0.0271 | 6 | 100.00% | 48.3 |
| 8 | A spin-half particle is in a linear superpositi... | ✓ | 21.50 | 0.0242 | 4 | 100.00% | 42.5 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 13.65 | 0.0089 | 4 | 25.00% | 37.5 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 8.19 | 0.0110 | 4 | 25.00% | 55.0 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 14.68 | 0.0177 | 6 | 66.67% | 43.3 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 20.27 | 0.0275 | 5 | 80.00% | 44.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 22.04 | 0.0272 | 4 | 100.00% | 75.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✓ | 21.16 | 0.0261 | 4 | 100.00% | 50.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 13.08 | 0.0205 | 5 | 60.00% | 48.0 |
| 16 | Which of the following statements is a correct ... | ✓ | 8.98 | 0.0096 | 4 | 25.00% | 57.5 |
| 17 | The universe is filled with the Cosmic Microwav... | ✓ | 21.95 | 0.0205 | 4 | 100.00% | 42.5 |
| 18 | You perform a high-throughput experiment on whi... | ✓ | 16.04 | 0.0256 | 5 | 60.00% | 40.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 25.85 | 0.0315 | 6 | 83.33% | 33.3 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 17.17 | 0.0173 | 4 | 100.00% | 57.5 |
| 21 | Why does the hydroboration reaction between a c... | ✗ | 8.33 | 0.0090 | 4 | 25.00% | 57.5 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✓ | 9.15 | 0.0116 | 5 | 20.00% | 58.0 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 14.58 | 0.0217 | 3 | 100.00% | 50.0 |
| 24 | A coating is applied to a substrate resulting i... | ✗ | 6.75 | 0.0097 | 4 | 25.00% | 50.0 |
| 25 | Astronomers are studying two binary star system... | ✗ | 17.43 | 0.0210 | 4 | 100.00% | 45.0 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 11.07 | 0.0156 | 4 | 100.00% | 35.0 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 12.34 | 0.0217 | 3 | 100.00% | 56.7 |
| 28 | In an industrial research lab, a scientist perf... | ✓ | 8.59 | 0.0129 | 3 | 100.00% | 63.3 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 5.80 | 0.0093 | 4 | 25.00% | 47.5 |
| 30 | Among the following exoplanets, which one has t... | ✗ | 12.65 | 0.0192 | 4 | 100.00% | 35.0 |
| 31 | All the following statements about the molecula... | ✗ | 11.41 | 0.0231 | 5 | 60.00% | 52.0 |
| 32 | You are interested in studying a rare type of b... | ✓ | 5.89 | 0.0096 | 4 | 25.00% | 57.5 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 10.47 | 0.0226 | 4 | 75.00% | 45.0 |
| 34 | Measuring stellar inclinations is fundamental i... | ✓ | 13.40 | 0.0219 | 4 | 100.00% | 42.5 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 19.93 | 0.0294 | 6 | 100.00% | 105.0 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✓ | 6.52 | 0.0098 | 5 | 20.00% | 38.0 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 11.24 | 0.0155 | 4 | 100.00% | 62.5 |
| 38 | Identify the final product produced when cyclob... | ✗ | 12.03 | 0.0151 | 4 | 100.00% | 50.0 |
| 39 | Researchers are attempting to detect transits o... | ✗ | 10.36 | 0.0178 | 4 | 75.00% | 47.5 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 15.48 | 0.0253 | 4 | 100.00% | 102.5 |
| 41 | How many of the following compounds will exhibi... | ✓ | 12.12 | 0.0185 | 4 | 100.00% | 47.5 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 14.02 | 0.0175 | 4 | 100.00% | 50.0 |
| 43 | A paper you are reading about the seesaw mechan... | ✓ | 8.56 | 0.0103 | 4 | 100.00% | 37.5 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 11.23 | 0.0167 | 5 | 80.00% | 46.0 |
| 45 | Consider the extension of the Standard Model gi... | ✓ | 15.29 | 0.0283 | 4 | 100.00% | 100.0 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 14.46 | 0.0222 | 4 | 100.00% | 50.0 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 14.23 | 0.0322 | 4 | 75.00% | 37.5 |
| 48 | Which of the following statements about enhance... | ✗ | 12.59 | 0.0229 | 6 | 66.67% | 56.7 |
| 49 | The Paranal Observatory is situated in Chile at... | ✗ | 16.11 | 0.0262 | 4 | 100.00% | 40.0 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✓ | 12.44 | 0.0174 | 4 | 100.00% | 50.0 |
