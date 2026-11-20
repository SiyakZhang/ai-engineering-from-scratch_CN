# 水印 —— SynthID、Stable Signature、C2PA · 自测

每题先选答案，再展开解析。

## 1. Kirchenbauer 式（SynthID-text）的 token 水印如何嵌入信号？

- **A** 通过修改 prompt 模板
- **B** 通过插入一个隐藏的 HTML 注释
- **C** 在每个解码步对前 K 个 token 做哈希，把词表划分为绿/红集合并使采样偏向绿集合；检测时通过 z 分数统计绿 token 数量
- **D** 通过用公钥加密输出

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 2. 文本水印面对改写（paraphrase）的主要局限是什么？

- **A** 对文本重新措辞或改写会破坏绿 token 的统计信号
- **B** 改写会增强水印
- **C** 改写只影响图像水印
- **D** 它们实际上能在改写后存活

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 3. Stable Signature（Fernandez 等人，ICCV 2023）做什么？

- **A** 用私钥对元数据签名
- **B** 在上传时用 C2PA 对图像签名
- **C** 在图像角落添加可见水印
- **D** 微调潜在扩散解码器，使每张生成图像都携带一条固定嵌入消息，可从潜在表示中检测出

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 4. 2024 年 5 月的「Stable Signature is Unstable」结果证明了什么？

- **A** 该水印仅在 JPEG 压缩下失效
- **B** 该水印被证明不可伪造
- **C** 该水印需要 C2PA 才能工作
- **D** 对解码器进行生成后微调可在保持图像质量的同时移除水印，削弱了其对抗鲁棒性

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 5. C2PA 元数据与水印如何互补？

- **A** 它们可以互换
- **B** C2PA 完全取代了水印
- **C** 水印由与 C2PA 相同的密钥签名
- **D** 元数据可被剥除但携带丰富的溯源链；水印能在转码中存活但携带的比特很少；分层叠加，二者提供一套可用的溯源叙事

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 6. 为什么「没有 SynthID 信号」不能证明真实性（人类起源）？

- **A** 因为 SynthID 是闭源的
- **B** 因为 SynthID 只对 Gemini 输出有效
- **C** 因为 SynthID 总是在人类文本上产生假阳性
- **D** 因为 SynthID 只为启用了 SynthID 的模型的生成内容打水印；任何未启用 SynthID 的模型产出的内容默认就没有水印

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>


[返回本课](docs/zh.md)
