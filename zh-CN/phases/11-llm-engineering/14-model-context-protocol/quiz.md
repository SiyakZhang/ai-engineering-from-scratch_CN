# 模型上下文协议（MCP） · 自测

每题先选答案，再展开解析。

## 1. 在 MCP 2026-07-28 中，client 在哪里发送协议版本和能力？

- **A** 在 server 端的 session 记录中发送
- **B** 在每个请求的 params._meta 中发送
- **C** 只在 initialize 请求中发送
- **D** 只在 HTTP cookie 中发送

<details>
<summary>查看答案与解析</summary>

**答案**　B

现代 MCP 是无状态的。每个请求都会在 params._meta 中携带协议版本和 client 能力。

</details>

## 2. 每个现代 MCP server 都必须实现什么，用于预先发现版本和能力？

- **A** server/discover
- **B** initialize
- **C** sessions/create
- **D** logging/setLevel

<details>
<summary>查看答案与解析</summary>

**答案**　A

server/discover 会公布支持的版本、server 能力和 server 身份。

</details>

## 3. MCP 2026-07-28 当前的 Streamable HTTP 形式是什么？

- **A** 由 Mcp-Session-Id 标识的 WebSocket session
- **B** 每条 JSON-RPC 消息一个 POST；请求 POST 收到 JSON 或请求范围内的 SSE
- **C** 一个 GET 流加上单独的 POST endpoint
- **D** 每次 tool call 后发送一个 DELETE 请求

<details>
<summary>查看答案与解析</summary>

**答案**　B

当前传输有一个 POST endpoint。请求 POST 收到 JSON 或请求范围内的 SSE；已接受的 notification POST 返回没有 body 的 HTTP 202。

</details>

## 4. server 应如何区分缺少协议版本元数据和格式正确但不受支持的版本？

- **A** 两种情况都返回 -32022
- **B** 接受缺少的版本，并为不受支持版本返回 -32601
- **C** 缺少版本时返回 HTTP 301，不受支持时签发 Mcp-Session-Id
- **D** 缺少或非字符串元数据返回 -32602；不受支持的字符串版本返回带 supported/requested 的 -32022

<details>
<summary>查看答案与解析</summary>

**答案**　D

缺少或类型不正确的必填字段属于格式错误的 JSON-RPC params。只有已提供但未实现的版本字符串才适用 UnsupportedProtocolVersionError。

</details>

## 5. 一个多步骤 tool 需要跨调用连续性。现代 MCP 应如何设计？

- **A** 签发一个不透明 handle，并要求后续调用把它作为 tool 参数传入
- **B** 将可变状态放进 clientInfo
- **C** 只为这个 tool 恢复 Mcp-Session-Id
- **D** 将状态存放在 TCP connection 后面

<details>
<summary>查看答案与解析</summary>

**答案**　A

跨调用状态是显式的应用状态。由 server 签发的 handle 作为普通且经过授权的参数传递。

</details>

## 6. 现代 server 如何在一次 tool 操作中请求用户、模型或 root 输入？

- **A** 返回 input_required，随后 client 携带 inputResponses 重试
- **B** 打开第二条 SSE connection
- **C** 发送独立的 server-to-client JSON-RPC 请求
- **D** 把问题写到 stderr

<details>
<summary>查看答案与解析</summary>

**答案**　A

Multi Round-Trip Requests 模式会把 inputRequests 嵌入 input_required 结果中，并重试原操作。

</details>


[返回本课](docs/zh.md)
