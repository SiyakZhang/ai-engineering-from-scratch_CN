# perplexity 与 calibration · 自测

每题先选答案，再展开解析。

## 1. 语言模型在测试语料上的 perplexity 为 1.0，意味着什么？

- **A** 语料是空的
- **B** 模型坏了
- **C** 模型在词表上是均匀分布的
- **D** 模型给每个真实 token 都赋了概率 1；它是个完美模型

<details>
<summary>查看答案与解析</summary>

**答案**　D

perplexity 等于 exp(平均负对数似然)。当每个 token 都拿到概率 1 时，NLL 为零，exp(0) 就是 1。

</details>

## 2. 为什么 harness 要求适配器返回的对数概率为非负？

- **A** 负对数概率按定义就是非负的；收到负值意味着适配器送来的是 log p，而不是 -log p
- **B** Numpy 遇到负值会崩
- **C** ECE 里的 bin 边界假定了正值
- **D** perplexity 对负值没有定义

<details>
<summary>查看答案与解析</summary>

**答案**　A

一个概率的 -log p 是非负的。负值是对契约的违背，会悄悄给出 perplexity < 1，而这是不可能的。

</details>

## 3. 期望校准误差（ECE）衡量的是什么？

- **A** 预测的交叉熵
- **B** softmax 输出的方差
- **C** 预测标签与真实标签之间的平均绝对距离
- **D** bin 级置信度与 bin 级准确率之间的平均差距，按 bin 大小加权

<details>
<summary>查看答案与解析</summary>

**答案**　D

ECE 按置信度把预测分到各个 bin，衡量每个 bin 里平均置信度与平均准确率的差距，再按 bin 大小加权。

</details>

## 4. 为什么实现里要在返回 ECE 值的同时还返回 populated_bins？

- **A** 当填充的 bin 太少、单个数字不可信时，它能给出信号
- **B** 画可靠性图（reliability diagram）需要它
- **C** numpy 需要它
- **D** 它是 Brier score 的分母

<details>
<summary>查看答案与解析</summary>

**答案**　A

填充的 bin 一少，ECE 就被噪声主导。报告填充数能让 runner 拒绝发布一个有误导性的单一数字。

</details>

## 5. Brier score 能捕捉到、而 ECE 捕捉不到的是什么？

- **A** 它直接惩罚局部失准，因为它就是每条预测的平方误差
- **B** 它算起来更快
- **C** 它只对二元结果有效
- **D** 它不需要真实标签

<details>
<summary>查看答案与解析</summary>

**答案**　A

ECE 只看每个 bin 的平均。Brier 对每条预测的误差取平方，所以能抓住那种同一个 bin 内部误差相互抵消的情况：bin 的平均值匹配了，但其中的预测单条都失准。

</details>

## 6. 为什么校准是按模型出报告，而不是按任务出指标？

- **A** 单个任务的预测太少，估不出 bin 统计量；报告是跨整个 eval 聚合的
- **B** 任务没有概率
- **C** ECE 需要 runner 知道模型架构
- **D** 校准按任务算太慢

<details>
<summary>查看答案与解析</summary>

**答案**　A

按任务做校准会被噪声主导。runner 先把所有任务的（置信度，是否正确）对汇集起来，再算 ECE、Brier 和可靠性图。

</details>


[返回本课](docs/zh.md)
