# 用 BM25 与 Dense Embedding 做 Hybrid Retrieval · 自测

每题先选答案，再展开解析。

## 1. 为什么生产环境的 RAG 端点需要同时用上 lexical 和 semantic retrieval？

- **A** semantic retrieval 永远更准
- **B** query 分布里既有字面标识符查询又有改写过的查询；每一类各有一种模态会失手
- **C** 这样能把索引体积砍掉一半
- **D** 合规上法律强制要求做 lexical 检索

<details>
<summary>查看答案与解析</summary>

**答案**　B

BM25 在字面符号上占优，dense 在改写表述上占优。真实端点会从同一批用户那里同时收到这两类 query。

</details>

## 2. BM25 里默认取 0.75 的参数 b 是什么含义？

- **A** 对 IDF 项的一个乘数
- **B** 一个长度归一化的旋钮：较长的文档会被惩罚，但不是线性的
- **C** query 时作用在 cosine 相似度上的指数
- **D** 文档里的字段数量

<details>
<summary>查看答案与解析</summary>

**答案**　B

b 在不做长度归一化（0）和完全归一化（1）之间插值；0.75 是公开推荐的取值。

</details>

## 3. Reciprocal Rank Fusion（RRF）对每个候选计算的是什么？

- **A** 在每个包含该候选的排序列表上，对 1 / (k + rank) 求和
- **B** 各模态排名的中位数
- **C** 各模态 cosine 相似度的乘积
- **D** 对 BM25 和 dense 分数做 min-max 归一化后取平均

<details>
<summary>查看答案与解析</summary>

**答案**　A

RRF 把每个排序列表里的 1 / (k + rank) 贡献加起来；k = 60 是公开的默认值。

</details>

## 4. 为什么基于排名的融合比对 BM25 和 cosine 分数做线性插值更受青睐？

- **A** cosine 分数是无界的
- **B** 线性插值需要 GPU 支持
- **C** BM25 分数无法排序
- **D** BM25 分数无界且依赖语料，cosine 被限制在 -1 到 1 之间；两者的分数尺度在不同语料间不可比

<details>
<summary>查看答案与解析</summary>

**答案**　D

分数插值会在每次重建索引时失效，因为分数分布会漂移；而排名按构造方式在各模态间天然可比。

</details>

## 5. 当你把 RRF 的常数 k 取得非常小时会发生什么？

- **A** 融合等价于线性分数求和
- **B** 语料外的词会得到一个正分
- **C** top-1 的贡献会主导整个融合；靠后的排名几乎没有贡献
- **D** 融合会忽略第二种模态

<details>
<summary>查看答案与解析</summary>

**答案**　C

k 取小会把贡献集中到 rank-1 上；k 取大则会把贡献曲线压平，让靠后的候选也能投票。

</details>

## 6. 通过重复 token 来做字段加权，专门规避了哪种失效模式？

- **A** 在 query 时再加一步分数聚合；这样数学形式保持不变，也就不需要按字段分数组合的逻辑
- **B** cosine 相似度变成负数
- **C** 词表外（OOV）的 embedding
- **D** BM25 的 IDF 坍缩为零

<details>
<summary>查看答案与解析</summary>

**答案**　A

在建索引时重复 token 会成倍提高词频，从而让 BM25 的打分数学保持一个求和式，而不必再引入一个独立的字段分数组合器。

</details>


[返回本课](docs/zh.md)
