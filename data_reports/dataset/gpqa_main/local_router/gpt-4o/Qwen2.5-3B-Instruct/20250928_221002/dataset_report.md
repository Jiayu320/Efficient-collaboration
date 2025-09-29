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
- 正确数量: 4
- 准确率: 8.00%
- 平均执行时间: 35.78 秒
- 平均成本: $0.0118

## 任务规划指标

- 平均任务步骤数: 4.40
- 平均压缩比例: 83.54%
- 平均每步骤Token限制: 62.68 tokens

## 理论性能指标

- 平均理论执行时间: 5.264 秒
- 平均顺序执行时间: 11.624 秒
- 平均并行加速比: 2.21x
- 理论与实际执行时间比例: 0.15x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.640 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 25.071 秒

### 生成速度
- 小模型平均每秒生成token数: 1.48 tokens/s
- 大模型平均每秒生成token数: 15.42 tokens/s
- 路由模型平均每秒生成token数: 32.70 tokens/s
- 总平均每秒生成token数: 49.60 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 29.78 | 0.0124 | 4 | 100.00% | 55.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 28.40 | 0.0066 | 3 | 100.00% | 56.7 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 28.28 | 0.0085 | 4 | 100.00% | 52.5 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 37.97 | 0.0312 | 9 | 22.22% | 63.3 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 29.65 | 0.0131 | 3 | 100.00% | 70.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✗ | 53.87 | 0.0073 | 5 | 100.00% | 44.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✗ | 29.74 | 0.0109 | 4 | 100.00% | 67.5 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 25.31 | 0.0077 | 3 | 66.67% | 50.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 30.51 | 0.0058 | 3 | 100.00% | 50.0 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 28.82 | 0.0175 | 6 | 50.00% | 63.3 |
| 11 | To investigate the causes of a complex genetic ... | ✗ | 24.55 | 0.0090 | 3 | 66.67% | 100.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✗ | 60.49 | 0.0065 | 6 | 100.00% | 46.7 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✗ | 29.84 | 0.0065 | 3 | 66.67% | 53.3 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 33.82 | 0.0185 | 5 | 80.00% | 78.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✗ | 41.25 | 0.0129 | 4 | 100.00% | 75.0 |
| 16 | Which of the following statements is a correct ... | ✗ | 26.67 | 0.0117 | 4 | 75.00% | 70.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✗ | 25.89 | 0.0026 | 3 | 100.00% | 43.3 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 26.50 | 0.0069 | 3 | 66.67% | 80.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 39.78 | 0.0199 | 5 | 100.00% | 70.0 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 26.45 | 0.0063 | 3 | 100.00% | 53.3 |
| 21 | Why does the hydroboration reaction between a c... | ✗ | 25.35 | 0.0109 | 4 | 100.00% | 75.0 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✗ | 35.32 | 0.0060 | 4 | 100.00% | 42.5 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 31.14 | 0.0057 | 2 | 100.00% | 70.0 |
| 24 | A coating is applied to a substrate resulting i... | ✗ | 22.43 | 0.0170 | 4 | 100.00% | 60.0 |
| 25 | Astronomers are studying two binary star system... | ✗ | 34.93 | 0.0038 | 3 | 66.67% | 36.7 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 25.67 | 0.0100 | 4 | 100.00% | 72.5 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 30.31 | 0.0110 | 4 | 100.00% | 67.5 |
| 28 | In an industrial research lab, a scientist perf... | ✓ | 22.63 | 0.0113 | 4 | 75.00% | 60.0 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✗ | 60.59 | 0.0099 | 3 | 100.00% | 80.0 |
| 30 | Among the following exoplanets, which one has t... | ✗ | 52.00 | 0.0078 | 5 | 60.00% | 44.0 |
| 31 | All the following statements about the molecula... | ✗ | 72.27 | 0.0115 | 5 | 40.00% | 62.0 |
| 32 | You are interested in studying a rare type of b... | ✗ | 61.02 | 0.0085 | 3 | 100.00% | 70.0 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 57.90 | 0.0086 | 6 | 66.67% | 40.0 |
| 34 | Measuring stellar inclinations is fundamental i... | ✗ | 21.56 | 0.0087 | 5 | 60.00% | 44.0 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✗ | 37.41 | 0.0136 | 4 | 100.00% | 70.0 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✗ | 21.57 | 0.0079 | 3 | 100.00% | 73.3 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✗ | 31.37 | 0.0108 | 4 | 100.00% | 62.5 |
| 38 | Identify the final product produced when cyclob... | ✗ | 32.27 | 0.0110 | 4 | 100.00% | 75.0 |
| 39 | Researchers are attempting to detect transits o... | ✗ | 36.83 | 0.0102 | 4 | 100.00% | 57.5 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 56.46 | 0.0444 | 16 | 25.00% | 65.6 |
| 41 | How many of the following compounds will exhibi... | ✓ | 35.23 | 0.0262 | 8 | 25.00% | 67.5 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 30.42 | 0.0099 | 3 | 100.00% | 83.3 |
| 43 | A paper you are reading about the seesaw mechan... | ✓ | 13.93 | 0.0021 | 1 | 100.00% | 70.0 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✓ | 21.04 | 0.0080 | 3 | 100.00% | 73.3 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 55.84 | 0.0178 | 4 | 75.00% | 85.0 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 34.27 | 0.0106 | 3 | 100.00% | 63.3 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 40.05 | 0.0111 | 6 | 50.00% | 43.3 |
| 48 | Which of the following statements about enhance... | ✗ | 22.69 | 0.0078 | 3 | 100.00% | 60.0 |
| 49 | The Paranal Observatory is situated in Chile at... | ✗ | 69.15 | 0.0299 | 10 | 40.00% | 60.0 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✗ | 39.73 | 0.0146 | 5 | 100.00% | 58.0 |
