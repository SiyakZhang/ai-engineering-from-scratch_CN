# 范围契约与任务边界 · 自测

每题先选答案，再展开解析。

## 1. 为什么范围蔓延（scope creep）被称为最缺乏监控的失败模式？

- **A** 测试会自动抓住它
- **B** 它太罕见，不值得监控
- **C** 每一次改动当下都有看似合理的理由；合在一起却构成了一个与审查过的不同的改动
- **D** 它会让 agent 大声崩溃

<details>
<summary>查看答案与解析</summary>

**答案**　C

agent 善意地为每一步做叙述；那个无声的总和就是蔓延。

</details>

## 2. 本课把哪个契约字段称为「契约的一半」？

- **A** approvals_required
- **B** goal
- **C** task_id
- **D** forbidden_files（负空间）

<details>
<summary>查看答案与解析</summary>

**答案**　D

没有 forbidden_files 的契约是不完整的；负空间是契约的一半。

</details>

## 3. 为什么把 allowed/forbidden 固定为 glob 而非原始路径？

- **A** 原始路径不可 JSON 序列化
- **B** glob 更快
- **C** glob 加密更好
- **D** 真实 repo 会移动文件；glob 能在跨会话的重构中存活

<details>
<summary>查看答案与解析</summary>

**答案**　D

glob（app/**/*.py）让契约在重构中保持有效。

</details>

## 4. 「违规预算」（violation budget）模式做什么？

- **A** 对模型调用限流
- **B** 在一个预算内允许轻微的范围滑动作为警告；只有超出才触发合并拒绝——这是一个能上线的门和一个会被禁用的门之间的差别
- **C** 按违规收费
- **D** 为 agent 设置一个月度预算

<details>
<summary>查看答案与解析</summary>

**答案**　B

agent-guardrails 使用 violationBudget，使这个门在日常流程中可用。

</details>

## 5. 那位 specsmaxxing 实践者报告了什么？

- **A** 成本上升 5 倍
- **B** 测试变慢
- **C** 在不改动 agent 的情况下，三周内「钻牛角尖率」从 52% 降到 21%；起作用的是契约，不是模型
- **D** 延迟下降 90%

<details>
<summary>查看答案与解析</summary>

**答案**　C

在调用 agent 前用 YAML 写好范围契约，在不改模型的情况下把钻牛角尖率减半。

</details>

## 6. 多契约合并的语义（最小权限）是什么？

- **A** 最后一个契约胜出
- **B** 第一个契约胜出
- **C** 对 allowed_files 取交集；对 forbidden_files 取并集；time_budget 取最小；累积审批；deny-all 黏住；与 None 合并时让位给另一方
- **D** 随机决胜

<details>
<summary>查看答案与解析</summary>

**答案**　C

最小权限合并：允许取交集，禁止取并集，时间取最严格，审批累积。

</details>

## 7. 为什么时间和网络预算也属于契约？

- **A** Apache 2.0 要求它们
- **B** 它们让 JSON 更小
- **C** 墙上时钟和外部主机访问是范围维度；仅文件 glob 是必要但不充分的
- **D** 提供商要求它们

<details>
<summary>查看答案与解析</summary>

**答案**　C

time_budget_minutes 和 network_egress 允许列表是文件 glob 之上的范围维度。

</details>


[返回本课](docs/zh.md)
