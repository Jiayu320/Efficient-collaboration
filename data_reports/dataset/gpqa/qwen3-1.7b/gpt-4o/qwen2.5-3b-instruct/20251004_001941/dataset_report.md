# 数据集处理报告

## 模型配置

- 小模型: qwen2.5-3b-instruct
- 大模型: gpt-4o
- 路由模型: qwen3-1.7b
- 难度阈值: 5
- 工作线程数: 10

## 概述

- 数据集: dataset/TestData/gpqa.json
- 问题总数: 50
- 正确数量: 18
- 准确率: 36.00%
- 平均执行时间: 13.66 秒
- 平均成本: $0.0042

## 任务规划指标

- 平均任务步骤数: 4.58
- 平均压缩比例: 86.29%
- 平均每步骤Token限制: 56.75 tokens

## 理论性能指标

- 平均理论执行时间: 5.416 秒
- 平均顺序执行时间: 6.929 秒
- 平均并行加速比: 1.31x
- 理论与实际执行时间比例: 0.40x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.160 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 8.064 秒

### 生成速度
- 小模型平均每秒生成token数: 2.73 tokens/s
- 大模型平均每秒生成token数: 28.57 tokens/s
- 路由模型平均每秒生成token数: 19.28 tokens/s
- 总平均每秒生成token数: 50.57 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A large gene has dozens of exons, of which the ... | ✗ | 23.15 | 0.0000 | 4 | 25.00% | 10.0 |
| 2 | Two quantum states with energies E1 and E2 have... | ✗ | 6.36 | 0.0018 | 3 | 100.00% | 10.0 |
| 3 | trans-cinnamaldehyde was treated with methylmag... | ✗ | 10.22 | 0.0018 | 4 | 100.00% | 100.0 |
| 4 | how many of the following compounds exhibit opt... | ✗ | 8.07 | 0.0034 | 8 | 25.00% | 212.5 |
| 5 | A coating is applied to a substrate resulting i... | ✗ | 16.70 | 0.0135 | 3 | 66.67% | 40.0 |
| 6 | Consider the following metric:  ds^{2}=\frac{32... | ✓ | 10.87 | 0.0069 | 2 | 100.00% | 20.0 |
| 7 | aniline is heated with sulfuric acid, forming p... | ✓ | 4.61 | 0.0009 | 4 | 100.00% | 100.0 |
| 8 | A spin-half particle is in a linear superpositi... | ✗ | 8.68 | 0.0047 | 3 | 100.00% | 100.0 |
| 9 | In a parallel universe where a magnet can have ... | ✗ | 31.54 | 0.0073 | 6 | 83.33% | 21.7 |
| 10 | In a cycloaddition reaction, two π systems comb... | ✗ | 13.79 | 0.0049 | 3 | 66.67% | 26.7 |
| 11 | To investigate the causes of a complex genetic ... | ✓ | 5.00 | 0.0006 | 5 | 100.00% | 10.0 |
| 12 | We would like to dissolve (at 25°С) 0.1 g Fe(OH... | ✓ | 8.17 | 0.0019 | 4 | 100.00% | 20.0 |
| 13 | Calculate the eigenvector of a quantum mechanic... | ✗ | 13.05 | 0.0045 | 4 | 100.00% | 100.0 |
| 14 | A quantum mechanical particle of mass m moves i... | ✗ | 16.27 | 0.0000 | 9 | 100.00% | 60.0 |
| 15 | Scientist 1 is studying linkage maps in Drosoph... | ✗ | 5.21 | 0.0007 | 6 | 100.00% | 25.0 |
| 16 | Which of the following statements is a correct ... | ✓ | 4.49 | 0.0010 | 4 | 100.00% | 200.0 |
| 17 | The universe is filled with the Cosmic Microwav... | ✓ | 12.88 | 0.0048 | 2 | 100.00% | 10.0 |
| 18 | You perform a high-throughput experiment on whi... | ✗ | 22.50 | 0.0027 | 10 | 40.00% | 10.0 |
| 19 | When 49 g of KClO3 decomposes, the resulting O2... | ✗ | 25.08 | 0.0353 | 13 | 46.15% | 10.0 |
| 20 | which of the following molecules has c3h symmet... | ✗ | 6.93 | 0.0025 | 4 | 100.00% | 100.0 |
| 21 | Why does the hydroboration reaction between a c... | ✓ | 9.08 | 0.0037 | 4 | 100.00% | 100.0 |
| 22 | Let an infinite plate, with conductivity sigma,... | ✗ | 17.50 | 0.0079 | 3 | 100.00% | 23.3 |
| 23 | In the last few decades, reverberation mapping,... | ✗ | 13.31 | 0.0000 | 5 | 100.00% | 226.0 |
| 24 | A coating is applied to a substrate resulting i... | ✗ | 8.69 | 0.0003 | 4 | 100.00% | 40.0 |
| 25 | Astronomers are studying two binary star system... | ✓ | 6.78 | 0.0021 | 4 | 75.00% | 10.0 |
| 26 | The experimental proof for the chromosomal theo... | ✗ | 6.75 | 0.0028 | 2 | 100.00% | 10.0 |
| 27 | "Scientist aims to analyze 200 nucleotides that... | ✗ | 6.47 | 0.0038 | 1 | 100.00% | 100.0 |
| 28 | In an industrial research lab, a scientist perf... | ✓ | 26.07 | 0.0000 | 6 | 100.00% | 10.0 |
| 29 | A chemist performed a reaction on 2,3-diphenylb... | ✓ | 5.39 | 0.0004 | 3 | 100.00% | 10.0 |
| 30 | Among the following exoplanets, which one has t... | ✗ | 8.65 | 0.0050 | 5 | 60.00% | 10.0 |
| 31 | All the following statements about the molecula... | ✗ | 4.73 | 0.0011 | 1 | 100.00% | 100.0 |
| 32 | You are interested in studying a rare type of b... | ✓ | 4.74 | 0.0009 | 5 | 80.00% | 16.0 |
| 33 | Find KE of product particles in, Pi(+) = mu(+) ... | ✗ | 10.30 | 0.0000 | 4 | 100.00% | 10.0 |
| 34 | Measuring stellar inclinations is fundamental i... | ✓ | 10.54 | 0.0106 | 3 | 66.67% | 10.0 |
| 35 | A methanol solution of (R)-(+)-Limonene is stir... | ✓ | 11.83 | 0.0059 | 4 | 100.00% | 100.0 |
| 36 | ChIP-seq on a PFA-fixed sample with an antibody... | ✓ | 6.28 | 0.0008 | 4 | 100.00% | 100.0 |
| 37 | methyl isoamyl ketone is treated with hydrogen ... | ✓ | 11.97 | 0.0073 | 3 | 100.00% | 100.0 |
| 38 | Identify the final product produced when cyclob... | ✗ | 6.65 | 0.0015 | 3 | 100.00% | 23.3 |
| 39 | Researchers are attempting to detect transits o... | ✓ | 93.54 | 0.0119 | 6 | 66.67% | 40.0 |
| 40 | The majority of stars in our Galaxy form and ev... | ✗ | 8.64 | 0.0094 | 6 | 33.33% | 25.0 |
| 41 | How many of the following compounds will exhibi... | ✗ | 7.15 | 0.0026 | 10 | 100.00% | 100.0 |
| 42 | "Consider the following compounds: 1: 7,7-diflu... | ✗ | 6.74 | 0.0044 | 5 | 40.00% | 36.0 |
| 43 | A paper you are reading about the seesaw mechan... | ✓ | 4.30 | 0.0003 | 1 | 100.00% | 100.0 |
| 44 | v-FLIPS are viral proteins that were first iden... | ✗ | 4.40 | 0.0006 | 4 | 100.00% | 20.0 |
| 45 | Consider the extension of the Standard Model gi... | ✗ | 11.20 | 0.0017 | 6 | 100.00% | 100.0 |
| 46 | What is the concentration of calcium ions in a ... | ✗ | 92.16 | 0.0053 | 3 | 100.00% | 70.0 |
| 47 | Two stars (Star_1 and Star_2) each have masses ... | ✗ | 5.22 | 0.0012 | 7 | 100.00% | 10.0 |
| 48 | Which of the following statements about enhance... | ✗ | 5.34 | 0.0008 | 5 | 100.00% | 22.0 |
| 49 | The Paranal Observatory is situated in Chile at... | ✗ | 9.04 | 0.0163 | 5 | 40.00% | 120.0 |
| 50 | You have prepared a tri-substituted 6-membered ... | ✓ | 6.03 | 0.0015 | 6 | 100.00% | 10.0 |
