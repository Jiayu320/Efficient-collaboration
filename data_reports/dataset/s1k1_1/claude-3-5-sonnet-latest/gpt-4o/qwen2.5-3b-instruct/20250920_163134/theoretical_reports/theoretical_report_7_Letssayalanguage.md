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
| 规划阶段总时间 (Planner) | 10.757 | 100% |
| 规划过程中启动的任务数 | 8 / 9 | 88.9% |
| 规划与执行重叠的任务数 | 8 / 9 | 88.9% |
| 第一个任务规划完成时间 | 2.309 | - |
| 最后一个任务规划完成时间 | 10.699 | - |
| 最后一个任务执行完成时间 | 12.188 | - |
| 任务总执行时间(累计) | 10.528 | - |
| 流水线加速比 | 2.41x | - |
| 并行效率 | 86.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 1.465 | - |
| 大模型任务 | 8 | 9.063 | - |
| 规划模型 | 1 | 18.816 | - |
| 顺序总时间 | - | 29.345 | - |
| 并行总时间 | - | 12.188 | 2.41x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For part 1, how can we encode elements from multiple sparse sets into a single sparse set while maintaining their original set membership information? | 大模型 | 2.309 | 3.390 | 1.081 | 2 |
| 2 | Given that each Si is sparse with |Si^=n| ≤ pi(n) for some polynomial pi, what would be a suitable encoding scheme for S that preserves sparsity and allows for efficient retrieval? | 大模型 | 3.513 | 4.663 | 1.150 | 3 |
| 3 | How can we design the oracle TM M that, given input ⟨x,i⟩, efficiently determines whether x ∈ Si by making appropriate queries to the oracle S? | 小模型 | 4.663 | 6.128 | 1.465 | 4 |
| 4 | For part 2, what is the relationship between P_bad-angel and P, given that the angel string must be computable in polynomial time? | 大模型 | 5.533 | 6.614 | 1.081 | 5 |
| 5 | If α_n is computable in polynomial time, can P_bad-angel decide any languages that P cannot? Conversely, can P decide any languages that P_bad-angel cannot? | 大模型 | 6.679 | 7.829 | 1.150 | 6 |
| 6 | What is the relationship between P_bad-angel and NP? Can P_bad-angel decide languages that are NP-complete? | 大模型 | 7.829 | 8.979 | 1.150 | 7 |
| 7 | For part 3, given a language L ∈ P_angel with angel strings {α_n}, how can we construct a sparse set S_L that encodes the necessary information to decide L? | 大模型 | 8.737 | 9.887 | 1.150 | 8 |
| 8 | What information needs to be included in S_L to allow a polynomial-time oracle TM to decide L? How does this relate to the angel strings {α_n}? | 大模型 | 9.887 | 11.107 | 1.219 | 9 |
| 9 | How can we design the oracle TM M that, given access to S_L, efficiently decides whether any input x is in L? | 大模型 | 11.107 | 12.188 | 1.081 | 10 |

## 理论执行甘特图

```
时间轴:
0                                                            9.88s
+------------------------------------------------------------+
步骤 1 |######                                                      | 2.31s - 3.39s
步骤 2 |       #######                                              | 3.51s - 4.66s
步骤 3 |              #########                                     | 4.66s - 6.13s
步骤 4 |                   #######                                  | 5.53s - 6.61s
步骤 5 |                          #######                           | 6.68s - 7.83s
步骤 6 |                                 #######                    | 7.83s - 8.98s
步骤 7 |                                       #######              | 8.74s - 9.89s
步骤 8 |                                              #######       | 9.89s - 11.11s
步骤 9 |                                                     #######| 11.11s - 12.19s
```

