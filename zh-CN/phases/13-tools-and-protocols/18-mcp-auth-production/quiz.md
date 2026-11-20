# 生产环境中的 MCP Auth：与 issuer 绑定的入册与 token · 自测

每题先选答案，再展开解析。

## 1. MCP client 为同一 resource 发现了不同的 authorization-server issuer。它该如何处理已有注册和 access token？

- **A** 仅在本地修改 access token 的受众后重用它
- **B** 由于 MCP resource URL 未变，因此重用两者
- **C** 将两者都存到 tool name 下，而不是 issuer 下
- **D** 为新 issuer 入册，并按 issuer 隔离凭据

<details>
<summary>查看答案与解析</summary>

**答案**　D

client identifier 和注册凭据属于创建它们的 authorization-server issuer。issuer 变化要求独立入册，而每个 access token 同时按该 issuer 和它的 resource audience 缓存。

</details>

## 2. MCP 2026-07-28 authorization profile 首选哪种入册方式？

- **A** 每个请求都使用 RFC 7591 Dynamic Client Registration
- **B** 由 client 的 HTTPS URL 提供 Client ID Metadata Document
- **C** 用 protocol session 保存一个全局 client identifier
- **D** 在每个 desktop client 中嵌入共享 client secret

<details>
<summary>查看答案与解析</summary>

**答案**　B

CIMD 让 authorization server 从 HTTPS client identifier 解析 client metadata。DCR 已废弃，仅为兼容保留。

</details>

## 3. 已废弃 DCR 请求描述一个 loopback desktop client。哪项 metadata 对正确分类至关重要？

- **A** 可复用 bearer token
- **B** 通配符 redirect URI
- **C** Mcp-Session-Id
- **D** 设为 native 的 application_type

<details>
<summary>查看答案与解析</summary>

**答案**　D

当前兼容指引要求正确的 application type。loopback desktop client 是 native；web client 使用 HTTPS redirect URI。

</details>

## 4. client 为什么要在兑换 authorization code 前校验 RFC 9207 iss 值？

- **A** 从 server/discover 中选择一个 tool
- **B** 用 issuer discovery 取代 PKCE
- **C** 防止在错误的 token endpoint 兑换诚实 issuer 的 code
- **D** 避免刷新 JWKS 缓存

<details>
<summary>查看答案与解析</summary>

**答案**　C

issuer 检查防御 authorization-server mix-up。它通过确认 response 来自 redirect 前记录的 issuer，与 PKCE 相互补充。

</details>

## 5. 在当前无状态 transport 中，MCP resource server 应将授权决定缓存在哪里？

- **A** 不作为 protocol-session 决策缓存；每个请求都校验 bearer token
- **B** 存于 Mcp-Session-Id 下，直到 client 发送 DELETE
- **C** 放到 server/discover 结果中，供之后所有调用使用
- **D** 放在 SSE connection 中，直到其重连

<details>
<summary>查看答案与解析</summary>

**答案**　A

MCP 2026-07-28 移除了 protocol session。每个请求都独立跨越 authorization boundary，因此每次都检查身份、受众、过期时间和 scope。

</details>

## 6. 在信任 authorization server 前，哪项部署证据最有力？

- **A** 一次未检查 token audience 的成功登录
- **B** 声称支持 OAuth 的产品页面
- **C** 对照 PKCE、issuer、入册和 resource-binding 要求检查目标 server 发现到的 metadata
- **D** 从旧课程复制的 vendor category table

<details>
<summary>查看答案与解析</summary>

**答案**　C

能力会随部署和版本变化。具体需要检查的是 live discovery document，之后还要做端到端 issuer 和 audience 校验。

</details>


[返回本课](docs/zh.md)
