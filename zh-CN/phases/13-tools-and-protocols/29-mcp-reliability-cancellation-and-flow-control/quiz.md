# MCP 可靠性、取消与流量控制 · 自测

每题先选答案，再展开解析。

## 1. 一次变更的响应丢失，客户端使用新的 JSON-RPC ID 重试。什么让这次重试变得安全？

- **A** 重试使用同一个 HTTP 连接
- **B** 工具描述符包含 idempotentHint
- **C** 新的 JSON-RPC ID 会自动对该变更去重
- **D** 复用带有完全相同参数的持久化应用幂等键

<details>
<summary>查看答案与解析</summary>

**答案**　D

JSON-RPC ID 用于关联消息。业务幂等性需要持久化键、参数指纹和已存储的提交结果。

</details>

## 2. 在 MCP 2026-07-28 中，客户端如何通过 stdio 取消正在进行的请求？

- **A** 发送带有活动请求 ID 的 notifications/cancelled
- **B** 关闭每请求一个的 SSE 流
- **C** 向 MCP 端点发送 DELETE 请求
- **D** 为 JSON-RPC ID 调用 tasks/cancel

<details>
<summary>查看答案与解析</summary>

**答案**　A

stdio 没有按请求划分的响应流，因此客户端发送即发即弃的 notifications/cancelled 通知。

</details>

## 3. 客户端如何取消正在进行的 Streamable HTTP 请求？

- **A** 发送值为空的 Last-Event-ID
- **B** 等待服务器发送 notifications/cancelled
- **C** 关闭该请求的 SSE 响应流
- **D** 向 MCP 端点 POST notifications/cancelled

<details>
<summary>查看答案与解析</summary>

**答案**　C

对于现代 Streamable HTTP，关闭该请求专属的响应流就是取消信号。

</details>

## 4. 每次空闲超时之前都持续有进度到达。哪一个截止时间仍必须终止失控的请求？

- **A** 代理保活间隔
- **B** Task 轮询间隔
- **C** 下一次分页游标过期时间
- **D** 从请求开始算起的绝对最大超时

<details>
<summary>查看答案与解析</summary>

**答案**　D

有效进度可以重置空闲时钟，但绝对最大截止时间必须继续生效。

</details>

## 5. 成功的 tasks/cancel 响应证明什么？

- **A** Task 最终一定会变为 cancelled
- **B** 服务器已确认取消意图
- **C** 持久化结果已被删除
- **D** worker 已经停止

<details>
<summary>查看答案与解析</summary>

**答案**　B

Task 取消是协作式的。Task 可能保持 working、先完成，或在 worker 检查点后变为 cancelled。

</details>

## 6. 一个订阅 SSE 流在数个进度事件后中断。哪种恢复计划符合 MCP 2026-07-28？

- **A** 保留旧请求 ID，并假定没有丢失更新
- **B** 从 Last-Event-ID 恢复，并重放每个正在进行的变更
- **C** 打开新的 listen 请求，重新获取权威状态，并避免重放不安全的变更
- **D** 打开一个 GET 事件流并恢复 Mcp-Session-Id

<details>
<summary>查看答案与解析</summary>

**答案**　C

现代 MCP 流不能通过 Last-Event-ID 恢复。恢复使用新请求，加上权威重新获取和显式的重试安全性。

</details>


[返回本课](docs/zh.md)
