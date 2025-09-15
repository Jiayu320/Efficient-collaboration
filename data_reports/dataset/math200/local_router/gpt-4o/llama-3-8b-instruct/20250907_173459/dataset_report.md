# 数据集处理报告

## 模型配置

- 小模型: meta-llama/llama-3-8b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft (New)
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/original_data/math200.json
- 问题总数: 100
- 正确数量: 21
- 准确率: 21.00%
- 平均执行时间: 15.85 秒
- 平均成本: $0.0024

## 任务规划指标

- 平均任务步骤数: 6.76
- 平均压缩比例: 76.68%
- 平均每步骤Token限制: 28.55 tokens

## 理论性能指标

- 平均理论执行时间: 6.273 秒
- 平均顺序执行时间: 16.250 秒
- 平均并行加速比: 2.59x
- 理论与实际执行时间比例: 0.40x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.184 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 10.347 秒

### 生成速度
- 小模型平均每秒生成token数: 0.78 tokens/s
- 大模型平均每秒生成token数: 5.90 tokens/s
- 路由模型平均每秒生成token数: 25.01 tokens/s
- 总平均每秒生成token数: 31.69 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Three semicircles of radius 1 are constructed o... | ✗ | 15.76 | 0.0031 | 6 | 66.67% | 25.0 |
| 2 | What is the distance between the two intersecti... | ✗ | 12.72 | 0.0042 | 5 | 80.00% | 31.0 |
| 3 | By joining alternate vertices of a regular hexa... | ✗ | 14.52 | 0.0020 | 8 | 62.50% | 29.4 |
| 4 | Two parallel chords in a circle have lengths 10... | ✗ | 15.53 | 0.0035 | 7 | 71.43% | 32.9 |
| 5 | Find all solutions to \[\sin \left( \tan^{-1} (... | ✗ | 15.83 | 0.0021 | 5 | 80.00% | 25.0 |
| 6 | There exists a polynomial $P$ of degree 5 with ... | ✗ | 17.63 | 0.0023 | 10 | 60.00% | 26.5 |
| 7 | Triangle $ABC$ has three different integer side... | ✓ | 16.15 | 0.0035 | 7 | 71.43% | 22.9 |
| 8 | Let $x,$ $y,$ and $z$ be positive real numbers ... | ✓ | 15.97 | 0.0019 | 7 | 71.43% | 22.9 |
| 9 | Simplify: $\frac{\sqrt{2.5^2-0.7^2}}{2.7-2.5}$. | ✓ | 17.84 | 0.0013 | 9 | 77.78% | 20.6 |
| 10 | Four points, $A$, $B$, $C$, and $D$, are chosen... | ✓ | 12.25 | 0.0016 | 5 | 80.00% | 35.0 |
| 11 | Determine the number of solutions in $x$ of the... | ✓ | 16.93 | 0.0044 | 6 | 100.00% | 27.5 |
| 12 | On the graph of $y=(x+2)^4-100$, how many point... | ✗ | 12.91 | 0.0014 | 5 | 100.00% | 23.0 |
| 13 | Convert $\frac{3}{16}$ to base 2. Express your ... | ✗ | 16.83 | 0.0019 | 7 | 100.00% | 17.9 |
| 14 | Let $S$ be the set of points $(a,b)$ with $0 \l... | ✗ | 12.73 | 0.0018 | 5 | 80.00% | 32.0 |
| 15 | What is the perimeter, in units, of a rhombus i... | ✓ | 12.41 | 0.0020 | 4 | 100.00% | 26.2 |
| 16 | Three schools have a chess tournament. Four pla... | ✗ | 12.21 | 0.0007 | 7 | 57.14% | 23.6 |
| 17 | Three distinct integers $a,$ $b,$ and $c$ have ... | ✗ | 19.11 | 0.0050 | 8 | 87.50% | 30.6 |
| 18 | Determine $w^2+x^2+y^2+z^2$ if \[\begin{aligned... | ✗ | 14.99 | 0.0013 | 6 | 50.00% | 22.5 |
| 19 | If $a$ and $b$ are positive integers such that ... | ✗ | 18.72 | 0.0040 | 8 | 100.00% | 35.0 |
| 20 | Find the maximum value of \[\frac{x - y}{x^4 + ... | ✗ | 17.09 | 0.0037 | 8 | 62.50% | 24.4 |
| 21 | Let $\mathbb{Q}^+$ denote the set of positive r... | ✗ | 19.65 | 0.0066 | 8 | 87.50% | 40.0 |
| 22 | Find the sum of all complex numbers $z$ that sa... | ✓ | 19.44 | 0.0024 | 10 | 80.00% | 27.5 |
| 23 | The sides of a triangle with positive area have... | ✓ | 12.33 | 0.0015 | 5 | 80.00% | 38.0 |
| 24 | What is the smallest positive integer $n$ for w... | ✓ | 12.82 | 0.0016 | 5 | 80.00% | 27.0 |
| 25 | Find a nonzero monic polynomial $P(x)$ with int... | ✗ | 15.39 | 0.0018 | 6 | 83.33% | 40.0 |
| 26 | There exist two complex numbers $c$, say $c_1$ ... | ✗ | 13.10 | 0.0023 | 6 | 83.33% | 26.7 |
| 27 | A $30^\circ$-$60^\circ$-$90^\circ$ triangle is ... | ✗ | 15.93 | 0.0031 | 7 | 85.71% | 29.3 |
| 28 | The greatest common divisor of positive integer... | ✓ | 16.33 | 0.0022 | 8 | 87.50% | 28.1 |
| 29 | A $\textit{palindrome}$ is a positive integer w... | ✗ | 12.91 | 0.0024 | 5 | 80.00% | 33.0 |
| 30 | How many positive and negative integers is $12$... | ✓ | 16.07 | 0.0025 | 6 | 83.33% | 33.3 |
| 31 | In triangle $ABC$, $AB = AC = 5$ and $BC = 6$. ... | ✗ | 11.37 | 0.0011 | 5 | 60.00% | 23.0 |
| 32 | A $\textit{palindrome}$ is an integer that read... | ✓ | 13.97 | 0.0030 | 5 | 80.00% | 29.0 |
| 33 | Suppose that the least common multiple of the f... | ✗ | 12.16 | 0.0000 | 10 | 70.00% | 30.5 |
| 34 | Randy presses RAND on his calculator twice to o... | ✓ | 13.73 | 0.0007 | 9 | 55.56% | 31.7 |
| 35 | You have seven bags of gold coins. Each bag has... | ✓ | 11.92 | 0.0009 | 6 | 66.67% | 28.3 |
| 36 | How many digits are in the value of the followi... | ✗ | 17.18 | 0.0013 | 9 | 55.56% | 27.2 |
| 37 | Square $ABCD$ has side length $s$, a circle cen... | ✗ | 14.84 | 0.0063 | 8 | 62.50% | 36.2 |
| 38 | How many positive  cubes  divide $3!\cdot 5!\cd... | ✗ | 16.92 | 0.0008 | 13 | 30.77% | 23.5 |
| 39 | What is the value of $b$ if $5^b + 5^b + 5^b + ... | ✓ | 15.21 | 0.0027 | 7 | 71.43% | 24.3 |
| 40 | The parabola $y = ax^2 + bx + c$ crosses the $x... | ✓ | 13.84 | 0.0016 | 8 | 62.50% | 29.4 |
| 41 | One line is defined by \[\begin{pmatrix} 3 \\ -... | ✓ | 13.76 | 0.0022 | 7 | 57.14% | 25.7 |
| 42 | A circle of radius 5 with its center at $(0,0)$... | ✗ | 17.24 | 0.0024 | 9 | 77.78% | 22.2 |
| 43 | There exist constants $r,$ $s,$ and $t$ so that... | ✗ | 19.45 | 0.0054 | 6 | 100.00% | 39.2 |
| 44 | The number $(\sqrt{2}+\sqrt{3})^3$ can be writt... | ✗ | 15.94 | 0.0014 | 6 | 100.00% | 28.3 |
| 45 | The medians $AD$, $BE$, and $CF$ of triangle $A... | ✓ | 13.50 | 0.0023 | 6 | 66.67% | 31.7 |
| 46 | A sheet of 8-inch by 10-inch paper is placed on... | ✓ | 13.74 | 0.0030 | 6 | 66.67% | 20.0 |
| 47 | A regular tetrahedron is a triangular pyramid i... | ✗ | 12.54 | 0.0014 | 5 | 100.00% | 22.0 |
| 48 | Find the minimum value of \[17 \log_{30} x - 3 ... | ✓ | 15.62 | 0.0020 | 8 | 75.00% | 31.2 |
| 49 | If $0 < \theta < \frac{\pi}{2}$ and $\sqrt{3} \... | ✗ | 15.65 | 0.0032 | 5 | 100.00% | 32.0 |
| 50 | Suppose $a$ and $b$ are positive integers such ... | ✓ | 17.84 | 0.0021 | 7 | 71.43% | 32.9 |
| 51 | Estimate $14.7923412^2$ to the nearest hundred. | ✗ | 13.43 | 0.0000 | - | - | - |
| 52 | What is the sum of the lengths of the $\textbf{... | ✓ | 16.92 | 0.0037 | 6 | 83.33% | 32.5 |
| 53 | Ellen baked $2$ dozen cupcakes of which half co... | ✗ | 12.12 | 0.0005 | 7 | 42.86% | 17.9 |
| 54 | The smallest distance between the origin and a ... | ✓ | 17.16 | 0.0037 | 8 | 100.00% | 29.4 |
| 55 | Tim wants to create a circle graph showing the ... | ✓ | 17.53 | 0.0030 | 8 | 87.50% | 23.8 |
| 56 | Spinner I is divided into four equal sections l... | ✗ | 18.26 | 0.0049 | 6 | 100.00% | 40.0 |
| 57 | The set $\{5, 8, 10, 18, 19, 28, 30, x\}$ has e... | ✗ | 14.89 | 0.0025 | 7 | 71.43% | 30.7 |
| 58 | Three mutually tangent spheres of radius 1 rest... | ✓ | 14.44 | 0.0011 | 4 | 100.00% | 32.5 |
| 59 | Let $z_1,$ $z_2,$ $z_3$ be complex numbers such... | ✗ | 17.72 | 0.0016 | 7 | 42.86% | 33.6 |
| 60 | On a true-false test of 100 items, every questi... | ✓ | 13.51 | 0.0007 | 9 | 55.56% | 26.1 |
| 61 | Billy shoots an arrow from 10 feet above the gr... | ✗ | 13.58 | 0.0015 | 7 | 71.43% | 23.6 |
| 62 | The graph of $f(x)=\frac{2x}{x^2-5x-14}$ has ve... | ✓ | 17.29 | 0.0016 | 8 | 62.50% | 16.9 |
| 63 | In the diagram shown here (which is not drawn t... | ✗ | 14.22 | 0.0025 | 7 | 71.43% | 32.1 |
| 64 | For every positive integer $n$, let $\text{mod}... | ✓ | 19.58 | 0.0040 | 5 | 100.00% | 30.0 |
| 65 | Find the number of ordered pairs $(a,b)$ of int... | ✗ | 12.13 | 0.0008 | 5 | 80.00% | 27.0 |
| 66 | Suppose a function $f(x)$ has domain $(-\infty,... | ✓ | 14.44 | 0.0029 | 6 | 100.00% | 27.5 |
| 67 | A student brings whole cherry and cheese danish... | ✗ | 11.73 | 0.0009 | 5 | 60.00% | 29.0 |
| 68 | The parabola with equation $y=ax^2+bx+c$ and ve... | ✗ | 16.02 | 0.0027 | 8 | 75.00% | 26.9 |
| 69 | Let $S$ be the set of points $(a,b)$ in the coo... | ✗ | 14.67 | 0.0027 | 5 | 100.00% | 40.0 |
| 70 | If $c$ is a nonzero constant such that $x^2+cx+... | ✓ | 11.21 | 0.0018 | 4 | 100.00% | 37.5 |
| 71 | Let $x$ and $y$ be positive real numbers.  Find... | ✗ | 17.62 | 0.0034 | 9 | 88.89% | 34.4 |
| 72 | Let $\omega$ be a complex number such that $|\o... | ✓ | 17.99 | 0.0032 | 8 | 100.00% | 23.8 |
| 73 | A sequence $(a_n)$ is defined as follows: \[a_{... | ✗ | 19.14 | 0.0051 | 9 | 100.00% | 34.4 |
| 74 | Find the domain of $\sqrt{6-x-x^2}$. | ✓ | 11.42 | 0.0013 | 5 | 60.00% | 24.0 |
| 75 | An angle $x$ is chosen at random from the inter... | ✗ | 22.83 | 0.0059 | 10 | 90.00% | 32.0 |
| 76 | Find the value of $6+\frac{1}{2+\frac{1}{6+\fra... | ✗ | 14.38 | 0.0000 | 9 | 100.00% | 26.1 |
| 77 | Let $\alpha$ and $\beta$ be angles for which \[... | ✓ | 15.68 | 0.0027 | 6 | 66.67% | 39.2 |
| 78 | Bill walks $\frac{1}{2}$ mile south, then $\fra... | ✓ | 10.45 | 0.0006 | 4 | 75.00% | 21.2 |
| 79 | Anna, Bertram, Carli, and David have a competit... | ✗ | 17.31 | 0.0012 | 10 | 50.00% | 36.5 |
| 80 | What is the minimum value of the expression $x^... | ✓ | 11.06 | 0.0009 | 4 | 75.00% | 21.2 |
| 81 | In triangle $ABC$, $\angle BAC = 72^\circ$.  Th... | ✓ | 12.68 | 0.0024 | 5 | 100.00% | 30.0 |
| 82 | A group of people have the number 12345.6789 wr... | ✗ | 16.92 | 0.0000 | 13 | 38.46% | 18.8 |
| 83 | Let $\alpha,$ $\beta,$ and $\gamma$ be three an... | ✗ | 16.72 | 0.0020 | 8 | 62.50% | 26.2 |
| 84 | In acute triangle $ABC$, altitudes $AD$, $BE$, ... | ✗ | 13.59 | 0.0016 | 8 | 62.50% | 36.2 |
| 85 | The sum of two numbers is 15. Four times the sm... | ✗ | 11.61 | 0.0015 | 5 | 80.00% | 30.0 |
| 86 | An equilateral triangle has a side of length 12... | ✓ | 11.20 | 0.0013 | 4 | 100.00% | 22.5 |
| 87 | The polynomial $p(x)$ satisfies $p(1) = 210$ an... | ✗ | 14.14 | 0.0007 | 8 | 50.00% | 38.1 |
| 88 | The height (in meters) of a shot cannonball fol... | ✗ | 11.84 | 0.0019 | 6 | 50.00% | 23.3 |
| 89 | The data in the stem and leaf plot shown are th... | ✓ | 13.26 | 0.0025 | 5 | 80.00% | 24.0 |
| 90 | What is the sum of all integer values of $x$ su... | ✓ | 21.80 | 0.0037 | 4 | 100.00% | 26.2 |
| 91 | Let $0, a, b, c$ be the vertices of a square in... | ✗ | 22.83 | 0.0026 | 6 | 83.33% | 26.7 |
| 92 | In trapezoid $ABCD$ with bases $\overline{AB}$ ... | ✗ | 17.73 | 0.0022 | 6 | 50.00% | 24.2 |
| 93 | It is a beautiful day at the beach and ten beac... | ✓ | 17.96 | 0.0030 | 8 | 50.00% | 21.2 |
| 94 | Two eight-sided dice each have faces numbered 1... | ✗ | 21.84 | 0.0017 | 4 | 75.00% | 33.8 |
| 95 | Two sequences $A=\{a_0, a_1, a_2,\ldots\}$ and ... | ✗ | 28.37 | 0.0055 | 7 | 85.71% | 25.7 |
| 96 | Each day, two out of the three teams in a class... | ✗ | 22.36 | 0.0032 | 5 | 100.00% | 27.0 |
| 97 | Tom got a Mr. Potato Head for his birthday. It ... | ✗ | 16.58 | 0.0010 | 8 | 25.00% | 21.2 |
| 98 | I draw a card from a standard 52-card deck.  If... | ✗ | 27.82 | 0.0036 | 6 | 83.33% | 29.2 |
| 99 | Find the number of quadratic equations of the f... | ✗ | 21.39 | 0.0017 | 5 | 100.00% | 30.0 |
| 100 | In Cartesian space, three spheres centered at $... | ✗ | 27.02 | 0.0047 | 8 | 87.50% | 36.9 |
