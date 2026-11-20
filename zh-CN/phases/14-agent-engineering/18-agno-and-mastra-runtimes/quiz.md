# 生产级 Agent 运行时——快速实例化与类型化工作流 · 自测

每题先选答案，再展开解析。

## 1. 本课为每个运行时推荐了哪种语言搭配？

- **A** 两者都是 Rust 优先
- **B** 两者都是 Go 优先
- **C** Agno 用 TypeScript，Mastra 用 Python
- **D** Agno 用 Python，Mastra 用 TypeScript

<details>
<summary>查看答案与解析</summary>

**答案**　D

Agno 是 Python（FastAPI 形态）；Mastra 是 TypeScript（Vercel AI SDK 形态）。

</details>

## 2. Agno 推荐的生产部署形态是什么？

- **A** 一个仅 WebSocket 的服务器
- **B** 一个无状态、会话作用域的 FastAPI 后端；每个请求启动一个全新的 agent，会话状态存在数据库里
- **C** 只用 serverless cron worker
- **D** 一个长存活的有状态守护进程

<details>
<summary>查看答案与解析</summary>

**答案**　B

每请求无状态 FastAPI；会话状态外置到数据库。

</details>

## 3. Mastra 的三个原语是什么？

- **A** Node、Edge、State
- **B** Actor、Message、Inbox
- **C** Plan、Worker、Solver
- **D** Agents、Tools、Workflows

<details>
<summary>查看答案与解析</summary>

**答案**　D

Agents（LLM + 角色）、Tools（Zod 类型化）和 Workflows 是 Mastra 的三个原语。

</details>

## 4. 按其文档，Agno 大致瞄准多少的 agent 实例化成本？

- **A** 约 2 微秒，每个 agent 约 3.75 KiB
- **B** 约 200 毫秒，每个 agent 100 MiB
- **C** 约 10 分钟，每个 agent 4 GiB
- **D** 约 1 秒，每个 agent 1 GiB

<details>
<summary>查看答案与解析</summary>

**答案**　A

Agno 文档引用每个 agent 约 2 微秒、约 3.75 KiB。

</details>

## 5. Mastra 的统一模型路由器（Unified Model Router）提供了什么？

- **A** 跨众多提供商、面向数千个模型的单一客户端接口
- **B** 一个向量数据库层
- **C** 工具调用的队列
- **D** 一个图检查点器

<details>
<summary>查看答案与解析</summary>

**答案**　A

Mastra 的统一模型路由器引用横跨 94 个提供商的 3300+ 模型。

</details>

## 6. 什么时候「为性能而性能」是选用 Agno 的错误理由？

- **A** 当使用 Langfuse 时
- **B** 当部署到 AWS 时
- **C** 当使用 Python 3.13 时
- **D** 当工作负载是每个请求一次慢的 agent 调用，且开销不是瓶颈时

<details>
<summary>查看答案与解析</summary>

**答案**　D

2 微秒在聊天扇入规模下才重要，对每请求一次慢调用并无意义。

</details>

## 7. 在 fork Mastra 之前，你应该仔细阅读哪部分许可证面？

- **A** 没有许可证文件
- **B** Mastra 要求 CLA 但无需许可证审查
- **C** Mastra 全部是 GPL
- **D** ee/ 目录是 source-available 而非 Apache 2.0，并限制商业使用

<details>
<summary>查看答案与解析</summary>

**答案**　D

Mastra 除 ee/ 外是 Apache 2.0，ee/ 是 source-available；fork 前先看清其限制。

</details>


[返回本课](docs/zh.md)
