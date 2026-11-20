# 显式 Scope 与无状态 Elicitation · 自测

每题先选答案，再展开解析。

## 1. MCP Roots 提供了什么 security guarantee？

- **A** 每个 server process 的 operating-system isolation
- **B** 信息性 workspace guidance，而非 authorization 或 sandboxing
- **C** caller 拥有 root 下每个 file 的证明
- **D** 自动防止 symbolic-link escapes

<details>
<summary>查看答案与解析</summary>

**答案**　B

Roots 是信息性的，并在 2026-07-28 中弃用。server 仍需要 authorization、containment 和 sandboxing。

</details>

## 2. 当 workspace scope 每次 tool call 都变化时，最清晰的现代替代方案是什么？

- **A** 由 server 授权的显式 workspace URI argument
- **B** 存于 transport session 下的隐藏 value
- **C** mutation 后发送的 roots/list request
- **D** self-reported clientInfo name

<details>
<summary>查看答案与解析</summary>

**答案**　A

显式 handle 可见且可 replay，但 server 仍必须为 authenticated principal 授权它。

</details>

## 3. 在 MCP 2026-07-28 下，form-mode elicitation 如何传递？

- **A** 由 server/discover 进行 HTTP redirect
- **B** 作为 input_required result 中的 inputRequests
- **C** 通过 Mcp-Session-Id stream 的反向 request
- **D** 通过 notifications/roots/list_changed

<details>
<summary>查看答案与解析</summary>

**答案**　B

MRTR 将 elicitation/create 嵌入 inputRequests，随后 client 使用 inputResponses 重试原始 operation。elicitation {} 和 elicitation.form 支持 form mode；仅 URL support 返回带 data.requiredCapabilities.elicitation.form 的 -32021。

</details>

## 4. 哪种 value 绝不可通过 form-mode elicitation 收集？

- **A** 从 enum 选择的 note id
- **B** API access token
- **C** 非敏感 display preference
- **D** boolean 的破坏性 action confirmation

<details>
<summary>查看答案与解析</summary>

**答案**　B

secrets 与 credentials 不得经过 MCP client。敏感外部 interaction 应使用仔细绑定的 URL-mode flow。

</details>

## 5. 用户 decline deletion elicitation。安全结果是什么？

- **A** 将缺失 content 视为隐式 consent
- **B** 返回 complete、non-error 的拒绝 outcome，并保留 note
- **C** 删除，因为模型已经选择 note
- **D** 重复相同 dialog 直到用户 accept

<details>
<summary>查看答案与解析</summary>

**答案**　B

Decline 是明确拒绝，不能转为 consent、error-loop prompting 或 mutation。

</details>

## 6. 哪种设计能将破坏性 confirmation 安全绑定到用户所见内容？

- **A** 仅 Base64-encode 已选 note id，不签名
- **B** 签名 principal、原始 argument digest、candidate ids、phase 和 expiry，再重新检查 live target
- **C** 将 clientInfo 用作权威 user identity
- **D** 信任随 action accept 返回的任意 note id

<details>
<summary>查看答案与解析</summary>

**答案**　B

完整性保护 state 可防止篡改。共享原子 one-time nonce claim 防止 replay，最终 live checks 在 mutation 前处理 races。

</details>


[返回本课](docs/zh.md)
