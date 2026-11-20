# LLM 的 FinOps —— 单位经济学与多租户归因 · 自测

每题先选答案，再展开解析。

## 1. 为什么传统 FinOps 在 LLM 支出上失效？

- **A** LLM 不花钱
- **B** 成本是 token 交易而非资源在线时长；标签不会从 API 调用自动传播，你必须在调用现场打上 user/task/tenant 戳记
- **C** LLM 账单总是免费的
- **D** 云服务商拒绝逐项列出

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 2. 本课要求从第一天就埋点哪三个归因维度？

- **A** 区域、可用区、数据中心
- **B** 按用户（user_id）、按任务（task_id + route）、按租户（tenant_id）
- **C** GPU、CPU、内存
- **D** 供应商、模型、API 版本

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 3. 在成本归因中应当拆分出哪四个 token 层？

- **A** 缓存、模型、网关、可观测性
- **B** prompt、tool、memory、response
- **C** 输入、输出、网络、磁盘
- **D** GPU、CPU、内存、存储

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 4. 在执法阶梯中，熔断开关（kill-switch）的触发条件是什么？

- **A** 一分钟内支出超过 1 美元
- **B** 租户支出相对基线的 z 分数 > 4；自动暂停该租户并呼叫值班
- **C** 延迟 P50 > 2 秒
- **D** 任何 5xx 响应

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 5. 本课推荐用哪个单位指标取代「每百万 token 美元数」？

- **A** 每秒成本
- **B** 每个产品成果的成本（例如每解决一张支持工单的成本、每生成一篇文章的成本、每完成一个 agent 任务的成本）
- **C** 每网关成本
- **D** 每 GPU 小时成本

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 6. 本课把哪种归因模式称为成熟团队所用的最高精度方案？

- **A** 采样与外推
- **B** 仅打标签并聚合
- **C** 基于模型的分摊
- **D** 遥测连接器（telemetry joiner）—— 通过 trace ID 把 trace 与账单关联起来

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>


[返回本课](docs/zh.md)
