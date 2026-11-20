# 无状态 MCP 网关与注册表准入 · 自测

每题先选答案，再展开解析。

## 1. 当前 MCP 网关必须在普通 client 请求之间保留什么？

- **A** 不保留协议会话；每个请求携带校验和路由所需的信息
- **B** 最后一个 HTTP 连接
- **C** 每个后端一个 Mcp-Session-Id
- **D** 一个独立的 GET 事件流

<details>
<summary>查看答案与解析</summary>

**答案**　A

MCP 2026-07-28 的普通请求是自包含的，可以抵达任意健康的网关实例。

</details>

## 2. 按主体过滤的 tools/list 结果通常应使用哪种缓存范围？

- **A** public
- **B** private
- **C** global
- **D** session

<details>
<summary>查看答案与解析</summary>

**答案**　B

用户专属的工具列表不得在不同授权上下文之间共享。

</details>

## 3. 网关应如何将工具调用转发给当前协议后端？

- **A** 将外层 JSON-RPC id 复用为持久状态
- **B** 复制外层 bearer token 和 session id
- **C** 先打开一个 GET 流
- **D** 创建全新的自包含请求，携带网关 client 元数据和经调解的能力

<details>
<summary>查看答案与解析</summary>

**答案**　D

网关是后端的 client，会创建独立有效的新请求。

</details>

## 4. 网关在准入时应如何使用官方 Registry 的 server.json 记录？

- **A** 从任意记录字段复制验证声明
- **B** 相信任何名称看起来熟悉的记录
- **C** 将发布行为视为已经完成的安全审查
- **D** 校验其发布形状，再关联独立的已验证发布者、溯源、策略和批准状态

<details>
<summary>查看答案与解析</summary>

**答案**　D

server.json 携带发布元数据。已验证的溯源和网关的批准决定仍是外部准入证据。

</details>

## 5. 在现代 Streamable HTTP 中，如何打开长生命周期的列表变更通知？

- **A** 通过 resources/subscribe
- **B** 通过携带 Last-Event-ID 的独立 GET
- **C** 通过 notifications/initialized
- **D** 通过 POST 发送 subscriptions/listen 请求，其响应为 SSE

<details>
<summary>查看答案与解析</summary>

**答案**　D

subscriptions/listen 取代了旧的非请求式 GET 和资源订阅模型。

</details>

## 6. 哪个 Tasks 扩展路由规则是当前规则？

- **A** 使用 taskId 作为 Mcp-Name 来路由 tasks/get、tasks/update 和 tasks/cancel
- **B** 将任务存入 Mcp-Session-Id
- **C** 使用 tasks/list 恢复一个会话中的所有任务
- **D** 使用 tasks/result 获取最终输出

<details>
<summary>查看答案与解析</summary>

**答案**　A

官方扩展使用 get、update 和 cancel；任务 id 在无需协议会话的情况下提供路由句柄。

</details>


[返回本课](docs/zh.md)
