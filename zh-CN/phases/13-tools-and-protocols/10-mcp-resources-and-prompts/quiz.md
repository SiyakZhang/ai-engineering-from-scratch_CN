# MCP Resources 与 Prompts：为无状态 Server 提供可寻址上下文 · 自测

每题先选答案，再展开解析。

## 1. host 需要通过 URI 取回一份稳定的 architecture note。最适合哪种 MCP 基元？

- **A** Resource
- **B** 破坏性 tool
- **C** 协议 session
- **D** 取消 notification

<details>
<summary>查看答案与解析</summary>

**答案**　A

resource 通过 URI 暴露可寻址 content。tool 执行 operation，session 与 cancellation 都不用于建模可读 content。

</details>

## 2. 当 resources/read 收到未知 resource URI 时，2026-07-28 server 应返回什么？

- **A** JSON-RPC error -32602
- **B** 成功但为空的 contents array
- **C** resources/list_changed notification
- **D** JSON-RPC error -32601

<details>
<summary>查看答案与解析</summary>

**答案**　A

当前 Resources 契约将无效或未知 resource URI 视为 invalid parameters，code 为 -32602。成功空结果会隐藏调用者 error。

</details>

## 3. 对于 resources/read 返回的用户拥有 note，哪种 cache policy 最安全？

- **A** 使用有界 TTL 的 private
- **B** 因 URI 稳定而设为 public
- **C** 使用无限 TTL 的 public
- **D** 当 MIME type 匹配时跨用户共享

<details>
<summary>查看答案与解析</summary>

**答案**　A

用户拥有的结果不应跨 identity boundaries。带界限的私有 cache 能减少重复读取，同时保留 authorization context。

</details>

## 4. subscriptions/listen response stream 上的每个 notification 由什么标识？

- **A** server process ID
- **B** subscription metadata 中的原始 listen request ID
- **C** resource MIME type
- **D** 新生成的协议 session

<details>
<summary>查看答案与解析</summary>

**答案**　B

subscriptions/listen 的 JSON-RPC ID 会成为 io.modelcontextprotocol/subscriptionId，并在 acknowledgment 和每个后续 event 中重复。

</details>

## 5. 为什么 resources/list 和 prompts/list 对同一请求输入必须保持确定性？

- **A** 让 list membership 依赖此前 read
- **B** 为所有返回 entries 授予 public access
- **C** 避免校验 pagination cursors
- **D** 稳定 caches、snapshots 和 host interfaces

<details>
<summary>查看答案与解析</summary>

**答案**　D

稳定 membership 与 ordering 能防止噪声 cache misses 和变化的 interfaces。因为 credentials 是显式请求输入，authorization 仍可影响可见性。

</details>

## 6. 即使 client 可以直接调用 resources/list，当前 MCP server 仍必须暴露什么？

- **A** 独立 HTTP GET event stream
- **B** 包含支持 revisions 和 capabilities 的 server/discover
- **C** 每个 URI 的 resources/subscribe method
- **D** 创建协议 session 的 initialize method

<details>
<summary>查看答案与解析</summary>

**答案**　B

server 必须实现 server/discover，使 client 能获取一份 capability 与 version snapshot。client 仍可选择调用其他 method，并处理结构化版本 error。

</details>


[返回本课](docs/zh.md)
