# Anthropic 的工作流模式：简单胜过复杂 · 自测

每题先选答案，再展开解析。

## 1. Anthropic 如何区分工作流（workflow）和 agent？

- **A** 工作流跑在 CPU 上；agent 需要 GPU
- **B** 工作流是无状态的；agent 是有状态的
- **C** 工作流是工程师拥有的预定义图；agent 是模型拥有的动态工具调度
- **D** 工作流用 embedding；agent 用工具

<details>
<summary>查看答案与解析</summary>

**答案**　C

工作流 = 工程师拥有的预定义代码路径；agent = 模型拥有那张图。

</details>

## 2. 支撑全部五种模式的增强型 LLM 有哪三种能力？

- **A** Plan、execute、reflect
- **B** 向量、KV、图
- **C** Embedding、微调、RAG
- **D** 搜索（检索）、工具（动作）、记忆（持久化）

<details>
<summary>查看答案与解析</summary>

**答案**　D

原子单元是一个接好了检索、工具和记忆的 LLM。

</details>

## 3. 下列哪一个不是 Anthropic 的五种工作流模式之一？

- **A** Routing（路由）
- **B** Prompt chaining（prompt 链）
- **C** Evaluator-optimizer（评估器-优化器）
- **D** Gradient distillation（梯度蒸馏）

<details>
<summary>查看答案与解析</summary>

**答案**　D

五种是 prompt chaining、routing、parallelization、orchestrator-workers、evaluator-optimizer。梯度蒸馏是一个训练概念。

</details>

## 4. 并行化（parallelization）有哪两种形态？

- **A** 分区（sectioning，不同的块）和投票（voting，对同一 prompt 调用 N 次再聚合）
- **B** 有状态和无状态
- **C** 热和冷
- **D** 同步和异步

<details>
<summary>查看答案与解析</summary>

**答案**　A

并行化是分区或投票；两者都扇出 N 个调用并聚合。

</details>

## 5. Self-Refine 被泛化成了哪种工作流模式？

- **A** Prompt chaining
- **B** Routing
- **C** Orchestrator-workers
- **D** Evaluator-optimizer

<details>
<summary>查看答案与解析</summary>

**答案**　D

Evaluator-optimizer 是 Anthropic 对 Self-Refine / CRITIC 迭代模式的命名。

</details>

## 6. 按本课所说，什么时候工作流胜过 agent？

- **A** 在可预测、有成本边界或有合规边界的任务上，图可以被枚举和审计
- **B** 总是
- **C** 只在 GPU 上
- **D** 只在聊天时

<details>
<summary>查看答案与解析</summary>

**答案**　A

工作流更便宜、更易调试、可审计；当步骤可知时就选它。

</details>

## 7. 本课推荐的默认起点是什么？

- **A** 构建一个自定义 MCTS
- **B** 微调模型
- **C** 一个多 agent 框架
- **D** 直接 API 调用；只在持久状态、actor 并发或角色模板能值回其成本时才加框架

<details>
<summary>查看答案与解析</summary>

**答案**　D

Schluntz 和 Zhang：从简单开始；只在有正当理由时才增加框架复杂度。

</details>


[返回本课](docs/zh.md)
