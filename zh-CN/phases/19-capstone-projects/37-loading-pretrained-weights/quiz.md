# 加载预训练权重 · 自测

每题先选答案，再展开解析。

## 1. loader 为什么需要一张名字映射表？

- **A** 发布的 GPT-2 权重用的名字是 wte、wpe、h.N.attn.c_attn 这种；本地模型用的是 tok_embed、pos_embed、blocks.N.attn.qkv 这种；loader 负责把一套名字翻译成另一套
- **B** safetensors 文件是加密的
- **C** 预训练 tensor 和本地参数共享相同名字
- **D** PyTorch 要求的

<details>
<summary>查看答案与解析</summary>

**答案**　A

两套命名约定来自不同的历史；映射表就是一个按层展开的字典。

</details>

## 2. conv1d transpose 是什么，哪些 tensor 需要它？

- **A** 只有 LayerNorm 的 scale
- **B** 只有 embedding
- **C** 所有 weight tensor
- **D** 发布的 GPT-2 把 c_attn、c_proj 和 c_fc 的权重存成 TensorFlow conv1d layout，与 nn.Linear.weight 期望的布局互为转置；loader 在赋值时对它们调用 .t()

<details>
<summary>查看答案与解析</summary>

**答案**　D

三种后缀需要转置；bias 和 LayerNorm 的 shape 本来就是对的。

</details>

## 3. 为什么 LM head 不在 safetensors 文件里？

- **A** 它在运行时由 logits 计算得到
- **B** weight tying：LM head 和 token embedding (wte) 共享存储，所以加载 wte 后再设置 lm_head.weight = tok_embed.weight 就恢复了 head
- **C** 它太大了
- **D** 它从单独的文件加载

<details>
<summary>查看答案与解析</summary>

**答案**　B

在 wte 加载完成后设置 lm_head.weight = tok_embed.weight 恢复别名；拷贝则会让参数量翻倍。

</details>

## 4. loader 在 shape 不匹配时怎么处理？

- **A** 截断较大的 tensor
- **B** 对较小的 tensor 做 padding
- **C** 把不匹配的信息记录到 LoadReport.shape_mismatch 中，拒绝赋值，保持本地参数不变
- **D** 让进程崩溃

<details>
<summary>查看答案与解析</summary>

**答案**　C

加载到一半的模型是无声的失败机器；拒绝赋值才能让报告保持诚实。

</details>

## 5. 为什么 demo 用的 stub fixture 不是真正的 GPT-2 下载文件？

- **A** 真实权重是加密的
- **B** safetensors 无法存储大 tensor
- **C** demo 必须能离线快速运行；stub 用了和预训练完全一致的命名约定，所以 loader 走的代码路径完全相同，换成真实文件对 loader 没有任何影响
- **D** 真实文件不是 safetensors 格式

<details>
<summary>查看答案与解析</summary>

**答案**　C

相同的代码路径，更小的 payload；loader 在两种文件上都一样工作。

</details>

## 6. 为什么在加载前后各生成一次样本？

- **A** 测量推理速度
- **B** 预热 GPU 缓存
- **C** 设置随机种子
- **D** 如果加载后的样本和加载前一模一样，说明加载没有改变模型，意味着映射静默地漏掉了每一个 tensor

<details>
<summary>查看答案与解析</summary>

**答案**　D

sanity generation 是最便宜的验证门：如果样本指纹没有变化，就能暴露出一次失败的加载——而这种失败光看 LoadReport 的摘要是抓不到的。

</details>


[返回本课](docs/zh.md)
