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
| 规划阶段总时间 (Planner) | 7.747 | 100% |
| 规划过程中启动的任务数 | 3 / 8 | 37.5% |
| 规划与执行重叠的任务数 | 3 / 8 | 37.5% |
| 第一个任务规划完成时间 | 3.374 | - |
| 最后一个任务规划完成时间 | 7.715 | - |
| 最后一个任务执行完成时间 | 46.624 | - |
| 任务总执行时间(累计) | 86.837 | - |
| 流水线加速比 | 2.02x | - |
| 并行效率 | 186.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 3 | 48.560 | - |
| 大模型任务 | 5 | 38.277 | - |
| 规划模型 | 1 | 7.470 | - |
| 顺序总时间 | - | 94.307 | - |
| 并行总时间 | - | 46.624 | 2.02x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | To solve the first part, how can we construct a single set S from k sparse sets S_1, ..., S_k, such that membership of a string x in a specific set S_i can be determined by querying S? Propose a formal definition for the elements of S. | 大模型 | 3.374 | 11.029 | 7.655 | 2 |
| 2 | Given that each source set S_i is sparse, provide a justification for why the combined set S, as defined in the previous step, also meets the definition of a sparse set. | 大模型 | 11.029 | 18.685 | 7.655 | 3 |
| 3 | Describe the algorithm for a deterministic polynomial-time Turing Machine M that uses an oracle for the set S to decide if an input string x belongs to a specific set S_i. | 小模型 | 11.029 | 27.216 | 16.187 | 4 |
| 4 | For the second part, what is the formal definition of the complexity class P_bad-angel? Based on this definition, evaluate the claim P = P_bad-angel by providing arguments for both directions of the set inclusion (P ⊆ P_bad-angel and P_bad-angel ⊆ P). | 大模型 | 5.454 | 13.109 | 7.655 | 5 |
| 5 | What is the relationship between NP and P_bad-angel? Explain how this relationship is contingent upon the resolution of the P vs. NP problem. | 大模型 | 13.109 | 20.765 | 7.655 | 6 |
| 6 | For the third part, what is the critical piece of information required by the P_angel Turing Machine that depends only on the input length n, not the input string x itself? | 小模型 | 6.595 | 22.782 | 16.187 | 7 |
| 7 | Propose a formal definition for a sparse set S_L that effectively stores the critical length-dependent information identified in the previous step for all possible input lengths. | 大模型 | 22.782 | 30.437 | 7.655 | 8 |
| 8 | Describe the algorithm for a deterministic polynomial-time Turing Machine M that uses an oracle for the set S_L to decide if an input string x is in the language L. | 小模型 | 30.437 | 46.624 | 16.187 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            43.25s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 3.37s - 11.03s
步骤 4 |  ###########                                               | 5.45s - 13.11s
步骤 6 |    ######################                                  | 6.60s - 22.78s
步骤 2 |          ###########                                       | 11.03s - 18.68s
步骤 3 |          #######################                           | 11.03s - 27.22s
步骤 5 |             ###########                                    | 13.11s - 20.76s
步骤 7 |                          ###########                       | 22.78s - 30.44s
步骤 8 |                                     #######################| 30.44s - 46.62s
```

