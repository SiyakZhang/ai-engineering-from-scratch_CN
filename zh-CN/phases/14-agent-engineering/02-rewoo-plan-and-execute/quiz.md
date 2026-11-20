# ReWOO 与 Plan-and-Execute：解耦的规划 · 自测

每题先选答案，再展开解析。

## 1. 为什么 ReAct 的 prompt 随深度二次方增长？

- **A** 模型在每一步都对自身重新分词
- **B** 提供商按字节而非按 token 计费
- **C** 工具 schema 在每次调用时被复制
- **D** 每一步都携带完整的先前上下文，包括之前的每个 thought 和 observation

<details>
<summary>查看答案与解析</summary>

**答案**　D

ReAct 在每一步重新纳入先前的 thought 和 observation，使总 prompt 长度随深度的平方增长。

</details>

## 2. 定义 ReWOO 的三角色拆分是什么？

- **A** Planner、Workers、Solver
- **B** Reader、Writer、Reviewer
- **C** Generator、Critic、Optimizer
- **D** Actor、Evaluator、Reflector

<details>
<summary>查看答案与解析</summary>

**答案**　A

ReWOO 分离出发出 DAG 的 Planner、获取证据的 Workers，以及组合最终答案的 Solver。

</details>

## 3. 论文在 HotpotQA 上为 ReWOO 对比 ReAct 报告了哪些标志性数字？

- **A** token 多约 2 倍，准确率 +10
- **B** token 减少 10 倍，准确率 -2
- **C** token 减少约 5 倍，准确率绝对值提升 +4
- **D** token 相同，准确率 +1

<details>
<summary>查看答案与解析</summary>

**答案**　C

相比 ReAct，ReWOO 在 HotpotQA 上报告了约 5 倍的 token 削减和 +4 的绝对准确率提升。

</details>

## 4. ReWOO 计划节点中像 #E1 这样的占位符意味着什么？

- **A** 证据获取的重试计数器
- **B** 一个在派发时被替换为某个更早 worker 节点输出的引用
- **C** worker 1 返回的错误码
- **D** planner 版本标识符

<details>
<summary>查看答案与解析</summary>

**答案**　B

计划节点使用像 #E1、#E2 这样的证据引用，执行器会用上游 worker 的输出来替换它们。

</details>

## 5. 为什么 ReWOO 比 ReAct 更能定位失败？

- **A** ReWOO 对每次失败的调用最多重试十次
- **B** worker 中的错误变成 Solver 与原始计划一起看到的字符串，因此降级是按节点而非按步骤的
- **C** worker 在任何错误时都会让整个运行崩溃
- **D** Planner 在每次错误后重新发出一份全新的 DAG

<details>
<summary>查看答案与解析</summary>

**答案**　B

按节点的失败、加上上下文中的原始计划，让 Solver 能优雅降级，而不是在流式过程中从错误里推理出去。

</details>

## 6. 哪种任务形态比起朴素的 ReWOO 更适合 Plan-and-Act？

- **A** 一条 40 步的 web 或移动端导航轨迹
- **B** 一个纯算术问题
- **C** 单轮分类
- **D** 一个两步的事实查找

<details>
<summary>查看答案与解析</summary>

**答案**　A

Plan-and-Act 是为长程（超过 30 步）的 web 和移动端 agent 而建的，单条 ReAct 轨迹在这种情况下会失去连贯性。

</details>

## 7. ReWOO 的 planner 蒸馏结果对生产级 agent 意味着什么？

- **A** 一个小 planner（约 7B）可以匹敌大教师模型，因为 planner 从不看 observation
- **B** 蒸馏需要基于梯度的 RL 数据
- **C** 规划质量在 7B 参数以下会下降
- **D** 每一步都必须使用前沿模型

<details>
<summary>查看答案与解析</summary>

**答案**　A

由于 planner 不看 observation，来自大教师模型的计划轨迹能干净地迁移到一个小的微调 planner 上。

</details>


[返回本课](docs/zh.md)
