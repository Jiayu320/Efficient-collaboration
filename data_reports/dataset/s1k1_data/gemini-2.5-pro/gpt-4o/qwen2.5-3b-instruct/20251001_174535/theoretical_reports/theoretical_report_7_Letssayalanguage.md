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
| 规划阶段总时间 (Planner) | 14.723 | 100% |
| 规划过程中启动的任务数 | 5 / 21 | 23.8% |
| 规划与执行重叠的任务数 | 5 / 21 | 23.8% |
| 第一个任务规划完成时间 | 2.937 | - |
| 最后一个任务规划完成时间 | 14.691 | - |
| 最后一个任务执行完成时间 | 67.479 | - |
| 任务总执行时间(累计) | 237.545 | - |
| 流水线加速比 | 3.74x | - |
| 并行效率 | 352.0% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 9 | 145.680 | - |
| 大模型任务 | 12 | 91.865 | - |
| 规划模型 | 1 | 14.691 | - |
| 顺序总时间 | - | 252.236 | - |
| 并行总时间 | - | 67.479 | 3.74x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the formal definition of a 'sparse set' in computational complexity theory? | 大模型 | 2.937 | 10.592 | 7.655 | 2 |
| 2 | To combine information from k sparse sets S_1...S_k into a single set S, propose a string encoding scheme that represents both a string x and the index i of the set S_i it came from. | 大模型 | 3.609 | 11.264 | 7.655 | 3 |
| 3 | Using the encoding scheme '1^i # x', provide a formal definition for the combined set S. | 小模型 | 11.264 | 27.451 | 16.187 | 4 |
| 4 | Given the definition of S from the previous step, what is the length of a string x from a set S_i, if the corresponding encoded string '1^i # x' in S has a total length of m? | 小模型 | 27.451 | 43.637 | 16.187 | 5 |
| 5 | For a fixed length m and a fixed index i, how many strings in S of length m can originate from the set S_i? Express your answer in terms of the polynomial bound p_i for the set S_i. | 小模型 | 43.637 | 59.824 | 16.187 | 6 |
| 6 | To show that S is sparse, we must sum the number of strings of length m over all possible originating sets S_i for i=1 to k. Explain why the sum of these counts is still bounded by a polynomial in m. | 大模型 | 59.824 | 67.479 | 7.655 | 7 |
| 7 | Describe the step-by-step algorithm for a deterministic Turing Machine M with oracle access to S, that decides if a string x is in S_i, given the input &lt;x, i&gt;. | 小模型 | 27.451 | 43.637 | 16.187 | 8 |
| 8 | Analyze the time complexity of the Turing Machine M described in the previous step. Is it a polynomial-time algorithm? | 小模型 | 43.637 | 59.824 | 16.187 | 9 |
| 9 | What is the key difference in the definition of the complexity class P_bad-angel compared to P_angel? | 大模型 | 7.768 | 15.424 | 7.655 | 10 |
| 10 | To prove that P is a subset of P_bad-angel, describe how to construct the required components (poly-time algorithm A for the angel string, and poly-time TM M) for any language L that is already in P. | 大模型 | 15.424 | 23.079 | 7.655 | 1 |
| 11 | To prove that P_bad-angel is a subset of P, describe an algorithm for a standard deterministic polynomial-time Turing Machine that can decide any language L in P_bad-angel. | 大模型 | 15.424 | 23.079 | 7.655 | 2 |
| 12 | Based on the conclusions from the previous two steps, what is the precise relationship between the complexity classes P and P_bad-angel? | 小模型 | 23.079 | 39.266 | 16.187 | 3 |
| 13 | Given the established relationship between P and P_bad-angel, what can be concluded about the relationship between P_bad-angel and NP? | 小模型 | 39.266 | 55.453 | 16.187 | 4 |
| 14 | If an NP-complete language like SAT were shown to be in P_bad-angel, what would this imply about the fundamental relationship between P and NP? | 大模型 | 39.266 | 46.921 | 7.655 | 5 |
| 15 | Synthesizing the previous answers, is it generally believed that NP = P_bad-angel? Justify your answer. | 大模型 | 55.453 | 63.108 | 7.655 | 6 |
| 16 | According to the definition of P_angel, for a given language L, what is the specific piece of information that allows a deterministic polynomial-time TM to decide membership for all strings of a given length n? | 大模型 | 11.918 | 19.573 | 7.655 | 7 |
| 17 | Propose a structure for a sparse set S_L that can be used as an oracle to store the critical information identified in the previous step for every possible input length n. | 大模型 | 19.573 | 27.228 | 7.655 | 8 |
| 18 | Using the encoding '&lt;n&gt; # alpha_n', where &lt;n&gt; is a representation of the length n, provide a formal definition for the sparse set S_L. | 小模型 | 27.228 | 43.415 | 16.187 | 9 |
| 19 | Explain why the set S_L, as defined in the previous step, satisfies the definition of a sparse set. | 小模型 | 43.415 | 59.602 | 16.187 | 10 |
| 20 | Describe the algorithm for a deterministic polynomial-time Turing Machine M with oracle access to S_L that decides if an input string x belongs to the language L. | 大模型 | 43.415 | 51.071 | 7.655 | 1 |
| 21 | Provide a justification that the oracle TM M described in the previous step runs in polynomial time with respect to the length of the input x. | 大模型 | 51.071 | 58.726 | 7.655 | 2 |

## 理论执行甘特图

```
时间轴:
0                                                            64.54s
+------------------------------------------------------------+
步骤 1 |#######                                                     | 2.94s - 10.59s
步骤 2 |#######                                                     | 3.61s - 11.26s
步骤 9 |    #######                                                 | 7.77s - 15.42s
步骤 3 |       ###############                                      | 11.26s - 27.45s
步骤 16 |        #######                                             | 11.92s - 19.57s
步骤 10 |           #######                                          | 15.42s - 23.08s
步骤 11 |           #######                                          | 15.42s - 23.08s
步骤 17 |               #######                                      | 19.57s - 27.23s
步骤 12 |                  ###############                           | 23.08s - 39.27s
步骤 18 |                      ###############                       | 27.23s - 43.42s
步骤 4 |                      ###############                       | 27.45s - 43.64s
步骤 7 |                      ###############                       | 27.45s - 43.64s
步骤 13 |                                 ###############            | 39.27s - 55.45s
步骤 14 |                                 #######                    | 39.27s - 46.92s
步骤 19 |                                     ###############        | 43.42s - 59.60s
步骤 20 |                                     #######                | 43.42s - 51.07s
步骤 5 |                                     ###############        | 43.64s - 59.82s
步骤 8 |                                     ###############        | 43.64s - 59.82s
步骤 21 |                                            #######         | 51.07s - 58.73s
步骤 15 |                                                #######     | 55.45s - 63.11s
步骤 6 |                                                    ########| 59.82s - 67.48s
```

