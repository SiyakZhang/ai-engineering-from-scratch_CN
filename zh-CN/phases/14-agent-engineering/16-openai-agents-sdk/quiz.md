# OpenAI Agents SDK：交接、护栏与追踪 · 自测

每题先选答案，再展开解析。

## 1. OpenAI Agents SDK 的五个原语是什么？

- **A** Tool、Prompt、Model、Memory、Trace
- **B** Node、Edge、Reducer、Checkpointer、Subgraph
- **C** Plan、Worker、Solver、Evaluator、Reflector
- **D** Agent、Handoff、Guardrail、Session、Tracing

<details>
<summary>查看答案与解析</summary>

**答案**　D

SDK 提供这五个原语。

</details>

## 2. 模型如何看到一次 handoff？

- **A** 作为一个特殊 token
- **B** 作为一个自定义 HTTP 端点
- **C** 作为一个名为 transfer_to_<agent_name> 的工具
- **D** 作为一条 system 消息

<details>
<summary>查看答案与解析</summary>

**答案**　C

handoff 以工具形式暴露，名字形态为 transfer_to_<agent>。

</details>

## 3. SDK 提供哪三种 guardrail 类型？

- **A** 前置、后置和内联 guardrail
- **B** 输入、输出和工具 guardrail
- **C** 硬、软和尽力而为 guardrail
- **D** 静态、动态和联邦 guardrail

<details>
<summary>查看答案与解析</summary>

**答案**　B

输入（首个 agent）、输出（最后一个 agent）和工具（每个函数工具）guardrail。

</details>

## 4. 并行 guardrail 和阻塞 guardrail 之间的区别是什么？

- **A** 并行总是更贵
- **B** 阻塞是异步的；并行是同步的
- **C** 并行与主 LLM 并排运行（延迟更低，触发时浪费 token）；阻塞先运行（触发时不浪费 token）
- **D** 阻塞只对输出有效

<details>
<summary>查看答案与解析</summary>

**答案**　C

并行以触发时浪费 token 为代价优化延迟；阻塞节省 token 但增加延迟。

</details>

## 5. SDK 中如何启用 tracing？

- **A** 只在托管仪表盘上
- **B** 默认开启；OPENAI_AGENTS_DISABLE_TRACING=1 可退出
- **C** 只能通过 OpenTelemetry collector
- **D** 默认关闭；按 agent 启用

<details>
<summary>查看答案与解析</summary>

**答案**　B

LLM、工具、handoff 和 guardrail 的 span 默认发出；一个环境变量可禁用它们。

</details>

## 6. 什么是 handoff 漂移（handoff drift），本课建议如何缓解？

- **A** tracing 落后；减少 span 量
- **B** guardrail 失同步；重训练
- **C** agent A 交给 B，B 又交回 A，形成循环；加一个跳数计数器（hop counter）
- **D** Session 溢出；归档旧的

<details>
<summary>查看答案与解析</summary>

**答案**　C

跳数计数器在转交链无限循环之前对其设上限。

</details>

## 7. 为什么内置工具是一个 guardrail 缺口？

- **A** 工具 guardrail 只对函数工具触发；内置工具（文件读取器、网页抓取）需要单独的策略
- **B** 它们不支持 handoff
- **C** 它们无法被 tracing
- **D** 它们比函数工具慢

<details>
<summary>查看答案与解析</summary>

**答案**　A

每工具 guardrail 覆盖函数工具；内置工具需要一个单独的策略层。

</details>


[返回本课](docs/zh.md)
