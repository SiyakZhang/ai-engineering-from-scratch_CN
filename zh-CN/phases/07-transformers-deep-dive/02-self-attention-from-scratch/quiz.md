# 从零实现 Self-Attention · 自测

每题先选答案，再展开解析。

## 1. 为什么普通自注意力要把点积乘以 1/sqrt(d_k)？

- **A** 为了让输出值落在 0 到 1 之间
- **B** 为了防止点积在高维度下变得过大，否则会把 softmax 推入梯度极小的区域
- **C** 为了把 query 和 key 向量归一化为单位长度
- **D** 为了降低矩阵乘法的计算成本

<details>
<summary>查看答案与解析</summary>

**答案**　B

当 d_k 较大时，随机向量的点积会按 sqrt(d_k) 成比例增长。若不做缩放，softmax 会收到很大的输入，产生近乎 one-hot 的输出，从而梯度消失。

</details>

## 2. 自注意力中的三个投影是什么？

- **A** 嵌入、位置和段（segment）
- **B** query、key 和 value —— 每个都是同一输入的一个学习线性投影
- **C** 输入、隐藏和输出
- **D** 编码器、解码器和交叉注意力

<details>
<summary>查看答案与解析</summary>

**答案**　B

自注意力把输入通过三个不同的权重矩阵投影，产生 query（我在找什么？）、key（我包含什么？）和 value（如果匹配上我输出什么？）。

</details>

## 3. 在 8 个 head、d_model=512 的多头注意力中，每个 head 的维度是多少？

- **A** 4096 —— 每个 head 扩展了表示
- **B** 512 —— 每个 head 看到完整维度
- **C** 8 —— 每个 head 一个维度
- **D** 64 —— d_model 在各 head 间均分（512/8=64）

<details>
<summary>查看答案与解析</summary>

**答案**　D

多头注意力把 d_model 拆分为 h 个 head，每个在 d_k = d_model/h 维度上运算。每个 head 512/8 = 64 维时，总计算成本等于在完整维度上做单头注意力。

</details>

## 4. 自回归注意力中的因果掩码（causal mask）防止了什么？

- **A** 它防止模型关注 padding token
- **B** 它防止模型关注自身位置
- **C** 它防止每个位置关注未来位置，确保模型在预测下一个 token 时只能使用过去的上下文
- **D** 它防止注意力权重变得过大

<details>
<summary>查看答案与解析</summary>

**答案**　C

在自回归生成中，token t 不得看到 token t+1、t+2 等。因果掩码在 softmax 之前把未来位置设为负无穷，从而把它们的注意力权重归零。

</details>

## 5. 为什么自注意力在序列长度 n 上有 O(n^2) 复杂度？

- **A** 因为模型有 n 层堆叠在一起
- **B** 因为每个 token 都与其他每个 token 计算注意力分数，产生一个 n x n 的注意力矩阵
- **C** 因为通过注意力的反向传播需要 n^2 次梯度计算
- **D** 因为注意力之后的前馈层是二次方的

<details>
<summary>查看答案与解析</summary>

**答案**　B

QK^T 矩阵乘法产生一个 n x n 的注意力矩阵，其中条目 (i,j) 是 token i 对 token j 的注意力。计算和内存都按 O(n^2) 增长，这正是长上下文模型需要 FlashAttention 等技术的原因。

</details>


[返回本课](docs/zh.md)
