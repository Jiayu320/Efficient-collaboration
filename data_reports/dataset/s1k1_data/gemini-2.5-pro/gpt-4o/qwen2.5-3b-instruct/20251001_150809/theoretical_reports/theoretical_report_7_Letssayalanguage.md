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
| 路由模型 (gemini-2.5-pro) | 2.510 | 93.75 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 8.291 | 100% |
| 规划过程中启动的任务数 | 3 / 8 | 37.5% |
| 规划与执行重叠的任务数 | 3 / 8 | 37.5% |
| 第一个任务规划完成时间 | 3.427 | - |
| 最后一个任务规划完成时间 | 8.259 | - |
| 最后一个任务执行完成时间 | 28.912 | - |
| 任务总执行时间(累计) | 78.306 | - |
| 流水线加速比 | 2.98x | - |
| 并行效率 | 270.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 32.373 | - |
| 大模型任务 | 6 | 45.932 | - |
| 规划模型 | 1 | 7.992 | - |
| 顺序总时间 | - | 86.298 | - |
| 并行总时间 | - | 28.912 | 2.98x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For Part 1, propose a method to construct a single set S from k sparse sets S_1, S_2, ..., S_k. The construction must encode both the original string x and its source set index i into a new, single string. What is a formal definition for this new set S? | 大模型 | 3.427 | 11.083 | 7.655 | 2 |
| 2 | For Part 2, what is the key difference in the definition of P_bad-angel compared to P_angel? Based on this difference, justify whether P = P_bad-angel by analyzing both inclusions (P ⊆ P_bad-angel and P_bad-angel ⊆ P). | 大模型 | 4.291 | 11.947 | 7.655 | 3 |
| 3 | For Part 3, let L be a language in P_angel. Propose a construction for a set S_L that encodes the necessary 'angel string' (α_n) for each input length n. What is a formal definition for this set S_L? | 大模型 | 5.070 | 12.725 | 7.655 | 4 |
| 4 | Based on the construction in Step 1, prove that the resulting set S is sparse. Your justification should use the fact that each S_i is sparse and that k is a fixed constant. | 大模型 | 11.083 | 18.738 | 7.655 | 5 |
| 5 | Describe the algorithm for a deterministic polynomial-time Turing Machine M that, given oracle access to the set S from Step 1, decides if an input string x belongs to a specific set S_i. | 小模型 | 11.083 | 27.269 | 16.187 | 6 |
| 6 | Based on the conclusion from Step 2 about the relationship between P and P_bad-angel, what is the resulting relationship between NP and P_bad-angel? Does this equivalence depend on any major unsolved problems in complexity theory? | 大模型 | 11.947 | 19.602 | 7.655 | 7 |
| 7 | Based on the construction in Step 3, explain why the set S_L is sparse. How many strings of any given length m can S_L contain at most? | 小模型 | 12.725 | 28.912 | 16.187 | 8 |
| 8 | Describe the algorithm for a deterministic polynomial-time Turing Machine M that, given oracle access to the set S_L from Step 3, can decide the language L for any input x. | 大模型 | 12.725 | 20.381 | 7.655 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            25.48s
+------------------------------------------------------------+
步骤 1 |##################                                          | 3.43s - 11.08s
步骤 2 |  ##################                                        | 4.29s - 11.95s
步骤 3 |   ##################                                       | 5.07s - 12.73s
步骤 4 |                  ##################                        | 11.08s - 18.74s
步骤 5 |                  ######################################    | 11.08s - 27.27s
步骤 6 |                    ##################                      | 11.95s - 19.60s
步骤 7 |                     #######################################| 12.73s - 28.91s
步骤 8 |                     ##################                     | 12.73s - 20.38s
```

