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
| 规划阶段总时间 (Planner) | 9.560 | 100% |
| 规划过程中启动的任务数 | 8 / 9 | 88.9% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 3.406 | - |
| 最后一个任务规划完成时间 | 9.528 | - |
| 最后一个任务执行完成时间 | 11.759 | - |
| 任务总执行时间(累计) | 11.736 | - |
| 流水线加速比 | 2.03x | - |
| 并行效率 | 99.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 9 | 11.736 | - |
| 规划模型 | 1 | 12.110 | - |
| 顺序总时间 | - | 23.846 | - |
| 并行总时间 | - | 11.759 | 2.03x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For Part 1, define a single set S that encodes all k sparse sets S_1, ..., S_k by tagging each string s from S_i with its index i using the encoding S = { 0^i 1 s | s ∈ S_i, 1 ≤ i ≤ k }? | 大模型 | 3.406 | 4.487 | 1.081 | 2 |
| 2 | Prove that the set S defined in Step 1 is sparse by showing that the number of strings of length m, |S^{=m}|, is bounded by the sum of k polynomials, which is itself a polynomial? | 大模型 | 4.487 | 5.776 | 1.289 | 3 |
| 3 | Describe the deterministic polynomial-time oracle TM M that, given input <x, i>, constructs the query string y = 0^i 1 x and queries the oracle S to decide if x ∈ S_i? | 大模型 | 4.793 | 5.943 | 1.150 | 4 |
| 4 | For Part 2, prove that P_bad-angel ⊆ P by describing how to construct a standard polynomial-time TM M' that, on input x, first runs the polynomial-time algorithm A(|x|) to compute the angel string α_{|x|} and then simulates the P_bad-angel machine M(x, α_{|x|})? | 大模型 | 5.795 | 7.222 | 1.427 | 5 |
| 5 | Complete the proof that P = P_bad-angel by showing P ⊆ P_bad-angel. Then, based on this equality, what is the relationship between P_bad-angel and NP, and why can't a definitive answer be given for their equality? | 大模型 | 7.222 | 8.580 | 1.358 | 6 |
| 6 | For Part 3, to show L ∈ P_angel can be decided by a TM with a sparse oracle, define a sparse set S_L based on the angel strings {α_n}. Use the encoding S_L = { 0^n 1 w | w is a prefix of α_n, for all n ∈ ℕ }? | 大模型 | 7.534 | 8.892 | 1.358 | 7 |
| 7 | Prove that the set S_L defined in Step 6 is sparse by showing that the number of strings of any given length m, |S_L^{=m}|, is bounded by a polynomial in m? | 大模型 | 8.892 | 10.180 | 1.289 | 8 |
| 8 | Describe the algorithm for the deterministic polynomial-time oracle TM M' that uses the oracle S_L. How does M', on input x of length n, reconstruct the angel string α_n in polynomial time by making a series of prefix queries to S_L? | 大模型 | 8.974 | 10.747 | 1.773 | 9 |
| 9 | After reconstructing α_n using the procedure from Step 8, what is the final step the oracle TM M' performs to decide if x ∈ L? | 大模型 | 10.747 | 11.759 | 1.012 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            8.35s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 3.41s - 4.49s
步骤 2 |       ##########                                           | 4.49s - 5.78s
步骤 3 |         #########                                          | 4.79s - 5.94s
步骤 4 |                 ##########                                 | 5.80s - 7.22s
步骤 5 |                           ##########                       | 7.22s - 8.58s
步骤 6 |                             ##########                     | 7.53s - 8.89s
步骤 7 |                                       #########            | 8.89s - 10.18s
步骤 8 |                                       #############        | 8.97s - 10.75s
步骤 9 |                                                    ########| 10.75s - 11.76s
```

