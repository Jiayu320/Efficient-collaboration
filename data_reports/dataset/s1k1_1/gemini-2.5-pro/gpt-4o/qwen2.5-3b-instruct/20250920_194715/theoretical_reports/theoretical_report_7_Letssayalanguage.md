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
| 规划阶段总时间 (Planner) | 8.472 | 100% |
| 规划过程中启动的任务数 | 6 / 8 | 75.0% |
| 规划与执行重叠的任务数 | 6 / 8 | 75.0% |
| 第一个任务规划完成时间 | 3.225 | - |
| 最后一个任务规划完成时间 | 8.440 | - |
| 最后一个任务执行完成时间 | 11.185 | - |
| 任务总执行时间(累计) | 9.340 | - |
| 流水线加速比 | 1.82x | - |
| 并行效率 | 83.5% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 8 | 9.340 | - |
| 规划模型 | 1 | 11.043 | - |
| 顺序总时间 | - | 20.383 | - |
| 并行总时间 | - | 11.185 | 1.82x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For Part 1, how can we define a single set S by encoding pairs of (index i, string x) for each x in S_i, and how can we prove that this new set S is sparse? | 大模型 | 3.225 | 4.375 | 1.150 | 2 |
| 2 | Given the sparse set S defined in Step 1, what is the precise description of the deterministic polynomial-time oracle TM M that, on input <x, i>, correctly determines if x is in S_i? | 大模型 | 4.375 | 5.456 | 1.081 | 3 |
| 3 | For Part 2, to prove P_bad-angel is equal to P, first show P_bad-angel ⊆ P. How can we construct a standard deterministic polynomial-time TM that decides a language in P_bad-angel by first computing the required angel string α_n and then simulating the P_bad-angel machine? | 大模型 | 4.825 | 6.044 | 1.219 | 4 |
| 4 | To complete the proof from Step 3, how do we show the other direction (P ⊆ P_bad-angel), and what does the resulting equality P = P_bad-angel imply about the relationship between NP and P_bad-angel? | 大模型 | 6.044 | 7.194 | 1.150 | 5 |
| 5 | For Part 3, let L be a language in P_angel with angel strings {α_n} and polynomial length bound p(n). How can we define a sparse set S_L that encodes the individual bits of each angel string α_n in a way that is retrievable by an oracle TM? | 大模型 | 6.446 | 7.734 | 1.289 | 6 |
| 6 | Using the definition of S_L from Step 5, what is the formal argument to prove that S_L is a sparse set by bounding the number of its elements for any given length m? | 大模型 | 7.734 | 8.885 | 1.150 | 7 |
| 7 | Given the sparse oracle S_L from Step 5, how can a deterministic oracle TM M, on input x of length n, reconstruct the entire angel string α_n by making a polynomial number of queries to S_L? | 大模型 | 8.885 | 10.104 | 1.219 | 8 |
| 8 | After the oracle TM M has successfully reconstructed the angel string α_n using the process from Step 7, what final computation must it perform to decide if the original input x belongs to the language L? | 大模型 | 10.104 | 11.185 | 1.081 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            7.96s
+------------------------------------------------------------+
步骤 1 |########                                                    | 3.22s - 4.37s
步骤 2 |        ########                                            | 4.37s - 5.46s
步骤 3 |            #########                                       | 4.82s - 6.04s
步骤 4 |                     ########                               | 6.04s - 7.19s
步骤 5 |                        #########                           | 6.45s - 7.73s
步骤 6 |                                 #########                  | 7.73s - 8.88s
步骤 7 |                                          #########         | 8.88s - 10.10s
步骤 8 |                                                   #########| 10.10s - 11.19s
```

