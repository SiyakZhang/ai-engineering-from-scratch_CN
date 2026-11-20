# 自托管推理服务选型——让引擎匹配硬件与规模 · 自测

每题先选答案，再展开解析。

## 1. 本课把哪个引擎选为开发笔记本上「一条命令」的默认选择？

- **A** vLLM
- **B** Ollama
- **C** TGI
- **D** llama.cpp

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 2. 2025 年的哪个事件使新项目不再默认选用 TGI？

- **A** TGI 放弃了 CUDA 支持
- **B** TGI 于 2025 年 12 月 11 日进入维护模式 —— 此后只做 bug 修复
- **C** TGI 被 Anthropic 收购
- **D** TGI 涨价了

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 3. 哪种硬件约束会强制使用 llama.cpp 并排除 vLLM / TRT-LLM？

- **A** Apple M4
- **B** AMD MI300X
- **C** NVIDIA Hopper
- **D** 仅 CPU（无加速器）

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 4. 得益于 RadixAttention，本课把哪个引擎定位为面向 agentic 多轮和前缀密集型工作负载？

- **A** SGLang
- **B** llama.cpp
- **C** Ollama
- **D** TGI

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 5. 本课推荐在相同的 GGUF 或 HF 权重上采用什么样的「开发到生产」流水线？

- **A** 开发用 Ollama，预发用 llama.cpp，生产用 vLLM（前缀密集型则用 SGLang）
- **B** 从头到尾只用 TRT-LLM
- **C** 处处都用 TGI
- **D** 开发用 Ollama，生产也用 Ollama

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 6. 为什么不建议在共享的生产环境中使用 Ollama？

- **A** 它只能在 Windows 上运行
- **B** 它无法加载 GGUF
- **C** 它是闭源的
- **D** Go 的 HTTP 序列化带来额外开销，并发管理比 vLLM 更简陋，且 OpenTelemetry 支持滞后

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>


[返回本课](docs/zh.md)
