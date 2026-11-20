# 长上下文评估 —— NIAH、RULER、LongBench、MRCR · 自测

每题先选答案，再展开解析。

## 1. 原始的 NIAH 基准衡量什么？

- **A** tokenizer 繁殖率
- **B** 仅多跳推理
- **C** 模型能否在长上下文中、在受控的不同深度检索到一个植入的事实
- **D** 嵌入余弦漂移

<details>
<summary>查看答案与解析</summary>

**答案**　C

NIAH = 大海捞针：植入一个事实，让模型检索它，并扫描深度和长度。

</details>

## 2. 为什么宣称的上下文窗口常常与可用上下文相差很大？

- **A** beam search 变慢
- **B** 嵌入溢出
- **C** tokenizer 截断
- **D** 注意力随长度和任务退化；规格表的最大值在多跳或推理负载下很少成立

<details>
<summary>查看答案与解析</summary>

**答案**　D

用于推理的有效上下文通常是宣称最大值的 25-50%。

</details>

## 3. RULER 相比 NIAH 增加了什么？

- **A** 覆盖检索、多跳追踪、聚合和 QA 的 13 种任务类型，在多个上下文长度上进行
- **B** 翻译任务
- **C** 逐 token 的 logprob
- **D** 更快的推理

<details>
<summary>查看答案与解析</summary>

**答案**　A

RULER 把 NIAH 扩展为多任务长上下文基准，能抓住那些在 NIAH 上饱和却在别处失败的模型。

</details>

## 4. 什么是“迷失在中间”（lost in the middle）效应？

- **A** 模型对放在长输入中间的内容关注不足；depth=0.5 常常比 depth=0 或 1 表现更差
- **B** 模型遗忘第一个 token
- **C** 模型丢失标点
- **D** 模型重排 token

<details>
<summary>查看答案与解析</summary>

**答案**　A

上下文中部的内容最不受关注；扫描深度会暴露呈 U 形的准确率曲线。

</details>

## 5. 为什么仅用 NIAH 的评估必须辅以多跳测试？

- **A** 多跳更快
- **B** 前沿模型可以在单针检索上得满分，却仍在多跳变量追踪或聚合任务上失败
- **C** NIAH 无法在长上下文上运行
- **D** NIAH 缺少真值

<details>
<summary>查看答案与解析</summary>

**答案**　B

通过检索并不意味着通过推理；多跳基准能暴露真实的上限。

</details>

## 6. NoLiMa 着重考验什么？

- **A** 流式输出
- **B** 分词
- **C** 延迟
- **D** 与查询不共享任何字面 token 的针，因此检索需要一个语义推理步骤

<details>
<summary>查看答案与解析</summary>

**答案**　D

NoLiMa 去除词面重叠，使模型必须推理而非匹配关键词。

</details>

## 7. 长上下文的规格表应该报告哪两个数字？

- **A** 有效检索长度（例如 90% NIAH 通过）和有效推理长度（例如 70% 多跳通过）
- **B** 仅 GPU 内存和延迟
- **C** 仅每秒 token 数
- **D** 仅宣称的最大值

<details>
<summary>查看答案与解析</summary>

**答案**　A

区分检索有效长度和推理有效长度，对真实世界的论断至关重要。

</details>

## 8. 为什么要测量长上下文长度下的首 token 时间（time-to-first-token）？

- **A** beam search 依赖它
- **B** RAG 所要求
- **C** 100 万 token 的预填充（prefill）可能耗时数十秒；仅看准确率会掩盖影响产品的延迟
- **D** 分词很慢

<details>
<summary>查看答案与解析</summary>

**答案**　C

长 prompt 的预填充成本巨大；延迟必须与准确率一并跟踪。

</details>


[返回本课](docs/zh.md)
