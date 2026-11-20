# 生产运行时：Queue、Event、Cron · 自测

每题先选答案，再展开解析。

## 1. 本课列出哪六种运行时形态？

- **A** Read、write、exec、fork、exit、wait
- **B** REST、gRPC、GraphQL、WebSocket、SSE、MQTT
- **C** 请求-响应、流式、持久化执行、基于队列、事件驱动、定时调度
- **D** Map、filter、reduce、fold、scan、group

<details>
<summary>查看答案与解析</summary>

**答案**　C

这是六种运行时形态；先选形态再选框架。

</details>

## 2. 什么时候请求-响应是糟糕的选择？

- **A** 在 REST API 上
- **B** 当任务耗时超过约 30 秒、用户挂断而 worker 堆积时
- **C** 在内部服务上
- **D** 在一个 1 秒的分类上

<details>
<summary>查看答案与解析</summary>

**答案**　B

同步 HTTP 只对短任务可行；长任务需要队列/持久化/事件形态。

</details>

## 3. 持久化执行的核心属性是什么？

- **A** 更低的 token 成本
- **B** 原生语音支持
- **C** 每一步之后对状态做检查点，使运行时在失败时能从上一个成功步骤恢复
- **D** 更快的推理

<details>
<summary>查看答案与解析</summary>

**答案**　C

检查点-恢复是关键差异；LangGraph 是本课的参考。

</details>

## 4. Anthropic 的哪个观察为长程 agent 的基于队列运行时提供了正当理由？

- **A** 任务总在 5 秒内完成
- **B** cron 解决一切
- **C** 计算机使用的公告：每个任务数十到数百步是常态
- **D** 任务必须同步运行

<details>
<summary>查看答案与解析</summary>

**答案**　C

Anthropic 指出每个任务数十到数百步是常态；这种工作负载需要队列或持久化运行时。

</details>

## 5. 本课所说的「可观测性是承重的」是什么意思？

- **A** 没有 OTel GenAI span 和一个 Langfuse/Phoenix/Opik 后端，你无法调试一个在第 40 步失败的多步 agent
- **B** 日志很漂亮
- **C** 磁盘满了
- **D** 提供商为计费而要求它

<details>
<summary>查看答案与解析</summary>

**答案**　A

对多步 agent 而言，可观测性不是可选的；它决定了你是调试还是从头重放。

</details>

## 6. 为什么队列 worker 必须有死信队列（DLQ）？

- **A** DLQ 让任务更快
- **B** 没有 DLQ，失败的任务会静默消失
- **C** DLQ 是加密的
- **D** DLQ 是 AWS 要求的

<details>
<summary>查看答案与解析</summary>

**答案**　B

没有 DLQ 的失败任务会消失；DLQ 是失败任务的停车场。

</details>

## 7. 本课建议把 cron 形态的 agent 与什么配对？

- **A** 持久化执行，使一次失败的夜间运行能在下一个时刻恢复
- **B** GPU 自动扩缩器
- **C** WebRTC
- **D** 流式 SSE

<details>
<summary>查看答案与解析</summary>

**答案**　A

cron + 持久化执行能从失败的定时运行中干净地恢复。

</details>


[返回本课](docs/zh.md)
