# 为 MCP Server 授权访问 · 自测

每题先选答案，再展开解析。

## 1. client 尚未对某个 MCP server 进行过身份验证时，server 要求授权的第一个信号是什么？

- **A** server 的 tools/list 结果在登录完成前悄悄省略所有工具
- **B** tools/call 收到不带 JSON-RPC body 的纯 HTTP 401 响应
- **C** server 要求先完成旧版 initialize 握手，之后才签发 token
- **D** client 的连接尝试反复超时，直到提供凭据

<details>
<summary>查看答案与解析</summary>

**答案**　B

未经身份验证的请求在解析为协议消息前就会在 HTTP 层以 401 拒绝，因此没有 result 或 error body 可读。

</details>

## 2. 401 响应的 WWW-Authenticate header 不含 resource_metadata 值。client 接下来必须如何查找 Protected Resource Metadata 文档？

- **A** 要求用户把 authorization server 的 URL 粘贴到配置文件
- **B** 立即中止流程，因为规范只允许通过 header 发现
- **C** 回退到 well-known URI，先尝试路径专用位置，再尝试根位置
- **D** 回退到 well-known URI，先尝试根位置，再尝试路径专用位置

<details>
<summary>查看答案与解析</summary>

**答案**　C

header 省略 resource_metadata 时，client 必须自行构造 well-known URI，先尝试路径专用位置，再回退到根位置。

</details>

## 3. authorization server 的 issuer 是带路径的 URL https://auth.example.com/tenant1。client 必须按什么顺序尝试 metadata endpoint？

- **A** 只尝试根位置的 oauth-authorization-server，因为发现前会移除路径
- **B** 先尝试路径后置的 openid-configuration，再尝试路径插入的 oauth-authorization-server，最后尝试路径插入的 openid-configuration
- **C** 只尝试路径插入的 openid-configuration，因为 MCP 没有定义 OAuth 专用 well-known suffix
- **D** 先尝试路径插入的 oauth-authorization-server，再尝试路径插入的 openid-configuration，最后尝试路径后置的 openid-configuration

<details>
<summary>查看答案与解析</summary>

**答案**　D

对于带路径 issuer，client 先尝试路径插入的 OAuth metadata，再尝试路径插入的 OpenID Connect discovery，最后尝试路径后置的 OpenID Connect discovery。

</details>

## 4. MCP server 接受调用前必须校验传入 bearer token 的 audience。该检查实际验证什么？

- **A** token 专门为此 MCP server 自身的规范 URI 签发
- **B** token 携带被请求工具可能需要的所有 scope
- **C** token 自 authorization server 签发后尚未过期
- **D** token 由 client 以前使用过的 authorization server 签发

<details>
<summary>查看答案与解析</summary>

**答案**　A

audience 校验确认 token 指向此 server 自身的规范 resource URI，因此为其他 server 签发的格式正确 token 仍必须遭拒。

</details>

## 5. client 即将在本次流程中首次把用户浏览器重定向到 authorization server。为防御 mix-up 攻击，它在 redirect 前必须做什么？

- **A** 先请求一个新 access token，redirect 完成后再丢弃
- **B** 记录已校验 metadata 中的预期 issuer，以便和返回的 iss 值比较
- **C** 缓存 authorization server 的 TLS 证书指纹，并在 redirect 返回后比较
- **D** 为这一次授权尝试注册全新的 redirect URI

<details>
<summary>查看答案与解析</summary>

**答案**　B

RFC 9207 的 mix-up 防御依赖 client 在 redirect 前记录预期 issuer，并将它与 authorization response 返回的 iss 值精确比较。

</details>

## 6. resource server 收到一个格式正确且未过期的 token，但其 audience 指向另一个 MCP server。它应如何处理？

- **A** 接受调用，因为来自已知 authorization server 的有效格式 token 可以信任
- **B** 把 token 转发给目标 server，并将响应代理回调用方
- **C** 以 401 Unauthorized 拒绝，因为该 token 对此 server 无效
- **D** 以 403 Forbidden 拒绝，因为 token 缺少所需 scope

<details>
<summary>查看答案与解析</summary>

**答案**　C

无论签名或有效期如何，audience 指向其他 server 的 token 对当前 server 都无效，因此应以 401 拒绝，而不是表示 scope 问题的 403。

</details>


[返回本课](docs/zh.md)
