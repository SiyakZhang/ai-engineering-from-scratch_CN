# 合规 —— SOC 2、HIPAA、GDPR、PCI-DSS、EU AI Act、ISO 42001 · 自测

每题先选答案，再展开解析。

## 1. 欧盟 AI 法案针对高风险系统的执法何时开始？

- **A** 2025 年 2 月 2 日
- **B** 2026 年 8 月 2 日
- **C** 2030 年 1 月 1 日
- **D** 2024 年就已全面执行

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 2. 欧盟 AI 法案定义了哪种两级罚款上限？

- **A** 任何违规最高 10 万欧元
- **B** 对高风险系统义务最高 1500 万欧元或全球年营业额的 3%（第 99(4) 条）；对被禁止的 AI 行为最高 3500 万欧元或 7%（第 99(3) 条）
- **C** 没有经济处罚，只有下架令
- **D** 任何违规一律最高 100 万欧元固定罚款

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 3. 为什么事后清理 PII 不是一种站得住脚的 GDPR 姿态？

- **A** 事后处理与实时处理完全相同
- **B** 模型已经看过了数据，因此实时的推理层脱敏（在 LLM 调用之前）才是站得住脚的 2026 年标准
- **C** GDPR 完全禁止脱敏
- **D** 它在规模化时太慢

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 4. SOC 2 Type I 和 Type II 的实际区别是什么？

- **A** Type I 比 Type II 更严格
- **B** Type I 需要 HIPAA BAA
- **C** Type I 证明控制措施已设计并记录在案；Type II 证明控制措施在 6-12 个月内有效运行
- **D** Type II 仅适用于初创公司

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 5. 跨框架的控制映射旨在交付什么？

- **A** 一条满足多个框架要求的控制策略（例如访问日志映射到 ISO 27001 A.5.15-5.18、GDPR 第 32 条、HIPAA §164.312(a)）
- **B** 取消审计
- **C** 用 ISO 42001 替换所有框架
- **D** 为每个框架制定更多互不相同的控制措施

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 6. 本课对 HIPAA + LLM 工作负载有何建议？

- **A** 未签署 BAA 绝不要把 PHI 发给外部 AI 服务；三家超大规模云厂商和主要 LLM API 供应商都提供 BAA
- **B** 只用本地模型，绝不用托管的
- **C** 把 PHI 发给任意供应商；BAA 是可选的
- **D** HIPAA 不适用于 LLM

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>


[返回本课](docs/zh.md)
