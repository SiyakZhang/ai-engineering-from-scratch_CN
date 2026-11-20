# Resources：无状态服务器中的可寻址内容 · 自测

每题先选答案，再展开解析。

## 1. 客户端针对服务器无法识别的 URI 发送 resources/read。合规的 2026-07-28 服务器必须返回什么？

- **A** JSON-RPC error -32602，并在 data 中指出请求的 URI
- **B** JSON-RPC error -32601，因为 read method 未知
- **C** contents 数组为空的 complete result
- **D** isError 设为 true 的工具执行错误 result

<details>
<summary>查看答案与解析</summary>

**答案**　A

缺失 resource 应返回 JSON-RPC error -32602，并通过 data.uri 标识请求目标；禁止使用空 contents 数组，因为它无法区分 resource 缺失和空文档。

</details>

## 2. SEP-2164 之前，服务器通常用 -32002 表示 resource 缺失。2026-07-28 服务器应如何处理该代码？

- **A** 在 stdio 上发出 -32002，在 Streamable HTTP transport 上发出 -32602
- **B** 今后使用 -32602；仍能接受旧 peer 返回的 -32002
- **C** 把 -32002 和 -32602 当作两个互不相关、无法识别的错误代码
- **D** resource 位于 file scheme 下时就发出 -32002

<details>
<summary>查看答案与解析</summary>

**答案**　B

SEP-2164 将 resource not found 标准化为普通的 Invalid params 代码 -32602。2026-07-28 服务器自身不得再发出 -32002，但客户端仍应识别旧 peer 返回的该代码。

</details>

## 3. resources/read 调用成功并返回 resultType complete。除了 contents，结果还必须携带哪两个字段？

- **A** nextCursor 和 pageSize，供客户端分页读取内容
- **B** supportedVersions 和 capabilities，供客户端重新协商版本
- **C** ttlMs 和 cacheScope，也就是缓存的新鲜度与共享提示
- **D** inputRequests 和 requestState，供客户端带输入重试

<details>
<summary>查看答案与解析</summary>

**答案**　C

Resources/read 是六个可缓存操作之一；complete result 必须携带 ttlMs（客户端可将内容视为新鲜内容的时长）和 cacheScope（public 或 private）。

</details>

## 4. 服务器持有一份只有自身可以访问的文档，客户端无法直接从开放 Web 获取相同字节。应采用哪条 URI scheme 指导？

- **A** 使用 https，因为任何 URI 都可以标记为可直接获取
- **B** 只有 resource 确实受版本控制时才使用 git
- **C** 使用 https，再通过 header 告诉客户端跳过它
- **D** 使用 file 或自定义 scheme；https 留给客户端可直接获取的内容

<details>
<summary>查看答案与解析</summary>

**答案**　D

规范将 https 留给客户端无需经过服务器就能直接从 Web 获取的内容；只有服务器能访问的内容应使用 file、git 或服务器自定义 scheme。

</details>

## 5. resource read 返回一条只属于某个已认证用户的笔记。哪个 cacheScope 能防止该结果泄漏到另一用户的缓存？

- **A** private，使缓存副本绝不跨越授权上下文
- **B** public，因为笔记体积小，可以安全共享
- **C** private，但只在 transport 为 stdio 时
- **D** public，并搭配非常短的 ttlMs

<details>
<summary>查看答案与解析</summary>

**答案**　A

cacheScope private 表示缓存响应可以在同一授权上下文中复用，但绝不能在不同调用方之间共享，正适合用户专属内容。

</details>

## 6. 客户端想知道某个特定 resource 何时变化。按照 2026-07-28 修订版，它应该发送什么？

- **A** server/discover，并把 capabilities.resources.subscribe 设为 true
- **B** subscriptions/listen，在 resourceSubscriptions 下列出 URI
- **C** 像早期版本那样发送指定 URI 的 resources/subscribe
- **D** 按很短的轮询间隔重复 resources/read

<details>
<summary>查看答案与解析</summary>

**答案**　B

独立的 resources/subscribe 请求已经废弃；客户端现在发送 subscriptions/listen，并在 resourceSubscriptions filter 中列出要监控更新的 URI。

</details>


[返回本课](docs/zh.md)
