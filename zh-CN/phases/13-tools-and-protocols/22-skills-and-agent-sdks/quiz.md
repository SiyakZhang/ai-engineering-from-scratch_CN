# Agent Skills：可移植契约与运行时边界 · 自测

每题先选答案，再展开解析。

## 1. 团队有可复用审查方法，也有提供拉取请求数据的既有 API。按运行时策略，如何将各项职责分配给正确原语？

- **A** 用更长的用户 prompt 替代 API
- **B** 仅用生命周期 hook 提供审查指令
- **C** 将方法和 API 实现都放进 AGENTS.md
- **D** 将审查方法放入 Agent Skill，并通过 MCP 工具暴露 API

<details>
<summary>查看答案与解析</summary>

**答案**　D

Skill 承载可复用的过程性知识，MCP 暴露外部能力，二者可以组合。AGENTS.md 更适合仓库级默认规则；hook 响应生命周期事件，不能替代两者。

</details>

## 2. 为什么验证器应要求 SKILL.md 的 name 与所在目录匹配？

- **A** 它让 Markdown 标题正确渲染
- **B** 它让发现与打包共享一个稳定标识，而不是两个冲突名称
- **C** 它让 skill 绕过 host 权限
- **D** 它保证每个 host 支持相同调用语法

<details>
<summary>查看答案与解析</summary>

**答案**　B

发现工具常按文件夹和 frontmatter 同时索引 skill。两者匹配能避免目录条目歧义和安装路径损坏；它不会授予权限，也不会统一 host 的调用 UI。

</details>

## 3. SKILL.md 包含只有一个运行时理解的字段时，可移植的解释是什么？

- **A** 每个运行时都必须实现它才能加载 skill
- **B** 把字段移进 skill 名称
- **C** 该字段会悄悄成为核心标准的一部分
- **D** 将其视为 host 扩展，只在显式 host 策略下验证

<details>
<summary>查看答案与解析</summary>

**答案**　D

可移植核心元数据与 host 运行时扩展是不同契约。适配器可以识别扩展，但核心验证器不应声称该字段具有普遍语义。

</details>

## 4. 每次工具调用后都必须运行的检查，最适合用哪个原语表示？

- **A** 仓库术语表
- **B** 生命周期 hook
- **C** 一次性 prompt
- **D** MCP resource

<details>
<summary>查看答案与解析</summary>

**答案**　B

决定性要求是事件时机，因此生命周期 hook 是正确机制。Skill 可解释流程，MCP 可暴露能力，但两者都不会天然在每次工具调用后触发。

</details>

## 5. 什么时候 AGENTS.md 比 Agent Skill 更适合作为归宿？

- **A** 约定应贯穿仓库内所有工作时
- **B** 外部服务需要经过身份验证的 API 调用时
- **C** 指令只应为罕见的专业任务加载时
- **D** 脚本需要在工作区 jail 外执行时

<details>
<summary>查看答案与解析</summary>

**答案**　A

AGENTS.md 传达构建命令和编码约定等长期仓库上下文。任务专属流程适合 skill，外部操作适合工具，任何指令文件都不应用于逃逸沙箱。

</details>

## 6. 有效的 Agent Skill 本身授予什么？

- **A** 每个 agent host 中通用的斜杠命令
- **B** 可发现的过程性指令，仍受 host 运行时策略约束
- **C** 执行每个随附脚本的权限
- **D** 自动网络访问

<details>
<summary>查看答案与解析</summary>

**答案**　B

可移植产物提供元数据和指令。发现、调用 UI、工具访问、审批和脚本执行仍是运行时职责，因此有效性不等于授权。

</details>


[返回本课](docs/zh.md)
