# 自然语言推理 —— 文本蕴含 · 自测

每题先选答案，再展开解析。

## 1. NLI 给（前提，假设）这一对分配哪三个标签？

- **A** 真 / 假 / 未知
- **B** 正面 / 负面 / 中性
- **C** 原因 / 结果 / 无关
- **D** 蕴含 / 矛盾 / 中性

<details>
<summary>查看答案与解析</summary>

**答案**　D

NLI 是在蕴含、矛盾和中性上的三分类。

</details>

## 2. NLI 如何被用作零样本文本分类器？

- **A** 通过对嵌入求平均
- **B** 通过给 LLM 发 prompt
- **C** 通过计算 TF-IDF
- **D** 把每个候选标签表述为一个假设（例如 'This text is about sports'），并挑选蕴含分数最高的标签

<details>
<summary>查看答案与解析</summary>

**答案**　D

NLI 作为分类器把标签变成假设；模型挑选蕴含度最高的标签。

</details>

## 3. 为什么 NLI 是对 RAG 输出的忠实度检查？

- **A** 它很廉价
- **B** 它是多语言的
- **C** 它使用 tokenizer
- **D** 检查检索到的上下文是否蕴含每条答案论断，正是 NLI 受训的那种表述形式

<details>
<summary>查看答案与解析</summary>

**答案**　D

幻觉 = 答案论断不被检索上下文蕴含；NLI 直接度量蕴含。

</details>

## 4. 仅用假设（hypothesis-only）的基线揭示了什么？

- **A** tokenizer 漂移
- **B** 在某些数据集上，仅凭假设（不看前提）就能预测标签，这预示着标签泄露
- **C** 推理慢
- **D** 多语言差距

<details>
<summary>查看答案与解析</summary>

**答案**　B

在 SNLI 上仅用假设就得高分，暴露了标注伪影；这对调试你的数据很有用。

</details>

## 5. 哪个 NLI 模型家族作为标准主力登顶 2026 年的排行榜？

- **A** fastText
- **B** GPT-2
- **C** 普通 Word2Vec
- **D** 在 MNLI/FEVER/ANLI 上微调的 DeBERTa-v3 变体

<details>
<summary>查看答案与解析</summary>

**答案**　D

在 MNLI 及相关语料上微调的 DeBERTa-v3 是 2026 年开源 NLI 的主力。

</details>

## 6. 为什么句子级 NLI 模型在文档长度的前提上准确率会下降？

- **A** 余弦相似度衰减
- **B** 它们在短前提上训练，在多句和多跳推理上失败；用 DocNLI 调过的模型能处理更长输入
- **C** 更大的输入跑得更慢
- **D** 文档触发 tokenizer 漂移

<details>
<summary>查看答案与解析</summary>

**答案**　B

训练分布不匹配：单句 NLI 模型在文档长度输入上会损失 20+ F1。

</details>

## 7. 为什么零样本准确率会因假设模板不同而摆动 10 个点以上？

- **A** 模板影响模型权重
- **B** 模型对措辞敏感；例如 'This text is about {label}' 与单独的 '{label}' 会改变蕴含概率
- **C** 模板改变 tokenizer 行为
- **D** 模板改变标签集

<details>
<summary>查看答案与解析</summary>

**答案**　B

模板措辞会实质性地改变蕴含分数；在一个小的留出集上调它。

</details>

## 8. 关于把 NLI 用于幻觉检测，一个稳妥的论断界限是什么？

- **A** 它消除了幻觉
- **B** 它作为忠实度信号能减少幻觉，但不能消除幻觉；要与检索召回率和人工审核结合
- **C** 它只对英语有效
- **D** 它需要 LLM

<details>
<summary>查看答案与解析</summary>

**答案**　B

NLI 是有用信号但非完整方案；搭配检索指标和人工抽查。

</details>


[返回本课](docs/zh.md)
