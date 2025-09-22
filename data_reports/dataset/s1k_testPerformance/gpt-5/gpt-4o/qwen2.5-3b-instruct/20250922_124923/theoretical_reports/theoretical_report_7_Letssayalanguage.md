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
| 路由模型 (openai/gpt-5) | 6.407 | 50.57 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 20.881 | 100% |
| 规划过程中启动的任务数 | 5 / 6 | 83.3% |
| 规划与执行重叠的任务数 | 5 / 6 | 83.3% |
| 第一个任务规划完成时间 | 8.839 | - |
| 最后一个任务规划完成时间 | 20.821 | - |
| 最后一个任务执行完成时间 | 33.403 | - |
| 任务总执行时间(累计) | 45.932 | - |
| 流水线加速比 | 2.82x | - |
| 并行效率 | 137.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 6 | 45.932 | - |
| 规划模型 | 1 | 48.148 | - |
| 顺序总时间 | - | 94.081 | - |
| 并行总时间 | - | 33.403 | 2.82x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For item (1), define the sparse oracle S as S := ⋃_{i=1}^k { 0^i 1 x : x ∈ S_i } over alphabet {0,1}; with |S_i^{=m}| ≤ p_i(m), compute the per-length bound |S^{=n}| ≤ ∑_{i=1}^k p_i(n − (i+1)); since k is constant and each p_i is polynomial, is S sparse under this bound? | 大模型 | 8.839 | 16.494 | 7.655 | 2 |
| 2 | Define the oracle TM M^S for item (1): on input ⟨x,i⟩, form y = 0^i 1 x and query y ∈ S; accept iff the answer is yes; does this ensure M^S(⟨x,i⟩) = 1 if and only if x ∈ S_i? | 大模型 | 16.494 | 24.150 | 7.655 | 3 |
| 3 | For item (2), show P_bad-angel ⊆ P by constructing a decider D for any L ∈ P_bad-angel as: on input x of length n, compute α_n := A(n) in poly(n) time, then run M(x, α_n) in poly(n + |α_n|) time; since |α_n| ≤ poly(n), is the total time polynomial, proving P_bad-angel ⊆ P? | 大模型 | 12.774 | 20.429 | 7.655 | 4 |
| 4 | For item (2), show P ⊆ P_bad-angel by choosing α_n = ε and letting M ignore its second input while deciding L in poly-time, with A(n) outputting ε in poly-time; conclude P_bad-angel = P, and therefore NP = P_bad-angel if and only if P = NP; is this conclusion justified? | 大模型 | 20.429 | 28.084 | 7.655 | 5 |
| 5 | For item (3), construct a sparse set S_L encoding the angel strings: given p(n) from L ∈ P_angel, choose r ≥ deg p and set t(n) = (n+1)^r; define s(n,j) = 1^n 0 bin(j) 0^{t(n) − (n + 1 + |bin(j)|)} and S_L = { s(n,j) : α_n[j] = 1 for j ∈ [1..p(n)] }; since for length m = t(n) we have |S_L^{=m}| ≤ p(n) ≤ (n+1)^{deg p} ≤ t(n) = m and otherwise 0, does this prove S_L is sparse? | 大模型 | 18.093 | 25.748 | 7.655 | 6 |
| 6 | Define M^{S_L} for item (3): on input x with n = |x|, reconstruct α_n by querying s(n,j) ∈ S_L for j = 1..p(n) to set α_n[j] (1 if yes, else 0), then run the original M(x, α_n) and output its answer; since p(n) and t(n) are polynomial, is the overall running time polynomial and does M^{S_L} decide L; combining Steps 1–5, does this complete the proof of all three items? | 大模型 | 25.748 | 33.403 | 7.655 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            24.56s
+------------------------------------------------------------+
步骤 1 |##################                                          | 8.84s - 16.49s
步骤 3 |         ###################                                | 12.77s - 20.43s
步骤 2 |                  ###################                       | 16.49s - 24.15s
步骤 5 |                      ###################                   | 18.09s - 25.75s
步骤 4 |                            ###################             | 20.43s - 28.08s
步骤 6 |                                         ###################| 25.75s - 33.40s
```

