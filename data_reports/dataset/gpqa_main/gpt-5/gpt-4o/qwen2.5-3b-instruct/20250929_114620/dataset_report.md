# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: gpt-5
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 50
- 正确数量: 7
- 准确率: 14.00%
- 平均执行时间: 72.86 秒
- 平均成本: $0.0230

## 任务规划指标

- 平均任务步骤数: 2.76
- 平均压缩比例: 95.15%
- 平均每步骤Token限制: 175.42 tokens

## 理论性能指标

- 平均理论执行时间: 15.121 秒
- 平均顺序执行时间: 27.211 秒
- 平均并行加速比: 1.83x
- 理论与实际执行时间比例: 0.21x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 10.679 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 26.391 秒

### 生成速度
- 小模型平均每秒生成token数: 1.03 tokens/s
- 大模型平均每秒生成token数: 10.35 tokens/s
- 路由模型平均每秒生成token数: 11.27 tokens/s
- 总平均每秒生成token数: 22.65 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 54.16 | 0.0152 | 2 | 100.00% | 185.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 61.16 | 0.0308 | 5 | 80.00% | 90.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 70.48 | 0.0171 | 3 | 100.00% | 83.3 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 65.25 | 0.0244 | 3 | 100.00% | 196.7 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 97.99 | 0.0396 | 4 | 100.00% | 135.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 49.67 | 0.0096 | 2 | 100.00% | 0.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✓ | 84.95 | 0.0218 | 2 | 100.00% | 235.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 106.37 | 0.0172 | 4 | 100.00% | 72.5 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 46.34 | 0.0139 | 1 | 100.00% | 250.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 57.45 | 0.0297 | 3 | 100.00% | 200.0 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 44.32 | 0.0208 | 2 | 100.00% | 235.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 83.47 | 0.0342 | 5 | 100.00% | 86.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✗ | 62.11 | 0.0239 | 3 | 100.00% | 126.7 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 52.84 | 0.0277 | 4 | 75.00% | 60.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 44.07 | 0.0263 | 4 | 100.00% | 110.0 |
| 16 | Which of the following statements is a correct ... | ✗ | 38.50 | 0.0122 | 1 | 100.00% | 300.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 57.40 | 0.0195 | 2 | 100.00% | 100.0 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 83.99 | 0.0222 | 2 | 100.00% | 265.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 68.16 | 0.0303 | 4 | 75.00% | 140.0 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 62.64 | 0.0167 | 1 | 100.00% | 700.0 |
| 21 | Why does the hydroboration reaction between a c... | ✗ | 71.67 | 0.0259 | 3 | 100.00% | 173.3 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✗ | 49.42 | 0.0297 | 4 | 100.00% | 105.0 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 59.44 | 0.0210 | 3 | 66.67% | 73.3 |
| 24 | A coating is applied to a substrate resulting i... | ✗ | 46.63 | 0.0170 | 2 | 100.00% | 75.0 |
| 25 | Astronomers are studying two binary star system... | ✗ | 51.14 | 0.0268 | 3 | 100.00% | 126.7 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 24.86 | 0.0068 | 2 | 100.00% | 0.0 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 74.75 | 0.0177 | 1 | 100.00% | 450.0 |
| 28 | In an industrial research lab, a scientist perf... | ✗ | 51.00 | 0.0161 | 1 | 100.00% | 450.0 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 128.66 | 0.0237 | 3 | 100.00% | 140.0 |
| 30 | Among the following exoplanets, which one has t... | ✓ | 53.25 | 0.0192 | 2 | 100.00% | 150.0 |
| 31 | All the following statements about the molecula... | ✗ | 45.46 | 0.0126 | 2 | 100.00% | 270.0 |
| 32 | You are interested in studying a rare type of b... | ✗ | 49.18 | 0.0141 | 1 | 100.00% | 350.0 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✓ | 119.99 | 0.0255 | 4 | 100.00% | 95.0 |
| 34 | Measuring stellar inclinations is fundamental i... | ✗ | 55.22 | 0.0231 | 3 | 100.00% | 106.7 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 82.38 | 0.0232 | 2 | 100.00% | 285.0 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✗ | 68.07 | 0.0303 | 4 | 75.00% | 165.0 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 104.35 | 0.0214 | 2 | 100.00% | 225.0 |
| 38 | Identify the final product produced when cyclob... | ✗ | 75.88 | 0.0341 | 5 | 100.00% | 178.0 |
| 39 | Researchers are attempting to detect transits o... | ✗ | 53.98 | 0.0224 | 2 | 100.00% | 135.0 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 128.67 | 0.0312 | 3 | 100.00% | 240.0 |
| 41 | How many of the following compounds will exhibi... | ✓ | 171.71 | 0.0212 | 3 | 100.00% | 130.0 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 79.16 | 0.0229 | 2 | 100.00% | 300.0 |
| 43 | A paper you are reading about the seesaw mechan... | ✓ | 58.79 | 0.0093 | 1 | 100.00% | 60.0 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 57.44 | 0.0161 | 2 | 100.00% | 120.0 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 164.66 | 0.0682 | 7 | 85.71% | 220.0 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 55.30 | 0.0328 | 4 | 100.00% | 95.0 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 79.19 | 0.0195 | 3 | 100.00% | 66.7 |
| 48 | Which of the following statements about enhance... | ✗ | 65.84 | 0.0236 | 2 | 100.00% | 300.0 |
| 49 | The Paranal Observatory is situated in Chile at... | ✗ | 114.28 | 0.0050 | 0 | 0.00% | 0.0 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✗ | 111.42 | 0.0349 | 5 | 100.00% | 116.0 |
