# 文本处理 —— 分词、词干提取、词形还原 · 自测

每题先选答案，再展开解析。

## 1. 为什么语言模型在训练前需要预处理？

- **A** 只有不使用空格的语言才需要预处理
- **B** 模型可以直接读取字符串
- **C** 预处理能提升 GPU 利用率
- **D** 模型消费的是离散的整数 token，而不是原始文本

<details>
<summary>查看答案与解析</summary>

**答案**　D

模型基于整数 token ID 运算；预处理把连续的语言桥接到离散的输入。

</details>

## 2. 哪种预处理操作是基于规则的后缀剥离？

- **A** 词形还原（Lemmatization）
- **B** 词性标注（POS tagging）
- **C** 词干提取（Stemming）
- **D** 分词（Tokenization）

<details>
<summary>查看答案与解析</summary>

**答案**　C

词干提取用规则裁掉后缀；速度快，但可能出错。

</details>

## 3. Porter 词干提取器的 step 1a 对单词 'ponies' 返回什么？

- **A** ponie
- **B** pony
- **C** poni
- **D** ponies

<details>
<summary>查看答案与解析</summary>

**答案**　C

'ies' 规则把后缀替换为 'i'，得到 'poni'；真正 Porter 的 step 1b 会进一步清理它。

</details>

## 4. 为什么词形还原通常需要一个词性标签？

- **A** 为了减少内存占用
- **B** 提速
- **C** 处理 Unicode
- **D** 语法上下文能消歧像 'better'（形容词）与 'better'（动词）这样的形式

<details>
<summary>查看答案与解析</summary>

**答案**　D

词元（lemma）取决于语法角色；没有词性标签，查找就会有歧义。

</details>

## 5. 把 NLTK Penn Treebank 词性标签转换为 WordNet 标签时，以 'V' 开头的标签映射到什么？

- **A** 'a'（形容词）
- **B** 'r'（副词）
- **C** 'n'（名词）
- **D** 'v'（动词）

<details>
<summary>查看答案与解析</summary>

**答案**　D

以 V 为前缀的 Penn Treebank 标签映射到 WordNet 的 'v'。

</details>

## 6. NLP 预处理中的“训练/推理不匹配”是指什么？

- **A** 一个 GPU 内存问题
- **B** 训练与服务（serving）施加了不同的预处理，导致模型在推理时看到陌生的分布
- **C** 在一个 notebook 中混用多个 tokenizer 库
- **D** 训练和测试之间 batch size 不同

<details>
<summary>查看答案与解析</summary>

**答案**　B

训练与推理使用不同的预处理是生产环境 NLP 最常见的故障。

</details>

## 7. 在 transformer 流水线中，你应该选用哪种工具来替代经典预处理？

- **A** spaCy 的 en_core_web_sm
- **B** 一个正则表达式 tokenizer
- **C** 模型自带的 tokenizer（例如通过 tokenizers / transformers）
- **D** NLTK 的 word_tokenize

<details>
<summary>查看答案与解析</summary>

**答案**　C

transformer 模型会配套发布一个 tokenizer；经典预处理被绕过。

</details>

## 8. 为什么要在 requirements 中固定（pin）NLTK 和 spaCy 的版本？

- **A** 新版本更慢
- **B** tokenizer 和 lemmatizer 的行为会在小版本之间发生变化，悄悄改变训练分布
- **C** 许可证兼容性
- **D** 旧版本支持更多语言

<details>
<summary>查看答案与解析</summary>

**答案**　B

库升级可能改变分词输出，从而偏离训练分布。

</details>


[返回本课](docs/zh.md)
