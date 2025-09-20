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
| 规划阶段总时间 (Planner) | 9.320 | 100% |
| 规划过程中启动的任务数 | 7 / 8 | 87.5% |
| 规划与执行重叠的任务数 | 7 / 8 | 87.5% |
| 第一个任务规划完成时间 | 2.523 | - |
| 最后一个任务规划完成时间 | 9.262 | - |
| 最后一个任务执行完成时间 | 10.668 | - |
| 任务总执行时间(累计) | 8.510 | - |
| 流水线加速比 | 2.38x | - |
| 并行效率 | 79.8% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 8 | 8.510 | - |
| 规划模型 | 1 | 16.874 | - |
| 顺序总时间 | - | 25.384 | - |
| 并行总时间 | - | 10.668 | 2.38x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For part 1, how can we construct a sparse set S that encodes all the sparse sets S_1, S_2, ..., S_k in a way that allows efficient retrieval? | 大模型 | 2.523 | 3.604 | 1.081 | 2 |
| 2 | What encoding scheme can we use to map elements from each S_i into our new set S while preserving sparsity and allowing for efficient lookup? | 大模型 | 3.604 | 4.615 | 1.012 | 3 |
| 3 | How can we design the polynomial-time Turing Machine M that uses oracle access to S to determine if x ∈ S_i given input ⟨x,i⟩? | 大模型 | 4.615 | 5.627 | 1.012 | 4 |
| 4 | For part 2, what is the relationship between P and P_bad-angel given that the angel string must be computable in polynomial time? | 大模型 | 5.436 | 6.517 | 1.081 | 5 |
| 5 | What is the relationship between NP and P_bad-angel? Can we use the polynomial-time computable angel string to solve NP-complete problems? | 大模型 | 6.517 | 7.667 | 1.150 | 6 |
| 6 | For part 3, given a language L ∈ P_angel with angel strings {α_n}, how can we construct a sparse set S_L that encodes these angel strings? | 大模型 | 7.494 | 8.575 | 1.081 | 7 |
| 7 | What information needs to be stored in S_L to allow a polynomial-time TM with oracle access to decide L? | 大模型 | 8.575 | 9.622 | 1.046 | 8 |
| 8 | How can we design a polynomial-time TM M that uses oracle access to S_L to decide if x ∈ L for any input x? | 大模型 | 9.622 | 10.668 | 1.046 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            8.15s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 2.52s - 3.60s
步骤 2 |       ########                                             | 3.60s - 4.62s
步骤 3 |               #######                                      | 4.62s - 5.63s
步骤 4 |                     ########                               | 5.44s - 6.52s
步骤 5 |                             ########                       | 6.52s - 7.67s
步骤 6 |                                    ########                | 7.49s - 8.58s
步骤 7 |                                            ########        | 8.58s - 9.62s
步骤 8 |                                                    ####### | 9.62s - 10.67s
```

