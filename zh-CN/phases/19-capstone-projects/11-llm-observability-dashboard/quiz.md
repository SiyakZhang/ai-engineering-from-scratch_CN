# 顶点项目 11 —— LLM 可观测性与评测看板 · 自测

每题先选答案，再展开解析。

## 1. Langfuse、Phoenix 和 OpenLLMetry 趋同到哪种摄入 schema？

- **A** 基于 OTLP HTTP 的 OpenTelemetry GenAI 语义约定
- **B** 纯 CSV 日志文件
- **C** 各厂商专有的 JSON
- **D** Prometheus 暴露格式

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 2. 为什么在存储层中分开使用 ClickHouse 和 Postgres？

- **A** ClickHouse 无法存储字符串
- **B** 它们可以互换，随机选一个
- **C** ClickHouse 处理对 span 的列式分析，而 Postgres 保存用户、会话和应用元数据
- **D** Postgres 在 span 摄入上更快

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 3. OpenTelemetry Collector 中的尾采样（tail-sampling）处理器做什么？

- **A** 把旧 trace 回放进 Postgres
- **B** 无条件流式传输每一个字节
- **C** 在一条 trace 完成后再决定是否保留它，使用「保留错误加采样成功」这类规则
- **D** 截断低于 100ms 的 span

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 4. 仪表盘如何检测跨周的漂移？

- **A** 读取最近的部署时间戳
- **B** 在汇集的 prompt 嵌入上计算 PSI 或 KL 散度，并观察评测分数趋势
- **C** 靠肉眼盯仪表盘
- **D** 统计唯一 trace ID 的数量

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 5. 交付物在一次注入的 PII 泄露回归上的平均检测时间（MTTD）目标是多少？

- **A** 1 小时以内
- **B** 从 bug 部署到 Slack 告警 5 分钟以内
- **C** 在下一个值班班次之内
- **D** 24 小时以内

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 6. 要满足 trace 覆盖率细则，哪些 SDK 系列必须产生规范的 GenAI span？

- **A** 仅 vLLM
- **B** 任意一个 SDK 就够了
- **C** 至少六个：OpenAI、Anthropic、Google GenAI、LangChain、LlamaIndex 和 vLLM
- **D** 仅 OpenAI 和 Anthropic

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 7. 评测结果如何与原始的 LLM 调用关联起来？

- **A** 以每晚邮件发送的 CSV 形式
- **B** 仅以 Slack 消息形式
- **C** 以评测 span 的形式，作为父 trace 的子节点写入 ClickHouse
- **D** 作为一张没有 trace ID 的独立 Postgres 表

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>


[返回本课](docs/zh.md)
