# 扩展框架 · 自测

每题先选答案，再展开解析。

## 1. 某团队希望在 MCP 核心 primitive 之外增加一种能力，同时避免与其他提出相同想法的人发生命名冲突。扩展标识符必须包含什么？

- **A** 根据其设置对象计算出的校验和
- **B** 紧跟名称之后的数字版本后缀
- **C** 位于斜杠和名称之前的强制厂商前缀
- **D** 表明字段仍处于实验阶段的前导下划线

<details>
<summary>查看答案与解析</summary>

**答案**　C

扩展标识符采用 vendor-prefix/extension-name 格式。与普通 _meta 键不同，这里的前缀不能省略，从而避免无关厂商及官方扩展使用同一名称时发生冲突。

</details>

## 2. 在 2026-07-28 版本中，客户端要在哪里声明希望为某一次 tools/call 请求激活的扩展？

- **A** 连接打开时只发送一次的 initialize 请求 capabilities 中
- **B** 附在同一个 HTTP 请求上的 Mcp-Extensions header 中
- **C** 紧接在调用之前发送的独立 extensions negotiate 请求中
- **D** 该请求自身的 _meta 中，位于 clientCapabilities extensions 下

<details>
<summary>查看答案与解析</summary>

**答案**　D

2026-07-28 没有 initialize 握手或 session；客户端必须在每个请求的 _meta 中重新声明扩展，位置是 io.modelcontextprotocol/clientCapabilities.extensions。

</details>

## 3. 客户端请求声明了扩展 A 和 B，服务器 capabilities 列出扩展 B 和 C。本次调用会激活哪个扩展？

- **A** 只有 B，因为只有它被双方同时点名
- **B** 全部不激活，因为还需要单独的确认步骤
- **C** A、B、C，因为声明其中任意一个就会激活全部三个
- **D** 只有 A，因为行为是由客户端提出请求的

<details>
<summary>查看答案与解析</summary>

**答案**　A

只有同一个标识符同时出现在客户端声明能力和服务器自身能力中，扩展才会激活，因此这里的协商集合只有 B。

</details>

## 4. 某工具不存在有意义的纯核心协议行为，只有一个特定的必要扩展处于活跃状态时才能工作。客户端未声明该扩展便调用了工具。符合规范的服务器应返回什么？

- **A** JSON-RPC 错误 -32001，即旧版工具失败错误码
- **B** JSON-RPC 错误 -32021，并点明仍需要的扩展
- **C** JSON-RPC 错误 -32601，因为方法本身未知
- **D** 只带 isError true、不含其他细节的普通结果

<details>
<summary>查看答案与解析</summary>

**答案**　B

请求需要某项能力（包括扩展），但自身 clientCapabilities 未声明时，应以 MissingRequiredClientCapabilityError（-32021）拒绝，并在 data.requiredCapabilities 中点明缺少的能力。

</details>

## 5. Core Maintainers 开始评审新的官方扩展提案之前，必须已经具备什么？

- **A** 由所有已注册 MCP 服务器运营者参与的公开投票
- **B** 针对草案记录满一年的生产流量
- **C** 该扩展在官方 SDK 中可工作的参考实现
- **D** 表明所有主流客户端均已支持的完整矩阵

<details>
<summary>查看答案与解析</summary>

**答案**　C

与 Standards Track SEP 不同，Extensions Track SEP 必须先在官方 SDK 中拥有参考实现，Core Maintainers 才会开始评审。

</details>

## 6. 官方扩展的维护者需要删除一个既有实现所依赖的字段。框架要求他们怎么做？

- **A** 要求所有客户端厂商在同一天完成更新
- **B** 像核心功能一样等待十二个月的弃用期
- **C** 直接静默发布，因为扩展演进无需核心评审
- **D** 使用新标识符发布变更，而不是沿用现有标识符

<details>
<summary>查看答案与解析</summary>

**答案**　D

删除字段等破坏性变更必须使用新的扩展标识符发布，例如添加 v2 后缀。这样，仍声明旧标识符的实现会继续获得旧有、未改变的行为。

</details>


[返回本课](docs/zh.md)
