# Cross-Attention 融合 · 自测

每题先选答案，再展开解析。

## 1. 在视觉-语言建模里，early fusion 和 late fusion 在运作上有什么区别？

- **A** early fusion 把图像和文本 token 拼成一个序列；late fusion 让它们分开，在每个 block 通过 cross-attention 桥接
- **B** early fusion 是不允许的
- **C** early fusion 在挂钟时间上先跑
- **D** late fusion 占更多内存

<details>
<summary>查看答案与解析</summary>

**答案**　A

Chameleon 和 Emu3 是 early-fusion；Flamingo 和 BLIP-2 是 late-fusion。这个架构选择会改变 mask 的形状和 KV caching。

</details>

## 2. 在一个同时有 self-attention 和 cross-attention 的 decoder block 里，哪个用 causal mask？

- **A** 两个都用
- **B** 两个都不用
- **C** 只有 self-attention 用；图像是完全可见的，cross-attention 没有时序顺序
- **D** 只有 cross-attention 用

<details>
<summary>查看答案与解析</summary>

**答案**　C

文本生成是自回归的，所以文本 self-attention 是 causal 的。图像 token 在任何文本被解码之前就全部可见。

</details>

## 3. 为什么 cross-attention 的 KV cache 每张图只构建一次？

- **A** PyTorch 要求必须缓存
- **B** 缓存能省磁盘空间
- **C** 它能避免用 GPU
- **D** 图像的 key 和 value 在文本解码过程中不会变，所以把 memory 投影一次、在所有解码步里复用这个 K 和 V，就是整个推理加速的关键

<details>
<summary>查看答案与解析</summary>

**答案**　D

视觉编码器只跑一次，它的 KV projection 只算一次，每个文本 token 都白嫖这份缓存。

</details>

## 4. 文本长度 Nt=10、图像长度 Nv=197、hidden=256 时，cross-attention 的输出形状是什么？

- **A** (B, 207, 256)
- **B** (B, 197, 256)
- **C** (B, 10, 256)
- **D** (B, 10, 197)

<details>
<summary>查看答案与解析</summary>

**答案**　C

cross-attention 的输出形状跟着 query 流走，所以无论 key 多长，输出都是 (B, Nt, hidden)。

</details>

## 5. 为什么 cross-attention 上不加 mask？

- **A** PyTorch 不支持 cross mask
- **B** mask 总会导致 NaN
- **C** 图像在文本生成开始前就完全可见；每个文本位置都可以 attend 到每个 patch
- **D** mask 太费算力

<details>
<summary>查看答案与解析</summary>

**答案**　C

图像 patch 没有时序顺序，也没有要防的信息泄露，所以 cross-attention 看得到整张图。

</details>

## 6. 想恢复 Flamingo 风格的训练稳定性，你会加哪个扩展？

- **A** 去掉 FFN
- **B** 只用一个 attention 头
- **C** 在 cross-attention 残差上插一个学出来的 tanh 门，让模型能从纯文本行为起步、逐渐长进图像流
- **D** 去掉 self-attention 层

<details>
<summary>查看答案与解析</summary>

**答案**　C

Flamingo 的 tanh 门从零起步，初始化时恢复纯文本行为，给模型一个平滑过渡到 cross-attention 的坡道。

</details>


[返回本课](docs/zh.md)
