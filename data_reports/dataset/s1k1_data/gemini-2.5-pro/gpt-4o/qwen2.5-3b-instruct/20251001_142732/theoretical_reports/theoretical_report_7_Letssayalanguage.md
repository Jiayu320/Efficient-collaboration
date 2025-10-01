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
| 规划阶段总时间 (Planner) | 9.208 | 100% |
| 规划过程中启动的任务数 | 2 / 8 | 25.0% |
| 规划与执行重叠的任务数 | 2 / 8 | 25.0% |
| 第一个任务规划完成时间 | 3.598 | - |
| 最后一个任务规划完成时间 | 9.176 | - |
| 最后一个任务执行完成时间 | 43.627 | - |
| 任务总执行时间(累计) | 95.368 | - |
| 流水线加速比 | 2.44x | - |
| 并行效率 | 218.6% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 4 | 64.747 | - |
| 大模型任务 | 4 | 30.622 | - |
| 规划模型 | 1 | 11.043 | - |
| 顺序总时间 | - | 106.411 | - |
| 并行总时间 | - | 43.627 | 2.44x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | To solve Parts 1 and 3, a central strategy is needed to combine multiple pieces of information into a single new set while maintaining the 'sparse' property. What general encoding technique can be used to construct a new string for the sparse set from multiple input components (e.g., an index `i` and a string `x`) such that the original components can be uniquely recovered? | 大模型 | 3.598 | 11.253 | 7.655 | 2 |
| 2 | For Part 1, applying the encoding strategy from Step 1, how would you formally define the new sparse set `S` that combines all strings from `k` sparse sets `S_1, ..., S_k`? Also, provide a step-by-step description of the oracle TM `M` that uses this set `S` to determine if a given input `x` belongs to a specific set `S_i`. | 小模型 | 11.253 | 27.440 | 16.187 | 3 |
| 3 | For Part 3, which concerns a language `L` in P_angel, what is the critical piece of information for each input length `n` that needs to be stored? Using the encoding strategy from Step 1, how would you define the sparse set `S_L` to store this information? | 小模型 | 11.253 | 27.440 | 16.187 | 4 |
| 4 | For Part 2, which introduces P_bad-angel, analyze the relationship `P_bad-angel` has with the class `P`. Is one a subset of the other? Are they equal? Provide a two-part justification for your conclusion. | 大模型 | 6.393 | 14.048 | 7.655 | 5 |
| 5 | Based on the definition of set `S` from Step 2, provide a formal argument explaining why `S` is guaranteed to be sparse, given that each individual `S_i` is sparse? | 大模型 | 27.440 | 35.095 | 7.655 | 6 |
| 6 | Based on the definition of set `S_L` from Step 3, provide a formal argument explaining why `S_L` is guaranteed to be sparse? | 小模型 | 27.440 | 43.627 | 16.187 | 7 |
| 7 | Following the construction of `S_L` in Step 3, describe the algorithm for the oracle TM `M` that uses `S_L` to decide the language `L` in polynomial time. | 小模型 | 27.440 | 43.627 | 16.187 | 8 |
| 8 | Based on your conclusion about the relationship between `P` and `P_bad-angel` from Step 4, what can be inferred about the relationship between `NP` and `P_bad-angel`? Does proving `NP = P_bad-angel` depend on any major unsolved problems in computer science? | 大模型 | 14.048 | 21.703 | 7.655 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            40.03s
+------------------------------------------------------------+
步骤 1 |###########                                                 | 3.60s - 11.25s
步骤 4 |    ###########                                             | 6.39s - 14.05s
步骤 2 |           ########################                         | 11.25s - 27.44s
步骤 3 |           ########################                         | 11.25s - 27.44s
步骤 8 |               ############                                 | 14.05s - 21.70s
步骤 5 |                                   ############             | 27.44s - 35.10s
步骤 6 |                                   #########################| 27.44s - 43.63s
步骤 7 |                                   #########################| 27.44s - 43.63s
```

