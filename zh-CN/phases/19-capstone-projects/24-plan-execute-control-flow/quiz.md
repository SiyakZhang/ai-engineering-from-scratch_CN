# Plan-Execute 控制流 · 自测

每题先选答案，再展开解析。

## 1. 在 Plan-Execute agent 中，planner 的职责是什么？

- **A** 执行超时控制
- **B** 处理 JSON-RPC 传输层
- **C** 产出一个带类型的有序步骤列表，交由 executor 执行
- **D** 对每个步骤调用 dispatcher

<details>
<summary>查看答案与解析</summary>

**答案**　C

Planner 产出结构化计划，Executor 执行。把两者混在一起就是本课要摆脱的 chain-of-thought 陷阱。

</details>

## 2. 为什么 expected_outcome 是 Step 的一部分，即使 executor 并不检查它？

- **A** 因为 dispatcher 把它当缓存 key 使用
- **B** 因为它给 replanner 和 tracer 提供了一个可读的成功条件
- **C** 因为模型会用它来训练
- **D** 因为注册中心要求它

<details>
<summary>查看答案与解析</summary>

**答案**　B

Replanner 在修订计划时会读它，tracer 在时间线上会渲染它。它是 step 上的一份人类可读契约。

</details>

## 3. 当某个步骤失败且 replanner 返回新计划时，executor 在事件流上发出什么？

- **A** plan.diff，包含被移除、新增和修订的 step id
- **B** session.complete 并带 status=failed
- **C** 什么也不发——replan 是静默的
- **D** tool.error 后跟 session.start

<details>
<summary>查看答案与解析</summary>

**答案**　A

plan.diff 让修订过程可见。静默重写才是我们要避免的 bug。

</details>

## 4. 为什么要把 max_steps 和 max_replans 作为两个独立预算？

- **A** 因为它们度量不同单位：steps 限制总执行量，replans 限制 planner 被调用的次数
- **B** 因为注册中心要统计 replan 次数
- **C** 因为 dispatcher 拒绝无界计划
- **D** 因为 asyncio 要求两个都有

<details>
<summary>查看答案与解析</summary>

**答案**　A

max_replans 抓住不断返回同一份坏计划的 planner。max_steps 抓住不断膨胀的失控计划。

</details>

## 5. 当 planner 在第一次调用时就返回空列表，返回的 reason 是什么？

- **A** step_budget
- **B** goal_met
- **C** replan_budget
- **D** no_plan

<details>
<summary>查看答案与解析</summary>

**答案**　D

没有计划就没有执行。会话以 reason=no_plan、status=failed 结束。

</details>

## 6. PlanDiff.revised 里装的是什么？

- **A** 在新计划中存在但不在旧计划中的 step id
- **B** 在旧计划中存在但不在新计划中的 step id
- **C** 在两次修订之间 tool_name 或 args 发生变化的 step id
- **D** planner 要求跳过的 step id

<details>
<summary>查看答案与解析</summary>

**答案**　C

revised 是在两次修订之间 (tool_name, args) 签名发生变化的 id 集合。

</details>

## 7. 当 executor 用尽 max_replans 时，SessionResult.reason 是什么？

- **A** goal_met
- **B** replan_budget
- **C** step_budget
- **D** no_plan

<details>
<summary>查看答案与解析</summary>

**答案**　B

replan_budget。status 为 failed。history 中包含所有已运行的步骤，包括触发 replan 的那些失败步骤。

</details>


[返回本课](docs/zh.md)
