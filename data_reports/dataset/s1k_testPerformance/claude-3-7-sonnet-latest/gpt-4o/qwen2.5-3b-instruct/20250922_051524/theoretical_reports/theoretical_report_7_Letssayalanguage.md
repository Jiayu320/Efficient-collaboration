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
| 路由模型 (claude-3-7-sonnet-latest) | 2.635 | 67.52 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 8.263 | 100% |
| 规划过程中启动的任务数 | 8 / 8 | 100.0% |
| 规划与执行重叠的任务数 | 7 / 8 | 87.5% |
| 第一个任务规划完成时间 | 3.435 | - |
| 最后一个任务规划完成时间 | 8.219 | - |
| 最后一个任务执行完成时间 | 9.358 | - |
| 任务总执行时间(累计) | 9.228 | - |
| 流水线加速比 | 2.75x | - |
| 并行效率 | 98.6% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 2.465 | - |
| 大模型任务 | 6 | 6.763 | - |
| 规划模型 | 1 | 16.542 | - |
| 顺序总时间 | - | 25.770 | - |
| 并行总时间 | - | 9.358 | 2.75x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For part 1, how can we define a sparse set S that encodes information from k sparse sets S₁, S₂, ..., Sₖ? | 大模型 | 3.435 | 4.516 | 1.081 | 2 |
| 2 | Given our definition of S in Step 1, how do we prove that S remains sparse if each S₁, S₂, ..., Sₖ is sparse? | 大模型 | 4.516 | 5.666 | 1.150 | 3 |
| 3 | What is the algorithm for the oracle TM M that decides whether x ∈ Sᵢ using oracle access to S? | 小模型 | 4.901 | 6.211 | 1.310 | 4 |
| 4 | For part 2, what is the relationship between P_bad-angel and P? Is P_bad-angel ⊆ P and is P ⊆ P_bad-angel? | 大模型 | 5.730 | 6.881 | 1.150 | 5 |
| 5 | What is the relationship between P_bad-angel and NP? Can P_bad-angel solve NP-complete problems? | 大模型 | 6.881 | 8.100 | 1.219 | 6 |
| 6 | For part 3, how can we define a sparse set S_L that encodes the angel strings for a language L ∈ P_angel? | 大模型 | 7.123 | 8.204 | 1.081 | 7 |
| 7 | Why is the set S_L defined in Step 6 sparse? | 小模型 | 8.204 | 9.358 | 1.155 | 8 |
| 8 | What is the algorithm for the oracle TM M that decides L using oracle access to S_L? | 大模型 | 8.219 | 9.300 | 1.081 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            5.92s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 3.43s - 4.52s
步骤 2 |          ############                                      | 4.52s - 5.67s
步骤 3 |              ##############                                | 4.90s - 6.21s
步骤 4 |                       ###########                          | 5.73s - 6.88s
步骤 5 |                                  #############             | 6.88s - 8.10s
步骤 6 |                                     ###########            | 7.12s - 8.20s
步骤 7 |                                                ############| 8.20s - 9.36s
步骤 8 |                                                ########### | 8.22s - 9.30s
```

