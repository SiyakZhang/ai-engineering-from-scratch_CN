# MCP 基础：无状态请求与 JSON-RPC · 自测

每题先选答案，再展开解析。

## 1. 两条 MCP 2026-07-28 请求之间，什么会创建协议状态？

- **A** Mcp-Session-Id
- **B** 协议核心中没有任何东西
- **C** HTTP 连接
- **D** stdio 进程

<details>
<summary>查看答案与解析</summary>

**答案**　B

现代协议核心是无状态的。每条请求都携带自己的版本和 capabilities。

</details>

## 2. 每条现代请求的 params._meta 中，哪两个字段是必填项？

- **A** protocolVersion 和 clientCapabilities
- **B** clientInfo 和 cacheScope
- **C** serverInfo 和 ttlMs
- **D** sessionId 和 capabilities

<details>
<summary>查看答案与解析</summary>

**答案**　A

协议版本和 client capabilities 是必填项。client identity 是建议项。

</details>

## 3. 每个现代 MCP server 都必须实现哪个 method 以供预先发现？

- **A** tools/list
- **B** notifications/initialized
- **C** server/discover
- **D** initialize

<details>
<summary>查看答案与解析</summary>

**答案**　C

server/discover 会声明支持的版本、capabilities、instructions 和 server identity。

</details>

## 4. 错误码 -32022 表示什么？

- **A** 不支持的协议版本
- **B** method 不存在
- **C** 内部错误
- **D** header 不匹配

<details>
<summary>查看答案与解析</summary>

**答案**　A

UnsupportedProtocolVersionError 包含请求的版本和 server 支持的版本。

</details>

## 5. 在 MCP 2026-07-28 中，哪种结果需要 ttlMs 和 cacheScope？

- **A** 取消通知
- **B** tools/list 结果
- **C** JSON-RPC error
- **D** tools/call 结果

<details>
<summary>查看答案与解析</summary>

**答案**　B

列表结果和 resources/read 是带有必填 cache hints 的可缓存结果。

</details>

## 6. server 应如何为当前请求选择 capabilities？

- **A** 从 Mcp-Session-Id 读取
- **B** 从当前请求元数据读取
- **C** 复用第一条请求的声明
- **D** 从进程推断

<details>
<summary>查看答案与解析</summary>

**答案**　B

server 不得从连接或此前请求状态推断现代 capabilities。

</details>


[返回本课](docs/zh.md)
