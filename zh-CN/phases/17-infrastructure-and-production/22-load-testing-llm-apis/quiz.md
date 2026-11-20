# 压测 LLM API —— 为什么 k6 和 Locust 会骗你 · 自测

每题先选答案，再展开解析。

## 1. 基于 Locust 的 LLM 负载测试中的 GIL 陷阱是什么？

- **A** Locust 不支持 HTTP
- **B** Locust 需要 CUDA
- **C** 客户端侧的分词在 Python GIL 下运行，并排在请求生成之后排队，从而虚高了上报的 token 间延迟
- **D** Locust 只能在 Windows 上工作

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 2. prompt 同质化陷阱是什么？

- **A** 同质化的 prompt 总会拖慢服务器
- **B** 同质化的 prompt 需要流式传输
- **C** 循环使用同一个 prompt 会让前缀缓存看起来像是满并发 decode，从而虚高了上报的吞吐量
- **D** 从真实分布采样会低估长 prompt 的占比

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 3. 本课推荐哪四种负载模式？

- **A** 仅突发（burst）
- **B** 连续 10 天恒定 1 RPS
- **C** 稳态（steady-state）、爬坡（ramp）、尖峰（spike）、浸泡（soak）
- **D** 手动点击测试

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 4. 本课建议如何构建一个真实的 prompt 分布？

- **A** 用均值和标准差从真实分布中采样（例如 LLMPerf 的 --mean-input-tokens / --stddev-input-tokens），或回放真实流量
- **B** 每个请求用随机字符
- **C** 手写 5 个 prompt 然后打乱
- **D** 始终使用同一个 prompt 以最大化缓存命中

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 5. 哪种 2026 年的工具组合被定位为最适合 CI/CD 的 SLA 门禁和 Kubernetes 原生的分布式运行？

- **A** 仅 Vegeta
- **B** 仅 guidellm
- **C** 原版 Locust 2.43.3
- **D** k6 v2026.1.0 搭配 k6 Operator 1.0 GA（TestRun / PrivateLoadZone CRD）

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 6. 浸泡（soak）负载模式能捕捉哪种失败模式？

- **A** 冷启动长尾
- **B** 缓存驱逐风暴
- **C** Tokenizer 的 GIL 争用
- **D** 数小时内的内存泄漏、连接池漂移以及可观测性溢出

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>


[返回本课](docs/zh.md)
