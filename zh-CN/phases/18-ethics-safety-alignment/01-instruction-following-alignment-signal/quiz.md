# 把「遵循指令」当作对齐信号 · 自测

每题先选答案，再展开解析。

## 1. 为什么一个原始的预训练语言模型在面对「写一个反转列表的 Python 函数」时，常常回以另一个 prompt 而非代码？

- **A** 它被训练来续写网页风格的文本，而在那里 prompt 之后往往跟着更多 prompt
- **B** 不经过微调它无法表示函数签名
- **C** 它的词表里缺少 Python token
- **D** 它的温度默认为零

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 2. InstructGPT 的奖励模型在成对偏好标签上使用哪种损失？

- **A** 对标注者分数的均方误差
- **B** Bradley-Terry：-log sigmoid(r(x, y_w) - r(x, y_l))
- **C** 预测奖励与真实奖励之间的交叉熵
- **D** 带固定 margin 的 hinge loss

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 3. InstructGPT 第 3 阶段中的 KL 惩罚主要防范什么？

- **A** 优化器找到能利用奖励模型漏洞的对抗性高奖励字符串
- **B** PPO 梯度更新中的数值不稳定
- **C** 采样期间上下文窗口溢出
- **D** 对 tokenizer 统计量的灾难性遗忘

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 4. PPO-ptx 在 RL 目标中混入预训练梯度，是为了缓解什么问题？

- **A** 对齐税（alignment tax）：在 RLHF 未针对的基准上出现回退
- **B** 奖励模型在 PPO 期间发生漂移
- **C** SFT 与 RM 之间的 tokenizer 不匹配
- **D** KL 项变为负值

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 5. 一个 1.3B 的 InstructGPT 约有 70% 的概率被偏好于 175B 的基础 GPT-3。这对对齐与能力说明了什么？

- **A** 对齐是与能力不同的一个维度，而基础模型设定了能力下限
- **B** 在规模化下，能力与对齐是同一个维度
- **C** 偏好率高于 50% 就证明了代理奖励等同于人类价值观
- **D** 更大的基础模型总会输给小的对齐模型

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 6. InstructGPT 中的奖励模型是从以下哪一项初始化而来的？

- **A** 把 LM head 替换为标量 head 的 SFT 模型
- **B** 一个单独的 encoder-only transformer
- **C** 保留 LM head 的基础预训练模型
- **D** 一个无预训练的随机标量回归器

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>


[返回本课](docs/zh.md)
