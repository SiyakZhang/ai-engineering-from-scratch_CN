# 子词分词 —— BPE、WordPiece、Unigram、SentencePiece · 自测

每题先选答案，再展开解析。

## 1. 相比词级词汇表，子词分词给你带来了什么？

- **A** 更小的模型
- **B** 更好的嵌入
- **C** 更快的训练
- **D** 稀有词分解为已知的子词片段，消除 OOV 的同时保持词汇表有界

<details>
<summary>查看答案与解析</summary>

**答案**　D

子词 token 通过分解覆盖任意输入，消除了词级词汇表的 OOV 问题。

</details>

## 2. 为什么 GPT-2 使用字节级 BPE 而非字符级 BPE？

- **A** 字节更小
- **B** 字节 BPE 跳过合并
- **C** transformer 所要求
- **D** 256 个字节的基础词汇表覆盖任意 UTF-8 输入，保证没有 [UNK] token

<details>
<summary>查看答案与解析</summary>

**答案**　D

字节级 BPE 从 256 个字节出发，使任何输入都能编码；不存在 OOV。

</details>

## 3. Unigram tokenizer 如何构建其词汇表？

- **A** 从一个大的候选集出发，迭代地剪除那些移除后对语料对数似然损害最小的 token
- **B** 贪心 IDF 加权
- **C** 随机采样
- **D** 贪心地合并高频对

<details>
<summary>查看答案与解析</summary>

**答案**　A

Unigram 拟合一个 unigram LM，并迭代移除最无用的 token 以达到目标词汇表大小。

</details>

## 4. WordPiece 的合并准则与 BPE 有何区别？

- **A** WordPiece 使用字节
- **B** WordPiece 合并能最大化训练语料似然的词对，而 BPE 合并频率最高的词对
- **C** WordPiece 跳过合并
- **D** WordPiece 是无监督的

<details>
<summary>查看答案与解析</summary>

**答案**　B

WordPiece 按似然挑选合并；BPE 按原始频率挑选。

</details>

## 5. 哪个工具直接在原始多语言 Unicode 文本上训练 tokenizer？

- **A** SentencePiece（把空格编码为特殊标记，并训练 BPE 或 Unigram）
- **B** tokenizers-lite
- **C** tiktoken
- **D** spaCy

<details>
<summary>查看答案与解析</summary>

**答案**　A

SentencePiece 在原始文本上训练 BPE/Unigram，无需预分词；tiktoken 只做编码。

</details>

## 6. 为什么生产 CI 必须对部署的 tokenizer.json 做哈希校验？

- **A** 为了压缩存储
- **B** tokenizer 漂移会产生与模型训练时不同的 token ID，悄悄损坏输出
- **C** Hugging Face 所要求
- **D** 它能缩小词汇表大小

<details>
<summary>查看答案与解析</summary>

**答案**　B

即便很小的 tokenizer 改动也会移动 ID；哈希校验能在影响用户之前发现漂移。

</details>

## 7. 单个 emoji 占用很多 token 的一个常见原因是什么？

- **A** 多码点 emoji 编码为多个 UTF-8 字节；没有专门 token 时每个字节就是各自的子词
- **B** emoji 以浮点数存储
- **C** emoji 是停止字符
- **D** emoji 是保留字符

<details>
<summary>查看答案与解析</summary>

**答案**　A

复合 emoji 编码为多个字节；字节级 tokenizer 可能每个字形用多个 token。

</details>

## 8. 为新的单语 transformer 选择词汇表大小有什么经验法则？

- **A** 总是 8000
- **B** 总是 1M
- **C** 与训练语料大小匹配
- **D** 1B 参数以下的模型大约 32k；1-10B 用 50-100k；多语言或前沿模型用 200k 以上

<details>
<summary>查看答案与解析</summary>

**答案**　D

词汇表大小随模型规模和语言覆盖而变；这些是大致的社区默认值。

</details>


[返回本课](docs/zh.md)
