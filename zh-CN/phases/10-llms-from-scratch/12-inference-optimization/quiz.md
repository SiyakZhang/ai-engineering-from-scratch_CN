# 推理优化 · 自测

每题先选答案，再展开解析。

## 1. LLM 推理的两个阶段是什么？

- **A** 预填充（prefill，并行处理 prompt，受计算限制）和解码（decode，逐个生成 token，受内存限制）
- **B** 编码和解码
- **C** 前向和反向
- **D** 训练和评估

<details>
<summary>查看答案与解析</summary>

**答案**　A

预填充并行处理所有 prompt token（受计算限制）。解码自回归地逐个生成 token（受加载模型权重的内存带宽限制）。不同的优化分别针对各个阶段。

</details>

## 2. KV-cache 在自回归生成中消除了什么？

- **A** 在每个生成步骤中对所有先前 token 的 key 和 value 向量的冗余重算
- **B** embedding 查找
- **C** 对 attention mask 的需求
- **D** softmax 计算

<details>
<summary>查看答案与解析</summary>

**答案**　A

没有 KV-cache，生成第 N 个 token 需要为前面 N-1 个 token 重算 attention 的 key 和 value。KV-cache 存储了这些向量，因此每个新 token 只计算它自己的 K 和 V，每步节省 O(N) 的计算。

</details>

## 3. 什么是连续批处理（continuous batching），为什么它能提升吞吐量？

- **A** 跨多个模型批处理
- **B** 使用更大的批次大小
- **C** 在请求开始和结束时动态地往运行中的批次里加入和移除请求，而不是等整个批次都完成
- **D** 把所有请求放进一个大批次处理

<details>
<summary>查看答案与解析</summary>

**答案**　C

在静态批处理中，一个短请求会一直占着它的批次槽位直到最长的请求完成。连续批处理立即用新请求填补已完成的槽位，让 GPU 保持忙碌并提升整体吞吐量。

</details>

## 4. PagedAttention（在 vLLM 中使用）解决了什么问题？

- **A** 它加快了 attention 计算
- **B** 它提升分词速度
- **C** 它像虚拟内存一样用固定大小的块管理 KV-cache 内存，消除变长序列带来的碎片化
- **D** 它减小模型大小

<details>
<summary>查看答案与解析</summary>

**答案**　C

变长序列的 KV-cache 会导致内存碎片化（分配之间浪费的空隙）。PagedAttention 以固定块分配 KV-cache，并用页表映射它们，就像操作系统的虚拟内存。

</details>

## 5. 什么是推测解码（speculative decoding）？

- **A** 缓存频繁生成的序列
- **B** 生成多个回复并挑选最好的
- **C** 用一个小的草稿模型提出多个 token，再由大模型并行验证，从而加快生成
- **D** 预测用户想要哪些 token

<details>
<summary>查看答案与解析</summary>

**答案**　C

一个小而快的模型生成 N 个候选 token。大模型在单次前向传播中并行验证全部 N 个。如果有 K 个 token 被接受，你就在大约 1 个大模型步骤的时间内生成了 K 个 token。

</details>


[返回本课](docs/zh.md)
