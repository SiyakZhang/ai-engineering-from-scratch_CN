# 基准：SWE-bench、GAIA、AgentBench · 自测

每题先选答案，再展开解析。

## 1. SWE-bench 的评估器对一个候选补丁检查什么？

- **A** 对照参考修复的 BLEU 分数
- **B** 补丁通过一个单独的 LLM 评判
- **C** 补丁长度在 200 行以内
- **D** 之前失败的测试现在通过（FAIL_TO_PASS），且之前通过的测试仍通过（PASS_TO_PASS）

<details>
<summary>查看答案与解析</summary>

**答案**　D

评估框架以测试状态转移为门槛：暴露 bug 的测试必须翻转，而回归测试必须保持绿色。

</details>

## 2. SWE-bench Verified 为什么存在？

- **A** OpenAI 的 500 个任务、人工筛选的子集，移除了模糊的 issue 和不可靠的测试
- **B** 它包含更多语言
- **C** 它使用不同的补丁格式
- **D** 它运行更快

<details>
<summary>查看答案与解析</summary>

**答案**　A

Verified 是用于可信报告的更干净子集。

</details>

## 3. SWE-bench+ 关于成功补丁发现了什么？

- **A** 补丁总是超过 1000 行
- **B** 32.67% 在 issue 中泄露了解答文本，31.08% 的测试覆盖弱得可疑
- **C** 不存在数据污染
- **D** 所有补丁都是被记住的

<details>
<summary>查看答案与解析</summary>

**答案**　B

SWE-bench+ 在很大一部分成功补丁上标记出了解答泄露和弱覆盖。

</details>

## 4. GAIA 的设计理念是什么？

- **A** 对人难、对 AI 易
- **B** 对人在概念上简单（约 92%）但对 AI 难（早期带插件的 GPT-4：约 15%）
- **C** 纯粹是向量检索的基准
- **D** 只有单轮问题

<details>
<summary>查看答案与解析</summary>

**答案**　B

GAIA 刻意做到对人易、对 AI 难，测试推理 + 工具 + 模态。

</details>

## 5. 下列哪一个不是 AgentBench 的环境类别之一？

- **A** 游戏（Alfworld、LTP）
- **B** Web（WebShop、Mind2Web）
- **C** 代码（Bash、DB、KG）
- **D** 梯度（RL、IRL）

<details>
<summary>查看答案与解析</summary>

**答案**　D

AgentBench 覆盖代码、游戏、web 和开放式生成。不存在梯度类别。

</details>

## 6. 本课指出报告 SWE-bench 数字的错误方式是什么？

- **A** 按 repo 拆分报告
- **B** 报告步数
- **C** 只报一个聚合数字，而不提 Verified 或 SWE-bench+ 的背景
- **D** 报告墙上时钟

<details>
<summary>查看答案与解析</summary>

**答案**　C

执着于单一数字会掩盖数据污染和成本；总要报告 Verified 和按分布拆分的背景。

</details>

## 7. 这些基准没有衡量哪个维度？

- **A** 每任务成功率
- **B** 步数
- **C** 真实世界的运维成本（token、墙上时钟）、对抗安全性，以及你自己的领域
- **D** 测试状态转移

<details>
<summary>查看答案与解析</summary>

**答案**　C

基准做的是聚合；它们没有刻画成本、对抗鲁棒性或你自己的领域。

</details>


[返回本课](docs/zh.md)
