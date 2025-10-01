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
| 规划阶段总时间 (Planner) | 7.694 | 100% |
| 规划过程中启动的任务数 | 3 / 6 | 50.0% |
| 规划与执行重叠的任务数 | 3 / 6 | 50.0% |
| 第一个任务规划完成时间 | 3.406 | - |
| 最后一个任务规划完成时间 | 7.662 | - |
| 最后一个任务执行完成时间 | 30.704 | - |
| 任务总执行时间(累计) | 54.464 | - |
| 流水线加速比 | 2.02x | - |
| 并行效率 | 177.4% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 1 | 16.187 | - |
| 大模型任务 | 5 | 38.277 | - |
| 规划模型 | 1 | 7.480 | - |
| 顺序总时间 | - | 61.944 | - |
| 并行总时间 | - | 30.704 | 2.02x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | To solve Part 1, what is an effective strategy for creating a single sparse set `S` from `k` sparse sets `S_i`? Propose a specific string format for elements in `S` that encodes both the original string `x` and its source set index `i`. | 大模型 | 3.406 | 11.061 | 7.655 | 2 |
| 2 | Using the encoding format from Step 1, provide a mathematical argument to show that the resulting set `S` is also sparse. Then, describe the algorithm for the oracle TM `M` that uses `S` to decide if a given string `x` belongs to a specific set `S_i`. | 大模型 | 11.061 | 18.717 | 7.655 | 3 |
| 3 | To solve Part 2, first analyze the relationship between `P` and `P_bad-angel`. What are the arguments for both inclusions, `P_bad-angel \subseteq P` and `P \subseteq P_bad-angel`, to demonstrate their equivalence? | 大模型 | 5.102 | 12.757 | 7.655 | 4 |
| 4 | Continuing Part 2, what is the relationship between `NP` and `P_bad-angel`? What major open question in computer science would be resolved if it were proven that `NP \subseteq P_bad-angel`? | 大模型 | 12.757 | 20.413 | 7.655 | 5 |
| 5 | To solve Part 3, what is the key non-uniform information that the 'angel string' `\alpha_n` provides for a `P_angel` language? Propose a method to store all these angel strings (one for each length `n`) in a single sparse oracle set `S_L`, including a specific format for the strings in `S_L`. | 大模型 | 6.862 | 14.517 | 7.655 | 6 |
| 6 | Based on the construction of `S_L` from Step 5, what is the formal argument that this set is sparse? Also, describe the algorithm for the oracle TM that uses `S_L` to find the correct angel string and decide the language `L`. | 小模型 | 14.517 | 30.704 | 16.187 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            27.30s
+------------------------------------------------------------+
步骤 1 |################                                            | 3.41s - 11.06s
步骤 3 |   #################                                        | 5.10s - 12.76s
步骤 5 |       #################                                    | 6.86s - 14.52s
步骤 2 |                #################                           | 11.06s - 18.72s
步骤 4 |                    #################                       | 12.76s - 20.41s
步骤 6 |                        ####################################| 14.52s - 30.70s
```

