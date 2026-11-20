# 用 Projection Layer 做模态对齐 · 自测

每题先选答案，再展开解析。

## 1. 为什么视觉编码器产出的 token，文本 decoder 没法直接消费？

- **A** 图像 token 活在编码器视觉预训练时学到的一组基里，跟 decoder 的词向量没有任何对应关系
- **B** 图像 token 太短
- **C** 它们是不同的文件格式
- **D** 图像 token 被加密了

<details>
<summary>查看答案与解析</summary>

**答案**　A

两个编码器各自学出独立的基，需要一个桥接模块把它们对齐到共享空间。

</details>

## 2. 为什么实践中两层 MLP 就足以做 modality 对齐？

- **A** 单层 projection 是被禁止的
- **B** 更深的 projection 是不允许的
- **C** PyTorch 要求必须两层
- **D** 在两个线性 projection 之间夹一个非线性拐点（GELU），经验上就足以把 CLIP 风格的特征和文本 embedding 对齐

<details>
<summary>查看答案与解析</summary>

**答案**　D

LLaVA 及其后续工作都用这个两层 MLP，因为非线性能修正单个线性层搞不定的曲率失配。

</details>

## 3. 为什么在这个对齐阶段要冻结视觉编码器？

- **A** PyTorch 不支持训练编码器
- **B** 冻结意味着挂钟时间更短
- **C** 编码器是空的
- **D** 8600 万参数的编码器没法在一个小型 mock 语料上重训；单独 130 万参数的 projection 才轻到能在几分钟内对齐

<details>
<summary>查看答案与解析</summary>

**答案**　D

冻结编码器和文本词表，让 projection 成为唯一在学的东西，这正是所有基于 adapter 的 VLM 的运作形态。

</details>

## 4. 当两个向量方向相反时，cosine_alignment_loss(image_emb, text_emb) 返回什么？

- **A** 1.0
- **B** 0.0
- **C** 2.0
- **D** 无穷大

<details>
<summary>查看答案与解析</summary>

**答案**　C

loss 是 1 - cos(夹角)。反平行向量的 cos = -1，所以 loss 是 1 - (-1) = 2.0。

</details>

## 5. 为什么要用 CLS pooling，从 197 个 token 里产出单个图像级向量？

- **A** patch token 没用上
- **B** 每个样本的 caption 是一个向量，所以图像侧也需要一个向量；CLS token 正是编码器内置的图像摘要
- **C** PyTorch 会自动把 token 求和
- **D** 它能省磁盘空间

<details>
<summary>查看答案与解析</summary>

**答案**　B

对齐是一个图像向量对一个 caption 向量；CLS pooling 不加任何额外参数就能产出那个图像向量。

</details>

## 6. 哪个生产系统跟第 60 课的模式最直接对应？

- **A** PaLM
- **B** AlphaFold
- **C** LLaVA 1.5：冻结视觉编码器、冻结 LLM，只训一个两层 MLP projection
- **D** Stable Diffusion

<details>
<summary>查看答案与解析</summary>

**答案**　C

LLaVA 第一阶段训练就是这样：冻结的编码器和 LM，加一个两层 MLP 桥接作为唯一可训练的部分。

</details>


[返回本课](docs/zh.md)
