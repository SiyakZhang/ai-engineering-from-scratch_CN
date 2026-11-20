# MCP 将能力与宿主解耦 · 自测

每题先选答案，再展开解析。

## 1. 在 MCP 中，哪个组件负责用户体验、模型交互、同意策略以及一个或多个协议 client？

- **A** 执行能力并决定 host 如何呈现它们的 server
- **B** 协调模型、用户和 server client 的 host 应用
- **C** 解析 URI 并存储对话状态的 resource provider
- **D** 每次调用时选择模型的 tool handler

<details>
<summary>查看答案与解析</summary>

**答案**　B

host 负责 AI 应用的体验和策略。一个 client 与一个 server 通信，而 server 执行其已声明的能力。

</details>

## 2. 当前 MCP `2026-07-28` client 必须在每个请求中包含哪些 metadata？

- **A** 仅包含 clientInfo，因为 server 会从既有连接隐式推断版本和能力，无需请求范围的 _meta
- **B** 一个 initialized 标记和 Last-Event-ID header
- **C** params._meta 中同时携带的协议版本和 client capabilities
- **D** 协议会话 ID，以及 initialize 期间协商出的 server 能力

<details>
<summary>查看答案与解析</summary>

**答案**　C

每个请求都携带 io.modelcontextprotocol/protocolVersion 和 io.modelcontextprotocol/clientCapabilities。也应发送 clientInfo，但它是可选的自报信息。

</details>

## 3. 某个 tools/call 需要 roots、sampling 和 elicitation 输入。当前报文模式是什么？

- **A** server 创建 MCP 会话，保存待处理 callback，并等待 notifications/initialized
- **B** client 在每个初始 tool 参数中预加载所有可能的 root、批准答案和模型输出
- **C** server 在开放连接上发送三条独立的 JSON-RPC 请求
- **D** 返回 input_required，然后用 inputResponses、原样的 requestState 和新 ID 重试原 method

<details>
<summary>查看答案与解析</summary>

**答案**　D

MRTR 在 input_required 结果中嵌入请求的 client 输入。client 收集响应后，用新 ID、inputResponses 和原样的 requestState 重试原请求。

</details>

## 4. server/discover 响应必须包含什么，才能描述当前协议支持？

- **A** resultType、精确的 supportedVersions 字段，以及已声明的能力
- **B** negotiatedVersion 字段和协议会话过期时间
- **C** server 发起的 roots/list 请求，随后是绑定该连接的能力响应
- **D** 仅一个 tools 数组，因为 client 会自行推断版本、身份和缓存策略

<details>
<summary>查看答案与解析</summary>

**答案**　A

当前 server 必须实现 server/discover。其 complete 结果报告 supportedVersions 和 capabilities，并且应包含 serverInfo。

</details>

## 5. 为什么不能仅因 server 最初创建了 MCP MRTR requestState 值，就信任它？

- **A** JSON-RPC 总会将 opaque 字符串转换为可执行指令
- **B** 它穿过不受 server 控制的 client 边界，返回时可能已经被篡改
- **C** 协议要求 client 在每次重试前解码、规范化和编辑 requestState
- **D** 每个负载均衡器都会用自己的会话 cookie 替换 requestState

<details>
<summary>查看答案与解析</summary>

**答案**　B

requestState 经由 client 返回，因此受攻击者控制。用 HMAC 或 AEAD 保护安全敏感状态，并将其绑定到身份、过期时间、method 和重要参数。

</details>

## 6. 哪种部署描述符合当前 MCP `2026-07-28` Streamable HTTP？

- **A** 一个 initialize POST，返回 Mcp-Session-Id，并要求在关闭时 DELETE
- **B** 一个由 server 持有、承载直接 sampling 请求的 WebSocket 会话
- **C** 一个 POST endpoint、逐请求返回 JSON 或 SSE 响应，并且没有协议会话
- **D** 一个接收请求的 POST endpoint，以及由 Last-Event-ID 恢复的永久 GET 流

<details>
<summary>查看答案与解析</summary>

**答案**　C

当前 Streamable HTTP 使用单个 POST endpoint 和自描述请求。它取消了 GET 流、协议会话、会话删除和 Last-Event-ID 恢复。

</details>


[返回本课](docs/zh.md)
