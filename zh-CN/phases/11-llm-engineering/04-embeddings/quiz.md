# 嵌入（embedding）与向量表示 · 自测

每题先选答案，再展开解析。

## 1. embedding 解决了关键词搜索无法解决的什么问题？

- **A** embedding 更快
- **B** embedding 可以离线工作
- **C** embedding 占用更少存储
- **D** embedding 捕捉语义含义，即使「付款没成功」和「扣款被拒绝」没有共同的词也能匹配上

<details>
<summary>查看答案与解析</summary>

**答案**　D

关键词搜索把词当作独立符号。embedding 把文本映射到高维向量，语义相似度即几何邻近度。含义相同的文本会聚在一起，无论选词如何。

</details>

## 2. 余弦相似度（cosine similarity）衡量两个 embedding 向量之间的什么？

- **A** 向量之间的夹角，表示它们的方向有多相似，与大小无关
- **B** 它们各分量之和
- **C** 欧氏距离
- **D** 匹配维度的数量

<details>
<summary>查看答案与解析</summary>

**答案**　A

余弦相似度 = dot(A,B) / (|A|*|B|)。它的取值范围从 -1（方向相反）到 1（方向相同）。含义相同的两段文本，向量方向几乎一致，余弦相似度接近 1。

</details>

## 3. 现代文本 embedding 模型的典型维度是多少？

- **A** 2-10 维
- **B** 10 万以上维
- **C** 768-3072 维
- **D** 50-100 维

<details>
<summary>查看答案与解析</summary>

**答案**　C

现代 embedding 模型（OpenAI text-embedding-3、BGE、E5）产生 768 到 3072 维的向量。维度越高捕捉的细微差别越多，但存储和搜索的成本也更高。

</details>

## 4. 为什么应该用检索基准来评估 embedding 质量，而不只是查看相似度分数？

- **A** 相似度的绝对值因模型而异；重要的是相关文档是否排在不相关文档之前（precision@k、recall）
- **B** 检索基准更快
- **C** 相似度分数总是错的
- **D** 相似度分数不使用余弦距离

<details>
<summary>查看答案与解析</summary>

**答案**　A

0.85 的余弦相似度，对一个模型可能意味着「非常相似」，对另一个模型可能只是「有些相似」。检索指标（precision@k、recall）衡量真正重要的东西：正确的文档有没有被找回来？

</details>

## 5. 什么时候你会使用本地/开源 embedding 模型，而不是基于 API 的模型？

- **A** 本地模型产生更高质量的 embedding
- **B** 本地模型总是更好
- **C** 当你需要数据隐私、离线运行、大规模下更低的成本，或针对特定领域微调时
- **D** API 模型不支持批处理

<details>
<summary>查看答案与解析</summary>

**答案**　C

API embedding（OpenAI、Cohere）使用方便，但会把你的数据发到外部。本地模型（BGE、E5、Nomic）让数据保密，大规模下消除按次调用成本，并可在特定领域数据上微调。

</details>


[返回本课](docs/zh.md)
