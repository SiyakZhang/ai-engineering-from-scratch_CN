# 失败模式：agent 为什么会坏 · 自测

每题先选答案，再展开解析。

## 1. MASFT 的核心主张是什么？

- **A** 失败源于网络中断
- **B** 失败会随更大的模型消失
- **C** 多 agent 失败是根本性的设计缺陷，而非可以靠更好的基座模型修复的 LLM 局限
- **D** 失败是随机噪声

<details>
<summary>查看答案与解析</summary>

**答案**　C

伯克利的 MASFT 把失败归类为设计缺陷；它们不会因扩展基座模型而消失。

</details>

## 2. 下列哪一个不是本课列出的五种反复出现的行业失败模式之一？

- **A** embedding 版本管理
- **B** 范围蔓延（scope creep）
- **C** 级联错误（cascading errors）
- **D** 幻觉式动作（hallucinated actions）

<details>
<summary>查看答案与解析</summary>

**答案**　A

这五种是幻觉式动作、范围蔓延、级联错误、上下文丢失、工具误用。

</details>

## 3. 本课中的级联错误（cascading error）是什么？

- **A** 一个 YAML 解析器错误
- **B** 一次 cron 失败
- **C** 一次错误调用触发跨系统的下游影响（一个虚构 SKU 触发了四次下游 API 调用）
- **D** 一次 LLM 限流级联

<details>
<summary>查看答案与解析</summary>

**答案**　C

级联把单次错误调用放大成跨多系统的事故；当 agent 伪造成功时尤其严重。

</details>

## 4. 《LLM Agent 幻觉综述》列出了哪两种表现形式？

- **A** 热 token 和冷 token
- **B** 指令遵循偏离（Instruction-following Deviation）和长程上下文误用（Long-range Contextual Misuse）
- **C** 软 prompt 和硬 prompt
- **D** 贪心搜索和束搜索

<details>
<summary>查看答案与解析</summary>

**答案**　B

幻觉表现为要么忽略 system prompt，要么忘记/误用更早轮次的上下文。

</details>

## 5. 成功幻觉（success hallucination）是什么意思？

- **A** 用户以为成功了而其实没有
- **B** 模型在基准上过度自信
- **C** 一个单元测试通过了
- **D** agent 返回成功消息，尽管目标状态并未改变（常发生在工具返回 400 时）

<details>
<summary>查看答案与解析</summary>

**答案**　D

要重新探测环境状态；当 agent 无法区分「我失败了」和「不可能」时，常会伪造完成。

</details>

## 6. 为什么只标记崩溃是不够的？

- **A** 大多数 agent 失败产生看起来有效、不会崩溃的输出；需要内容层面的检查
- **B** 崩溃很慢
- **C** 崩溃泄露 PII
- **D** 日志记录收费

<details>
<summary>查看答案与解析</summary>

**答案**　A

基于崩溃的监控会漏掉大部分 agent 失败，因为它们是内容形态的。

</details>

## 7. 本课建议在推理链的每一步采取什么缓解措施？

- **A** 加一个 sleep()
- **B** 对照环境状态核实事实接地的自动化验证门
- **C** 只降低温度
- **D** 禁用重试

<details>
<summary>查看答案与解析</summary>

**答案**　B

每步的门（安全分类器、参数校验、CRITIC、状态重探测）能在失败级联之前抓住它们。

</details>


[返回本课](docs/zh.md)
