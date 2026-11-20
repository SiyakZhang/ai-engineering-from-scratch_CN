# 生产环境中的 EAGLE-3 Speculative Decoding · 自测

每题先选答案，再展开解析。

## 1. 为什么推测解码（speculative decoding）能利用普通 decode 中存在的一个空隙？

- **A** decode 比 prefill 需要更多的网络带宽
- **B** decode 是计算受限的，所以增加算力是免费的
- **C** decode 无法从批处理中获益
- **D** decode 是内存受限的，所以 GPU 大部分时间都在空闲等待从 HBM 读取权重

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 2. 接受率 alpha 衡量的是什么？

- **A** decode 期间使用的 GPU 显存比例
- **B** draft 模型提议的 token 中被目标模型接受的比例
- **C** KV 缓存的命中率
- **D** draft 模型带来的延迟开销

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 3. 相比 EAGLE-2，EAGLE-3 改变了什么，使其在通用对话上把 alpha 推到大约 0.6-0.8？

- **A** draft head 是在多个目标层上训练的，而不仅仅是最后一层
- **B** 它完全移除了 verify 步骤
- **C** 它使用同系列的全尺寸 draft 模型
- **D** 它运行在 CPU 而非 GPU 上

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 4. 本课指出，在大多数 2026 年硬件上、高并发场景下，alpha 大约低于多少时推测解码就会变成净负收益？

- **A** 0.95
- **B** 0.85
- **C** 0.55
- **D** 0.05

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 5. 在打开 EAGLE-3 之后，即使平均 ITL 下降了，你也应该最密切关注哪个指标？

- **A** 冷启动时间
- **B** 平均端到端（E2E）延迟
- **C** P99 ITL，因为被拒绝的 draft 导致的双趟（two-pass）处理在满批次下可能被串行化
- **D** GPU 显存利用率

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 6. 按本课所述，为什么在 2026 年的 vLLM 中推测解码是按需开启（而非默认）的？

- **A** 它只在 Blackwell GPU 上工作
- **B** 接受率取决于工作负载，未测量 alpha 就开启它是一种生产反模式
- **C** 它需要单独的许可证
- **D** 它与 PagedAttention 不兼容

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>


[返回本课](docs/zh.md)
