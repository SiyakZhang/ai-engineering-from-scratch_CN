# 多区域 LLM 服务与 KV Cache 局部性 · 自测

每题先选答案，再展开解析。

## 1. 为什么轮询（round-robin）负载均衡对带缓存的 LLM 推理是有害的？

- **A** 轮询只对有状态数据库有效
- **B** 一个请求若没有落到持有其前缀的节点上，就要付出完整的 prefill 成本，而不是命中缓存
- **C** 轮询需要粘性会话（sticky sessions）
- **D** 轮询会破坏 TLS

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 2. 一个缓存感知路由器消费哪两类输入？

- **A** 轮询计数器和 TLS 密钥
- **B** 来自各副本的 KV 缓存事件，以及对传入请求计算的前缀哈希
- **C** 仅 user_id 和 tenant_id
- **D** 随机洗牌和请求大小

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 3. 对于 Llama 3.3 70B FP8，在一个 2K token 的 prompt 上，缓存命中与冷 prefill 之间的 TTFT 差距大约是多少？

- **A** 约 10 倍（约 80 ms 对比 约 800 ms）
- **B** 约 1000 倍
- **C** 约 1.1 倍
- **D** 完全相同

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 4. 为什么跨区域路由在缓存命中方面并不总是优于区域内路由？

- **A** 所有超大规模云厂商都禁止跨区域路由
- **B** 跨区域无法实现缓存感知路由
- **C** 网络 RTT 会抵消大部分 prefill 节省，例如美洲到亚太的 220 ms 往返时延，会把 720 ms 的节省压缩到约 500 ms
- **D** GORGO 研究发现缓存命中对延迟没有帮助

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 5. 本课把什么列为占 32% 的 LLM 灾备（DR）失败诱因？

- **A** 未加密的备份
- **B** 区域配额耗尽
- **C** 备份包含了权重，却漏掉了 tokenizer 文件或量化配置
- **D** 配置错误的负载均衡器

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 6. 对于像 Bedrock CRI 这样的商用跨区域推理产品，本课怎么说？

- **A** 它们优化的是可用性而非 TTFT，并把推理视为黑盒 —— 你仍然需要一个应用层的缓存感知路由器
- **B** 它们是 KV 缓存感知的，可以替代应用层路由
- **C** 在 GDPR 下它们是被禁止的
- **D** 它们只在 us-east-1 工作

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>


[返回本课](docs/zh.md)
