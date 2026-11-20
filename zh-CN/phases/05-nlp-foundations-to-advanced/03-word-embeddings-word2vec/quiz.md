# 词嵌入 —— 从零实现 Word2Vec · 自测

每题先选答案，再展开解析。

## 1. 什么是分布假设（distributional hypothesis）？

- **A** 高频词携带最多的含义
- **B** 所有词都能嵌入到 300 维中
- **C** 观其伴而知其义（通过一个词的伴随上下文来了解它）
- **D** 词在各文档中均匀分布

<details>
<summary>查看答案与解析</summary>

**答案**　C

Firth（1957）的分布假设：相似的上下文意味着相似的含义。

</details>

## 2. 为什么在 Word2Vec 中对整个词汇表做普通 softmax 不切实际？

- **A** 在每个训练步对 10 万以上的词汇项计算 softmax 代价高得无法承受
- **B** softmax 无法建模概率
- **C** softmax 没有梯度
- **D** 它会导致梯度消失

<details>
<summary>查看答案与解析</summary>

**答案**　A

全词汇表 softmax 代价太高；负采样把它重新表述为二分类问题。

</details>

## 3. skip-gram 和 CBOW 有什么区别？

- **A** skip-gram 由中心词预测上下文词；CBOW 由上下文预测中心词
- **B** skip-gram 用 bigram；CBOW 用 unigram
- **C** skip-gram 由上下文预测中心词；CBOW 则相反
- **D** skip-gram 训练深层网络；CBOW 是浅层的

<details>
<summary>查看答案与解析</summary>

**答案**　A

skip-gram：中心词 -> 上下文。CBOW：上下文 -> 中心词。

</details>

## 4. 在负采样中，对正样本对（中心词，上下文）的目标是什么？

- **A** 强制它们正交
- **B** 去相关这些向量
- **C** 最小化它们的点积
- **D** 最大化 sigmoid(W[center] dot W'[context])，使其接近 1

<details>
<summary>查看答案与解析</summary>

**答案**　D

正样本对训练 sigmoid 接近 1；采样的负样本训练 sigmoid 接近 0。

</details>

## 5. 训练完 Word2Vec 后，哪个权重矩阵成为词嵌入？

- **A** 输入到隐藏层的 W 矩阵（中心词查找表）
- **B** 一个独立的训练后投影
- **C** 隐藏层到输出的 W' 矩阵
- **D** 两者相乘

<details>
<summary>查看答案与解析</summary>

**答案**　A

中心词查找表 W 是标准的嵌入输出；W' 通常被丢弃或被平均进去。

</details>

## 6. 为什么 Word2Vec 在一词多义（例如 'bank'）上会失败？

- **A** 窗口大小太小
- **B** 它忽略稀有词
- **C** 负采样丢掉了稀有含义
- **D** 它给每个词分配一个静态向量，所以 'river bank'（河岸）和 'financial bank'（银行）共享同一个向量

<details>
<summary>查看答案与解析</summary>

**答案**　D

静态嵌入无法消歧词义；上下文嵌入（ELMo/BERT）解决了这个问题。

</details>

## 7. 在 2026 年，什么情况下你仍会选用 Word2Vec 而非 transformer？

- **A** 当对话质量重要时
- **B** 当输入非常长时
- **C** 当你需要上下文消歧时
- **D** 轻量、设备端、领域特定的检索，其中单行查找就是全部的延迟预算

<details>
<summary>查看答案与解析</summary>

**答案**　D

在极小的延迟预算、设备端推理或快速领域特定训练上，Word2Vec 占优。

</details>

## 8. 是什么让著名的类比 'king - man + woman ~ queen' 成为可能？

- **A** 余弦相似度对性别不变
- **B** 向量算术捕捉到了像“皇室”这样可跨性别迁移的线性方向
- **C** skip-gram 在皇室词汇上训练
- **D** 模型把“皇室”编码为一个标志位

<details>
<summary>查看答案与解析</summary>

**答案**　B

嵌入空间中的方向编码了关系特征，因此加减会带来系统性的位移。

</details>


[返回本课](docs/zh.md)
