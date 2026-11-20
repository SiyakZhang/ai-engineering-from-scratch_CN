# 文本摘要 · 自测

每题先选答案，再展开解析。

## 1. 抽取式与生成式摘要在行为上的关键区别是什么？

- **A** 抽取式用 TF-IDF；生成式用 Word2Vec
- **B** 抽取式只能多语言
- **C** 抽取式比生成式慢
- **D** 抽取式从源文逐字返回句子；生成式生成新文本并可能产生幻觉

<details>
<summary>查看答案与解析</summary>

**答案**　D

抽取式逐字摘取句子；生成式则重写，并有幻觉风险。

</details>

## 2. ROUGE 衡量什么？

- **A** token 级困惑度
- **B** 系统摘要与参考摘要之间的 n-gram 及最长公共子序列重叠
- **C** 阅读时长
- **D** 嵌入相似度

<details>
<summary>查看答案与解析</summary>

**答案**　B

ROUGE-1/2/L 衡量与参考摘要的 unigram、bigram 和 LCS 重叠。

</details>

## 3. 在抽取式摘要中，TextRank 如何给句子打分？

- **A** 通过与参考摘要比较
- **B** 按原始词数
- **C** 通过与问题的嵌入余弦
- **D** 在以句子相似度为边权的图上运行 PageRank 风格的迭代

<details>
<summary>查看答案与解析</summary>

**答案**　D

TextRank 在句子相似度图上使用 PageRank；连接度高的句子得分最高。

</details>

## 4. 为什么在计算 ROUGE 时启用词干提取？

- **A** 词干提取规范化大小写
- **B** rouge-score 包要求做词干提取
- **C** 不做词干提取，'running' 和 'run' 会被算作不同 token，ROUGE 会低估真实重叠
- **D** 为了加速 ROUGE

<details>
<summary>查看答案与解析</summary>

**答案**　C

词干提取合并形态变体，让 ROUGE 给予语义等价形式以信用。

</details>

## 5. 2026 年哪个指标专门通过 NLI 蕴含来检测摘要幻觉？

- **A** BLEU
- **B** ROUGE-L
- **C** 忠实度检查（例如 FactCC 或 RAGAS faithfulness），用 NLI 比较源文与摘要论断
- **D** chrF

<details>
<summary>查看答案与解析</summary>

**答案**　C

基于 NLI 的忠实度评分会标记出摘要中不被源文蕴含的论断。

</details>

## 6. 为什么对涉及合规的内容更偏好抽取式摘要？

- **A** 它更快
- **B** ROUGE 分数更高
- **C** 输出逐字摘自源文，消除了生成式那一类幻觉
- **D** 抽取式支持更长的输出

<details>
<summary>查看答案与解析</summary>

**答案**　C

逐字抽取无法捏造内容，这在事实性受监管的场景中很重要。

</details>

## 7. 以下哪个是需要监控的生成式幻觉类型？

- **A** 标点漂移
- **B** 长句子
- **C** 停用词去除
- **D** 实体调换（例如把 'John Smith' 写成 'John Brown'）、数字漂移、极性翻转或捏造事实

<details>
<summary>查看答案与解析</summary>

**答案**　D

实体调换、数字漂移、极性翻转和捏造事实是生成式摘要的典型失败模式。

</details>

## 8. 什么时候你会选用 Pegasus 检查点而非 BART-large-CNN？

- **A** 评估 BLEU 时
- **B** 在像科学论文摘要这样的领域，Pegasus 的 gap-sentence 预训练目标更契合
- **C** 需要抽取式输出时
- **D** 输入很短时

<details>
<summary>查看答案与解析</summary>

**答案**　B

Pegasus 的 gap-sentence 目标在长篇领域摘要（例如 pubmed）上表现出色。

</details>


[返回本课](docs/zh.md)
