# Agent 的 Actor 模型——异步消息与类型化运行时 · 自测

每题先选答案，再展开解析。

## 1. 在 AutoGen v0.4 中，actor 交互的唯一合法方式是什么？

- **A** 互相修改对方的 prompt
- **B** 直接访问一个共享 dict
- **C** 通过收件箱交换异步消息；没有共享内存
- **D** 共享 SQL 事务

<details>
<summary>查看答案与解析</summary>

**答案**　C

actor 拥有私有状态和一个收件箱；消息是唯一的交互方式。

</details>

## 2. AutoGen v0.4 的三个 API 层是什么？

- **A** Plan、Act、Reflect
- **B** Tools、Models、Memory
- **C** Core、AgentChat、Extensions
- **D** Frontend、Backend、Database

<details>
<summary>查看答案与解析</summary>

**答案**　C

Core 是底层的 actor 框架，AgentChat 是任务驱动的高层 API，Extensions 是各种集成。

</details>

## 3. 为什么把投递（delivery）与处理（handling）解耦能带来故障隔离？

- **A** 运行时在失败时重启操作系统
- **B** 处理器是纯函数
- **C** 每个 actor 跑在单独的机器上
- **D** 运行时在 B 中捕获处理器失败而不让 A 崩溃；A 的 send() 立即返回，从不阻塞

<details>
<summary>查看答案与解析</summary>

**答案**　D

send() 把消息放进接收方的收件箱然后返回；处理器崩溃是该 actor 局部的事情。

</details>

## 4. 哪种 AgentChat 拓扑按固定顺序轮转 agent？

- **A** Supervisor
- **B** RoundRobinGroupChat
- **C** Magentic-One
- **D** SelectorGroupChat

<details>
<summary>查看答案与解析</summary>

**答案**　B

RoundRobinGroupChat 是固定轮转；SelectorGroupChat 用一个选择器来挑下一个。

</details>

## 5. 本课中的 Magentic-One 是什么？

- **A** 一个新的 LLM 模型
- **B** 一个构建在 AgentChat 之上、用于网页浏览、代码执行和文件处理的参考多 agent 团队
- **C** 一种序列化格式
- **D** 一个 OTel 导出器

<details>
<summary>查看答案与解析</summary>

**答案**　B

Magentic-One 是微软用来演示 AgentChat API 的参考团队。

</details>

## 6. 本课所述 AutoGen v0.4 在 2026 年初的状态是什么？

- **A** 被 LangGraph 取代
- **B** 已弃用并移除
- **C** 稳定但处于维护模式；Microsoft Agent Framework 是向前的路径
- **D** 刚刚发布

<details>
<summary>查看答案与解析</summary>

**答案**　C

AutoGen v0.7.x 对研究是稳定的；活跃开发已转向 Microsoft Agent Framework。

</details>

## 7. AutoGen v0.4 默认发出哪种可观测性标准？

- **A** StatsD
- **B** 仅 Prometheus 指标
- **C** 带 gen_ai.* 属性的 OpenTelemetry span，遵循 OTel GenAI 语义约定
- **D** Datadog APM

<details>
<summary>查看答案与解析</summary>

**答案**　C

每条消息都发出一个 span；工具调用按 OTel GenAI 约定携带 gen_ai.* 属性。

</details>


[返回本课](docs/zh.md)
