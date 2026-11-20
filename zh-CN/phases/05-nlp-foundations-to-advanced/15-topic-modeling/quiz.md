# 主题建模 —— LDA 与 BERTopic · 自测

每题先选答案，再展开解析。

## 1. LDA 对每篇文档做了什么假设？

- **A** 文档就是句子
- **B** 每篇文档恰好属于一个主题
- **C** 文档与主题相互独立
- **D** 每篇文档是主题的混合；每个主题是词上的一个分布

<details>
<summary>查看答案与解析</summary>

**答案**　D

LDA 的生成故事是混合成员制：每篇文档有一个主题分布，每个主题有一个词分布。

</details>

## 2. BERTopic 用什么来形成主题聚类？

- **A** 先跑 BM25 再跑 k-means
- **B** 对词汇表直接做 softmax
- **C** 用 sentence transformer 编码文档，用 UMAP 降维，再用 HDBSCAN 聚类
- **D** 端到端训练一个 LSTM

<details>
<summary>查看答案与解析</summary>

**答案**　C

BERTopic = 嵌入 + UMAP + HDBSCAN，并用基于类的 TF-IDF 提取主题词。

</details>

## 3. 为什么 scikit-learn 的 LDA 期望原始计数（CountVectorizer）而非 TF-IDF？

- **A** 内存限制
- **B** TF-IDF 太慢
- **C** LDA 无法处理浮点数
- **D** LDA 的概率模型定义在整数词频计数上；TF-IDF 会扭曲底层分布

<details>
<summary>查看答案与解析</summary>

**答案**　D

LDA 的似然假设是计数；喂入 TF-IDF 值会违反模型假设。

</details>

## 4. 在 BERTopic 输出中，HDBSCAN 的 -1 标签意味着什么？

- **A** 顶层主题
- **B** 停用词簇
- **C** 基于密度的算法无法有信心分配的文档离群簇
- **D** 一个保留类别

<details>
<summary>查看答案与解析</summary>

**答案**　C

HDBSCAN 用 -1 标记未聚类的点；在 BERTopic 中这些是未匹配任何主题的文档。

</details>

## 5. 主题模型评估常用的默认连贯性指标是哪个？

- **A** 仅困惑度
- **B** 通过对顶层主题词的滑动窗口做 NPMI 得到的 c_v 连贯性
- **C** 准确率
- **D** BLEU

<details>
<summary>查看答案与解析</summary>

**答案**　B

c_v 连贯性（Roder 等, 2015）是规范的自动主题连贯性指标。

</details>

## 6. 什么时候 LDA 通常比 BERTopic 更契合？

- **A** 在短推文上
- **B** 当嵌入有噪声时
- **C** 当你需要每篇文档单一主题时
- **D** 长文档，其混合成员制主题分布很有用，而嵌入会截断输入

<details>
<summary>查看答案与解析</summary>

**答案**　D

长文档受益于 LDA 的混合成员制模型；BERT 编码器会截断输入。

</details>

## 7. 为什么 BERTopic 在短文本（推文、标题）上通常占优？

- **A** 它支持更多语言
- **B** 它更快
- **C** 短文本主题更少
- **D** 嵌入空间中的语义相似度能捕捉含义，而词袋计数在此过于稀疏

<details>
<summary>查看答案与解析</summary>

**答案**　D

在词重叠统计失效的短文本上，BERT 嵌入提供了语义相似度。

</details>

## 8. LDA 有一个常见失败模式，你应该监控主题以防范它，它是什么？

- **A** 吸收停用词或极高频词的垃圾主题
- **B** 文档数太少的主题
- **C** 文档混合比例总和为 1
- **D** 与标注类别完美吻合的主题

<details>
<summary>查看答案与解析</summary>

**答案**　A

LDA 可能生成吸收停用词的垃圾主题；收紧 min_df/max_df 和停用词过滤可缓解。

</details>


[返回本课](docs/zh.md)
