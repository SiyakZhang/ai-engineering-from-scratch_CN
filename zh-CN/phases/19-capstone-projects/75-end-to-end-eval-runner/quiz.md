# 端到端 eval runner · 自测

每题先选答案，再展开解析。

## 1. ModelAdapter 接口最小可行的暴露面是什么？

- **A** load_weights、generate、save_weights
- **B** complete、embed、classify、summarise
- **C** generate(prompt, task)，返回文本外加可选的置信度和逐 token nll
- **D** init、login、generate、close

<details>
<summary>查看答案与解析</summary>

**答案**　C

一个方法就能覆盖任何适配器。其余都是可选的装饰。runner 并不需要更丰富的接口面。

</details>

## 2. 为什么 runner 接受一个 parallel 标志，而不是一律并行运行？

- **A** 并行执行需要 GPU
- **B** 测试需要确定性的执行顺序；这个标志让它们能切回顺序执行
- **C** ThreadPoolExecutor 不在标准库里
- **D** 在 CPython 里并行执行不安全

<details>
<summary>查看答案与解析</summary>

**答案**　B

测试要可复现，生产要吞吐量。这个标志把这两个诉求拆开，而不用维护两条代码路径。

</details>

## 3. runner 是怎么为校准缓冲区确定「正确」标志的？

- **A** 默认对 exact_match 风格的 metric 用阈值 1.0，对分级（graded）metric 用阈值 0.5
- **B** 它用平均 bin 置信度
- **C** 它调用适配器两次并比较输出
- **D** 它用 Brier 分解

<details>
<summary>查看答案与解析</summary>

**答案**　A

阈值是 metric 感知的：exact_match 风格的 metric 用接近 1.0 的截断，分级 metric 默认用 0.5。

</details>

## 4. 为什么 runner 要构建 EvalRun 记录再交给聚合器，而不是内联算出 leaderboard？

- **A** 聚合器在 numpy 数组上比在 dataclass 上更快
- **B** JSON Schema 要求用 EvalRun
- **C** EvalRun 更省内存
- **D** 这能让 runner 对聚合器无感知，并让 leaderboard 层独立演进而不用动 runner

<details>
<summary>查看答案与解析</summary>

**答案**　D

组合优于内联。runner 产出记录，聚合器掌管 leaderboard 的数学。每节课只负责一件事。

</details>

## 5. 最终 JSON 信封里那块 perplexity 的作用是什么？

- **A** 它是校准报告的输入
- **B** 它是从 bootstrap CI 算出来的
- **C** 它承载每个模型在留出集上的语言建模数字，独立于任务打分
- **D** 它是 leaderboard 排名所必需的

<details>
<summary>查看答案与解析</summary>

**答案**　C

perplexity 是放在 leaderboard 旁边，而不是嵌在里面。它用的是适配器逐次调用返回的 token NLL 和 token 数。

</details>

## 6. 这个自终止 demo 的「干净跑完」退出标准是什么？

- **A** 每一对的 bootstrap CI 都不含零
- **B** 每个模型的 ECE 都低于 0.05
- **C** 每个任务都打分高于 0.9
- **D** 每个任务都校验、都打分，校准已聚合，并且基于规则的适配器在 leaderboard 上严格高于随机适配器

<details>
<summary>查看答案与解析</summary>

**答案**　D

这个 demo 端到端地强制契约：每一层都跑过了，而最准的适配器也据此排在前面。

</details>


[返回本课](docs/zh.md)
