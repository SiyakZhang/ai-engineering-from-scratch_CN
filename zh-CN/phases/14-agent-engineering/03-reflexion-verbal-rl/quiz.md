# Reflexion：言语强化学习 · 自测

每题先选答案，再展开解析。

## 1. Reflexion 替换了标准强化学习中的什么？

- **A** 用一个恒定奖励替换奖励塑形
- **B** 用存储在试验之间的自然语言反思替换梯度更新
- **C** 用随机搜索替换策略网络
- **D** 用参数化记忆替换情景记忆

<details>
<summary>查看答案与解析</summary>

**答案**　B

Reflexion 用情景记忆中的自然语言反思代替权重更新。

</details>

## 2. 哪三个组件定义了一个 Reflexion 系统？

- **A** Actor、Evaluator、Self-Reflector
- **B** Generator、Critic、Optimizer
- **C** Planner、Worker、Solver
- **D** Selector、Expander、Backpropagator

<details>
<summary>查看答案与解析</summary>

**答案**　A

Reflexion 把 agent 拆成运行轨迹的 Actor、给轨迹打分的 Evaluator，以及写下经验教训的 Self-Reflector。

</details>

## 3. 哪种评估器类型使用像单元测试或已知正确答案这样的外部二元信号？

- **A** 自评估（Self-evaluated）
- **B** 基于投票（Vote-based）
- **C** 标量（Scalar）
- **D** 启发式（Heuristic）

<details>
<summary>查看答案与解析</summary>

**答案**　C

标量评估器从标准答案读取通过/失败信号（ALFWorld 成功、HumanEval 测试）。

</details>

## 4. 为什么自评估比标量反馈是更弱的信号？

- **A** 模型评判自己时没有外部基准，所以它可能给自己的答案盖橡皮图章式通过
- **B** 它计算起来更慢
- **C** 它总是需要更大的模型
- **D** 它无法在工具上运行

<details>
<summary>查看答案与解析</summary>

**答案**　A

自评估缺乏外部检查，所以一个自信的幻觉也能得高分；要把它和基于工具的核实配对。

</details>

## 5. 本课把哪种情况列为 Reflexion 帮不上忙的地方？

- **A** 测试可以打分的代码生成
- **B** ALFWorld 导航任务
- **C** HotpotQA 多跳问题
- **D** 外部瞬时故障，比如网络中断

<details>
<summary>查看答案与解析</summary>

**答案**　D

对一次瞬时的外部中断做反思，产生的反思对未来的运行毫无帮助。

</details>

## 6. Reflexion 模式中的记忆腐烂（memory rot）是什么？

- **A** 情景缓冲区被过时或错误的反思填满，拖慢或带偏未来的试验
- **B** 反思被提供商加密了
- **C** 反思 prompt 超出了上下文窗口
- **D** 进程重启时丢失反思

<details>
<summary>查看答案与解析</summary>

**答案**　A

累积的陈旧或错误反思会降低行为质量；用压实（compaction）或 TTL 来缓解。

</details>

## 7. 哪种生产模式是本课对 Reflexion 最清晰的对应？

- **A** Cursor 的 apply-edits 流程
- **B** Anthropic 的 prompt caching
- **C** Claude Code 把 CLAUDE.md 中的经验教训前置到未来会话
- **D** OpenAI 的 batch API

<details>
<summary>查看答案与解析</summary>

**答案**　C

CLAUDE.md 的经验教训、pro-workflow 的 learn-rule，以及 Letta 的 sleep-time compute，都把情景反思缓冲区外置了。

</details>


[返回本课](docs/zh.md)
