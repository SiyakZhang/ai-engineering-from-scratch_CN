# 函数调用分发器 · 自测

每题先选答案，再展开解析。

## 1. 为什么对非幂等工具，超时后默认不重试？

- **A** 因为分发器无法度量非幂等调用
- **B** 因为非幂等 handler 执行更快
- **C** 因为工具可能已经部分提交了；重试会导致副作用重复
- **D** 因为幂等 key 的生成很慢

<details>
<summary>查看答案与解析</summary>

**答案**　C

一次在 4.9 秒超时的 db.write 被重试后可能产生第二次写入。除非 handler 告知该调用可以安全重复，否则分发器会拒绝重试。

</details>

## 2. 幂等 key 去重保护的是什么场景？

- **A** 网络慢
- **B** Schema 校验错误
- **C** 重试触发时原始调用仍在进行中
- **D** 进程重启

<details>
<summary>查看答案与解析</summary>

**答案**　C

没有去重的话，5 秒处触发的重试会和仍在等待的原始调用形成竞争。缓存把两者合并为一次 handler 调用。

</details>

## 3. 在这个分发器中，哪些错误类型可以被重试？

- **A** internal 和 budget_exceeded
- **B** timeout（仅幂等时）和 transient
- **C** 全部都可以
- **D** schema 和 not_found

<details>
<summary>查看答案与解析</summary>

**答案**　B

schema 和 not_found 是确定性错误。internal 掩盖了未知的 handler bug。budget_exceeded 是一次 yield。只有幂等调用的 timeout 和显式的 TransientError 才会重试。

</details>

## 4. _run_with_retries 外面的信号量保护的是什么？

- **A** 重试计数器
- **B** validator
- **C** 后端不被 gather() 扇出的大量并发调用压垮
- **D** handler 不和自己冲突

<details>
<summary>查看答案与解析</summary>

**答案**　C

四十个调用的 gather 如果没有限制就会同时打开四十个并发分发。信号量限制了并发波峰。

</details>

## 5. 为什么幂等 key 由调用方派生，而不是由分发器生成？

- **A** 因为 Python 的 hash 不稳定
- **B** 因为缓存不能存字符串
- **C** 因为仅凭参数派生会导致两个语义不同但参数相同的调用发生碰撞
- **D** 因为注册中心拿不到 key

<details>
<summary>查看答案与解析</summary>

**答案**　C

调用方知道 step id、planner 意图、用户身份。仅靠参数无法提供足够的上下文来安全去重。

</details>

## 6. 分发时 schema 校验失败会映射到哪个 JSON-RPC 错误码？

- **A** -32601
- **B** -32603
- **C** -32700
- **D** -32602

<details>
<summary>查看答案与解析</summary>

**答案**　D

-32602 Invalid params。分发器在任何 handler 运行之前就返回这个错误。

</details>

## 7. 对幂等工具连续超时直到 max_attempts 用尽后，返回什么？

- **A** DispatchError，kind=timeout，attempts==max_attempts
- **B** DispatchOk 但没有结果
- **C** 抛出异常
- **D** DispatchError，kind=internal

<details>
<summary>查看答案与解析</summary>

**答案**　A

分发器返回类型化的错误信封。kind 反映最后一次失败模式，attempts 反映总共尝试了多少次。

</details>


[返回本课](docs/zh.md)
