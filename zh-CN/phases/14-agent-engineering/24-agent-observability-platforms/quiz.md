# Agent 可观测性：Langfuse、Phoenix、Opik · 自测

每题先选答案，再展开解析。

## 1. 在 2025 年 6 月把原先的商业模块开源后，Langfuse 以什么许可证发布？

- **A** MIT
- **B** GPLv3
- **C** Apache 2.0
- **D** Elastic License 2.0

<details>
<summary>查看答案与解析</summary>

**答案**　A

2025 年 6 月后，Langfuse 是 MIT，包括 LLM-as-a-judge、标注队列、prompt 实验和 Playground。

</details>

## 2. 按本课所说，Arize Phoenix 最擅长什么？

- **A** 自动化优化循环
- **B** prompt 版本管理
- **C** 深度的、agent 专属的评估：trace 聚类、异常检测、RAG 检索相关性、OpenInference 自动 instrumentation
- **D** 代码的静态分析

<details>
<summary>查看答案与解析</summary>

**答案**　C

Phoenix 专注于行为漂移和 RAG 评估，配 OpenInference 自动 instrumentation。

</details>

## 3. 哪个平台把自动 prompt 优化与护栏（PII 脱敏、话题约束）以及 LLM 评判的幻觉检测配在一起？

- **A** Opik
- **B** Langfuse
- **C** Phoenix
- **D** Jaeger

<details>
<summary>查看答案与解析</summary>

**答案**　A

Opik 以「优化 + 护栏」循环为核心。

</details>

## 4. 本课为带 prompt 管理的一体化推荐哪个平台？

- **A** Datadog APM
- **B** Opik
- **C** Phoenix
- **D** Langfuse

<details>
<summary>查看答案与解析</summary>

**答案**　D

Langfuse 端到端覆盖 tracing + prompt 管理 + 评估 + 会话回放。

</details>

## 5. 本课对厂商发布的平台基准怎么说？

- **A** 只有 Opik 的可靠
- **B** 它们是权威的
- **C** 它们被 OpenTelemetry 禁止
- **D** 把它们当作方向性参考；用你自己的语料来衡量

<details>
<summary>查看答案与解析</summary>

**答案**　D

即便是引用的 Opik 与 Langfuse 之间 14 倍的差距，决定前也应在你自己的数据上衡量。

</details>

## 6. 为什么有 tracing 而无评估被视为昂贵的日志记录？

- **A** 磁盘比 CPU 贵
- **B** 提供商对 span 收费
- **C** span 无法被重放
- **D** 你能看到运行但不给它们打分，因此回归不可见、二分定位不可能

<details>
<summary>查看答案与解析</summary>

**答案**　D

评估才是把 trace 转化为可付诸行动的质量信号的东西。

</details>

## 7. 本课关于自建 LLM 评判者的警告是什么？

- **A** 它们被 Apache 2.0 禁止
- **B** CRITIC 适用：评判者需要外部接地来做事实核实，否则就会盖橡皮图章
- **C** 它们必须在 GPU 上运行
- **D** 它们只在 TypeScript 中有效

<details>
<summary>查看答案与解析</summary>

**答案**　B

没有基于外部工具的核实，LLM 评判者会漂向盖橡皮图章（CRITIC，第 5 课）。

</details>


[返回本课](docs/zh.md)
