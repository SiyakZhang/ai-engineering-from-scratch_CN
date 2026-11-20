# 缓存新鲜度与基于 Cursor 的分页 · 自测

每题先选答案，再展开解析。

## 1. 完整的 resources/read 或 resources/list 结果始终携带哪两个字段？

- **A** cursor 值，以及前一次调用回显的 requestState
- **B** Mcp-Session-Id header 值，以及 Last-Event-ID stream 标记
- **C** protocolVersion 字符串，以及 _meta 下的 clientCapabilities 对象
- **D** 整数 ttlMs，以及取值为 public 或 private 的 cacheScope

<details>
<summary>查看答案与解析</summary>

**答案**　D

六种可缓存操作的完整结果都必须携带大于等于零的整数 ttlMs，以及取值为 public 或 private 的 cacheScope；这是 SEP-2549 为 2026-07-28 缓存规则添加的字段。

</details>

## 2. 调用方 private note 的 resources/read 结果将 cacheScope 设为 private。该字段实际控制什么？

- **A** 缓存字节只能由与之前相同的授权上下文复用
- **B** 客户端必须先加密缓存字节才能写入磁盘
- **C** 任何复用 cache 的调用方都会获得该 note 的完整读取权限
- **D** 服务器未来调用无需再检查调用方访问权限

<details>
<summary>查看答案与解析</summary>

**答案**　A

cacheScope 只告诉 cache 谁可以存储和回放字节，绝不能替代服务器对每个请求执行的逐 primitive 访问控制。

</details>

## 3. resources/list 响应的 nextCursor 是空字符串。合规客户端下一步应该怎么做？

- **A** 报告 -32602，因为空 cursor 在线上永远无效
- **B** 把相同的空 cursor 值发回，因为它是有效列表位置
- **C** 把空字符串视为列表末尾并停止分页
- **D** 省略 cursor 字段，从头重新开始分页

<details>
<summary>查看答案与解析</summary>

**答案**　B

空字符串是合法的不透明 cursor；只有缺少 nextCursor 才表示列表结束。把空字符串当作结束会让客户端提前一页停止分页。

</details>

## 4. 客户端在回答 input_required elicitation 后重试 resources/read 请求。按 2026-07-28 缓存规则，随后返回的完成结果应如何处理？

- **A** 仅当服务器还在能力中将 listChanged 设为 true 时缓存
- **B** 无论资源真实 scope 如何，都以 public cacheScope 缓存
- **C** 绝不缓存，因为它依赖 cache key 之外的 inputResponses
- **D** 使用原请求 id 作为 key 缓存，使重试无需再次执行

<details>
<summary>查看答案与解析</summary>

**答案**　C

MRTR 重试得到的结果携带未纳入 cache key 的 inputResponses，因此规范要求客户端不要缓存，即使结果本身仍报告 ttlMs 和 cacheScope。

</details>

## 5. 客户端缓存的 tools/list 条目还剩两分钟 ttlMs 时，listen stream 收到 notifications/tools/list_changed。客户端应怎么做？

- **A** 延长 TTL 窗口，因为 notification 证明服务器仍可访问
- **B** 等待 TTL 自然到期后再将条目标记为过期
- **C** 忽略 notification，因为缓存条目仍在 TTL 窗口内
- **D** 立即将条目标记为过期，并在下次需要时重新获取

<details>
<summary>查看答案与解析</summary>

**答案**　D

TTL 与 push notification 相互补充：相关 list_changed notification 会立即使缓存响应失效，无视 TTL 时钟剩余时间。

</details>

## 6. 除了让客户端自身 cache 和分页更可预测，为什么规范还建议 tools/list 以确定顺序返回条目？

- **A** 稳定前缀能提高上游 provider 自身 prompt cache 的命中率
- **B** 稳定顺序使客户端在重复 tools/list 调用时可省略 clientCapabilities
- **C** 只有顺序稳定后，服务器才可声明 listChanged 能力
- **D** 只有稳定顺序才能把 cursor 当作不透明值

<details>
<summary>查看答案与解析</summary>

**答案**　A

工具目录每次序列化结果相同，上游 LLM provider 的 prompt caching 就能复用缓存前缀，减少重复处理；这是独立于 MCP ttlMs 机制的真实延迟和成本收益。

</details>


[返回本课](docs/zh.md)
