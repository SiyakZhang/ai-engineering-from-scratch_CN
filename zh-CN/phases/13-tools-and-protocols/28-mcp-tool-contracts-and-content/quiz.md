# MCP 工具契约与内容 · 自测

每题先选答案，再展开解析。

## 1. 一个工具发布了 type 为 array 的 outputSchema。哪种 structuredContent 值有效？

- **A** 元素符合已发布 schema 的数组
- **B** 任意 JSON 值，因为 outputSchema 只是文档
- **C** 不含 structuredContent 的文本块
- **D** 只能是对象，因为 MCP 结构化结果只能是对象

<details>
<summary>查看答案与解析</summary>

**答案**　A

structuredContent 可以是任意 JSON 值，包括数组；但当工具发布 outputSchema 时，它必须符合该 schema。

</details>

## 2. 一个 tools/list 结果将 nextCursor 设为空字符串。客户端应该怎么做？

- **A** 解码它以找出下一页页码
- **B** 将空字符串视为分页结束
- **C** 使用完全相同的空字符串游标再发送一次列表请求
- **D** 用游标零替换它

<details>
<summary>查看答案与解析</summary>

**答案**　C

游标值是不透明的。空字符串是有效的非 null 游标，必须原样发送回去。

</details>

## 3. 严格的部署策略应拒绝哪个标记了 x-mcp-header 的参数？

- **A** 镜像为 Dry-Run 的 boolean dry_run 字段
- **B** 镜像为 Region 的 string region 字段
- **C** 镜像为 Shard 的 integer shard 字段
- **D** 镜像为 Token 的 string token 字段

<details>
<summary>查看答案与解析</summary>

**答案**　D

协议建议不要镜像敏感值。严格的客户端准入策略应拒绝 token、password、secret、credential 和 PII 字段。

</details>

## 4. resource_link 块和嵌入式 resource 块的主要区别是什么？

- **A** 只有资源链接可以包含 URI
- **B** 嵌入式资源也必须出现在 resources/list 中
- **C** 资源链接指向稍后获取的数据，而嵌入式资源现在就携带数据
- **D** 资源链接会永远自动获得授权

<details>
<summary>查看答案与解析</summary>

**答案**　C

链接会延后获取，跟随它时需要授权。嵌入式资源将数据置于当前结果中。

</details>

## 5. 客户端应如何处理 tools/list 页面中一个格式错误的工具描述符？

- **A** 将它暴露给模型 prompt，但添加警告
- **B** 静默修复该描述符
- **C** 拒绝该工具，同时继续评估无关的其他工具
- **D** 将每一次工具执行视为 JSON-RPC 通知

<details>
<summary>查看答案与解析</summary>

**答案**　C

描述符准入以工具为单位。一个格式错误的定义应被排除，但不应导致有效工具不可用。

</details>

## 6. 哪种失败应归入 JSON-RPC 错误，而不是带 isError true 的工具结果？

- **A** 下游 API 返回可处理的、工具特定的错误
- **B** 报告数据源暂时不可用
- **C** 请求的工具名不存在
- **D** 业务规则拒绝请求的日期

<details>
<summary>查看答案与解析</summary>

**答案**　C

未知工具会阻止协议分派，应归入 JSON-RPC 错误。模型可处理的执行失败使用 isError true。

</details>


[返回本课](docs/zh.md)
