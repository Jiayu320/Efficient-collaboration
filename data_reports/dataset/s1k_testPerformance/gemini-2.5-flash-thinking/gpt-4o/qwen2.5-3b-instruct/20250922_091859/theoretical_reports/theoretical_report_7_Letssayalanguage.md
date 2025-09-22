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
| 小模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |
| 大模型 (gpt-4o) | 0.735 | 144.50 |
| 路由模型 (gemini-2.5-flash-thinking) | 0.737 | 103.71 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 6.223 | 100% |
| 规划过程中启动的任务数 | 5 / 7 | 71.4% |
| 规划与执行重叠的任务数 | 5 / 7 | 71.4% |
| 第一个任务规划完成时间 | 1.585 | - |
| 最后一个任务规划完成时间 | 6.194 | - |
| 最后一个任务执行完成时间 | 8.254 | - |
| 任务总执行时间(累计) | 10.462 | - |
| 流水线加速比 | 4.68x | - |
| 并行效率 | 126.7% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 3 | 5.169 | - |
| 大模型任务 | 4 | 5.293 | - |
| 规划模型 | 1 | 28.199 | - |
| 顺序总时间 | - | 38.661 | - |
| 并行总时间 | - | 8.254 | 4.68x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For Part 1, define the single sparse set S using an encoding function `encode(i, x)` (e.g., `binary(i) # x`) such that `S = {encode(i, x) | 1 <= i <= k, x in S_i}`. What is the precise definition of S? | 大模型 | 1.585 | 2.805 | 1.219 | 2 |
| 2 | For Part 1, describe the deterministic polynomial time TM M with oracle access to S. Specifically, how does M process an input `(x, i)` to decide if `x in S_i`? | 小模型 | 2.805 | 4.424 | 1.620 | 3 |
| 3 | For Part 2, to show P = P_bad-angel, first prove P is a subset of P_bad-angel. How can a language L in P be represented in P_bad-angel by defining the angel string `alpha_n` and the poly-time algorithm A that computes it? | 小模型 | 2.983 | 4.758 | 1.775 | 4 |
| 4 | For Part 2, to show P = P_bad-angel, next prove P_bad-angel is a subset of P. How can a language L in P_bad-angel be decided by a deterministic polynomial time TM in P, given the existence of a poly-time algorithm A for `alpha_n` and a poly-time TM M? | 小模型 | 4.758 | 6.533 | 1.775 | 5 |
| 5 | For Part 2, to determine if NP = P_bad-angel, what is the relationship between NP, P, and P_bad-angel, and what open problem in complexity theory is relevant to this question? Justify your conclusion. | 大模型 | 6.533 | 7.891 | 1.358 | 6 |
| 6 | For Part 3, define the sparse set S_L for a language L in P_angel. Use an encoding `encode(n, i, b)` (e.g., `1^n 0 binary(i) 0 b`) such that `S_L = {encode(n, i, b) | the i-th bit of alpha_n is b}`. What is the precise definition of S_L? | 大模型 | 5.539 | 6.827 | 1.289 | 7 |
| 7 | For Part 3, describe the deterministic polynomial time TM M with oracle access to S_L that can decide the language L. Detail the steps M takes to reconstruct `alpha_n` and then use it with `M_angel`. | 大模型 | 6.827 | 8.254 | 1.427 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            6.67s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 1.59s - 2.80s
步骤 2 |          ###############                                   | 2.80s - 4.42s
步骤 3 |            ################                                | 2.98s - 4.76s
步骤 4 |                            ################                | 4.76s - 6.53s
步骤 6 |                                   ############             | 5.54s - 6.83s
步骤 5 |                                            ############    | 6.53s - 7.89s
步骤 7 |                                               #############| 6.83s - 8.25s
```

