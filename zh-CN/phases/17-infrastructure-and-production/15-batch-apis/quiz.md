# Batch API —— 5 折成为行业标准 · 自测

每题先选答案，再展开解析。

## 1. 2026 年 OpenAI、Anthropic 和 Google 通用的 batch-API 报价是什么？

- **A** 10% 折扣，1 小时交付
- **B** 90% 折扣，7 天交付
- **C** 1k token 以下免费
- **D** 50% 折扣，24 小时交付

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 2. 在本课的框架下，「24 小时交付」实际保证的是什么？

- **A** 只有 1k 请求以下的批次才符合资格
- **B** 批处理总是耗时 24 小时
- **C** 24 小时是缓存的 TTL
- **D** 供应商承诺在 24 小时内返回，典型 P50 约为 2-6 小时

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 3. 在一个共享系统提示的工作负载上，把 batch 与缓存输入叠加，相比同步无缓存会如何改变账单？

- **A** 可降至同步无缓存基线的大约 10%
- **B** 会让成本增加 50%
- **C** 没有影响，因为缓存是自动的
- **D** 只有当模型在 Vertex 上时才有帮助

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 4. 对于内容流水线和离线标注，2026 年默认走哪条工作负载分流通道是错误的？

- **A** 带异步队列的半交互式
- **B** 交互式，因为它听起来很紧急
- **C** 批处理与缓存混合
- **D** 批处理，因为用户看不到 24 小时的延迟

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 5. 跨供应商的输出 schema 陷阱是什么？

- **A** 各供应商的批处理文件格式各不相同（OpenAI JSONL、Anthropic JSONL、Vertex BigQuery/GCS），因此可移植的客户端需要为每家供应商提供适配器
- **B** 所有供应商都使用相同的 OpenAI JSONL 格式
- **C** Anthropic 不支持 JSONL
- **D** Vertex 仅要求 Parquet

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 6. 按本课所述，把工作负载分流到批处理的最简单决策规则是什么？

- **A** 如果它用到了工具，就走批处理
- **B** 只有当网关要求时才走批处理
- **C** 如果用户不会察觉到 24 小时的交付延迟，就总是走批处理（并叠加缓存）
- **D** 如果 prompt 不到 1k token，就走批处理

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>


[返回本课](docs/zh.md)
