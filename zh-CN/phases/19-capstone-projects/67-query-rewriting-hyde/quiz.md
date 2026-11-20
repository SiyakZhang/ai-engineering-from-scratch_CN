# Query 改写：HyDE、Multi-Query 与 Decomposition · 自测

每题先选答案，再展开解析。

## 1. HyDE（Hypothetical Document Embeddings）的核心机制是什么？

- **A** 用一个更大的模型来 embed 用户 query
- **B** 对 query 做哈希，再去缓存里查
- **C** 把 query 喂给多个 retriever，再挑出最好的那个
- **D** 用 LLM 生成一段假的答案，把这份假想文档 embed 出来，然后拿它的向量去检索，而不是用 query 向量

<details>
<summary>查看答案与解析</summary>

**答案**　D

HyDE 用语料的语气写出一段文档形态的文字，并基于它的 embedding 去检索；query 向量被替换掉了。

</details>

## 2. 为什么 HyDE 里 LLM 生成的假想文档即便事实有误也无所谓？

- **A** retriever 在意的是 token 分布而非事实正确性；假想文档的向量会落在真实段落附近
- **B** 出错时这次 LLM 调用会被回滚
- **C** 用户永远看不到这份假想文档
- **D** reranker 会修正事实错误

<details>
<summary>查看答案与解析</summary>

**答案**　A

retrieval 本质是 embedding 空间里的相似度；只要假想文档的词汇与语料匹配，它的向量就会落在正确的区域。

</details>

## 3. 多 query 扩展（multi-query expansion）和 query 拆解（decomposition）的区别是什么？

- **A** 多 query 用 cosine，拆解用 BM25
- **B** 它们完全一样
- **C** 拆解在本地跑，多 query 需要远程模型
- **D** 多 query 产出同一个问题的 N 个改写；拆解产出若干子问题，它们合起来覆盖一个多主题的问题

<details>
<summary>查看答案与解析</summary>

**答案**　D

改写保留意图；子问题则把一个多主题 query 拆成可以各自独立回答的片段。

</details>

## 4. query 拆解在什么情况下会过度拆分、反而损害 retrieval？

- **A** 当 query 对 LLM 来说太长时
- **B** 当 query 本身是原子的（单一主题）时，拆解器会硬造出假的子问题，结果各路检索都返回同一个文档，但排名被拉低了
- **C** 当 BM25 被禁用时
- **D** 当语料太小时

<details>
<summary>查看答案与解析</summary>

**答案**　B

拆解一个原子 query 会把它拆成假的子问题；这些子问题的检索结果稀释了合并结果，让正确文档排得更靠后。

</details>

## 5. 为什么这三种重写策略用 RRF 融合，而不是用分数插值？

- **A** 分数插值需要按语料做标定；RRF 基于排名贡献做组合、无需标定，而在融合来自不同重写的 N 路检索时正需要这一点
- **B** RRF 是 Python 唯一支持的操作
- **C** 分数插值无法处理超过两个列表
- **D** RRF 能在 GPU 上跑，分数插值不能

<details>
<summary>查看答案与解析</summary>

**答案**　A

和第 65 课同样的论证；基于排名的融合不需要按语料调 alpha，并且在面对各种重写器输出时都保持稳定。

</details>

## 6. 并行跑这三个重写器时，延迟的下限是多少？

- **A** 最慢的那一路单次检索
- **B** 串行的三次 LLM 调用
- **C** 零，因为重写器把一切都缓存了
- **D** 一次 LLM 调用（重写器和检索都并行跑，LLM 调用就是下限）

<details>
<summary>查看答案与解析</summary>

**答案**　D

三个重写器都扇出到一次模型调用；如果它们并行跑，下限就是一次模型调用的延迟，之后各路检索再并行执行。

</details>


[返回本课](docs/zh.md)
