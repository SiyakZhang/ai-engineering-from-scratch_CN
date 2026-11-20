# 注意力机制 —— 那次突破 · 自测

每题先选答案，再展开解析。

## 1. Bahdanau 注意力解决了 seq2seq 中的什么问题？

- **A** beam search 延迟
- **B** 固定大小上下文向量的瓶颈，即解码器只能看到编码器的最终状态
- **C** 编码器中的梯度消失
- **D** 分词不匹配

<details>
<summary>查看答案与解析</summary>

**答案**　B

注意力让解码器能查询每一个编码器状态，而不只是最后一个。

</details>

## 2. 解码器第 t 步的注意力上下文向量是什么？

- **A** 一个随机投影
- **B** 编码器的最终隐藏状态
- **C** 编码器隐藏状态的加权平均，权重来自 query-key 评分
- **D** 解码器的输入嵌入

<details>
<summary>查看答案与解析</summary>

**答案**　C

上下文 = sum of alpha_i * h_i，是编码器状态的、随步骤变化的加权平均。

</details>

## 3. 在 Bahdanau（加性）注意力中，向量 v_a 起什么作用？

- **A** 它是把注意力维度的隐藏组合转换为每个编码器位置一个标量分数的那个投影
- **B** 它给 softmax 加偏置
- **C** 它编码位置
- **D** 它控制 dropout

<details>
<summary>查看答案与解析</summary>

**答案**　A

v_a 与 tanh(W_a s + U_a h) 做点积，把一个 d_attn 向量坍缩成一个标量分数。

</details>

## 4. 在 Luong 的 'dot' 注意力变体中，必须满足什么约束？

- **A** 解码器状态和编码器状态必须共享相同的维度（d_s == d_h）
- **B** 需要 beam search
- **C** softmax 必须在对数空间
- **D** 编码器必须是双向的

<details>
<summary>查看答案与解析</summary>

**答案**　A

dot 使用 s^T h 而无投影，所以维度必须完全匹配。

</details>

## 5. 哪种 Q/K/V 映射描述了经典（Bahdanau/Luong）注意力？

- **A** Q、K、V 是源序列的三个独立学习投影
- **B** Q 是随机的，K 和 V 是学习的
- **C** Q = 解码器状态；K 和 V = 编码器状态（同一个张量）
- **D** Q 来自编码器，K 和 V 来自解码器

<details>
<summary>查看答案与解析</summary>

**答案**　C

在经典注意力中，键和值都是编码器状态；transformer 通过学习投影把 K 和 V 分开。

</details>

## 6. 为什么把原始注意力权重当作“解释”来报告被认为是脆弱的？

- **A** 它们太小无法绘图
- **B** 研究（例如 Jain and Wallace, 2019）表明，在某些任务上注意力分布可以被打乱而不改变预测
- **C** 注意力权重会泄露标签
- **D** 注意力权重不可微

<details>
<summary>查看答案与解析</summary>

**答案**　B

注意力权重与预测相关，但若不做消融/反事实检验，它们并非忠实的解释。

</details>

## 7. 哪一步把 Bahdanau 注意力衔接到 transformer 自注意力？

- **A** 去掉 beam search
- **B** 增加更多 RNN 层
- **C** 用 sigmoid 替换 softmax
- **D** 用各自学习的 Q、K、V 投影让序列对自身做查询，并在多个并行的 head 中运行

<details>
<summary>查看答案与解析</summary>

**答案**　D

自注意力对同一序列做查询，使用拆分的 K 和 V 投影，并跨多个 head 并行化。

</details>

## 8. 注意力中的 masking 有什么实际用例？

- **A** 缩小模型规模
- **B** 把 padding token 的注意力权重设为零，使它们不贡献到上下文向量
- **C** 替代 dropout
- **D** 编码位置

<details>
<summary>查看答案与解析</summary>

**答案**　B

对 padding（或解码器中的未来 token）做 masking，防止 softmax 把权重分散到无效位置上。

</details>


[返回本课](docs/zh.md)
