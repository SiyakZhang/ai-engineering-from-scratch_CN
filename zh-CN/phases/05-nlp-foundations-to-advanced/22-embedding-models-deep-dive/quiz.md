# 嵌入模型 —— 2026 年深入剖析 · 自测

每题先选答案，再展开解析。

## 1. 什么是稠密嵌入（dense embedding）？

- **A** 每段文本一个固定大小向量，余弦相似度按语义接近度对段落排序
- **B** 一个 token 级对齐矩阵
- **C** 文档之上的一张图
- **D** 每个词汇 token 一个稀疏权重

<details>
<summary>查看答案与解析</summary>

**答案**　A

稠密嵌入给每段文本一个向量（通常 384-3072 维）；余弦对相似度排序。

</details>

## 2. Matryoshka 表示学习能实现什么？

- **A** cross-encoder 重打分
- **B** 多语言训练
- **C** 更快的 softmax
- **D** 把训练好的嵌入截断到前 N 维，仍能得到一个有用的更小嵌入

<details>
<summary>查看答案与解析</summary>

**答案**　D

Matryoshka 训练使向量的前 N 维可独立使用，从而实现低成本截断。

</details>

## 3. 多向量（ColBERT）嵌入如何给 query-doc 对打分？

- **A** 交叉熵
- **B** MaxSim：为每个 query token 找到最相似的 document token，再把这些最大值求和
- **C** 推土机距离（Earth-mover's distance）
- **D** 对均值池化后的 token 向量取余弦

<details>
<summary>查看答案与解析</summary>

**答案**　B

ColBERT 风格的后期交互（late interaction）在逐 token 向量上使用 MaxSim。

</details>

## 4. BGE-M3 同时输出什么？

- **A** 仅一个 colbert 向量
- **B** 仅一个稠密向量
- **C** 在单次推理中由一个模型同时输出稠密、稀疏和多向量（colbert）表示
- **D** 仅一个稀疏向量

<details>
<summary>查看答案与解析</summary>

**答案**　C

BGE-M3 由一个模型发出三种检索模式，对融合式混合打分很有用。

</details>

## 5. 为什么在做余弦相似度之前，必须对 Matryoshka 截断后的向量重新归一化？

- **A** 截断改变了向量范数；不重新归一化的话，点积就不再等于余弦
- **B** 余弦忽略归一化
- **C** 仅 FAISS 所要求
- **D** 截断会破坏训练

<details>
<summary>查看答案与解析</summary>

**答案**　A

截断后重新归一化恢复单位范数，使点积重新等于余弦。

</details>

## 6. 为什么 BGE 模型常常需要在 query 侧加一个前缀字符串？

- **A** FAISS 所要求
- **B** 前缀改变 tokenizer 行为
- **C** 为了压缩查询
- **D** BGE 是带显式 query prompt 训练的；省略它会损失 3-5 个点的召回率

<details>
<summary>查看答案与解析</summary>

**答案**　D

BGE 模型期望在 query 上加一个 'Represent this sentence for searching...' 前缀。

</details>

## 7. 为什么 MTEB 对挑选嵌入模型而言是必要的但不充分？

- **A** MTEB 偏袒更大的模型
- **B** MTEB 只覆盖英语
- **C** MTEB 忽略延迟
- **D** 排行榜名次是众多任务的平均；你的具体领域可能不同，所以始终要在自己的数据上做基准测试

<details>
<summary>查看答案与解析</summary>

**答案**　D

MTEB 跨任务求平均；领域特定的评估可能颠覆这个排名。

</details>

## 8. 什么时候应该在稠密嵌入之外加上 SPLADE 稀疏检索？

- **A** 当查询关键词密集，或包含稠密嵌入会模糊掉的标识符/代码时
- **B** 仅在小语料上
- **C** 只要编码器是多语言的
- **D** 只要使用了 Matryoshka

<details>
<summary>查看答案与解析</summary>

**答案**　A

SPLADE 捕捉稠密模型可能漏掉的词面/关键词匹配；通过 RRF 与稠密融合。

</details>


[返回本课](docs/zh.md)
