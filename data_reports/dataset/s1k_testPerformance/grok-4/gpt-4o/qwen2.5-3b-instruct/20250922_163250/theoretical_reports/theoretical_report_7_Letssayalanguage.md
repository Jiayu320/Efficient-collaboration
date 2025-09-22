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
| 路由模型 (grok-4) | 12.650 | 36.37 |

## 执行流程理论时间

| 阶段 | 理论时间 (秒) | 百分比 |
| --- | --- | --- |
| 规划阶段总时间 (Planner) | 29.560 | 100% |
| 规划过程中启动的任务数 | 6 / 6 | 100.0% |
| 规划与执行重叠的任务数 | 5 / 6 | 83.3% |
| 第一个任务规划完成时间 | 15.894 | - |
| 最后一个任务规划完成时间 | 29.477 | - |
| 最后一个任务执行完成时间 | 30.766 | - |
| 任务总执行时间(累计) | 7.040 | - |
| 流水线加速比 | 1.69x | - |
| 并行效率 | 22.9% | - |

## 任务类型理论时间

| 模型类型 | 任务数 | 顺序执行时间 (秒) | 并行加速比 |
| --- | --- | --- | --- |
| 小模型任务 | 0 | 0.000 | - |
| 大模型任务 | 6 | 7.040 | - |
| 规划模型 | 1 | 44.847 | - |
| 顺序总时间 | - | 51.887 | - |
| 并行总时间 | - | 30.766 | 1.69x |

## 任务执行明细

| 步骤ID | 任务描述 | 使用模型 | 理论开始时间 (秒) | 理论结束时间 (秒) | 理论执行时间 (秒) | 工作线程 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | For part 1, define the combined sparse set S by, for each i from 1 to k and each x in Si with |x|=n, including in S the string 0^{q(|x| + log k)} 1^i 0^{r(n)} x where q and r are polynomials chosen to ensure unique lengths and sparsity; what is the explicit definition of S ensuring |S^{=m}| <= poly(m) for all m? | 大模型 | 15.894 | 17.183 | 1.289 | 2 |
| 2 | For part 1, describe the deterministic poly-time TM M with oracle S that, on input <x,i> with |x|=n, constructs the query string as per the padding and prefix from Step 1 corresponding to i and x, queries if it is in S, and accepts if yes; what is the step-by-step algorithm for M? | 大模型 | 18.424 | 19.574 | 1.150 | 3 |
| 3 | For part 2, to show P = P_{bad-angel}, argue that any language in P_{bad-angel} can be decided by a poly-time TM that first runs A to compute alpha_n = A(n) then runs M(x, alpha_n), and conversely any P language has trivial computable angel strings (e.g., empty); what is the justification for equality? | 大模型 | 21.119 | 22.200 | 1.081 | 4 |
| 4 | For part 2, to address NP = P_{bad-angel}, note that if NP = P then yes, but assuming NP != P (standard conjecture), then NP != P_{bad-angel} since P_{bad-angel} = P, and provide an example like SAT in NP but not believed in P; what is the justification for inequality under the assumption? | 大模型 | 23.786 | 24.936 | 1.150 | 5 |
| 5 | For part 3, define the sparse set S_L as {1^n 0 alpha_n | n in N}, which has at most one string per length n + 1 + p(n), hence sparse with bounding polynomial n + 1 + p(n); what is the explicit definition of S_L? | 大模型 | 26.040 | 27.121 | 1.081 | 6 |
| 6 | For part 3, describe the deterministic poly-time TM M with oracle S_L that, on input x with |x|=n, enumerates possible strings y of length n + 1 + p(n) starting with 1^n 0, queries if y in S_L, and if found extracts alpha_n and runs the P_angel machine M(x, alpha_n) to decide; since at most one such y, it's poly-time; what is the final description of M and proof it decides L? | 大模型 | 29.477 | 30.766 | 1.289 | 7 |

## 理论执行甘特图

```
时间轴:
0                                                            14.87s
+------------------------------------------------------------+
步骤 1 |#####                                                       | 15.89s - 17.18s
步骤 2 |          ####                                              | 18.42s - 19.57s
步骤 3 |                     ####                                   | 21.12s - 22.20s
步骤 4 |                               #####                        | 23.79s - 24.94s
步骤 5 |                                        #####               | 26.04s - 27.12s
步骤 6 |                                                      ######| 29.48s - 30.77s
```

