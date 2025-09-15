# 数据集处理报告

## 模型配置

- 小模型: meta-llama/llama-3-8b-instruct
- 大模型: gpt-4o
- 路由模型: claude-3-5-sonnet-latest
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/original_data/math200.json
- 问题总数: 50
- 正确数量: 10
- 准确率: 20.00%
- 平均执行时间: 22.91 秒
- 平均成本: $0.0188

## 任务规划指标

- 平均任务步骤数: 7.16
- 平均压缩比例: 80.04%
- 平均每步骤Token限制: 33.18 tokens

## 理论性能指标

- 平均理论执行时间: 8.200 秒
- 平均顺序执行时间: 22.078 秒
- 平均并行加速比: 2.69x
- 理论与实际执行时间比例: 0.36x


## 任务分配统计

- 总任务数: 358
- 小模型执行任务数: 16
- 大模型执行任务数: 342
- 小模型任务占比: 4.47%
- 大模型任务占比: 95.53%

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 2.211 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 6.891 秒

### 生成速度
- 小模型平均每秒生成token数: 0.66 tokens/s
- 大模型平均每秒生成token数: 10.98 tokens/s
- 路由模型平均每秒生成token数: 13.06 tokens/s
- 总平均每秒生成token数: 24.70 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Three semicircles of radius 1 are constructed o... | ✗ | 29.34 | 0.0162 | 5 | 80.00% | 22.0 |
| 2 | What is the distance between the two intersecti... | ✗ | 23.18 | 0.0155 | 6 | 83.33% | 28.3 |
| 3 | By joining alternate vertices of a regular hexa... | ✗ | 19.96 | 0.0216 | 8 | 75.00% | 32.5 |
| 4 | Two parallel chords in a circle have lengths 10... | ✗ | 18.15 | 0.0165 | 6 | 100.00% | 30.0 |
| 5 | Find all solutions to \[\sin \left( \tan^{-1} (... | ✗ | 17.98 | 0.0135 | 7 | 85.71% | 32.9 |
| 6 | There exists a polynomial $P$ of degree 5 with ... | ✗ | 24.15 | 0.0220 | 8 | 75.00% | 37.5 |
| 7 | Triangle $ABC$ has three different integer side... | ✗ | 26.32 | 0.0184 | 9 | 77.78% | 33.9 |
| 8 | Let $x,$ $y,$ and $z$ be positive real numbers ... | ✓ | 23.51 | 0.0203 | 8 | 62.50% | 38.8 |
| 9 | Simplify: $\frac{\sqrt{2.5^2-0.7^2}}{2.7-2.5}$. | ✓ | 21.06 | 0.0169 | 7 | 71.43% | 21.4 |
| 10 | Four points, $A$, $B$, $C$, and $D$, are chosen... | ✓ | 19.94 | 0.0165 | 8 | 75.00% | 34.4 |
| 11 | Determine the number of solutions in $x$ of the... | ✗ | 13.44 | 0.0125 | 6 | 100.00% | 35.0 |
| 12 | On the graph of $y=(x+2)^4-100$, how many point... | ✓ | 24.39 | 0.0166 | 6 | 83.33% | 35.8 |
| 13 | Convert $\frac{3}{16}$ to base 2. Express your ... | ✗ | 18.84 | 0.0138 | 5 | 60.00% | 21.0 |
| 14 | Let $S$ be the set of points $(a,b)$ with $0 \l... | ✗ | 29.16 | 0.0206 | 8 | 87.50% | 46.9 |
| 15 | What is the perimeter, in units, of a rhombus i... | ✓ | 19.83 | 0.0147 | 5 | 80.00% | 31.0 |
| 16 | Three schools have a chess tournament. Four pla... | ✗ | 19.26 | 0.0163 | 6 | 66.67% | 25.8 |
| 17 | Three distinct integers $a,$ $b,$ and $c$ have ... | ✗ | 21.93 | 0.0221 | 9 | 55.56% | 37.2 |
| 18 | Determine $w^2+x^2+y^2+z^2$ if \[\begin{aligned... | ✓ | 26.04 | 0.0283 | 8 | 87.50% | 44.4 |
| 19 | If $a$ and $b$ are positive integers such that ... | ✗ | 49.73 | 0.0184 | 7 | 85.71% | 36.4 |
| 20 | Find the maximum value of \[\frac{x - y}{x^4 + ... | ✗ | 19.41 | 0.0201 | 8 | 75.00% | 35.0 |
| 21 | Let $\mathbb{Q}^+$ denote the set of positive r... | ✓ | 18.76 | 0.0177 | 6 | 100.00% | 40.8 |
| 22 | Find the sum of all complex numbers $z$ that sa... | ✗ | 21.42 | 0.0179 | 7 | 100.00% | 35.7 |
| 23 | The sides of a triangle with positive area have... | ✓ | 19.59 | 0.0174 | 7 | 71.43% | 37.1 |
| 24 | What is the smallest positive integer $n$ for w... | ✗ | 56.70 | 0.0208 | 8 | 100.00% | 35.6 |
| 25 | Find a nonzero monic polynomial $P(x)$ with int... | ✓ | 21.05 | 0.0184 | 8 | 87.50% | 29.4 |
| 26 | There exist two complex numbers $c$, say $c_1$ ... | ✗ | 22.39 | 0.0236 | 8 | 62.50% | 31.9 |
| 27 | A $30^\circ$-$60^\circ$-$90^\circ$ triangle is ... | ✓ | 19.88 | 0.0205 | 9 | 55.56% | 28.9 |
| 28 | The greatest common divisor of positive integer... | ✓ | 20.56 | 0.0191 | 6 | 100.00% | 36.7 |
| 29 | A $\textit{palindrome}$ is a positive integer w... | ✓ | 17.40 | 0.0167 | 7 | 57.14% | 31.4 |
| 30 | How many positive and negative integers is $12$... | ✓ | 18.51 | 0.0166 | 7 | 71.43% | 27.1 |
| 31 | In triangle $ABC$, $AB = AC = 5$ and $BC = 6$. ... | ✗ | 19.68 | 0.0185 | 6 | 100.00% | 30.8 |
| 32 | A $\textit{palindrome}$ is an integer that read... | ✓ | 18.51 | 0.0165 | 7 | 57.14% | 30.0 |
| 33 | Suppose that the least common multiple of the f... | ✗ | 29.96 | 0.0228 | 9 | 55.56% | 44.4 |
| 34 | Randy presses RAND on his calculator twice to o... | ✓ | 18.89 | 0.0174 | 7 | 85.71% | 37.1 |
| 35 | You have seven bags of gold coins. Each bag has... | ✗ | 22.22 | 0.0184 | 7 | 100.00% | 33.6 |
| 36 | How many digits are in the value of the followi... | ✓ | 21.55 | 0.0175 | 7 | 85.71% | 25.7 |
| 37 | Square $ABCD$ has side length $s$, a circle cen... | ✓ | 22.80 | 0.0241 | 8 | 75.00% | 40.0 |
| 38 | How many positive  cubes  divide $3!\cdot 5!\cd... | ✓ | 21.65 | 0.0168 | 7 | 57.14% | 25.7 |
| 39 | What is the value of $b$ if $5^b + 5^b + 5^b + ... | ✓ | 19.37 | 0.0164 | 7 | 85.71% | 22.9 |
| 40 | The parabola $y = ax^2 + bx + c$ crosses the $x... | ✗ | 27.37 | 0.0254 | 9 | 66.67% | 41.7 |
| 41 | One line is defined by \[\begin{pmatrix} 3 \\ -... | ✗ | 20.86 | 0.0192 | 7 | 57.14% | 37.1 |
| 42 | A circle of radius 5 with its center at $(0,0)$... | ✓ | 21.42 | 0.0193 | 7 | 71.43% | 27.1 |
| 43 | There exist constants $r,$ $s,$ and $t$ so that... | ✗ | 27.89 | 0.0237 | 8 | 100.00% | 41.2 |
| 44 | The number $(\sqrt{2}+\sqrt{3})^3$ can be writt... | ✗ | 20.75 | 0.0176 | 7 | 85.71% | 27.9 |
| 45 | The medians $AD$, $BE$, and $CF$ of triangle $A... | ✗ | 19.51 | 0.0202 | 7 | 85.71% | 35.0 |
| 46 | A sheet of 8-inch by 10-inch paper is placed on... | ✗ | 17.35 | 0.0152 | 5 | 100.00% | 23.0 |
| 47 | A regular tetrahedron is a triangular pyramid i... | ✓ | 24.34 | 0.0172 | 6 | 100.00% | 37.5 |
| 48 | Find the minimum value of \[17 \log_{30} x - 3 ... | ✗ | 25.87 | 0.0217 | 9 | 100.00% | 33.3 |
| 49 | If $0 < \theta < \frac{\pi}{2}$ and $\sqrt{3} \... | ✗ | 20.64 | 0.0200 | 7 | 85.71% | 35.0 |
| 50 | Suppose $a$ and $b$ are positive integers such ... | ✗ | 22.79 | 0.0211 | 8 | 75.00% | 35.0 |
