# AI 网关 —— LiteLLM、Portkey、Kong AI Gateway、Bifrost · 自测

每题先选答案，再展开解析。

## 1. 本课中 AI 网关的核心角色是什么？

- **A** 一个仅做日志的 sidecar
- **B** 一个用于检索的向量数据库
- **C** 一个模型微调服务
- **D** 一个位于应用与模型供应商之间的进程，把路由、回退、重试、限流、密钥引用、可观测性和护栏整合到同一个 API 之后

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 2. Kong 的基准测试报告 LiteLLM 的规模天花板是多少？

- **A** LiteLLM 无法被基准测试
- **B** 它在 50 RPS 时见顶
- **C** 它在超过 10k RPS 后仍线性扩展
- **D** 它在约 2000 RPS 附近崩溃，占用 8 GB 内存，并在持续负载下出现级联故障

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 3. 按 Kong 在同等 CPU 上的基准测试，Kong AI Gateway 比 Portkey 和 LiteLLM 快多少？

- **A** 大约快 10% 和 20%
- **B** 比两者都慢
- **C** 比 Portkey 快 228%，比 LiteLLM 快 859%
- **D** 完全相同

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 4. 本课把哪个网关定位为延迟开销 20-40 ms、聚焦护栏 / PII 脱敏 / 越狱检测？

- **A** Portkey
- **B** Kong AI Gateway
- **C** Cloudflare AI Gateway
- **D** LiteLLM

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 5. 本课认为自托管与托管网关之间做决策的决定性因素（forcing function）是什么？

- **A** 每请求成本
- **B** 支持的供应商数量
- **C** 数据驻留（data residency）要求
- **D** 网关是否开源

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 6. 当 SLA 为 TTFT P99 < 100 ms 时，哪些网关能保持在预算之内？

- **A** 仅 LiteLLM
- **B** 仅 Portkey
- **C** Kong（约 3-8 ms）或 Cloudflare/Vercel 边缘网关（约 1-3 ms）；Portkey 在 20-40 ms 太重了
- **D** 任何网关

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>


[返回本课](docs/zh.md)
