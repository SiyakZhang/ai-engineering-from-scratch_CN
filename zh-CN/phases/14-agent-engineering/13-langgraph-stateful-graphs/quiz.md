# 有状态图编排——持久执行与检查点 · 自测

每题先选答案，再展开解析。

## 1. LangGraph 把什么当作 agent 的核心单元？

- **A** 一次自由形式的 LLM 调用
- **B** 一个向量索引
- **C** 一个状态机，带类型化状态、函数节点和条件边
- **D** 单个工具注册表

<details>
<summary>查看答案与解析</summary>

**答案**　C

LangGraph 把 agent 建模为一张状态图：节点是纯函数，边是转移，状态是类型化且不可变的。

</details>

## 2. 持久化执行（durable execution）解决了哪个问题？

- **A** 在提供商之间翻译
- **B** 降低推理成本
- **C** 更快地生成 embedding
- **D** 当一个 40 步的运行在第 38 步失败时，以精确的状态从第 38 步恢复，而不是从头再来

<details>
<summary>查看答案与解析</summary>

**答案**　D

每个节点之后的检查点让运行时能从上一个成功步骤恢复。

</details>

## 3. 下列哪一个不是 LangGraph 支持的三种拓扑之一？

- **A** Supervisor（监督者）
- **B** Swarm（点对点）
- **C** Hierarchical（嵌套子图）
- **D** Gradient ring（梯度环）

<details>
<summary>查看答案与解析</summary>

**答案**　D

拓扑是 supervisor、swarm 和 hierarchical。Gradient ring 不是 LangGraph 的拓扑。

</details>

## 4. 为什么节点必须是确定性的，恢复才能干净地工作？

- **A** 确定性降低 token 成本
- **B** 提供商要求确定性
- **C** 恢复假设相同输入产生相同的状态更新；随机种子、墙上时钟和外部 API 必须被捕获
- **D** 这是 GIL 要求的

<details>
<summary>查看答案与解析</summary>

**答案**　C

如果一个节点依赖未被捕获的非确定性，恢复就无法重建该步骤之后的状态。

</details>

## 5. 什么是条件边（conditional edge）？

- **A** 一条由状态的函数选择的边，用于让图分支
- **B** 一条只在 GPU 上运行的边
- **C** 一条按训练损失加权的边
- **D** 一条带 TTL 的边

<details>
<summary>查看答案与解析</summary>

**答案**　A

条件边基于状态分支；过度使用它们会让图难以推理。

</details>

## 6. 当检查点太小时会出什么问题？

- **A** 图无法到达 END
- **B** 工具状态和记忆写入无法恢复；完整状态必须序列化
- **C** 模型产出更短的答案
- **D** 磁盘被填满

<details>
<summary>查看答案与解析</summary>

**答案**　B

只对对话轮做检查点，会把工具状态和记忆写入留在恢复能触及的范围之外。

</details>

## 7. 人在回路（human-in-the-loop）在 LangGraph 的设计中处于哪里？

- **A** 在关键节点前暂停，把序列化的状态呈现给人，接受修改，然后恢复；checkpointer 让这变得廉价
- **B** 它需要 fork 运行时
- **C** 只在 START 和 END
- **D** 通过一个单独的提供商 API

<details>
<summary>查看答案与解析</summary>

**答案**　A

由于状态在节点之间已被序列化，人工审查与编辑就是一个自然的「暂停-恢复」模式。

</details>


[返回本课](docs/zh.md)
