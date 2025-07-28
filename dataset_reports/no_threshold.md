# 数据集处理报告

## 模型配置

- 小模型: meta-llama/llama-3-8b-instruct
- 大模型: gpt-4o
- 路由模型: claude-3-5-sonnet-latest
- 难度阈值: 2
- 工作线程数: 10

## 概述

- 数据集: dataset/original_data/math200.json
- 问题总数: 100
- 正确数量: 39
- 准确率: 39.00%
- 平均执行时间: 28.93 秒
- 平均成本: $0.0064

## 任务规划指标

- 平均任务步骤数: 7.38
- 平均压缩比例: 74.31%
- 平均每步骤Token限制: 31.98 tokens

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 2.285 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 11.847 秒

### 生成速度
- 小模型平均每秒生成token数: 0.71 tokens/s
- 大模型平均每秒生成token数: 4.85 tokens/s
- 路由模型平均每秒生成token数: 5.16 tokens/s
- 总平均每秒生成token数: 10.73 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Three semicircles of radius 1 are constructed o... | ✗ | 34.74 | 0.0057 | 7 | 57.14% | 28.6 |
| 2 | What is the distance between the two intersecti... | ✓ | 28.04 | 0.0032 | 4 | 100.00% | 22.5 |
| 3 | By joining alternate vertices of a regular hexa... | ✗ | 36.82 | 0.0087 | 9 | 66.67% | 40.6 |
| 4 | Two parallel chords in a circle have lengths 10... | ✗ | 27.52 | 0.0089 | 8 | 75.00% | 28.1 |
| 5 | Find all solutions to \[\sin \left( \tan^{-1} (... | ✗ | 5.25 | 0.0000 | - | - | - |
| 6 | There exists a polynomial $P$ of degree 5 with ... | ✗ | 27.97 | 0.0071 | 7 | 85.71% | 33.6 |
| 7 | Triangle $ABC$ has three different integer side... | ✓ | 26.55 | 0.0079 | 8 | 75.00% | 36.9 |
| 8 | Let $x,$ $y,$ and $z$ be positive real numbers ... | ✗ | 31.66 | 0.0064 | 7 | 85.71% | 25.7 |
| 9 | Simplify: $\frac{\sqrt{2.5^2-0.7^2}}{2.7-2.5}$. | ✓ | 21.10 | 0.0033 | 7 | 71.43% | 19.3 |
| 10 | Four points, $A$, $B$, $C$, and $D$, are chosen... | ✓ | 23.95 | 0.0045 | 5 | 80.00% | 52.0 |
| 11 | Determine the number of solutions in $x$ of the... | ✓ | 34.30 | 0.0058 | 8 | 87.50% | 23.8 |
| 12 | On the graph of $y=(x+2)^4-100$, how many point... | ✓ | 31.79 | 0.0100 | 8 | 87.50% | 34.4 |
| 13 | Convert $\frac{3}{16}$ to base 2. Express your ... | ✗ | 25.11 | 0.0047 | 7 | 57.14% | 20.0 |
| 14 | Let $S$ be the set of points $(a,b)$ with $0 \l... | ✗ | 35.82 | 0.0105 | 8 | 100.00% | 56.2 |
| 15 | What is the perimeter, in units, of a rhombus i... | ✓ | 33.06 | 0.0052 | 7 | 71.43% | 24.3 |
| 16 | Three schools have a chess tournament. Four pla... | ✗ | 23.16 | 0.0056 | 6 | 66.67% | 22.5 |
| 17 | Three distinct integers $a,$ $b,$ and $c$ have ... | ✗ | 35.25 | 0.0068 | 7 | 71.43% | 37.9 |
| 18 | Determine $w^2+x^2+y^2+z^2$ if \[\begin{aligned... | ✗ | 33.25 | 0.0082 | 8 | 75.00% | 56.2 |
| 19 | If $a$ and $b$ are positive integers such that ... | ✓ | 32.13 | 0.0089 | 9 | 77.78% | 35.6 |
| 20 | Find the maximum value of \[\frac{x - y}{x^4 + ... | ✓ | 35.73 | 0.0085 | 8 | 75.00% | 70.0 |
| 21 | Let $\mathbb{Q}^+$ denote the set of positive r... | ✓ | 21.57 | 0.0052 | 6 | 66.67% | 44.2 |
| 22 | Find the sum of all complex numbers $z$ that sa... | ✗ | 24.87 | 0.0056 | 6 | 100.00% | 43.3 |
| 23 | The sides of a triangle with positive area have... | ✓ | 26.40 | 0.0103 | 9 | 77.78% | 47.8 |
| 24 | What is the smallest positive integer $n$ for w... | ✓ | 31.86 | 0.0059 | 9 | 77.78% | 31.7 |
| 25 | Find a nonzero monic polynomial $P(x)$ with int... | ✗ | 53.88 | 0.0049 | 6 | 66.67% | 28.3 |
| 26 | There exist two complex numbers $c$, say $c_1$ ... | ✗ | 32.52 | 0.0080 | 6 | 66.67% | 29.2 |
| 27 | A $30^\circ$-$60^\circ$-$90^\circ$ triangle is ... | ✓ | 56.26 | 0.0063 | 6 | 100.00% | 33.3 |
| 28 | The greatest common divisor of positive integer... | ✓ | 45.11 | 0.0067 | 7 | 71.43% | 32.1 |
| 29 | A $\textit{palindrome}$ is a positive integer w... | ✓ | 41.79 | 0.0056 | 7 | 85.71% | 26.4 |
| 30 | How many positive and negative integers is $12$... | ✓ | 23.59 | 0.0049 | 7 | 71.43% | 18.6 |
| 31 | In triangle $ABC$, $AB = AC = 5$ and $BC = 6$. ... | ✗ | 32.29 | 0.0057 | 7 | 57.14% | 22.9 |
| 32 | A $\textit{palindrome}$ is an integer that read... | ✗ | 37.22 | 0.0061 | 8 | 75.00% | 24.4 |
| 33 | Suppose that the least common multiple of the f... | ✗ | 26.67 | 0.0079 | 8 | 75.00% | 43.8 |
| 34 | Randy presses RAND on his calculator twice to o... | ✓ | 32.24 | 0.0081 | 9 | 66.67% | 31.1 |
| 35 | You have seven bags of gold coins. Each bag has... | ✗ | 32.81 | 0.0066 | 6 | 100.00% | 30.0 |
| 36 | How many digits are in the value of the followi... | ✗ | 42.02 | 0.0062 | 9 | 88.89% | 26.7 |
| 37 | Square $ABCD$ has side length $s$, a circle cen... | ✗ | 30.86 | 0.0101 | 8 | 75.00% | 33.8 |
| 38 | How many positive  cubes  divide $3!\cdot 5!\cd... | ✗ | 28.24 | 0.0051 | 8 | 62.50% | 21.2 |
| 39 | What is the value of $b$ if $5^b + 5^b + 5^b + ... | ✗ | 23.90 | 0.0051 | 7 | 71.43% | 22.9 |
| 40 | The parabola $y = ax^2 + bx + c$ crosses the $x... | ✗ | 30.42 | 0.0106 | 9 | 66.67% | 42.8 |
| 41 | One line is defined by \[\begin{pmatrix} 3 \\ -... | ✗ | 27.18 | 0.0081 | 7 | 71.43% | 38.6 |
| 42 | A circle of radius 5 with its center at $(0,0)$... | ✓ | 31.92 | 0.0102 | 8 | 75.00% | 33.8 |
| 43 | There exist constants $r,$ $s,$ and $t$ so that... | ✓ | 33.61 | 0.0082 | 7 | 85.71% | 43.6 |
| 44 | The number $(\sqrt{2}+\sqrt{3})^3$ can be writt... | ✗ | 28.36 | 0.0050 | 6 | 100.00% | 46.7 |
| 45 | The medians $AD$, $BE$, and $CF$ of triangle $A... | ✗ | 28.78 | 0.0077 | 8 | 62.50% | 33.1 |
| 46 | A sheet of 8-inch by 10-inch paper is placed on... | ✓ | 26.52 | 0.0053 | 8 | 50.00% | 17.5 |
| 47 | A regular tetrahedron is a triangular pyramid i... | ✓ | 30.43 | 0.0053 | 6 | 83.33% | 33.3 |
| 48 | Find the minimum value of \[17 \log_{30} x - 3 ... | ✗ | 57.09 | 0.0096 | 9 | 77.78% | 46.7 |
| 49 | If $0 < \theta < \frac{\pi}{2}$ and $\sqrt{3} \... | ✓ | 44.73 | 0.0087 | 8 | 62.50% | 25.6 |
| 50 | Suppose $a$ and $b$ are positive integers such ... | ✓ | 49.06 | 0.0074 | 7 | 71.43% | 35.0 |
| 51 | Estimate $14.7923412^2$ to the nearest hundred. | ✗ | 24.29 | 0.0032 | 6 | 50.00% | 16.7 |
| 52 | What is the sum of the lengths of the $\textbf{... | ✗ | 4.10 | 0.0000 | - | - | - |
| 53 | Ellen baked $2$ dozen cupcakes of which half co... | ✗ | 39.53 | 0.0043 | 7 | 57.14% | 17.9 |
| 54 | The smallest distance between the origin and a ... | ✗ | 37.03 | 0.0094 | 10 | 90.00% | 33.0 |
| 55 | Tim wants to create a circle graph showing the ... | ✓ | 35.69 | 0.0059 | 6 | 83.33% | 30.8 |
| 56 | Spinner I is divided into four equal sections l... | ✓ | 21.92 | 0.0052 | 6 | 83.33% | 22.5 |
| 57 | The set $\{5, 8, 10, 18, 19, 28, 30, x\}$ has e... | ✗ | 22.63 | 0.0036 | 5 | 80.00% | 23.0 |
| 58 | Three mutually tangent spheres of radius 1 rest... | ✗ | 21.59 | 0.0052 | 5 | 100.00% | 28.0 |
| 59 | Let $z_1,$ $z_2,$ $z_3$ be complex numbers such... | ✓ | 28.80 | 0.0094 | 8 | 75.00% | 42.5 |
| 60 | On a true-false test of 100 items, every questi... | ✓ | 33.07 | 0.0078 | 8 | 50.00% | 27.5 |
| 61 | Billy shoots an arrow from 10 feet above the gr... | ✗ | 28.74 | 0.0061 | 7 | 71.43% | 23.6 |
| 62 | The graph of $f(x)=\frac{2x}{x^2-5x-14}$ has ve... | ✓ | 22.91 | 0.0050 | 8 | 50.00% | 21.2 |
| 63 | In the diagram shown here (which is not drawn t... | ✗ | 5.70 | 0.0000 | - | - | - |
| 64 | For every positive integer $n$, let $\text{mod}... | ✓ | 27.30 | 0.0072 | 8 | 75.00% | 30.6 |
| 65 | Find the number of ordered pairs $(a,b)$ of int... | ✗ | 25.27 | 0.0055 | 6 | 100.00% | 38.3 |
| 66 | Suppose a function $f(x)$ has domain $(-\infty,... | ✓ | 23.23 | 0.0036 | 5 | 100.00% | 20.0 |
| 67 | A student brings whole cherry and cheese danish... | ✓ | 27.59 | 0.0076 | 8 | 75.00% | 31.2 |
| 68 | The parabola with equation $y=ax^2+bx+c$ and ve... | ✓ | 33.25 | 0.0070 | 9 | 66.67% | 34.4 |
| 69 | Let $S$ be the set of points $(a,b)$ in the coo... | ✗ | 25.56 | 0.0109 | 9 | 66.67% | 41.1 |
| 70 | If $c$ is a nonzero constant such that $x^2+cx+... | ✗ | 30.90 | 0.0047 | 6 | 83.33% | 33.3 |
| 71 | Let $x$ and $y$ be positive real numbers.  Find... | ✗ | 126.92 | 0.0124 | 9 | 77.78% | 70.0 |
| 72 | Let $\omega$ be a complex number such that $|\o... | ✗ | 27.83 | 0.0075 | 9 | 66.67% | 25.0 |
| 73 | A sequence $(a_n)$ is defined as follows: \[a_{... | ✗ | 5.10 | 0.0000 | - | - | - |
| 74 | Find the domain of $\sqrt{6-x-x^2}$. | ✓ | 24.19 | 0.0059 | 8 | 87.50% | 19.4 |
| 75 | An angle $x$ is chosen at random from the inter... | ✗ | 10.12 | 0.0000 | - | - | - |
| 76 | Find the value of $6+\frac{1}{2+\frac{1}{6+\fra... | ✓ | 29.06 | 0.0071 | 8 | 100.00% | 31.2 |
| 77 | Let $\alpha$ and $\beta$ be angles for which \[... | ✗ | 26.00 | 0.0068 | 7 | 85.71% | 51.4 |
| 78 | Bill walks $\frac{1}{2}$ mile south, then $\fra... | ✗ | 21.36 | 0.0047 | 8 | 62.50% | 17.5 |
| 79 | Anna, Bertram, Carli, and David have a competit... | ✗ | 23.92 | 0.0130 | 8 | 62.50% | 40.6 |
| 80 | What is the minimum value of the expression $x^... | ✓ | 20.37 | 0.0050 | 6 | 83.33% | 25.8 |
| 81 | In triangle $ABC$, $\angle BAC = 72^\circ$.  Th... | ✗ | 24.12 | 0.0068 | 7 | 85.71% | 33.6 |
| 82 | A group of people have the number 12345.6789 wr... | ✗ | 16.69 | 0.0042 | 10 | 20.00% | 25.5 |
| 83 | Let $\alpha,$ $\beta,$ and $\gamma$ be three an... | ✗ | 1.95 | 0.0000 | - | - | - |
| 84 | In acute triangle $ABC$, altitudes $AD$, $BE$, ... | ✗ | 23.47 | 0.0074 | 7 | 71.43% | 37.1 |
| 85 | The sum of two numbers is 15. Four times the sm... | ✗ | 24.86 | 0.0056 | 8 | 75.00% | 25.6 |
| 86 | An equilateral triangle has a side of length 12... | ✓ | 19.41 | 0.0038 | 5 | 80.00% | 21.0 |
| 87 | The polynomial $p(x)$ satisfies $p(1) = 210$ an... | ✗ | 19.00 | 0.0039 | 6 | 50.00% | 28.3 |
| 88 | The height (in meters) of a shot cannonball fol... | ✗ | 22.56 | 0.0054 | 7 | 71.43% | 29.3 |
| 89 | The data in the stem and leaf plot shown are th... | ✗ | 19.40 | 0.0046 | 5 | 80.00% | 21.0 |
| 90 | What is the sum of all integer values of $x$ su... | ✗ | 28.08 | 0.0063 | 7 | 100.00% | 30.7 |
| 91 | Let $0, a, b, c$ be the vertices of a square in... | ✗ | 26.52 | 0.0095 | 9 | 77.78% | 31.7 |
| 92 | In trapezoid $ABCD$ with bases $\overline{AB}$ ... | ✗ | 22.88 | 0.0062 | 8 | 50.00% | 41.9 |
| 93 | It is a beautiful day at the beach and ten beac... | ✗ | 19.60 | 0.0073 | 8 | 37.50% | 20.0 |
| 94 | Two eight-sided dice each have faces numbered 1... | ✓ | 23.43 | 0.0063 | 7 | 71.43% | 26.4 |
| 95 | Two sequences $A=\{a_0, a_1, a_2,\ldots\}$ and ... | ✗ | 27.89 | 0.0090 | 9 | 77.78% | 38.9 |
| 96 | Each day, two out of the three teams in a class... | ✗ | 23.88 | 0.0059 | 6 | 83.33% | 28.3 |
| 97 | Tom got a Mr. Potato Head for his birthday. It ... | ✓ | 20.19 | 0.0045 | 9 | 33.33% | 18.9 |
| 98 | I draw a card from a standard 52-card deck.  If... | ✗ | 27.96 | 0.0088 | 9 | 55.56% | 31.7 |
| 99 | Find the number of quadratic equations of the f... | ✗ | 27.36 | 0.0097 | 8 | 87.50% | 33.8 |
| 100 | In Cartesian space, three spheres centered at $... | ✓ | 24.42 | 0.0080 | 9 | 66.67% | 29.4 |
