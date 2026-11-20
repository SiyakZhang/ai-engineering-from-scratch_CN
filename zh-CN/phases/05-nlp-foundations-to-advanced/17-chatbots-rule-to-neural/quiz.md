# 聊天机器人 —— 从规则到神经再到 LLM agent · 自测

每题先选答案，再展开解析。

## 1. 在基于规则的聊天机器人中，槽填充（slot-filling）状态机做什么？

- **A** 跟踪哪些必需参数（日期、目的地、金额）仍然缺失，并依次询问它们
- **B** 检测讽刺
- **C** 嵌入用户消息
- **D** 挑选最通顺的回复

<details>
<summary>查看答案与解析</summary>

**答案**　A

槽填充迭代地收集任务处理器所需的结构化参数。

</details>

## 2. 为什么基于检索的对话能抵抗幻觉？

- **A** 它拒绝所有查询
- **B** 它使用嵌入
- **C** 它从一个精心整理的集合中返回预设回复，而不是生成新文本
- **D** 它使用 BM25

<details>
<summary>查看答案与解析</summary>

**答案**　C

检索呈现的是预先写好的答案；没有生成就没有捏造的内容。

</details>

## 3. LLM agent 循环与单次 LLM 调用的区别是什么？

- **A** 更大的上下文窗口
- **B** 一个控制器把 LLM 调用与工具调用交错执行，直到模型返回最终答案或步数预算耗尽
- **C** 使用 softmax
- **D** 使用贪心解码

<details>
<summary>查看答案与解析</summary>

**答案**　B

agent 增加了一个“规划-行动-观察”的循环，带工具调用和终止条件。

</details>

## 4. 为什么混合路由（规则 + 检索 + LLM agent）是 2026 年的生产默认方案？

- **A** 它避免使用嵌入
- **B** 没有单一架构能很好处理所有请求；规则覆盖破坏性操作，检索覆盖 FAQ，agent 处理模糊的开放式查询
- **C** 它免除了评估的需要
- **D** 它维护成本更低

<details>
<summary>查看答案与解析</summary>

**答案**　B

混合系统对高风险操作使用确定性规则，把 LLM agent 留给开放式查询。

</details>

## 5. 什么是 prompt 注入（prompt injection）？

- **A** 一种 tokenizer 攻击
- **B** 仅是 SQL 注入的一种变体
- **C** 用户提供（直接）或文档提供（间接）的文本，试图覆盖系统 prompt 或劫持 agent 行为
- **D** 把 token 注入到嵌入中

<details>
<summary>查看答案与解析</summary>

**答案**　C

prompt 注入通过用户输入或工具输出中的不可信文本来改写 agent 的行为。

</details>

## 6. OWASP Top 10（LLM Apps 2025）中排在 LLM01 的风险是哪个？

- **A** 不安全的反序列化
- **B** SQL 注入
- **C** 失效的访问控制
- **D** prompt 注入（直接与间接）

<details>
<summary>查看答案与解析</summary>

**答案**　D

prompt 注入在 OWASP LLM Apps Top 10（2025）中是 LLM01。

</details>

## 7. 哪种缓解模式通过把规划与执行分离来减少间接 prompt 注入？

- **A** Plan-Verify-Execute（规划-验证-执行）：agent 先规划，对照计划验证每个动作，再执行——防止工具输出注入新的、计划外的动作
- **B** 更短的上下文
- **C** 更大的模型
- **D** 更低的 temperature

<details>
<summary>查看答案与解析</summary>

**答案**　A

PVE 对照已商定的计划检查每一步，因此来自工具输出的注入指令会被拒绝。

</details>

## 8. 为什么即使在 LLM-agent 系统中，破坏性操作（支付、删除）也必须经由结构化流程？

- **A** 工具无法被调用
- **B** beam search 不安全
- **C** LLM 很慢
- **D** 自信的捏造、prompt 注入和范围蔓延意味着 LLM 不能成为不可逆副作用的唯一权威

<details>
<summary>查看答案与解析</summary>

**答案**　D

幻觉和注入使得通过纯 LLM agent 执行不可逆操作不安全；需要确定性的确认流程。

</details>


[返回本课](docs/zh.md)
