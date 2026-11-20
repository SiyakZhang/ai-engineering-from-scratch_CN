# 关系抽取与知识图谱构建 · 自测

每题先选答案，再展开解析。

## 1. 知识图谱的原子单元是什么？

- **A** 一个词性标签
- **B** 一个句子
- **C** 一个 token
- **D** 一个（主语，关系，宾语）三元组

<details>
<summary>查看答案与解析</summary>

**答案**　D

知识图谱以（s, r, o）三元组存储信息；聚合的三元组构成图谱。

</details>

## 2. 在 2026 年的关系抽取中，AEVS 代表什么？

- **A** Anchor-Extraction-Verification-Supplement（锚定-抽取-验证-补充）：锚定跨度，抽取三元组，对照源文验证，补充覆盖
- **B** Async Entity Validation Service
- **C** Auto-Encoder Vector Search
- **D** Aggregated Entity-Value Schema

<details>
<summary>查看答案与解析</summary>

**答案**　A

AEVS 是 2026 年用于基于来源的关系抽取的幻觉缓解框架。

</details>

## 3. 为什么每个三元组都必须携带来源出处（doc id + 跨度）？

- **A** 出处让你能审计三元组，并拒绝那些跨度与源文不匹配的幻觉
- **B** 出处改变本体
- **C** SPARQL 要求出处
- **D** 它加速抽取

<details>
<summary>查看答案与解析</summary>

**答案**　A

出处使审计成为可能，是 AEVS 式幻觉检测的核心。

</details>

## 4. 关系的规范化（canonicalization）做什么？

- **A** 添加嵌入
- **B** 移除三元组
- **C** 翻译文档
- **D** 把表面动词短语（例如 'was born in'、'is a native of'）映射到一个固定的属性 id，使图谱可查询

<details>
<summary>查看答案与解析</summary>

**答案**　D

规范化把各种同义改写归并为规范的知识图谱属性 id。

</details>

## 5. 为什么关系抽取通常需要先做共指消解？

- **A** 共指提供位置
- **B** 像 'he founded Apple' 中的代词，必须在三元组抽取前消解为一个命名实体
- **C** 共指规范化大小写
- **D** 共指添加嵌入

<details>
<summary>查看答案与解析</summary>

**答案**　B

没有共指，关系抽取会把关系挂到代词上，而非其背后的命名实体。

</details>

## 6. 哪个选择以牺牲开放式信息抽取（open IE）召回率为代价换取图谱可查询性？

- **A** 跳过 NER
- **B** 随机采样三元组
- **C** 在并入知识图谱前，把 open-IE 关系映射到一个封闭本体（例如 Wikidata 属性）
- **D** 仅嵌入的图谱

<details>
<summary>查看答案与解析</summary>

**答案**　C

封闭本体使图谱可查询；规范化步骤在下游能回本。

</details>

## 7. 为什么许多生产知识图谱使用时间限定符（起始/结束时间）？

- **A** 许多关系是有时间界限的（雇主、配偶、职位）；限定符防止那些会过期的“永远为真”的论断
- **B** 更快的 SPARQL
- **C** RDF 所要求
- **D** 为了移除 NIL 实体

<details>
<summary>查看答案与解析</summary>

**答案**　A

有时间界限的关系需要限定符（例如 Wikidata 的 P580/P582），否则事实会悄悄过期。

</details>

## 8. REBEL 是什么？

- **A** 一个向量数据库
- **B** 一个共指模型
- **C** 一个 seq2seq 关系抽取器，输出的三元组已经采用 Wikidata 属性 id
- **D** 一个 tokenizer

<details>
<summary>查看答案与解析</summary>

**答案**　C

REBEL（Babelscape）是一个在远程监督的 Wikidata 三元组上训练的 seq2seq 关系抽取模型。

</details>


[返回本课](docs/zh.md)
