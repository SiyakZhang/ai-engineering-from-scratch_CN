# Agent 框架取舍——图、角色与 Actor 编排 · 自测

每题先选答案，再展开解析。

## 1. 对于一个必须在崩溃后恢复、在运行中途接受人工审批、并向三个检索器并行扇出的工作流，正确的首选框架是哪个？

- **A** AutoGen
- **B** CrewAI
- **C** Agno
- **D** LangGraph

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 2. 为什么由 LLM 选择的路由比显式路由每轮花费更多 token？

- **A** 每一轮都有一次 planner LLM 调用来挑选下一步，为每个决策增加 prompt 和 completion token。
- **B** 它把整个对话历史发给一个验证模型。
- **C** 它并行预取下一个节点以对冲延迟。
- **D** 它为 crew 中的每个 agent 复制工具列表。

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 3. 代码审查中的提议者-批评者（proposer-critic）对话，天然地映射到哪个框架的核心抽象？

- **A** AutoGen 的 GroupChat / ConversableAgent 配对
- **B** Agno 的带工具的单个 Agent
- **C** CrewAI 的顺序式 Crew
- **D** LangGraph 的 StateGraph

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 4. 哪个框架内置了直接挂在 Agent 类上的存储驱动（SQLite、Postgres、Redis、Mongo、DynamoDB），用于会话和记忆持久化？

- **A** LangGraph
- **B** CrewAI
- **C** AutoGen
- **D** Agno

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 5. 你有一个两次调用的摘要器：取文本、做摘要。哪个选项是正确的框架选择？

- **A** 带 researcher + summarizer 角色的 CrewAI —— 角色让它更清晰。
- **B** 纯 Python 加提供商 SDK —— 对于微型流水线，不用框架就是最快的框架。
- **C** AutoGen GroupChat —— 两个 agent 可以争论哪个摘要最好。
- **D** LangGraph StateGraph —— 为了可靠性总是用框架。

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>


[返回本课](docs/zh.md)
