# 认证测评 · 自测

每题先选答案，再展开解析。

## 1. 没有共享协议时，一个组织要把 N 个 AI 应用连接到 M 个外部系统，大约需要构建和维护多少个定制集成？

- **A** M 减 N 个独立集成
- **B** N 乘 M 个独立集成
- **C** 所有应用共享一个集成
- **D** N 加 M 个独立集成

<details>
<summary>查看答案与解析</summary>

**答案**　B

没有共享协议时，每一对“应用—系统”都需要专用连接器，因此集成数量按 N×M 增长。MCP 这类标准协议把乘法成本降为大致 N+M 的加法关系。

</details>

## 2. 在 MCP 2026-07-28 中，服务端可以依据什么决定如何响应一个新请求？

- **A** 同一连接上更早的调用顺序
- **B** 从上一个已响应请求延续下来的假设
- **C** 该请求中的字段，以及其中指定的任何句柄
- **D** 连接首次建立时创建的会话对象

<details>
<summary>查看答案与解析</summary>

**答案**　C

MCP 2026-07-28 是无状态协议：服务端必须把每个请求视为自描述请求，不能从同一连接的早先流量推断身份、版本或能力。跨调用状态必须通过服务端生成、由客户端作为参数传回的显式句柄携带。

</details>

## 3. 客户端发送请求后收到 UnsupportedProtocolVersionError。接下来应该怎么做？

- **A** 原样重发同一请求并等待新结果
- **B** 永久回退到旧版 2024-11-05 initialize 握手流程
- **C** 永久关闭连接并拒绝再次联系该服务端
- **D** 使用错误中 supported 列表里的某个版本重试一次

<details>
<summary>查看答案与解析</summary>

**答案**　D

UnsupportedProtocolVersionError 的 data 中会给出服务端支持的版本。客户端应选其中一个版本重试，而不是猜测、放弃或认定必须使用旧版握手。

</details>

## 4. 按照 MCP 规范对 RFC 2119 关键词的用法，以 MUST 表述的要求对实现意味着什么？

- **A** 该行为是强制要求，不符合的实现即不合规
- **B** 该行为只是建议，实现可以合理跳过
- **C** 该行为只是多个同等有效设计中的可选方案
- **D** 该行为只是给未来规范草案的建议

<details>
<summary>查看答案与解析</summary>

**答案**　A

RFC 2119 与 RFC 8174 把 MUST 定义为绝对要求。准确区分 MUST、SHOULD 和 MAY，才能正确解读规范条款的强制程度。

</details>

## 5. MCP 的 JSON-RPC 消息结构中，哪两项说法正确？请选择两项。

- **A** 仍可把多个请求批量放进一个数组
- **B** 请求 id 不得为 null，也不能与尚未完成的请求重复
- **C** 服务端愿意时，结果响应可以安全省略 resultType
- **D** 通知不带 id，也不会收到回复

<details>
<summary>查看答案与解析</summary>

**答案**　B、D

通知没有 id，接收方不得回复；请求 id 必须非 null，且在同 id 的早先请求仍待响应时不得重复。批处理已移除，现代结果必须包含 resultType。

</details>

## 6. 某工具定义完全省略了 annotations 对象。按照默认值，客户端应如何看待该工具？

- **A** 具有破坏性、只读、幂等且封闭世界
- **B** 具有破坏性、非只读、非幂等且开放世界
- **C** 非破坏性、非幂等、封闭世界且只读
- **D** 只读、非破坏性、幂等且封闭世界

<details>
<summary>查看答案与解析</summary>

**答案**　B

省略 annotations 时采用默认值：readOnlyHint=false、destructiveHint=true、idempotentHint=false、openWorldHint=true。客户端还应把它们视为服务端提供的不可信提示，而非强制保证。

</details>

## 7. 服务端发布了一个不接收参数的工具。在 2026-07-28 规范下，哪种 inputSchema 值正确？

- **A** 用空 JSON 数组表示 schema
- **B** 用 null 表示工具不接收参数
- **C** type 为 object 且 additionalProperties 为 false 的对象 schema
- **D** 完全省略工具定义中的 inputSchema

<details>
<summary>查看答案与解析</summary>

**答案**　C

inputSchema 不能是 null，也不能省略。无参数工具仍需声明对象 schema，通常是 type=object 且 additionalProperties=false，只有空 arguments 对象能通过验证。

</details>

## 8. 宿主连接多个 MCP 服务端时，哪两项说法正确？请选择两项。

- **A** 不同服务端的工具重名时，用服务端前缀消歧
- **B** 服务端自报的 serverInfo.name 保证全局唯一，可用于路由
- **C** 所有服务端连接共享一个客户端实例
- **D** 宿主为每个服务端连接内嵌一个独立客户端

<details>
<summary>查看答案与解析</summary>

**答案**　A、D

宿主为每个服务端绑定一个客户端，以隔离职责和信任；处理重名时通常加服务端标识前缀，因为 serverInfo 是自报信息，不保证唯一。

</details>

## 9. 一次工具调用因参数验证失败，返回 isError 为 true 的结果。宿主应该如何处理？

- **A** 静默丢弃调用，永不告知模型
- **B** 完全按协议错误处理并停止所有重试
- **C** 丢弃对话并从头重启请求
- **D** 把错误内容送回模型，让它修正后重试

<details>
<summary>查看答案与解析</summary>

**答案**　D

工具执行错误是带 isError 和说明内容的普通结果，设计目的就是进入模型上下文，让模型修改参数后重试；这与协议级失败不同。

</details>

## 10. 客户端要响应 tools/call 返回的 input_required 结果，应如何把答案发回服务端？

- **A** 使用新 id 和匹配的 requestState 重试原请求
- **B** 完全独立地新建一个 elicitation/create 请求
- **C** 沿用服务端最初看到的原请求 id 回复
- **D** 把答案作为通知发送，因为不期望服务端回复

<details>
<summary>查看答案与解析</summary>

**答案**　A

多轮请求的重试必须使用新的 JSON-RPC id，带上 inputResponses，并逐字节回显 requestState。复用旧 id 或自行生成新状态都会破坏这轮交互。

</details>

## 11. 服务端接受 subscriptions/listen 请求后，发送的第一条消息必须是什么？

- **A** 携带新 subscriptionId 的进度通知
- **B** 说明服务端将接受哪些过滤条件的 acknowledged 消息
- **C** 碰巧待发送的第一条 list_changed 通知
- **D** 打开后立即关闭流的空结果

<details>
<summary>查看答案与解析</summary>

**答案**　B

流必须先发送确认消息，说明服务端会接受所请求通知类型中的哪些子集，然后才能发送 list-changed 或 resource-updated 事件。

</details>

## 12. 关于 2026-07-28 中的 tasks 扩展，哪两项说法正确？请选择两项。

- **A** 客户端通过反复调用 tasks/list 轮询进度
- **B** tasks/cancel 请求服务端协作式停止，并非瞬时中止
- **C** 客户端必须先声明扩展，服务端才能返回 task
- **D** Tasks 属于每个服务端都必须实现的核心协议

<details>
<summary>查看答案与解析</summary>

**答案**　B、C

Tasks 已从核心协议移入可选扩展。只有客户端声明支持后，服务端才能返回 task 结果；客户端用 tasks/get 而非列表方法轮询，取消也是协作式而非瞬时完成。

</details>

## 13. 未知工具名、无效 prompt 名称和缺少必需 prompt 参数，在 2026-07-28 中都对应哪个 JSON-RPC 错误码？

- **A** -32021，因为客户端缺少必需能力
- **B** -32601，因为它们都是服务端无法识别的方法
- **C** -32602，因为它们都是执行前的无效参数错误
- **D** -32002，这是所有当前服务端都应继续发出的旧版未找到错误码

<details>
<summary>查看答案与解析</summary>

**答案**　C

这三类失败都在工具或 prompt 执行前即可识别，因此 2026-07-28 将它们归为 Invalid params，而不是未知方法、旧版未找到错误或缺少客户端能力。

</details>

## 14. HTTP 请求的 Mcp-Method 标头写着 tools/call，但 JSON 正文的 method 字段是 prompts/get。服务端应该怎么做？

- **A** 合并两个方法并分别尝试部分执行
- **B** 按 tools/call 处理，因为标头优先
- **C** 信任 JSON 正文并静默忽略标头
- **D** 因标头与正文不一致，返回 -32020 拒绝请求

<details>
<summary>查看答案与解析</summary>

**答案**　D

必需标头让网关无需解析正文也能路由。因此标头与正文不一致时，服务端必须返回 HeaderMismatch（-32020），不能任选一边或混合处理。

</details>

## 15. 一个已确认幂等的工具调用，其 Streamable HTTP 响应流在结果到达前中断。客户端确认重新调用不会产生额外副作用后，正确的恢复方式是什么？

- **A** 用新 id 重新发起同一调用
- **B** 把中断的流视为空结果且成功
- **C** 彻底放弃该工具并从工具列表移除
- **D** 在同一条流上无限等待，因为结果仍会到达

<details>
<summary>查看答案与解析</summary>

**答案**　A

流一旦中断，进行中的响应就丢失了，不能依赖流恢复。只有在幂等性和重试安全已确认时，才用新 id 把调用作为全新请求重新发出；非幂等工具的结果不明时，应先确认副作用，不能盲目重放。

</details>

## 16. 在 MCP 2026-07-28 中，哪两个功能已弃用但仍可用？请选择两项。

- **A** Roots，现在通过多轮输入请求访问
- **B** Sampling，现在通过多轮输入请求访问
- **C** 用于打开通知流的 subscriptions/listen 请求
- **D** 每个服务端都必须实现的 server/discover 请求

<details>
<summary>查看答案与解析</summary>

**答案**　A、B

Roots 和 Sampling 在 2026-07-28 中已弃用，但仍通过 roots/list 和 sampling/createMessage 类型的多轮输入请求工作；server/discover 与 subscriptions/listen 仍是当前核心协议。

</details>

## 17. resources/read 结果标记为 cacheScope public。这个 scope 实际控制什么？

- **A** 服务端返回资源前是否实施访问控制
- **B** 缓存条目是否可以跨不同用户和 token 共享
- **C** 资源内容本身是否允许任何用户读取
- **D** 底层磁盘文件是否可由客户端写入

<details>
<summary>查看答案与解析</summary>

**答案**　B

cacheScope 只决定缓存响应能否跨调用者复用，不是访问控制机制。无论结果是否允许公共缓存，服务端仍必须独立授权每次读取。

</details>

## 18. 服务端的 discover 结果报告了一个看起来可信的 serverInfo 名称。serverInfo 可以正确用于什么？

- **A** 证明服务端工具描述值得信任
- **B** 无需进一步检查便给予服务端更高权限
- **C** 仅用于展示和日志，绝不能用于授权决策
- **D** 替代服务端 OAuth token 的 audience 验证

<details>
<summary>查看答案与解析</summary>

**答案**　C

clientInfo 和 serverInfo 都是自报字段，只用于展示、日志和调试。任何服务端都能声称任意名称，因此宿主不能据此授权、判断工具安全或替代 audience 验证。

</details>

## 19. 授权服务器的元数据没有列出 code_challenge_methods_supported。合规的 MCP 客户端必须怎么做？

- **A** 回退为在 URL 中发送客户端密钥
- **B** 假定支持 S256 并照常继续
- **C** 由于该字段对旧服务端可选，跳过 PKCE
- **D** 拒绝继续与该授权服务器进行授权

<details>
<summary>查看答案与解析</summary>

**答案**　D

每个 MCP 授权流程都必须使用 PKCE。授权服务器未公布支持的 challenge 方法时，客户端无法确认 PKCE 支持，必须拒绝继续，不能猜测或跳过。

</details>

## 20. MCP 客户端没有预注册凭据，而授权服务器声明支持 client_id_metadata_document_supported。接下来应尝试什么？

- **A** 使用 HTTPS URL 上的 Client ID Metadata Document 注册
- **B** 等待服务端主动把凭据推送给客户端
- **C** 直接使用 Dynamic Client Registration，因为最快
- **D** 要求最终用户手动输入 client id

<details>
<summary>查看答案与解析</summary>

**答案**　A

注册优先级是预注册、支持时使用 Client ID Metadata Documents、再使用已弃用的 Dynamic Client Registration，最后才让用户手工提供。

</details>

## 21. 请求因 403 和 insufficient_scope 失败，响应列出了客户端从未持有的三个必需 scope。客户端重试时应申请什么？

- **A** 保持原 scope 集不变，不断重试
- **B** 此前已授予 scope 与新要求 scope 的并集
- **C** 授权服务器定义过的所有 scope，以求保险
- **D** 仅申请新要求的三个 scope，放弃原有 scope

<details>
<summary>查看答案与解析</summary>

**答案**　B

阶梯式授权应申请原有 scope 与 challenge 新列出 scope 的并集，并限制重试次数。这样只精确扩权，不会缩权、过度申请或原样重复失败请求。

</details>

## 22. 哪两种做法能帮助宿主防御用户首次批准后工具定义被恶意修改？请选择两项。

- **A** 把每条 list_changed 通知都自动视为重新批准
- **B** 完全禁用 tools/list 缓存，什么都不固定
- **C** 在重新审查前，把变更后的列表视为 rug pull
- **D** 固定已批准的工具定义，复用前审查任何变化

<details>
<summary>查看答案与解析</summary>

**答案**　C、D

工具定义在获批后悄然变化就是 rug pull。防御方法是固定获批定义，并把任何变化送回重新审查；自动信任更新或仅仅禁用缓存都不能检测漂移。

</details>

## 23. 请求在 _meta 中携带 traceparent，并继续调用上游系统。该追踪上下文应如何处理？

- **A** 只存入服务端日志，绝不继续转发
- **B** 每一跳都重新生成，让各跳使用不同 trace
- **C** 沿调用链传播，让各 span 共享同一 trace id
- **D** 请求离开发起客户端后就丢弃

<details>
<summary>查看答案与解析</summary>

**答案**　C

traceparent 等 W3C Trace Context 字段应沿完整调用链传播，让宿主、客户端、服务端和上游系统的 span 共享 trace id，便于关联观测。

</details>

## 24. 审计日志需要证明早先记录事后没有被篡改。哪种技术可以提供这种篡改证据？

- **A** 加密日志，只允许管理员打开文件
- **B** 每天轮转日志并删除旧副本
- **C** 把所有记录无结构地存进纯文本文件
- **D** 让每条记录的校验和链接前一条记录

<details>
<summary>查看答案与解析</summary>

**答案**　D

哈希链让每条审计记录都引用前一条记录的哈希。修改或删除任何早期条目都会破坏链条，因而可被检测；单纯存储、轮转或加密都不提供这一保证。

</details>

## 25. 某项 MCP 规范变更已作为 Final SEP 合并，弃用窗口也已结束。由谁决定是否真正移除该功能？

- **A** Core Maintainers，在最短弃用窗口结束后决定
- **B** 弃用窗口结束后由自动脚本决定
- **C** 任何提交 pull request 的单个贡献者
- **D** AI 应用的最终用户以多数票决定

<details>
<summary>查看答案与解析</summary>

**答案**　A

功能生命周期只规定最短弃用窗口。窗口结束仅表示可以移除，真正何时移除仍由 Core Maintainers 决定。

</details>

## 26. 团队部署了一个以本地 stdio 子进程运行的 MCP 服务端。谁负责为它提供凭据？

- **A** 模型，通过工具调用请求凭据
- **B** 运维方，通过本地环境提供凭据
- **C** 最终用户，在模型聊天窗口输入
- **D** 授权服务器，通过浏览器重定向流程提供

<details>
<summary>查看答案与解析</summary>

**答案**　B

stdio 服务端不应运行 OAuth 浏览器流程，而应从运维方控制的环境读取凭据。这是部署责任，不应让用户、模型或重定向流程传递凭据。

</details>

## 27. 以下哪三项建议正确匹配了使用场景与合适的 MCP 机制？请选择三项。

- **A** 读取某个用户私有数据时，应使用 private cacheScope
- **B** 用户发起的斜杠命令模板应作为工具公开
- **C** 耗时数分钟的构建任务应使用 tasks 扩展
- **D** 无人值守的机器间集成应使用 client credentials 扩展

<details>
<summary>查看答案与解析</summary>

**答案**　A、C、D

长任务适合 tasks 扩展；无人值守的服务间调用适合 client credentials 授权扩展；用户私有读取应使用 private 缓存范围。用户触发的模板属于 prompt，而不是工具。

</details>

## 28. 在 MCP Apps 扩展中，工具的 _meta.ui 对象除了 resourceUri 之外还包含哪个字段？

- **A** csp，列出渲染 iframe 可连接的域
- **B** domain，指定 UI 资源的来源 origin
- **C** visibility，控制模型或 app 是否可以调用它
- **D** permissions，授予 iframe 相机或麦克风权限

<details>
<summary>查看答案与解析</summary>

**答案**　C

工具的 _meta.ui 包含 resourceUri 和 visibility，后者默认同时允许 model 与 app。缺少 model 时宿主不得向 agent 列出工具；缺少 app 时必须拒绝 app 发起的工具调用。

</details>

## 29. 第三方想定义新的 MCP 扩展标识符。按照命名规则，哪种形式正确？

- **A** 任意字符串，因为扩展名称不验证
- **B** 没有域或前缀的单个词
- **C** 任何扩展作者都可使用保留的 io.modelcontextprotocol 前缀
- **D** 作者拥有的反向域名，例如 com.example/my-extension

<details>
<summary>查看答案与解析</summary>

**答案**　D

扩展标识符遵循 _meta 命名规则。官方扩展使用 io.modelcontextprotocol；第三方必须使用自己拥有的反向域名，不能使用保留前缀或无约束单词。

</details>

## 30. SDK 必须通过多少比例的一致性测试，才能达到 Tier 1？

- **A** 完整的 100%，并且需要很早交付功能
- **B** 50%，其余安排到后续版本
- **C** 60%，与所有上架 SDK 的最低门槛一致
- **D** 80%，与 Tier 2 的门槛相同

<details>
<summary>查看答案与解析</summary>

**答案**　A

Tier 1 是最高 SDK 等级：要求通过全部一致性测试、在相关规范发布前交付功能，并满足快速分诊和修复窗口；Tier 2 的门槛才是 80%。

</details>
