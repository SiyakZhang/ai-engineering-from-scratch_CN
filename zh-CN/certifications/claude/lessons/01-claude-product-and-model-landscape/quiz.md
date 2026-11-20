# 选择能承载工作的最小载体 · 自测

每题先选答案，再展开解析。

## 1. 某个受监管应用必须使用现有 Azure 协议、Entra 身份、Azure RBAC 和美国数据区部署。哪条路径最值得优先评估？

- **A** 使用 AWS 区域端点的 Amazon Bedrock
- **B** 采用所需 Azure 托管和部署类型的 Microsoft Foundry
- **C** Claude for Enterprise 席位加直连 Claude API workspaces
- **D** 使用美国多区域端点的 Google Vertex AI

<details>
<summary>查看答案与解析</summary>

**答案**　B

Foundry 符合题目给出的采购、身份、运维和云边界要求。团队仍需核验当前托管选项与功能支持。

</details>

## 2. 什么时候 Research 比直接网页搜索更合适？

- **A** 需要从权威的一手页面确认一个最新事实时
- **B** 答案需要引用，但相关来源和主张都已经明确时
- **C** 必须收集、协调并引用多个来源时
- **D** 必须打开一份已知文档，核对确切政策条款时

<details>
<summary>查看答案与解析</summary>

**答案**　C

Research 适合范围广泛的多步骤调查。核对单个事实通常只需要更简单的搜索和验证路径。

</details>

## 3. 在 Haiku、Sonnet 和 Opus 之间做选择时，哪条长期规则最稳妥？

- **A** 选择上下文窗口最大的家族，再调整 prompt 以满足成本目标
- **B** 根据公开定位，为每个家族永久分配一种任务类别
- **C** 外部工作默认使用最强家族，再为低风险内部任务降级
- **D** 用代表性成功标准测试最小的可行家族，仅在实测失败时升级

<details>
<summary>查看答案与解析</summary>

**答案**　D

模型家族的定位有参考价值，但实际选择应依据任务的质量、延迟和成本约束进行实测。

</details>

## 4. 某组织为员工购买 Claude for Enterprise，同时又从应用调用直连 Claude API。哪种控制设计最合理？

- **A** 将具名用户席位和成员限制，与 API workspace 密钥、速率限制和支出上限分开治理
- **B** 只选一个控制平面，因为 Anthropic 直连产品共享相同的身份与预算语义
- **C** 用 Enterprise 席位政策管理应用速率限制，用 API workspace 管理员工访问
- **D** 把席位和 API token 视为同一个容量池，因为两者都向 Anthropic 采购

<details>
<summary>查看答案与解析</summary>

**答案**　A

人员席位与应用用量是不同的使用形态。即使都采用直采，也必须分别明确身份、预算和访问控制。

</details>

## 5. 一家以 AWS 为主的公司要求使用 AWS IAM、AWS 计费和 AWS 管理的推理安全边界。哪条部署路径最符合这些要求？

- **A** Google Vertex AI，因为多区域端点与云无关
- **B** Amazon Bedrock，并核验当前模型、区域和功能
- **C** Claude for Enterprise，因为 SSO 可以取代工作负载 IAM
- **D** Microsoft Foundry，因为 Azure Marketplace 费用可以转计到 AWS

<details>
<summary>查看答案与解析</summary>

**答案**　B

Bedrock 符合题目给出的 AWS 控制平面。当前模型访问、端点、数据处理和功能支持仍属于必须标注日期的输入。

</details>

## 6. 某 Google Cloud 团队需要在现有项目、IAM、计费和欧盟端点策略内运行应用推理。其 ADR 应该怎么做？

- **A** 选择 Vertex AI，并永久写入今天的功能矩阵，因为项目身份会保持稳定
- **B** 只比较 token 价格，因为 Google Cloud 已经负责身份、采购和事件响应
- **C** 选择 Vertex AI，并记录当前模型、功能、端点、数据处理者和定价证据及其核验日期
- **D** 选择直连 Claude API，因为模型行为在各供应商间相同，控制平面不会影响架构

<details>
<summary>查看答案与解析</summary>

**答案**　C

Vertex AI 符合题目给出的控制平面，但 ADR 必须为每项可能变化的平台事实保留带日期的证据，并写明复核触发条件。

</details>


[返回本课](docs/zh.md)
