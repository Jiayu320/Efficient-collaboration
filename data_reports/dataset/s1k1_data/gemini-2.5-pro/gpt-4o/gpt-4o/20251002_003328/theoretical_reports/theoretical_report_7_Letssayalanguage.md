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
| 规划阶段总时间 (Planner) | 7.843 | 100% |
| 规划过程中启动的任务数 | 3 / 8 | 37.5% |
| 规划与执行重叠的任务数 | 3 / 8 | 37.5% |
| 第一个任务规划完成时间 | 3.331 | - |
| 最后一个任务规划完成时间 | 7.811 | - |
| 最后一个任务执行完成时间 | 21.863 | - |
| 任务总执行时间(累计) | 61.243 | - |
| 流水线加速比 | 3.15x | - |
| 并行效率 | 280.1% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 15.311 | - |
| 大模型任务 | 6 | 45.932 | - |
| 规划模型 | 1 | 7.555 | - |
| 顺序总时间 | - | 68.798 | - |
| 并行总时间 | - | 21.863 | 3.15x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For the first problem, propose a method to construct a single set S from k sparse sets S_1, ..., S_k such that S encodes both a string x and its original set index i, allowing membership in any S_i to be checked by querying S? | 大模型 | 3.331 | 10.987 | 7.655 | 2 |
| 2 | Based on the construction from Step 1 and the definition of a sparse set, provide a formal argument explaining why the resulting set S is also sparse? | 大模型 | 10.987 | 18.642 | 7.655 | 3 |
| 3 | Describe the algorithm for a deterministic polynomial-time Turing Machine M that uses an oracle for the set S (from Step 1) to decide if an input `<x, i>` means x is in S_i? | 小模型 | 10.987 | 18.642 | 7.655 | 4 |
| 4 | For the second problem, is the complexity class P equal to P_bad-angel? Justify your answer by proving or disproving containment in both directions (P ⊆ P_bad-angel and P_bad-angel ⊆ P). | 大模型 | 5.283 | 12.939 | 7.655 | 5 |
| 5 | Based on the conclusion from Step 4, what is the relationship between NP and P_bad-angel? Justify your answer by connecting it to the P vs NP problem. | 大模型 | 12.939 | 20.594 | 7.655 | 6 |
| 6 | For the third problem, propose a construction for a sparse set S_L that can serve as an oracle for a language L in P_angel. What specific information must this set contain for each input length n? | 大模型 | 6.553 | 14.208 | 7.655 | 7 |
| 7 | Based on your proposed construction for S_L in Step 6, explain why this set satisfies the formal definition of being sparse? | 小模型 | 14.208 | 21.863 | 7.655 | 8 |
| 8 | Describe the algorithm for a deterministic polynomial-time Turing Machine M that uses an oracle for S_L (from Step 6) to decide if an input x of length n is in the language L. How does it retrieve and use the information from the oracle? | 大模型 | 14.208 | 21.863 | 7.655 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            18.53s
+------------------------------------------------------------+
步骤 1 |########################                                    | 3.33s - 10.99s
步骤 4 |      #########################                             | 5.28s - 12.94s
步骤 6 |          #########################                         | 6.55s - 14.21s
步骤 2 |                        #########################           | 10.99s - 18.64s
步骤 3 |                        #########################           | 10.99s - 18.64s
步骤 5 |                               ########################     | 12.94s - 20.59s
步骤 7 |                                   #########################| 14.21s - 21.86s
步骤 8 |                                   #########################| 14.21s - 21.86s
```

