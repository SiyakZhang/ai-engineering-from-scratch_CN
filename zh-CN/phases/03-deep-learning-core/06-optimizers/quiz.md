# 优化器 · 自测

每题先选答案，再展开解析。

## 1. 动量（momentum）在梯度下降中解决了什么问题？

- **A** 它消除了对学习率的需要
- **B** 它减少内存占用
- **C** 它防止过拟合
- **D** 它通过累积过去的梯度来抑制振荡，并在一致的方向上加速移动

<details>
<summary>查看答案与解析</summary>

**答案**　D

在狭窄的山谷中，梯度会横跨山谷振荡，而沿山谷前进却很慢。动量累积过去的梯度：一致的方向被放大，而振荡的方向相互抵消，从而带来更平滑、更快的收敛。

</details>

## 2. Adam 和 AdamW 之间的关键区别是什么？

- **A** AdamW 只对 transformer 有效
- **B** AdamW 把权重衰减直接施加到权重上，而不是通过梯度，从而实现正确的正则化
- **C** AdamW 不使用动量
- **D** AdamW 使用更高的学习率

<details>
<summary>查看答案与解析</summary>

**答案**　B

在 Adam + L2 中，自适应学习率会对每个参数以不同方式缩放正则化项。AdamW 把权重衰减与梯度更新解耦，无论梯度统计量如何都施加统一的收缩。

</details>

## 3. 为什么 Adam 在训练早期使用偏差校正？

- **A** 为了加快收敛
- **B** 矩估计被初始化为零，因此早期的值偏向零；校正补偿了这种冷启动
- **C** 为了防止过拟合
- **D** 为了裁剪大梯度

<details>
<summary>查看答案与解析</summary>

**答案**　B

在 beta1=0.9 的第 1 步，m_1 = 0.1 * 梯度（小了 10 倍）。除以 (1 - 0.9^1) = 0.1 可将其校正为实际梯度。约 50 步后这种校正就可忽略不计。

</details>

## 4. Adam 的标准默认超参数是什么？

- **A** lr=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8
- **B** lr=0.1, beta1=0.5, beta2=0.5
- **C** lr=0.0001, beta1=0.8, beta2=0.9
- **D** lr=0.01, beta1=0.99, beta2=0.99

<details>
<summary>查看答案与解析</summary>

**答案**　A

最初的 Adam 论文（Kingma & Ba, 2014）推荐 lr=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8。这些默认值对大多数问题都效果良好。

</details>

## 5. 训练 transformer 和大语言模型时，哪个优化器是现代默认选择？

- **A** 普通 SGD
- **B** 带动量的 SGD
- **C** RMSProp
- **D** AdamW

<details>
<summary>查看答案与解析</summary>

**答案**　D

AdamW（带解耦权重衰减的 Adam）被用于训练 BERT、GPT、LLaMA 以及几乎所有现代 transformer。它把自适应学习率与正确的权重衰减正则化结合在一起。

</details>


[返回本课](docs/zh.md)
