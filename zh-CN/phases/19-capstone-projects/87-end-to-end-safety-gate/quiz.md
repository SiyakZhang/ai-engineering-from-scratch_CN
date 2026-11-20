# 端到端 safety gate · 自测

每题先选答案，再展开解析。

## 1. 这三个检查点（checkpoint）分别落在请求生命周期的哪里？

- **A** 只有 post-gen 会运行；pre-gen 和 during-gen 只是它的别名
- **B** pre-gen 在模型之前对 prompt 运行，during-gen 对输出流做过滤，post-gen 对已完成的输出运行
- **C** 三个都在模型被调用之前运行
- **D** 三个都在模型跑完之后运行

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 2. during-gen 过滤的目标是什么？

- **A** 提升 token 吞吐量
- **B** 把输出翻译成另一种语言
- **C** 用一段 refusal 替换 prompt
- **D** 缓冲输出块，一旦出现已知的有害续写就提前终止流，在用户看到之前拦下

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 3. aggregator 是怎么决定最终动作的？

- **A** 只看 rules engine
- **B** 再调用一次模型
- **C** 在 detector、token-filter、classifier 和 rules 这几路信号里取最高 severity，再映射到 block、redact、warn 或 allow
- **D** 对每个信号的置信度取平均

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 4. 为什么 gate 要为每个请求产出一个结构化的 RequestTrace？

- **A** 为了拖慢系统
- **B** 为了把 trace 复制进 prompt
- **C** 为了给 reviewer 一份按 checkpoint 分的审计轨迹，让任何一层的回归都能追溯到对应的模块
- **D** 为了取代日志

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 5. 当 pre-gen 的置信度超过 block 阈值时，会发生什么？

- **A** gate 调低阈值后重试
- **B** gate 抛出异常
- **C** 为了完整性，模型仍然会被调用
- **D** gate 返回 policy refusal，完全跳过 during-gen 和 post-gen

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 6. 为什么 demo 要故意放一些 encoding-trick 的 prompt 进入 during-gen？

- **A** 因为输入流水线不总能及时 normalize 它们；during-gen 过滤就是那道纵深防御，负责抓住漏出去的续写
- **B** 因为 encoding trick 不是真正的攻击
- **C** 因为模型反正都会拒绝它们
- **D** 因为 encoding 由 rules engine 处理

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>


[返回本课](docs/zh.md)
