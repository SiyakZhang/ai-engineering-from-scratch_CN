# 模型交互流程 · 自测

每题先选答案，再展开解析。

## 1. host 发出 tools/call 前，模型究竟能看到工具的哪些信息？

- **A** 工具完整的服务器端实现、源码和已存储的秘密
- **B** 工具发布时所属的完整注册表 server.json 条目
- **C** 工具名称、描述、输入 schema，以及服务器提供的所有 annotations
- **D** 服务器在先前握手期间分配的缓存 session 标识符

<details>
<summary>查看答案与解析</summary>

**答案**　C

模型只能看到 tools/list 中的定义字段：name、description、inputSchema，以及服务器提供时的 annotations。它看不到服务器实现、注册表条目或 session；2026-07-28 协议中也没有这些 session。

</details>

## 2. 拟定的 close_ticket 调用指向一个完全没有 annotations 块的工具。client 发送任何内容前，host 必须做什么？

- **A** 先等待 list_changed 通知，再决定是否需要确认
- **B** 立即发送调用，因为没有 annotations 块表示工具安全
- **C** 直接拒绝调用，因为没有 annotations 的工具无效
- **D** 默认将工具视为具有破坏性，并先请求人类确认

<details>
<summary>查看答案与解析</summary>

**答案**　D

readOnlyHint 默认为 false，destructiveHint 默认为 true。因此，完全没有 annotations 块的工具依照规范默认具有破坏性，host 应在发送前请求人类确认。

</details>

## 3. tools/call 结果因缺少必填参数而返回 isError true。模型下一步应该怎么做？

- **A** 读取 content 中的解释，用修正后的参数和新 id 重试
- **B** 原样重发调用，因为大多数瞬时故障会自行恢复
- **C** 等待服务器发送 input_required 结果后再尝试
- **D** 终止整个对话，因为 isError true 始终表示调用不可重试

<details>
<summary>查看答案与解析</summary>

**答案**　A

工具执行错误是 isError 为 true 的正常结果，其中的 content 可供模型采取行动。模型会使用新 id 和修正参数重试；这与 input_required 模式是不同机制。

</details>

## 4. open_ticket 调用返回 resultType 为 input_required。客户端重试与原请求必须有何不同？

- **A** 完全省略 requestState，因为服务器已经拥有该上下文
- **B** 使用新的 JSON-RPC id，并原样回显 requestState
- **C** 复用相同的 JSON-RPC id，让服务器匹配两次调用
- **D** 改为通过新开的 subscriptions/listen stream 发送请求

<details>
<summary>查看答案与解析</summary>

**答案**　B

MRTR 重试必须使用新的 JSON-RPC id；服务器提供 requestState 时，还要逐字节原样回显。复用原 id 或自行构造其他 state 值都会破坏规范定义的模式。

</details>

## 5. 模型尝试服务器未公开的工具名称，并收到代码为 -32602 的 JSON-RPC error。循环下一步应该怎么做？

- **A** 将 error 转换成 isError true 的结果，再用修正内容重试
- **B** 开启 input_required 往返，询问用户应该使用哪个工具
- **C** 不要原样重发调用，直接继续处理，因为请求没有发生任何变化
- **D** 使用相同参数再次发送完全相同的 tools/call

<details>
<summary>查看答案与解析</summary>

**答案**　C

未知工具之类的协议错误没有给模型留下可修正内容，因此良好实现的循环不会原样重试。工具执行错误则不同，它会邀请模型用新 id 发起修正后的重试。

</details>

## 6. 对于维持长对话的 host，为什么每轮都按相同的确定性顺序返回 tools/list 很重要？

- **A** 这样 host 后续请求可以不再发送必需的协议元数据
- **B** 这是 client 打开 subscriptions/listen stream 前的硬性要求
- **C** 这样服务器后续收到调用时可以跳过参数验证
- **D** 这样能保持缓存前缀稳定，保护模型提供商自己的 prompt cache

<details>
<summary>查看答案与解析</summary>

**答案**　D

多数模型提供商会缓存容纳工具数组的 prompt 前缀。稳定、确定的顺序让 host 在多轮中复用上下文，不会使提供商缓存失效，也不必再次为工具定义付出成本。

</details>


[返回本课](docs/zh.md)
