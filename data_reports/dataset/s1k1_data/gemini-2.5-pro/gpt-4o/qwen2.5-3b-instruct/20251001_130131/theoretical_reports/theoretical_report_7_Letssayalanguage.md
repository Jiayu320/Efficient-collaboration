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
| 规划阶段总时间 (Planner) | 7.427 | 100% |
| 规划过程中启动的任务数 | 1 / 5 | 20.0% |
| 规划与执行重叠的任务数 | 1 / 5 | 20.0% |
| 第一个任务规划完成时间 | 3.609 | - |
| 最后一个任务规划完成时间 | 7.395 | - |
| 最后一个任务执行完成时间 | 43.637 | - |
| 任务总执行时间(累计) | 55.340 | - |
| 流水线加速比 | 1.43x | - |
| 并行效率 | 126.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 32.373 | - |
| 大模型任务 | 3 | 22.966 | - |
| 规划模型 | 1 | 7.256 | - |
| 顺序总时间 | - | 62.596 | - |
| 并行总时间 | - | 43.637 | 1.43x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | To begin, please define the three core concepts from the problem description: 1. What is a 'sparse set'? 2. What are the key components of the complexity class 'P_angel' (the machine M and the angel string α_n)? 3. How does the definition of 'P_bad-angel' specifically alter the properties of the angel string α_n? | 小模型 | 3.609 | 19.795 | 16.187 | 2 |
| 2 | For the first problem, address how to combine k sparse sets. Propose a method for constructing a single set S from k given sparse sets (S_1, ..., S_k) that allows an oracle TM to check membership in any specific S_i. Your response should include a formal definition of S, a justification for why S is also sparse, and a description of the polynomial-time oracle TM M. | 大模型 | 19.795 | 27.451 | 7.655 | 3 |
| 3 | For the third problem, demonstrate that any language L in P_angel can be decided by a polynomial-time TM with access to a sparse oracle. Propose a construction for the required sparse set S_L, prove that your proposed set is sparse, and describe the algorithm for the oracle TM that uses S_L to decide L. | 大模型 | 19.795 | 27.451 | 7.655 | 4 |
| 4 | For the second problem, analyze the P_bad-angel class. First, determine the relationship between P and P_bad-angel by providing arguments for inclusion in both directions (P ⊆ P_bad-angel and P_bad-angel ⊆ P). Second, based on your conclusion, what is the resulting relationship between NP and P_bad-angel, and how does it relate to the P vs. NP problem? | 大模型 | 19.795 | 27.451 | 7.655 | 5 |
| 5 | Synthesize the complete solutions from steps 2, 3, and 4 into a final, structured answer that addresses all three parts of the original problem in order. | 小模型 | 27.451 | 43.637 | 16.187 | 6 |

## 理论执行甘特图

```
时间轴:
0                                                            40.03s
+------------------------------------------------------------+
步骤 1 |########################                                    | 3.61s - 19.80s
步骤 2 |                        ###########                         | 19.80s - 27.45s
步骤 3 |                        ###########                         | 19.80s - 27.45s
步骤 4 |                        ###########                         | 19.80s - 27.45s
步骤 5 |                                   #########################| 27.45s - 43.64s
```

