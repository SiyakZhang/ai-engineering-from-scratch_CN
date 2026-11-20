# 边缘推理 —— Apple Neural Engine、Qualcomm Hexagon、WebGPU/WebLLM、Jetson · 自测

每题先选答案，再展开解析。

## 1. 按本课所述，使移动端 LLM 推理慢于数据中心的核心约束是什么？

- **A** 内存带宽（移动 DRAM 为 50-90 GB/s，对比 HBM3 的 2-3 TB/s）
- **B** 计算吞吐量
- **C** 存储容量
- **D** Wi-Fi 延迟

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 2. 为什么 Apple 的 Neural Engine 能避免 CPU-NPU 的拷贝开销？

- **A** Apple Silicon 采用统一内存（unified memory）—— CPU 和 ANE 共享同一个内存池
- **B** Core ML 禁用了 KV 缓存
- **C** 它使用 PCIe 5.0
- **D** 它在拷贝前把权重转码为 FP4

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 3. 本课为浏览器中的 WebGPU + WebLLM 推荐哪种量化格式？

- **A** NVFP4
- **B** GGUF Q4_K_M
- **C** FP8
- **D** 通过 mlc_llm convert_weight 编译的 Q4 MLC（q4f16_1）

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 4. 本课报告 2026 年 WebGPU 在移动端的覆盖率大约是多少？

- **A** 在所有浏览器上达到 100%
- **B** 约 70-75%，其中 Firefox Android 仍在追赶
- **C** 仅 iOS Safari
- **D** 不到 10%

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 5. 为什么在一台典型手机上保持 128K 上下文不切实际？

- **A** Tokenizer 在超过 8K 时会失败
- **B** WebGPU 将上下文上限设为 4K
- **C** iOS 禁止长上下文
- **D** 模型权重加上 32K token 的 KV 缓存再加上操作系统开销，很容易超出 8 GB 内存预算

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 6. 为什么语音被强调为边缘推理的杀手级应用？

- **A** 语音模型总能塞进 50 MB
- **B** 语音只在 WebAssembly 中运行
- **C** 语音模型不需要 KV 缓存
- **D** 语音 agent 对延迟敏感（首 token < 500 ms），而本地推理能完全消除网络延迟

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>


[返回本课](docs/zh.md)
