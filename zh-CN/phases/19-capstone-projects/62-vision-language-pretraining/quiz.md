# Vision-Language 预训练 · 自测

每题先选答案，再展开解析。

## 1. 把 InfoNCE 和 LM loss 结合起来，训出的是哪两种各不相同的能力？

- **A** tokenization 和 detokenization
- **B** 排序（为一段 caption 找到对的图）和生成（为一张图写出 caption）
- **C** 压缩和解压
- **D** 速度和准确率

<details>
<summary>查看答案与解析</summary>

**答案**　B

InfoNCE 负责排序；LM loss 负责生成。CoCa、BLIP 等都在一次训练里把两者结合起来。

</details>

## 2. InfoNCE 里，一个 batch 有 N 对配对时，会形成多少正样本对和负样本对？

- **A** 1 个正样本对，N 个负样本对
- **B** N^2 个正样本对
- **C** N 个正样本对，N 个负样本对
- **D** 相似度矩阵对角线上 N 个正样本对，对角线外 N*(N-1) 个负样本对

<details>
<summary>查看答案与解析</summary>

**答案**　D

N 对匹配落在对角线上；对角线之外的一切都是负样本。

</details>

## 3. 为什么对比学习的 temperature 通常是个学出来的参数？

- **A** 学出来的 tau 在 GPU 上更快
- **B** 手动调很脆弱；让 tau 自己学，模型才能在训练中 embedding 尺度演变时找到合适的 softmax 尖锐度
- **C** 它能避免用 Adam
- **D** PyTorch 要求这样

<details>
<summary>查看答案与解析</summary>

**答案**　B

CLIP 引入了可学习的 log-tau，让对比 softmax 在 embedding 范数增长时仍然停在有用的区间。

</details>

## 4. 哪个子模块只从 LM loss 拿到梯度，而拿不到对比 loss 的梯度？

- **A** cross-attention decoder
- **B** MLP projector
- **C** 视觉编码器
- **D** 文本侧编码器

<details>
<summary>查看答案与解析</summary>

**答案**　A

对比 loss 碰不到 decoder；LM loss 碰不到文本侧的 mean-pool 编码器。

</details>

## 5. 在 LM cross-entropy 里 ignore_index=PAD_ID 起到什么作用？

- **A** 加密 pad token
- **B** 给 token 重新排序
- **C** 把 padding 位置从 loss 里屏蔽掉，这样模型不会因为预测 caption 结束之后的 token 而挨罚
- **D** 加快 loss 计算

<details>
<summary>查看答案与解析</summary>

**答案**　C

padding 位置不带任何信号；忽略它们能阻止 loss 去学预测 pad。

</details>

## 6. 为什么在合成数据上跑 50 步的 demo 就能算这一课完成了？

- **A** 真实数据会改变架构
- **B** 50 步是支持的上限
- **C** 这个 demo 证明梯度管路端到端通了；生产训练的形态完全一样，只是在真实数据上跑几百万步
- **D** 模型在 50 步就达到 state of the art

<details>
<summary>查看答案与解析</summary>

**答案**　C

demo 演示出的动态（两个 loss 都下降、没有 NaN、tau 稳定）跟一次十亿级图像训练会呈现的动态是一样的，只是规模放大了。

</details>


[返回本课](docs/zh.md)
