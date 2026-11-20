# 端到端 RAG 系统 · 自测

每题先选答案，再展开解析。

## 1. 为什么集成测试才是给一条六组件 RAG pipeline 打分的唯一诚实方式？

- **A** 生产服务器无法运行单个阶段的测试
- **B** 每个阶段单独的指标都预测不了整个系统的指标，因为每个阶段都会与下一个阶段相互作用；唯一有效的评分方式是用同一份 qrels 把整条 pipeline 端到端跑一遍
- **C** 这些组件跑在不同的机器上
- **D** chunker 是唯一重要的组件

<details>
<summary>查看答案与解析</summary>

**答案**　B

各阶段的孤立胜利无法叠加成整体；pipeline 要看联合输出来打分。

</details>

## 2. 答案生成器里「低置信度就拒答（refuse-on-low-confidence）」的作用是什么？

- **A** 用另一个 chunker 触发一次重新检索
- **B** 把每一次拒答都写到磁盘里
- **C** 当 reranker 的 top-1 分数低于某个语料相关的阈值时，就返回「我不知道」，从而在召回的上下文没有切中 query 时避免产生臆造的答案
- **D** 拦截超过 100 个 token 的 query

<details>
<summary>查看答案与解析</summary>

**答案**　C

一个持续偏低的 rank-1 分数，是模型在告诉你语料里没有任何东西能回答这个 query；这时应当拒答，而不是去臆造。

</details>

## 3. 为什么 rerank 的训练三元组要与评估 query 保持互不相交？

- **A** 为了省 GPU 显存
- **B** 因为 cross-encoder 要求不同的词表
- **C** 为了防止训练-测试泄漏；如果评估 query 与 rerank 训练集重叠，评估看起来会好得不真实，回归测试也就抓不到真实的漂移
- **D** 因为 RRF 无法融合相互重叠的列表

<details>
<summary>查看答案与解析</summary>

**答案**　C

严格隔离是最基本的卫生准则；否则 rerank 指标预测不了生产中的真实表现。

</details>

## 4. 自终止 demo 的退出码（exit code）有什么用？

- **A** 它把「是否达标」编码进退出码：CI 冒烟测试可以把这个 demo 接入 pipeline，并以非零退出码来卡住合并
- **B** reranker 把它当作训练信号
- **C** 纯装饰
- **D** Python 强制要求

<details>
<summary>查看答案与解析</summary>

**答案**　A

退出码 0 表示达到阈值；非零表示出现回归。这正是 CI 门禁所消费的契约。

</details>

## 5. 在这条 pipeline 里，引用锚点（citation anchor）长什么样？

- **A** 带源 URL 的 Markdown 链接
- **B** embedding 向量本身
- **C** JSON-RPC 信封
- **D** [doc_id:chunk_index]

<details>
<summary>查看答案与解析</summary>

**答案**　D

生成器把 (doc_id, chunk_index) 元组作为锚点输出，这样下游的 UI 或审计方就能把每一条主张映射回它的来源 chunk。

</details>

## 6. 哪种失效模式对 mock 生成器是不可见的，必须在上线前用真实 LLM 测试？

- **A** 向量索引大小
- **B** 延迟
- **C** tokenization
- **D** 幻觉（hallucination）：mock 生成器只会从召回的 chunk 里输出文字、无法凭空造内容；而真实 LLM 可能会无视这些 chunk、生成无依据的答案

<details>
<summary>查看答案与解析</summary>

**答案**　D

mock 无法测试生成器在臆造内容面前的安全性；只有换上真实模型才能测。

</details>


[返回本课](docs/zh.md)
