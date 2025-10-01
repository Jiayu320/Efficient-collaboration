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
| 路由模型 (gpt-4o) | 0.735 | 144.50 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 3.386 | 100% |
| 规划过程中启动的任务数 | 3 / 8 | 37.5% |
| 规划与执行重叠的任务数 | 3 / 8 | 37.5% |
| 第一个任务规划完成时间 | 1.060 | - |
| 最后一个任务规划完成时间 | 3.365 | - |
| 最后一个任务执行完成时间 | 32.558 | - |
| 任务总执行时间(累计) | 78.306 | - |
| 流水线加速比 | 2.51x | - |
| 并行效率 | 240.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 2 | 32.373 | - |
| 大模型任务 | 6 | 45.932 | - |
| 规划模型 | 1 | 3.261 | - |
| 顺序总时间 | - | 81.567 | - |
| 并行总时间 | - | 32.558 | 2.51x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the definition of a sparse set in terms of the polynomial bound on the number of strings of a given length? | 小模型 | 1.060 | 17.247 | 16.187 | 2 |
| 2 | How can we construct a single sparse set S from k sparse sets S1, S2, ..., Sk, such that S can be used to determine membership in any Si? | 大模型 | 17.247 | 24.902 | 7.655 | 3 |
| 3 | What is the structure of a deterministic polynomial time Turing Machine with oracle access to a sparse set that can determine membership in any of the k sparse sets? | 大模型 | 24.902 | 32.558 | 7.655 | 4 |
| 4 | What is the definition of P_angel and how does it differ from P_bad-angel, particularly in terms of computing the angel string? | 小模型 | 2.140 | 18.327 | 16.187 | 5 |
| 5 | Is P equal to P_bad-angel? Provide a justification for your answer. | 大模型 | 18.327 | 25.982 | 7.655 | 6 |
| 6 | Is NP equal to P_bad-angel? Provide a justification for your answer. | 大模型 | 18.327 | 25.982 | 7.655 | 7 |
| 7 | How can we construct a sparse set SL for a language L in P_angel, and what is the role of the angel string in this construction? | 大模型 | 3.012 | 10.667 | 7.655 | 8 |
| 8 | What is the structure of a deterministic polynomial time Turing Machine with oracle access to a sparse set SL that can decide a language L in P_angel? | 大模型 | 10.667 | 18.323 | 7.655 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            31.50s
+------------------------------------------------------------+
步骤 1 |##############################                              | 1.06s - 17.25s
步骤 4 |  ##############################                            | 2.14s - 18.33s
步骤 7 |   ###############                                          | 3.01s - 10.67s
步骤 8 |                  ##############                            | 10.67s - 18.32s
步骤 2 |                              ###############               | 17.25s - 24.90s
步骤 5 |                                ###############             | 18.33s - 25.98s
步骤 6 |                                ###############             | 18.33s - 25.98s
步骤 3 |                                             ###############| 24.90s - 32.56s
```

