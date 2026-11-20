# 顶点课 29：把端到端 Coding Agent 跑在 Harness 上 · 自测

每题先选答案，再展开解析。

## 1. 在阅读本课之前：为什么端到端演示用确定性策略替代 LLM？

- **A** 确定性策略在编码任务上总是优于 LLM。
- **B** 本课承担不起推理成本。
- **C** LLM 跑测试太慢了。
- **D** 本课测试的是驱动层；策略是可替换的接缝。

<details>
<summary>查看答案与解析</summary>

**答案**　D

驱动层契约不关心策略是 LLM 还是状态机。去掉 LLM 就去掉了网络和随机性，把本课变成一个可复现的集成测试。

</details>

## 2. Agent 的状态机有五个状态。正常通过时它们的执行顺序是什么？

- **A** SURVEY -> RUN_TESTS -> INSPECT -> FIX -> VERIFY
- **B** RUN_TESTS -> SURVEY -> INSPECT -> FIX -> VERIFY
- **C** SURVEY -> INSPECT -> FIX -> RUN_TESTS -> VERIFY
- **D** SURVEY -> FIX -> VERIFY -> RUN_TESTS -> INSPECT

<details>
<summary>查看答案与解析</summary>

**答案**　A

Agent 先勘察项目，跑测试，检查失败的测试，修复 bug，然后验证。RUN_TESTS 在 INSPECT 之前，因为测试失败是策略读取的信号。

</details>

## 3. 内置 fixture 的 bug 是 src/fizz.py 里的 off-by-one：range(1, n) 应为 range(1, n + 1)。策略在哪个状态决定修复方案？

- **A** 在 SURVEY 状态，通过读取文件头。
- **B** 在 VERIFY 状态，在重跑之后。
- **C** 在 INSPECT 状态，在测试失败指明了预期输出之后。
- **D** 在状态机之外，在 gate chain 中。

<details>
<summary>查看答案与解析</summary>

**答案**　C

INSPECT 是策略读取失败测试并了解预期形状的地方。修复方案在此确定，在下一个 FIX 状态写入。

</details>

## 4. 每次工具调用依次经过哪些组件？

- **A** Sandbox -> GateChain -> SpanBuilder -> ObservationLedger
- **B** GateChain -> SpanBuilder -> Sandbox -> ObservationLedger
- **C** ObservationLedger -> GateChain -> Sandbox -> SpanBuilder
- **D** SpanBuilder -> GateChain -> Sandbox -> ObservationLedger

<details>
<summary>查看答案与解析</summary>

**答案**　B

先 Gate（允许/拒绝），再 Span（拒绝也要被捕获），然后 Sandbox（只在允许时执行），最后 Ledger（只在成功时记录）。本课代码就是这样串的。

</details>

## 5. 你把确定性策略换成真正的 LLM。驱动层的哪个组件需要改？

- **A** Gate chain 需要重写来处理 LLM 的随机性。
- **B** 驱动层什么都不用改；策略是唯一要换的部分。
- **C** Prometheus 导出格式会变得不兼容。
- **D** Sandbox 需要用 seccomp 加固。

<details>
<summary>查看答案与解析</summary>

**答案**　B

这就是本课的核心观点：驱动层与策略无关。接缝是 next_action / observe 接口。LLM 在此接入，不需要动 gate、sandbox、ledger 或 span。

</details>

## 6. 演示断言 agent 在不到 12 步内解决 fixture。确定性策略用了 5 步。真正的 LLM agent 可能怎样，驱动层如何应对？

- **A** 驱动层会静默延长预算。
- **B** LLM 可能用更多步；step_budget 限制循环，未解决的运行会以带 halted_reason 的失败上报。
- **C** LLM 也会用 5 步；驱动层不变。
- **D** LLM 无法在这个驱动层里运行。

<details>
<summary>查看答案与解析</summary>

**答案**　B

Step budget 是响亮、确定性的停止标准。一个四处游荡的 LLM 会被限制住，报告会明确告诉你原因。

</details>


[返回本课](docs/zh.md)
