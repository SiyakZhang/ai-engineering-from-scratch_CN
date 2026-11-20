# 顶点课 25：Verification Gate 与 Observation Budget · 自测

每题先选答案，再展开解析。

## 1. 在阅读本课之前：为什么驱动层需要确定性的 gate chain 而不是用模型当裁判？

- **A** 模型在生产环境中当裁判太慢了。
- **B** Gate chain 允许模型自己编写策略。
- **C** 模型裁判总是会产生幻觉式的 allow 判定。
- **D** 确定性使得拒绝原因可审计，整个链路可回放。

<details>
<summary>查看答案与解析</summary>

**答案**　D

审计记录和可复现性是实际收益。模型裁判也可以接入，但结构化的 gate 必须是确定性的，这样判定才能被复现和审查。

</details>

## 2. 为什么本课把 WhitelistGate 放在 BudgetGate 前面？

- **A** BudgetGate 要等至少调用过一次工具之后才能运行。
- **B** 白名单拒绝更便宜，短路后可以避免代价更高的 ledger 求和。
- **C** 顺序无所谓，因为 GateChain 会随机化评估顺序。
- **D** 按照惯例白名单必须是最后一个 gate。

<details>
<summary>查看答案与解析</summary>

**答案**　B

便宜的拒绝先跑。WhitelistGate 是 O(1) 哈希查找，BudgetGate 需要对 ledger 求和。在白名单上短路可以在调用结构性非法时省掉那部分计算。

</details>

## 3. ObservationLedger 已经记录了一条 read_file 的 60 token 观测。随后驱动层拒绝了一个调用。Ledger 对拒绝记录了什么？

- **A** 拒绝被当作以拒绝者名字命名的合成 Observation 追加进来。
- **B** 什么也不记。Ledger 只记录成功的观测。
- **C** 一行 token 为零、标记为 refused 的 Observation 记录。
- **D** 一行负 token 的 Observation，代表拒绝开销。

<details>
<summary>查看答案与解析</summary>

**答案**　B

Ledger 记录的是模型已经看到的观测。拒绝产生的是 GateDecision，不是 Observation。拒绝计数和 ledger 并列存放，不混在里面。

</details>

## 4. RecencyGate.window 设为 3。Ledger 最近一次记录在 turn 5。一个新的 ToolCall 在 turn 10 到来。会怎样？

- **A** Gate 拒绝：间隔 5 超过了窗口值 3。
- **B** Gate 抛异常，因为 ledger 过期了。
- **C** Gate 放行：该调用在最新的 turn 上。
- **D** Gate 放行：window 作用于 ledger 大小而非 turn 间隔。

<details>
<summary>查看答案与解析</summary>

**答案**　A

RecencyGate 比较 (call.turn - ledger.latest_turn) 和 window。10 - 5 = 5，大于 3，所以拒绝。

</details>

## 5. 你想加一个单次调用输出上限（单条观测不超过 8000 token）。这个 gate 在链路中该放在哪里？

- **A** 放在 BudgetGate 内部，让两个限制组合起来。
- **B** 它不能作为 gate，因为输出大小只有在工具执行后才知道。
- **C** 放在 WhitelistGate 前面，因为大小是最便宜的检查属性。
- **D** 放在 BudgetGate 后面，因为累积预算总是占主导。

<details>
<summary>查看答案与解析</summary>

**答案**　B

在 gate 评估时输出大小还不可知。驱动层在工具执行之后、模型看到之前截断观测。Gate 评估的是输入，不是输出。

</details>

## 6. 审阅者要求你证明 agent 在整个会话中从未执行过被拒绝的工具调用。你应该给他看哪个产物？

- **A** ObservationLedger 快照，里面只有成功的观测。
- **B** ChainOutcome 记录列表，包含每次调用的判定和拒绝原因。
- **C** 模型的聊天记录，包含它的自我报告。
- **D** pytest 的输出，记录了测试通过/失败。

<details>
<summary>查看答案与解析</summary>

**答案**　B

ChainOutcome 记录带有每次调用的判定和拒绝原因。Ledger 和聊天记录可以辅助佐证，但可审计的产物是 chain 的判定记录。

</details>


[返回本课](docs/zh.md)
