# MCP Transports：stdio 与无状态 Streamable HTTP · 自测

每题先选答案，再展开解析。

## 1. 每条现代 Streamable HTTP 消息由哪种 HTTP method 承载？

- **A** GET
- **B** PATCH
- **C** POST
- **D** DELETE

<details>
<summary>查看答案与解析</summary>

**答案**　C

每条现代 JSON-RPC request 或 notification 都是发送到一个 MCP endpoint 的新 POST。

</details>

## 2. 现代专用 MCP endpoint 应对 GET 和 DELETE 返回什么？

- **A** 301
- **B** 200
- **C** 405
- **D** 202

<details>
<summary>查看答案与解析</summary>

**答案**　C

独立 GET 和 DELETE 不属于 Streamable HTTP 2026-07-28。

</details>

## 3. 每条现代请求中，哪些 headers 必须与 body 匹配？

- **A** MCP-Protocol-Version 和 Mcp-Method
- **B** Cookie 和 Host
- **C** ETag 和 If-None-Match
- **D** Mcp-Session-Id 和 Last-Event-ID

<details>
<summary>查看答案与解析</summary>

**答案**　A

Mcp-Name 对 tools/call、resources/read 和 prompts/get 也是必填项。

</details>

## 4. client 如何请求长生命周期的 change notifications？

- **A** GET /mcp
- **B** Mcp-Session-Id
- **C** POST subscriptions/listen
- **D** resources/subscribe

<details>
<summary>查看答案与解析</summary>

**答案**　C

subscriptions/listen 打开 response stream。其 acknowledgement、notifications 和最终 result 都将 listen request id 作为 subscription metadata 携带。

</details>

## 5. 现代请求范围的 SSE stream 在最终 response 前断开。下一步是什么？

- **A** DELETE session
- **B** 以新的 JSON-RPC id 安全重试
- **C** 复用同一 response stream
- **D** 用 Last-Event-ID 恢复

<details>
<summary>查看答案与解析</summary>

**答案**　B

现代 SSE 不可恢复。安全重试是带新 id 的新请求。

</details>

## 6. server 应如何处理 2026-07-28 请求中的 Mcp-Session-Id？

- **A** 用它路由
- **B** 忽略它且不回显
- **C** 拒绝包含它的每条请求
- **D** 轮换它

<details>
<summary>查看答案与解析</summary>

**答案**　B

协议 sessions 和 session header 已从现代修订版移除。

</details>


[返回本课](docs/zh.md)
