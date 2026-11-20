# 分离式 Prefill/Decode —— NVIDIA Dynamo 与 llm-d · 自测

每题先选答案，再展开解析。

## 1. 为什么 prefill 和 decode 想要不同的最优 GPU 配置？

- **A** decode 需要更多网络带宽
- **B** 它们使用不同的模型权重
- **C** prefill 必须跑在 AMD 上，decode 必须跑在 NVIDIA 上
- **D** prefill 在矩阵乘吞吐上是计算受限的；decode 在 HBM 带宽上是内存受限的，因此把它们放在一起会浪费其中一种资源

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 2. NVIDIA Dynamo 使用什么传输方式在 prefill 池与 decode 池之间搬运 KV 缓存？

- **A** 仅 gRPC 双向流
- **B** 纯 HTTP
- **C** NIXL（可用时走 RDMA/InfiniBand，回退到 TCP）
- **D** NFS 上的共享文件系统

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 3. 按本课所述，什么情况下分离（disaggregation）不划算？

- **A** prompt 不到 512 token、输出不到 200 token 时，KV 传输税会盖过收益
- **B** 带共享系统提示的多租户服务
- **C** Blackwell 上的 MoE 工作负载
- **D** 带 8K+ 前缀的 RAG

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 4. Dynamo 与 llm-d 的核心架构差异是什么？

- **A** Dynamo 要求 AMD，llm-d 要求 NVIDIA
- **B** Dynamo 跑在 CPU 上，llm-d 跑在 GPU 上
- **C** Dynamo 是凌驾于 vLLM/SGLang/TRT-LLM 之上的编排器；llm-d 是 Kubernetes 原生的，把 prefill/decode/router 作为相互独立的 Service
- **D** Dynamo 是开源的，llm-d 是闭源的

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 5. Dynamo 的哪些组件会为达成某个 SLO 而自动调优 prefill:decode 比例？

- **A** Sidecar 代理与 Envoy 过滤器
- **B** Marlin 内核
- **C** Planner Profiler 与 SLA Planner
- **D** Cluster Autoscaler

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 6. 分离与 Phase 17 · 11 的缓存感知路由如何相互配合？

- **A** 缓存感知路由器可以把请求落到已经持有其前缀的 decode 池上；未命中时则流经 prefill -> decode，因此两者相辅相成
- **B** 它们是互斥的
- **C** 分离会完全禁用 KV 缓存复用
- **D** 缓存感知路由仅适用于同机部署（colocated）的服务

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>


[返回本课](docs/zh.md)
