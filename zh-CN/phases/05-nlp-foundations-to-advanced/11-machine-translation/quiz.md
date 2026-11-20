# 机器翻译 · 自测

每题先选答案，再展开解析。

## 1. BLEU 衡量的是什么？

- **A** 嵌入余弦相似度
- **B** 语言识别准确率
- **C** 假设译文与参考译文之间的 n-gram 精确率（通常 1-4），并带一个简短惩罚（brevity penalty）
- **D** 字符级 F 分数

<details>
<summary>查看答案与解析</summary>

**答案**　C

BLEU 是对参考译文的 1-4 gram 精确率的几何平均，再加上简短惩罚。

</details>

## 2. 为什么用 sacrebleu 而不是自己手写 BLEU？

- **A** 它支持流式处理
- **B** 它在 GPU 上运行
- **C** 它规范化了分词，使得分数在不同论文和不同运行之间可比
- **D** 它更准确

<details>
<summary>查看答案与解析</summary>

**答案**　C

sacrebleu 固定了分词方式，消除了 BLEU 数字不可比的一个常见来源。

</details>

## 3. NLLB 中哪个特定设置在解码时控制目标语言？

- **A** forced_bos_token_id 设为目标语言代码对应的 token id
- **B** num_beams
- **C** length_penalty
- **D** src_lang

<details>
<summary>查看答案与解析</summary>

**答案**　A

NLLB 通过 forced_bos_token_id 把第一个解码 token 强制为目标语言代码。

</details>

## 4. 在有标注数据的场景下，2026 年生产级 MT 质量评估的默认指标家族是哪个？

- **A** 仅 BLEU
- **B** 在人类判断上训练的学习型指标，如 COMET（以及 BERTScore/BLEURT）
- **C** token 编辑距离
- **D** 延迟

<details>
<summary>查看答案与解析</summary>

**答案**　B

像 COMET 这样的学习型指标，比单独使用 BLEU/chrF 与人类判断的相关性更强。

</details>

## 5. 什么时候 chrF 往往比 BLEU 更具信息量？

- **A** 在非常短的句子上
- **B** 使用 beam search 时
- **C** 只要存在参考译文
- **D** 对于形态丰富的语言，字符级匹配能捕捉到 BLEU 漏掉的屈折变体

<details>
<summary>查看答案与解析</summary>

**答案**　D

字符 F 分数能捕捉词级 BLEU 计算不足的部分形态匹配。

</details>

## 6. 多语言 MT 中的偏离目标语言生成（off-target generation）是什么？

- **A** 丢掉命名实体的输出
- **B** 漏掉标点的输出
- **C** 太短的输出
- **D** 模型解码成了错误的目标语言（例如请求法语时 NLLB 输出了西班牙语）

<details>
<summary>查看答案与解析</summary>

**答案**　D

偏离目标语言生成在稀有语言对上很常见；翻译后做一次语言识别检查可以发现它。

</details>

## 7. 为什么在几千条高质量领域语言对上微调，常常胜过规模大得多的嘈杂网络数据？

- **A** 质量和领域匹配胜过数据量；嘈杂的平行数据会引入漂移和幻觉
- **B** 网络数据使用起来不合法
- **C** 更小的数据集训练更快
- **D** 更大的数据会撑爆 GPU 内存

<details>
<summary>查看答案与解析</summary>

**答案**　A

干净的、领域对齐的语言对是生产中最大的杠杆；嘈杂数据会降低适配效果。

</details>

## 8. 在 2026 年，什么情况下 LLM（例如 GPT-4）可能胜过专用 MT 模型？

- **A** 延迟敏感的浏览器翻译
- **B** 习语内容、长上下文、通过 prompt 做风格适配，或需要语气控制的内容
- **C** 最高吞吐量的批量翻译
- **D** 拥有数百万平行句子的小语种语言对

<details>
<summary>查看答案与解析</summary>

**答案**　B

LLM 在习语、长上下文或风格可控的翻译上占优；专用 MT 在吞吐量和延迟上占优。

</details>


[返回本课](docs/zh.md)
