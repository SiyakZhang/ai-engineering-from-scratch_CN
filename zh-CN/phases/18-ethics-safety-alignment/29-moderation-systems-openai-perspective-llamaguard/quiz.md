# 审核系统 —— OpenAI、Perspective、Llama Guard · 自测

每题先选答案，再展开解析。

## 1. OpenAI 的 omni-moderation-latest（2024）是什么？

- **A** 一个 C2PA 水印端点
- **B** 一个专注推理的前沿模型
- **C** 一个 RLHF 奖励模型
- **D** 一个基于 GPT-4o 的审核分类器，可在一次调用中同时处理文本和图像，返回 13 类响应 schema（骚扰、仇恨、自残、性、暴力、违法，及其子类别），对大多数开发者免费

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 2. 以下哪一项不是 OpenAI Moderation 的主要顶层类别之一？

- **A** violence（暴力）
- **B** harassment（骚扰）
- **C** election-interference（干预选举）
- **D** self-harm（自残）

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 3. 2026 年标准审核模式的三层是什么？

- **A** Tokenizer / 模型 / detokenizer
- **B** Probe / detector / harness
- **C** 输入审核（生成前）、输出审核（生成后）、自定义审核（领域规则）
- **D** 望远镜式 / 潜望镜式 / 显微镜式

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 4. Perspective API（Google Jigsaw）主要被设计用来对什么打分？

- **A** 用户满意度奖励
- **B** 推理质量
- **C** 毒性（toxicity，带有严重毒性、侮辱、脏话、威胁、身份攻击等子维度），作为 LLM 时代之前的内容审核基线
- **D** 水印强度

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 5. 仅做输入审核的一种失败模式是什么？

- **A** 它消除了对输出分类器的需求
- **B** 它无法在 GPU 上运行
- **C** 它总是拦截合法内容
- **D** 它无法捕捉模型输出的失败或幻觉；编码攻击（第 12-14 课）可以完全绕过输入分类器

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 6. Azure Content Moderator 的弃用情况和迁移目标是什么？

- **A** 并入 Llama Guard 4
- **B** 于 2024 年 2 月弃用，2027 年 3 月 15 日停服；迁移目标是 Azure AI Content Safety（基于 LLM，与 Azure OpenAI 集成）
- **C** 立即弃用且无替代品
- **D** 被 Perspective API 取代

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>


[返回本课](docs/zh.md)
