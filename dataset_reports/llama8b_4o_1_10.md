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
- 正确数量: 47
- 准确率: 47.00%
- 平均执行时间: 31.18 秒
- 平均成本: $0.0074

## 任务规划指标

- 平均任务步骤数: 7.21
- 平均压缩比例: 84.40%
- 平均每步骤Token限制: 36.52 tokens

## 性能指标

### 首个令牌响应时间 (TTFT)
- 平均首个令牌响应时间: 2.229 秒

### 去除TTFT的执行时间
- 平均去除TTFT的执行时间: 13.365 秒

### 生成速度
- 小模型平均每秒生成token数: 0.34 tokens/s
- 大模型平均每秒生成token数: 6.33 tokens/s
- 路由模型平均每秒生成token数: 4.72 tokens/s
- 总平均每秒生成token数: 11.39 tokens/s

## 详细结果

| # | 问题 | 正确? | 执行时间(秒) | 成本($) | 步骤数 | 压缩比例 | 平均Token |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Three semicircles of radius 1 are constructed o... | ✓ | 31.62 | 0.0055 | 6 | 83.33% | 38.3 |
| 2 | What is the distance between the two intersecti... | ✓ | 31.55 | 0.0069 | 7 | 100.00% | 52.9 |
| 3 | By joining alternate vertices of a regular hexa... | ✗ | 23.05 | 0.0057 | 6 | 66.67% | 40.0 |
| 4 | Two parallel chords in a circle have lengths 10... | ✗ | 27.55 | 0.0048 | 5 | 80.00% | 27.0 |
| 5 | Find all solutions to \[\sin \left( \tan^{-1} (... | ✓ | 26.84 | 0.0049 | 6 | 100.00% | 33.3 |
| 6 | There exists a polynomial $P$ of degree 5 with ... | ✓ | 30.78 | 0.0092 | 7 | 100.00% | 51.4 |
| 7 | Triangle $ABC$ has three different integer side... | ✓ | 27.22 | 0.0098 | 9 | 77.78% | 35.6 |
| 8 | Let $x,$ $y,$ and $z$ be positive real numbers ... | ✗ | 27.37 | 0.0058 | 7 | 71.43% | 42.9 |
| 9 | Simplify: $\frac{\sqrt{2.5^2-0.7^2}}{2.7-2.5}$. | ✓ | 19.93 | 0.0020 | 4 | 75.00% | 10.0 |
| 10 | Four points, $A$, $B$, $C$, and $D$, are chosen... | ✓ | 39.52 | 0.0064 | 6 | 100.00% | 19.2 |
| 11 | Determine the number of solutions in $x$ of the... | ✓ | 39.23 | 0.0078 | 9 | 100.00% | 27.8 |
| 12 | On the graph of $y=(x+2)^4-100$, how many point... | ✓ | 34.21 | 0.0045 | 6 | 100.00% | 21.7 |
| 13 | Convert $\frac{3}{16}$ to base 2. Express your ... | ✓ | 29.85 | 0.0066 | 9 | 88.89% | 11.1 |
| 14 | Let $S$ be the set of points $(a,b)$ with $0 \l... | ✗ | 46.89 | 0.0200 | 9 | 88.89% | 102.2 |
| 15 | What is the perimeter, in units, of a rhombus i... | ✗ | 1.89 | 0.0000 | - | - | - |
| 16 | Three schools have a chess tournament. Four pla... | ✓ | 19.68 | 0.0042 | 4 | 75.00% | 26.2 |
| 17 | Three distinct integers $a,$ $b,$ and $c$ have ... | ✗ | 29.91 | 0.0088 | 8 | 87.50% | 39.4 |
| 18 | Determine $w^2+x^2+y^2+z^2$ if \[\begin{aligned... | ✗ | 28.79 | 0.0064 | 6 | 100.00% | 24.2 |
| 19 | If $a$ and $b$ are positive integers such that ... | ✓ | 42.35 | 0.0106 | 7 | 100.00% | 54.3 |
| 20 | Find the maximum value of \[\frac{x - y}{x^4 + ... | ✗ | 5.60 | 0.0000 | - | - | - |
| 21 | Let $\mathbb{Q}^+$ denote the set of positive r... | ✓ | 45.95 | 0.0099 | 7 | 100.00% | 68.6 |
| 22 | Find the sum of all complex numbers $z$ that sa... | ✗ | 39.27 | 0.0089 | 9 | 66.67% | 42.2 |
| 23 | The sides of a triangle with positive area have... | ✓ | 39.82 | 0.0131 | 8 | 75.00% | 81.2 |
| 24 | What is the smallest positive integer $n$ for w... | ✓ | 26.87 | 0.0049 | 7 | 71.43% | 19.3 |
| 25 | Find a nonzero monic polynomial $P(x)$ with int... | ✓ | 45.70 | 0.0087 | 8 | 100.00% | 45.6 |
| 26 | There exist two complex numbers $c$, say $c_1$ ... | ✗ | 31.90 | 0.0080 | 7 | 71.43% | 35.7 |
| 27 | A $30^\circ$-$60^\circ$-$90^\circ$ triangle is ... | ✗ | 34.91 | 0.0073 | 8 | 100.00% | 35.0 |
| 28 | The greatest common divisor of positive integer... | ✓ | 24.35 | 0.0058 | 7 | 85.71% | 16.4 |
| 29 | A $\textit{palindrome}$ is a positive integer w... | ✗ | 26.06 | 0.0063 | 7 | 71.43% | 30.0 |
| 30 | How many positive and negative integers is $12$... | ✓ | 19.34 | 0.0030 | 4 | 100.00% | 18.8 |
| 31 | In triangle $ABC$, $AB = AC = 5$ and $BC = 6$. ... | ✗ | 34.43 | 0.0070 | 6 | 83.33% | 28.3 |
| 32 | A $\textit{palindrome}$ is an integer that read... | ✗ | 32.16 | 0.0124 | 9 | 66.67% | 33.3 |
| 33 | Suppose that the least common multiple of the f... | ✓ | 45.94 | 0.0197 | 8 | 100.00% | 125.0 |
| 34 | Randy presses RAND on his calculator twice to o... | ✗ | 38.18 | 0.0103 | 9 | 77.78% | 67.8 |
| 35 | You have seven bags of gold coins. Each bag has... | ✗ | 34.56 | 0.0100 | 9 | 100.00% | 25.6 |
| 36 | How many digits are in the value of the followi... | ✗ | 22.40 | 0.0031 | 5 | 100.00% | 22.0 |
| 37 | Square $ABCD$ has side length $s$, a circle cen... | ✗ | 38.81 | 0.0089 | 8 | 62.50% | 48.8 |
| 38 | How many positive  cubes  divide $3!\cdot 5!\cd... | ✓ | 36.66 | 0.0064 | 6 | 83.33% | 41.7 |
| 39 | What is the value of $b$ if $5^b + 5^b + 5^b + ... | ✓ | 35.84 | 0.0031 | 5 | 80.00% | 26.0 |
| 40 | The parabola $y = ax^2 + bx + c$ crosses the $x... | ✓ | 63.22 | 0.0141 | 10 | 60.00% | 51.0 |
| 41 | One line is defined by \[\begin{pmatrix} 3 \\ -... | ✗ | 46.68 | 0.0123 | 8 | 50.00% | 61.2 |
| 42 | A circle of radius 5 with its center at $(0,0)$... | ✗ | 50.86 | 0.0117 | 8 | 75.00% | 44.4 |
| 43 | There exist constants $r,$ $s,$ and $t$ so that... | ✓ | 56.58 | 0.0163 | 8 | 62.50% | 75.0 |
| 44 | The number $(\sqrt{2}+\sqrt{3})^3$ can be writt... | ✗ | 28.42 | 0.0050 | 7 | 100.00% | 24.3 |
| 45 | The medians $AD$, $BE$, and $CF$ of triangle $A... | ✗ | 42.81 | 0.0141 | 9 | 77.78% | 81.1 |
| 46 | A sheet of 8-inch by 10-inch paper is placed on... | ✗ | 20.53 | 0.0030 | 4 | 100.00% | 22.5 |
| 47 | A regular tetrahedron is a triangular pyramid i... | ✗ | 27.64 | 0.0046 | 5 | 100.00% | 34.0 |
| 48 | Find the minimum value of \[17 \log_{30} x - 3 ... | ✓ | 53.83 | 0.0204 | 9 | 88.89% | 132.2 |
| 49 | If $0 < \theta < \frac{\pi}{2}$ and $\sqrt{3} \... | ✓ | 33.97 | 0.0081 | 8 | 100.00% | 26.9 |
| 50 | Suppose $a$ and $b$ are positive integers such ... | ✗ | 34.01 | 0.0079 | 7 | 85.71% | 26.4 |
| 51 | Estimate $14.7923412^2$ to the nearest hundred. | ✗ | 24.27 | 0.0030 | 5 | 100.00% | 13.0 |
| 52 | What is the sum of the lengths of the $\textbf{... | ✗ | 25.24 | 0.0044 | 5 | 80.00% | 11.0 |
| 53 | Ellen baked $2$ dozen cupcakes of which half co... | ✗ | 31.48 | 0.0078 | 8 | 75.00% | 35.6 |
| 54 | The smallest distance between the origin and a ... | ✓ | 27.18 | 0.0078 | 9 | 77.78% | 27.2 |
| 55 | Tim wants to create a circle graph showing the ... | ✓ | 31.94 | 0.0064 | 7 | 85.71% | 15.0 |
| 56 | Spinner I is divided into four equal sections l... | ✗ | 22.50 | 0.0033 | 5 | 80.00% | 17.0 |
| 57 | The set $\{5, 8, 10, 18, 19, 28, 30, x\}$ has e... | ✗ | 24.68 | 0.0035 | 4 | 100.00% | 27.5 |
| 58 | Three mutually tangent spheres of radius 1 rest... | ✗ | 34.01 | 0.0075 | 8 | 62.50% | 27.5 |
| 59 | Let $z_1,$ $z_2,$ $z_3$ be complex numbers such... | ✓ | 28.91 | 0.0067 | 7 | 71.43% | 28.6 |
| 60 | On a true-false test of 100 items, every questi... | ✓ | 26.53 | 0.0063 | 7 | 57.14% | 23.6 |
| 61 | Billy shoots an arrow from 10 feet above the gr... | ✓ | 32.05 | 0.0078 | 9 | 100.00% | 16.1 |
| 62 | The graph of $f(x)=\frac{2x}{x^2-5x-14}$ has ve... | ✓ | 46.09 | 0.0037 | 5 | 60.00% | 48.0 |
| 63 | In the diagram shown here (which is not drawn t... | ✗ | 38.78 | 0.0113 | 7 | 71.43% | 50.0 |
| 64 | For every positive integer $n$, let $\text{mod}... | ✓ | 32.75 | 0.0086 | 8 | 100.00% | 31.2 |
| 65 | Find the number of ordered pairs $(a,b)$ of int... | ✓ | 39.68 | 0.0094 | 7 | 71.43% | 28.6 |
| 66 | Suppose a function $f(x)$ has domain $(-\infty,... | ✓ | 37.02 | 0.0046 | 6 | 83.33% | 40.0 |
| 67 | A student brings whole cherry and cheese danish... | ✗ | 43.39 | 0.0073 | 8 | 62.50% | 23.1 |
| 68 | The parabola with equation $y=ax^2+bx+c$ and ve... | ✓ | 39.15 | 0.0092 | 8 | 75.00% | 63.8 |
| 69 | Let $S$ be the set of points $(a,b)$ in the coo... | ✓ | 45.91 | 0.0071 | 7 | 85.71% | 36.4 |
| 70 | If $c$ is a nonzero constant such that $x^2+cx+... | ✗ | 49.84 | 0.0061 | 9 | 88.89% | 12.2 |
| 71 | Let $x$ and $y$ be positive real numbers.  Find... | ✗ | 43.94 | 0.0074 | 8 | 75.00% | 21.2 |
| 72 | Let $\omega$ be a complex number such that $|\o... | ✗ | 32.47 | 0.0075 | 8 | 100.00% | 34.4 |
| 73 | A sequence $(a_n)$ is defined as follows: \[a_{... | ✗ | 35.15 | 0.0095 | 9 | 88.89% | 41.1 |
| 74 | Find the domain of $\sqrt{6-x-x^2}$. | ✓ | 23.86 | 0.0043 | 6 | 100.00% | 15.0 |
| 75 | An angle $x$ is chosen at random from the inter... | ✗ | 29.82 | 0.0108 | 8 | 87.50% | 56.2 |
| 76 | Find the value of $6+\frac{1}{2+\frac{1}{6+\fra... | ✓ | 33.34 | 0.0096 | 10 | 100.00% | 31.0 |
| 77 | Let $\alpha$ and $\beta$ be angles for which \[... | ✗ | 4.20 | 0.0000 | - | - | - |
| 78 | Bill walks $\frac{1}{2}$ mile south, then $\fra... | ✓ | 19.84 | 0.0035 | 5 | 100.00% | 20.0 |
| 79 | Anna, Bertram, Carli, and David have a competit... | ✗ | 26.78 | 0.0104 | 7 | 100.00% | 38.6 |
| 80 | What is the minimum value of the expression $x^... | ✓ | 30.85 | 0.0076 | 9 | 88.89% | 28.9 |
| 81 | In triangle $ABC$, $\angle BAC = 72^\circ$.  Th... | ✗ | 25.99 | 0.0086 | 8 | 87.50% | 15.6 |
| 82 | A group of people have the number 12345.6789 wr... | ✓ | 25.91 | 0.0109 | 6 | 83.33% | 75.0 |
| 83 | Let $\alpha,$ $\beta,$ and $\gamma$ be three an... | ✓ | 28.26 | 0.0073 | 10 | 70.00% | 17.2 |
| 84 | In acute triangle $ABC$, altitudes $AD$, $BE$, ... | ✓ | 25.90 | 0.0108 | 9 | 77.78% | 36.7 |
| 85 | The sum of two numbers is 15. Four times the sm... | ✓ | 27.10 | 0.0062 | 8 | 87.50% | 14.4 |
| 86 | An equilateral triangle has a side of length 12... | ✓ | 18.05 | 0.0022 | 3 | 100.00% | 18.3 |
| 87 | The polynomial $p(x)$ satisfies $p(1) = 210$ an... | ✗ | 28.44 | 0.0096 | 9 | 66.67% | 46.7 |
| 88 | The height (in meters) of a shot cannonball fol... | ✗ | 30.36 | 0.0074 | 9 | 100.00% | 20.6 |
| 89 | The data in the stem and leaf plot shown are th... | ✗ | 1.23 | 0.0000 | - | - | - |
| 90 | What is the sum of all integer values of $x$ su... | ✓ | 32.61 | 0.0089 | 8 | 100.00% | 45.0 |
| 91 | Let $0, a, b, c$ be the vertices of a square in... | ✗ | 22.00 | 0.0061 | 7 | 71.43% | 30.0 |
| 92 | In trapezoid $ABCD$ with bases $\overline{AB}$ ... | ✗ | 22.89 | 0.0077 | 7 | 85.71% | 41.4 |
| 93 | It is a beautiful day at the beach and ten beac... | ✗ | 23.76 | 0.0058 | 6 | 83.33% | 24.2 |
| 94 | Two eight-sided dice each have faces numbered 1... | ✗ | 23.21 | 0.0080 | 8 | 87.50% | 23.8 |
| 95 | Two sequences $A=\{a_0, a_1, a_2,\ldots\}$ and ... | ✗ | 19.99 | 0.0000 | - | - | - |
| 96 | Each day, two out of the three teams in a class... | ✗ | 25.03 | 0.0062 | 7 | 71.43% | 22.1 |
| 97 | Tom got a Mr. Potato Head for his birthday. It ... | ✓ | 21.39 | 0.0052 | 5 | 100.00% | 18.0 |
| 98 | I draw a card from a standard 52-card deck.  If... | ✗ | 20.72 | 0.0087 | 8 | 62.50% | 30.6 |
| 99 | Find the number of quadratic equations of the f... | ✗ | 30.39 | 0.0094 | 9 | 77.78% | 44.4 |
| 100 | In Cartesian space, three spheres centered at $... | ✗ | 27.17 | 0.0071 | 8 | 87.50% | 35.6 |
