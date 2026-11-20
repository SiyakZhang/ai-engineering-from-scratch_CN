# 构建 MCP Client：发现、路由与双时代回退 · 自测

每题先选答案，再展开解析。

## 1. 双时代 stdio client 应首先发送什么？

- **A** server/discover
- **B** initialize
- **C** Mcp-Session-Id
- **D** HTTP GET

<details>
<summary>查看答案与解析</summary>

**答案**　A

发现 probe 在现代逐请求元数据与旧版初始化之间建立了清晰边界。

</details>

## 2. 发现 probe 返回带有双方支持版本的 -32022。client 应如何做？

- **A** 打开 HTTP GET
- **B** 以受支持版本重试现代发现
- **C** 发送 initialize
- **D** 忽略该 server

<details>
<summary>查看答案与解析</summary>

**答案**　B

-32022 是已识别的现代证据，因此 client 保持现代方式并重试。

</details>

## 3. 选择旧版 era 的充分条件是什么？

- **A** peer 位于旧版 allowlist
- **B** 仅仅一次发现 timeout
- **C** 任意 -32601 error
- **D** peer 已 allowlisted，且有限 initialize probe 返回有效、受支持的旧版结果

<details>
<summary>查看答案与解析</summary>

**答案**　D

allowlist 允许探测，但只有为配置旧版 revision 得到结构上有效的正向 initialize 结果，才能证明旧版 era。

</details>

## 4. client 应如何处理两个都叫 search 的 tools？

- **A** 创建协议 session
- **B** 静默覆盖其中一个
- **C** 相信启动顺序
- **D** 按声明 policy 加前缀或拒绝

<details>
<summary>查看答案与解析</summary>

**答案**　D

显式加前缀或拒绝，能让路由可见且保持确定性。

</details>

## 5. client 协商旧版 era 后，某个旧版结果缺少 resultType。应如何解释？

- **A** 解释为 server/discover
- **B** 解释为 input_required
- **C** 解释为 complete
- **D** 解释为 transport error

<details>
<summary>查看答案与解析</summary>

**答案**　C

client 将较早协议版本中缺失的 resultType 视作 complete。

</details>

## 6. 现代 transport 丢失后，在恢复路由前必须做什么？

- **A** 用 Last-Event-ID 恢复
- **B** 重连、重新发现并重新列出
- **C** 复用旧 connection metadata
- **D** 回显 Mcp-Session-Id

<details>
<summary>查看答案与解析</summary>

**答案**　B

client 重建 peer bookkeeping，并只以新的请求 ids 重试安全操作。

</details>


[返回本课](docs/zh.md)
