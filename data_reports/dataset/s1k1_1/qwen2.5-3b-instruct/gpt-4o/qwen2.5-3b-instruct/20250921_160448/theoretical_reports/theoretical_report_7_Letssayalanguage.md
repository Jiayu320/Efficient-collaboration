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
| 路由模型 (qwen2.5-3b-instruct) | 0.690 | 64.53 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 4.766 | 100% |
| 规划过程中启动的任务数 | 5 / 5 | 100.0% |
| 规划与执行重叠的任务数 | 4 / 5 | 80.0% |
| 第一个任务规划完成时间 | 1.480 | - |
| 最后一个任务规划完成时间 | 4.719 | - |
| 最后一个任务执行完成时间 | 20.906 | - |
| 任务总执行时间(累计) | 65.828 | - |
| 流水线加速比 | 3.66x | - |
| 并行效率 | 314.9% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 4 | 64.747 | - |
| 大模型任务 | 1 | 1.081 | - |
| 规划模型 | 1 | 10.639 | - |
| 顺序总时间 | - | 76.467 | - |
| 并行总时间 | - | 20.906 | 3.66x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Define the sparse set \( S \) as the union of \( S_1, S_2, \ldots, S_k \). | 大模型 | 1.480 | 2.561 | 1.081 | 2 |
| 2 | Show that \( S \) is sparse by proving \( |S^{=n}| \leq p(n) \), where \( p(n) \) is the maximum of the polynomials bounding \( |S_i^{=n}| \). | 小模型 | 2.519 | 18.705 | 16.187 | 3 |
| 3 | Describe the Turing Machine \( M \) that queries the oracle \( S \) and decides \( x \in L \). | 小模型 | 3.200 | 19.387 | 16.187 | 4 |
| 4 | Prove that \( M \) runs in polynomial time and correctly decides \( x \in L \). | 小模型 | 3.836 | 20.022 | 16.187 | 5 |
| 5 | Conclude that there exists a sparse set \( S \) and a polynomial-time TM \( M \) with oracle access to \( S \) such that \( M \) decides \( L \). | 小模型 | 4.719 | 20.906 | 16.187 | 6 |

## 理论执行甘特图

```
时间轴:
0                                                            19.43s
+------------------------------------------------------------+
步骤 1 |###                                                         | 1.48s - 2.56s
步骤 2 |   ##################################################       | 2.52s - 18.71s
步骤 3 |     ##################################################     | 3.20s - 19.39s
步骤 4 |       ##################################################   | 3.84s - 20.02s
步骤 5 |          ##################################################| 4.72s - 20.91s
```

