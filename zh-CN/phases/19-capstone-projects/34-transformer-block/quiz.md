# 从零实现 Transformer Block · 自测

每题先选答案，再展开解析。

## 1. 一个 decoder transformer block 内部有哪两个 sublayer？

- **A** Embedding lookup 和 softmax
- **B** 卷积和循环门控
- **C** RNN encoder 和 decoder
- **D** Multi-head causal attention 和逐位置 MLP，各自包裹在一条 residual connection 里

<details>
<summary>查看答案与解析</summary>

**答案**　D

现代 decoder LLM 的每个 block 都是 attention 加 MLP，各有自己的 residual 路径和自己的 LayerNorm。

</details>

## 2. 在深层网络中，pre-LN 和 post-LN 的关键区别是什么？

- **A** post-LN 在 GPU 上更快
- **B** pre-LN 只适用于 encoder
- **C** pre-LN 用了不同的 attention 数学
- **D** pre-LN 让 residual 信号保持未归一化状态，梯度可以干净地传到 embedding；post-LN 把 norm 放在 residual add 之后，会在深层压缩梯度，需要 warmup

<details>
<summary>查看答案与解析</summary>

**答案**　D

pre-LN 在常见学习率下不需要 warmup 就能稳定训练；post-LN 是 2017 年原始论文的做法，需要 warmup。

</details>

## 3. multi-head attention 中的 causal mask 做了什么？

- **A** 对 attention score 做归一化
- **B** 随机丢弃 token
- **C** 选取 batch 中最长的序列
- **D** 把 attention logits 的上三角设为负无穷，使位置 i 不能 attend 到大于 i 的位置

<details>
<summary>查看答案与解析</summary>

**答案**　D

忘记 causal mask 就等于训了一个能看到未来 token 的模型；mask 是唯一保证因果性的部件。

</details>

## 4. 为什么用融合的 QKV 投影而不是三个独立的 linear？

- **A** 它改变了模型的表达能力
- **B** 它去掉了 residual
- **C** 它避免了 softmax
- **D** 一个宽度为 3 倍 d_model 的 linear 把三次 kernel launch 和三次 matmul 合成一次，在所有加速器上都更快，且与 GPT-2 参考实现一致

<details>
<summary>查看答案与解析</summary>

**答案**　D

数学一样，kernel 更少；GPT-2、LLaMA 和 Mistral 的参考实现都用了融合投影。

</details>

## 5. Dropout 不该放在 transformer block 的哪里？

- **A** residual identity 路径本身上，因为这会破坏让梯度在深层畅通流动的加法恒等性
- **B** attention softmax 输出上
- **C** feed-forward 扩展内部
- **D** 第二个 MLP linear 之后

<details>
<summary>查看答案与解析</summary>

**答案**　A

dropout 应该放在 attention 输出和 MLP 的 residual 更新上，永远不要放在 residual 的 identity 分支上。

</details>

## 6. 为什么把 causal mask 注册为 buffer 而不是每次 forward 时分配？

- **A** buffer 是加密的
- **B** buffer 只能在 GPU 上运行
- **C** buffer 能提高数值精度
- **D** mask 只取决于最大上下文长度，在构造时分配一次、每次 forward 时切片出活跃窗口，就能避免长上下文场景下的分配器热点

<details>
<summary>查看答案与解析</summary>

**答案**　D

用 register_buffer 分配一次，forward 时切片；否则 mask 就成了每次调用的分配开销。

</details>


[返回本课](docs/zh.md)
