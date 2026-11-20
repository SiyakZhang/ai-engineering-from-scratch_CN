# Tool 合约、错误与渐进式发现 · 自测

每题先选答案，再展开解析。

## 1. 名为 search、find 和 lookup 的三个 tool 描述几乎相同。首先该修复什么？

- **A** 保留目录，但用此前成功调用的示例重新尝试选择
- **B** 建立清晰的动作、来源、用例、schema 与副作用边界
- **C** 把三个 tool 都暴露给每个角色，让 agent 能从较差的首次选择中恢复
- **D** 使用更强模型来推断重叠 schema 的差异

<details>
<summary>查看答案与解析</summary>

**答案**　B

目录移除了选择所需的信息。不同的名称、描述、反向用法、schema 与权限边界，才能从结构上修复接口。

</details>

## 2. 结构化 authorization 错误应传达什么？

- **A** 请求切换模型，并以更保守的参数重复调用
- **B** 通用失败类别和自动重试延迟，同时隐藏 policy 细节
- **C** 类别、不可重试状态、安全消息，以及正确的批准或访问下一步
- **D** 内部 stack trace 和被拒绝的身份声明，以便 agent 诊断访问问题

<details>
<summary>查看答案与解析</summary>

**答案**　C

盲目重试不会改变 authorization。harness 需要安全的类别和升级操作，同时不能泄露内部信息或凭证。

</details>

## 3. 应用何时应强制调用结构化输出 tool？

- **A** 只要对话最终可能调用 tool，就让每个回复都保持结构化
- **B** 某项操作已在 prompt 中获批，但 client 无法检查它的参数时
- **C** 模型既要格式化退款请求，又必须执行交易时
- **D** 需要无现实副作用、具有类型且经过验证的记录时

<details>
<summary>查看答案与解析</summary>

**答案**　D

仅含 schema 的 tool 可以强制输出合约。现实世界执行仍是单独获授权的操作，不应只为取得 JSON 而被强制调用。

</details>

## 4. 为什么要对大型 tool 目录使用渐进式发现？

- **A** 它能减少上下文和选择负担，同时保留小而稳定的起始界面
- **B** 它保证选中的 tool 安全，因为发现只发生在模型请求之后
- **C** 它会连同描述一起加载凭证，从而让凭证远离集成代码
- **D** 它让未发现的 tool 不可达，因此不再需要执行授权

<details>
<summary>查看答案与解析</summary>

**答案**　A

按需加载相关能力可改善上下文、选择和缓存行为；但仍需要限定范围的发现与执行授权。

</details>

## 5. 团队应把共享 MCP server 声明和个人 secret 值分别存在哪里？

- **A** 将声明和加密后的 secret 值一起提交为一份共享配置
- **B** 共享的安全声明放在项目作用域；secret 值放在环境或获批的 secret 存储中
- **C** 将 secret 引用和解析后的值保存在仅 host 可见的描述中
- **D** 把声明放入项目指令，并让每个用户在 prompt 中提供 secret

<details>
<summary>查看答案与解析</summary>

**答案**　B

项目配置支持可版本化协作；secret 值必须留在版本控制之外，并通过安全机制配置。

</details>

## 6. 一份静态 policy 文档以无副作用的 get_policy tool 暴露。哪种 MCP 原语能更直接地表达这一边界？

- **A** 分配给具备文档访问权的 policy specialist 的 agent-to-agent 任务
- **B** 确认预期用途后注入文档的 approval hook
- **C** 将 policy 作为由 URI 标识的上下文数据暴露的 resource
- **D** 只读 tool，因为由模型选择的检索总应使用 tools 原语

<details>
<summary>查看答案与解析</summary>

**答案**　C

resource 表示 host 或模型可以读取的上下文数据。tool 最适合保留给模型请求的动作或计算。

</details>


[返回本课](docs/zh.md)
