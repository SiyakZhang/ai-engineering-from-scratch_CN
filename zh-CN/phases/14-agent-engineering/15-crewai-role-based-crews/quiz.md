# 基于角色的 Agent 团队——角色、任务与流程 · 自测

每题先选答案，再展开解析。

## 1. CrewAI 的四个原语是什么？

- **A** Node、Edge、Reducer、Checkpointer
- **B** Tool、Prompt、Model、Memory
- **C** Agent、Task、Crew、Process
- **D** Actor、Message、Inbox、Runtime

<details>
<summary>查看答案与解析</summary>

**答案**　C

Agent、Task、Crew 和 Process 是这四个原语。

</details>

## 2. 按 CrewAI 文档，推荐的生产起点是什么？

- **A** 顺序式 process（sequential）
- **B** Flow
- **C** Crew
- **D** 层级式 process（hierarchical）

<details>
<summary>查看答案与解析</summary>

**答案**　B

文档说生产应用从 Flow 开始；当自主性值回成本时，再把 Crew 作为子步骤折叠进来。

</details>

## 3. Crew 和 Flow 之间的区别是什么？

- **A** Crew 是自主的、LLM 驱动的；Flow 是事件驱动、代码拥有、确定且可测试的
- **B** Crew 收费，Flow 免费
- **C** Flow 没有 agent
- **D** Crew 只跑在 GPU 上

<details>
<summary>查看答案与解析</summary>

**答案**　A

Crew 以自主性为先；Flow 以确定性为先。

</details>

## 4. 下列哪一个不是 CrewAI 内置的四种记忆类型之一？

- **A** 短期（Short-term）
- **B** 长期（Long-term）
- **C** 量化（Quantized）
- **D** 实体（Entity）

<details>
<summary>查看答案与解析</summary>

**答案**　C

短期、长期、实体和情境（contextual）是这四种。量化记忆不是 CrewAI 的概念。

</details>

## 5. 什么是背景故事膨胀（backstory bloat），本课建议如何处理？

- **A** Bedrock 调用慢；换区域
- **B** 存了太多 crew；归档旧的
- **C** 2000 字的 agent 背景故事挤占了上下文预算；保持精简
- **D** 工具太多；删一些

<details>
<summary>查看答案与解析</summary>

**答案**　C

背景故事塑造语气和判断，但过长会吃掉上下文。

</details>

## 6. 什么时候层级式 process 比顺序式更值得选用？

- **A** 总是
- **B** 当你有 4 个以上专家、需要一个 manager Agent 在它们之间路由时
- **C** 当你没有任何工具时
- **D** 当你只有一个任务时

<details>
<summary>查看答案与解析</summary>

**答案**　B

层级式增加了一个 manager Agent；只有当多个专家需要动态路由时才值得。

</details>

## 7. 为什么本课告诫不要在生产中使用自由形式的 Crew？

- **A** 输出可变性高，没有 Flow 包装时调试很痛苦
- **B** Crew 缺乏记忆
- **C** Crew 不受支持
- **D** Crew 比 Flow 贵

<details>
<summary>查看答案与解析</summary>

**答案**　A

Crew 的自主性让生产环境的重放和审计很痛苦；上线时用 Flow 包装它。

</details>


[返回本课](docs/zh.md)
