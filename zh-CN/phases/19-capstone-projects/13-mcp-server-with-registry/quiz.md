# 顶点项目 13：带 Registry 和治理的无状态 MCP 服务器 · 自测

每题先选答案，再展开解析。

## 1. 为什么本顶点项目同时使用 server.json 和 server/discover？

- **A** server.json 发布安装和 endpoint 元数据，而 server/discover 报告实时协议 capabilities
- **B** Registry 要求两个文件包含完全相同的版本日期
- **C** server.json 存储 sessions，而 server/discover 删除它们
- **D** 它们是同一份工具清单的两个名称

<details>
<summary>查看答案与解析</summary>

**答案**　A

Registry 记录帮助 clients 定位和配置服务器。实时 RPC 报告运行中进程支持什么。它们的 schema 和版本域彼此独立，但发布的身份必须使用已认证的命名空间并与实时 serverInfo 匹配。

</details>

## 2. 在 MCP 修订版 2026-07-28 中，什么取代了 initialize 握手？

- **A** 一个打开永久服务器流的 GET 请求
- **B** 每个 TCP 连接只发送一次的 session cookie
- **C** Mcp-Session-Id 加 notifications/initialized
- **D** 每个请求携带协议版本和 client capabilities，且 clients 可以调用强制的 server/discover

<details>
<summary>查看答案与解析</summary>

**答案**　D

协议是无状态的。版本和 capabilities 是请求元数据，而 server/discover 在不创建 session 的情况下提供实时版本和 capability 发现。

</details>

## 3. 哪种 tools/list 行为支持安全且高效的发现？

- **A** 每个副本上随机的工具顺序
- **B** 在 initialize 期间创建的连接本地列表
- **C** 一份没有 scope、永久缓存的响应
- **D** 确定性顺序，加上 ttlMs 和正确的 public 或 private cacheScope

<details>
<summary>查看答案与解析</summary>

**答案**　D

稳定排序提升可复现性和 prompt caching。ttlMs 传达新鲜度，cacheScope 则防止按用户变化的结果经共享缓存泄露。

</details>

## 4. 哪种 Streamable HTTP 设计符合当前的无状态 transport？

- **A** 所有 clients 都要求负载均衡器 sticky routing
- **B** 独立的 GET 流使用 Last-Event-ID replay
- **C** POST 创建 session，GET 恢复它，DELETE 关闭它
- **D** 每条 JSON-RPC 消息各用一个 POST；请求使用 JSON 或请求范围的 SSE

<details>
<summary>查看答案与解析</summary>

**答案**　D

当前 Streamable HTTP 对 MCP 消息只使用 POST，没有协议 session、独立 GET 流、session DELETE 或 Last-Event-ID 可恢复性。

</details>

## 5. 在策略已批准的工具 handler 运行前，生产服务器必须校验什么？

- **A** 只校验 server.json 是否列出 remote URL
- **B** 只校验是否有人发布了一条审批消息
- **C** 协议元数据，以及 token issuer、audience 或 resource、expiry、scope 和任何精确动作审批
- **D** 只校验工具的 destructiveHint 注释

<details>
<summary>查看答案与解析</summary>

**答案**　C

传输元数据、token 校验和策略是相互独立的 gates。注释与发布元数据不会授予权限。

</details>

## 6. 哪种证据最能支持“服务器无需协议 sessions 即可扩展”的主张？

- **A** 一条 server.json remote 条目
- **B** 一张展示负载均衡器的图
- **C** 一个构造单个响应字典的 unit test
- **D** 跨两个可互换副本的 wire-level 并发运行，且没有 affinity 依赖

<details>
<summary>查看答案与解析</summary>

**答案**　D

必须演练真实 transport 与部署边界。让请求在副本间交替，才能证明正确性没有隐藏在一个进程或 sticky session 中。

</details>


[返回本课](docs/zh.md)
