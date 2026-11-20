# 词性标注与句法分析 · 自测

每题先选答案，再展开解析。

## 1. 词性标注的目标是什么？

- **A** 检测情感
- **B** 抽取命名实体
- **C** 翻译句子
- **D** 为每个 token 分配一个语法类别（名词、动词等）

<details>
<summary>查看答案与解析</summary>

**答案**　D

词性标注用词性给每个 token 打标签。

</details>

## 2. 跨语言工作的默认标签集是哪个？

- **A** CoNLL-2003
- **B** Universal Dependencies
- **C** Penn Treebank
- **D** Stanford Dependencies

<details>
<summary>查看答案与解析</summary>

**答案**　B

Universal Dependencies 提供一套更粗粒度、与语言无关的 17 个标签的集合。

</details>

## 3. bigram HMM 词性标注器建模的是什么？

- **A** 嵌入相似度
- **B** 依存句法分析
- **C** P(tag | previous tag) 转移加上 P(word | tag) 发射，用 Viterbi 解码
- **D** 仅 P(tags)

<details>
<summary>查看答案与解析</summary>

**答案**　C

bigram HMM 使用标签转移和词发射；Viterbi 找出概率最高的序列。

</details>

## 4. 对于 HMM 标注器，Viterbi 算法计算的是什么？

- **A** 通过在标签格（lattice）上做动态规划，得到唯一一条概率最高的标签序列
- **B** 仅前向概率
- **C** 转移矩阵
- **D** 每个标签的边缘概率

<details>
<summary>查看答案与解析</summary>

**答案**　A

Viterbi 用 O(n * |T|^2) 的动态规划找出 argmax 序列。

</details>

## 5. 依存句法分析产出什么？

- **A** 一个扁平的 BIO 序列
- **B** 一棵带 NP/VP/PP 标签的成分句法树
- **C** 一棵树，其中每个词有一个中心词（head）和一个带标签的语法关系
- **D** 一条共指链

<details>
<summary>查看答案与解析</summary>

**答案**　C

依存句法分析给出逐词的（中心词，关系）边；成分句法分析给出嵌套的短语结构。

</details>

## 6. 为什么 PTB 词性标注的准确率上限在 97-98% 左右？

- **A** Universal Dependencies 封顶在 98%
- **B** 硬件限制
- **C** 模型在任何任务上都无法超过 98%
- **D** 人类标注员只有约 97% 的时候意见一致，所以超过约 98% 的模型可能是在过拟合测试数据

<details>
<summary>查看答案与解析</summary>

**答案**　D

标注员的意见分歧限定了可达到的准确率；非常高的数字往往意味着过拟合。

</details>

## 7. 为什么在 2026 年的 LLM 流水线中词性标注仍然重要？

- **A** 词形还原、基于方面的情感分析、查询分解、结构化输出校验以及跨语言迁移，全都仍在消费词性或依存句法分析结果
- **B** 分词所必需
- **C** 没有它 LLM 就无法运行
- **D** 替代 transformer

<details>
<summary>查看答案与解析</summary>

**答案**　A

即便由 LLM 生成正文，词性和依存句法分析仍为许多结构化的下游任务提供输入。

</details>

## 8. 在大多数生产级词性/句法分析任务中，你应该选用哪个库？

- **A** scikit-learn
- **B** spaCy（追求顶尖准确率或更广语言覆盖时用 stanza/trankit）
- **C** NumPy
- **D** 自己手写一个 parser

<details>
<summary>查看答案与解析</summary>

**答案**　B

spaCy 提供快速的生产级词性 + 依存句法分析器；stanza/trankit 覆盖更广的语言。

</details>


[返回本课](docs/zh.md)
