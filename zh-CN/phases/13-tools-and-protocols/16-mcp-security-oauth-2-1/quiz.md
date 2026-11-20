# MCP 授权：CIMD、签发方绑定、PKCE 与权限升级 · 自测

每题先选答案，再展开解析。

## 1. 在 2026-07-28 中，新的 MCP OAuth client 注册优先使用哪种机制？

- **A** Dynamic Client Registration
- **B** 把 access token 放在 URL 中
- **C** Mcp-Session-Id
- **D** Client ID Metadata Documents

<details>
<summary>查看答案与解析</summary>

**答案**　D

优先使用 CIMD；DCR 已被弃用，仅保留为兼容路径。

</details>

## 2. 带有 loopback 重定向的桌面 client 在 DCR 回退期间应声明什么 application_type？

- **A** native
- **B** confidential
- **C** stateless
- **D** web

<details>
<summary>查看答案与解析</summary>

**答案**　A

桌面、移动端、命令行和 loopback client 都是 native 应用。

</details>

## 3. client 必须如何处理授权响应中的 iss 值？

- **A** 在使用响应前，将它与已记录的 issuer 精确比较
- **B** PKCE 成功后忽略它
- **C** 规范化它，再比较 hostname
- **D** 将它存为 clientInfo

<details>
<summary>查看答案与解析</summary>

**答案**　A

RFC 9207 的 issuer 校验可以防止不同 issuer 之间的授权响应混淆。

</details>

## 4. client 应如何为由 issuer 生成的 OAuth 凭据和 access token 设置存储键？

- **A** 所有注册和 token 都放在一个全局 client 名称下
- **B** 按协议会话标识符存储
- **C** 只按 server 展示名称存储
- **D** 由 issuer 生成的凭据按 issuer 存储，token 按 issuer 加 resource 存储

<details>
<summary>查看答案与解析</summary>

**答案**　D

issuer 和 resource 键防止已生成的凭据跨越安全主体或 audience。自行托管的 CIMD URL 仍可移植。

</details>

## 5. 资源返回 scope 为 notes:delete 的 403 后，正确的下一步是什么？

- **A** 解释该 scope、取得同意、为其授权，然后用新的请求 id 重试
- **B** 把 MCP token 发送给下游 API
- **C** 不经授权就在本地添加 notes:delete
- **D** 复用当前 token 并忽略 challenge

<details>
<summary>查看答案与解析</summary>

**答案**　A

权限升级会先取得新授权的 token，再重试操作。

</details>

## 6. MCP 资源 https://notes.example.com/mcp 对应的 RFC 9728 元数据 URL 是什么？

- **A** https://notes.example.com/mcp/.well-known/oauth-protected-resource
- **B** https://notes.example.com/.well-known/oauth-protected-resource
- **C** https://notes.example.com/.well-known/oauth-protected-resource/mcp
- **D** https://auth.example.com/.well-known/oauth-protected-resource

<details>
<summary>查看答案与解析</summary>

**答案**　C

RFC 9728 会在 well-known 段之后保留受保护资源 path，因此必须带上 /mcp 后缀。

</details>


[返回本课](docs/zh.md)
