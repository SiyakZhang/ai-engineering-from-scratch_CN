# 任务规格格式 · 自测

每题先选答案，再展开解析。

## 1. 为什么要在编写打分代码之前先冻结任务记录的 schema？

- **A** 它锁死了契约，让 metric、runner 和后处理器对字段名达成一致
- **B** 这样 JSON 解析器跑得更快
- **C** 它省掉了写校验器的必要
- **D** 它允许随意新增 metric 名字而不用再改任何东西

<details>
<summary>查看答案与解析</summary>

**答案**　A

schema 就是每个下游消费者读取的契约。把它锁死后，你就能独立改动各个组件而不会破坏其余部分。

</details>

## 2. metric_name 字段接受的封闭词表是什么？

- **A** 只有 exact_match 和 f1
- **B** exact_match、f1、bleu_4、rouge_l、accuracy、code_exec
- **C** 任务作者随便挑的任意字符串
- **D** runner 被配置成能识别的任何值

<details>
<summary>查看答案与解析</summary>

**答案**　B

本课把 metric 词表钉死为六个名字。要加一个就得开一节新课，并在校验器里新增一条条目。

</details>

## 3. 当校验器在一条记录上看到未知的顶层字段时，它会怎么做？

- **A** 返回校验错误并拒绝这条记录
- **B** 把它重命名为 metadata.unknown
- **C** 把它剥掉然后继续
- **D** 记一条 warning 但接受这条记录

<details>
<summary>查看答案与解析</summary>

**答案**　A

未知字段是前向兼容的隐患。校验器直接拒绝它们，好让 schema 始终是唯一的事实来源。

</details>

## 4. 为什么 few-shot 示例是附在任务记录上，而不是由 runner 计算出来？

- **A** 作者意图是 eval 的一部分；把示例绑定到任务上，就消除了不同模型在构造 prompt 时的差异
- **B** 这样能省磁盘空间
- **C** runner 没有文件 I/O
- **D** few-shot 只在 fine-tuning 时才用

<details>
<summary>查看答案与解析</summary>

**答案**　A

few-shot 的组织方式属于 eval 定义，而不属于模型接口。把它放进任务里，每个模型看到的 prompt 就完全一样。

</details>

## 5. 在校验器看来，哪一对「类别-metric」组合是非法的？

- **A** summary + rouge_l
- **B** code_exec + code_exec
- **C** arithmetic + exact_match
- **D** mcq + bleu_4

<details>
<summary>查看答案与解析</summary>

**答案**　D

对单个字母算 BLEU 毫无意义。校验器强制要求 mcq 任务只能用 exact_match 或 accuracy。

</details>

## 6. 当生成结果是 `Answer: C is correct` 时，后处理规则 extract_letter 会返回什么？

- **A** 原封不动的整个字符串
- **B** C
- **C** 空字符串
- **D** Answer

<details>
<summary>查看答案与解析</summary>

**答案**　B

extract_letter 返回生成结果中第一个匹配 [A-E] 的字符。这个字符串在正文开头就是 C。

</details>


[返回本课](docs/zh.md)
