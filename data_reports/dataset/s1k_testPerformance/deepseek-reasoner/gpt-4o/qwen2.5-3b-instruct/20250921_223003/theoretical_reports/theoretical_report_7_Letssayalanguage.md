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
| 路由模型 (deepseek-reasoner) | 1.182 | 46.49 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 17.595 | 100% |
| 规划过程中启动的任务数 | 9 / 9 | 100.0% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 3.096 | - |
| 最后一个任务规划完成时间 | 17.530 | - |
| 最后一个任务执行完成时间 | 18.681 | - |
| 任务总执行时间(累计) | 11.284 | - |
| 流水线加速比 | 2.42x | - |
| 并行效率 | 60.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 4 | 5.394 | - |
| 大模型任务 | 5 | 5.890 | - |
| 规划模型 | 1 | 33.943 | - |
| 顺序总时间 | - | 45.227 | - |
| 并行总时间 | - | 18.681 | 2.42x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For part 1, define the set S as S = { (i, x) | 1 ≤ i ≤ k and x ∈ S_i }, where (i, x) denotes the string formed by concatenating the binary representation of i (using exactly ⌈log2(k)⌉ bits) and then x. | 小模型 | 3.096 | 4.561 | 1.465 | 2 |
| 2 | Verify that S is sparse: for any length m, the number of strings in S of length m is at most k * max_{i} |{ x ∈ S_i : |x| = m - ⌈log2(k)⌉ }|, which is bounded by k * p(m) for some polynomial p. | 大模型 | 4.989 | 6.140 | 1.150 | 3 |
| 3 | Describe the TM M with oracle S: On input 〈x, i〉, encode i into a fixed-length string, form s = (i, x), query if s ∈ S, and accept iff the oracle returns yes. | 小模型 | 6.431 | 7.741 | 1.310 | 4 |
| 4 | For part 2, show that P_bad-angel ⊆ P: given L ∈ P_bad-angel with poly-time algorithms A and M, decide L by computing α_n = A(n) and then output M(x, α_n). | 小模型 | 7.958 | 9.423 | 1.465 | 5 |
| 5 | Show that P ⊆ P_bad-angel: for L ∈ P, let M be a poly-time decider for L. Define A(n) = ε (empty string) and let M'(x, α) = M(x), which is poly-time. | 小模型 | 9.528 | 10.683 | 1.155 | 6 |
| 6 | Conclude that P = P_bad-angel. For NP, since P_bad-angel = P, NP = P_bad-angel if and only if P = NP. | 大模型 | 10.840 | 11.921 | 1.081 | 7 |
| 7 | For part 3, given L ∈ P_angel with advice length p(n) and TM M, define S_L = { (1^n, j) | 0 ≤ j < p(n) and the j-th bit of α_n is 1 } ∪ { (0^n, j) | 0 ≤ j < p(n) and the j-th bit of α_n is 0 }, where (1^n, j) is a string of n '1's followed by the binary representation of j using ⌈log2(p(n))⌉ bits. | 大模型 | 13.766 | 14.985 | 1.219 | 8 |
| 8 | Prove S_L is sparse: for length m, the number of strings is at most 2p(n) for n such that m = n + ⌈log2(p(n))⌉. Since n ≈ m, p(n) is polynomial in m, so the number of strings is O(poly(m)). | 大模型 | 15.637 | 16.926 | 1.289 | 9 |
| 9 | Describe the poly-time oracle TM for L: on input x of length n, for j from 0 to p(n)-1, form string s_j = (1^n, j), query if s_j ∈ S_L, set β[j] = 1 if yes else 0, then output M(x, β). | 大模型 | 17.530 | 18.681 | 1.150 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            15.58s
+------------------------------------------------------------+
步骤 1 |#####                                                       | 3.10s - 4.56s
步骤 2 |       ####                                                 | 4.99s - 6.14s
步骤 3 |            #####                                           | 6.43s - 7.74s
步骤 4 |                  ######                                    | 7.96s - 9.42s
步骤 5 |                        #####                               | 9.53s - 10.68s
步骤 6 |                             ####                           | 10.84s - 11.92s
步骤 7 |                                         ####               | 13.77s - 14.99s
步骤 8 |                                                #####       | 15.64s - 16.93s
步骤 9 |                                                       #####| 17.53s - 18.68s
```

