# Agent 循环：观察、思考、行动 · 自测

每题先选答案，再展开解析。

## 1. 为什么单凭一个 LLM 的行为更像自动补全，而不像一个 agent？

- **A** 没有 system prompt 它就拒绝回答
- **B** 它的上下文窗口太小，装不下一个问题
- **C** 它一次只能产出一个 token
- **D** 它无法读取文件、运行查询，或对照外部世界核实主张

<details>
<summary>查看答案与解析</summary>

**答案**　D

一个没有循环、没有工具的 LLM 只能从它的权重里产出文本；它无法观察状态或对状态采取行动。

</details>

## 2. Yao 等人 2022 年那条经典的 ReAct trace 中出现了哪三个标签？

- **A** System、User、Assistant
- **B** Plan、Execute、Reflect
- **C** Prompt、Response、Reward
- **D** Thought、Action、Observation

<details>
<summary>查看答案与解析</summary>

**答案**　D

ReAct 在单一流中交替出现 Thought、Action 和 Observation 几行。

</details>

## 3. 下列哪一项不是本课列出的 agent 循环五要素之一？

- **A** 消息缓冲区（message buffer）
- **B** 梯度优化器（gradient optimizer）
- **C** 观察格式化器（observation formatter）
- **D** 工具注册表（tool registry）

<details>
<summary>查看答案与解析</summary>

**答案**　B

五要素是消息缓冲区、工具注册表、停止条件、轮次预算和观察格式化器。梯度优化器属于训练，而非推理循环。

</details>

## 4. 轮次预算（turn budget）在循环中起什么作用？

- **A** 它对循环迭代次数设硬上限，以防止失控的 agent
- **B** 它对 LLM 提供商限流
- **C** 它限制每次回复的 token 数
- **D** 它控制注册表暴露多少个工具

<details>
<summary>查看答案与解析</summary>

**答案**　A

轮次预算是对循环迭代次数的上限；2026 年的 agent 常运行 40-400 步，需要一个与任务相称的上限。

</details>

## 5. 相比基于 prompt 的 Thought token，2025-2026 的原生推理（native-reasoning）转变改变了什么？

- **A** Thought token 现在在一个单独的推理通道（reasoning channel）上发出，并贯穿各轮传递
- **B** 循环控制流被替换成了 DAG
- **C** 模型不再使用工具调用，只依赖思维链
- **D** Observation 被从 prompt 中完全移除

<details>
<summary>查看答案与解析</summary>

**答案**　A

推理内容移到一个专用通道（在各提供商间通常是加密的），但「观察-思考-行动」的控制流不变。

</details>

## 6. 为什么本课说工具输出是不可信输入（untrusted input）？

- **A** 工具结果总是大于模型的上下文窗口
- **B** 工具运行时又慢又不可靠
- **C** 检索到的内容可能携带隐藏指令（比如「删掉这个 repo」），而只有直接的用户输入才算授权
- **D** 提供商默认会剥离工具输出的字节

<details>
<summary>查看答案与解析</summary>

**答案**　C

OpenAI CUA 文档明确指出，只有直接的用户指令才算授权；工具输出可能携带对抗性指令，必须被当作不可信对待。

</details>

## 7. 为什么本课声称 2026 年的每个框架底层仍在运行 ReAct？

- **A** 因为「观察-思考-行动」的控制流是不变量；框架的差异在于围绕它的检查点、actor、角色模板和 tracing
- **B** 因为 Yao 等人拥有这个循环的专利
- **C** 因为 LangGraph 强迫所有其他框架继承自它
- **D** 因为提供商要求 prompt 里出现 ReAct 关键词

<details>
<summary>查看答案与解析</summary>

**答案**　A

Claude Agent SDK、OpenAI Agents SDK、LangGraph、AutoGen、CrewAI、Agno 和 Mastra 之间的差异在于包裹循环的东西，而非循环本身。

</details>


[返回本课](docs/zh.md)
