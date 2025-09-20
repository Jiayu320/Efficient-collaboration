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
| 规划阶段总时间 (Planner) | 8.640 | 100% |
| 规划过程中启动的任务数 | 7 / 7 | 100.0% |
| 规划与执行重叠的任务数 | 6 / 7 | 85.7% |
| 第一个任务规划完成时间 | 2.426 | - |
| 最后一个任务规划完成时间 | 8.582 | - |
| 最后一个任务执行完成时间 | 9.594 | - |
| 任务总执行时间(累计) | 7.727 | - |
| 流水线加速比 | 2.36x | - |
| 并行效率 | 80.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.310 | - |
| 大模型任务 | 6 | 6.417 | - |
| 规划模型 | 1 | 14.932 | - |
| 顺序总时间 | - | 22.659 | - |
| 并行总时间 | - | 9.594 | 2.36x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For part 1, how can we construct a sparse set S that encodes membership information for all the sparse sets S₁, S₂, ..., Sₖ? | 大模型 | 2.426 | 3.437 | 1.012 | 2 |
| 2 | How can we design a polynomial-time oracle TM M that, given input ⟨x,i⟩, can extract information from the oracle set S to determine if x ∈ Sᵢ? | 小模型 | 3.552 | 4.862 | 1.310 | 3 |
| 3 | For part 2, what is the computational power of P_bad-angel compared to P? Can we prove P = P_bad-angel? | 大模型 | 4.542 | 5.623 | 1.081 | 4 |
| 4 | For part 2, what is the computational power of P_bad-angel compared to NP? Can we prove NP = P_bad-angel? | 大模型 | 5.623 | 6.704 | 1.081 | 5 |
| 5 | For part 3, given a language L ∈ P_angel with angel strings {αₙ}, how can we construct a sparse set S_L that encodes the necessary information from these angel strings? | 大模型 | 6.717 | 7.868 | 1.150 | 6 |
| 6 | How can we design a polynomial-time oracle TM that uses S_L to decide L? What information should it extract from the oracle and how should it process it? | 大模型 | 7.868 | 8.949 | 1.081 | 7 |
| 7 | Why is the set S_L sparse? How can we prove this property based on the definition of sparsity? | 大模型 | 8.582 | 9.594 | 1.012 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            7.17s
+------------------------------------------------------------+
步骤 1 |########                                                    | 2.43s - 3.44s
步骤 2 |         ###########                                        | 3.55s - 4.86s
步骤 3 |                 #########                                  | 4.54s - 5.62s
步骤 4 |                          #########                         | 5.62s - 6.70s
步骤 5 |                                   ##########               | 6.72s - 7.87s
步骤 6 |                                             #########      | 7.87s - 8.95s
步骤 7 |                                                   #########| 8.58s - 9.59s
```

