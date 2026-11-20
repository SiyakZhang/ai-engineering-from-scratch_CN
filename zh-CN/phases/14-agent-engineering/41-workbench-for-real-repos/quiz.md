# 真实仓库上的工作台 · 自测

每题先选答案，再展开解析。

## 1. 把同一个任务分别走「仅 prompt」和「工作台引导」两条流水线，目标是什么？

- **A** 对 GPU 做基准测试
- **B** 比较模型
- **C** 选一个厂商
- **D** 产出一份前后对比报告，能用数字而非争论交给一个怀疑者

<details>
<summary>查看答案与解析</summary>

**答案**　D

数字来做争辩；论据建立在一个有真实感的任务上，而非玩具任务。

</details>

## 2. 下列哪一个不是被衡量的五个结果之一？

- **A** tests_actually_run
- **B** files_outside_scope
- **C** model_perplexity
- **D** acceptance_met

<details>
<summary>查看答案与解析</summary>

**答案**　C

这五个是 tests_actually_run、acceptance_met、files_outside_scope、handoff_quality、reviewer_total。

</details>

## 3. LangChain 的《Anatomy of an Agent Harness》在 Terminal Bench 2.0 上测到了什么？

- **A** harness 改动不改变排名
- **B** 所有模型都收敛到前三
- **C** 顶级模型掉了 25 名
- **D** 仅改变 harness，同一个模型就从 30 名开外升到了第五名

<details>
<summary>查看答案与解析</summary>

**答案**　D

同一模型上 25 名的排名变化，是「harness vs 模型」最有力的凭证。

</details>

## 4. preprints.org 那篇论文引用的企业 agent 项目失败率是多少？

- **A** 约 88% 无法进入生产，失败集中在运行时，而非推理
- **B** 无一失败
- **C** 约 50%
- **D** 8%

<details>
<summary>查看答案与解析</summary>

**答案**　A

《Harness Engineering for Language Agents》预印本把失败追溯到运行时问题（陈旧状态、脆弱重试、过度膨胀的上下文）。

</details>

## 5. 在长上下文条件下，WebAgent 基线准确率会怎样？

- **A** 减半但保持在 30% 以上
- **B** 保持平稳
- **C** 上升 30%
- **D** 从 40-50% 掉到 10% 以下，主要源于无限循环和目标丢失

<details>
<summary>查看答案与解析</summary>

**答案**　D

长上下文坍缩正是 Ralph Loop 和交接包要吸收的东西。

</details>

## 6. 本课关于假阴性（仅 prompt 更快的情况）怎么说？

- **A** 单步事实任务、单行 lint、格式化运行在仅 prompt 时更快；诚实地列举它们，免得工作台被说成杀鸡用牛刀
- **B** 它们推翻了 harness 论点
- **C** 它们证明工作台失败
- **D** 它们不存在

<details>
<summary>查看答案与解析</summary>

**答案**　A

诚实列举仅 prompt 最快的情况，能让 harness 论点保持可信。

</details>

## 7. 你应在什么场合引用本课的这份报告？

- **A** 内部 HR 评审
- **B** 只在营销 PPT 里
- **C** 只在黑客松上
- **D** 当有人想「就这个冲刺先去掉验证门」，或当一个新 agent 产品发布、需要一个可移植的省时基准时

<details>
<summary>查看答案与解析</summary>

**答案**　D

数字比解释传播得更远；当有压力想抄近路绕过这些面时，引用这份报告。

</details>


[返回本课](docs/zh.md)
