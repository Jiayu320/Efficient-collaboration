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
| 路由模型 (claude-3-5-sonnet-latest) | 1.338 | 51.49 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 12.097 | 100% |
| 规划过程中启动的任务数 | 8 / 9 | 88.9% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 2.561 | - |
| 最后一个任务规划完成时间 | 12.039 | - |
| 最后一个任务执行完成时间 | 13.260 | - |
| 任务总执行时间(累计) | 10.304 | - |
| 流水线加速比 | 2.20x | - |
| 并行效率 | 77.7% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.310 | - |
| 大模型任务 | 8 | 8.994 | - |
| 规划模型 | 1 | 18.816 | - |
| 顺序总时间 | - | 29.120 | - |
| 并行总时间 | - | 13.260 | 2.20x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For part 1, how can we define a sparse set S that encodes membership information from all k sparse sets S₁, S₂, ..., Sₖ in a way that allows efficient retrieval? | 大模型 | 2.561 | 3.643 | 1.081 | 2 |
| 2 | Given the sparse sets S₁, S₂, ..., Sₖ, can we construct S by concatenating strings with their set identifiers, such as S = {⟨x,i⟩ | x ∈ Sᵢ}? Is this set sparse? | 大模型 | 3.960 | 5.041 | 1.081 | 3 |
| 3 | How can we prove that the constructed set S from Step 2 is sparse by establishing an upper bound on |S^=n| in terms of the polynomials bounding each |Sᵢ^=m|? | 大模型 | 5.222 | 6.372 | 1.150 | 4 |
| 4 | What is the algorithm for TM M with oracle access to S that decides whether x ∈ Sᵢ given input ⟨x,i⟩? | 小模型 | 6.174 | 7.484 | 1.310 | 5 |
| 5 | For part 2, what is the relationship between P and P_bad-angel? If α_n is computable in polynomial time, can any language in P_bad-angel be decided in polynomial time without the angel string? | 大模型 | 7.475 | 8.625 | 1.150 | 6 |
| 6 | For the relationship between NP and P_bad-angel, can we construct a language in NP that cannot be in P_bad-angel, or conversely, a language in P_bad-angel that cannot be in NP? | 大模型 | 8.776 | 9.995 | 1.219 | 7 |
| 7 | For part 3, given a language L ∈ P_angel with angel strings {α_n}, how can we define a sparse set S_L that encodes these angel strings? | 大模型 | 9.844 | 10.925 | 1.081 | 8 |
| 8 | Can we define S_L = {⟨1ⁿ,α_n⟩ | n ∈ ℕ}, and prove this set is sparse by analyzing how many strings of length m can be in S_L? | 大模型 | 11.029 | 12.179 | 1.150 | 9 |
| 9 | How can a TM M with oracle access to S_L decide the language L in polynomial time? What specific queries would M make to the oracle? | 大模型 | 12.179 | 13.260 | 1.081 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            10.70s
+------------------------------------------------------------+
步骤 1 |######                                                      | 2.56s - 3.64s
步骤 2 |       ######                                               | 3.96s - 5.04s
步骤 3 |              #######                                       | 5.22s - 6.37s
步骤 4 |                    #######                                 | 6.17s - 7.48s
步骤 5 |                           #######                          | 7.47s - 8.63s
步骤 6 |                                  #######                   | 8.78s - 10.00s
步骤 7 |                                        ######              | 9.84s - 10.93s
步骤 8 |                                               ######       | 11.03s - 12.18s
步骤 9 |                                                     #######| 12.18s - 13.26s
```

