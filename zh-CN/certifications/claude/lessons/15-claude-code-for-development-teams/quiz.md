# Claude Code 靠共享约束支持规模化协作 · 自测

每题先选答案，再展开解析。

## 1. 项目 CLAUDE.md 最重要的用途是什么？

- **A** 记录项目环境值，包括常用开发命令需要的 secret
- **B** 作为精简的上手合约，包含命令、布局与不直观的约束
- **C** 用更强的自然语言仓库规则取代确定性测试与 hook
- **D** 保存完整 API 参考，让每个 session 无需打开其他文件就能工作

<details>
<summary>查看答案与解析</summary>

**答案**　B

精简的项目指南提供反复需要的仓库事实，并指向更深入的来源，避免每个 session 都背负整本手册。

</details>

## 2. 开发者希望 Claude Code 无需询问即可编辑文件，但其他终端命令仍需批准。哪种 permission mode 符合该边界？

- **A** default
- **B** bypassPermissions
- **C** acceptEdits
- **D** dontAsk

<details>
<summary>查看答案与解析</summary>

**答案**　C

acceptEdits 取消逐次编辑批准，同时保留其他命令的权限检查。它不会授权发布、部署或任意 shell 操作。

</details>

## 3. 为什么团队 settings 与 hook 必须像代码一样接受审查？

- **A** 它们会影响本地开发者行为，却无法改变 headless 或自动化执行
- **B** 只有可执行 hook 才能改变权限或信任边界
- **C** 纳入版本管理后便是安全的，因为仓库历史会自动提供回滚
- **D** 它们可以改变权限、tool、执行行为与信任边界

<details>
<summary>查看答案与解析</summary>

**答案**　D

配置可以开放 shell、文件系统、网络和 MCP 能力，也能改变生命周期行为。文件能被解析，不代表它产生的实际行为安全。

</details>

## 4. command hook 应如何返回结构化的 PermissionRequest 拒绝？

- **A** 以退出码 0 退出，并在 hookSpecificOutput 中返回 PermissionRequest JSON decision
- **B** 以退出码 1 退出，并向 stderr 打印 JSON decision，让普通 Unix 失败语义阻止请求
- **C** 以退出码 0 退出并向 stdout 打印纯文本，依赖文本覆盖命中的 permission deny rule
- **D** 以退出码 2 退出并向 stdout 打印 JSON decision，让 Claude Code 解析并执行两种信号

<details>
<summary>查看答案与解析</summary>

**答案**　A

结构化控制要求退出码为 0，stdout 只输出 JSON。退出码 2 是使用 stderr 的另一条阻止路径，同时打印的 JSON 会被忽略。

</details>

## 5. 哪种 CI 设计最适合安全地自动审查 pull request？

- **A** 固定 review plugin，并在主工作目录中启用所有可用 tool
- **B** 最小权限、隔离 checkout、有界运行、结构化产物与人工审查
- **C** 只读仓库访问，加上用于 fork 变更集成测试的生产 secret
- **D** 写 token、开放网络，并在检查通过后直接 merge

<details>
<summary>查看答案与解析</summary>

**答案**　B

headless execution 移除了交互监督，因此能力、时间、token、网络与公开操作边界必须更加严格。

</details>

## 6. Anthropic managed Code Review 与官方 Claude Code GitHub Action 有什么区别？

- **A** Managed Code Review 可以读取仓库指导，而 Action 无法加载 CLAUDE.md 或 Skill
- **B** Managed Code Review 会自动成为必需的 GitHub check，而 Action 只能留下可选 comment
- **C** Managed Code Review 是托管服务；Action 在仓库自己的 workflow 中运行
- **D** Managed Code Review 仅适用于私有仓库，而 Action 仅限公开仓库

<details>
<summary>查看答案与解析</summary>

**答案**　C

Managed Code Review 在 Anthropic 基础设施上运行，只报告 finding，不会批准或阻止。官方 Action 在团队 workflow 中运行，由团队配置仓库权限、trigger、tool 与 secret。

</details>


[返回本课](docs/zh.md)
