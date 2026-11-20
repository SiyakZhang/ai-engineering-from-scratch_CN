# MCP 解决的集成难题 · 自测

每题先选答案，再展开解析。

## 1. 四个 AI 应用分别需要访问六个外部系统。使用一个共享协议需要多少套实现？

- **A** 六套，因为只有外部系统需要实现任何东西
- **B** 四套，因为只有 AI 应用需要实现任何东西
- **C** 十套，因为每个应用和每个系统各实现一次
- **D** 二十四套，因为每一对仍需自己的定制胶水代码

<details>
<summary>查看答案与解析</summary>

**答案**　C

共享协议把 N×M 配对变成 N+M 套实现：四个客户端加六个服务端，共十套。

</details>

## 2. 在 2026-07-28 修订版中，服务端如何得知一个请求使用哪个协议版本？

- **A** 读取服务端最近一次 tools/list 响应中公布的版本
- **B** 读取此前打开连接时完成的 initialize 握手
- **C** 读取服务端在第一个请求上分配的 session 标识符
- **D** 读取请求 _meta 中的 io.modelcontextprotocol/protocolVersion

<details>
<summary>查看答案与解析</summary>

**答案**　D

协议是无状态的：每个请求都在 params._meta 中携带自己的协议版本和客户端能力，不存在握手或 session。

</details>

## 3. 客户端发送 tools/call，并指定了服务端未暴露的工具。符合规范的服务端会返回什么？

- **A** JSON-RPC error -32602，因为 params 无效
- **B** input_required 结果，请用户选择其他工具
- **C** JSON-RPC error -32601，因为 method 未知
- **D** isError 为 true、content 列表为空的普通结果

<details>
<summary>查看答案与解析</summary>

**答案**　A

未知工具属于协议错误，应报告为 -32602 Invalid params；-32601 只用于未知 JSON-RPC method。

</details>

## 4. 下列哪项正确描述了各服务端 primitive 的控制方？

- **A** 三种 primitive 都由服务端运营者预先选择
- **B** tools 由模型控制，resources 由应用驱动，prompts 由用户控制
- **C** tools 由用户控制，resources 由模型控制，prompts 由应用驱动
- **D** 三种 primitive 都由模型在运行时自行选择，不经过 host

<details>
<summary>查看答案与解析</summary>

**答案**　B

模型决定何时调用 tools，host 应用决定哪些 resources 进入上下文，用户明确选择 prompts。

</details>

## 5. 调用 get_forecast 时漏掉必需的 city 参数。哪种响应最有助于模型恢复？

- **A** 返回空的成功结果，让对话继续
- **B** 返回 JSON-RPC error -32603，报告服务端内部故障
- **C** 返回 isError 为 true 的结果，说明必须提供 city
- **D** 返回由 host 对模型隐藏的 JSON-RPC error -32602

<details>
<summary>查看答案与解析</summary>

**答案**　C

输入问题属于工具执行错误：isError 为 true 的普通结果能让模型读取说明，并补充 city 后重试。

</details>

## 6. 以下哪项是 MCP 刻意留给 host 应用决定，而不是由协议标准化的？

- **A** 服务端如何向连接的客户端描述其工具
- **B** 客户端如何调用工具并读取返回结果
- **C** 结果与错误在线上传输时采用什么形状
- **D** host 使用哪个模型，以及如何组装模型 prompt

<details>
<summary>查看答案与解析</summary>

**答案**　D

MCP 标准化应用与系统之间的对话；模型选择和 prompt 构建仍由 host 决定。

</details>


[返回本课](docs/zh.md)
