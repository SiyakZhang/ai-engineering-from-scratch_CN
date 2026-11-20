# 拒答评估 · 自测

每题先选答案，再展开解析。

## 1. under-refusal（拒绝不足）衡量的是什么？

- **A** 模型拒绝被标为 safe 的 prompt 的频率
- **B** 模型回答被标为 unsafe 的 prompt 的频率
- **C** 每条 prompt 一次 API 调用的成本
- **D** 模型每条回复输出多少 token

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 2. 本课为什么用 mock LLM 而不是真实模型？

- **A** 因为本课需要 GPU 硬件
- **B** 因为 mock LLM 比真实模型更准
- **C** 因为同样的输入在多次运行中能得到同样的输出，让代码改动能归因到已知原因
- **D** 因为顶点课里不允许用真实模型

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 3. 已知 safe prompt 数 = 30，被拒绝的 safe prompt 数 = 5，over-refusal（过度拒绝）率是多少？

- **A** 0.30
- **B** 0.17
- **C** 0.50
- **D** 0.05

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 4. 这里的 Expected Calibration Error（ECE，期望校准误差）衡量的是什么？

- **A** 在 unsafe prompt 上拒绝的比例
- **B** 所有回复加起来的总 token 数
- **C** 模型声称的置信度与它实际观测到的准确率之间的差距，按置信度区间分桶统计
- **D** 命中的 regex 规则数量

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 5. 为什么这套框架要把 unsafe prompt 跟第 82 课的 taxonomy 做关联（join）？

- **A** 为了把每条 prompt 的 severity 都加一
- **B** 为了去重
- **C** 为了重新跑一遍第 82 课的语料加载器
- **D** 为了按攻击分类报告 under-refusal，让团队看清模型在哪条边界上漏掉了

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 6. 为什么这套框架要同时返回 under-refusal 和 over-refusal，而不是给一个单一的安全分？

- **A** 因为 over-refusal 是另一个团队算的
- **B** 因为 Python dataclass 更喜欢多个字段
- **C** 因为它们是两种相反的错误，一个单一数字会把某个 build 上更严重的那种藏起来
- **D** 因为 under-refusal 只在 CI 里用

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>


[返回本课](docs/zh.md)
