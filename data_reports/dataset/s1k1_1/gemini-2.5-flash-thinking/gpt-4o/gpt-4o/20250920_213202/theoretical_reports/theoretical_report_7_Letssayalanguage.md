# 问题 7 的理论性能分析报告

## 问题描述

Let's say a language  $L \subseteq \{0,1\}^*$  is in  $\textbf{P}_{angel}$  if there exists a polynomial  $p : \mathbb{N} \mapsto \mathbb{N}$ , a sequence of strings  $\{\alpha_n\}_{n \in \mathbb{N}}$  with  $\alpha_n \in \{0,1\}^{p(n)}$ , and a deterministic polynomial time Turing Machine  $M$  such that for every  $x \in \{0,1\}^n$   $$ x \in L \Leftrightarrow M(x, \alpha_n) = 1 $$  Let us call  $\alpha_n$  to be the *angel string*for all  $x$  of the length  $n$ . Note that the *angel string* is  $\textbf{not}$  similar to a *witness* or *certificate*as used in the definition of  $\textbf{NP}$  For example, all unary languages, even  $UHALT$  which is undecidable, are in  $\textbf{P}_{angel}$  because the \textit{angel string} can simply be a single bit that tells us if the given unary string is in  $UHALT$  or not.


A set  $S \subseteq \Sigma^*$  is said to be **sparse** if there exists a polynomial   $p : \mathbb{N} \mapsto \mathbb{N}$  such that for each  $n \in \mathbb{N}$ , the number of strings of length  $n$  in  $S$  is bounded by  $p(n)$ . In other words,  $|S^{=n}| \leq p(n)$ , where  $S^{=n} \subseteq S$  contains all the strings in  $S$  that are of length  $n$ . 

[list=1]
    [*] Given  $k \in \mathbb{N}$  sparse sets  $S_1, S_2 \ldots S_k$ , show that there exists a sparse set  $S$  and a deterministic polynomial time TM  $M$  with oracle access to  $S$  such that given an input  $\langle x,i \rangle$  the TM  $M$  will accept it if and only if  $x \in S_i$ .
    Define the set  $S$  (note that it need not be computable), and give the description of  $M$  with oracle  $S$ .
    Note that a TM  $M$  with oracle access to  $S$  can query whether  $s \in S$  and get the correct answer in return in constant time. [/*]
    
    [*] Let us define a variant of  $\textbf{P}_{angel}$  called  $\textbf{P}_{bad-angel}$  with a constraint that there should exists a polynomial time algorithm that can **compute** the angel string for any length  $n \in \mathbb{N}$ . In other words, there is a poly-time algorithm  $A$  such that  $\alpha_n = A(n)$ . 
    Is  $\textbf{P} =\textbf{P}_{bad-angel}$ ? Is  $\textbf{NP}=\textbf{P}_{bad-angel}$ ? Justify.
    [/*]
    
    [*] Let the language  $L \in$   $\textbf{P}_{angel}$ . Show that there exists a sparse set  $S_L$  and a deterministic polynomial time TM  $M$  with oracle access to  $S_L$  that can decide the language  $L$ .  [/*]

# 理论性能模型分析

## 模型性能参数

| 模型 | 延迟 (秒) | 吞吐量 (tokens/s) |
| --- | --- | --- |
| 小模型 (gpt-4o) | 0.735 | 144.50 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (gemini-2.5-flash-thinking) | 0.737 | 103.71 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 5.529 | 100% |
| 规划过程中启动的任务数 | 5 / 6 | 83.3% |
| 规划与执行重叠的任务数 | 5 / 6 | 83.3% |
| 第一个任务规划完成时间 | 1.595 | - |
| 最后一个任务规划完成时间 | 5.500 | - |
| 最后一个任务执行完成时间 | 7.910 | - |
| 任务总执行时间(累计) | 8.631 | - |
| 流水线加速比 | 1.92x | - |
| 并行效率 | 109.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 6 | 8.631 | - |
| 规划模型 | 1 | 6.522 | - |
| 顺序总时间 | - | 15.154 | - |
| 并行总时间 | - | 7.910 | 1.92x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Part 1: Define the sparse set S. For each $j \in \{1, \ldots, k\}$ and $x \in S_j$, let the encoded string be $\langle \text{binary}(j), x \rangle$. What is the formal definition of S as a union of these encoded strings? | 大模型 | 1.595 | 2.745 | 1.150 | 2 |
| 2 | Part 1: Describe the deterministic polynomial time Turing Machine M with oracle access to S. Given input $\langle x, i \rangle$, how does M use the oracle S to decide if $x \in S_i$? | 大模型 | 2.745 | 3.965 | 1.219 | 3 |
| 3 | Part 2: Is P = P_bad-angel? Justify by showing both P ⊆ P_bad-angel and P_bad-angel ⊆ P. For P ⊆ P_bad-angel, what is the angel string $\alpha_n$ and how is it computed by A(n)? For P_bad-angel ⊆ P, how does a new DTM M' decide L? | 大模型 | 3.215 | 4.988 | 1.773 | 4 |
| 4 | Part 2: Is NP = P_bad-angel? Justify your answer by relating it to a known open problem in complexity theory, based on the conclusion from Step 3. | 大模型 | 4.988 | 6.277 | 1.289 | 5 |
| 5 | Part 3: Define the sparse set $S_L$. For a language $L \in \textbf{P}_{angel}$ with angel string $\alpha_n$ of length $p(n)$, how is $S_L$ constructed using unary encoding for $n$ and binary encoding for bit index $i$ to ensure sparsity while encoding individual bits of $\alpha_n$? | 大模型 | 4.709 | 6.136 | 1.427 | 6 |
| 6 | Part 3: Describe the deterministic polynomial time Turing Machine M with oracle access to $S_L$. Given input $x$ of length $n$, how does M reconstruct the angel string $\alpha_n$ bit by bit using queries to $S_L$, and then use it to decide $L$? | 大模型 | 6.136 | 7.910 | 1.773 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            6.31s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 1.59s - 2.75s
步骤 2 |          ############                                      | 2.75s - 3.96s
步骤 3 |               #################                            | 3.21s - 4.99s
步骤 5 |                             ##############                 | 4.71s - 6.14s
步骤 4 |                                ############                | 4.99s - 6.28s
步骤 6 |                                           #################| 6.14s - 7.91s
```

