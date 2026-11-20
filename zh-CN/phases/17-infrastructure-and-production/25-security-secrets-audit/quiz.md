# 安全 —— 密钥、API Key 轮换、审计日志、Guardrails · 自测

每题先选答案，再展开解析。

## 1. 2026 年 LLM 服务凭证的标准模式是什么？

- **A** 集中式 vault，由 AI 网关在运行时通过 IAM role 拉取；在 vault 中轮换，所有应用在数分钟内自动生效
- **B** 为了图快，把 API key 硬编码在配置文件里
- **C** 把密钥邮件发给每个工程师
- **D** 把密钥存放在 Slack 频道里

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 2. 本课为 API key、vault 根令牌和 CI/CD 凭证推荐什么轮换节奏？

- **A** 仅在泄露时
- **B** 90 天以内，尽可能自动化，手动时则记录并追踪
- **C** 每 5 年
- **D** 永不轮换

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 3. 为什么 PII 脱敏要使用一致性分词（Mesh 方法）？

- **A** 它比正则用更少的内存
- **B** 它会把发给模型的 prompt 加密
- **C** 这是 ISO 27001 的要求
- **D** 相同的源值映射到相同的占位符，因此 LLM 能在整个 prompt 中保留代码和关系语义

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 4. 本课为 LLM 服务子网推荐什么样的出站（egress）姿态？

- **A** 阻断所有出站，包括供应商
- **B** 允许所有出站流量
- **C** 把一小组域名加白名单（api.openai.com、api.anthropic.com、向量数据库、vault）并丢弃其余一切，配合仅允许白名单的 DNS 解析器
- **D** 允许 DNS 但阻断 HTTP

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 5. 2026 年的 Vercel 供应链事件在 CI/CD 凭证方面给了什么教训？

- **A** CI/CD 凭证等同于生产凭证 —— 存入 vault、范围收窄、积极轮换
- **B** CI/CD 密钥无法被窃取
- **C** CI/CD 凭证风险低，可以留在 env 文件里
- **D** Vercel 未受影响

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 6. 本课建议为每次 LLM 调用保留哪些审计日志字段？

- **A** 只存原始 prompt
- **B** 只存成本
- **C** 时间戳、用户/租户、prompt 哈希（而非原文）、模型 + 版本、token 计数、成本、响应哈希、任何触发的护栏
- **D** 只存响应

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>


[返回本课](docs/zh.md)
