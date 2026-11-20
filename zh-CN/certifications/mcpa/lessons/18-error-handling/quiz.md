# 请求失败的两种方式 · 自测

每题先选答案，再展开解析。

## 1. 一条 tools/call 请求指定了服务器从未注册的工具。按照 MCP 2026-07-28，哪种响应正确？

- **A** 返回错误码 -32601（找不到方法）的 JSON-RPC 错误
- **B** 返回错误码 -32602（无效参数）的 JSON-RPC 错误
- **C** 返回 isError 为 true 并附简短说明的普通结果
- **D** 返回错误码 -32002（旧版资源错误码）的 JSON-RPC 错误

<details>
<summary>查看答案与解析</summary>

**答案**　B

未知工具属于协议错误，使用 -32602 Invalid params；-32601 表示方法本身不存在，而 -32002 已在 2026-07-28 前退役。

</details>

## 2. 客户端在请求的 _meta 中省略了 io.modelcontextprotocol/clientCapabilities。服务器必须怎么做？

- **A** 使用错误码 -32021 Missing capability 拒绝请求
- **B** 等待连接上的下一条请求补充该字段
- **C** 使用错误码 -32602 Invalid params 拒绝请求
- **D** 假定能力集为空并继续处理请求

<details>
<summary>查看答案与解析</summary>

**答案**　C

缺少必需 _meta 字段（包括 clientCapabilities）的请求格式不正确，服务器必须使用 -32602 拒绝，而不能假定默认值或等待永远不会补全当前请求的后续请求。

</details>

## 3. 2026-07-28 实现绝不能发出哪一对 JSON-RPC 错误码？

- **A** -32601 和 -32603，两者都是标准 JSON-RPC 错误码
- **B** -32700 和 -32600，两者都是标准 JSON-RPC 错误码
- **C** -32020 和 -32021，两者都由当前版本定义
- **D** -32002 和 -32042，两者都已在当前版本前退役

<details>
<summary>查看答案与解析</summary>

**答案**　D

规范已退役 -32002（2026-07-28 前的资源不存在错误码）和 -32042（2025-11-25 的 URL elicitation 错误码）；-32020 至 -32022 仍在使用，标准错误码也继续有效。

</details>

## 4. 工具参数未通过其声明的 input schema，例如缺少必填字段。合规服务器应如何报告？

- **A** 返回 isError 为 true 并说明原因的普通结果
- **B** 返回错误码 -32602 Invalid params 的 JSON-RPC 错误
- **C** 关闭连接，要求客户端重新连接
- **D** 返回错误码 -32600 Invalid Request 的 JSON-RPC 错误

<details>
<summary>查看答案与解析</summary>

**答案**　A

SEP-1303 将输入验证失败归入工具执行错误，即返回 isError 为 true 的普通结果，使模型能读取原因并用修正后的参数重试。

</details>

## 5. Streamable HTTP 服务器因 MCP-Protocol-Version header 与请求体中的协议版本不一致而拒绝请求。正确的 HTTP 状态与错误码组合是什么？

- **A** 401 Unauthorized 与错误码 -32021
- **B** 400 Bad Request 与错误码 -32020
- **C** 403 Forbidden 与错误码 -32022
- **D** 404 Not Found 与错误码 -32601

<details>
<summary>查看答案与解析</summary>

**答案**　B

header 与请求体不一致属于 HeaderMismatch，错误码为 -32020；服务器必须返回 400 Bad Request，而不是方法、授权或版本错误。

</details>

## 6. 服务器需要客户端先声明 elicitation 能力才能完成请求，但该请求的 clientCapabilities 不包含它。服务器必须返回什么？

- **A** 错误码 -32602，并用 data.uri 指明缺失资源
- **B** 在此返回 inputRequests 为空的 input_required 结果
- **C** 错误码 -32021，并用 data.requiredCapabilities 指明缺失能力
- **D** isError 为 true 且没有更多数据的普通结果

<details>
<summary>查看答案与解析</summary>

**答案**　C

服务器不能依赖客户端未在当前请求中声明的能力；它应返回 MissingRequiredClientCapabilityError（错误码 -32021），并在 data.requiredCapabilities 中列出缺失能力。

</details>


[返回本课](docs/zh.md)
