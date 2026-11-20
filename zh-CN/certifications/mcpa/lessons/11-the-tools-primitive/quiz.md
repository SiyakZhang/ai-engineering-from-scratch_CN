# Tools primitive：调用操作并读取结果 · 自测

每题先选答案，再展开解析。

## 1. tools/list 请求已经返回部分工具，并携带值为空字符串、而非字段缺失的 nextCursor。客户端下一步应该怎么做？

- **A** 再次发送 tools/list，并把 cursor 设为空字符串，因为字段存在本身就表示还有内容
- **B** 不带 cursor 原样重复请求，因为空字符串绝不可能是有效 cursor
- **C** 等待 notifications/tools/list_changed 消息后才能请求下一页
- **D** 立即停止分页，因为空 nextCursor 始终表示服务器没有更多内容

<details>
<summary>查看答案与解析</summary>

**答案**　A

只要结果中存在 nextCursor，即使值为空字符串，也表示可能还有更多工具；只有该字段缺失才表示列表结束。

</details>

## 2. 工具调用成功，服务器结果完全省略 isError。合规客户端必须如何理解该结果？

- **A** 视为 isError true，因为缺失字段始终应采用更谨慎的解释
- **B** 视为 isError false，因为 isError 缺失表示整个工具调用成功
- **C** 视为无效，因为每个 CallToolResult 都必须包含 isError
- **D** 视为未定义，因此客户端必须询问服务器本意是什么

<details>
<summary>查看答案与解析</summary>

**答案**　B

CallToolResult 将缺失的 isError 视为 false；只有工具执行任务时遇到问题，才需要显式将该字段设为 true。

</details>

## 3. 客户端调用 tools/call，指定了服务器从未注册的工具。哪种响应符合 MCP 2026-07-28？

- **A** 返回普通 result，将 isError 设为 true，并携带空 content 列表
- **B** 返回代码为 -32601 的 JSON-RPC error，因为服务器找不到 method 本身
- **C** 返回代码为 -32602 的 JSON-RPC error，因为调用指定了未注册工具
- **D** 返回 input_required 结果，要求客户端立即选择其他工具

<details>
<summary>查看答案与解析</summary>

**答案**　C

未知工具属于协议错误，应返回 -32602 Invalid params；-32601 保留给服务器完全无法识别的 JSON-RPC method，而不是缺失工具。

</details>

## 4. 工具定义完全没有 annotations 对象。客户端必须对它的行为作何假设？

- **A** 工具会悄悄继承客户端上一次调用工具的 annotations
- **B** 服务器明确提供 annotations 前，该工具完全不能被列出
- **C** readOnlyHint 为 true、destructiveHint 为 false，也就是 schema 允许的最安全组合
- **D** 采用 schema 默认值：readOnlyHint false、destructiveHint true、idempotentHint false、openWorldHint true

<details>
<summary>查看答案与解析</summary>

**答案**　D

ToolAnnotations 的默认值是 readOnlyHint false、destructiveHint true、idempotentHint false、openWorldHint true。annotations 对象缺失时，客户端采用这些谨慎默认值，而不能擅自假设安全。

</details>

## 5. 客户端已打开 toolsListChanged 为 true 的 subscriptions/listen stream，此时服务器工具列表新增一项。客户端如何得知变化？

- **A** 服务器在该 stream 上发送 notifications/tools/list_changed，并标注其 subscription id
- **B** 服务器不经请求，直接在同一开放 stream 上重发完整 tools/list 结果
- **C** 下一次 tools/call 响应会悄悄把新工具放入自己的 content 列表
- **D** 客户端必须关闭并重新建立整条连接，才能看到新工具

<details>
<summary>查看答案与解析</summary>

**答案**　A

已订阅客户端通过 notifications/tools/list_changed 得知工具列表变化。消息携带打开该 stream 的 listen 请求对应的 subscriptionId，随后客户端再用普通 tools/list 重新获取。

</details>

## 6. 工具需要把模型指向一个大文件，而不是把文件内容内联到结果。应使用哪种 content block，且至少必须携带什么？

- **A** image block，把文件渲染成小型预览缩略图
- **B** resource_link block，至少携带文件的 uri 和 name
- **C** text block，只携带纯字符串文件路径，不需要其他字段
- **D** resource block，把文件完整文本或 base64 blob 内联到结果

<details>
<summary>查看答案与解析</summary>

**答案**　B

resource_link block 通过 uri 和 name 指向资源，而不内联内容，适合模型可能根本无需完整读取的大型内容。

</details>


[返回本课](docs/zh.md)
