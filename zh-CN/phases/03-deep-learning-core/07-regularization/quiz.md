# 正则化 · 自测

每题先选答案，再展开解析。

## 1. 神经网络中的过拟合是什么？

- **A** 模型太小，学不了数据
- **B** 损失函数错了
- **C** 模型记住了训练数据而不是学到可泛化的模式，表现为训练准确率与测试准确率之间存在巨大差距
- **D** 模型训练太慢

<details>
<summary>查看答案与解析</summary>

**答案**　C

当模型达到高训练准确率但测试准确率很差时，就发生了过拟合。它记住了训练数据的噪声，而不是学到了底层模式。

</details>

## 2. dropout 如何对神经网络进行正则化？

- **A** 它从训练数据中移除异常值
- **B** 它永久移除表现最差的神经元
- **C** 它降低学习率
- **D** 它在训练期间随机把神经元置零，迫使网络学习冗余的表示

<details>
<summary>查看答案与解析</summary>

**答案**　D

在每次前向传播中，dropout 以概率 p 随机把神经元输出置为零。这防止了协同适应（神经元依赖特定的其他神经元），并等价于训练一个由 2^N 个子网络组成的集成。

</details>

## 3. 为什么 transformer 使用 LayerNorm 而不是 BatchNorm？

- **A** LayerNorm 对每个样本跨特征做归一化（与批次无关），这适用于可变的序列长度和较小的批大小
- **B** LayerNorm 是更晚发明的
- **C** BatchNorm 会导致梯度爆炸
- **D** LayerNorm 计算更快

<details>
<summary>查看答案与解析</summary>

**答案**　A

BatchNorm 依赖批次统计量，在小批量时这些统计量带噪声，在批大小为 1 时（生成时常见）则毫无意义。LayerNorm 在每个样本内部跨特征做归一化，与批大小无关。

</details>

## 4. RMSNorm 和 LayerNorm 之间的关键区别是什么？

- **A** RMSNorm 增加了可学习参数
- **B** RMSNorm 跳过减均值这一步，只除以均方根，在准确率相当的情况下提速约 10%
- **C** RMSNorm 只对 CNN 有效
- **D** RMSNorm 使用批次统计量

<details>
<summary>查看答案与解析</summary>

**答案**　B

RMSNorm 去掉了 LayerNorm 中的减均值步骤，该步骤对准确率贡献甚微却增加了计算量。LLaMA、Mistral 以及大多数现代大语言模型都使用 RMSNorm 来获得这种效率提升。

</details>

## 5. 在 PyTorch 中运行推理前调用 model.eval() 为什么至关重要？

- **A** 它释放 GPU 显存
- **B** 它禁用 dropout 并让 BatchNorm 改用运行统计量而非批次统计量，从而给出确定性的输出
- **C** 它加快计算
- **D** 它启用梯度计算

<details>
<summary>查看答案与解析</summary>

**答案**　B

如果不调用 model.eval()，dropout 会在推理时随机把神经元置零（导致输出随机波动），而 BatchNorm 会使用当前批次的统计量，而不是训练期间累积的稳定运行平均值。

</details>


[返回本课](docs/zh.md)
