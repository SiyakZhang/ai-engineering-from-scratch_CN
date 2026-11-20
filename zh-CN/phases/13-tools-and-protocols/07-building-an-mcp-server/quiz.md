# 构建 MCP Server：无状态 Python 与 TypeScript · 自测

每题先选答案，再展开解析。

## 1. 现代 MCP server 从哪里读取 client capabilities？

- **A** 从进程环境
- **B** 从每条当前请求
- **C** 从 Mcp-Session-Id
- **D** 从第一条 initialize 调用

<details>
<summary>查看答案与解析</summary>

**答案**　B

MCP 2026-07-28 在每条请求的 params._meta 中携带 client capabilities。

</details>

## 2. 现代 server 必须实现哪个 method？

- **A** resources/subscribe
- **B** initialize
- **C** shutdown
- **D** server/discover

<details>
<summary>查看答案与解析</summary>

**答案**　D

现代 server 必须提供 server/discover，尽管 client 可以先调用其他 method。

</details>

## 3. tools/list 的成功结果需要哪些字段？

- **A** protocolVersion 和 tools
- **B** resultType、ttlMs、cacheScope、tools
- **C** sessionId 和 tools
- **D** initialized 和 tools

<details>
<summary>查看答案与解析</summary>

**答案**　B

现代列表结果带有类型，且可缓存。

</details>

## 4. 为什么 server 应以确定性方式排序 tools？

- **A** 替代授权
- **B** 创建 session
- **C** 协商协议
- **D** 稳定 caches 和模型上下文

<details>
<summary>查看答案与解析</summary>

**答案**　D

稳定排序让等价 registry 产生等价响应。

</details>

## 5. 一次有效 tool call 已运行，但领域操作失败。哪种结果形状合适？

- **A** 带 isError true 的完整 tool 结果
- **B** notifications/initialized
- **C** HTTP DELETE
- **D** 一条新的 server 请求

<details>
<summary>查看答案与解析</summary>

**答案**　A

通过 content 和 isError，让模型能够看到 tool 层失败。

</details>

## 6. 什么应结束 stdio server 的 transport 生命周期？

- **A** 一条必需的 shutdown RPC
- **B** stdin 上的 EOF
- **C** Mcp-Session-Id 过期
- **D** 一条 GET 请求

<details>
<summary>查看答案与解析</summary>

**答案**　B

EOF 是可移植的 stdio shutdown signal。它不会关闭现代协议 session。

</details>


[返回本课](docs/zh.md)
