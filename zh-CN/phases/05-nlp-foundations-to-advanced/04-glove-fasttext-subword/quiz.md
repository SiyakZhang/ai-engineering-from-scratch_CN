# GloVe、FastText 与子词嵌入 · 自测

每题先选答案，再展开解析。

## 1. 相比 Word2Vec，GloVe 贡献了什么？

- **A** 子词 n-gram 嵌入
- **B** 字节级分词
- **C** 更深的神经网络
- **D** 用带权重的损失直接分解词-词共现矩阵

<details>
<summary>查看答案与解析</summary>

**答案**　D

GloVe 用经过精心加权的对数损失来分解全局共现矩阵。

</details>

## 2. FastText 解决了 Word2Vec 和 GloVe 没有解决的什么问题？

- **A** 多语言迁移
- **B** 通过组合字符 n-gram 来为未见过的词生成向量
- **C** 一词多义消歧
- **D** 降低训练成本

<details>
<summary>查看答案与解析</summary>

**答案**　B

FastText 从一个词的子词 n-gram 组合出词向量，因此 OOV（未登录）词仍能得到一个合理的向量。

</details>

## 3. 在 GloVe 中，加权函数 f(x) = (x/x_max)^alpha 起什么作用？

- **A** 把向量归一化为单位长度
- **B** 选择负样本
- **C** 对极高频的词对降权，使其不会主导损失
- **D** 随机初始化权重

<details>
<summary>查看答案与解析</summary>

**答案**　C

加权防止像 (the, and) 这样无处不在的共现主导训练。

</details>

## 4. BPE 的合并步骤如何挑选接下来要合并的词对？

- **A** IDF 最高的词对
- **B** 按字典序排在最前面的词对
- **C** 全语料中频率最高的相邻 token 对
- **D** 一个随机的词对

<details>
<summary>查看答案与解析</summary>

**答案**　C

BPE 迭代地合并频率最高的相邻词对。

</details>

## 5. 为什么 GPT-2 使用字节级 BPE？

- **A** 字节隐式保留大小写
- **B** 字节比字符训练更快
- **C** 字节 BPE 跳过了合并训练
- **D** 256 个字节的基础词汇表覆盖任意输入，彻底消除了未登录词

<details>
<summary>查看答案与解析</summary>

**答案**　D

从 256 个字节出发意味着任何 UTF-8 字符串都能被分词；不存在 OOV。

</details>

## 6. 在微调预训练 transformer 时，你应该用哪个 tokenizer？

- **A** 与模型一同发布的那个确切 tokenizer；不匹配会破坏嵌入
- **B** 永远用字节级 BPE
- **C** 永远用 SentencePiece
- **D** 词汇表最大的那个

<details>
<summary>查看答案与解析</summary>

**答案**　A

tokenizer 与模型不匹配会悄悄损坏输入；始终把配套发布的 tokenizer 与其模型搭配使用。

</details>

## 7. 什么情况下你会在预训练词向量上选 FastText 而非 GloVe？

- **A** 当你需要一个 50 维模型时
- **B** 对于形态丰富的语言，或频繁出现新造词和拼写错误的领域
- **C** 当延迟要求最严苛时
- **D** 当语料非常小时

<details>
<summary>查看答案与解析</summary>

**答案**　B

FastText 的子词组合能处理 GloVe 无法处理的屈折变化、新造词和拼写错误。

</details>

## 8. WordPiece、BPE 和 SentencePiece 的词汇表以什么单元为基础？

- **A** 句子
- **B** 整词
- **C** 段落
- **D** 低于词级别的子词片段（字符、n-gram，或学到的合并）

<details>
<summary>查看答案与解析</summary>

**答案**　D

这三者都是子词 tokenizer；它们的区别在于如何学习合并或片段，而非是否为子词。

</details>


[返回本课](docs/zh.md)
