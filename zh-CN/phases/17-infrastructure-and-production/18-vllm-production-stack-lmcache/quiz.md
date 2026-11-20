# 生产级推理服务栈——KV 卸载与缓存感知路由 · 自测

每题先选答案，再展开解析。

## 1. 在 vLLM 部署中，LMCache 主要解决什么问题？

- **A** HBM 中的 KV 缓存压力导致抢占，以及对相同前缀的重复 prefill
- **B** 冷启动时的镜像拉取
- **C** Tokenizer 的 GIL 争用
- **D** 网络出站（egress）过滤

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 2. 哪个 vLLM API 引入了可插拔的 KV 缓存后端？

- **A** vLLM v0.9.0 中的 Connector API
- **B** ChunkedPrefill API
- **C** 前缀缓存开关
- **D** PagedAttention v2

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 3. vLLM 0.11.0（2026 年 1 月）版本为 KV 卸载路径增加了什么？

- **A** 移除了对 LMCache 的支持
- **B** 强制使用 FP8 KV 缓存
- **C** 仅同步卸载
- **D** 一条异步卸载路径，使引擎在常见情形下不会因卸载而阻塞

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 4. 什么时候应该选择 LMCache 而非原生的 CPU 卸载？

- **A** 当多个引擎跨租户、跨 LoRA 变体或在重复的 RAG 上下文之间共享前缀时，跨引擎复用才划算
- **B** 当单个引擎有 HBM 压力且没有前缀共享时
- **C** 当你想完全禁用 KV 缓存时
- **D** 当你只在 CPU 上运行时

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 5. 当 KV 占用远低于 HBM 时，LMCache 的收益会怎样？

- **A** LMCache 会自动禁用
- **B** 它仍能把吞吐量翻倍
- **C** 引擎崩溃
- **D** 各配置与基线持平，伴随约 3-5% 的开销，且没有实际收益

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 6. 为什么 LMCache 能与分离式服务（Phase 17 · 17）组合使用？

- **A** 因为 LMCache 与引擎跑在同一块 GPU 上
- **B** 并不能 —— 它们是互斥的
- **C** 从 prefill 传到 decode 的 KV 会落入 LMCache；后续查询可从 LMCache 拉取并跳过 prefill，因此缓存感知路由器可以挑选其本地缓存或 LMCache 共享缓存能匹配的引擎
- **D** 因为 LMCache 取代了 NIXL

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>


[返回本课](docs/zh.md)
