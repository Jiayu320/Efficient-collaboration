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
| 路由模型 (gemini-2.5-pro) | 2.510 | 93.75 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 7.971 | 100% |
| 规划过程中启动的任务数 | 6 / 7 | 85.7% |
| 规划与执行重叠的任务数 | 6 / 7 | 85.7% |
| 第一个任务规划完成时间 | 3.289 | - |
| 最后一个任务规划完成时间 | 7.939 | - |
| 最后一个任务执行完成时间 | 11.659 | - |
| 任务总执行时间(累计) | 12.619 | - |
| 流水线加速比 | 1.94x | - |
| 并行效率 | 108.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 7 | 12.619 | - |
| 规划模型 | 1 | 9.976 | - |
| 顺序总时间 | - | 22.595 | - |
| 并行总时间 | - | 11.659 | 1.94x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For Part 1, define a single set S that encodes all k sparse sets S_1, ..., S_k. Use a fixed-length binary prefix for each set's index to distinguish its elements. What is the formal definition of this set S? | 大模型 | 3.289 | 4.716 | 1.427 | 2 |
| 2 | Using the definition of S from Step 1 and the fact that each S_i is sparse (bounded by a polynomial p_i(n)), prove that S is also sparse by deriving a polynomial bound for |S^{=m}|, the number of strings of length m in S? | 大模型 | 4.716 | 6.489 | 1.773 | 3 |
| 3 | Describe the deterministic polynomial-time algorithm for an oracle Turing machine M which, given oracle access to the set S from Step 1 and an input <x, i>, decides if x is in S_i? | 大模型 | 4.782 | 6.209 | 1.427 | 4 |
| 4 | For Part 2, prove that P_bad-angel = P by showing both P_bad-angel ⊆ P and P ⊆ P_bad-angel. What are the constructions for the required Turing Machines in each direction? | 大模型 | 5.486 | 7.605 | 2.119 | 5 |
| 5 | Based on the result from Step 4 that P = P_bad-angel, what can be concluded about the question 'Is NP = P_bad-angel?' in relation to major open problems in complexity theory? | 大模型 | 7.605 | 8.894 | 1.289 | 6 |
| 6 | For Part 3, define a sparse oracle set S_L for a language L in P_angel. The set must encode the individual bits of all angel strings {α_n} using a unary encoding of the output of an injective pairing function pair(n, i). What is the precise definition of S_L? | 大模型 | 7.075 | 9.194 | 2.119 | 7 |
| 7 | Describe the complete algorithm for a deterministic polynomial-time oracle TM M' that uses the oracle S_L from Step 6 to decide the language L. The algorithm must detail the process of reconstructing the angel string α_n for an input x of length n before simulating the original P_angel machine M? | 大模型 | 9.194 | 11.659 | 2.465 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            8.37s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 3.29s - 4.72s
步骤 2 |          ############                                      | 4.72s - 6.49s
步骤 3 |          ##########                                        | 4.78s - 6.21s
步骤 4 |               ###############                              | 5.49s - 7.60s
步骤 6 |                           ###############                  | 7.08s - 9.19s
步骤 5 |                              ##########                    | 7.60s - 8.89s
步骤 7 |                                          ################# | 9.19s - 11.66s
```

