# 硬件专用推理编译——Blackwell 上的 FP8 与 NVFP4 · 自测

每题先选答案，再展开解析。

## 1. 在一个可比的 120B 级别工作负载上，本课报告的 Blackwell + TRT-LLM + Dynamo 与 H100 + vLLM 之间，每百万 token 的成本差距大约是多少？

- **A** 约 1.1 倍
- **B** 约 100 倍
- **C** 约 2 倍
- **D** 约 7 倍

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 2. 为什么本课建议在 Blackwell 上把 KV 缓存保持为 FP8 而非 NVFP4？

- **A** 目前还没有任何引擎支持 NVFP4 的 KV 缓存
- **B** FP8 比 FP4 占用更少的显存
- **C** KV 缓存跨越很宽的动态范围；FP4 量化会导致 attention 分数出现灾难性的精度损失
- **D** FP8 是 NVLink 5 唯一支持的精度

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 3. TRT-LLM 利用了 Blackwell 的哪个特性，使模型加载时无需经过训练后转换步骤？

- **A** 通过 bitsandbytes 实现的 INT2 权重
- **B** FP64 attention
- **C** 模型提供方随发布即提供的 Day-0 FP4 权重
- **D** BF16 KV 缓存

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 4. 按本课所述，选择 TRT-LLM 技术栈的主要权衡是什么？

- **A** 它无法服务 MoE 模型
- **B** 它只能在小规模下工作
- **C** 它要求完全自主的修复
- **D** 它把你锁定在 NVIDIA 硬件上 —— 不支持 AMD、不支持 Intel、不支持 ARM

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 5. 本课把哪种精度组合描述为典型的 Blackwell 配置？

- **A** 权重 NVFP4，激活 NVFP4，KV 缓存 FP8，attention 累加器 FP32
- **B** 权重 FP4，KV 缓存 FP4，attention 用 INT8
- **C** 全部使用 BF16
- **D** 权重 INT8，激活 FP32，KV 缓存 INT4

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 6. 对于推理密集型工作负载，若 NVFP4 权重转换会使 MATH 准确率下降几个点，本课建议怎么做？

- **A** 禁用推测解码
- **B** 针对每个模型在你自己的评测集上验证任务质量；团队通常使用 FP8 权重 + FP4 激活，或继续在 H200 上全程使用 FP8
- **C** 切换到 AMD MI300X
- **D** 无论如何都上 NVFP4，因为成本优势压倒一切

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>


[返回本课](docs/zh.md)
