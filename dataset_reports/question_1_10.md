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
- 正确数量: 42
- 准确率: 42.00%
- 平均执行时间: 28.04 秒
- 平均成本: $0.0060

## 任务规划指标

- 平均任务步骤数: 7.35
- 平均压缩比例: 74.55%
- 平均每步骤Token限制: 29.10 tokens

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 2.204 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 11.558 秒

### 生成速度
- 小模型平均每秒生成token数: 0.48 tokens/s
- 大模型平均每秒生成token数: 4.14 tokens/s
- 路由模型平均每秒生成token数: 4.68 tokens/s
- 总平均每秒生成token数: 9.30 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Three semicircles of radius 1 are constructed o... | ✗ | 26.51 | 0.0066 | 8 | 62.50% | 26.9 |
| 2 | What is the distance between the two intersecti... | ✗ | 29.06 | 0.0053 | 6 | 100.00% | 35.0 |
| 3 | By joining alternate vertices of a regular hexa... | ✗ | 32.22 | 0.0088 | 10 | 70.00% | 28.5 |
| 4 | Two parallel chords in a circle have lengths 10... | ✓ | 26.82 | 0.0085 | 8 | 87.50% | 28.1 |
| 5 | Find all solutions to \[\sin \left( \tan^{-1} (... | ✗ | 27.06 | 0.0051 | 8 | 75.00% | 26.2 |
| 6 | There exists a polynomial $P$ of degree 5 with ... | ✓ | 27.75 | 0.0087 | 8 | 87.50% | 38.8 |
| 7 | Triangle $ABC$ has three different integer side... | ✗ | 22.40 | 0.0057 | 7 | 71.43% | 24.3 |
| 8 | Let $x,$ $y,$ and $z$ be positive real numbers ... | ✗ | 21.40 | 0.0031 | 8 | 62.50% | 33.1 |
| 9 | Simplify: $\frac{\sqrt{2.5^2-0.7^2}}{2.7-2.5}$. | ✓ | 20.00 | 0.0027 | 6 | 66.67% | 20.0 |
| 10 | Four points, $A$, $B$, $C$, and $D$, are chosen... | ✓ | 20.98 | 0.0060 | 7 | 57.14% | 32.1 |
| 11 | Determine the number of solutions in $x$ of the... | ✓ | 25.84 | 0.0063 | 6 | 100.00% | 35.8 |
| 12 | On the graph of $y=(x+2)^4-100$, how many point... | ✗ | 23.40 | 0.0059 | 6 | 83.33% | 30.8 |
| 13 | Convert $\frac{3}{16}$ to base 2. Express your ... | ✓ | 28.61 | 0.0052 | 7 | 71.43% | 30.7 |
| 14 | Let $S$ be the set of points $(a,b)$ with $0 \l... | ✗ | 26.41 | 0.0080 | 8 | 50.00% | 41.2 |
| 15 | What is the perimeter, in units, of a rhombus i... | ✓ | 21.12 | 0.0046 | 6 | 66.67% | 25.0 |
| 16 | Three schools have a chess tournament. Four pla... | ✗ | 25.57 | 0.0072 | 8 | 75.00% | 22.5 |
| 17 | Three distinct integers $a,$ $b,$ and $c$ have ... | ✓ | 26.75 | 0.0088 | 10 | 70.00% | 28.5 |
| 18 | Determine $w^2+x^2+y^2+z^2$ if \[\begin{aligned... | ✗ | 26.07 | 0.0060 | 9 | 66.67% | 31.7 |
| 19 | If $a$ and $b$ are positive integers such that ... | ✗ | 27.22 | 0.0069 | 9 | 100.00% | 21.7 |
| 20 | Find the maximum value of \[\frac{x - y}{x^4 + ... | ✓ | 30.42 | 0.0084 | 10 | 90.00% | 24.5 |
| 21 | Let $\mathbb{Q}^+$ denote the set of positive r... | ✗ | 24.73 | 0.0066 | 7 | 71.43% | 42.1 |
| 22 | Find the sum of all complex numbers $z$ that sa... | ✗ | 27.44 | 0.0082 | 6 | 83.33% | 60.0 |
| 23 | The sides of a triangle with positive area have... | ✓ | 21.67 | 0.0047 | 5 | 80.00% | 36.0 |
| 24 | What is the smallest positive integer $n$ for w... | ✗ | 29.81 | 0.0050 | 7 | 71.43% | 29.3 |
| 25 | Find a nonzero monic polynomial $P(x)$ with int... | ✗ | 9.95 | 0.0000 | - | - | - |
| 26 | There exist two complex numbers $c$, say $c_1$ ... | ✗ | 28.17 | 0.0080 | 8 | 62.50% | 30.6 |
| 27 | A $30^\circ$-$60^\circ$-$90^\circ$ triangle is ... | ✗ | 37.63 | 0.0066 | 8 | 75.00% | 30.6 |
| 28 | The greatest common divisor of positive integer... | ✗ | 31.11 | 0.0064 | 7 | 85.71% | 28.6 |
| 29 | A $\textit{palindrome}$ is a positive integer w... | ✓ | 29.38 | 0.0072 | 8 | 75.00% | 33.8 |
| 30 | How many positive and negative integers is $12$... | ✓ | 25.68 | 0.0038 | 7 | 71.43% | 18.6 |
| 31 | In triangle $ABC$, $AB = AC = 5$ and $BC = 6$. ... | ✗ | 34.59 | 0.0100 | 9 | 66.67% | 26.7 |
| 32 | A $\textit{palindrome}$ is an integer that read... | ✗ | 5.16 | 0.0000 | - | - | - |
| 33 | Suppose that the least common multiple of the f... | ✗ | 43.26 | 0.0110 | 9 | 66.67% | 63.9 |
| 34 | Randy presses RAND on his calculator twice to o... | ✗ | 27.36 | 0.0065 | 8 | 75.00% | 28.1 |
| 35 | You have seven bags of gold coins. Each bag has... | ✓ | 35.53 | 0.0054 | 5 | 100.00% | 26.0 |
| 36 | How many digits are in the value of the followi... | ✗ | 25.06 | 0.0048 | 8 | 75.00% | 24.4 |
| 37 | Square $ABCD$ has side length $s$, a circle cen... | ✗ | 42.62 | 0.0083 | 9 | 88.89% | 33.9 |
| 38 | How many positive  cubes  divide $3!\cdot 5!\cd... | ✗ | 24.28 | 0.0051 | 8 | 50.00% | 26.9 |
| 39 | What is the value of $b$ if $5^b + 5^b + 5^b + ... | ✓ | 28.14 | 0.0054 | 8 | 75.00% | 26.2 |
| 40 | The parabola $y = ax^2 + bx + c$ crosses the $x... | ✓ | 29.45 | 0.0095 | 9 | 77.78% | 26.1 |
| 41 | One line is defined by \[\begin{pmatrix} 3 \\ -... | ✓ | 30.00 | 0.0051 | 6 | 66.67% | 25.0 |
| 42 | A circle of radius 5 with its center at $(0,0)$... | ✗ | 26.39 | 0.0053 | 6 | 83.33% | 24.2 |
| 43 | There exist constants $r,$ $s,$ and $t$ so that... | ✗ | 5.04 | 0.0000 | - | - | - |
| 44 | The number $(\sqrt{2}+\sqrt{3})^3$ can be writt... | ✗ | 32.99 | 0.0064 | 10 | 50.00% | 25.5 |
| 45 | The medians $AD$, $BE$, and $CF$ of triangle $A... | ✓ | 26.78 | 0.0061 | 7 | 71.43% | 27.9 |
| 46 | A sheet of 8-inch by 10-inch paper is placed on... | ✓ | 27.57 | 0.0033 | 5 | 60.00% | 17.0 |
| 47 | A regular tetrahedron is a triangular pyramid i... | ✓ | 29.09 | 0.0036 | 4 | 100.00% | 26.2 |
| 48 | Find the minimum value of \[17 \log_{30} x - 3 ... | ✓ | 39.47 | 0.0085 | 9 | 88.89% | 37.2 |
| 49 | If $0 < \theta < \frac{\pi}{2}$ and $\sqrt{3} \... | ✗ | 34.94 | 0.0061 | 8 | 62.50% | 24.4 |
| 50 | Suppose $a$ and $b$ are positive integers such ... | ✗ | 32.19 | 0.0054 | 7 | 57.14% | 25.0 |
| 51 | Estimate $14.7923412^2$ to the nearest hundred. | ✗ | 34.82 | 0.0034 | 6 | 66.67% | 19.2 |
| 52 | What is the sum of the lengths of the $\textbf{... | ✗ | 6.72 | 0.0000 | - | - | - |
| 53 | Ellen baked $2$ dozen cupcakes of which half co... | ✗ | 23.91 | 0.0038 | 7 | 57.14% | 12.9 |
| 54 | The smallest distance between the origin and a ... | ✗ | 41.61 | 0.0084 | 10 | 100.00% | 26.5 |
| 55 | Tim wants to create a circle graph showing the ... | ✓ | 29.07 | 0.0055 | 6 | 83.33% | 22.5 |
| 56 | Spinner I is divided into four equal sections l... | ✗ | 37.18 | 0.0062 | 8 | 75.00% | 29.4 |
| 57 | The set $\{5, 8, 10, 18, 19, 28, 30, x\}$ has e... | ✓ | 28.93 | 0.0046 | 6 | 83.33% | 25.0 |
| 58 | Three mutually tangent spheres of radius 1 rest... | ✓ | 21.54 | 0.0041 | 5 | 60.00% | 28.0 |
| 59 | Let $z_1,$ $z_2,$ $z_3$ be complex numbers such... | ✗ | 28.39 | 0.0076 | 8 | 75.00% | 30.6 |
| 60 | On a true-false test of 100 items, every questi... | ✓ | 29.74 | 0.0072 | 9 | 44.44% | 20.0 |
| 61 | Billy shoots an arrow from 10 feet above the gr... | ✗ | 35.13 | 0.0060 | 7 | 71.43% | 20.7 |
| 62 | The graph of $f(x)=\frac{2x}{x^2-5x-14}$ has ve... | ✓ | 25.14 | 0.0049 | 8 | 37.50% | 30.0 |
| 63 | In the diagram shown here (which is not drawn t... | ✗ | 2.70 | 0.0000 | - | - | - |
| 64 | For every positive integer $n$, let $\text{mod}... | ✗ | 39.90 | 0.0105 | 9 | 100.00% | 30.0 |
| 65 | Find the number of ordered pairs $(a,b)$ of int... | ✗ | 29.16 | 0.0054 | 6 | 100.00% | 26.7 |
| 66 | Suppose a function $f(x)$ has domain $(-\infty,... | ✓ | 26.98 | 0.0033 | 6 | 66.67% | 25.0 |
| 67 | A student brings whole cherry and cheese danish... | ✗ | 32.46 | 0.0095 | 9 | 66.67% | 27.2 |
| 68 | The parabola with equation $y=ax^2+bx+c$ and ve... | ✓ | 34.16 | 0.0045 | 5 | 80.00% | 32.0 |
| 69 | Let $S$ be the set of points $(a,b)$ in the coo... | ✗ | 25.79 | 0.0075 | 9 | 66.67% | 25.0 |
| 70 | If $c$ is a nonzero constant such that $x^2+cx+... | ✗ | 25.69 | 0.0039 | 5 | 100.00% | 25.0 |
| 71 | Let $x$ and $y$ be positive real numbers.  Find... | ✗ | 35.24 | 0.0127 | 10 | 70.00% | 41.0 |
| 72 | Let $\omega$ be a complex number such that $|\o... | ✗ | 39.71 | 0.0079 | 9 | 100.00% | 26.7 |
| 73 | A sequence $(a_n)$ is defined as follows: \[a_{... | ✗ | 28.38 | 0.0055 | 6 | 100.00% | 26.7 |
| 74 | Find the domain of $\sqrt{6-x-x^2}$. | ✓ | 27.11 | 0.0047 | 7 | 100.00% | 19.3 |
| 75 | An angle $x$ is chosen at random from the inter... | ✗ | 12.26 | 0.0000 | - | - | - |
| 76 | Find the value of $6+\frac{1}{2+\frac{1}{6+\fra... | ✓ | 36.12 | 0.0085 | 8 | 100.00% | 40.0 |
| 77 | Let $\alpha$ and $\beta$ be angles for which \[... | ✓ | 30.21 | 0.0069 | 8 | 75.00% | 41.9 |
| 78 | Bill walks $\frac{1}{2}$ mile south, then $\fra... | ✓ | 21.67 | 0.0042 | 6 | 83.33% | 20.0 |
| 79 | Anna, Bertram, Carli, and David have a competit... | ✓ | 26.16 | 0.0101 | 6 | 83.33% | 51.7 |
| 80 | What is the minimum value of the expression $x^... | ✓ | 20.56 | 0.0029 | 4 | 75.00% | 32.5 |
| 81 | In triangle $ABC$, $\angle BAC = 72^\circ$.  Th... | ✓ | 22.73 | 0.0053 | 5 | 60.00% | 55.0 |
| 82 | A group of people have the number 12345.6789 wr... | ✗ | 29.13 | 0.0096 | 10 | 20.00% | 14.5 |
| 83 | Let $\alpha,$ $\beta,$ and $\gamma$ be three an... | ✗ | 36.78 | 0.0054 | 7 | 57.14% | 28.6 |
| 84 | In acute triangle $ABC$, altitudes $AD$, $BE$, ... | ✗ | 30.34 | 0.0085 | 8 | 75.00% | 30.0 |
| 85 | The sum of two numbers is 15. Four times the sm... | ✓ | 34.03 | 0.0049 | 6 | 100.00% | 22.5 |
| 86 | An equilateral triangle has a side of length 12... | ✓ | 29.25 | 0.0026 | 4 | 75.00% | 20.0 |
| 87 | The polynomial $p(x)$ satisfies $p(1) = 210$ an... | ✗ | 33.01 | 0.0055 | 6 | 83.33% | 34.2 |
| 88 | The height (in meters) of a shot cannonball fol... | ✗ | 25.40 | 0.0040 | 5 | 80.00% | 25.0 |
| 89 | The data in the stem and leaf plot shown are th... | ✓ | 30.23 | 0.0049 | 6 | 66.67% | 31.7 |
| 90 | What is the sum of all integer values of $x$ su... | ✓ | 50.40 | 0.0060 | 7 | 100.00% | 26.4 |
| 91 | Let $0, a, b, c$ be the vertices of a square in... | ✗ | 27.59 | 0.0082 | 9 | 77.78% | 30.0 |
| 92 | In trapezoid $ABCD$ with bases $\overline{AB}$ ... | ✗ | 37.62 | 0.0087 | 8 | 62.50% | 26.2 |
| 93 | It is a beautiful day at the beach and ten beac... | ✓ | 23.62 | 0.0052 | 8 | 37.50% | 23.8 |
| 94 | Two eight-sided dice each have faces numbered 1... | ✓ | 23.43 | 0.0061 | 7 | 71.43% | 31.4 |
| 95 | Two sequences $A=\{a_0, a_1, a_2,\ldots\}$ and ... | ✗ | 32.88 | 0.0082 | 10 | 70.00% | 29.0 |
| 96 | Each day, two out of the three teams in a class... | ✓ | 21.90 | 0.0059 | 5 | 80.00% | 34.0 |
| 97 | Tom got a Mr. Potato Head for his birthday. It ... | ✓ | 23.23 | 0.0048 | 9 | 33.33% | 13.3 |
| 98 | I draw a card from a standard 52-card deck.  If... | ✗ | 36.48 | 0.0118 | 10 | 60.00% | 23.5 |
| 99 | Find the number of quadratic equations of the f... | ✗ | 30.97 | 0.0101 | 8 | 87.50% | 38.1 |
| 100 | In Cartesian space, three spheres centered at $... | ✗ | 27.14 | 0.0064 | 7 | 85.71% | 32.9 |
