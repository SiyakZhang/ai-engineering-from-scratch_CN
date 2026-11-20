# 采样方法 · 自测

每题先选答案，再展开解析。

## 1. temperature < 1.0 对语言模型的输出分布有什么影响？

- **A** 使分布更尖锐，让概率最高的 token 更有可能被选中
- **B** 移除除最高项之外的所有 token
- **C** 使分布更均匀（更随机）
- **D** 对输出没有影响

<details>
<summary>查看答案与解析</summary>

**答案**　A

temperature < 1.0 会把 logits 除以一个小于 1 的数，从而放大 logits 之间的差异。经过 softmax 后，概率最高的 token 占据更大的份额。temperature 趋近于 0 时即为贪心（argmax）解码。

</details>

## 2. top-k 与 top-p（核）采样之间的关键区别是什么？

- **A** top-k 比 top-p 更快
- **B** top-k 作用于 logits，而 top-p 作用于概率
- **C** top-k 保留固定数量的 token；top-p 根据累积概率保留可变数量的 token
- **D** top-p 只在 temperature = 1.0 时有效

<details>
<summary>查看答案与解析</summary>

**答案**　C

无论概率分布如何，top-k 总是恰好保留 k 个 token。top-p 自适应地保留累积概率超过 p 的最小 token 集合。当模型有信心时，top-p 保留很少的 token；当不确定时，则保留很多。

</details>

## 3. 为什么无法对标准采样操作 z ~ N(mu, sigma^2) 进行反向传播？

- **A** 采样操作是非确定性的，对 mu 和 sigma 没有良定义的导数
- **B** 梯度始终恰好为零
- **C** 正态分布没有梯度
- **D** PyTorch 不支持正态分布

<details>
<summary>查看答案与解析</summary>

**答案**　A

采样引入了一个随机不连续性——你无法为一次随机抽样计算 d(样本)/d(mu)。重参数化技巧通过把它写成 z = mu + sigma * epsilon（其中 epsilon ~ N(0,1)）来解决这一问题，使 z 成为 mu 和 sigma 的确定性、可微函数。

</details>

## 4. 在 Metropolis-Hastings MCMC 中，如果提议分布的标准差设得过大会发生什么？

- **A** 平稳分布变为均匀分布
- **B** 大多数提议落在低概率区域而被拒绝，因此链几乎不动
- **C** 预热期变为零
- **D** 链收敛更快，因为它迈出更大的步子

<details>
<summary>查看答案与解析</summary>

**答案**　B

当提议标准差很大时，提议的点远离当前位置，很可能落在低概率区域。这些提议会被拒绝，导致链卡在当前点不动。对于高维高斯提议，最优接受率约为 23%。

</details>

## 5. 在拒绝采样中，随着目标分布维度的增加，接受率会怎样？

- **A** 在所有情况下它都趋近于 50%
- **B** 它指数级下降，因为大部分提议体积都被拒绝
- **C** 它增大，因为有更多维度可供接受
- **D** 无论维度如何，它保持恒定

<details>
<summary>查看答案与解析</summary>

**答案**　B

在高维中，提议分布与目标分布重叠的体积呈指数级缩小。上界 M 增大，接受率（1/M）呈指数级下降。这就是拒绝采样面临的维度灾难。

</details>


[返回本课](docs/zh.md)
