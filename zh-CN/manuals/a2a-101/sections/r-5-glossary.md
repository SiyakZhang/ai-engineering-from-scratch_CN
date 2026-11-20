# 术语表

> 下列术语在全手册保持同一含义，链接指向定义它的章节。

| 术语 | 本手册中的含义 | 定义章节 |
|---|---|---|
| A2A 错误 | 规范定义并映射到各绑定的九种错误之一，如 `TaskNotFoundError` | [5.5](5-5-errors.md) |
| agent 卡片 | 描述 agent 的 JSON 文档，通常位于 `/.well-known/agent-card.json` | [2.1](2-1-agentcard-fields.md) |
| 产物 | 由 part 构成的任务输出，长产物分块到达 | [3.3](3-3-artifact-and-chunks.md) |
| 阻塞调用 | 等待终态或中断态的发送，默认行为 | [4.1](4-1-send-message.md) |
| 能力 | 允许一组操作的卡片标志，如 `streaming` | [2.1](2-1-agentcard-fields.md) |
| 卡片签名 | `signatures` 条目，覆盖卡片 RFC 8785 规范形式的 JSON Web Signature | [2.3](2-3-extended-cards-and-signatures.md) |
| 上下文 | 用一个 `contextId` 归组任务与消息的对话 | [3.5](3-5-context-id.md) |
| 直接回复 | 不带任务、作为发送完整结果的 `Message` | [4.1](4-1-send-message.md) |
| 扩展卡片 | `GetExtendedAgentCard` 向已认证客户端返回的更完整卡片 | [2.3](2-3-extended-cards-and-signatures.md) |
| 扩展 | 以 URI 命名、在 `capabilities.extensions` 声明、用 `A2A-Extensions` 激活的协议补充 | [6.2](6-2-extensions.md) |
| 历史 | 任务保存的消息，由 `historyLength` 限制 | [4.3](4-3-get-task-and-list-tasks.md) |
| 任务内授权 | agent 在任务中途请求权限，任务在 `TASK_STATE_AUTH_REQUIRED` 等待从 A2A 外部到达的回答 | [6.1](6-1-security-schemes-and-in-task-authorization.md) |
| 接口 | `supportedInterfaces` 条目，含 URL、协议绑定、协议版本和可选 tenant | [2.1](2-1-agentcard-fields.md) |
| 中断态 | `TASK_STATE_INPUT_REQUIRED` 或 `TASK_STATE_AUTH_REQUIRED`，任务等待 | [4.2](4-2-input-required-and-auth-required.md) |
| Message | 一轮对话，带 `messageId`、`role` 和 parts | [3.1](3-1-message.md) |
| 不透明 | 对调用者隐藏，不透明 agent 只展示返回内容 | [1.1](1-1-what-a2a-standardizes.md) |
| Part | 最小内容单元，含 `text`、`raw`、`url` 或 `data` 之一 | [3.2](3-2-part.md) |
| 轮询 | 重复调用 `GetTask` 跟踪任务 | [4.1](4-1-send-message.md) |
| 协议绑定 | 操作的一种具体形式：JSON-RPC、gRPC 或 HTTP+JSON | [5.1](5-1-json-rpc.md) |
| 推送通知 | 向客户端注册的 webhook HTTP POST 一个 `StreamResponse` | [4.6](4-6-push-notification-configs.md) |
| 远程 agent | A2A 端点背后接收消息并运行任务的 agent | [1.1](1-1-what-a2a-standardizes.md) |
| 安全要求 | `securityRequirements` 条目，将方案名映射到请求所需 scope | [6.1](6-1-security-schemes-and-in-task-authorization.md) |
| 安全方案 | 有名称的认证方式，在卡片 `securitySchemes` 声明 | [6.1](6-1-security-schemes-and-in-task-authorization.md) |
| 服务参数 | 每次请求的键，如 `A2A-Version`，通过 HTTP 头或 gRPC metadata 发送 | [5.4](5-4-version-and-extension-headers.md) |
| 技能 | 卡片 `skills` 条目，如 `run-tests` | [2.1](2-1-agentcard-fields.md) |
| 状态消息 | `TaskStatus` 可包含的一条 `message`，如问题或原因 | [3.1](3-1-message.md) |
| 流 | 由 `StreamResponse` 帧构成的 Server-Sent Events 或 gRPC 流，`SubscribeToTask` 在任务上打开流 | [4.5](4-5-streaming-and-subscribe-to-task.md) |
| Task | 服务器响应消息创建的工作单元，带 `id` 和 `TaskState` | [3.4](3-4-task-and-task-state.md) |
| Tenant | 接口上的可选路由字符串，复制到发给该接口的每个请求 | [5.2](5-2-http-json.md) |
| 终态 | `TASK_STATE_COMPLETED`、`TASK_STATE_FAILED`、`TASK_STATE_CANCELED`、`TASK_STATE_REJECTED`，任务不再变化 | [4.4](4-4-cancel-task-and-terminal-states.md) |

Sources: spec §1, §1.2, §1.3, §2.2, §3.2.2, §3.2.6, §3.4.1, §3.4.2, §3.7, §4.6, §7.3, §7.6.1, §8.2, §8.3.2, §8.4, §B (research/sources/specification.md); proto TaskState, Role, Message, Part, Artifact, TaskStatus, TaskPushNotificationConfig, AgentCard, AgentCapabilities, AgentExtension, AgentInterface, SecurityRequirement (research/sources/a2a.proto); the definition paragraphs of sections 1.1 to 6.2; capture/planner.py, capture/agents.py, capture/out/05-streaming.events.json

---

[返回中文手册目录](../../README.md) · [本节英文原文](../../../../manuals/a2a-101/sections/r-5-glossary.md)
