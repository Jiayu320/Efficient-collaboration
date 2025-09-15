# 数据集处理报告

## 模型配置

- 小模型: meta-llama/llama-3-8b-instruct
- 大模型: gpt-4o
- 路由模型: claude-3-5-sonnet-latest
- 难度阈值: 3
- 工作线程数: 10

## 概述

- 数据集: dataset/original_data/math200.json
- 问题总数: 50
- 正确数量: 3
- 准确率: 6.00%
- 平均执行时间: 14.65 秒
- 平均成本: $0.0103

## 任务规划指标

- 平均任务步骤数: 7.04
- 平均压缩比例: 81.95%
- 平均每步骤Token限制: 34.71 tokens

## 理论性能指标

- 平均理论执行时间: 8.043 秒
- 平均顺序执行时间: 21.202 秒
- 平均并行加速比: 2.64x
- 理论与实际执行时间比例: 0.55x


## 任务分配统计

- 总任务数: 197
- 小模型执行任务数: 57
- 大模型执行任务数: 140
- 小模型任务占比: 28.93%
- 大模型任务占比: 71.07%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.147 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 6.044 秒

### 生成速度
- 小模型平均每秒生成token数: 4.52 tokens/s
- 大模型平均每秒生成token数: 5.52 tokens/s
- 路由模型平均每秒生成token数: 6.32 tokens/s
- 总平均每秒生成token数: 16.37 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Three semicircles of radius 1 are constructed o... | ✓ | 26.30 | 0.0141 | 7 | 71.43% | 22.1 |
| 2 | What is the distance between the two intersecti... | ✗ | 19.32 | 0.0156 | 6 | 83.33% | 29.2 |
| 3 | By joining alternate vertices of a regular hexa... | ✓ | 34.37 | 0.0234 | 8 | 87.50% | 34.4 |
| 4 | Two parallel chords in a circle have lengths 10... | ✗ | 32.28 | 0.0177 | 6 | 100.00% | 30.0 |
| 5 | Find all solutions to \[\sin \left( \tan^{-1} (... | ✗ | 21.15 | 0.0190 | 7 | 85.71% | 33.6 |
| 6 | There exists a polynomial $P$ of degree 5 with ... | ✓ | 23.60 | 0.0240 | 8 | 75.00% | 45.0 |
| 7 | Triangle $ABC$ has three different integer side... | ✗ | 31.28 | 0.0192 | 8 | 87.50% | 29.4 |
| 8 | Let $x,$ $y,$ and $z$ be positive real numbers ... | ✓ | 20.38 | 0.0208 | 8 | 62.50% | 38.8 |
| 9 | Simplify: $\frac{\sqrt{2.5^2-0.7^2}}{2.7-2.5}$. | ✓ | 3.64 | 0.0000 | - | - | - |
| 10 | Four points, $A$, $B$, $C$, and $D$, are chosen... | ✓ | 28.52 | 0.0177 | 6 | 83.33% | 37.5 |
| 11 | Determine the number of solutions in $x$ of the... | ✗ | 21.73 | 0.0167 | 6 | 100.00% | 35.0 |
| 12 | On the graph of $y=(x+2)^4-100$, how many point... | ✓ | 26.96 | 0.0202 | 8 | 100.00% | 35.0 |
| 13 | Convert $\frac{3}{16}$ to base 2. Express your ... | ✗ | 20.74 | 0.0124 | 5 | 80.00% | 26.0 |
| 14 | Let $S$ be the set of points $(a,b)$ with $0 \l... | ✗ | 23.40 | 0.0205 | 8 | 87.50% | 41.2 |
| 15 | What is the perimeter, in units, of a rhombus i... | ✗ | 19.64 | 0.0138 | 5 | 80.00% | 24.0 |
| 16 | Three schools have a chess tournament. Four pla... | ✗ | 20.63 | 0.0145 | 6 | 66.67% | 25.8 |
| 17 | Three distinct integers $a,$ $b,$ and $c$ have ... | ✗ | 41.04 | 0.0172 | 8 | 50.00% | 36.2 |
| 18 | Determine $w^2+x^2+y^2+z^2$ if \[\begin{aligned... | ✓ | 27.86 | 0.0219 | 7 | 100.00% | 41.4 |
| 19 | If $a$ and $b$ are positive integers such that ... | ✓ | 26.66 | 0.0169 | 7 | 85.71% | 32.9 |
| 20 | Find the maximum value of \[\frac{x - y}{x^4 + ... | ✗ | 37.70 | 0.0160 | 7 | 100.00% | 31.4 |
| 21 | Let $\mathbb{Q}^+$ denote the set of positive r... | ✗ | 22.75 | 0.0248 | 7 | 85.71% | 57.1 |
| 22 | Find the sum of all complex numbers $z$ that sa... | ✓ | 20.88 | 0.0187 | 7 | 71.43% | 35.0 |
| 23 | The sides of a triangle with positive area have... | ✗ | 22.92 | 0.0183 | 7 | 71.43% | 37.1 |
| 24 | What is the smallest positive integer $n$ for w... | ✗ | 25.44 | 0.0194 | 7 | 71.43% | 40.7 |
| 25 | Find a nonzero monic polynomial $P(x)$ with int... | ✗ | 22.57 | 0.0205 | 9 | 88.89% | 41.1 |
| 26 | There exist two complex numbers $c$, say $c_1$ ... | ✗ | 23.10 | 0.0222 | 7 | 57.14% | 33.6 |
| 27 | A $30^\circ$-$60^\circ$-$90^\circ$ triangle is ... | ✗ | 23.88 | 0.0197 | 7 | 100.00% | 34.3 |
| 28 | The greatest common divisor of positive integer... | ✓ | 30.56 | 0.0188 | 7 | 100.00% | 32.9 |
| 29 | A $\textit{palindrome}$ is a positive integer w... | ✗ | 17.31 | 0.0134 | 8 | 62.50% | 31.2 |
| 30 | How many positive and negative integers is $12$... | ✗ | 0.83 | 0.0000 | - | - | - |
| 31 | In triangle $ABC$, $AB = AC = 5$ and $BC = 6$. ... | ✗ | 0.75 | 0.0000 | - | - | - |
| 32 | A $\textit{palindrome}$ is an integer that read... | ✗ | 0.76 | 0.0000 | - | - | - |
| 33 | Suppose that the least common multiple of the f... | ✗ | 0.77 | 0.0000 | - | - | - |
| 34 | Randy presses RAND on his calculator twice to o... | ✗ | 0.76 | 0.0000 | - | - | - |
| 35 | You have seven bags of gold coins. Each bag has... | ✗ | 0.72 | 0.0000 | - | - | - |
| 36 | How many digits are in the value of the followi... | ✗ | 0.75 | 0.0000 | - | - | - |
| 37 | Square $ABCD$ has side length $s$, a circle cen... | ✗ | 0.73 | 0.0000 | - | - | - |
| 38 | How many positive  cubes  divide $3!\cdot 5!\cd... | ✗ | 0.78 | 0.0000 | - | - | - |
| 39 | What is the value of $b$ if $5^b + 5^b + 5^b + ... | ✗ | 0.76 | 0.0000 | - | - | - |
| 40 | The parabola $y = ax^2 + bx + c$ crosses the $x... | ✗ | 0.80 | 0.0000 | - | - | - |
| 41 | One line is defined by \[\begin{pmatrix} 3 \\ -... | ✗ | 0.82 | 0.0000 | - | - | - |
| 42 | A circle of radius 5 with its center at $(0,0)$... | ✗ | 0.75 | 0.0000 | - | - | - |
| 43 | There exist constants $r,$ $s,$ and $t$ so that... | ✗ | 0.75 | 0.0000 | - | - | - |
| 44 | The number $(\sqrt{2}+\sqrt{3})^3$ can be writt... | ✗ | 0.77 | 0.0000 | - | - | - |
| 45 | The medians $AD$, $BE$, and $CF$ of triangle $A... | ✗ | 0.74 | 0.0000 | - | - | - |
| 46 | A sheet of 8-inch by 10-inch paper is placed on... | ✗ | 0.75 | 0.0000 | - | - | - |
| 47 | A regular tetrahedron is a triangular pyramid i... | ✗ | 0.77 | 0.0000 | - | - | - |
| 48 | Find the minimum value of \[17 \log_{30} x - 3 ... | ✗ | 0.75 | 0.0000 | - | - | - |
| 49 | If $0 < \theta < \frac{\pi}{2}$ and $\sqrt{3} \... | ✗ | 0.74 | 0.0000 | - | - | - |
| 50 | Suppose $a$ and $b$ are positive integers such ... | ✗ | 0.75 | 0.0000 | - | - | - |
