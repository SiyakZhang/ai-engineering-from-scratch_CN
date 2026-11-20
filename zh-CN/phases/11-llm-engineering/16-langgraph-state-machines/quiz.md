# Agent 状态机——图、节点与检查点 · 自测

每题先选答案，再展开解析。

## 1. 为什么 LangGraph State 的 TypedDict 中的 `messages` 字段需要 `Annotated[list, add_messages]`？

- **A** 没有这个 reducer，节点更新会覆盖列表而不是追加，于是每一轮都会丢掉之前的历史。
- **B** 它在运行时把普通 dict 转换成 LangChain 消息对象。
- **C** 它在把检查点（checkpoint）写入磁盘时压缩消息列表。
- **D** 它启用从模型流式传输 token 增量。

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 2. `interrupt_before=['tools']` 和 `interrupt_after=['tools']` 之间的区别是什么？

- **A** `interrupt_before` 用于单元测试；`interrupt_after` 用于生产。
- **B** 没有区别；它们是别名。
- **C** `interrupt_before` 在模型发出 tool_calls 之后、但在工具执行之前暂停；`interrupt_after` 在工具已经运行之后暂停。
- **D** `interrupt_before` 先在沙箱里运行工具；`interrupt_after` 在生产中运行它。

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 3. 给定一个线程的检查点历史，你如何时间旅行（time-travel）到某个先前状态并探索一个不同的分支？

- **A** 设置 `graph.rewind = True` 并重新调用。
- **B** 用 config 中所需的先前 `checkpoint_id` 调用图；传 `None` 作为输入会从那个检查点重放，传入一个新值则会在恢复前把它追加进去。
- **C** 调用 `graph.reset(thread_id)` 然后 `graph.invoke(new_input, config)`。
- **D** 删除检查点目录并用相同的 thread_id 重新调用。

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 4. 在一个四节点的 ReAct 图（agent、tools、条件边、回到 agent 的静态边）中，条件边位于哪里？

- **A** 从 `agent` 出发，如果最后一条消息有 tool_calls 就路由到 `tools`，否则路由到 `END`。
- **B** 从 `START` 出发，根据输入长度路由到 `agent` 或 `END`。
- **C** 从 `tools` 回到 `agent`，根据工具输出是否为空进行路由。
- **D** 没有条件边；两条都是静态的。

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 5. 什么时候应该使用 `Send(node_name, state)` 而不是普通的边？

- **A** 把一个节点推迟到计时器到期。
- **B** 在失败后重试一个节点。
- **C** 派发对某个目标节点的 N 个并行执行，其输出通过 state 的 reducer 合并回来。
- **D** 在另一个进程中调用节点以实现隔离。

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>


[返回本课](docs/zh.md)
