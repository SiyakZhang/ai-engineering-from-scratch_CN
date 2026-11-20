# API 与密钥 · 自测

每题先选答案，再展开解析。

## 1. 调用 LLM 服务时，API 密钥用来做什么？

- **A** 选择服务器使用哪种编程语言
- **B** 加密发送到服务器的数据
- **C** 验证你的身份并授权请求
- **D** 压缩请求以减少带宽

<details>
<summary>查看答案与解析</summary>

**答案**　C

API 密钥是一串唯一字符串，用于标识你的账户、授权你的请求，并让服务商能够追踪用量和计费。

</details>

## 2. 为什么绝不应该把 API 密钥直接硬编码在源代码里？

- **A** Python 无法读取超过 50 个字符的字符串字面量
- **B** API 服务商会封禁出现在源文件中的密钥
- **C** 它们可能被意外提交到 git 并被公开泄露
- **D** 硬编码的密钥会让代码运行变慢

<details>
<summary>查看答案与解析</summary>

**答案**　C

源代码中硬编码的密钥有被提交到版本控制并推送到公开仓库的风险，在那里它们可能被他人抓取和滥用。

</details>

## 3. 在本地开发时，推荐用哪种方式存储 API 密钥？

- **A** 放在 requirements.txt 里与包版本写在一起
- **B** 放在脚本顶部的一个 Python 变量里
- **C** 放在 README.md 里以便随手取用
- **D** 放在一个已列入 .gitignore 的 .env 文件里

<details>
<summary>查看答案与解析</summary>

**答案**　D

.env 文件以环境变量的形式存储密钥，并应加入 .gitignore，这样它永远不会被提交到版本控制。SDK 会自动从环境变量中读取密钥。

</details>

## 4. 在向 Anthropic 发起的原始 HTTP API 调用中，哪个请求头携带 API 密钥？

- **A** anthropic-version: 2023-06-01
- **B** Authorization: Bearer sk-ant-...
- **C** Content-Type: application/json
- **D** x-api-key: sk-ant-...

<details>
<summary>查看答案与解析</summary>

**答案**　D

Anthropic 的 API 使用 'x-api-key' 请求头进行认证，而不是更常见的 'Authorization: Bearer' 模式。这是其 API 设计的特有之处。

</details>

## 5. 当你超过某个 API 的速率限制时会发生什么？

- **A** 服务器返回一个错误（通常是 HTTP 429），你必须等待后再重试
- **B** 你的请求会被排队，稍后自动处理
- **C** API 会静默丢弃你的请求且不返回任何响应
- **D** 你的 API 密钥被永久吊销

<details>
<summary>查看答案与解析</summary>

**答案**　A

速率限制会返回 HTTP 429（请求过多）。你需要等待后重试，通常采用指数退避。速率限制可防止滥用并确保公平使用。

</details>


[返回本课](docs/zh.md)
