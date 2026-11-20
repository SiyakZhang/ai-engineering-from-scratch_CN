# 结构化输出与约束解码 · 自测

每题先选答案，再展开解析。

## 1. 为什么仅靠 prompt 让模型“返回 JSON”对生产环境不够？

- **A** JSON 太冗长
- **B** prompt 无法描述 schema
- **C** prompt 太长
- **D** 前沿模型大多数时候会遵从但并非总是；那一小部分格式错误的输出会破坏下游解析器

<details>
<summary>查看答案与解析</summary>

**答案**　D

仅靠 prompt 约束在前沿模型上约 80% 的时候有效；生产需要更硬的保证。

</details>

## 2. 受约束解码在每个生成步修改什么？

- **A** logit 向量，屏蔽掉会使目标语法失效的 token，使得只能采样合法的后续 token
- **B** 训练损失
- **C** tokenizer
- **D** KV cache

<details>
<summary>查看答案与解析</summary>

**答案**　A

一个 logit 处理器把非法 token 设为 -inf，使 softmax 无法采样它们。

</details>

## 3. 为什么受约束解码可能比自由生成更快？

- **A** 模型更小
- **B** 强制的脚手架 token（例如 '{"name": "'）可以直接发出而无需采样，且合法 token 的搜索空间缩小
- **C** 它跳过反向传播
- **D** 它完全避免了 softmax

<details>
<summary>查看答案与解析</summary>

**答案**　B

已确定的 token 跳过采样，缩小的合法 token 集降低了解码成本。

</details>

## 4. 哪种 schema 设计选择能防止模型过早做出认定？

- **A** 使用 snake_case
- **B** 使用更短的键名
- **C** 把推理字段放在答案/决策字段之前，让模型先思考再认定
- **D** 把 'answer' 放在最前面

<details>
<summary>查看答案与解析</summary>

**答案**　C

字段顺序即逻辑：把推理放在前面，让模型在锁定答案之前先思考。

</details>

## 5. 像 Outlines 这样基于有限状态机（FSM）的受约束解码工具有什么局限？

- **A** 它们只支持枚举
- **B** 它们不是确定性的
- **C** 递归 schema 必须被展平；真正递归的结构需要基于 CFG 的引擎，如 XGrammar
- **D** 它们把你锁定到 OpenAI

<details>
<summary>查看答案与解析</summary>

**答案**　C

FSM 无法表示无界递归；CFG 引擎能处理它。

</details>

## 6. 为什么说 Instructor 不修改 logit？

- **A** Instructor 把 schema 格式化进 prompt 并对输出做解析/重试；logit 屏蔽发生在服务端或根本不发生
- **B** Anthropic 所要求
- **C** 它编辑 prompt
- **D** 它使用梯度更新

<details>
<summary>查看答案与解析</summary>

**答案**　A

Instructor 使用提供方侧的结构化输出加上客户端校验和重试，而非 logit 屏蔽。

</details>

## 7. 像 date='YYYY-MM-DD' 这样严格的正则会引入什么问题？

- **A** 正则很慢
- **B** 它移除了未知值的任何退路，于是模型会捏造一个日期，而非返回 null/哨兵值
- **C** 它破坏 JSON 解析
- **D** 它需要 CFG 支持

<details>
<summary>查看答案与解析</summary>

**答案**　B

过严的语法迫使模型臆造值；对未知值始终允许 null/哨兵值。

</details>

## 8. 什么时候应该选用 vLLM 引导解码而非厂商的结构化输出 API？

- **A** 总是用厂商
- **B** 仅配合字节级 BPE
- **C** 自托管推理，你掌控模型并希望在不重试的情况下获得 logit 级别的保证
- **D** 仅对极小的 schema

<details>
<summary>查看答案与解析</summary>

**答案**　C

vLLM 引导解码适合带 logit 级约束的自托管服务；厂商 API 会把你锁定到其技术栈。

</details>


[返回本课](docs/zh.md)
