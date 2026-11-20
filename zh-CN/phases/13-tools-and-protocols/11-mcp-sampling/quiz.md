# MCP Model Input：Sampling 迁移与无状态 MRTR · 自测

每题先选答案，再展开解析。

## 1. 一个新的 MCP server 需要 model inference。在 2026-07-28 下默认架构是什么？

- **A** 将 client model key 存在协议 session 中
- **B** 直接集成 model provider
- **C** 在每次 tool call 前发送 sampling/createMessage
- **D** 为 Sampling 打开永久 SSE stream

<details>
<summary>查看答案与解析</summary>

**答案**　B

新设计中的 Sampling 已弃用。当 server 需要 model inference 时，推荐默认方案是直接集成 provider。

</details>

## 2. 2026-07-28 server 在 tools/call 期间如何请求兼容性 Sampling？

- **A** 返回 resultType input_required，并在 inputRequests 中放入 sampling/createMessage
- **B** 在同一 connection 上发送反向 JSON-RPC request
- **C** 将 prompt 写入 server/discover
- **D** 将 prompt 放进 Mcp-Session-Id header

<details>
<summary>查看答案与解析</summary>

**答案**　A

MRTR 在 input_required result 中承载 server-to-client requests，避免反向 request channel。已声明的 summarize_repo tool 必须先通过有有效 inputSchema 的确定性 tools/list 提供。

</details>

## 3. 哪项属性证明 MRTR retry 是独立 JSON-RPC request？

- **A** 它省略逐请求 metadata
- **B** 它移除原始 tool arguments
- **C** 它使用与原始 request 相同的 id
- **D** 它使用新的 id，同时重复原始 method 和 arguments

<details>
<summary>查看答案与解析</summary>

**答案**　D

client 以新的 JSON-RPC id、当前 inputResponses 和回显的 requestState 重复原始 operation。

</details>

## 4. 当 requestState 影响 resource access 时，必须用什么保护它？

- **A** clientInfo name
- **B** 仅 Base64 encoding
- **C** 绑定到 principal、request 与 expiry 的 HMAC 或 authenticated encryption
- **D** 长生命周期 transport session

<details>
<summary>查看答案与解析</summary>

**答案**　C

requestState 会经过不可信 client。完整性保护与绑定可防止篡改和跨请求 replay。

</details>

## 5. client 没有在逐请求 capabilities 中声明 Sampling。server 应使用什么精确协议响应？

- **A** 假定此前请求中有该 capability
- **B** 将 capability 加到 client metadata
- **C** 仍发送嵌入 sampling request
- **D** 返回带 data.requiredCapabilities 的 -32021，或选择非 Sampling 路径

<details>
<summary>查看答案与解析</summary>

**答案**　D

server 不得发出当前请求中 client 未声明支持的 input request。精确的缺少 capability code 是 -32021。

</details>

## 6. 哪种迁移可让两轮兼容性 loop 在协议层保持无状态？

- **A** 将 phase state 存在 Mcp-Session-Id 下
- **B** 在隐藏 session 中累积所有 model responses
- **C** 在完成前重用原始 request id
- **D** 每次新 retry 仅携带当前 round inputResponses 和已签名 phase state

<details>
<summary>查看答案与解析</summary>

**答案**　D

每次 retry 都是自包含的。已签名 requestState 携带已校验 intermediate state，inputResponses 仅包含当前 round。

</details>


[返回本课](docs/zh.md)
