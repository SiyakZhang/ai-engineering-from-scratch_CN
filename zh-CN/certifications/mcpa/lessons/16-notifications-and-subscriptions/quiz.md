# 订阅流：通知、进度与取消 · 自测

每题先选答案，再展开解析。

## 1. 服务器的 tool 列表刚刚发生变化。为什么不能把该变化作为普通请求的回复来报告？

- **A** 必须先通过新的 discovery 调用重新协商 tool capability
- **B** 客户端必须再次轮询 tool 列表，变化才会可见
- **C** 回复会关闭所响应的请求，之后没有通道承载该变化
- **D** JSON-RPC 完全不允许服务器发送未经请求的消息

<details>
<summary>查看答案与解析</summary>

**答案**　C

JSON-RPC 回复绑定到它所关闭的单个请求，因此当没有请求进行时，持续变化需要通过流上的通知传递。

</details>

## 2. 客户端用全新请求 id 打开 subscriptions/listen 流。该流上的第一条消息必须是什么？

- **A** resources/subscribe，确认资源监视已成功注册
- **B** 空的 tools/list 结果，仅用于确认新流已经打开
- **C** notifications/resources/updated，报告服务器最先产生的内容
- **D** notifications/subscriptions/acknowledged，并以 listen 请求 id 作为 subscriptionId

<details>
<summary>查看答案与解析</summary>

**答案**　D

服务器必须首先发送确认消息；在该流出现任何其他通知之前，它会在 _meta 中携带 listen 请求 id 作为 subscription id。

</details>

## 3. tools/call 请求包含 progressToken，服务器在运行期间报告进度。这些 progress 通知会出现在哪里？

- **A** 只出现在同一请求的响应通道上，绝不出现在 listen 流中
- **B** 出现在由 logLevel 设置门控的独立 logging 通道上
- **C** 出现在该客户端最近确认的任意订阅流上
- **D** 出现在 subscriptions/listen 流上，并携带相同 subscription id

<details>
<summary>查看答案与解析</summary>

**答案**　A

Progress 通知属于携带 progressToken 的请求，只通过该响应通道传递；它们绝不携带 subscription id，也不会出现在 listen 流中。

</details>

## 4. stdio 上的客户端决定取消仍在运行的 tools/call 请求。它应怎么做？

- **A** 关闭子进程 stdin，让服务器把管道关闭视为取消
- **B** 发送 notifications/cancelled 通知，并指出准确的 request id
- **C** 使用同一 id 发送新的 tools/call，arguments 为空对象
- **D** 继续等待，因为 stdio 请求一旦开始就无法取消

<details>
<summary>查看答案与解析</summary>

**答案**　B

stdio 没有可关闭的每请求流，因此客户端通过发送 notifications/cancelled，并提供不再需要响应的请求 id 来取消。

</details>

## 5. 服务器在计划关闭期间主动结束订阅，而不是连接突然断开。关闭流前应发送什么？

- **A** 由服务器发起、指向客户端的全新 subscriptions/listen 请求
- **B** 列出订阅所监视每项资源的 notifications/cancelled 消息
- **C** 针对原 listen 请求返回 complete 结果，并携带 subscription id
- **D** 什么也不发送，因为通知驱动的流不会有关闭消息

<details>
<summary>查看答案与解析</summary>

**答案**　C

服务器主动结束订阅时，应针对原 listen 请求返回携带 subscription id 的 complete 结果，让客户端区分干净结束与 transport 突然中断。

</details>

## 6. stdio 服务器进程崩溃后重启。客户端必须怎么做，才能继续接收此前订阅的通知？

- **A** 发送 Last-Event-ID header，让流从中断处继续
- **B** 重新连接并等待，因为新进程会自动恢复之前的所有订阅
- **C** 无需操作，因为订阅状态会在磁盘上跨重启保存
- **D** 用新 id 重新发送 subscriptions/listen，因为新进程不记得任何内容

<details>
<summary>查看答案与解析</summary>

**答案**　D

重启后的服务器不会保留崩溃前的订阅状态，客户端必须重新发送 subscriptions/listen 并重建每条流，这与其他请求遵循相同的无状态原则。

</details>


[返回本课](docs/zh.md)
