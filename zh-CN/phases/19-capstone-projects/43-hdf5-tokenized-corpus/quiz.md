# HDF5 分词语料库 · 自测

每题先选答案，再展开解析。

## 1. 为什么把 tokenized corpus 存成可扩容、分块的 HDF5 dataset，而不是 JSONL？

- **A** HDF5 的 logo 更小。
- **B** HDF5 提供分块、纯整数、缓存友好的读取和 O(1) 随机访问；JSONL 每次热路径读取都要走解析器。
- **C** 随机原因。
- **D** JSONL 已弃用。

<details>
<summary>查看答案与解析</summary>

**答案**　B

Dataloader 需要一个扁平 token 流和可寻址的切片；HDF5 原生支持。

</details>

## 2. HDF5 chunk 大小相对于 trainer 的 window_size 应该怎么选？

- **A** 把 chunk 设成文档长度。
- **B** 选能放进内存的最大 chunk。
- **C** 始终选 chunk=1。
- **D** 把 chunk 设为 window_size 的整数倍，这样每个样本落在一到两个 chunk 内，读取保持页缓存对齐。

<details>
<summary>查看答案与解析</summary>

**答案**　D

Chunk 和 window_size 不对齐会让吞吐量减半，因为每个样本都会跨两个 chunk。

</details>

## 3. 为什么 token_count 要存成 HDF5 attribute，而不是从 dataset shape 推断？

- **A** Attribute 比较好看。
- **B** 尾部 chunk 可能没填满；没有这个显式 attribute，reader 会读过真实末尾、进入零填充的 token 区域，导致模型学会预测零。
- **C** Attribute 是必需的。
- **D** 读取 shape 很慢。

<details>
<summary>查看答案与解析</summary>

**答案**　B

分块布局有时会留下尾部空位；attribute 才是 ground truth。

</details>

## 4. Writer 把 token 缓冲到 chunk_size 再做一次 resize，这实现了什么？

- **A** 写入是连续且 chunk 对齐的，避免了逐 token resize 带来的碎片化。
- **B** 减小词表大小。
- **C** 省几个 CPU 周期。
- **D** 加快 sha256 计算。

<details>
<summary>查看答案与解析</summary>

**答案**　A

按 chunk 大小缓冲再扩展，是保持 HDF5 chunk 在磁盘上连续的唯一方式。

</details>

## 5. 为什么 swmr=True 是在 reader 端打开，而不是 writer 端？

- **A** 性能考虑。
- **B** 随意偏好。
- **C** Single-Writer-Multiple-Reader 模式让 dataloader worker 能安全共享文件；writer 不需要特殊模式，因为它是每个进程写一个分片。
- **D** 安全考虑。

<details>
<summary>查看答案与解析</summary>

**答案**　C

把两种模式搞混是 'file is locked' 报错最常见的原因。

</details>

## 6. Boundary token id 的存在是为了显式化什么？

- **A** Packed window 内的文档边界，防止模型被静默地训练在跨文档拼接上。
- **B** 随机数据。
- **C** 压缩。
- **D** 词表大小限制。

<details>
<summary>查看答案与解析</summary>

**答案**　A

没有显式边界标记，trainer 会把边界当噪声学；有了它，边界就变成可用的分隔符。

</details>


[返回本课](docs/zh.md)
