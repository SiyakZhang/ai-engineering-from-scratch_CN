# MCP Tasks 扩展：无状态核心上的持久工作 · 自测

每题先选答案，再展开解析。

## 1. 无状态 MCP server 如何支持持续十分钟的工作？

- **A** 要求每个 client 使用粘性负载均衡
- **B** 保持一条 Mcp-Session-Id 连接十分钟
- **C** 返回一个由应用存储支持的显式持久 task handle
- **D** 仅在 initialize 状态中保存进度

<details>
<summary>查看答案与解析</summary>

**答案**　C

无状态描述的是协议请求模型。持久应用状态由显式 task id 和共享存储表示。

</details>

## 2. server 何时可以从 tools/call 返回 resultType task？

- **A** 仅当 params._meta.task.required 为 true 时
- **B** 当前请求宣告扩展，且 task 已可从持久存储读取之后
- **C** 持久化之前，让 client 乐观轮询时
- **D** 之前的某个 session 曾宣告 Tasks 时

<details>
<summary>查看答案与解析</summary>

**答案**　B

task 创建由 server 决定，但当前请求的 capability 支持与先持久化再返回都是强制条件。缺少支持时返回带 data.requiredCapabilities 的 -32021。

</details>

## 3. tasks/get 响应的 resultType 是 complete、status 是 working，表示什么？

- **A** 该响应违反扩展规范
- **B** 底层 job 已完成
- **C** 轮询 RPC 已完成，但 job 仍在运行
- **D** task 已取消

<details>
<summary>查看答案与解析</summary>

**答案**　C

resultType 描述 tasks/get RPC；task status 独立描述持久 job。status 为 completed 时，嵌套 CallToolResult 有自己的 resultType complete 和 serverInfo metadata。

</details>

## 4. task 已存在后，client 如何回答 input_required？

- **A** 打开一个新的 initialize session
- **B** 使用同一 id 重试原始 tools/call
- **C** 调用带 answer 字段的 tasks/result
- **D** 用 tasks/update 向待处理 task keys 发送 inputResponses

<details>
<summary>查看答案与解析</summary>

**答案**　D

创建后的 task 输入由 tasks/get 展示，并通过 tasks/update 完成，不是重试原始调用。

</details>

## 5. 成功的 tasks/cancel 响应保证什么？

- **A** 最终 task status 必然是 cancelled
- **B** worker 已经停止
- **C** server 已确认取消意图
- **D** 结果已被删除

<details>
<summary>查看答案与解析</summary>

**答案**　C

取消是协作且最终一致的。acknowledgement 之后工作仍可能完成或忽略取消。

</details>

## 6. 哪组方法符合当前官方 Tasks 扩展？

- **A** tasks/create、tasks/subscribe 和 tasks/delete
- **B** tasks/status、tasks/result 和 tasks/list
- **C** tools/task、notifications/task_result 和 roots/list
- **D** tasks/get、tasks/update 和 tasks/cancel

<details>
<summary>查看答案与解析</summary>

**答案**　D

扩展使用 tasks/get、tasks/update 和 tasks/cancel。每个 HTTP 请求将 Mcp-Name 设为 params.taskId。旧的 status、result 和 list 方法仅用于迁移。

</details>


[返回本课](docs/zh.md)
