# 评估驱动的 Agent 开发 · 自测

每题先选答案，再展开解析。

## 1. 本课命名的三个评估层是什么？

- **A** 静态基准、自定义离线评估、在线生产评估
- **B** 单元、集成、端到端
- **C** 冒烟、回归、验收
- **D** Pre、check、post

<details>
<summary>查看答案与解析</summary>

**答案**　A

静态（SWE-bench、GAIA）、自定义离线（LLM 评判、执行、轨迹）、在线（重放、告警、成本/延迟）。

</details>

## 2. Anthropic 推荐的起点是什么？

- **A** 从多 agent 辩论开始
- **B** 从简单的 prompt 开始，用全面的评估来优化它们，只在需要时再加入多步 agent 系统
- **C** 只从一个前沿模型开始
- **D** 从层级式编排开始

<details>
<summary>查看答案与解析</summary>

**答案**　B

Anthropic 明确说评估是驱动其他每个选择的外层循环。

</details>

## 3. 评估器-优化器的紧循环是什么？

- **A** 训练、评估、部署
- **B** 提议者生成输出，评估器评判，refine 直到评估器通过（Self-Refine 的泛化）
- **C** Cache、retry、fail
- **D** Sample、sort、deduplicate

<details>
<summary>查看答案与解析</summary>

**答案**　B

它是 Self-Refine 的泛化：任何流程都可以包装成「提议-评判-refine」。

</details>

## 4. 关于评估应放在哪里，2026 年的最佳实践是什么？

- **A** 完全由 QA 团队拥有
- **B** 只在一个单独的厂商仪表盘里
- **C** 放在代码旁边，在每个 PR 的 CI 中运行，用评估分数把控合并
- **D** 只每季度运行一次

<details>
<summary>查看答案与解析</summary>

**答案**　C

与代码同处、CI 把控、回归追踪是标准做法。

</details>

## 5. 为什么本课告诫不要使用无接地的 LLM 评判者？

- **A** 评判者也会产生幻觉；与 CRITIC 模式配对，使评判基于外部工具接地
- **B** 它只在 GPU 上有效
- **C** 它违反 Apache 2.0
- **D** 它太慢

<details>
<summary>查看答案与解析</summary>

**答案**　A

CRITIC（第 5 课）适用：基于工具的核实让评判者保持诚实。

</details>

## 6. 对评估过拟合的危险是什么？

- **A** 算力成本上升
- **B** 为评估集优化会偏离生产有用性；要轮换用例
- **C** 向量索引碎片化
- **D** 延迟下降太多

<details>
<summary>查看答案与解析</summary>

**答案**　B

评估集轮换使优化与生产现实保持一致。

</details>

## 7. 为什么不稳定的评估（flaky evals）会造成问题？

- **A** 它们无法连到数据库
- **B** 它们超出上下文窗口
- **C** 非确定性用例会产生误报；固定种子并对状态做快照
- **D** 它们使推理成本翻倍

<details>
<summary>查看答案与解析</summary>

**答案**　C

不稳定让回归无法读懂；需要确定性（种子、状态快照）。

</details>


[返回本课](docs/zh.md)
