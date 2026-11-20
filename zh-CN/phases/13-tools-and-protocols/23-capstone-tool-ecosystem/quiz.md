# 综合项目：无状态工具生态 · 自测

每题先选答案，再展开解析。

## 1. 本课标准库 harness 成功运行证明了什么？

- **A** collector 接收到了每一个 OpenTelemetry span
- **B** 真实 MCP 传输层完成了初始化
- **C** 进程内策略与数据流如断言所示地运行
- **D** OAuth 授权 server 签发了有效 token

<details>
<summary>查看答案与解析</summary>

**答案**　C

该 harness 使用 Python 函数、静态 token、fixture 和内存 span。它验证这些本地边界，而把协议、授权、导出、浏览器和沙箱集成留给后续测试。

</details>

## 2. 以下哪条流程符合 MCP 修订版 2026-07-28 对发现 server 和轮询耗时工作的规定？

- **A** server/discover、返回任务 handle 的 tools/call、tasks/get
- **B** server/connect、tools/poll、tasks/status
- **C** initialize、tools/call、tasks/result
- **D** GET /mcp、tools/call、tasks/list

<details>
<summary>查看答案与解析</summary>

**答案**　A

无状态修订版使用强制要求的 `server/discover`。可选的 `io.modelcontextprotocol/tasks` 扩展会返回任务 handle，并使用 `tasks/get`；终止任务携带其最终结果。旧握手、GET 端点、`tasks/result` 和 `tasks/list` 都不属于该流程。

</details>

## 3. A2A v1 在其 gRPC 与 JSON-RPC 绑定中如何命名发送消息操作？

- **A** tasks/send
- **B** AgentMessage
- **C** SendMessage
- **D** message/create

<details>
<summary>查看答案与解析</summary>

**答案**　C

A2A v1 在 gRPC 和 JSON-RPC 中使用 `SendMessage`。其 HTTP+JSON 绑定公开 `POST /message:send`。

</details>

## 4. 哪个 MCP Apps SDK 调用可让 App 在其来源 server 上请求工具？

- **A** server.tools.call(args)
- **B** app.callServerTool({ name, arguments })
- **C** host.callTool(name, args)
- **D** app.invoke(name, args)

<details>
<summary>查看答案与解析</summary>

**答案**　B

App 实例调用 `callServerTool`，传入包含 `name` 和可选 `arguments` 的对象；host 会代理底层的 `tools/call` 请求。

</details>

## 5. 本综合项目的 Agent Skill 对 MCP 工具和沙箱拥有什么授权能力？

- **A** 授予只读网络访问权限
- **B** 显式调用后绕过审批
- **C** 没有；host 适配器和策略仍会逐项授权每项能力
- **D** 授予正文中列出的每一个工具

<details>
<summary>查看答案与解析</summary>

**答案**　C

skill 提供的是流程。发现、调用、工具暴露、授权、凭据和隔离均由 host 与外部运行时边界实施。

</details>

## 6. 什么证据最能证明遥测穿过了生产导出边界？

- **A** 预期 span 层级的图示
- **B** 要求发出 span 的 skill 指令
- **C** 带有 trace 与父级断言的 collector 接收端数据
- **D** 包含 traceId 键的本地字典

<details>
<summary>查看答案与解析</summary>

**答案**　C

接收端观察可以证明 SDK、propagator、exporter、传输层和 collector 路径均已工作。本地数据和图示只证明本地构造或意图。

</details>


[返回本课](docs/zh.md)
