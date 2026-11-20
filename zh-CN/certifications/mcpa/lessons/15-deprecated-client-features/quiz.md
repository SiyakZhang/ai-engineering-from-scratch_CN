# 已弃用，不等于已移除：Roots、Sampling 与 Logging · 自测

每题先选答案，再展开解析。

## 1. 根据 MCP 功能生命周期，在 2026-07-28 修订版中，roots、sampling 和 logging 被标记为 Deprecated 意味着什么？

- **A** 它们只是改了名称，其他行为完全不变
- **B** 它们现在仍完整可用，只会在更晚的时候面临移除
- **C** 它们从核心功能变成了可选扩展
- **D** 该修订版发布时，它们已从 schema 中删除

<details>
<summary>查看答案与解析</summary>

**答案**　B

生命周期策略中的 Deprecated 表示功能仍有完整规范且可正常使用，已有迁移路径，并且至少经过十二个月窗口后才具备被移除的资格。

</details>

## 2. 服务器处理 tools/call 请求时，需要客户端侧语言模型生成。2026-07-28 允许它如何提出请求？

- **A** 等待客户端轮询后台 task
- **B** 在调用途中向客户端推送 createMessage 请求
- **C** 返回 input_required，并提供一个待回答的 createMessage 项
- **D** 打开第二条连接，直接查询模型

<details>
<summary>查看答案与解析</summary>

**答案**　C

Sampling 仍作为弃用客户端功能存在，服务器通过多轮模式请求它：返回 input_required 结果，并在 inputRequests 映射中携带 sampling createMessage 项供客户端回答。

</details>

## 3. 客户端在某次请求中既未声明 roots capability，也未声明 sampling capability。需要两者的服务器必须怎么做？

- **A** 仍然发送请求，因为默认值覆盖所有客户端
- **B** 回退到已移除的 initialize 握手
- **C** 假定客户端原本想声明两项 capability
- **D** 跳过这些输入请求，或直接拒绝调用

<details>
<summary>查看答案与解析</summary>

**答案**　D

服务器不得依赖调用方未在当前请求中声明的 capability，因此只能省略未声明的输入请求或拒绝调用，绝不能擅自假定或静默发送。

</details>

## 4. 在 2026-07-28 中，服务器何时可以针对某个请求发送 notifications/message 通知？

- **A** 仅当该请求自身的 meta 中携带 logLevel
- **B** 只要服务器声明了 logging capability 就可以
- **C** 仅在客户端调用已移除的 logging setLevel 方法后
- **D** Logging 启动后，在共享 subscriptions listen 流上发送

<details>
<summary>查看答案与解析</summary>

**答案**　A

Logging 现在按请求传递：只有某个请求的 meta 携带 io.modelcontextprotocol logLevel 时，服务器才能在该请求的响应流上发送 notifications/message；缺少该键时必须保持静默。

</details>

## 5. 以下哪一项在 2026-07-28 的 wire 中已经真正消失，而不只是被弃用？

- **A** 作为 MRTR 输入请求发送的 roots/list
- **B** 旧的 session 级日志级别设置器 logging/setLevel
- **C** 与 notifications/message 配合的每请求 logLevel 键
- **D** 作为 MRTR 输入请求发送的 sampling/createMessage

<details>
<summary>查看答案与解析</summary>

**答案**　B

Roots 和 sampling 仍作为 MRTR 输入请求传递，每请求 logLevel 仍会触发 notifications/message；但 logging/setLevel 依赖连接级 session，而无状态核心已将其彻底移除。

</details>

## 6. Roots 在 2026-07-28 发布的规范修订版中被标记为 Deprecated。它最早可能何时移除？

- **A** 立即在下一版发布的修订版中移除
- **B** 永不移除，因为按策略弃用功能会永久保留
- **C** 在 2027-07-28 当日或之后发布的第一版修订版中
- **D** 固定在 2027-07-28，不受规范实际发布时间影响

<details>
<summary>查看答案与解析</summary>

**答案**　C

最短弃用窗口从该修订版发布起计算十二个月，因此最早移除时间是 2027-07-28 当日或之后第一版成为 Current 的规范，而不是一个固定日历日期。

</details>


[返回本课](docs/zh.md)
