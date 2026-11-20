# Self-Refine 与 CRITIC：迭代式输出改进 · 自测

每题先选答案，再展开解析。

## 1. 哪三个 prompt 组成一个 Self-Refine 循环？

- **A** search、score、synthesize
- **B** generate、feedback、refine
- **C** plan、execute、solve
- **D** actor、evaluator、reflector

<details>
<summary>查看答案与解析</summary>

**答案**　B

Self-Refine 用一个模型扮演三个角色：generate、feedback、refine。

</details>

## 2. 为什么 Self-Refine 在 refine 这一步需要历史？

- **A** 它加快 token 生成
- **B** 计费需要历史
- **C** 提供商只对历史做缓存
- **D** 没有先前的输出和批评，refine 这一步会重复早先的错误；消融实验显示质量急剧下降

<details>
<summary>查看答案与解析</summary>

**答案**　D

refine 这个 prompt 以完整历史为条件，使模型不重复它早先的错误。

</details>

## 3. 相对于 Self-Refine，CRITIC 改变了什么？

- **A** 它把自反馈这一步替换成一个基于外部工具的核实器
- **B** 它用更大的模型来生成
- **C** 它移除了 refine 这一步
- **D** 它并行运行反馈步骤

<details>
<summary>查看答案与解析</summary>

**答案**　A

CRITIC 把自我批评换成一个经由搜索、代码解释器、计算器或领域核实器路由的 verify 步骤。

</details>

## 4. 用 Claude 友好的说法，哪种 Anthropic 工作流模式对应 Self-Refine 和 CRITIC？

- **A** Evaluator-Optimizer（评估器-优化器）
- **B** Router（路由）
- **C** Parallel sampling（并行采样）
- **D** Prompt chain（prompt 链）

<details>
<summary>查看答案与解析</summary>

**答案**　A

Anthropic 把这种模式命名为 Evaluator-Optimizer：评估器打分，优化器修订，循环直到收敛。

</details>

## 5. 什么是橡皮图章循环（rubber-stamp loop），本课建议如何避免它？

- **A** 一个总是通过的测试；移除这个测试
- **B** 同一个模型用同一个 prompt 批评它自己的输出并批准它；改用结构上不同的 prompt 或一个独立的、更小的批评者
- **C** 一个总是失败的重试；提高预算
- **D** 一个超时的护栏；放宽超时

<details>
<summary>查看答案与解析</summary>

**答案**　B

同风格的自我批评会收敛到「我看着挺好」；要把评估器和优化器区分开。

</details>

## 6. OpenAI Agents SDK 中哪个 SDK 特性是 CRITIC 形态的？

- **A** 输出护栏（可以调用工具）
- **B** Sessions
- **C** Handoffs
- **D** Tracing

<details>
<summary>查看答案与解析</summary>

**答案**　A

输出护栏核实 agent 的最终输出，且可以调用工具，对应 CRITIC 的核实器角色。

</details>

## 7. 本课为 2026 年的 evaluator-optimizer 循环建议什么停止条件？

- **A** 组合：核实器通过 或（模型说行 且 迭代数 >= 2）或 迭代数 >= max_iterations
- **B** 永不停止；让 agent 无限自我改进
- **C** 仅当模型说「行」时停止
- **D** 仅当核实器通过时停止

<details>
<summary>查看答案与解析</summary>

**答案**　A

组合条件避免了单一条件的失败模式。

</details>


[返回本课](docs/zh.md)
