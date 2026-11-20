# 记忆块与休眠时计算 · 自测

每题先选答案，再展开解析。

## 1. Letta 的三个记忆层级是什么？

- **A** RAM、swap、disk
- **B** Cache、KV、archival
- **C** Core、recall、archival
- **D** Working、episodic、semantic

<details>
<summary>查看答案与解析</summary>

**答案**　C

Letta 使用 core（始终可见）、recall（对话历史）和 archival（外部）三个层级。

</details>

## 2. 睡眠时计算（sleep-time compute）针对哪个生产问题？

- **A** 更快的 JSON 解析
- **B** 在关键路径上做记忆整合所导致的尾部延迟
- **C** 更低的 embedding 成本
- **D** 数学问题上更高的准确率

<details>
<summary>查看答案与解析</summary>

**答案**　B

睡眠时计算把剪枝/摘要/对账从面向用户的路径上挪走，使主响应保持快速。

</details>

## 3. 下列哪个属性不是 Letta 中记忆块的字段？

- **A** limit
- **B** embedding_model_version
- **C** label
- **D** value

<details>
<summary>查看答案与解析</summary>

**答案**　B

记忆块携带 id、label、value、limit、description；embedding 模型版本不是记忆块 schema 的一部分。

</details>

## 4. 为什么睡眠时 agent 能运行比主 agent 更强的模型？

- **A** 记忆操作只花一半的 token
- **B** 它收到一个私有 API key
- **C** 它不在关键路径上，因此不受延迟约束
- **D** 它豁免于限流

<details>
<summary>查看答案与解析</summary>

**答案**　C

由于它不阻塞用户响应，睡眠时 agent 可以更慢、更贵。

</details>

## 5. Human 块和 Persona 块泛化成了什么模式？

- **A** 向量 embedding
- **B** 操作系统进程
- **C** JSON-RPC 通道
- **D** 任意用户定义的、带类型的可编辑块（Task、Project、Safety……）

<details>
<summary>查看答案与解析</summary>

**答案**　D

Letta 把 MemGPT 的两个块泛化为任何带 id、label、value、limit、description 的用户定义块。

</details>

## 6. 在此模式中，静默漂移（silent drift）是什么？

- **A** 磁盘写入缓慢
- **B** 主 agent 从未察觉睡眠时 agent 在它脚下重写了某个块；用版本化和可见的 diff 修复
- **C** 限流抖动
- **D** embedding 模型升级

<details>
<summary>查看答案与解析</summary>

**答案**　B

对块做版本化、并在 trace 中呈现 diff，能让睡眠时的重写对主循环可见。

</details>

## 7. 在 Letta V1 中，什么替换了内联的 `Thought:` token 以及 send_message/heartbeat 模式？

- **A** 一个专门负责思考的第二个 LLM
- **B** 一个更大的 system prompt
- **C** 在单独通道上发出、并贯穿各轮传递的原生推理
- **D** 用户手动输入的想法

<details>
<summary>查看答案与解析</summary>

**答案**　C

Letta V1（letta_v1_agent）使用提供商层面的原生推理，而非 prompt 形态的 thought。

</details>


[返回本课](docs/zh.md)
