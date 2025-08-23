# 数据集处理报告

## 模型配置

- 小模型: meta-llama/llama-3-8b-instruct
- 大模型: gpt-4o
- 路由模型: saves/Qwen3-1.7B-Instruct/full/sft
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/original_data/math200.json
- 问题总数: 100
- 正确数量: 36
- 准确率: 36.00%
- 平均执行时间: 20.96 秒
- 平均成本: $0.0021

## 任务规划指标

- 平均任务步骤数: 7.05
- 平均压缩比例: 74.85%
- 平均每步骤Token限制: 25.80 tokens

## 理论性能指标

- 平均理论执行时间: 15.959 秒
- 平均规划阶段时间: 10.402 秒 (65.2%)
- 平均任务执行时间: 5.556 秒 (34.8%)
- 平均顺序执行时间: 17.720 秒
- 平均并行加速比: 1.11x
- 理论与实际执行时间比例: 0.76x

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.620 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 12.033 秒

### 生成速度
- 小模型平均每秒生成token数: 0.37 tokens/s
- 大模型平均每秒生成token数: 3.58 tokens/s
- 路由模型平均每秒生成token数: 5.59 tokens/s
- 总平均每秒生成token数: 9.53 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Three semicircles of radius 1 are constructed o... | ✗ | 21.88 | 0.0027 | 7 | 71.43% | 25.0 |
| 2 | What is the distance between the two intersecti... | ✓ | 19.40 | 0.0018 | 5 | 80.00% | 37.0 |
| 3 | By joining alternate vertices of a regular hexa... | ✗ | 15.07 | 0.0013 | 7 | 57.14% | 27.1 |
| 4 | Two parallel chords in a circle have lengths 10... | ✗ | 19.61 | 0.0025 | 7 | 85.71% | 25.0 |
| 5 | Find all solutions to \[\sin \left( \tan^{-1} (... | ✗ | 26.14 | 0.0029 | 9 | 88.89% | 25.6 |
| 6 | There exists a polynomial $P$ of degree 5 with ... | ✗ | 33.76 | 0.0049 | 9 | 77.78% | 34.4 |
| 7 | Triangle $ABC$ has three different integer side... | ✗ | 20.99 | 0.0010 | 7 | 71.43% | 17.1 |
| 8 | Let $x,$ $y,$ and $z$ be positive real numbers ... | ✗ | 42.86 | 0.0021 | 5 | 100.00% | 30.0 |
| 9 | Simplify: $\frac{\sqrt{2.5^2-0.7^2}}{2.7-2.5}$. | ✓ | 32.04 | 0.0009 | 8 | 75.00% | 13.8 |
| 10 | Four points, $A$, $B$, $C$, and $D$, are chosen... | ✗ | 32.51 | 0.0025 | 6 | 66.67% | 37.5 |
| 11 | Determine the number of solutions in $x$ of the... | ✓ | 19.11 | 0.0024 | 7 | 71.43% | 30.7 |
| 12 | On the graph of $y=(x+2)^4-100$, how many point... | ✓ | 26.89 | 0.0039 | 8 | 75.00% | 33.8 |
| 13 | Convert $\frac{3}{16}$ to base 2. Express your ... | ✓ | 17.77 | 0.0012 | 6 | 66.67% | 23.3 |
| 14 | Let $S$ be the set of points $(a,b)$ with $0 \l... | ✗ | 18.74 | 0.0021 | 7 | 85.71% | 25.7 |
| 15 | What is the perimeter, in units, of a rhombus i... | ✓ | 17.02 | 0.0014 | 5 | 80.00% | 28.0 |
| 16 | Three schools have a chess tournament. Four pla... | ✓ | 22.28 | 0.0013 | 6 | 66.67% | 30.0 |
| 17 | Three distinct integers $a,$ $b,$ and $c$ have ... | ✗ | 20.98 | 0.0029 | 9 | 77.78% | 24.4 |
| 18 | Determine $w^2+x^2+y^2+z^2$ if \[\begin{aligned... | ✓ | 13.28 | 0.0010 | 3 | 100.00% | 25.0 |
| 19 | If $a$ and $b$ are positive integers such that ... | ✗ | 23.01 | 0.0029 | 6 | 83.33% | 25.0 |
| 20 | Find the maximum value of \[\frac{x - y}{x^4 + ... | ✗ | 17.17 | 0.0013 | 8 | 75.00% | 21.2 |
| 21 | Let $\mathbb{Q}^+$ denote the set of positive r... | ✗ | 28.25 | 0.0042 | 9 | 100.00% | 28.3 |
| 22 | Find the sum of all complex numbers $z$ that sa... | ✗ | 17.33 | 0.0016 | 6 | 66.67% | 25.8 |
| 23 | The sides of a triangle with positive area have... | ✓ | 15.69 | 0.0016 | 4 | 75.00% | 26.2 |
| 24 | What is the smallest positive integer $n$ for w... | ✗ | 20.26 | 0.0013 | 8 | 75.00% | 28.1 |
| 25 | Find a nonzero monic polynomial $P(x)$ with int... | ✗ | 21.94 | 0.0018 | 6 | 83.33% | 27.5 |
| 26 | There exist two complex numbers $c$, say $c_1$ ... | ✗ | 21.97 | 0.0027 | 6 | 66.67% | 30.0 |
| 27 | A $30^\circ$-$60^\circ$-$90^\circ$ triangle is ... | ✓ | 18.64 | 0.0027 | 7 | 71.43% | 23.6 |
| 28 | The greatest common divisor of positive integer... | ✗ | 22.92 | 0.0041 | 7 | 85.71% | 31.4 |
| 29 | A $\textit{palindrome}$ is a positive integer w... | ✓ | 15.99 | 0.0017 | 5 | 80.00% | 33.0 |
| 30 | How many positive and negative integers is $12$... | ✓ | 19.76 | 0.0014 | 9 | 66.67% | 21.7 |
| 31 | In triangle $ABC$, $AB = AC = 5$ and $BC = 6$. ... | ✗ | 13.89 | 0.0023 | 5 | 40.00% | 36.0 |
| 32 | A $\textit{palindrome}$ is an integer that read... | ✓ | 16.99 | 0.0036 | 4 | 100.00% | 36.2 |
| 33 | Suppose that the least common multiple of the f... | ✗ | 20.84 | 0.0000 | - | - | - |
| 34 | Randy presses RAND on his calculator twice to o... | ✗ | 20.70 | 0.0020 | 7 | 57.14% | 25.7 |
| 35 | You have seven bags of gold coins. Each bag has... | ✗ | 13.86 | 0.0008 | 5 | 60.00% | 32.0 |
| 36 | How many digits are in the value of the followi... | ✗ | 20.31 | 0.0019 | 10 | 50.00% | 21.5 |
| 37 | Square $ABCD$ has side length $s$, a circle cen... | ✗ | 18.62 | 0.0023 | 9 | 66.67% | 24.4 |
| 38 | How many positive  cubes  divide $3!\cdot 5!\cd... | ✗ | 22.21 | 0.0017 | 8 | 75.00% | 26.2 |
| 39 | What is the value of $b$ if $5^b + 5^b + 5^b + ... | ✓ | 25.49 | 0.0029 | 9 | 77.78% | 22.8 |
| 40 | The parabola $y = ax^2 + bx + c$ crosses the $x... | ✓ | 17.61 | 0.0017 | 9 | 55.56% | 24.4 |
| 41 | One line is defined by \[\begin{pmatrix} 3 \\ -... | ✗ | 17.87 | 0.0020 | 7 | 57.14% | 22.9 |
| 42 | A circle of radius 5 with its center at $(0,0)$... | ✓ | 22.84 | 0.0020 | 8 | 87.50% | 22.5 |
| 43 | There exist constants $r,$ $s,$ and $t$ so that... | ✓ | 19.97 | 0.0020 | 8 | 62.50% | 36.9 |
| 44 | The number $(\sqrt{2}+\sqrt{3})^3$ can be writt... | ✓ | 18.18 | 0.0023 | 7 | 71.43% | 30.7 |
| 45 | The medians $AD$, $BE$, and $CF$ of triangle $A... | ✗ | 21.26 | 0.0023 | 9 | 77.78% | 19.4 |
| 46 | A sheet of 8-inch by 10-inch paper is placed on... | ✓ | 21.76 | 0.0020 | 10 | 70.00% | 21.0 |
| 47 | A regular tetrahedron is a triangular pyramid i... | ✗ | 21.34 | 0.0017 | 6 | 100.00% | 30.0 |
| 48 | Find the minimum value of \[17 \log_{30} x - 3 ... | ✗ | 21.69 | 0.0021 | 9 | 55.56% | 30.0 |
| 49 | If $0 < \theta < \frac{\pi}{2}$ and $\sqrt{3} \... | ✗ | 19.07 | 0.0017 | 6 | 66.67% | 30.0 |
| 50 | Suppose $a$ and $b$ are positive integers such ... | ✗ | 17.14 | 0.0011 | 6 | 83.33% | 29.2 |
| 51 | Estimate $14.7923412^2$ to the nearest hundred. | ✗ | 13.48 | 0.0003 | 5 | 60.00% | 18.0 |
| 52 | What is the sum of the lengths of the $\textbf{... | ✗ | 16.84 | 0.0020 | 6 | 83.33% | 21.7 |
| 53 | Ellen baked $2$ dozen cupcakes of which half co... | ✗ | 21.21 | 0.0012 | 7 | 42.86% | 16.4 |
| 54 | The smallest distance between the origin and a ... | ✗ | 25.10 | 0.0036 | 8 | 100.00% | 27.5 |
| 55 | Tim wants to create a circle graph showing the ... | ✗ | 15.80 | 0.0018 | 5 | 80.00% | 19.0 |
| 56 | Spinner I is divided into four equal sections l... | ✗ | 17.67 | 0.0017 | 6 | 83.33% | 29.2 |
| 57 | The set $\{5, 8, 10, 18, 19, 28, 30, x\}$ has e... | ✓ | 23.33 | 0.0019 | 6 | 83.33% | 20.8 |
| 58 | Three mutually tangent spheres of radius 1 rest... | ✗ | 17.46 | 0.0013 | 6 | 83.33% | 20.8 |
| 59 | Let $z_1,$ $z_2,$ $z_3$ be complex numbers such... | ✗ | 25.23 | 0.0030 | 9 | 66.67% | 32.2 |
| 60 | On a true-false test of 100 items, every questi... | ✗ | 20.30 | 0.0011 | 8 | 50.00% | 20.0 |
| 61 | Billy shoots an arrow from 10 feet above the gr... | ✗ | 20.18 | 0.0020 | 5 | 80.00% | 23.0 |
| 62 | The graph of $f(x)=\frac{2x}{x^2-5x-14}$ has ve... | ✓ | 16.30 | 0.0014 | 4 | 75.00% | 27.5 |
| 63 | In the diagram shown here (which is not drawn t... | ✗ | 18.81 | 0.0020 | 7 | 71.43% | 22.9 |
| 64 | For every positive integer $n$, let $\text{mod}... | ✗ | 24.66 | 0.0034 | 9 | 88.89% | 25.0 |
| 65 | Find the number of ordered pairs $(a,b)$ of int... | ✓ | 21.03 | 0.0027 | 9 | 77.78% | 26.7 |
| 66 | Suppose a function $f(x)$ has domain $(-\infty,... | ✓ | 15.43 | 0.0014 | 6 | 66.67% | 24.2 |
| 67 | A student brings whole cherry and cheese danish... | ✓ | 17.42 | 0.0017 | 6 | 66.67% | 24.2 |
| 68 | The parabola with equation $y=ax^2+bx+c$ and ve... | ✗ | 18.92 | 0.0022 | 8 | 62.50% | 38.8 |
| 69 | Let $S$ be the set of points $(a,b)$ in the coo... | ✓ | 25.58 | 0.0030 | 9 | 100.00% | 25.6 |
| 70 | If $c$ is a nonzero constant such that $x^2+cx+... | ✓ | 24.15 | 0.0034 | 9 | 88.89% | 23.9 |
| 71 | Let $x$ and $y$ be positive real numbers.  Find... | ✗ | 19.69 | 0.0024 | 6 | 100.00% | 25.0 |
| 72 | Let $\omega$ be a complex number such that $|\o... | ✗ | 29.68 | 0.0052 | 10 | 100.00% | 31.5 |
| 73 | A sequence $(a_n)$ is defined as follows: \[a_{... | ✓ | 36.94 | 0.0025 | 9 | 77.78% | 25.6 |
| 74 | Find the domain of $\sqrt{6-x-x^2}$. | ✗ | 20.33 | 0.0018 | 6 | 83.33% | 23.3 |
| 75 | An angle $x$ is chosen at random from the inter... | ✗ | 25.76 | 0.0017 | 9 | 77.78% | 22.8 |
| 76 | Find the value of $6+\frac{1}{2+\frac{1}{6+\fra... | ✓ | 27.74 | 0.0026 | 9 | 100.00% | 28.3 |
| 77 | Let $\alpha$ and $\beta$ be angles for which \[... | ✓ | 18.81 | 0.0022 | 6 | 100.00% | 30.0 |
| 78 | Bill walks $\frac{1}{2}$ mile south, then $\fra... | ✓ | 14.40 | 0.0010 | 4 | 75.00% | 16.2 |
| 79 | Anna, Bertram, Carli, and David have a competit... | ✗ | 20.40 | 0.0016 | 8 | 62.50% | 25.0 |
| 80 | What is the minimum value of the expression $x^... | ✓ | 15.96 | 0.0017 | 4 | 75.00% | 25.0 |
| 81 | In triangle $ABC$, $\angle BAC = 72^\circ$.  Th... | ✗ | 15.38 | 0.0017 | 6 | 66.67% | 25.8 |
| 82 | A group of people have the number 12345.6789 wr... | ✗ | 18.28 | 0.0012 | 12 | 33.33% | 9.8 |
| 83 | Let $\alpha,$ $\beta,$ and $\gamma$ be three an... | ✗ | 18.51 | 0.0018 | 6 | 83.33% | 22.5 |
| 84 | In acute triangle $ABC$, altitudes $AD$, $BE$, ... | ✗ | 21.22 | 0.0031 | 8 | 87.50% | 28.1 |
| 85 | The sum of two numbers is 15. Four times the sm... | ✗ | 17.21 | 0.0011 | 5 | 80.00% | 20.0 |
| 86 | An equilateral triangle has a side of length 12... | ✓ | 29.43 | 0.0015 | 5 | 100.00% | 20.0 |
| 87 | The polynomial $p(x)$ satisfies $p(1) = 210$ an... | ✗ | 26.17 | 0.0033 | 9 | 88.89% | 37.2 |
| 88 | The height (in meters) of a shot cannonball fol... | ✗ | 25.97 | 0.0028 | 8 | 75.00% | 23.8 |
| 89 | The data in the stem and leaf plot shown are th... | ✗ | 15.16 | 0.0015 | 4 | 75.00% | 21.2 |
| 90 | What is the sum of all integer values of $x$ su... | ✓ | 24.68 | 0.0020 | 5 | 100.00% | 26.0 |
| 91 | Let $0, a, b, c$ be the vertices of a square in... | ✗ | 27.65 | 0.0008 | 8 | 50.00% | 18.8 |
| 92 | In trapezoid $ABCD$ with bases $\overline{AB}$ ... | ✗ | 14.29 | 0.0009 | 5 | 40.00% | 24.0 |
| 93 | It is a beautiful day at the beach and ten beac... | ✓ | 20.06 | 0.0030 | 10 | 60.00% | 19.5 |
| 94 | Two eight-sided dice each have faces numbered 1... | ✓ | 14.65 | 0.0014 | 4 | 75.00% | 30.0 |
| 95 | Two sequences $A=\{a_0, a_1, a_2,\ldots\}$ and ... | ✓ | 22.05 | 0.0029 | 10 | 60.00% | 15.5 |
| 96 | Each day, two out of the three teams in a class... | ✗ | 17.91 | 0.0010 | 7 | 57.14% | 22.1 |
| 97 | Tom got a Mr. Potato Head for his birthday. It ... | ✗ | 18.54 | 0.0009 | 10 | 40.00% | 24.0 |
| 98 | I draw a card from a standard 52-card deck.  If... | ✗ | 23.32 | 0.0038 | 7 | 85.71% | 23.6 |
| 99 | Find the number of quadratic equations of the f... | ✗ | 23.57 | 0.0027 | 8 | 87.50% | 31.9 |
| 100 | In Cartesian space, three spheres centered at $... | ✗ | 18.89 | 0.0020 | 8 | 62.50% | 33.1 |
