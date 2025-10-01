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
| 规划阶段总时间 (Planner) | 13.112 | 100% |
| 规划过程中启动的任务数 | 6 / 17 | 35.3% |
| 规划与执行重叠的任务数 | 6 / 17 | 35.3% |
| 第一个任务规划完成时间 | 2.937 | - |
| 最后一个任务规划完成时间 | 13.080 | - |
| 最后一个任务执行完成时间 | 77.503 | - |
| 任务总执行时间(累计) | 198.392 | - |
| 流水线加速比 | 2.73x | - |
| 并行效率 | 256.0% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 8 | 129.493 | - |
| 大模型任务 | 9 | 68.899 | - |
| 规划模型 | 1 | 13.059 | - |
| 顺序总时间 | - | 211.451 | - |
| 并行总时间 | - | 77.503 | 2.73x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the formal definition of a 'sparse set' in computational complexity theory? | 大模型 | 2.937 | 10.592 | 7.655 | 2 |
| 2 | To combine k sparse sets (S_1, ..., S_k) into a single set S, propose a string encoding scheme that incorporates both the original string 'x' from S_i and its original set index 'i'. | 大模型 | 3.641 | 11.296 | 7.655 | 3 |
| 3 | Using the definition from Step 1 and the encoding from Step 2, explain why the resulting combined set S is also a sparse set. | 大模型 | 11.296 | 18.951 | 7.655 | 4 |
| 4 | Describe the step-by-step algorithm for a deterministic Turing Machine M that uses an oracle for the set S (from Step 2) to decide if an input string 'x' belongs to a specific original set S_i. | 小模型 | 11.296 | 27.483 | 16.187 | 5 |
| 5 | Analyze the time complexity of the Turing Machine M described in Step 4. Does it run in polynomial time? Justify your answer. | 小模型 | 27.483 | 43.669 | 16.187 | 6 |
| 6 | Based on the problem description, what is the formal definition of the complexity class P_bad-angel, and what is the key difference between it and P_angel? | 小模型 | 5.977 | 22.163 | 16.187 | 7 |
| 7 | To prove that P is a subset of P_bad-angel, assume a language L is in P. How can you construct a polynomial-time algorithm 'A' for the angel string and a polynomial-time TM 'M' that satisfy the definition of P_bad-angel for L? | 大模型 | 22.163 | 29.819 | 7.655 | 8 |
| 8 | To prove that P_bad-angel is a subset of P, assume a language L is in P_bad-angel. Describe how to construct a single, standard deterministic polynomial-time Turing machine that decides L. | 大模型 | 22.163 | 29.819 | 7.655 | 9 |
| 9 | Based on the bidirectional proofs in Steps 7 and 8, what is the definitive relationship between the complexity classes P and P_bad-angel? | 小模型 | 29.819 | 46.005 | 16.187 | 10 |
| 10 | Given the relationship established in Step 9, rephrase the question 'Is NP = P_bad-angel?' into an equivalent, well-known open problem in complexity theory. | 小模型 | 46.005 | 62.192 | 16.187 | 1 |
| 11 | If an NP-complete language, such as SAT, were proven to be in P_bad-angel, what would be the major implication for the relationship between P and NP? | 大模型 | 62.192 | 69.847 | 7.655 | 2 |
| 12 | Based on the current consensus in theoretical computer science regarding the problem identified in Step 10, what is the most likely (though unproven) answer to whether NP = P_bad-angel? | 大模型 | 69.847 | 77.503 | 7.655 | 3 |
| 13 | According to the definition of P_angel, what is the critical piece of information, specific to each input length 'n', that allows a polynomial-time TM to decide a language L? | 小模型 | 10.552 | 26.739 | 16.187 | 4 |
| 14 | Propose a structure for a new set, S_L, that can store the critical information from Step 13 for every possible input length 'n'. The structure should allow for unambiguous retrieval of the information for a given 'n'. | 大模型 | 26.739 | 34.394 | 7.655 | 5 |
| 15 | Using the formal definition of a sparse set from Step 1, provide a justification for why the set S_L, as constructed in Step 14, is sparse. | 大模型 | 34.394 | 42.050 | 7.655 | 6 |
| 16 | Describe the algorithm for a deterministic Turing Machine M that, given an input 'x' of length 'n' and oracle access to the sparse set S_L, can decide the language L. | 小模型 | 34.394 | 50.581 | 16.187 | 7 |
| 17 | Analyze the time complexity of the oracle machine M described in Step 16. Explain why its runtime is considered polynomial in the length of the input 'x'. | 小模型 | 50.581 | 66.768 | 16.187 | 8 |

## 理论执行甘特图

```
时间轴:
0                                                            74.57s
+------------------------------------------------------------+
步骤 1 |######                                                      | 2.94s - 10.59s
步骤 2 |######                                                      | 3.64s - 11.30s
步骤 6 |  #############                                             | 5.98s - 22.16s
步骤 13 |      #############                                         | 10.55s - 26.74s
步骤 3 |      ######                                                | 11.30s - 18.95s
步骤 4 |      #############                                         | 11.30s - 27.48s
步骤 7 |               ######                                       | 22.16s - 29.82s
步骤 8 |               ######                                       | 22.16s - 29.82s
步骤 14 |                   ######                                   | 26.74s - 34.39s
步骤 5 |                   #############                            | 27.48s - 43.67s
步骤 9 |                     #############                          | 29.82s - 46.01s
步骤 15 |                         ######                             | 34.39s - 42.05s
步骤 16 |                         #############                      | 34.39s - 50.58s
步骤 10 |                                  #############             | 46.01s - 62.19s
步骤 17 |                                      #############         | 50.58s - 66.77s
步骤 11 |                                               ######       | 62.19s - 69.85s
步骤 12 |                                                     #######| 69.85s - 77.50s
```

