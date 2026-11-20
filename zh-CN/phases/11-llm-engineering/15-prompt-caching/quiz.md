# Prompt Caching 与上下文缓存 · 自测

每题先选答案，再展开解析。

## 1. 相比基础输入费率，Anthropic 对缓存读取（cache read）给予多少折扣？

- **A** 打 5 折（便宜 50%）
- **B** 打 7.5 折（便宜 25%）
- **C** 打 2.5 折（便宜 75%）
- **D** 打 1 折（便宜 90%）

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 2. 为什么动态时间戳必须放在缓存断点（cache breakpoint）之下，而不是之上？

- **A** 缓存只在前缀逐字节相同时才命中；一个变化的时间戳会破坏它之后所有内容的匹配
- **B** 时间戳会让 tokenizer 困惑
- **C** Anthropic 明确拒绝缓存块中的时间戳
- **D** 它们比静态文本花费更多 token

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 3. OpenAI 的 prompt 缓存是如何配置的？

- **A** 你创建并引用的 CachedContent API
- **B** 无需配置的自动前缀匹配
- **C** 你为每个项目切换的系统级开关
- **D** 显式的 cache_control 标记

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 4. 对 Anthropic 而言，相比 5 分钟的默认值，1 小时的延长 TTL 会带来多少写入溢价（write premium）？

- **A** 无写入溢价
- **B** 4 倍写入溢价
- **C** 相同
- **D** 2 倍写入溢价（比基线高 50%）

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 5. 要在 Anthropic 的 25% 写入溢价上达到收支平衡，需要多少次复用？

- **A** 10 次
- **B** 5 次
- **C** 2 次
- **D** 1 次

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>


[返回本课](docs/zh.md)
