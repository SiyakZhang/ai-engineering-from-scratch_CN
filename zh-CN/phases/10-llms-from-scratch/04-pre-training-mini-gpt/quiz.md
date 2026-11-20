# 预训练一个 Mini GPT（1.24 亿参数） · 自测

每题先选答案，再展开解析。

## 1. GPT 在预训练期间使用什么训练目标？

- **A** 下一个 token 预测：给定前面的 token，预测下一个
- **B** 掩码语言建模（预测被掩盖的 token）
- **C** 图文对齐
- **D** 句子分类

<details>
<summary>查看答案与解析</summary>

**答案**　A

GPT 是一个因果（自回归）语言模型，用下一个 token 预测来训练。给定 token [t1, t2, ..., tn]，它学习预测 tn+1。损失是预测的下一个 token 与真实下一个 token 之间的交叉熵。

</details>

## 2. GPT-2 Small（124M）有多少个 transformer 层、attention 头和 embedding 维度？

- **A** 6 层，6 个头，512 维
- **B** 24 层，16 个头，1024 维
- **C** 48 层，25 个头，1600 维
- **D** 12 层，12 个头，768 维

<details>
<summary>查看答案与解析</summary>

**答案**　D

GPT-2 Small 有 12 个 transformer 层，每层 12 个 attention 头，以及 768 维的 embedding。这个架构有 1.24 亿参数，可以在单张 GPU 上几小时内训练完成。

</details>

## 3. 因果 attention mask 在 GPT 中起什么作用？

- **A** 它阻止每个 token 注意到未来的 token，确保模型只能用过去的上下文做预测
- **B** 它减少训练时的内存占用
- **C** 它掩盖掉低置信度的 attention 分数
- **D** 它阻止对填充 token 的注意

<details>
<summary>查看答案与解析</summary>

**答案**　A

因果 mask 是一个三角矩阵，在 softmax 之前把未来位置设为负无穷。位置 5 的 token 可以注意位置 1-5，但不能注意 6 及之后。这确保模型从左到右生成 token。

</details>

## 4. 「温度」（temperature）在文本生成中控制什么？

- **A** 生成的 token 数量
- **B** token 选择的随机性：温度越低输出越确定，越高输出越多样
- **C** 模型的置信度阈值
- **D** 生成速度

<details>
<summary>查看答案与解析</summary>

**答案**　B

温度在 softmax 之前对 logits 做除法。温度=0.1 会让分布非常尖锐（近乎确定）。温度=1.0 是训练分布。温度>1.0 会把分布拉平，增加随机性。

</details>

## 5. 为什么预训练需要的算力远多于微调？

- **A** 微调不使用梯度
- **B** 预训练使用不同的架构
- **C** 预训练要从零开始处理数万亿 token 来学习通用语言模式，而微调只是在数千个样本上调整一个已有能力的模型
- **D** 预训练使用更大的批次

<details>
<summary>查看答案与解析</summary>

**答案**　C

预训练从随机权重出发，在数万亿 token 上构建全部语言知识。微调则从这些学到的权重出发，在一个小得多的数据集（数千到数百万个样本）上进行调整。

</details>


[返回本课](docs/zh.md)
