# 长时间运行的工作与 Tasks Extension · 自测

每题先选答案，再展开解析。

## 1. 服务器为什么不能一直保持连接，直到二十分钟的 pipeline 完成？

- **A** 传输 timeout、执行中没有输入通道，而且完全无法在崩溃后恢复
- **B** 因为 MCP 要求每个工具调用都必须使用 tasks extension
- **C** 因为客户端总会在恰好一条请求完成后关闭连接
- **D** 因为 JSON-RPC 禁止任何请求花费超过一秒才能响应

<details>
<summary>查看答案与解析</summary>

**答案**　A

阻塞会遭遇服务器无法设置的传输 timeout；调用中途没有请求输入的通道；崩溃或连接中断后也无法恢复。

</details>

## 2. 客户端应在何处声明当前请求支持 io.modelcontextprotocol/tasks？

- **A** 在服务器之前返回的 tools/list 响应的 tasks 字段中
- **B** 在该请求自身 params._meta 的 clientCapabilities.extensions 字段中
- **C** 在第一次成功工具调用后服务器签发的 session header 中
- **D** 在双方为整条连接记住的一次性 initialize handshake 中

<details>
<summary>查看答案与解析</summary>

**答案**　B

extension 支持按请求声明，位置是 params._meta 内的 clientCapabilities.extensions，因为没有 session 或 handshake 可以让服务器记住之前的声明。

</details>

## 3. tasks/get 响应显示 resultType 为 complete，内嵌 status 为 working。这种组合表示什么？

- **A** poll 请求和底层 job 都已完全结束
- **B** 客户端必须重新发送 tools/call 才能让底层 job 继续
- **C** poll 请求本身成功，但底层 job 仍在运行
- **D** 服务器因为 task 尚不可读取而拒绝了 poll

<details>
<summary>查看答案与解析</summary>

**答案**　C

tasks/get 每次都会完成，因此自身 resultType 是 complete；job 的真实状态位于独立的内嵌 status 字段，此处仍为 working。

</details>

## 4. task 进入 input_required，tasks/get 返回 inputRequests map。客户端应如何响应？

- **A** 继续等待，因为 input_required task 无需答复就会自动恢复
- **B** 使用新 id 和相同 inputRequests key 重试原始 tools/call
- **C** 自行向服务器直接发起新的 elicitation/create request
- **D** 发送 tasks/update，并用尚未完成的条目 key 组织 inputResponses

<details>
<summary>查看答案与解析</summary>

**答案**　D

task 输入通过 tasks/update 回答，其中 inputResponses 以尚未完成的条目为 key；客户端不会为此重发原始 tools/call。

</details>

## 5. tools/call 的 content 中以 isError true 结束。其 task 会进入什么 status？

- **A** completed，因为工具调用仍产生了自身正常定义的结果
- **B** cancelled，因为结果中的错误等同于隐式取消
- **C** input_required，因为模型必须先批准该错误才算完成
- **D** failed，因为结果任何位置出现错误都视为 JSON-RPC 失败

<details>
<summary>查看答案与解析</summary>

**答案**　A

带 isError true 的工具结果仍是成功的协议交互，因此 task 进入 completed；failed 只保留给执行期间的 JSON-RPC 错误，而不是工具层失败。

</details>

## 6. 哪项工作最适合 tasks extension，而不是普通调用或 MRTR 往返？

- **A** 读取一个在不同请求间内容始终不变的资源
- **B** 可能暂停等待批准、且可能超过 timeout 的 deploy pipeline
- **C** 向新连接的客户端列出服务器当前暴露的工具
- **D** 在完成当前请求前让用户确认一个值

<details>
<summary>查看答案与解析</summary>

**答案**　B

工作可能超过 timeout、执行中暂停等待输入，或需要跨重启与取消存活时，task 的额外复杂度才值得；其他选项不符合这些条件。

</details>


[返回本课](docs/zh.md)
