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
| 路由模型 (gpt-5) | 6.407 | 50.57 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 21.770 | 100% |
| 规划过程中启动的任务数 | 6 / 10 | 60.0% |
| 规划与执行重叠的任务数 | 6 / 10 | 60.0% |
| 第一个任务规划完成时间 | 7.692 | - |
| 最后一个任务规划完成时间 | 21.711 | - |
| 最后一个任务执行完成时间 | 45.201 | - |
| 任务总执行时间(累计) | 119.210 | - |
| 流水线加速比 | 3.10x | - |
| 并行效率 | 263.7% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 5 | 80.933 | - |
| 大模型任务 | 5 | 38.277 | - |
| 规划模型 | 1 | 21.098 | - |
| 顺序总时间 | - | 140.309 | - |
| 并行总时间 | - | 45.201 | 3.10x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | What is the formal definition of a sparse set in terms of the number of strings of each length, and what exactly is the oracle query interface and response semantics for a deterministic polynomial-time Turing Machine with oracle S? | 大模型 | 7.692 | 15.347 | 7.655 | 2 |
| 2 | Design a binary, prefix-decodable encoding that combines an index i ∈ {1,...,k} and a string x into a single binary string, and define the set S using this encoding so that deciding whether x ∈ S_i reduces to a single membership query of the encoded string to S. What encoding and definition achieve this without using any non-binary separators? | 大模型 | 15.347 | 23.003 | 7.655 | 3 |
| 3 | Given that each S_i is sparse with a polynomial bound p_i(m) on |S_i^{=m}|, derive a polynomial bound on |S^{=n}| under your encoding from Step 2 and explain why S is sparse. | 小模型 | 23.003 | 39.189 | 16.187 | 4 |
| 4 | Using the encoding from Step 2, how should the oracle Turing Machine M operate on input ⟨x,i⟩ to decide whether x ∈ S_i via a single membership query to S, and why does M run in polynomial time? | 小模型 | 23.003 | 39.189 | 16.187 | 5 |
| 5 | Precisely restate the definitions of P_angel and P_bad-angel, emphasizing the role of the angel strings α_n and the additional requirement in P_bad-angel that α_n be computable in polynomial time. What are these definitions? | 大模型 | 13.703 | 21.358 | 7.655 | 6 |
| 6 | How can you show that every language in P is in P_bad-angel by choosing a trivial, polynomial-time computable angel string and an M that ignores it? What is the resulting runtime on input x? | 小模型 | 21.358 | 37.545 | 16.187 | 7 |
| 7 | How can you show that every language in P_bad-angel is in P by computing α_|x| in polynomial time and then running M(x, α_|x|)? What is the combined runtime bound in terms of |x|? | 小模型 | 21.358 | 37.545 | 16.187 | 8 |
| 8 | Synthesizing Steps 6 and 7, what is the relationship between P and P_bad-angel? Additionally, if SAT were in P_bad-angel, what consequence would follow for P versus NP, and what conditional conclusion should be stated? | 大模型 | 37.545 | 45.201 | 7.655 | 9 |
| 9 | For a language L in P_angel with angel strings α_n of length p(n), construct a sparse binary set S_L that encodes the bits of α_n so that, given n and an index j, the j-th bit of α_n can be recovered via membership queries to S_L in O(1) time per query. Specify the encoding and prove that S_L is sparse. | 大模型 | 21.358 | 29.014 | 7.655 | 10 |
| 10 | Given S_L from Step 9, describe a deterministic polynomial-time oracle Turing Machine for L that, on input x of length n, reconstructs α_n using membership queries and then decides L by running the given polynomial-time machine M(x, α_n). How many oracle queries and time does this take as a function of n, and why is the whole computation polynomial? | 小模型 | 29.014 | 45.201 | 16.187 | 1 |

## 理论执行甘特图

```
时间轴:
0                                                            37.51s
+------------------------------------------------------------+
步骤 1 |############                                                | 7.69s - 15.35s
步骤 5 |         ############                                       | 13.70s - 21.36s
步骤 2 |            ############                                    | 15.35s - 23.00s
步骤 6 |                     ##########################             | 21.36s - 37.55s
步骤 7 |                     ##########################             | 21.36s - 37.55s
步骤 9 |                     #############                          | 21.36s - 29.01s
步骤 3 |                        ##########################          | 23.00s - 39.19s
步骤 4 |                        ##########################          | 23.00s - 39.19s
步骤 10 |                                  ##########################| 29.01s - 45.20s
步骤 8 |                                               #############| 37.55s - 45.20s
```

