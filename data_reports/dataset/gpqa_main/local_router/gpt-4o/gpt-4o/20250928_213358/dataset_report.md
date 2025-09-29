# 数据集处理报告

## 模型配置

- 小模型: gpt-4o
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-4B-Thinking/full/ep5
- 难度阈值: 4
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa_main.json
- 问题总数: 50
- 正确数量: 7
- 准确率: 14.00%
- 平均执行时间: 29.99 秒
- 平均成本: $0.0165

## 任务规划指标

- 平均任务步骤数: 4.52
- 平均压缩比例: 81.34%
- 平均每步骤Token限制: 58.18 tokens

## 理论性能指标

- 平均理论执行时间: 5.169 秒
- 平均顺序执行时间: 11.933 秒
- 平均并行加速比: 2.34x
- 理论与实际执行时间比例: 0.17x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.402 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 20.829 秒

### 生成速度
- 小模型平均每秒生成token数: 20.78 tokens/s
- 大模型平均每秒生成token数: 0.00 tokens/s
- 路由模型平均每秒生成token数: 40.08 tokens/s
- 总平均每秒生成token数: 60.86 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 29.80 | 0.0168 | 5 | 80.00% | 58.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 25.52 | 0.0110 | 3 | 100.00% | 70.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 25.82 | 0.0084 | 3 | 100.00% | 43.3 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 38.78 | 0.0376 | 9 | 22.22% | 63.3 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 27.40 | 0.0133 | 3 | 66.67% | 73.3 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 26.81 | 0.0084 | 2 | 100.00% | 50.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 37.01 | 0.0187 | 6 | 83.33% | 66.7 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 29.92 | 0.0146 | 4 | 100.00% | 45.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 29.31 | 0.0195 | 6 | 50.00% | 55.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 30.40 | 0.0179 | 5 | 40.00% | 62.0 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 30.03 | 0.0185 | 5 | 80.00% | 84.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 35.13 | 0.0256 | 6 | 66.67% | 51.7 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✗ | 37.98 | 0.0249 | 4 | 100.00% | 67.5 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 31.27 | 0.0288 | 5 | 80.00% | 76.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✓ | 25.64 | 0.0119 | 3 | 100.00% | 63.3 |
| 16 | Which of the following statements is a correct ... | ✗ | 33.36 | 0.0182 | 5 | 100.00% | 62.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 30.31 | 0.0150 | 4 | 75.00% | 50.0 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 33.22 | 0.0241 | 5 | 80.00% | 68.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 39.96 | 0.0243 | 8 | 75.00% | 37.5 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 29.76 | 0.0193 | 6 | 66.67% | 71.7 |
| 21 | Why does the hydroboration reaction between a c... | ✗ | 26.32 | 0.0093 | 3 | 100.00% | 70.0 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✗ | 24.73 | 0.0115 | 3 | 100.00% | 56.7 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 30.70 | 0.0199 | 5 | 80.00% | 38.0 |
| 24 | A coating is applied to a substrate resulting i... | ✗ | 30.57 | 0.0127 | 4 | 75.00% | 55.0 |
| 25 | Astronomers are studying two binary star system... | ✗ | 23.79 | 0.0095 | 3 | 66.67% | 23.3 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 22.37 | 0.0086 | 4 | 100.00% | 30.0 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✓ | 29.94 | 0.0091 | 3 | 100.00% | 60.0 |
| 28 | In an industrial research lab, a scientist perf... | ✓ | 26.23 | 0.0155 | 4 | 75.00% | 60.0 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 31.69 | 0.0141 | 4 | 100.00% | 67.5 |
| 30 | Among the following exoplanets, which one has t... | ✓ | 30.51 | 0.0141 | 5 | 60.00% | 44.0 |
| 31 | All the following statements about the molecula... | ✗ | 23.92 | 0.0082 | 5 | 20.00% | 72.0 |
| 32 | You are interested in studying a rare type of b... | ✗ | 29.22 | 0.0149 | 5 | 100.00% | 72.0 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 36.83 | 0.0222 | 4 | 100.00% | 72.5 |
| 34 | Measuring stellar inclinations is fundamental i... | ✗ | 46.16 | 0.0117 | 4 | 75.00% | 32.5 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 32.31 | 0.0148 | 4 | 100.00% | 65.0 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✗ | 25.27 | 0.0115 | 4 | 100.00% | 72.5 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 31.91 | 0.0167 | 5 | 80.00% | 70.0 |
| 38 | Identify the final product produced when cyclob... | ✗ | 29.06 | 0.0129 | 4 | 100.00% | 60.0 |
| 39 | Researchers are attempting to detect transits o... | ✗ | 24.52 | 0.0148 | 4 | 75.00% | 52.5 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 30.68 | 0.0264 | 4 | 100.00% | 72.5 |
| 41 | How many of the following compounds will exhibi... | ✓ | 29.06 | 0.0290 | 8 | 25.00% | 56.2 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 26.15 | 0.0110 | 3 | 100.00% | 70.0 |
| 43 | A paper you are reading about the seesaw mechan... | ✓ | 17.76 | 0.0053 | 2 | 100.00% | 75.0 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 30.49 | 0.0150 | 5 | 100.00% | 56.0 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 33.30 | 0.0201 | 5 | 80.00% | 54.0 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 21.38 | 0.0100 | 3 | 100.00% | 40.0 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 35.61 | 0.0196 | 5 | 60.00% | 32.0 |
| 48 | Which of the following statements about enhance... | ✗ | 25.49 | 0.0144 | 5 | 80.00% | 54.0 |
| 49 | The Paranal Observatory is situated in Chile at... | ✗ | 32.42 | 0.0289 | 8 | 50.00% | 40.0 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✗ | 33.64 | 0.0161 | 4 | 100.00% | 67.5 |
