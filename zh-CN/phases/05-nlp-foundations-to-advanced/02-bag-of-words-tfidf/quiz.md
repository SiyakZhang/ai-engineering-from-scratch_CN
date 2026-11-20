# 词袋、TF-IDF 与文本表示 · 自测

每题先选答案，再展开解析。

## 1. 词袋模型（Bag of Words）丢弃了什么？

- **A** 文档长度
- **B** token 顺序
- **C** 标点符号
- **D** 词汇表大小

<details>
<summary>查看答案与解析</summary>

**答案**　B

BoW 统计每篇文档中各 token 的出现次数，但丢弃了它们的顺序。

</details>

## 2. 为什么要用 IDF 因子来缩放 TF？

- **A** 为了归一化文档长度
- **B** 为了加速训练
- **C** 为了去除标点符号
- **D** 在每篇文档都出现的词几乎不带区分性信号，应该被降权

<details>
<summary>查看答案与解析</summary>

**答案**　D

IDF 惩罚无处不在的词，提升稀有词的权重。

</details>

## 3. 在平滑的 IDF 公式 log((N+1)/(df+1)) + 1 中，末尾的 +1 保证了什么？

- **A** 计算更快
- **B** 大 N 时的数值稳定性
- **C** 与原始计数兼容
- **D** 在每篇文档都出现的词其 IDF 仍为 1 而不是 0

<details>
<summary>查看答案与解析</summary>

**答案**　D

+1 让无处不在的词保持在 IDF=1，使其不会被归零，这与 scikit-learn 的默认行为一致。

</details>

## 4. 为什么在做余弦相似度之前要对 TF-IDF 行做 L2 归一化？

- **A** 把稀疏向量转换为稠密向量
- **B** 否则较长的文档会主导相似度得分；归一化把所有文档放到单位超球面上
- **C** 移除零项
- **D** 压缩词汇表

<details>
<summary>查看答案与解析</summary>

**答案**　B

L2 归一化消除了文档长度偏差，并把余弦相似度变成了点积。

</details>

## 5. 在做情感分析时，启用 TfidfVectorizer 的哪个设置是有风险的？

- **A** sublinear_tf=True
- **B** min_df=2
- **C** stop_words='english'
- **D** ngram_range=(1, 2)

<details>
<summary>查看答案与解析</summary>

**答案**　C

英语停用词表会去掉像 'not' 这样的否定词，而它们携带着情感信号。

</details>

## 6. 到 2026 年，TF-IDF 在哪类任务上仍然占优？

- **A** 图像描述生成
- **B** 机器翻译
- **C** 垃圾邮件检测、日志异常标记，以及低延迟的窄域分类
- **D** 开放式对话

<details>
<summary>查看答案与解析</summary>

**答案**　C

当信号来自词是否出现、且看重可解释性或速度时，TF-IDF 胜过 embedding。

</details>

## 7. 为什么 TF-IDF 在 'The movie was not good' 与 'The movie was excellent' 这一对句子上会失败？

- **A** embedding 的重叠度太高
- **B** TF-IDF 无法处理停用词
- **C** TF-IDF 需要 bigram 才能工作
- **D** 两篇文档共享了大部分 token；词袋模型没有否定或词序的概念

<details>
<summary>查看答案与解析</summary>

**答案**　D

没有词序或句法上下文，BoW 无法建模 'not' 翻转 'good' 情感这件事。

</details>

## 8. 什么是 TF-IDF 加权 embedding 的混合方法？

- **A** 对 TF-IDF 做 PCA 后再重新 embedding
- **B** 把 BoW 和稠密 embedding 拼接起来
- **C** 在 TF-IDF 特征上训练 BERT
- **D** 在求平均之前，用 TF-IDF 权重作为对各 token embedding 的池化权重

<details>
<summary>查看答案与解析</summary>

**答案**　D

该混合方法用每个 token 的 TF-IDF 分数加权其 embedding 后求平均，把语义能力与稀有词强调结合在一起。

</details>


[返回本课](docs/zh.md)
