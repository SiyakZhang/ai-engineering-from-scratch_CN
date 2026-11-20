# MCP 安全：投毒元数据、路由与 MRTR 状态 · 自测

每题先选答案，再展开解析。

## 1. 哪个 MCP 字段可安全地用作经过认证的 client 身份？

- **A** clientCapabilities
- **B** clientInfo.name
- **C** clientInfo.version
- **D** 没有任何对端自行声明的 clientInfo 字段

<details>
<summary>查看答案与解析</summary>

**答案**　D

Client 信息和 capability 是协议元数据，不是认证证据。

</details>

## 2. 批准一个工具后，gateway 应该对什么做哈希？

- **A** 当前 session 标识符
- **B** 仅 server 展示名称
- **C** 仅工具名称
- **D** 规范化后的完整 descriptor，包括描述、schema 和相关 annotation

<details>
<summary>查看答案与解析</summary>

**答案**　D

完整 descriptor 钉定可以检测只对描述做哈希会漏掉的 schema 和 annotation 变更。

</details>

## 3. gateway 应如何暴露两个都叫 search 的 backend 工具？

- **A** 让模型推断 server
- **B** 使用稳定的限定名称，例如 notes.search 和 issues.search
- **C** 随机选择一个 backend
- **D** 保留最后发现的工具

<details>
<summary>查看答案与解析</summary>

**答案**　B

限定名称让路由、批准、审计和 header 验证都指向同一个稳定工具。

</details>

## 4. 哪些 client capability 声明支持 MCP form elicitation？

- **A** 只有启用了 form 的协议 session
- **B** 隐式的 elicitation: {} 或显式的 elicitation: {form: {}} 都可以
- **C** 任何非空的 extensions 对象
- **D** 只有 elicitation.url

<details>
<summary>查看答案与解析</summary>

**答案**　B

空的 elicitation 对象隐式支持 form，而 form: {} 明确声明了它。仅 URL 支持不足以请求 form。

</details>

## 5. 为什么 requestState 必须受到完整性保护并绑定到精确参数？

- **A** 用于替代 OAuth
- **B** 让 JSON 更小
- **C** 用于选择缓存范围
- **D** 阻止 client 将确认复用或篡改到另一项操作

<details>
<summary>查看答案与解析</summary>

**答案**　D

requestState 要经过不可信对端往返，因此 server 必须检测篡改和上下文变更。共享的原子 nonce claim 可防止它在 handler 实例之间被复用。

</details>

## 6. 现代 gateway 的正确顺序是什么？

- **A** 认证、验证连线和 header、检查 capability 兼容性、授权，然后执行
- **B** 创建 session，按发现顺序路由，然后授权
- **C** 将已声明 capability 视为权限
- **D** 信任 clientInfo，执行，然后审计

<details>
<summary>查看答案与解析</summary>

**答案**　A

必须在授权和执行之前解决连线歧义和身份问题。

</details>


[返回本课](docs/zh.md)
