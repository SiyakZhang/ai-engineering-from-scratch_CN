# 向 Authorization Server 证明 Client 身份 · 自测

每题先选答案，再展开解析。

## 1. MCP client 即将连接一个 server，且从未使用过它的 authorization server，但 client 已保存该 authorization server 的信息。根据规范的注册优先顺序，client 应怎么做？

- **A** 通过 Dynamic Client Registration 注册全新 client，避免使用过期凭据
- **B** 使用已经为该 authorization server 保存的预注册凭据
- **C** 向 server 发送任何请求前，先提示用户输入 client id
- **D** 仍然获取 Client ID Metadata Document，因为它始终优先于存储信息

<details>
<summary>查看答案与解析</summary>

**答案**　B

预注册凭据位于优先顺序首位；只有该 issuer 没有存档信息时，client 才依次尝试 Client ID Metadata Document、Dynamic Client Registration，最后询问用户。

</details>

## 2. Client ID Metadata Document 从 https://app.example.com/oauth/client.json 获取。authorization server 信任该文档前必须确认哪项属性？

- **A** 文档通过纯 HTTP 获取，以便 authorization server 缓存
- **B** 文档已提前通过 registration_endpoint 调用注册
- **C** 文档中的 client_id 字段与该 URL 逐字符精确匹配
- **D** 文档包含 authorization server 可在本地验证的 client secret

<details>
<summary>查看答案与解析</summary>

**答案**　C

authorization server 必须验证文档内的 client_id 与获取文档的 URL 精确相等；若不匹配，就不能把该文档作为 client 身份予以信任。

</details>

## 3. 桌面 CLI 工具通过 Dynamic Client Registration 注册，并重定向到 http://127.0.0.1:PORT/callback。它应声明哪个 application_type？

- **A** confidential，因为 CLI 工具能在本地磁盘安全存储 client secret
- **B** 应省略 application_type，因为非 OIDC server 始终忽略该字段
- **C** web，因为 authorization server 只为浏览器 client 读取 application_type
- **D** native，因为该工具是通过 localhost 访问的本地托管应用

<details>
<summary>查看答案与解析</summary>

**答案**　D

native application 包括桌面工具、CLI 和通过 localhost 访问的本地托管应用，应声明 application_type native；OIDC 中省略会默认为 web，可能与 localhost redirect URI 冲突。

</details>

## 4. client 的持久化凭据由 authorization server A 签发，但同一 MCP server 的 protected resource metadata 现在改为指向 authorization server B。client 必须怎么做？

- **A** 将凭据视为对 B 无效，并向正确的 server 重新注册
- **B** 把两个 authorization server 合并进共享单一 client id 的信任域
- **C** 把 A 的凭据转发给 B，由 B 决定是否接受
- **D** 继续使用 A 的凭据，因为 resource server 本身没有变化

<details>
<summary>查看答案与解析</summary>

**答案**　A

凭据绑定到签发它的 issuer；authorization server 变更时，client 不得复用旧凭据，必须向新的 server 重新注册。

</details>

## 5. MCP proxy 使用一个静态 client id，代表许多动态注册的下游 client 连接第三方 authorization server。规范对该 proxy 有何要求？

- **A** 无需额外操作，因为静态 client id 已代表所有下游 client
- **B** 转发前必须分别取得用户对每个动态注册 client 的同意
- **C** 必须为服务的所有下游 client 完全禁用 Dynamic Client Registration
- **D** 每出现一个新下游 client，都必须轮换静态 client id

<details>
<summary>查看答案与解析</summary>

**答案**　B

使用静态 client id 的 proxy 存在 confused deputy 风险；规范要求它在把每个动态注册 client 的请求转发给第三方 authorization server 前，分别取得用户同意。

</details>

## 6. CI pipeline 需要每晚定时调用 MCP server，且没有人可以批准访问。哪种机制合适，server 又如何得知 client 支持它？

- **A** Dynamic Client Registration，因为它是唯一为无人值守 client 构建的流程
- **B** Enterprise-Managed Authorization，因为它完全不再需要 access token
- **C** OAuth Client Credentials extension，由 client 在每次请求的 capabilities 中声明
- **D** 标准交互式 authorization code 流程，由管理员提前批准一次

<details>
<summary>查看答案与解析</summary>

**答案**　C

没有交互用户的 machine-to-machine 访问适合 OAuth Client Credentials extension；client 在每次请求的 io.modelcontextprotocol/clientCapabilities.extensions 中声明支持。extension 需要显式选择，绝不会默认启用。

</details>


[返回本课](docs/zh.md)
