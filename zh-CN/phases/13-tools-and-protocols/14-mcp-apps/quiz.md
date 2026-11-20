# 无状态协议上的 MCP Apps · 自测

每题先选答案，再展开解析。

## 1. 现代 MCP App 应在何处将其 UI 资源绑定到工具？

- **A** 在独立的 HTTP GET 流中
- **B** 在 tools/list 返回的工具定义中
- **C** 在 MCP 会话 cookie 中
- **D** 只在最终文本结果中

<details>
<summary>查看答案与解析</summary>

**答案**　B

工具定义上嵌套的 _meta.ui.resourceUri 让宿主能在调用前预加载并审查 UI。

</details>

## 2. 2026-07-28 client 如何声明对 MCP Apps 的支持？

- **A** 接受所有 ui:// 资源
- **B** 使用 Mcp-Session-Id
- **C** 在每个请求的 io.modelcontextprotocol/clientCapabilities.extensions 中声明
- **D** 使用 notifications/initialized

<details>
<summary>查看答案与解析</summary>

**答案**　C

扩展通过每个请求的 client 能力映射选择加入。

</details>

## 3. ui/initialize 初始化的是什么？

- **A** Streamable HTTP GET 通道
- **B** 协议级 server 会话
- **C** OAuth client 注册
- **D** iframe 与宿主之间的 Apps postMessage 桥接

<details>
<summary>查看答案与解析</summary>

**答案**　D

ui/initialize 属于 Apps 桥接方言，与已移除的 MCP 核心握手分离。

</details>

## 4. 对一个与用户无关的打包 App，哪种资源响应最安全？

- **A** 在 HTML 中嵌入会话 token
- **B** ttlMs 无上限且 CSP 域名通配
- **C** resultType 为 complete、ttlMs 有上限、cacheScope 为 public，且 CSP 默认拒绝
- **D** 没有 resultType，也没有缓存策略

<details>
<summary>查看答案与解析</summary>

**答案**　C

完整结果、显式缓存提示和收窄的 CSP 让传输与浏览器策略都可审查。

</details>

## 5. 宿主收到一个读取某 URI 的 resources/read body，但 Mcp-Name 请求头指向不同 URI。应如何处理？

- **A** 打开两个资源
- **B** 优先使用请求头
- **C** 返回 HTTP 400 和 JSON-RPC 错误 -32020
- **D** 优先使用 body

<details>
<summary>查看答案与解析</summary>

**答案**　C

应在评估版本支持或功能策略前匹配路由请求头与 body；传输返回 HTTP 400 和 JSON-RPC 错误 -32020。

</details>

## 6. 未支持 MCP Apps 的宿主应使用什么正确回退？

- **A** 自动授予扩展
- **B** 让工具通过普通文本或结构化输出继续可用，并省略 UI 绑定
- **C** 将 HTML 作为受信任的宿主 chrome 返回
- **D** 创建隐藏会话后重试

<details>
<summary>查看答案与解析</summary>

**答案**　B

可选扩展不能让底层工具对未协商该扩展的 client 失效。

</details>


[返回本课](docs/zh.md)
