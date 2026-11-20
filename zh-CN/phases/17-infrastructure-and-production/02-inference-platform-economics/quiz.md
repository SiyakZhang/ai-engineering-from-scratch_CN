# 推理平台经济学 —— Fireworks、Together、Baseten、Modal、Replicate、Anyscale · 自测

每题先选答案，再展开解析。

## 1. 本课用哪三个市场细分来组织 2026 年的推理供应商？

- **A** 开源、商业、混合
- **B** 单租户、多租户、本地部署（on-prem）
- **C** 免费、付费、企业版
- **D** 定制芯片、GPU 平台、API 优先的市场（marketplace）

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 2. 大约在多高的持续 GPU 利用率下，按分钟计费（Baseten、Modal）开始优于按 token 计费（Fireworks、Together）？

- **A** 5%
- **B** 90%
- **C** 60%
- **D** 30%

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 3. 哪个平台被描述为 Python 原生的 serverless，按秒计费，且预热后冷启动为 2-4 秒？

- **A** Anyscale
- **B** Modal
- **C** Baseten
- **D** Fireworks

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 4. Fireworks 在 LoRA 定价上有什么显著的差异化优势？

- **A** LoRA 请求需要单独的专用 GPU 合约
- **B** 用 LoRA 服务的请求比基础模型更贵
- **C** 用 LoRA 服务的请求按基础模型的每 token 费率计费
- **D** 完全不支持 LoRA

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 5. 对于一个受监管的医疗客户，需要 SOC 2 Type II、满足 HIPAA 要求的合规姿态以及专用 GPU，哪个平台最合适？

- **A** Baseten
- **B** Replicate
- **C** Together
- **D** Anyscale

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 6. 为什么本课认为在平台这一层，「定制引擎」的宣称大多只是营销上的暗讽？

- **A** vLLM 和 SGLang 大约占了生产环境开源推理的 80%，因此平台的差异化更多来自开发体验（DX）、成本归因和 SLA，而非引擎本身
- **B** 定制引擎从来不会超越 vLLM
- **C** 按 token 定价是唯一真正的差异化点
- **D** 所有定制引擎都是 TensorRT-LLM 的分支

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>


[返回本课](docs/zh.md)
