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
| 路由模型 (deepseek-chat) | 1.600 | 31.97 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 23.652 | 100% |
| 规划过程中启动的任务数 | 8 / 17 | 47.1% |
| 规划与执行重叠的任务数 | 8 / 17 | 47.1% |
| 第一个任务规划完成时间 | 3.008 | - |
| 最后一个任务规划完成时间 | 23.558 | - |
| 最后一个任务执行完成时间 | 72.767 | - |
| 任务总执行时间(累计) | 181.330 | - |
| 流水线加速比 | 2.79x | - |
| 并行效率 | 249.2% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 6 | 97.120 | - |
| 大模型任务 | 11 | 84.210 | - |
| 规划模型 | 1 | 21.681 | - |
| 顺序总时间 | - | 203.011 | - |
| 并行总时间 | - | 72.767 | 2.79x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the key difference between the angel string in P_angel and a witness/certificate in NP? | 大模型 | 3.008 | 10.663 | 7.655 | 2 |
| 2 | For Part 1, what is the main challenge in combining k sparse sets into one sparse oracle set S? | 大模型 | 4.321 | 11.977 | 7.655 | 3 |
| 3 | What encoding strategy can be used to combine information about multiple sparse sets while preserving sparsity? | 大模型 | 11.977 | 19.632 | 7.655 | 4 |
| 4 | Using the encoding strategy from Step 3, formally define the sparse set S for Part 1. | 小模型 | 19.632 | 35.819 | 16.187 | 5 |
| 5 | Why does the set S defined in Step 4 remain sparse? Provide the sparsity justification. | 大模型 | 35.819 | 43.474 | 7.655 | 6 |
| 6 | Describe the polynomial-time oracle Turing machine M for Part 1 that uses oracle S to decide membership in any S_i. | 小模型 | 35.819 | 52.005 | 16.187 | 7 |
| 7 | For Part 2, what is the critical constraint that distinguishes P_bad-angel from P_angel? | 大模型 | 10.827 | 18.483 | 7.655 | 8 |
| 8 | Show that any language in P is also in P_bad-angel by constructing appropriate angel strings and algorithms. | 小模型 | 18.483 | 34.669 | 16.187 | 9 |
| 9 | Show that any language in P_bad-angel is also in P by analyzing the computational requirements. | 大模型 | 18.483 | 26.138 | 7.655 | 10 |
| 10 | Based on Steps 8 and 9, what is the relationship between P and P_bad-angel? | 小模型 | 34.669 | 50.856 | 16.187 | 1 |
| 11 | What is the relationship between P_bad-angel and NP? Justify your answer using complexity theory principles. | 大模型 | 50.856 | 58.512 | 7.655 | 2 |
| 12 | For Part 3, what key insight connects P_angel languages with sparse oracle sets? | 大模型 | 17.427 | 25.083 | 7.655 | 3 |
| 13 | How can the angel strings for different input lengths be encoded into a sparse set S_L? | 大模型 | 25.083 | 32.738 | 7.655 | 4 |
| 14 | Formally define the sparse set S_L for a given P_angel language L. | 小模型 | 32.738 | 48.925 | 16.187 | 5 |
| 15 | Why is the set S_L defined in Step 14 sparse? Provide the sparsity justification. | 大模型 | 48.925 | 56.580 | 7.655 | 6 |
| 16 | Describe the polynomial-time oracle Turing machine that uses S_L to decide the P_angel language L. | 小模型 | 48.925 | 65.112 | 16.187 | 7 |
| 17 | Verify that the oracle machine from Step 16 runs in polynomial time when deciding L. | 大模型 | 65.112 | 72.767 | 7.655 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            69.76s
+------------------------------------------------------------+
步骤 1 |######                                                      | 3.01s - 10.66s
步骤 2 | ######                                                     | 4.32s - 11.98s
步骤 7 |      #######                                               | 10.83s - 18.48s
步骤 3 |       #######                                              | 11.98s - 19.63s
步骤 12 |            ######                                          | 17.43s - 25.08s
步骤 8 |             ##############                                 | 18.48s - 34.67s
步骤 9 |             ######                                         | 18.48s - 26.14s
步骤 4 |              ##############                                | 19.63s - 35.82s
步骤 13 |                  #######                                   | 25.08s - 32.74s
步骤 14 |                         ##############                     | 32.74s - 48.92s
步骤 10 |                           ##############                   | 34.67s - 50.86s
步骤 5 |                            ######                          | 35.82s - 43.47s
步骤 6 |                            ##############                  | 35.82s - 52.01s
步骤 15 |                                       #######              | 48.92s - 56.58s
步骤 16 |                                       ##############       | 48.92s - 65.11s
步骤 11 |                                         ######             | 50.86s - 58.51s
步骤 17 |                                                     #######| 65.11s - 72.77s
```

