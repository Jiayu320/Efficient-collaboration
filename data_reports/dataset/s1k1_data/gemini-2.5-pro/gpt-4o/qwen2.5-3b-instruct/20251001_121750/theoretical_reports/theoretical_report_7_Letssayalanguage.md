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
| 规划阶段总时间 (Planner) | 8.995 | 100% |
| 规划过程中启动的任务数 | 1 / 9 | 11.1% |
| 规划与执行重叠的任务数 | 1 / 9 | 11.1% |
| 第一个任务规划完成时间 | 3.054 | - |
| 最后一个任务规划完成时间 | 8.963 | - |
| 最后一个任务执行完成时间 | 50.738 | - |
| 任务总执行时间(累计) | 85.961 | - |
| 流水线加速比 | 1.87x | - |
| 并行效率 | 169.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 32.373 | - |
| 大模型任务 | 7 | 53.588 | - |
| 规划模型 | 1 | 8.675 | - |
| 顺序总时间 | - | 94.636 | - |
| 并行总时间 | - | 50.738 | 1.87x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What are the formal definitions of a 'sparse set' and the complexity class `P_angel` as described in the problem statement? | 小模型 | 3.054 | 19.241 | 16.187 | 2 |
| 2 | For Part 1, propose a method to combine `k` sparse sets `S_1, ..., S_k` into a single set `S`. How should the strings in `S` be structured to encode both the original string `x` and the index `i` of the set it came from? | 大模型 | 19.241 | 26.896 | 7.655 | 3 |
| 3 | Based on the structure of `S` proposed in Step 2, provide a formal argument explaining why `S` must also be a sparse set? | 大模型 | 26.896 | 34.551 | 7.655 | 4 |
| 4 | Based on the structure of `S` proposed in Step 2, describe the algorithm for the deterministic polynomial-time Turing Machine `M` that uses `S` as an oracle to decide if an input `⟨x,i⟩` corresponds to `x ∈ S_i`? | 小模型 | 26.896 | 43.083 | 16.187 | 5 |
| 5 | For Part 2, concerning the class `P_bad-angel` where the angel string is computable in polynomial time, is it true that `P = P_bad-angel`? Justify your answer by proving the relationship in both directions (`P ⊆ P_bad-angel` and `P_bad-angel ⊆ P`). | 大模型 | 19.241 | 26.896 | 7.655 | 6 |
| 6 | For Part 2, is it true that `NP = P_bad-angel`? Justify your answer by relating this question to the P vs. NP problem. | 大模型 | 26.896 | 34.551 | 7.655 | 7 |
| 7 | For Part 3, propose a structure for a sparse set `S_L` that can serve as an oracle for a language `L` in `P_angel`. What specific information must this set contain for each possible input length `n`? | 大模型 | 19.241 | 26.896 | 7.655 | 8 |
| 8 | Based on the proposed structure for `S_L` in Step 7, explain why this set is sparse and describe the algorithm for the oracle TM that uses `S_L` to decide membership in `L` for an input `x`? | 大模型 | 26.896 | 34.551 | 7.655 | 9 |
| 9 | Synthesize the results from all preceding steps to provide a complete and justified solution for all three parts of the problem. | 大模型 | 43.083 | 50.738 | 7.655 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            47.68s
+------------------------------------------------------------+
步骤 1 |####################                                        | 3.05s - 19.24s
步骤 2 |                    ##########                              | 19.24s - 26.90s
步骤 5 |                    ##########                              | 19.24s - 26.90s
步骤 7 |                    ##########                              | 19.24s - 26.90s
步骤 3 |                              #########                     | 26.90s - 34.55s
步骤 4 |                              ####################          | 26.90s - 43.08s
步骤 6 |                              #########                     | 26.90s - 34.55s
步骤 8 |                              #########                     | 26.90s - 34.55s
步骤 9 |                                                  ##########| 43.08s - 50.74s
```

