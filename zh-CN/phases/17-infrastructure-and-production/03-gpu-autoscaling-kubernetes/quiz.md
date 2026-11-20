# Kubernetes 上的 GPU 自动扩缩 —— Karpenter、KAI Scheduler、Gang Scheduling · 自测

每题先选答案，再展开解析。

## 1. HPA 默认通常基于哪个信号进行扩缩，而本课认为该信号对 vLLM 式的服务是失效的？

- **A** P99 TTFT
- **B** DCGM_FI_DEV_GPU_UTIL 占空比（duty cycle）
- **C** 队列深度（queue depth）
- **D** KV 缓存利用率

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 2. KAI Scheduler 中的 gang scheduling 主要防止什么问题？

- **A** 部分分配陷阱：8 块 GPU 中有 7 块空转等待第 8 块
- **B** GPU 显存碎片化
- **C** Tokenizer 的 GIL 争用
- **D** 冷启动延迟

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 3. 为什么 Karpenter 默认的 consolidationPolicy: WhenEmptyOrUnderutilized 对推理 GPU 池是危险的？

- **A** 它在突发流量下拒绝扩容
- **B** 它会阻止 Karpenter 配置新节点
- **C** 它会终止正在运行的 GPU 节点以迁移 pod，从而驱逐正在处理的请求并重新加载权重
- **D** 它只合并 spot 实例

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 4. 与 Cluster Autoscaler 相比，Karpenter 配置一个 GPU 节点大约快多少？

- **A** 一样快
- **B** 大约快 5%
- **C** 大约快 40%（约 45-60 秒 对比 约 90-120 秒）
- **D** 大约慢 10 倍

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 5. 对于 prefill / decode 分离的 pod（Phase 17 · 17），本课推荐使用哪些扩缩信号？

- **A** prefill pod 用队列深度，decode pod 用 KV 缓存压力，分别作为按角色独立的 HPA
- **B** 仅手动扩缩
- **C** 用单个基于占空比的 HPA 覆盖两类 pod
- **D** 两者都用 Cluster Autoscaler

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 6. 为避免驱逐正在运行的作业，本课为推理 GPU 池推荐哪种 Karpenter 中断（disruption）设置？

- **A** consolidationPolicy: WhenEmptyOrUnderutilized 配合 consolidateAfter: 0s
- **B** 完全禁用 Karpenter
- **C** 始终使用 spot 实例且不进行合并
- **D** consolidationPolicy: WhenEmpty 配合 consolidateAfter: 1h

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>


[返回本课](docs/zh.md)
