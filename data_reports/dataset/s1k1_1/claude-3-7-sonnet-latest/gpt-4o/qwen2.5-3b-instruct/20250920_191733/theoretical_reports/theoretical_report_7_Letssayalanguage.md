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
| 规划阶段总时间 (Planner) | 8.396 | 100% |
| 规划过程中启动的任务数 | 6 / 7 | 85.7% |
| 规划与执行重叠的任务数 | 6 / 7 | 85.7% |
| 第一个任务规划完成时间 | 3.376 | - |
| 最后一个任务规划完成时间 | 8.352 | - |
| 最后一个任务执行完成时间 | 9.937 | - |
| 任务总执行时间(累计) | 8.398 | - |
| 流水线加速比 | 2.15x | - |
| 并行效率 | 84.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 7 | 8.398 | - |
| 规划模型 | 1 | 13.002 | - |
| 顺序总时间 | - | 21.400 | - |
| 并行总时间 | - | 9.937 | 2.15x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | How can we define a sparse set S that encodes membership information from k sparse sets S₁, S₂, ..., Sₖ? | 大模型 | 3.376 | 4.526 | 1.150 | 2 |
| 2 | Given the set S defined in Step 1, how can we design a polynomial-time TM M with oracle access to S that decides whether x ∈ Sᵢ? | 大模型 | 4.526 | 5.607 | 1.081 | 3 |
| 3 | For P_bad-angel, if the angel string αₙ must be computable in polynomial time, what constraints does this place on the languages in this class? | 大模型 | 4.990 | 6.209 | 1.219 | 4 |
| 4 | Based on the constraints identified in Step 3, what is the relationship between P and P_bad-angel? Are they equal or is one a subset of the other? | 大模型 | 6.209 | 7.498 | 1.289 | 5 |
| 5 | Based on the constraints identified in Step 3, what is the relationship between NP and P_bad-angel? Are they equal, is one a subset of the other, or are they incomparable? | 大模型 | 7.498 | 8.787 | 1.289 | 6 |
| 6 | For a language L in P_angel, how can we encode all possible angel strings {αₙ}_{n∈ℕ} into a sparse set S_L? | 大模型 | 7.567 | 8.786 | 1.219 | 7 |
| 7 | Given the sparse set S_L constructed in Step 6, how can we design a polynomial-time TM M with oracle access to S_L that decides language L? | 大模型 | 8.786 | 9.937 | 1.150 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            6.56s
+------------------------------------------------------------+
步骤 1 |##########                                                  | 3.38s - 4.53s
步骤 2 |          ##########                                        | 4.53s - 5.61s
步骤 3 |              ###########                                   | 4.99s - 6.21s
步骤 4 |                         ############                       | 6.21s - 7.50s
步骤 5 |                                     ############           | 7.50s - 8.79s
步骤 6 |                                      ###########           | 7.57s - 8.79s
步骤 7 |                                                 ###########| 8.79s - 9.94s
```

