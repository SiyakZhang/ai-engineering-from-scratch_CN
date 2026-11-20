# Token Embedding 与 Positional Embedding · 自测

每题先选答案，再展开解析。

## 1. embedding 阶段把 (B, T) 的 ids 变成什么 shape？

- **A** (B, T, V)，其中 V 是词表大小
- **B** (B, V)
- **C** (B, T, D)，其中 D 是模型维度
- **D** (B, T)

<details>
<summary>查看答案与解析</summary>

**答案**　C

每个 id 被映射到一个 D 维向量。batch 保留 B 和 T，多出一个特征维度 D。

</details>

## 2. 本课中 token embedding 和 positional embedding 是怎么组合的？

- **A** 沿特征轴拼接
- **B** 额外加一层线性投影
- **C** 取逐元素最大值
- **D** 逐元素相加，position 向量在 batch 维度上广播

<details>
<summary>查看答案与解析</summary>

**答案**　D

shape 为 (B, T, D) 和 (T, D) 的两个 tensor 做加法。广播把 positional table 沿 batch 轴复制。

</details>

## 3. SinusoidalPositionalEmbedding 贡献了多少可学习参数？

- **A** 零
- **B** max_context_length
- **C** max_context_length * d_model
- **D** d_model

<details>
<summary>查看答案与解析</summary>

**答案**　A

正弦表是根据公式计算出来并存为 buffer 的，不贡献任何可学习参数。

</details>

## 4. 哪种 positional encoding 不能接受超过其构造上限的序列长度？

- **A** Sinusoidal positional embedding
- **B** 两者都是
- **C** 两者都不是
- **D** Learned positional embedding

<details>
<summary>查看答案与解析</summary>

**答案**　B

在本课的实现中，两个类都在 forward 时强制检查 max_context_length。Learned 本身受表大小限制；这里的 sinusoidal 也受限，因为它用的是预先构建好的表。

</details>

## 5. 正弦方案为什么在相邻特征对上同时使用 sin 和 cos？

- **A** 因为单独的 sin 不是周期性的
- **B** 因为单独的 cos 不能做反向传播
- **C** 这样位置 p+k 处的向量就是位置 p 处向量的线性函数
- **D** 因为这样能翻倍参数量

<details>
<summary>查看答案与解析</summary>

**答案**　C

在同一波长上配对 sin 和 cos，意味着位置偏移 k 等价于一次旋转，而旋转是线性变换。attention 因此可以通过线性投影来学习相对偏移。

</details>

## 6. 为什么 embedding 的反向传播只更新 token table 中在本 batch 出现过的行？

- **A** 前向传播中没被碰到的行，根据链式法则对 loss 的梯度为零
- **B** token id 是用稀疏数据结构存储的
- **C** PyTorch 只存储非零 entry 的梯度
- **D** 优化器会跳过它没见过的行

<details>
<summary>查看答案与解析</summary>

**答案**　A

一行如果没有参与任何输出的计算，它对 loss 的导数就是零，所以这一步它的梯度为零。

</details>


[返回本课](docs/zh.md)
