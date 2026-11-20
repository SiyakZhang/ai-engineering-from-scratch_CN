# Messages API 是一台状态机 · 自测

每题先选答案，再展开解析。

## 1. 应用连续调用 Messages API 时，谁负责维护对话历史？

- **A** 供应商，它会自动把先前 Messages 请求带入下一次调用
- **B** Prompt 缓存，前缀匹配时会恢复被省略的历史
- **C** 最新工具，它会同时返回结果与完整对话状态
- **D** 客户端应用，它负责选择、存储并重新发送必需消息

<details>
<summary>查看答案与解析</summary>

**答案**　D

Messages API 是无状态的。客户端选择、存储并重新发送每次转换所需的消息历史。

</details>

## 2. 下一次请求中，user 角色的 tool_result 前必须出现什么？

- **A** 保留下来的、包含匹配 tool_use 块的 assistant 消息
- **B** 一条只含 tool_result ID 和输出、不含先前内容块的 user 消息
- **C** 先前的 assistant 文本块，但执行后移除了 tool_use 块
- **D** 一条对所请求工具调用的新 assistant 摘要

<details>
<summary>查看答案与解析</summary>

**答案**　A

Assistant tool_use 块建立了请求。后续 tool_result 必须引用其 ID，并保持协议顺序。

</details>

## 3. 响应看似完整，但 stop_reason 是 max_tokens。怎样理解最安全？

- **A** 只要最终内容块能解析且结束于完整句子，响应就是完整的
- **B** 输出可能不完整，需要明确恢复或升级
- **C** 客户端应只重发最后一段，并要求模型从那里继续
- **D** 把标点视为响应主动结束的证据

<details>
<summary>查看答案与解析</summary>

**答案**　B

控制元数据优先于视觉印象。max_tokens 表示生成达到配置上限，因此不能假设输出完整。

</details>

## 4. 有受支持的 SDK，需要处理 50,000 项可以稍后完成的独立分类。哪种访问模式最合适？

- **A** 原始 REST 加递归调度每条记录的工具循环
- **B** 用一个同步 SDK 请求在一次对话中包含完整集合
- **C** 使用稳定自定义 ID 和异步对账的 SDK Message Batches
- **D** 使用 SDK 流式传输，在每项分类的第一个文本 delta 到达时提交结果

<details>
<summary>查看答案与解析</summary>

**答案**　C

受支持 SDK 减少了 transport 样板；Message Batches 适合结果可以稍后到达的独立工作。客户端选择和完成模式是两项独立决策。

</details>

## 5. 为什么流消费者应等到终止事件后再提交结构化结果？

- **A** 内容块停止能证明整条消息和 transport 都已成功完成
- **B** 不含工具的流出现第一个完整 JSON 对象后即可提交
- **C** 如果缺失的可选字段有 schema 默认值，就可以提交有效前缀
- **D** 部分 delta 可能不完整，连接也可能继续失败

<details>
<summary>查看答案与解析</summary>

**答案**　D

部分流只是临时结果。客户端必须确认消息已完成，才能解析最终合约或触发下游状态变化。

</details>

## 6. 用户提供了一个存在于应用 workspace 中的 Files API file_id。把它放进 Message 前必须做什么？

- **A** 把它绑定到已认证租户，以及带保留政策的应用自有资产记录
- **B** 直接获取，因为存在于 workspace 就能证明当前租户拥有它
- **C** 把它复制进 system prompt，让 Claude 判断该引用是否获授权
- **D** 转换成内联 base64，因为内联内容没有数据边界要求

<details>
<summary>查看答案与解析</summary>

**答案**　A

Workspace 范围大于租户授权范围。应用必须把资产加入 allowlist、绑定所有权和敏感度，并独立于不透明 ID 执行删除。

</details>


[返回本课](docs/zh.md)
