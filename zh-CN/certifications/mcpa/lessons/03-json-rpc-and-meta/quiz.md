# JSON-RPC 信封 · 自测

每题先选答案，再展开解析。

## 1. 一条原始 JSON-RPC 消息包含 method 字段，但完全没有 id 字段。它属于四种 MCP 消息形状中的哪一种？

- **A** 请求，因为每条包含 method 的消息都是请求
- **B** 结果响应，因为没有 id 表示交互已经完成
- **C** 错误响应，因为只有错误可以省略 id
- **D** 通知，因为只有请求和结果必须携带 id

<details>
<summary>查看答案与解析</summary>

**答案**　D

包含 method 且完全没有 id 字段的消息是通知；JSON-RPC 通过是否存在 id 区分期待回复的请求与不期待回复的通知。

</details>

## 2. 2026-07-28 客户端收到较早协议版本服务端返回的结果对象，而该服务端从不发送 resultType。客户端必须如何解释缺失字段？

- **A** 视为 complete，这是兼容早于 resultType 的服务端时采用的默认值
- **B** 视为错误，因为 resultType 是必需字段，缺失会使结果格式错误
- **C** 视为客户端最近一次请求中使用的值
- **D** 视为 input_required，因为缺少信息通常会阻止完成

<details>
<summary>查看答案与解析</summary>

**答案**　A

为了向后兼容较早协议版本的服务端，客户端必须把缺失的 resultType 当作 complete，而不是拒绝响应。

</details>

## 3. 以下哪个 _meta 键前缀因为第二个点分 label 是 modelcontextprotocol 或 mcp，而保留给 MCP？

- **A** com.example.mcp/，因为 mcp 是第三个 label
- **B** dev.mcp/，因为第二个 label 是 mcp
- **C** mcp.example/，因为第一个 label 就是 mcp
- **D** org.tools.mcp/，因为 mcp 出现在前缀末尾

<details>
<summary>查看答案与解析</summary>

**答案**　B

只有第二个点分 label 为 modelcontextprotocol 或 mcp 时，前缀才保留给 MCP；dev.mcp 符合条件，其他前缀中的 mcp 都位于别处。

</details>

## 4. 请求的 params._meta 包含 io.modelcontextprotocol/protocolVersion，但完全省略 io.modelcontextprotocol/clientCapabilities。符合规范的服务端必须怎么做？

- **A** 按客户端没有声明任何可选能力来处理请求
- **B** 以 JSON-RPC error -32601 拒绝，因为 method 已无法识别
- **C** 以 JSON-RPC error -32602 拒绝，HTTP 上同时返回 400 Bad Request
- **D** 保持请求打开，直到客户端在后续消息中补充该字段

<details>
<summary>查看答案与解析</summary>

**答案**　C

缺少 clientCapabilities 等必需 _meta 字段的请求格式错误，符合规范的服务端必须以 -32602 拒绝；HTTP 传输还要返回 400 Bad Request。

</details>

## 5. gateway 运营者想根据发送请求的客户端采用不同路由，并读取 io.modelcontextprotocol/clientInfo 作决定。为什么这不安全？

- **A** 只有服务端能读取 clientInfo；gateway 只能读取 _meta.progressToken
- **B** 该字段在请求离开客户端前就会被移除，永远到不了 gateway
- **C** 该字段只会出现在全新连接的第一个请求上
- **D** clientInfo 由发送方自行报告，协议从不验证

<details>
<summary>查看答案与解析</summary>

**答案**　D

clientInfo 和 serverInfo 由发送方自行报告，只用于显示、日志和调试，因此路由或授权决策绝不能依赖它们。

</details>

## 6. 客户端准备向 Streamable HTTP 服务端发送三个独立请求。2026-07-28 要求它怎么做？

- **A** 发送三个独立 POST 请求，每个 body 只包含一个请求或通知
- **B** 用换行把它们连接在一个 POST body 中，每行一条消息
- **C** 打开一条 SSE stream，通过它推送三个请求
- **D** 把它们合并为一个 JSON-RPC batch 数组，一次 POST

<details>
<summary>查看答案与解析</summary>

**答案**　A

JSON-RPC batching 已在 MCP 2025-06-18 修订版中移除，因此每个 Streamable HTTP POST body 必须只携带一个请求或通知。

</details>


[返回本课](docs/zh.md)
