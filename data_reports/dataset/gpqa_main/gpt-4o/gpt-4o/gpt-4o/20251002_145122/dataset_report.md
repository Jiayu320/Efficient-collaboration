# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: gpt-4o
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 50
- 正确数量: 12
- 准确率: 24.00%
- 平均执行时间: 20.18 秒
- 平均成本: $0.0279

## 任务规划指标

- 平均任务步骤数: 4.66
- 平均压缩比例: 79.53%
- 平均每步骤Token限制: 0.00 tokens

## 理论性能指标

- 平均理论执行时间: 27.469 秒
- 平均顺序执行时间: 38.487 秒
- 平均并行加速比: 1.45x
- 理论与实际执行时间比例: 1.36x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.621 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 9.328 秒

### 生成速度
- 小模型平均每秒生成token数: 67.33 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 14.97 tokens/s
- 总平均每秒生成token数: 82.30 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 19.65 | 0.0168 | 4 | 100.00% | 0.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 18.95 | 0.0237 | 4 | 100.00% | 0.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✓ | 18.80 | 0.0177 | 5 | 100.00% | 0.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 15.39 | 0.0511 | 9 | 22.22% | 0.0 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 17.13 | 0.0209 | 4 | 75.00% | 0.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 15.56 | 0.0195 | 3 | 66.67% | 0.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 20.70 | 0.0198 | 4 | 100.00% | 0.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 21.68 | 0.0309 | 5 | 80.00% | 0.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 19.70 | 0.0245 | 4 | 75.00% | 0.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 16.53 | 0.0222 | 3 | 66.67% | 0.0 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 19.94 | 0.0258 | 4 | 75.00% | 0.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 26.67 | 0.0335 | 6 | 100.00% | 0.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✓ | 23.80 | 0.0331 | 4 | 100.00% | 0.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 28.51 | 0.0333 | 4 | 100.00% | 0.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 23.98 | 0.0219 | 3 | 100.00% | 0.0 |
| 16 | Which of the following statements is a correct ... | ✗ | 19.18 | 0.0169 | 3 | 100.00% | 0.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 19.24 | 0.0201 | 3 | 100.00% | 0.0 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 22.15 | 0.0286 | 4 | 100.00% | 0.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 19.91 | 0.0269 | 5 | 60.00% | 0.0 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 18.89 | 0.0401 | 6 | 50.00% | 0.0 |
| 21 | Why does the hydroboration reaction between a c... | ✗ | 20.66 | 0.0245 | 4 | 75.00% | 0.0 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✗ | 13.79 | 0.0142 | 3 | 100.00% | 0.0 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 12.78 | 0.0140 | 2 | 100.00% | 0.0 |
| 24 | A coating is applied to a substrate resulting i... | ✗ | 24.21 | 0.0377 | 5 | 80.00% | 0.0 |
| 25 | Astronomers are studying two binary star system... | ✗ | 24.05 | 0.0497 | 5 | 60.00% | 0.0 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 14.08 | 0.0089 | 3 | 100.00% | 0.0 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 20.59 | 0.0197 | 4 | 100.00% | 0.0 |
| 28 | In an industrial research lab, a scientist perf... | ✗ | 13.27 | 0.0233 | 5 | 40.00% | 0.0 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 13.72 | 0.0149 | 4 | 75.00% | 0.0 |
| 30 | Among the following exoplanets, which one has t... | ✓ | 17.79 | 0.0267 | 5 | 40.00% | 0.0 |
| 31 | All the following statements about the molecula... | ✗ | 16.64 | 0.0213 | 4 | 75.00% | 0.0 |
| 32 | You are interested in studying a rare type of b... | ✓ | 25.96 | 0.0292 | 4 | 100.00% | 0.0 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 11.85 | 0.0136 | 4 | 75.00% | 0.0 |
| 34 | Measuring stellar inclinations is fundamental i... | ✓ | 24.04 | 0.0300 | 6 | 83.33% | 0.0 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✓ | 24.24 | 0.0257 | 4 | 100.00% | 0.0 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✓ | 28.95 | 0.0312 | 5 | 100.00% | 0.0 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 20.25 | 0.0245 | 4 | 75.00% | 0.0 |
| 38 | Identify the final product produced when cyclob... | ✗ | 21.92 | 0.0216 | 4 | 100.00% | 0.0 |
| 39 | Researchers are attempting to detect transits o... | ✗ | 17.32 | 0.0269 | 5 | 60.00% | 0.0 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 20.88 | 0.0727 | 11 | 27.27% | 0.0 |
| 41 | How many of the following compounds will exhibi... | ✗ | 26.45 | 0.0628 | 10 | 40.00% | 0.0 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 22.86 | 0.0469 | 7 | 57.14% | 0.0 |
| 43 | A paper you are reading about the seesaw mechan... | ✓ | 13.82 | 0.0128 | 3 | 100.00% | 0.0 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 16.10 | 0.0154 | 3 | 100.00% | 0.0 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 39.66 | 0.0450 | 5 | 100.00% | 0.0 |
| 46 | What is the concentration of calcium ions in a ... | ✓ | 20.88 | 0.0253 | 4 | 75.00% | 0.0 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 24.65 | 0.0570 | 9 | 44.44% | 0.0 |
| 48 | Which of the following statements about enhance... | ✗ | 18.26 | 0.0172 | 4 | 100.00% | 0.0 |
| 49 | The Paranal Observatory is situated in Chile at... | ✓ | 17.80 | 0.0380 | 7 | 57.14% | 0.0 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✗ | 15.16 | 0.0184 | 3 | 66.67% | 0.0 |
