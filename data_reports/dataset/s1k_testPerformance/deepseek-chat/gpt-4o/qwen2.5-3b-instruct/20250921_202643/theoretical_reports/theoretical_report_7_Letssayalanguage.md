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
| 路由模型 (deepseek-chat) | 1.600 | 31.97 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 19.304 | 100% |
| 规划过程中启动的任务数 | 4 / 4 | 100.0% |
| 规划与执行重叠的任务数 | 3 / 4 | 75.0% |
| 第一个任务规划完成时间 | 6.073 | - |
| 最后一个任务规划完成时间 | 19.210 | - |
| 最后一个任务执行完成时间 | 20.568 | - |
| 任务总执行时间(累计) | 5.847 | - |
| 流水线加速比 | 5.40x | - |
| 并行效率 | 28.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 4 | 5.847 | - |
| 规划模型 | 1 | 105.291 | - |
| 顺序总时间 | - | 111.138 | - |
| 并行总时间 | - | 20.568 | 5.40x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For part (1), define the sparse set S as S = { ⟨x, i⟩ : x ∈ S_i } where ⟨.,.⟩ is a pairing function. Show that S is sparse: for any length m, the number of strings in S of length m is at most k * p(m - c) for some constant c, which is polynomial in m. Then describe the oracle TM M: on input ⟨x, i⟩, it forms the string s = ⟨x, i⟩ and queries S with s; it accepts if the oracle returns yes. Is this correct? | 大模型 | 6.073 | 7.500 | 1.427 | 2 |
| 2 | For part (2), first argue that P_bad-angel = P: given x, compute α_{|x|} = A(|x|) in poly-time, then run M(x, α_{|x|}) in poly-time. For NP, note that if NP ⊆ P_bad-angel, then since P_bad-angel = P, we have NP ⊆ P, so P=NP. Conversely, if P=NP, then NP = P = P_bad-angel. Therefore, NP = P_bad-angel if and only if P=NP. Is this reasoning sound? | 大模型 | 10.608 | 12.174 | 1.565 | 3 |
| 3 | For part (3), given L in P_angel with angel string α_n of length p(n), define the sparse set S_L = { ⟨1^n, i, b⟩ : n ∈ ℕ, i ∈ {1,2,...,p(n)}, and the i-th bit of α_n is b } using a pairing function. Show that S_L is sparse: for length L, the number of strings is O(poly(L)) because for each n approximately equal to L, there are p(n) = poly(L) strings, and only constantly many n contribute to length L. Is this sparse? | 大模型 | 15.113 | 16.609 | 1.496 | 4 |
| 4 | Describe the oracle TM M for part (3): on input x of length n, for i=1 to p(n), query S_L for membership of ⟨1^n, i, 0⟩. If yes, set bit i to 0; else, query for ⟨1^n, i, 1⟩ (which must be in S_L) and set bit i to 1. This reconstructs α_n. Then compute and return M_angel(x, α_n). This runs in poly-time. Does this correctly decide L? | 大模型 | 19.210 | 20.568 | 1.358 | 5 |

## 理论执行甘特图

```
时间轴:
0                                                            14.50s
+------------------------------------------------------------+
步骤 1 |#####                                                       | 6.07s - 7.50s
步骤 2 |                  #######                                   | 10.61s - 12.17s
步骤 3 |                                     ######                 | 15.11s - 16.61s
步骤 4 |                                                      ######| 19.21s - 20.57s
```

