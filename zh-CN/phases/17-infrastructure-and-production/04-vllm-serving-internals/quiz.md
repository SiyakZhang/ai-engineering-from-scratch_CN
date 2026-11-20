# 推理服务引擎内部机制——PagedAttention、连续批处理与分块预填充 · 自测

每题先选答案，再展开解析。

## 1. 经典静态批处理在处理长度不一的请求时，主要问题是什么？

- **A** 为最长 prompt 和最长输出做 padding 会浪费显存，并让整个批次卡在最慢的序列上
- **B** 它只能用于 FP4
- **C** 每对 GPU 之间都必须有 NVLink
- **D** 它完全无法使用 GPU

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 2. PagedAttention 如何把 KV cache 碎片率从 60–80% 降到 4% 以下？

- **A** 把权重量化到 INT4
- **B** 按固定大小的 block（默认 16 个 token）分配 KV cache，并通过每条序列的 block table 引用
- **C** 把完整 prompt 放在 CPU 内存里
- **D** 完全禁用 KV cache

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 3. vLLM V1 scheduler 中定义 continuous batching 的不变量是什么？

- **A** 每个请求使用独立 GPU stream
- **B** 调度器每个请求只运行一次，批次永不变化
- **C** 调度器等待 10 ms 窗口凑满批次
- **D** 调度器每次 decode 迭代运行一次，移出完成序列并接纳等待序列

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 4. 混合负载下，chunked prefill 主要保护哪个延迟指标？

- **A** P99 token 间延迟（ITL）
- **B** 平均吞吐
- **C** 网络 RTT
- **D** 冷启动时间

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 5. vLLM v0.18.0 特性兼容性矩阵如何标记 speculative decoding 与 `--enable-chunked-prefill` 的组合？

- **A** 矩阵标记该组合兼容
- **B** 只有草稿模型推测兼容
- **C** 任何配置下都不能组合
- **D** 只有 EAGLE-1 草稿头兼容

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 6. 为什么 chunked prefill 单独看并不会提高平均吞吐？

- **A** 它更激进地压缩权重
- **B** 它底层使用 speculative decoding
- **C** 它与 decode 运行在不同 GPU 上
- **D** 它只减少 decode 抖动；实践中的吞吐收益来自长 prefill 期间仍让 decode 序列前进，而不是减少实际工作量

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>


[返回本课](docs/zh.md)
