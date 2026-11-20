# RAG 评测：Precision、Recall、MRR、nDCG、Faithfulness、Answer Relevance · 自测

每题先选答案，再展开解析。

## 1. 为什么在生产 RAG 里 recall@k 通常是头号 retrieval 指标？

- **A** OpenAPI 规范要求用 recall
- **B** 在 RAG 里 recall 和 precision 是一回事
- **C** 生成阶段可以丢掉无关 chunk，但无法从一个它根本没看到的 chunk 里凭空造出答案，所以漏掉对的 chunk 是代价更高的失败
- **D** recall 忽略排名

<details>
<summary>查看答案与解析</summary>

**答案**　C

一个漏掉正确 chunk 的 retriever 在下游无法修复；多余的 chunk 会浪费 token，但很少会污染答案。

</details>

## 2. MRR 计算的是什么？

- **A** 第二个相关文档排名的中位数
- **B** 各 query 上「第一个相关文档位置的倒数」的均值
- **C** 答案的 token 数
- **D** cosine 相似度的几何平均

<details>
<summary>查看答案与解析</summary>

**答案**　B

MRR 由列表顶端主导：rank 1 贡献 1.0，rank 2 贡献 0.5，rank 10 贡献 0.1。

</details>

## 3. 什么时候应该用 nDCG 而不是 recall@k？

- **A** 当 retriever 不返回分数时
- **B** 当标注（gold label）带有分级相关性（比如文档 A 是 3、文档 B 是 2、文档 C 是 1），而二值指标会丢失信息时
- **C** 永远不用
- **D** 当语料很小时

<details>
<summary>查看答案与解析</summary>

**答案**　B

nDCG 使用分级增益和位置折扣；recall 则把一切压平成二值。

</details>

## 4. faithfulness 和答案相关性（answer relevance）的区别是什么？

- **A** faithfulness 问的是「答案是否扎根于召回的上下文」；答案相关性问的是「答案是否切中了问题」
- **B** faithfulness 是 retrieval 指标，relevance 是 chunker 指标
- **C** faithfulness 衡量 precision，relevance 衡量 recall
- **D** 它们是同一个指标的两个名字

<details>
<summary>查看答案与解析</summary>

**答案**　A

一个忠实但跑题的答案在 faithfulness 上得分高、在 relevance 上得分低；一个切题但无依据的答案在 relevance 上得分高、在 faithfulness 上得分低。

</details>

## 5. 一条 pipeline 的 recall@5 还不错但 MRR 很低，你应该先排查哪个阶段？

- **A** chunker
- **B** generator
- **C** reranker，因为正确的 chunk 在 top-k 里、但没排到最前面
- **D** 语料摄入（ingestor）

<details>
<summary>查看答案与解析</summary>

**答案**　C

recall@5 高说明 gold 在 top-5 里；MRR 低说明它没排到列表顶端。把它排到顶端正是 rerank 阶段的活。

</details>

## 6. 什么样的生产隐患会让一个冻结的 qrels 文件随着时间推移变得危险？

- **A** 评估套件会占满磁盘空间
- **B** retriever 在半年后就会停止工作
- **C** qrels 会腐坏：语料在变，上个季度还是标准答案的文档如今已不再是对的答案；指标却还在拿过期的标注来报
- **D** embedding 向量会过期

<details>
<summary>查看答案与解析</summary>

**答案**　C

排一个每季度的 qrels 复核，否则随着语料演变，你的指标会在衡量错误的东西。

</details>


[返回本课](docs/zh.md)
