# MCP 的无状态核心 · 自测

每题先选答案，再展开解析。

## 1. 按照 MCP 2026-07-28，服务端回答一个请求所需的信息必须满足什么条件？

- **A** 从绑定到连接的 session 记录中获取
- **B** 在同一连接上的多个请求中逐渐积累
- **C** 完整包含在这一个请求中，不能推断其他信息
- **D** 从连接开场握手交互中缓存

<details>
<summary>查看答案与解析</summary>

**答案**　C

MCP 2026-07-28 是无状态协议：每个请求都自描述，服务端不得从此前到达的请求推断上下文，即使它们使用同一连接。

</details>

## 2. 服务端刚处理完客户端在一条长连接 HTTP 上的第三个请求。它可以对同一连接上的第四个请求做什么假设？

- **A** 此前声明的相同客户端能力仍适用于第四个请求
- **B** 该连接现在已经构成后续请求的已认证 session
- **C** 第三个请求协商的相同协议版本仍然适用
- **D** 不能做任何假设：第四个请求必须再次提供自己的版本和能力

<details>
<summary>查看答案与解析</summary>

**答案**　D

服务端不得依赖同一连接上的早先请求来判断能力、协议版本或身份；每个请求都要在自己的 _meta 字段中提供这些元数据。

</details>

## 3. MCP 2026-07-28 为什么让每个请求自描述，而不是依赖连接级握手？

- **A** 这样任意 replica 都能回答，重试也可以安全发往任意位置
- **B** 这样服务端就可以放心跳过大多数请求的能力验证
- **C** 这样单个服务端进程可以维持更多并发连接
- **D** 这样客户端每次启动应用只需认证一次

<details>
<summary>查看答案与解析</summary>

**答案**　A

由于状态不绑定到特定进程，任意 replica 都能处理任意请求，重试可以发往其他 replica，负载均衡器也无需 session stickiness。

</details>

## 4. 客户端打开一条 stdio 连接，在不关闭连接的情况下先发送用户 A 的请求，再发送用户 B 的无关请求。MCP 2026-07-28 对此如何规定？

- **A** 只有两个请求共享同一授权 token 时才允许
- **B** 允许；开放连接从来不构成 session 或对话
- **C** 不允许，除非服务端先签发新的 session 标识符
- **D** 不允许；一个 stdio 进程只能承载一段对话

<details>
<summary>查看答案与解析</summary>

**答案**　B

stdio 进程等开放连接不是对话或 session：客户端可以在同一传输通道上交错发送无关请求，服务端不得把连接身份当作连续性的替代。

</details>

## 5. 服务端需要让购物车跨越多次工具调用。哪种设计符合 SEP-2567 对 MCP 2026-07-28 的指导？

- **A** 在服务端以客户端连接标识符为键保存购物车
- **B** 把购物车保存在服务端内存中，并依赖请求到达顺序
- **C** 由创建工具返回不透明 handle，后续调用复用它
- **D** 要求客户端在每个购物车请求中重发 session 标识符

<details>
<summary>查看答案与解析</summary>

**答案**　C

跨越多个请求的状态必须通过客户端每次显式传递的标识符引用：由创建工具返回服务端签发的 handle，再作为普通参数传入后续调用。

</details>

## 6. MCP 2026-07-28 为了让无状态性成为默认行为，移除了以下哪项？

- **A** tools/call method 及其 CallToolResult content 列表
- **B** 逐请求 _meta 字段及其 protocolVersion 值
- **C** server/discover method 及其 supportedVersions 列表
- **D** initialize 握手与 Mcp-Session-Id header

<details>
<summary>查看答案与解析</summary>

**答案**　D

2026-07-28 移除了 initialize 握手、notifications/initialized 和 Mcp-Session-Id header；带 protocolVersion 的逐请求 _meta 与 server/discover 正是替代它们的现行机制。

</details>


[返回本课](docs/zh.md)
