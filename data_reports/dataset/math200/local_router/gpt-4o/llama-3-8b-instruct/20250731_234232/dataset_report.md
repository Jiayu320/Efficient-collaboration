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
- 正确数量: 47
- 准确率: 47.00%
- 平均执行时间: 28.32 秒
- 平均成本: $0.0018

## 任务规划指标

- 平均任务步骤数: 7.15
- 平均压缩比例: 76.16%
- 平均每步骤Token限制: 26.19 tokens

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 1.777 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 19.131 秒

### 生成速度
- 小模型平均每秒生成token数: 0.35 tokens/s
- 大模型平均每秒生成token数: 2.66 tokens/s
- 路由模型平均每秒生成token数: 4.85 tokens/s
- 总平均每秒生成token数: 7.86 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Three semicircles of radius 1 are constructed o... | ✓ | 18.67 | 0.0007 | 5 | 60.00% | 24.0 |
| 2 | What is the distance between the two intersecti... | ✓ | 25.51 | 0.0014 | 5 | 60.00% | 30.0 |
| 3 | By joining alternate vertices of a regular hexa... | ✗ | 21.19 | 0.0014 | 8 | 62.50% | 26.2 |
| 4 | Two parallel chords in a circle have lengths 10... | ✓ | 86.18 | 0.0025 | 6 | 100.00% | 34.2 |
| 5 | Find all solutions to \[\sin \left( \tan^{-1} (... | ✗ | 23.38 | 0.0022 | 8 | 87.50% | 26.9 |
| 6 | There exists a polynomial $P$ of degree 5 with ... | ✗ | 22.25 | 0.0029 | 8 | 75.00% | 31.2 |
| 7 | Triangle $ABC$ has three different integer side... | ✗ | 28.10 | 0.0024 | 6 | 83.33% | 23.3 |
| 8 | Let $x,$ $y,$ and $z$ be positive real numbers ... | ✗ | 22.50 | 0.0022 | 8 | 87.50% | 22.5 |
| 9 | Simplify: $\frac{\sqrt{2.5^2-0.7^2}}{2.7-2.5}$. | ✓ | 18.27 | 0.0006 | 7 | 71.43% | 18.6 |
| 10 | Four points, $A$, $B$, $C$, and $D$, are chosen... | ✗ | 95.22 | 0.0030 | 9 | 77.78% | 31.7 |
| 11 | Determine the number of solutions in $x$ of the... | ✓ | 21.78 | 0.0019 | 6 | 100.00% | 30.0 |
| 12 | On the graph of $y=(x+2)^4-100$, how many point... | ✓ | 21.37 | 0.0015 | 10 | 50.00% | 23.0 |
| 13 | Convert $\frac{3}{16}$ to base 2. Express your ... | ✓ | 21.26 | 0.0011 | 8 | 87.50% | 13.1 |
| 14 | Let $S$ be the set of points $(a,b)$ with $0 \l... | ✓ | 29.61 | 0.0036 | 9 | 88.89% | 33.3 |
| 15 | What is the perimeter, in units, of a rhombus i... | ✓ | 18.68 | 0.0010 | 6 | 66.67% | 25.8 |
| 16 | Three schools have a chess tournament. Four pla... | ✗ | 19.08 | 0.0010 | 8 | 62.50% | 25.0 |
| 17 | Three distinct integers $a,$ $b,$ and $c$ have ... | ✗ | 25.80 | 0.0035 | 9 | 88.89% | 22.8 |
| 18 | Determine $w^2+x^2+y^2+z^2$ if \[\begin{aligned... | ✓ | 21.91 | 0.0017 | 5 | 100.00% | 35.0 |
| 19 | If $a$ and $b$ are positive integers such that ... | ✗ | 23.95 | 0.0018 | 8 | 87.50% | 25.0 |
| 20 | Find the maximum value of \[\frac{x - y}{x^4 + ... | ✗ | 21.09 | 0.0022 | 7 | 71.43% | 30.0 |
| 21 | Let $\mathbb{Q}^+$ denote the set of positive r... | ✓ | 22.76 | 0.0026 | 8 | 87.50% | 25.0 |
| 22 | Find the sum of all complex numbers $z$ that sa... | ✗ | 21.65 | 0.0021 | 6 | 100.00% | 21.7 |
| 23 | The sides of a triangle with positive area have... | ✓ | 16.85 | 0.0012 | 5 | 80.00% | 34.0 |
| 24 | What is the smallest positive integer $n$ for w... | ✗ | 78.40 | 0.0009 | 6 | 66.67% | 22.5 |
| 25 | Find a nonzero monic polynomial $P(x)$ with int... | ✗ | 26.52 | 0.0038 | 6 | 100.00% | 30.0 |
| 26 | There exist two complex numbers $c$, say $c_1$ ... | ✗ | 89.15 | 0.0039 | 6 | 100.00% | 24.2 |
| 27 | A $30^\circ$-$60^\circ$-$90^\circ$ triangle is ... | ✗ | 18.53 | 0.0006 | 6 | 66.67% | 25.0 |
| 28 | The greatest common divisor of positive integer... | ✗ | 88.85 | 0.0034 | 7 | 85.71% | 24.3 |
| 29 | A $\textit{palindrome}$ is a positive integer w... | ✓ | 17.62 | 0.0017 | 4 | 100.00% | 32.5 |
| 30 | How many positive and negative integers is $12$... | ✓ | 24.91 | 0.0009 | 8 | 75.00% | 26.9 |
| 31 | In triangle $ABC$, $AB = AC = 5$ and $BC = 6$. ... | ✓ | 17.91 | 0.0013 | 6 | 50.00% | 21.7 |
| 32 | A $\textit{palindrome}$ is an integer that read... | ✓ | 19.51 | 0.0007 | 5 | 80.00% | 21.0 |
| 33 | Suppose that the least common multiple of the f... | ✗ | 24.19 | 0.0033 | 9 | 77.78% | 39.4 |
| 34 | Randy presses RAND on his calculator twice to o... | ✗ | 23.23 | 0.0017 | 8 | 62.50% | 27.5 |
| 35 | You have seven bags of gold coins. Each bag has... | ✗ | 30.02 | 0.0009 | 9 | 44.44% | 27.8 |
| 36 | How many digits are in the value of the followi... | ✓ | 21.99 | 0.0017 | 9 | 55.56% | 22.8 |
| 37 | Square $ABCD$ has side length $s$, a circle cen... | ✗ | 30.27 | 0.0040 | 9 | 77.78% | 23.9 |
| 38 | How many positive  cubes  divide $3!\cdot 5!\cd... | ✗ | 18.27 | 0.0011 | 5 | 100.00% | 32.0 |
| 39 | What is the value of $b$ if $5^b + 5^b + 5^b + ... | ✓ | 23.53 | 0.0015 | 8 | 75.00% | 23.1 |
| 40 | The parabola $y = ax^2 + bx + c$ crosses the $x... | ✓ | 21.16 | 0.0017 | 9 | 66.67% | 31.7 |
| 41 | One line is defined by \[\begin{pmatrix} 3 \\ -... | ✓ | 23.03 | 0.0017 | 7 | 42.86% | 24.3 |
| 42 | A circle of radius 5 with its center at $(0,0)$... | ✓ | 30.19 | 0.0016 | 7 | 85.71% | 20.0 |
| 43 | There exist constants $r,$ $s,$ and $t$ so that... | ✓ | 24.84 | 0.0020 | 8 | 62.50% | 30.0 |
| 44 | The number $(\sqrt{2}+\sqrt{3})^3$ can be writt... | ✗ | 18.49 | 0.0009 | 7 | 71.43% | 20.7 |
| 45 | The medians $AD$, $BE$, and $CF$ of triangle $A... | ✗ | 20.88 | 0.0028 | 7 | 85.71% | 34.3 |
| 46 | A sheet of 8-inch by 10-inch paper is placed on... | ✗ | 18.30 | 0.0006 | 9 | 44.44% | 16.1 |
| 47 | A regular tetrahedron is a triangular pyramid i... | ✓ | 21.08 | 0.0020 | 5 | 100.00% | 37.0 |
| 48 | Find the minimum value of \[17 \log_{30} x - 3 ... | ✗ | 27.57 | 0.0032 | 10 | 90.00% | 34.5 |
| 49 | If $0 < \theta < \frac{\pi}{2}$ and $\sqrt{3} \... | ✗ | 21.02 | 0.0007 | 4 | 75.00% | 35.0 |
| 50 | Suppose $a$ and $b$ are positive integers such ... | ✓ | 21.47 | 0.0006 | 8 | 50.00% | 23.1 |
| 51 | Estimate $14.7923412^2$ to the nearest hundred. | ✓ | 85.40 | 0.0008 | 7 | 71.43% | 28.6 |
| 52 | What is the sum of the lengths of the $\textbf{... | ✗ | 20.55 | 0.0009 | 6 | 66.67% | 23.3 |
| 53 | Ellen baked $2$ dozen cupcakes of which half co... | ✗ | 19.25 | 0.0014 | 8 | 50.00% | 18.1 |
| 54 | The smallest distance between the origin and a ... | ✓ | 93.80 | 0.0038 | 10 | 100.00% | 25.5 |
| 55 | Tim wants to create a circle graph showing the ... | ✓ | 20.16 | 0.0026 | 8 | 75.00% | 22.5 |
| 56 | Spinner I is divided into four equal sections l... | ✓ | 19.37 | 0.0013 | 7 | 57.14% | 30.0 |
| 57 | The set $\{5, 8, 10, 18, 19, 28, 30, x\}$ has e... | ✓ | 18.16 | 0.0013 | 5 | 80.00% | 23.0 |
| 58 | Three mutually tangent spheres of radius 1 rest... | ✗ | 15.54 | 0.0007 | 5 | 40.00% | 21.0 |
| 59 | Let $z_1,$ $z_2,$ $z_3$ be complex numbers such... | ✗ | 20.44 | 0.0007 | 9 | 44.44% | 23.3 |
| 60 | On a true-false test of 100 items, every questi... | ✗ | 17.69 | 0.0000 | 10 | 40.00% | 22.5 |
| 61 | Billy shoots an arrow from 10 feet above the gr... | ✓ | 29.61 | 0.0028 | 9 | 66.67% | 23.3 |
| 62 | The graph of $f(x)=\frac{2x}{x^2-5x-14}$ has ve... | ✓ | 18.20 | 0.0008 | 7 | 57.14% | 22.9 |
| 63 | In the diagram shown here (which is not drawn t... | ✓ | 17.96 | 0.0015 | 6 | 66.67% | 25.0 |
| 64 | For every positive integer $n$, let $\text{mod}... | ✓ | 19.93 | 0.0013 | 8 | 62.50% | 24.4 |
| 65 | Find the number of ordered pairs $(a,b)$ of int... | ✓ | 20.05 | 0.0015 | 7 | 85.71% | 24.3 |
| 66 | Suppose a function $f(x)$ has domain $(-\infty,... | ✓ | 18.02 | 0.0010 | 5 | 80.00% | 31.0 |
| 67 | A student brings whole cherry and cheese danish... | ✗ | 33.21 | 0.0031 | 9 | 100.00% | 23.3 |
| 68 | The parabola with equation $y=ax^2+bx+c$ and ve... | ✗ | 21.02 | 0.0029 | 8 | 87.50% | 24.4 |
| 69 | Let $S$ be the set of points $(a,b)$ in the coo... | ✗ | 23.40 | 0.0018 | 10 | 60.00% | 28.0 |
| 70 | If $c$ is a nonzero constant such that $x^2+cx+... | ✓ | 25.82 | 0.0030 | 9 | 66.67% | 34.4 |
| 71 | Let $x$ and $y$ be positive real numbers.  Find... | ✗ | 25.59 | 0.0029 | 8 | 87.50% | 31.2 |
| 72 | Let $\omega$ be a complex number such that $|\o... | ✗ | 25.99 | 0.0024 | 9 | 77.78% | 26.7 |
| 73 | A sequence $(a_n)$ is defined as follows: \[a_{... | ✗ | 29.75 | 0.0038 | 8 | 100.00% | 35.6 |
| 74 | Find the domain of $\sqrt{6-x-x^2}$. | ✗ | 25.21 | 0.0000 | 6 | 100.00% | 18.3 |
| 75 | An angle $x$ is chosen at random from the inter... | ✗ | 33.28 | 0.0023 | 9 | 77.78% | 30.6 |
| 76 | Find the value of $6+\frac{1}{2+\frac{1}{6+\fra... | ✓ | 26.99 | 0.0039 | 8 | 100.00% | 37.5 |
| 77 | Let $\alpha$ and $\beta$ be angles for which \[... | ✓ | 24.68 | 0.0027 | 6 | 100.00% | 27.5 |
| 78 | Bill walks $\frac{1}{2}$ mile south, then $\fra... | ✓ | 18.19 | 0.0011 | 4 | 75.00% | 21.2 |
| 79 | Anna, Bertram, Carli, and David have a competit... | ✗ | 24.67 | 0.0031 | 9 | 77.78% | 26.7 |
| 80 | What is the minimum value of the expression $x^... | ✓ | 17.84 | 0.0011 | 4 | 100.00% | 21.2 |
| 81 | In triangle $ABC$, $\angle BAC = 72^\circ$.  Th... | ✓ | 21.87 | 0.0021 | 7 | 85.71% | 25.7 |
| 82 | A group of people have the number 12345.6789 wr... | ✗ | 21.27 | 0.0009 | 11 | 27.27% | 19.5 |
| 83 | Let $\alpha,$ $\beta,$ and $\gamma$ be three an... | ✗ | 19.54 | 0.0012 | 5 | 80.00% | 24.0 |
| 84 | In acute triangle $ABC$, altitudes $AD$, $BE$, ... | ✗ | 21.43 | 0.0023 | 7 | 85.71% | 27.1 |
| 85 | The sum of two numbers is 15. Four times the sm... | ✓ | 18.80 | 0.0013 | 5 | 80.00% | 28.0 |
| 86 | An equilateral triangle has a side of length 12... | ✓ | 20.34 | 0.0009 | 4 | 100.00% | 20.0 |
| 87 | The polynomial $p(x)$ satisfies $p(1) = 210$ an... | ✗ | 19.28 | 0.0011 | 4 | 100.00% | 26.2 |
| 88 | The height (in meters) of a shot cannonball fol... | ✗ | 30.21 | 0.0013 | 5 | 80.00% | 25.0 |
| 89 | The data in the stem and leaf plot shown are th... | ✗ | 23.36 | 0.0006 | 6 | 66.67% | 20.0 |
| 90 | What is the sum of all integer values of $x$ su... | ✓ | 19.21 | 0.0017 | 4 | 100.00% | 23.8 |
| 91 | Let $0, a, b, c$ be the vertices of a square in... | ✗ | 28.76 | 0.0019 | 8 | 100.00% | 30.6 |
| 92 | In trapezoid $ABCD$ with bases $\overline{AB}$ ... | ✗ | 82.52 | 0.0005 | 7 | 42.86% | 17.9 |
| 93 | It is a beautiful day at the beach and ten beac... | ✗ | 25.20 | 0.0015 | 9 | 66.67% | 19.4 |
| 94 | Two eight-sided dice each have faces numbered 1... | ✓ | 23.24 | 0.0027 | 6 | 83.33% | 26.7 |
| 95 | Two sequences $A=\{a_0, a_1, a_2,\ldots\}$ and ... | ✗ | 86.18 | 0.0029 | 6 | 100.00% | 30.8 |
| 96 | Each day, two out of the three teams in a class... | ✓ | 24.62 | 0.0024 | 8 | 75.00% | 30.0 |
| 97 | Tom got a Mr. Potato Head for his birthday. It ... | ✓ | 18.96 | 0.0008 | 10 | 30.00% | 20.5 |
| 98 | I draw a card from a standard 52-card deck.  If... | ✗ | 21.26 | 0.0014 | 7 | 71.43% | 25.0 |
| 99 | Find the number of quadratic equations of the f... | ✗ | 27.73 | 0.0028 | 9 | 77.78% | 38.3 |
| 100 | In Cartesian space, three spheres centered at $... | ✗ | 20.15 | 0.0018 | 6 | 83.33% | 21.7 |