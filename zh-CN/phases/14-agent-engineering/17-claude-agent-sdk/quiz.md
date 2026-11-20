# Harness 即库——子 agent 与会话存储 · 自测

每题先选答案，再展开解析。

## 1. Anthropic Client SDK 和 Claude Agent SDK 之间的区别是什么？

- **A** 没有区别
- **B** Client SDK 只支持 Python
- **C** Client SDK 是原始的 Messages API；Agent SDK 是 Claude Code 的 harness 形态，带内置工具、MCP、hook、子 agent 和会话存储
- **D** Client SDK 收费；Agent SDK 免费

<details>
<summary>查看答案与解析</summary>

**答案**　C

Client SDK 给你那个循环；Agent SDK 提供预先搭好的循环。

</details>

## 2. 子 agent（subagent）有文档记载的两个用途是什么？

- **A** 并行化和上下文隔离
- **B** 认证和授权
- **C** 日志和指标
- **D** 缓存和限流

<details>
<summary>查看答案与解析</summary>

**答案**　A

子 agent 并发运行独立工作，并通过隔离上下文来保住编排者的上下文预算。

</details>

## 3. 下列哪个方法不属于会话存储的接口面？

- **A** append
- **B** list_subkeys
- **C** compile_prompt
- **D** load

<details>
<summary>查看答案与解析</summary>

**答案**　C

会话存储提供 append、load、list_sessions、delete、list_subkeys；compile_prompt 不是会话 API。

</details>

## 4. 下列哪一个不是 Claude Agent SDK 的生命周期 hook？

- **A** PostToolUse
- **B** PreCompact
- **C** PreEmbedding
- **D** PreToolUse

<details>
<summary>查看答案与解析</summary>

**答案**　C

hook 包括 PreToolUse、PostToolUse、SessionStart/End、UserPromptSubmit、PreCompact、Stop、Notification。PreEmbedding 不是 hook。

</details>

## 5. trace 上下文如何跨 agent 和 CLI 子进程传播？

- **A** 通过文件系统
- **B** 通过传入 CLI 子进程的 W3C trace context 头
- **C** 只通过提供商的仪表盘
- **D** 只通过环境变量

<details>
<summary>查看答案与解析</summary>

**答案**　B

调用方的 OTel span 通过 W3C trace context 传播进 CLI 子进程，于是整个多进程运行是同一条 trace。

</details>

## 6. 什么是子 agent 过度孵化（over-spawn），它何时发生？

- **A** 为 100 个微小任务孵化 100 个子 agent，开销占主导；应改为批处理
- **B** 在 SessionStart 之前孵化
- **C** 忘记关闭子 agent
- **D** 孵化的子 agent 数量超过 CPU 核数

<details>
<summary>查看答案与解析</summary>

**答案**　A

子 agent 有开销；应对小任务做批处理，而不是每个都孵化一个。

</details>

## 7. 相比自托管的 SDK，Claude Managed Agents 做了什么权衡？

- **A** 用控制力换取托管基础设施（长时运行的异步、内置 prompt caching、内置压实）
- **B** 用延迟换成本
- **C** 用工具换记忆
- **D** 用 tracing 换流式输出

<details>
<summary>查看答案与解析</summary>

**答案**　A

Managed Agents 是面向长时异步工作的托管替代方案；更少控制力，更少运维面。

</details>


[返回本课](docs/zh.md)
