# 前缀缓存推理服务——RadixAttention 与 KV 复用 · 自测

每题先选答案，再展开解析。

## 1. 支撑 SGLang KV 缓存复用的核心数据结构是什么？

- **A** 一棵基数树（radix tree），每个节点拥有一段 token 范围及其 KV 块
- **B** 一个以完整 prompt 为键的哈希表
- **C** 一个以请求 id 为键的跳表（skip list）
- **D** 一棵存放 attention 分数的 B 树

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 2. 为什么 FCFS 调度对 SGLang 上的前缀密集型流量是错误的？

- **A** FCFS 可能在下一个长前缀请求到来之前就把热门前缀分支驱逐掉，从而破坏基数树的复用
- **B** FCFS 与 PagedAttention 不兼容
- **C** FCFS 只在 AMD GPU 上工作
- **D** FCFS 是 SGLang 推荐的策略

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 3. SGLang 的缓存感知调度器使用什么粒度的驱逐来匹配基数树的形状？

- **A** 仅按请求
- **B** 随机驱逐
- **C** 整条分支，从最短被使用的叶子节点开始
- **D** 单个 token

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 4. 对工程师而言，保持基数树共享前缀可被发现的最直接手段是什么？

- **A** 调低 GPU 显存利用率旋钮
- **B** 始终使用静态批处理
- **C** 禁用连续批处理
- **D** 固定 prompt 模板的顺序，让不可变内容（system、tools、schema）始终排在最前面

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 5. 本课认为 RadixAttention 在哪种负载模式下不会带来优势？

- **A** 使用独特 prompt、没有共享 system prompt 的单次生成
- **B** 带有共享检索前言的 RAG
- **C** 共享工具 schema 的 agent
- **D** 带有重复开场白的语音负载

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 6. ProjectDiscovery 的部署通过做了什么，把前缀缓存命中率从 7% 提升到 74%？

- **A** 禁用连续批处理
- **B** 把动态内容移出可缓存的前缀之外
- **C** 在不改动任何 prompt 的情况下从 vLLM 切换到 SGLang
- **D** 把 GPU 数量从 8 增加到 16

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>


[返回本课](docs/zh.md)
