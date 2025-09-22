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
| 规划阶段总时间 (Planner) | 9.315 | 100% |
| 规划过程中启动的任务数 | 7 / 8 | 87.5% |
| 规划与执行重叠的任务数 | 7 / 8 | 87.5% |
| 第一个任务规划完成时间 | 3.321 | - |
| 最后一个任务规划完成时间 | 9.283 | - |
| 最后一个任务执行完成时间 | 11.964 | - |
| 任务总执行时间(累计) | 10.970 | - |
| 流水线加速比 | 3.06x | - |
| 并行效率 | 91.7% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.465 | - |
| 大模型任务 | 7 | 9.505 | - |
| 规划模型 | 1 | 25.677 | - |
| 顺序总时间 | - | 36.647 | - |
| 并行总时间 | - | 11.964 | 3.06x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For Part 1, define a single set S that encodes all information from the k sparse sets S_1, ..., S_k by tagging each string x from S_i with its index i. What is a suitable string-based definition for S using this tagging principle? | 大模型 | 3.321 | 4.471 | 1.150 | 2 |
| 2 | Using the definition of S from Step 1 and the fact that each S_i is sparse with a polynomial bound p_i(n), show that S is also sparse by deriving a polynomial bound for the number of strings of length m in S. Then, describe the algorithm for the oracle TM M that decides if x is in S_i given oracle access to S? | 大模型 | 4.471 | 5.898 | 1.427 | 3 |
| 3 | For Part 2, to prove P = P_bad-angel, first show that P is a subset of P_bad-angel. How can you use a polynomial-time decider for a language L in P to construct the required Turing Machine M and angel string generation algorithm A for P_bad-angel? | 大模型 | 5.209 | 6.497 | 1.289 | 4 |
| 4 | To complete the proof that P = P_bad-angel, show that P_bad-angel is a subset of P. How can you construct a standard deterministic polynomial-time Turing Machine M' for a language L in P_bad-angel by combining the angel string generator A and the verifier M? | 大模型 | 6.497 | 7.855 | 1.358 | 5 |
| 5 | Based on the conclusion from Step 4 that P = P_bad-angel, what can be concluded about the relationship between NP and P_bad-angel, and what fundamental open problem in computer science is this relationship contingent upon? | 小模型 | 7.855 | 9.320 | 1.465 | 6 |
| 6 | For Part 3, to show that any language L in P_angel can be decided with a sparse oracle, define a sparse set S_L that encodes the angel strings {α_n}. How can you define S_L to encode each individual bit of each α_n in a way that facilitates efficient retrieval? | 大模型 | 7.683 | 9.249 | 1.565 | 7 |
| 7 | Describe the polynomial-time algorithm for an oracle TM M' with oracle S_L (as defined in Step 6) that decides a language L in P_angel. How does M' use the oracle to reconstruct the angel string α_n for an input x of length n? | 大模型 | 9.249 | 10.676 | 1.427 | 8 |
| 8 | After the oracle TM M' from Step 7 has successfully reconstructed the angel string α_n, what is the final step it must perform to decide if the original input x belongs to the language L, and why is the entire procedure guaranteed to run in polynomial time? | 大模型 | 10.676 | 11.964 | 1.289 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            8.64s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 3.32s - 4.47s
步骤 2 |       ##########                                           | 4.47s - 5.90s
步骤 3 |             #########                                      | 5.21s - 6.50s
步骤 4 |                      #########                             | 6.50s - 7.86s
步骤 6 |                              ###########                   | 7.68s - 9.25s
步骤 5 |                               ##########                   | 7.86s - 9.32s
步骤 7 |                                         ##########         | 9.25s - 10.68s
步骤 8 |                                                   #########| 10.68s - 11.96s
```

