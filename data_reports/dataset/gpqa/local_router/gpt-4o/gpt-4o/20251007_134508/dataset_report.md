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
- 正确数量: 22
- 准确率: 44.00%
- 平均执行时间: 10.89 秒
- 平均成本: $0.0174

## 任务规划指标

- 平均任务步骤数: 4.12
- 平均压缩比例: 73.12%
- 平均每步骤Token限制: 50.74 tokens

## 理论性能指标

- 平均理论执行时间: 4.977 秒
- 平均顺序执行时间: 7.076 秒
- 平均并行加速比: 1.43x
- 理论与实际执行时间比例: 0.46x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.109 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 4.808 秒

### 生成速度
- 小模型平均每秒生成token数: 42.44 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 31.21 tokens/s
- 总平均每秒生成token数: 73.65 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✓ | 13.40 | 0.0150 | 4 | 100.00% | 50.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✓ | 13.10 | 0.0183 | 4 | 100.00% | 35.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 5.96 | 0.0089 | 3 | 33.33% | 43.3 |
| 4 | how many of the following compounds exhibit opt... | ✓ | 14.24 | 0.0241 | 4 | 100.00% | 100.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 13.29 | 0.0196 | 4 | 100.00% | 50.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✓ | 13.81 | 0.0229 | 4 | 100.00% | 50.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 21.19 | 0.0316 | 6 | 100.00% | 51.7 |
| 8 | A spin-half particle is in a linear superpositi... | ✓ | 12.63 | 0.0209 | 3 | 100.00% | 46.7 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 13.78 | 0.0253 | 5 | 80.00% | 50.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 5.98 | 0.0107 | 4 | 25.00% | 52.5 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 12.47 | 0.0198 | 6 | 66.67% | 31.7 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 14.26 | 0.0210 | 4 | 100.00% | 42.5 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 8.57 | 0.0133 | 4 | 50.00% | 37.5 |
| 14 | A quantum mechanical particle of mass m moves i... | ✓ | 12.77 | 0.0194 | 4 | 100.00% | 55.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 6.34 | 0.0109 | 4 | 25.00% | 52.5 |
| 16 | Which of the following statements is a correct ... | ✗ | 9.86 | 0.0155 | 4 | 75.00% | 62.5 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 14.73 | 0.0212 | 4 | 100.00% | 45.0 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 11.47 | 0.0208 | 4 | 75.00% | 80.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 19.23 | 0.0368 | 8 | 62.50% | 40.0 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 6.17 | 0.0080 | 3 | 33.33% | 56.7 |
| 21 | Why does the hydroboration reaction between a c... | ✗ | 6.59 | 0.0090 | 4 | 25.00% | 45.0 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✓ | 6.30 | 0.0118 | 5 | 20.00% | 54.0 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 5.88 | 0.0098 | 4 | 25.00% | 47.5 |
| 24 | A coating is applied to a substrate resulting i... | ✓ | 11.74 | 0.0238 | 4 | 75.00% | 42.5 |
| 25 | Astronomers are studying two binary star system... | ✓ | 11.64 | 0.0186 | 3 | 100.00% | 43.3 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 10.51 | 0.0154 | 4 | 100.00% | 30.0 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 6.92 | 0.0139 | 3 | 33.33% | 60.0 |
| 28 | In an industrial research lab, a scientist perf... | ✓ | 10.12 | 0.0151 | 4 | 100.00% | 55.0 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 10.46 | 0.0138 | 4 | 100.00% | 55.0 |
| 30 | Among the following exoplanets, which one has t... | ✗ | 12.61 | 0.0196 | 4 | 100.00% | 35.0 |
| 31 | All the following statements about the molecula... | ✓ | 9.92 | 0.0168 | 3 | 100.00% | 43.3 |
| 32 | You are interested in studying a rare type of b... | ✓ | 9.86 | 0.0137 | 4 | 100.00% | 52.5 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 16.83 | 0.0274 | 5 | 100.00% | 34.0 |
| 34 | Measuring stellar inclinations is fundamental i... | ✓ | 14.40 | 0.0259 | 4 | 100.00% | 42.5 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 6.01 | 0.0097 | 3 | 33.33% | 60.0 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✗ | 6.08 | 0.0090 | 4 | 25.00% | 37.5 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 14.20 | 0.0252 | 5 | 80.00% | 50.0 |
| 38 | Identify the final product produced when cyclob... | ✗ | 13.52 | 0.0206 | 4 | 100.00% | 62.5 |
| 39 | Researchers are attempting to detect transits o... | ✓ | 14.10 | 0.0258 | 4 | 100.00% | 42.5 |
| 40 | The majority of stars in our Galaxy form and ev... | ✓ | 5.61 | 0.0092 | 4 | 25.00% | 102.5 |
| 41 | How many of the following compounds will exhibi... | ✗ | 11.18 | 0.0181 | 4 | 100.00% | 45.0 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 13.42 | 0.0230 | 5 | 80.00% | 40.0 |
| 43 | A paper you are reading about the seesaw mechan... | ✓ | 8.56 | 0.0111 | 4 | 100.00% | 42.5 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 12.41 | 0.0148 | 4 | 100.00% | 50.0 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 6.92 | 0.0140 | 4 | 25.00% | 117.5 |
| 46 | What is the concentration of calcium ions in a ... | ✓ | 6.05 | 0.0086 | 3 | 33.33% | 40.0 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 6.06 | 0.0099 | 4 | 25.00% | 50.0 |
| 48 | Which of the following statements about enhance... | ✗ | 12.17 | 0.0168 | 4 | 100.00% | 32.5 |
| 49 | The Paranal Observatory is situated in Chile at... | ✓ | 14.86 | 0.0240 | 5 | 100.00% | 40.0 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✓ | 6.08 | 0.0100 | 4 | 25.00% | 52.5 |
