# 工具使用与函数调用 · 自测

每题先选答案，再展开解析。

## 1. Toolformer 用什么信号来决定是否保留一个候选工具标注？

- **A** 工具是否在 100 毫秒内返回
- **B** 人类标注的一致性
- **C** 工具是否发出有效的 JSON
- **D** 纳入工具结果是否降低了周围文本上的下一个 token 损失

<details>
<summary>查看答案与解析</summary>

**答案**　D

Toolformer 的自监督信号会保留那些其工具结果能降低下一个 token 损失的标注。

</details>

## 2. 本课报告的 BFCL V4 的占比拆分是什么？

- **A** 50% live、50% synthetic
- **B** 33% agentic、33% planning、33% reflection
- **C** 100% 单轮
- **D** 40% agentic、30% multi-turn、10% live、10% non-live、10% hallucination

<details>
<summary>查看答案与解析</summary>

**答案**　D

BFCL V4 的权重是 40 agentic / 30 multi-turn / 10 live / 10 non-live / 10 hallucination。

</details>

## 3. 为什么一个工具的描述（description）是承重的？

- **A** 模型靠读它来选对工具；糟糕的描述是选错工具失败的首要原因
- **B** 它控制计费分桶
- **C** JSON Schema 要求它
- **D** 它是用户在 UI 中看到的东西

<details>
<summary>查看答案与解析</summary>

**答案**　A

工具描述是模型选择工具的主要信号；糟糕的描述会导致路由到错误的工具。

</details>

## 4. 在并行工具调用中，tool_use_id 起什么作用？

- **A** 它用 API key 授权这次调用
- **B** 它把每个工具结果与其发起调用关联起来，使乱序返回的结果也能正确路由
- **C** 它压缩 JSON 负载
- **D** 它启用缓存

<details>
<summary>查看答案与解析</summary>

**答案**　B

tool_use_id 是关联令牌；把它们互换会把结果路由到错误的调用。

</details>

## 5. V3 基于状态的评估试图捕捉哪一类失败？

- **A** 工具执行缓慢
- **B** token 泄露
- **C** 通过 AST 匹配看起来正确、但让 API 处于错误状态的工具调用
- **D** schema 版本漂移

<details>
<summary>查看答案与解析</summary>

**答案**　C

基于状态的评估检查最终的 API 状态（例如文件确实被创建了），而非语法上的调用匹配。

</details>

## 6. 本课没有把下列哪个 2026 年问题列为 function calling 的开放问题之一？

- **A** 跨轮记忆
- **B** 长程工具链接
- **C** token 级解码速度
- **D** 跨众多工具的动态决策

<details>
<summary>查看答案与解析</summary>

**答案**　C

开放问题是记忆、动态决策、长程链接和幻觉检测；解码速度不在列表中。

</details>

## 7. 为什么本课把一个通用的 run_shell(cmd) 工具称为危险信号？

- **A** 提供商会拒绝它
- **B** 它无法并行调用
- **C** 它扩大了沙箱边界；像 git_status() 这样的特定工具能限定读/写面和风险
- **D** 它很慢

<details>
<summary>查看答案与解析</summary>

**答案**　C

窄工具约束了沙箱面；一个通用的 shell 工具授予了主机的全部操作面。

</details>


[返回本课](docs/zh.md)
