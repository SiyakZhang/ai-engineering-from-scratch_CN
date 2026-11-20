# 命名实体识别 · 自测

每题先选答案，再展开解析。

## 1. 什么是 BIO 标注？

- **A** 一种分词风格
- **B** 一种实体/非实体的二元方案
- **C** 实体的树状表示
- **D** 逐 token 的标签：B-TYPE 表示实体起始，I-TYPE 表示实体内部，O 表示实体外部

<details>
<summary>查看答案与解析</summary>

**答案**　D

BIO 用 B/I/O 前缀把跨度抽取转化为 token 分类。

</details>

## 2. 为什么基于规则的词典表（gazetteer）在生产 NER 中很脆弱？

- **A** 它们对新实体毫无覆盖，且无法消歧（例如 Apple 是水果还是公司）
- **B** 它们很慢
- **C** 它们需要 GPU
- **D** 它们无法处理多 token 实体

<details>
<summary>查看答案与解析</summary>

**答案**　A

词典表能匹配已知字符串，但无法消歧词义，也无法泛化到未见过的名称。

</details>

## 3. 对于 NER，CRF 相比 HMM 的关键优势是什么？

- **A** CRF 更快
- **B** CRF 永远不需要训练数据
- **C** CRF 避免使用 Viterbi 算法
- **D** CRF 是判别式的，可以混合任意特征（词形、大小写、邻接词）

<details>
<summary>查看答案与解析</summary>

**答案**　D

CRF 是判别式的，让你能基于丰富的、相互重叠的特征做条件建模。

</details>

## 4. 在 BiLSTM-CRF 架构中，CRF 层起什么作用？

- **A** 替代嵌入
- **B** 执行分词
- **C** 预训练 LSTM
- **D** 通过在 LSTM 发射分数之上建模标签到标签的转移，强制生成合法的 BIO 标签序列

<details>
<summary>查看答案与解析</summary>

**答案**　D

位于 LSTM 特征之上的 CRF 建模标签间依赖，并排除非法序列。

</details>

## 5. 为什么 NER 必须用实体级 F1 而非 token 级 F1 来评估？

- **A** 预测跨度必须与真实跨度完全匹配；token 级 F1 因计入部分匹配而高估了准确率
- **B** 实体级 F1 更容易计算
- **C** HuggingFace 要求使用实体级 F1
- **D** token 级 F1 无法处理 BIO

<details>
<summary>查看答案与解析</summary>

**答案**　A

跨度精确匹配才是有意义的指标；token 级 F1 通过部分重叠虚高了分数。

</details>

## 6. 在 HuggingFace NER pipeline 中，aggregation_strategy='simple' 做什么？

- **A** 只返回置信度最高的实体
- **B** 把输出转为小写
- **C** 跳过分词
- **D** 把连续的 B-X 和 I-X token 合并成单个跨度

<details>
<summary>查看答案与解析</summary>

**答案**　D

它把同一类型的连续 BIO token 合并成跨度级别的实体。

</details>

## 7. 为什么标准 BIO 在嵌套实体上会失败？

- **A** BIO 无法表示多 token 实体
- **B** BIO 丢弃了类型标签
- **C** BIO 需要一个 transformer
- **D** BIO 是扁平的逐 token 方案，无法表达两个不同类型、相互重叠的跨度

<details>
<summary>查看答案与解析</summary>

**答案**　D

BIO 给每个 token 分配一个标签；嵌套跨度需要多趟处理或基于跨度的模型。

</details>

## 8. 在 2026 年，经典 NER（CRF 或 BiLSTM-CRF）什么时候仍然胜过 LLM？

- **A** 只要输入是英语
- **B** 在嵌套实体上
- **C** 在开放域叙事文本上
- **D** 在严苛的延迟预算、标注数据充足、本体稳定，或非生成式的合规约束下

<details>
<summary>查看答案与解析</summary>

**答案**　D

在延迟、标注数据充足的场景、固定本体以及私有化部署约束下，经典 NER 占优。

</details>


[返回本课](docs/zh.md)
