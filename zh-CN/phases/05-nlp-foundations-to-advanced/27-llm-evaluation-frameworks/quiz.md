# LLM 评估 —— RAGAS、DeepEval、G-Eval · 自测

每题先选答案，再展开解析。

## 1. 为什么 Exact Match 和 token-F1 不足以评估现代 LLM 输出？

- **A** 它们需要 GPU
- **B** 它们错过语义等价；'June 29th, 2007' 与 'June 29, 2007' 尽管正确却得 0 EM
- **C** 它们太慢
- **D** 它们不可微

<details>
<summary>查看答案与解析</summary>

**答案**　B

Exact-match/F1 无法识别人类会判为正确的同义改写或格式差异。

</details>

## 2. RAGAS 的忠实度（faithfulness）指标衡量什么？

- **A** 每秒 token 数
- **B** 检索召回率
- **C** 延迟
- **D** 通过 NLI，答案中的每条论断是否被检索到的上下文蕴含

<details>
<summary>查看答案与解析</summary>

**答案**　D

忠实度用 NLI 蕴含逐条核对答案论断与检索到的上下文。

</details>

## 3. 为什么在信任评分之前，必须用人工标签校准评判模型（judge）？

- **A** 校准是个分词问题
- **B** 校准加速评判
- **C** 如果评判与人工标签之间的 Spearman 相关性太低（例如低于 0.7），那分数就是噪声而非信号
- **D** GDPR 所要求

<details>
<summary>查看答案与解析</summary>

**答案**　C

没有校准，你无法分辨评判分数反映的是质量还是模型偏见。

</details>

## 4. 在 LLM-as-judge 设置中，自评偏差（self-evaluation bias）是什么？

- **A** 评判在缓存输出上跑得更快
- **B** 用同一 LLM 家族来生成和评判，相比独立评判会把分数虚高 10-20%
- **C** 更低的延迟
- **D** 评判忽略系统 prompt

<details>
<summary>查看答案与解析</summary>

**答案**　B

同家族的生成器+评判会把分数向上偏置；评判时应使用不同的模型家族。

</details>

## 5. 相比朴素的“打 0-1 分”prompt，G-Eval 具体增加了什么？

- **A** 更大的上下文
- **B** 多语言打分
- **C** 一份带命名评估步骤的显式思维链（chain-of-thought）评分表，能产生更稳定的分数
- **D** 更低的成本

<details>
<summary>查看答案与解析</summary>

**答案**　C

G-Eval 结构化的评估步骤比自由形式的“给它评分”prompt 产生更可靠的分数。

</details>

## 6. 为什么只报告聚合平均分是危险的？

- **A** 聚合需要 GPU
- **B** 聚合太大
- **C** 0.85 的均值可能掩盖 5% 的灾难性失败；始终检查最低分位
- **D** 聚合忽略评判

<details>
<summary>查看答案与解析</summary>

**答案**　C

均值掩盖尾部失败；暴露最低 10% 以捕捉高严重度问题。

</details>

## 7. 为什么要在 CI 中固定评判模型 + 版本？

- **A** tokenizer 漂移
- **B** 升级评判会改变每一个指标；没有冻结的评判，纵向比较就会失效
- **C** Anthropic 所要求
- **D** 更低的成本

<details>
<summary>查看答案与解析</summary>

**答案**　B

评判升级会悄悄移动指标基线；固定它可保持跨运行的可比性。

</details>

## 8. 相对于 RAGAS，DeepEval 处于什么位置？

- **A** DeepEval 仅托管
- **B** DeepEval 是“给 LLM 用的 pytest”（CI 门禁、G-Eval、幻觉指标）；RAGAS 专注于无参考的 RAG 监控
- **C** DeepEval 是个 tokenizer
- **D** 完全替代 RAGAS

<details>
<summary>查看答案与解析</summary>

**答案**　B

DeepEval 锚定 CI/CD 回归测试；RAGAS 处理无参考的 RAG 监控。

</details>


[返回本课](docs/zh.md)
