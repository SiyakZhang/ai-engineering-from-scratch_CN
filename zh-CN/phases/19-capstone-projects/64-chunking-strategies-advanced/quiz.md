# Chunking 策略横向对比 · 自测

每题先选答案，再展开解析。

## 1. 为什么 chunking 的选择是 retrieval 质量的上限，而不只是一个普通的超参数？

- **A** 因为 BM25 在现代 RAG 里没有任何作用
- **B** 因为 LLM 从来不读 chunk
- **C** 因为一旦答案片段被切成不连贯的碎片，下游的 embedding、reranker 或 LLM 都没法把它恢复回来
- **D** 因为 embedding 模型在训练时就固定了

<details>
<summary>查看答案与解析</summary>

**答案**　C

如果承载答案片段的 chunk 不连贯，它的 embedding 就会落到错误的聚类里，而下游组件无法修复这个损伤。

</details>

## 2. 在你对语料一无所知时，哪种单一策略是最强的默认选择？

- **A** 句子打包（sentence packer）
- **B** 结构化 markdown 切分
- **C** 递归切分（recursive split）
- **D** 固定窗口（fixed-window）

<details>
<summary>查看答案与解析</summary>

**答案**　C

递归切分会先尝试最强的分隔符，再逐级回退，从而按区域自适应，因此即便结构不一致也能扛得住。

</details>

## 3. 本课里 recall@k 衡量的是什么？

- **A** top-k 的 chunk 里是否有任意一个与标准答案片段（gold span）重叠
- **B** query 与 top-k chunk 之间的 cosine 相似度
- **C** top-k 里有多少个不同的文档
- **D** top-k 的 chunk 里是否包含 query 的原文字符串

<details>
<summary>查看答案与解析</summary>

**答案**　A

每个 query 都带有标准答案的偏移区间；只要 top-k 中任意一个 chunk 与 gold span 重叠，recall@k 就记为 1，否则为 0，再对所有 query 求平均。

</details>

## 4. 为什么固定窗口 chunking 在代码或 YAML 语料上表现极差？

- **A** 它无法并行化
- **B** 它产出的 chunk 比 embedding 模型的上下文窗口还大
- **C** 它会丢失 Unicode 字符
- **D** 它会把标识符和键值对从中间切断，产出的 chunk 只能 embed 成噪声

<details>
<summary>查看答案与解析</summary>

**答案**　D

在一个符号内部按字符切断，会摧毁 embedding 模型本该捕捉的语义。

</details>

## 5. 语义 chunking 里的质心漂移（centroid drift）终止条件是什么？

- **A** chunker 已经用尽了 embedding 预算
- **B** 当前累计均值向量与下一句之间的 cosine 相似度跌破阈值
- **C** 字符数超过上限
- **D** 句子数超过一个硬编码的上限

<details>
<summary>查看答案与解析</summary>

**答案**　B

语义 chunking 在累计质心按设定的相似度阈值不再匹配下一句时切分。

</details>

## 6. 语义 chunking 引入了哪种另外四种策略都不会有的 embedding 失效模式？

- **A** 只要你换掉用于切分的模型，chunk 边界就会变，必须做一次协调一致的重建
- **B** chunk 丢失了起止偏移
- **C** chunk 太小，装不进 embedding 的上下文
- **D** chunk 不再能被 BM25 索引

<details>
<summary>查看答案与解析</summary>

**答案**　A

语义聚类依赖某个 embedding 模型；换模型就会改变边界，因此切分用的模型必须单独锁定，或者与 retrieval 模型一起重建。

</details>


[返回本课](docs/zh.md)
