# transformer 之前的文本生成 —— N-gram 语言模型 · 自测

每题先选答案，再展开解析。

## 1. n-gram 语言模型估计的是什么？

- **A** 词之间的编辑距离
- **B** P(label | document)
- **C** 由计数统计得到的 P(next word | previous n-1 words)
- **D** 文档嵌入

<details>
<summary>查看答案与解析</summary>

**答案**　C

n-gram LM 通过计数出现次数来建模 P(w | last n-1 words)。

</details>

## 2. 平滑（smoothing）在 n-gram 模型中解决什么问题？

- **A** 数值精度
- **B** 内存占用
- **C** 分词不匹配
- **D** 对训练中未见过的 n-gram 赋予零概率，从而把句子似然坍缩为零

<details>
<summary>查看答案与解析</summary>

**答案**　D

平滑重新分配概率质量，使未见过的 n-gram 得到非零概率。

</details>

## 3. 什么洞见让 Kneser-Ney 平滑比朴素的绝对折扣更好？

- **A** 它使用更大的 n
- **B** 它使用梯度下降
- **C** 它用延续概率（一个词出现在多少个不同上下文中）而非原始频率来估计低阶分布
- **D** 它使用 TF-IDF

<details>
<summary>查看答案与解析</summary>

**答案**　C

延续概率奖励上下文多样性，而不仅仅是原始计数。

</details>

## 4. 困惑度（perplexity）衡量什么？

- **A** 留出测试集上每个 token 平均负对数似然的 exp；越低越好
- **B** 标签的交叉熵
- **C** 不同 n-gram 的数量
- **D** 生成的吞吐量

<details>
<summary>查看答案与解析</summary>

**答案**　A

困惑度 = exp(- mean log P)；越低表示模型对测试文本越不感到意外。

</details>

## 5. 为什么在比较困惑度数字时，训练集和测试集必须使用完全相同的分词？

- **A** 困惑度取决于分词方案；不匹配的 tokenizer 会产生不可比的分数
- **B** 为了避免 OOV
- **C** 梯度下降所要求
- **D** 为了控制 batch size

<details>
<summary>查看答案与解析</summary>

**答案**　A

不同的分词会改变 token 数量和似然，使困惑度值不可比。

</details>

## 6. 为什么 trigram-LM 生成的句子局部通顺却整体不连贯？

- **A** beam search 失败
- **B** 它们使用拉普拉斯平滑
- **C** 它们丢掉了标点
- **D** 局部 trigram 上下文引导每个下一个词，但模型在 n-1 个 token 之外没有长程记忆

<details>
<summary>查看答案与解析</summary>

**答案**　D

仅以最后 n-1 个 token 为条件，使得长程连贯只是偶然出现。

</details>

## 7. 在 2026 年，n-gram 模型仍在哪类生产中部署？

- **A** 多语言翻译
- **B** 摘要
- **C** 开放域聊天机器人
- **D** 延迟敏感的路径，如语音识别重打分和设备端自动补全（通过 KenLM 等库）

<details>
<summary>查看答案与解析</summary>

**答案**　D

KenLM 风格的 n-gram 模型仍作为快速的设备端或重打分组件服役。

</details>

## 8. 为什么在宣称一个神经 LM “好”之前，仍建议先计算一个 n-gram 基线？

- **A** 它消除 OOV
- **B** ROUGE 所要求
- **C** 它加速训练
- **D** 如果一个 transformer LM 在相同分词下没有大幅领先于一个调好的 Kneser-Ney 基线，那训练流水线就有问题

<details>
<summary>查看答案与解析</summary>

**答案**　D

KN 基线意外地强；神经 LM 应大幅领先，否则就是有 bug。

</details>


[返回本课](docs/zh.md)
