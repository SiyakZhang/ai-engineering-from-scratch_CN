# 面向 LLM 的差分隐私 · 自测

每题先选答案，再展开解析。

## 1. (epsilon, delta) 差分隐私为一个随机算法 M 保证了什么？

- **A** M 被证明等价于一个非隐私算法
- **B** 对于任意相差一个样本的两个数据集和任意事件 S，P(M(D) in S) <= e^epsilon * P(M(D') in S) + delta，因此无法可靠地推断出任何单个个体的贡献
- **C** M 在噪声范围内是确定性的
- **D** M 永远不会记住任何训练数据

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 2. 以下哪一项不是 Abadi 等人 2016 所述 DP-SGD 的步骤？

- **A** 在步骤之间重新随机化模型的 tokenizer
- **B** 采样一个小批次并计算逐样本梯度
- **C** 把每个逐样本梯度裁剪到阈值 C
- **D** 对裁剪后的梯度求和，并加入按 sigma * C 缩放的高斯噪声

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 3. 为什么 LoRA + DP-SGD 是常见的 2025 年配置？

- **A** 它把 LoRA 用作 tokenizer
- **B** LoRA 在设计上会增大 epsilon
- **C** 对前沿模型做完整 DP-SGD 代价高得令人却步；LoRA 把梯度更新限制在一个小适配器上，减少逐样本梯度存储，同时仍能为该适配器提供 DP 保证
- **D** LoRA 消除了对 accountant 的需求

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 4. 2025 年 3 月的审计（arXiv:2503.06808）如何化解「金丝雀-MIA」与「训练数据提取」之间的张力？

- **A** 它完全消除了对金丝雀的需求
- **B** 它证明 DP-SGD 没有必要
- **C** 它表明两者测量的是不同的东西：对插入金丝雀做 MIA 会低估记忆程度，因为金丝雀并非那些「最易被提取、对隐私真正重要」的样本
- **D** 它表明两者测量同一种属性

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 5. PMixED（arXiv:2403.15638）提供了什么作为 DP 训练的替代方案？

- **A** 推理时差分隐私：在 next-token 分布上用专家混合（mixture of experts）加聚合噪声；完全避免 DP 训练
- **B** 一种仅凭 epsilon-delta 核算就能计算 epsilon 的方法
- **C** 一个用于 Renyi DP 的新 accountant
- **D** 一个更快的 DP-SGD 变体

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 6. 「通过 LLM 反馈进行差分隐私逆转」攻击是什么？

- **A** 一种把 epsilon 重置为零的方法
- **B** 一种针对 tokenizer 熵的攻击
- **C** 一种针对金丝雀插入的对策
- **D** 把一个 DP 训练模型的置信度分数当作 oracle 来重新识别个体，即便输出本身并不直接泄露

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>


[返回本课](docs/zh.md)
