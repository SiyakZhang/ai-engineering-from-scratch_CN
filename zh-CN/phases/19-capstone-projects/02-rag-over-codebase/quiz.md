# 顶点项目 02 —— 代码库之上的 RAG（跨仓库语义搜索） · 自测

每题先选答案，再展开解析。

## 1. 为什么对原始 chunk 做朴素的余弦搜索不足以胜任跨仓库代码检索？

- **A** 向量索引无法存储超过 1KB 的载荷
- **B** 嵌入模型看不到代码作为 token
- **C** 它会因生成代码、monorepo 重复和很少被导入的符号而污染结果
- **D** 余弦相似度在代码嵌入上没有定义

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 2. 在摄入流水线中，AST 感知的分块（AST-aware chunking）是什么意思？

- **A** 在存储前用 gzip 压缩 chunk
- **B** 在嵌入前丢弃注释和空白
- **C** 把代码切成固定的 256-token 窗口
- **D** 在 tree-sitter 节点边界处切分，例如函数和类的范围

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 3. 在这条流水线中，每个 chunk 获得哪三种可检索模态？

- **A** 稠密嵌入、BM25 词项和一段自然语言摘要
- **B** AST、IR 和字节码
- **C** Token ID、语法树和调用图
- **D** 原始文本、gzip 和哈希

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 4. 在混合检索步骤之后，cross-encoder 重排器的作用是什么？

- **A** 它在发送给综合器之前压缩 chunk
- **B** 它把每个「查询-候选」对放在一起打分，从而获得比仅用余弦更高的准确率
- **C** 它重写 chunk 以移除生成代码
- **D** 它用不同的模型重新嵌入查询

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 5. 为什么综合器会拒绝没有 (repo/path:start-end) 锚点的答案？

- **A** 引用忠实性（citation faithfulness）对答案设了门禁，使用户可以核验每一条论断
- **B** 锚点能降低综合调用的 token 成本
- **C** 锚点是下游 BM25 重排所需要的
- **D** 锚点是向量数据库 schema 所要求的

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 6. 为了在 50 个文件的推送上把增量重建索引控制在 60 秒以内，需要什么？

- **A** 在每次提交时重新嵌入完整的 200 万行代码语料
- **B** 丢掉 BM25 索引并从头重建
- **C** 完全丢弃符号图
- **D** 只重新嵌入文本发生变化的 chunk，并重算受影响的符号边

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 7. 哪个指标衡量检索到的论断是否可在源代码中得到验证？

- **A** 引用忠实性（citation faithfulness）
- **B** p95 查询延迟
- **C** MRR@10
- **D** nDCG@10

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>


[返回本课](docs/zh.md)
