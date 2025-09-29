# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-4B-Thinking/full/ep5
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 50
- 正确数量: 8
- 准确率: 16.00%
- 平均执行时间: 31.65 秒
- 平均成本: $0.0123

## 任务规划指标

- 平均任务步骤数: 4.20
- 平均压缩比例: 82.48%
- 平均每步骤Token限制: 60.37 tokens

## 理论性能指标

- 平均理论执行时间: 4.974 秒
- 平均顺序执行时间: 10.585 秒
- 平均并行加速比: 2.13x
- 理论与实际执行时间比例: 0.16x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.386 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 22.977 秒

### 生成速度
- 小模型平均每秒生成token数: 1.64 tokens/s
- 大模型平均每秒生成token数: 18.60 tokens/s
- 路由模型平均每秒生成token数: 31.52 tokens/s
- 总平均每秒生成token数: 51.76 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 40.41 | 0.0082 | 3 | 100.00% | 60.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 31.58 | 0.0129 | 4 | 75.00% | 60.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 16.55 | 0.0001 | 1 | 100.00% | 30.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 42.71 | 0.0235 | 9 | 22.22% | 58.9 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 48.99 | 0.0169 | 5 | 80.00% | 56.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 31.32 | 0.0168 | 4 | 100.00% | 65.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 23.06 | 0.0132 | 4 | 100.00% | 70.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 41.31 | 0.0113 | 5 | 80.00% | 46.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 25.78 | 0.0081 | 3 | 100.00% | 60.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 27.95 | 0.0136 | 4 | 50.00% | 65.0 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 26.23 | 0.0116 | 4 | 75.00% | 65.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 52.24 | 0.0135 | 6 | 66.67% | 46.7 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✗ | 42.59 | 0.0118 | 3 | 100.00% | 73.3 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 25.56 | 0.0130 | 4 | 100.00% | 60.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✗ | 41.55 | 0.0114 | 3 | 100.00% | 70.0 |
| 16 | Which of the following statements is a correct ... | ✗ | 23.56 | 0.0121 | 4 | 100.00% | 60.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 49.61 | 0.0143 | 4 | 100.00% | 67.5 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 27.82 | 0.0154 | 4 | 75.00% | 57.5 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 61.06 | 0.0145 | 12 | 66.67% | 32.5 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 30.89 | 0.0137 | 4 | 100.00% | 65.0 |
| 21 | Why does the hydroboration reaction between a c... | ✗ | 20.67 | 0.0085 | 3 | 100.00% | 70.0 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✗ | 20.13 | 0.0159 | 5 | 80.00% | 48.0 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 41.50 | 0.0119 | 5 | 60.00% | 48.0 |
| 24 | A coating is applied to a substrate resulting i... | ✗ | 24.78 | 0.0109 | 3 | 100.00% | 66.7 |
| 25 | Astronomers are studying two binary star system... | ✗ | 30.00 | 0.0093 | 5 | 40.00% | 50.0 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 29.14 | 0.0067 | 4 | 75.00% | 60.0 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✓ | 25.24 | 0.0114 | 4 | 100.00% | 65.0 |
| 28 | In an industrial research lab, a scientist perf... | ✗ | 30.61 | 0.0122 | 4 | 75.00% | 70.0 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 33.15 | 0.0084 | 4 | 75.00% | 55.0 |
| 30 | Among the following exoplanets, which one has t... | ✓ | 11.88 | 0.0031 | 1 | 100.00% | 70.0 |
| 31 | All the following statements about the molecula... | ✗ | 20.01 | 0.0100 | 4 | 50.00% | 72.5 |
| 32 | You are interested in studying a rare type of b... | ✓ | 22.66 | 0.0074 | 3 | 100.00% | 66.7 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 31.32 | 0.0111 | 4 | 100.00% | 52.5 |
| 34 | Measuring stellar inclinations is fundamental i... | ✗ | 34.79 | 0.0029 | 4 | 75.00% | 30.0 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 41.30 | 0.0195 | 5 | 100.00% | 68.0 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✗ | 25.62 | 0.0087 | 3 | 100.00% | 70.0 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 31.99 | 0.0134 | 4 | 100.00% | 90.0 |
| 38 | Identify the final product produced when cyclob... | ✗ | 32.05 | 0.0145 | 5 | 100.00% | 68.0 |
| 39 | Researchers are attempting to detect transits o... | ✓ | 25.88 | 0.0140 | 3 | 66.67% | 63.3 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 40.64 | 0.0124 | 3 | 100.00% | 60.0 |
| 41 | How many of the following compounds will exhibi... | ✓ | 47.28 | 0.0206 | 8 | 25.00% | 56.2 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 32.69 | 0.0175 | 5 | 60.00% | 68.0 |
| 43 | A paper you are reading about the seesaw mechan... | ✓ | 16.73 | 0.0048 | 2 | 100.00% | 65.0 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 20.77 | 0.0090 | 3 | 100.00% | 70.0 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 35.73 | 0.0131 | 3 | 66.67% | 63.3 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 22.01 | 0.0102 | 3 | 100.00% | 60.0 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 35.99 | 0.0281 | 6 | 50.00% | 61.7 |
| 48 | Which of the following statements about enhance... | ✗ | 22.98 | 0.0104 | 4 | 75.00% | 60.0 |
| 49 | The Paranal Observatory is situated in Chile at... | ✓ | 22.29 | 0.0186 | 5 | 80.00% | 50.0 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✗ | 42.14 | 0.0132 | 5 | 80.00% | 52.0 |
