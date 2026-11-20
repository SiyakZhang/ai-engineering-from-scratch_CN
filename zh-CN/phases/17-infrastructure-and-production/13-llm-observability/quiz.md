# LLM 可观测性栈选型 · 自测

每题先选答案，再展开解析。

## 1. 本课如何划分 2026 年的 LLM 可观测性市场？

- **A** Python 与 TypeScript
- **B** 本地部署 与 云
- **C** 开发平台（捆绑了评测/prompt/会话）与 网关/遥测工具
- **D** 厂商 与 开源

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 2. 本课把哪个工具定位为：核心采用 MIT 许可证、自托管能力出色、且提供每月 5 万事件的免费云套餐？

- **A** LangSmith
- **B** Arize AX
- **C** Langfuse
- **D** Phoenix

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 3. 相对于 Datadog 这类一体化可观测性技术栈，Arize AX 的主要规模化卖点是什么？

- **A** 总是更贵
- **B** 通过零拷贝的 Iceberg/Parquet 集成，在规模化场景下大约便宜 100 倍
- **C** 便宜 10%
- **D** 在每天 100 万事件以内免费

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 4. 本课认为为了可移植性，哪一层是错误的埋点层？

- **A** 使用 OpenTelemetry GenAI 语义约定
- **B** 在你的 agent 框架内部埋点，因为这会把你与该框架耦合在一起
- **C** 在成功请求上按 5% 采样
- **D** 在 HTTP/OpenAI-SDK 层埋点

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 5. 本课把哪一套 OpenTelemetry 约定认定为 2026 年各可观测性工具之间的互操作层？

- **A** GenAI 语义约定（gen_ai.system、gen_ai.request.model、gen_ai.usage.input_tokens）
- **B** OTel HTTP 语义约定
- **C** OTel 数据库语义约定
- **D** OTel 消息（messaging）语义约定

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 6. 为什么本课主张全量 trace 保留无法在超过每天 100 万请求时扩展？

- **A** 厂商会阻止它
- **B** 保留所需的存储成本超过了 LLM 调用本身；团队必须采样（例如 100% 错误、100% 高成本、5% 成功）
- **C** Phoenix 只支持 100 万条 trace
- **D** OpenTelemetry 对 trace 总量设有上限

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>


[返回本课](docs/zh.md)
