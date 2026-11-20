# MCP 一致性工程：版本、证据与运维 · 自测

每题先选答案，再展开解析。

## 1. 为什么一次成功的 SDK tools/list 调用不足以证明一致性？

- **A** SDK 无法调用 MCP tools
- **B** 归一化后的值可能隐藏线上字段、版本行为、代理变更和无效响应
- **C** 一次成功调用总会选择遗留时代
- **D** 一致性只适用于 Registry publishers

<details>
<summary>查看答案与解析</summary>

**答案**　B

一致性必须检查原始请求和响应、选定的版本时代、中间层以及 SDK 转换。

</details>

## 2. 现代探测返回 JSON-RPC error -32021。支持回退的 client 应怎么做？

- **A** 忽略 error 并在没有 capabilities 的情况下重试
- **B** 立即为遗留时代发送 initialize
- **C** 将 peer 视为离线
- **D** 保持在现代时代，并修正或报告缺失的 capability 声明

<details>
<summary>查看答案与解析</summary>

**答案**　D

已识别的现代 error 证明现代行为。它是修正证据，而不是降级许可。

</details>

## 3. 现代 client 应如何处理 resultType 为 complete 且带有陌生可加字段的结果？

- **A** 将 resultType 改为 input_required
- **B** 接受已知 result type，并按字段角色保留或有意忽略该可加字段
- **C** 将陌生字段视为遗留握手
- **D** 拒绝包含未知 key 的每个结果

<details>
<summary>查看答案与解析</summary>

**答案**　B

可加字段支持前向兼容性。它们不同于未知的 lifecycle discriminator。

</details>

## 4. 对于没有 id 的 notification，要求的 JSON-RPC 响应是什么？

- **A** 不产生 JSON-RPC 响应
- **B** 带 null content 的 complete result
- **C** id 为 null 的 error
- **D** 一个 server/discover result

<details>
<summary>查看答案与解析</summary>

**答案**　A

Notifications 是单向的。最终 transport serializer 不得输出 JSON-RPC success 或 error。

</details>

## 5. 哪种证据最能证明 proxy 保留了 origin protocol error？

- **A** gateway dashboard 的截图
- **B** 仅 SDK exception class
- **C** proxy process uptime
- **D** 带稳定 digests 的、经脱敏的 ingress、origin 和 egress status 及 body 证据

<details>
<summary>查看答案与解析</summary>

**答案**　D

三边界证据能揭示 status 折叠、body 重写，以及行为改变的精确 hop。

</details>

## 6. 一个 candidate 未通过负向转录记录，且先前版本没有准入或健康度证据。release gate 应怎么做？

- **A** 暂停发布，直至证明合格的 rollback target 或已修正的 candidate
- **B** 选择最新的 Registry version
- **C** 回滚到标记为 latest 的 package
- **D** 因为 golden 转录记录通过而提升

<details>
<summary>查看答案与解析</summary>

**答案**　A

没有精确准入和健康度证据的 rollback 是另一次未经验证的发布，因此安全动作是暂停。

</details>


[返回本课](docs/zh.md)
