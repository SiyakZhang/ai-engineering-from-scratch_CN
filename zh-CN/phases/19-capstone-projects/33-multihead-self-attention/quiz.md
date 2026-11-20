# 多头自注意力 · 自测

每题先选答案，再展开解析。

## 1. 为什么高效的 self-attention block 用一个输出 3*D 特征的单线性层？

- **A** 它在数学上等价于三个 Linear(D, D) 层，但只跑一次 matmul
- **B** 它避免了使用 causal mask
- **C** 它强制 Q、K、V 之间共享权重
- **D** 它减少了模型参数量

<details>
<summary>查看答案与解析</summary>

**答案**　A

把三个 (D, D) 的投影矩阵叠成一个 (3D, D) 的矩阵，输出完全一致，但前向传播只需一次对加速器友好的 matmul。

</details>

## 2. d_model、n_heads 和 d_head 之间是什么关系？

- **A** d_head = d_model + n_heads
- **B** d_head 与 d_model 无关
- **C** d_head = d_model * n_heads
- **D** d_head = d_model // n_heads，且 d_model 必须能被 n_heads 整除

<details>
<summary>查看答案与解析</summary>

**答案**　D

该 block 把 d_model 均匀分配给各个 head。d_model % n_heads == 0 这个约束在构造时强制检查。

</details>

## 3. scaled dot-product attention 的缩放因子用的是什么值？

- **A** sqrt(d_model)
- **B** sqrt(n_heads)
- **C** sqrt(d_head)
- **D** sqrt(seq_len)

<details>
<summary>查看答案与解析</summary>

**答案**　C

分数要除以 sqrt(d_head)，即 matmul 收缩的那个 head 维度。这样可以让分数的方差在 d_head 增大时保持有界。

</details>

## 4. causal mask 如何保证位置 t 不能 attend 到位置 t+1？

- **A** 为未来位置使用不同的 attention head
- **B** 从输入中移除未来的 token
- **C** 将未来位置的 key 乘以零
- **D** 在 softmax 之前将上三角的 score 设为负无穷

<details>
<summary>查看答案与解析</summary>

**答案**　D

将未来 entry 设为 -inf，softmax 就会给它们分配零权重。过去和当前位置保留有效的权重分布。

</details>

## 5. 为什么 block 在合并 head 之后还要接一个 Linear(D, D) 的输出投影？

- **A** 让模型能够跨 head 混合信息
- **B** 匹配模型的词表大小
- **C** 将激活值归一化到均值为零
- **D** autograd 需要它来追踪梯度

<details>
<summary>查看答案与解析</summary>

**答案**　A

没有输出投影的话，各 head 的输出只能在更后面的层才能组合。这个投影让 block 在同一步内就有一个地方来混合 head 的信息。

</details>

## 6. shape 为 (B, H, T, T) 的 attention weight 矩阵告诉你什么？

- **A** 每个 head 有多少参数
- **B** 下一个 token 的输出 logits
- **C** 对于每个 batch 元素、每个 head，每个 query 位置 attend 到了哪些 key 位置
- **D** query 和 value 向量之间的余弦相似度

<details>
<summary>查看答案与解析</summary>

**答案**　C

per-head 矩阵中第 t 行是 query 位置 t 在 key 位置上的分布。检查它就能看到每个 head 在关注哪里。

</details>


[返回本课](docs/zh.md)
