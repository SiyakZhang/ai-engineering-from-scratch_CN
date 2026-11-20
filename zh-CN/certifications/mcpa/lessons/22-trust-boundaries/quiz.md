# MCP 交互中的信任区域 · 自测

每题先选答案，再展开解析。

## 1. 在一次 MCP 交互中，哪两个参与方位于 host 直接控制的同一信任域内？

- **A** host 及其运行的 client
- **B** client 及其连接的每一个 server
- **C** server 及其公开的工具
- **D** 模型及 server 调用的上游系统

<details>
<summary>查看答案与解析</summary>

**答案**　A

host 拥有并运行 client，两者位于同一信任域内；server 则是 host 无法控制的独立程序。

</details>

## 2. server 的发现结果中带有一个讨喜的 serverInfo.name。host 应该改用什么来作出信任决策？

- **A** server 工具注解中的 title 字段
- **B** host 连接 server 时记录的身份
- **C** server 在 serverInfo 字段中报告的名称
- **D** server 最新工具描述中显示的名称

<details>
<summary>查看答案与解析</summary>

**答案**　B

clientInfo 和 serverInfo 都是未经验证的自报信息，因此 host 必须根据自己保存的 server 连接记录作出信任决策，绝不能依赖连接对自身身份的声明。

</details>

## 3. 不在 host 受信列表中的 server，其工具声明 destructiveHint 为 false。host 作出安全决策时应如何处理这项声明？

- **A** 仅当工具描述听起来也无害时才接受
- **B** 接受，因为注解准确描述了工具行为
- **C** 忽略该声明，退回破坏性操作的默认值
- **D** 彻底拒绝该工具并将它从工具列表移除

<details>
<summary>查看答案与解析</summary>

**答案**　C

工具注解只是提示；除非 server 受信，否则 client 必须将其视为不可信。因此，不可信 server 声明 destructiveHint 为 false 时，应退回保守默认值 true。

</details>

## 4. 某工具定义包含 src 为 javascript:alert(1) 的图标。符合规范的 client 必须如何处理？

- **A** 在禁用脚本的沙箱 iframe 中渲染图标
- **B** 将图标转换成 data URI 后安全渲染
- **C** 征得用户许可后再渲染图标
- **D** 拒绝图标，因为其 scheme 不是 https 或 data

<details>
<summary>查看答案与解析</summary>

**答案**　D

client 必须拒绝使用 javascript、file 或 ftp 等不安全 scheme 的图标 URI，只接受 https 和 data URI 作为图标源。

</details>

## 5. notes server 的工具结果中有一段文本，指示 host 调用另一个 tickets server 上的删除工具。host 应如何处理？

- **A** 拒绝调用，因为是否跨 server 应由模型选择
- **B** 继续操作前，请 notes server 确认该指令
- **C** 执行调用，因为 notes server 已经连接
- **D** 把指令作为常规通知转发给 tickets server

<details>
<summary>查看答案与解析</summary>

**答案**　A

server 返回的内容是不可信数据，因此嵌在其中的指令绝不能触发对另一个 server 的调用。只有模型自行作出的选择才能跨越这条边界。

</details>

## 6. 对于需要凭据、在本地启动的 stdio server，哪种做法符合 MCP 指南？

- **A** 通过 server 发起的 sampling 请求获取凭据
- **B** 从环境变量读取凭据，而不是运行 OAuth 流程
- **C** 通过 stdio 传输执行完整的 OAuth 2.1 授权码流程
- **D** 把长期 token 嵌入 server 发布的软件包

<details>
<summary>查看答案与解析</summary>

**答案**　B

stdio 实现不应运行 OAuth 流程，而应从环境变量读取凭据，因为这种传输已经运行在用户自己的信任域内。

</details>


[返回本课](docs/zh.md)
