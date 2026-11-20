# LangChain 101 中文导读

这份手册从选型开始，追踪一个智能体如何调用工具、流式返回结果、暂停等待审批，以及在进程重启后从检查点恢复。最后一部分把这些能力接入一个使用 FastAPI 和 PostgreSQL 的服务。

这里提供中文导读和对应的英文章节。手册共 9 部分、60 节正文和 11 节参考，完整章节可在英文版中阅读。 [英文仓库说明](../../../manuals/langchain-101/README.md) · [英文前言](../../../manuals/langchain-101/front.md) · [英文网页版目录](https://aiengineeringfromscratch.com/manual-langchain-101.html)

## 先区分四个项目

| 项目 | 手册使用的版本 | 在本手册中承担的工作 |
| --- | --- | --- |
| LangChain | `langchain` 1.5.0、`langchain-core` 1.8.0 | 提供模型、消息与工具接口。`create_agent` 组装模型和工具调用循环。 |
| LangGraph | `langgraph` 1.2.22 | 执行由节点、边和共享状态组成的图，管理流式事件、检查点和中断恢复。 |
| LangSmith | `langsmith` 0.14.17 | 记录和查看运行轨迹，组织评估，管理部署。 |
| Deep Agents | `deepagents` 0.7.38 | 在智能体循环上加入文件工具、子智能体、规划和上下文管理。 |

这些版本是英文手册记录实验时固定的依赖。复现实验所用的精确依赖见锁定版本文件。 [依赖版本](../../../manuals/langchain-101/capture/requirements.txt) · [四个项目的分工（英文）](../../../manuals/langchain-101/sections/1-1-langchain-langgraph-langsmith-and-deep-agents.md)

## 框架怎么选

如果你已经有一个工具调用循环，先写下新增框架需要解决的具体问题，例如流式反馈、人工审批、失败恢复或跨模型的统一消息格式。手册用同一组任务比较手写循环、`create_agent`、手写 `StateGraph` 和 Deep Agents。实验会检查运行后的数据库、文件或其他状态，避免只凭智能体声称“已完成”计分。

在原文所测的任务和配置中，前三种实现对共同运行的任务逐题一致。Deep Agents 在手册测试的小型本地模型上通过的任务更少。评估自己的工作负载时，固定模型、工具和测试输入，分别比较通过率、耗时、token 用量和成本。 [选型对比与实验结果（英文）](../../../manuals/langchain-101/sections/1-2-do-you-need-langchain.md)

## 分章阅读

| 部分 | 阅读时要回答的问题 | 英文章节入口 |
| --- | --- | --- |
| 1. 选型与首次运行 | 模型在哪一步决定调用工具？工具结果如何回到消息历史？ | [跟踪一次 `create_agent` 运行](../../../manuals/langchain-101/sections/1-3-one-create-agent-run.md) |
| 2. LangGraph 运行机制 | 同一轮内的节点何时读取状态、写入通道、提交检查点？ | [超步循环](../../../manuals/langchain-101/sections/2-1-the-superstep-loop-plan-execute-update.md) |
| 3. 安装与基础接口 | 如何选择模型、组织消息并定义工具参数？ | [安装与包结构](../../../manuals/langchain-101/sections/3-1-install-and-the-package-map.md) |
| 4. 智能体循环 | 怎样配置结构化输出、中间件、重试与防护规则？ | [`create_agent` 生成的图](../../../manuals/langchain-101/sections/4-1-create-agent-and-the-graph-it-builds.md) |
| 5. 流式输出与持久化 | 哪些数据属于单次运行、单个会话或跨会话存储？ | [流式接口及工具事件](../../../manuals/langchain-101/sections/5-1-streaming-v1-v2-stream-events-v3-and-the-tools-mode.md) |
| 6. 图与控制流 | 如何用节点、条件边、状态合并与中断表达工作流？ | [`StateGraph` 的状态与合并函数](../../../manuals/langchain-101/sections/6-1-stategraph-state-and-reducers.md) |
| 7. 检索、MCP 与可观测性 | 如何接入检索和 MCP，并用运行轨迹检查结果？ | [嵌入、文本切分、向量存储与检索器](../../../manuals/langchain-101/sections/7-1-embeddings-splitters-vector-stores-and-retrievers.md) |
| 8. 部署与排障 | 如何定位服务错误、管理升级、控制权限和成本？ | [Agent Server 的开发与部署入口](../../../manuals/langchain-101/sections/8-1-agent-server-langgraph-dev-up-and-deploy.md) |
| 9. 生产服务 | 如何把审批、持久化、故障测试和评估接入同一个服务？ | [运行接口与事件流](../../../manuals/langchain-101/sections/9-1-the-run-endpoint-and-its-stream.md) |

## 配套中文课程

- [智能体循环](../../phases/14-agent-engineering/01-the-agent-loop/docs/zh.md)
- [LangGraph 有状态图](../../phases/14-agent-engineering/13-langgraph-stateful-graphs/docs/zh.md)
- [持久化执行](../../phases/15-autonomous-systems/12-durable-execution/docs/zh.md)
- [检查点与回滚](../../phases/15-autonomous-systems/16-checkpoints-rollback/docs/zh.md)

[返回中文工程手册目录](../README.md)
