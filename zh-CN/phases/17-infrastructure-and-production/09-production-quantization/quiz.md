# 生产量化 —— AWQ、GPTQ、GGUF K-quant、FP8、MXFP4/NVFP4 · 自测

每题先选答案，再展开解析。

## 1. 本课把哪种量化格式称为 CPU 和边缘服务的生产默认选择？

- **A** FP8
- **B** AWQ INT4
- **C** GGUF Q4_K_M / Q5_K_M
- **D** NVFP4

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 2. 当在 vLLM 中需要 multi-LoRA 时，本课为数据中心 GPU 服务挑选的格式是哪一种？

- **A** GGUF Q4_K_M
- **B** AWQ
- **C** 配合 Marlin 内核的 GPTQ
- **D** NVFP4

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 3. AWQ 中「我的模型现在只有 4 GB 了」这个陷阱是什么？

- **A** AWQ 只缩小权重；KV 缓存和激活是独立的，在生产批次规模下可能额外增加 30-50 GB
- **B** AWQ 实际上并不会缩小权重
- **C** AWQ 需要 INT8 的 KV 缓存
- **D** AWQ 与 vLLM 不兼容

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 4. 为什么用通用网页文本校准 AWQ 会损害领域模型？

- **A** 它只在 AMD GPU 上工作
- **B** 它会禁用 Marlin 内核
- **C** 它会增大模型尺寸
- **D** 算法在「该保护哪些权重」上做出了错误决策，从而拉低领域准确率（例如在 HumanEval 上掉几个 Pass@1 点）

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 5. 对于一个质量不容妥协的推理密集型工作负载，本课默认推荐哪种精度？

- **A** FP8 权重
- **B** NVFP4 权重
- **C** INT2 GGUF
- **D** GPTQ INT4

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 6. 本课指出 2026 年初 NVFP4 的哪个量化局限？

- **A** 尚不支持 LoRA
- **B** 无法与 FP8 KV 缓存组合使用
- **C** 在 H100 上不受支持
- **D** 只能在 CPU 上运行

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>


[返回本课](docs/zh.md)
