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
| 大模型 (deepseek-chat) | 1.600 | 31.97 |
| 路由模型 (gemini-2.5-flash-thinking) | 0.737 | 103.71 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 8.403 | 100% |
| 规划过程中启动的任务数 | 4 / 18 | 22.2% |
| 规划与执行重叠的任务数 | 4 / 18 | 22.2% |
| 第一个任务规划完成时间 | 1.113 | - |
| 最后一个任务规划完成时间 | 8.374 | - |
| 最后一个任务执行完成时间 | 134.843 | - |
| 任务总执行时间(累计) | 525.057 | - |
| 流水线加速比 | 4.03x | - |
| 并行效率 | 389.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 4 | 64.747 | - |
| 大模型任务 | 14 | 460.311 | - |
| 规划模型 | 1 | 18.093 | - |
| 顺序总时间 | - | 543.151 | - |
| 并行总时间 | - | 134.843 | 4.03x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the definition of a 'sparse set' in theoretical computer science? | 大模型 | 1.113 | 33.992 | 32.879 | 2 |
| 2 | What is the definition of a 'deterministic polynomial time Turing Machine (DPTM) with oracle access'? | 大模型 | 1.527 | 34.407 | 32.879 | 3 |
| 3 | Given k sparse sets S_1, ..., S_k, define a single sparse set S that encodes membership information for all S_i. Provide the formal construction of S. | 大模型 | 33.992 | 66.871 | 32.879 | 4 |
| 4 | Explain why the set S defined in Step 3 is sparse, referencing the sparsity of the individual S_i sets. | 大模型 | 66.871 | 99.751 | 32.879 | 5 |
| 5 | Describe the operation of a DPTM M with oracle access to S, that accepts input &lt;x,i&gt; if and only if x ∈ S_i. | 大模型 | 66.871 | 99.751 | 32.879 | 6 |
| 6 | Justify that the DPTM M described in Step 5 runs in polynomial time. | 小模型 | 99.751 | 115.937 | 16.187 | 7 |
| 7 | What is the definition of the complexity class P_bad-angel, as provided in the problem statement? | 大模型 | 3.832 | 36.711 | 32.879 | 8 |
| 8 | Does P_bad-angel contain all languages in P? Justify your answer. | 大模型 | 36.711 | 69.591 | 32.879 | 9 |
| 9 | Are all languages in P_bad-angel also in P? Justify your answer. | 大模型 | 36.711 | 69.591 | 32.879 | 10 |
| 10 | Based on the answers to Steps 8 and 9, what is the relationship between P and P_bad-angel? | 小模型 | 69.591 | 85.777 | 16.187 | 1 |
| 11 | Does NP contain all languages in P_bad-angel? Justify your answer. | 大模型 | 85.777 | 118.657 | 32.879 | 2 |
| 12 | Are all languages in NP also in P_bad-angel? Justify your answer, considering the implications for P vs NP. | 大模型 | 36.711 | 69.591 | 32.879 | 3 |
| 13 | Based on the answers to Steps 11 and 12, what is the relationship between NP and P_bad-angel? | 小模型 | 118.657 | 134.843 | 16.187 | 4 |
| 14 | What is the definition of the complexity class P_angel, as provided in the problem statement? | 大模型 | 6.715 | 39.594 | 32.879 | 5 |
| 15 | For a language L ∈ P_angel, define a sparse set S_L that stores the necessary angel strings. Provide the formal construction of S_L. | 大模型 | 39.594 | 72.474 | 32.879 | 6 |
| 16 | Explain why the set S_L defined in Step 15 is sparse. | 大模型 | 72.474 | 105.353 | 32.879 | 7 |
| 17 | Describe the operation of a DPTM M with oracle access to S_L, that decides the language L. | 大模型 | 72.474 | 105.353 | 32.879 | 8 |
| 18 | Justify that the DPTM M described in Step 17 runs in polynomial time. | 小模型 | 105.353 | 121.540 | 16.187 | 9 |

## 理论执行甘特图

```
时间轴:
0                                                            133.73s
+------------------------------------------------------------+
步骤 1 |##############                                              | 1.11s - 33.99s
步骤 2 |##############                                              | 1.53s - 34.41s
步骤 7 | ##############                                             | 3.83s - 36.71s
步骤 14 |  ###############                                           | 6.72s - 39.59s
步骤 3 |              ###############                               | 33.99s - 66.87s
步骤 8 |               ###############                              | 36.71s - 69.59s
步骤 9 |               ###############                              | 36.71s - 69.59s
步骤 12 |               ###############                              | 36.71s - 69.59s
步骤 15 |                 ###############                            | 39.59s - 72.47s
步骤 4 |                             ###############                | 66.87s - 99.75s
步骤 5 |                             ###############                | 66.87s - 99.75s
步骤 10 |                              #######                       | 69.59s - 85.78s
步骤 16 |                                ##############              | 72.47s - 105.35s
步骤 17 |                                ##############              | 72.47s - 105.35s
步骤 11 |                                     ###############        | 85.78s - 118.66s
步骤 6 |                                            #######         | 99.75s - 115.94s
步骤 18 |                                              ########      | 105.35s - 121.54s
步骤 13 |                                                    ########| 118.66s - 134.84s
```

