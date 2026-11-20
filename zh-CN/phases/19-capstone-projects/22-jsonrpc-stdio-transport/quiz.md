# 基于换行分隔 stdio 的 JSON-RPC 2.0 · 自测

每题先选答案，再展开解析。

## 1. 在线路上，JSON-RPC 的 notification 和 request 有什么区别？

- **A** Notification 省略了 id 字段；服务端不得对其响应
- **B** jsonrpc 版本号字段不同
- **C** Notification 被包裹在数组里
- **D** Notification 使用不同的 method 命名空间

<details>
<summary>查看答案与解析</summary>

**答案**　A

没有 id 是唯一标记。服务端不响应，因为没有 id 可以用来关联。

</details>

## 2. 为什么换行分隔 JSON 足以作为 stdio 的帧定界方案？

- **A** 因为 UTF-8 中没有换行字节
- **B** 因为管道保证换行符的原子性
- **C** 因为 JSON 不允许字符串内出现未转义的换行符，所以每个对象可以占一行
- **D** 因为规范强制要求这样

<details>
<summary>查看答案与解析</summary>

**答案**　C

json.dumps 每个对象输出一行；字符串内的换行符会被转义。这使得 \n 成为安全的记录分隔符。

</details>

## 3. 当 JSON 解析失败时，传输层返回哪个错误码？

- **A** -32600
- **B** -32700
- **C** -32601
- **D** -32603

<details>
<summary>查看答案与解析</summary>

**答案**　B

-32700 是 Parse error。因为无法提取到 id，响应中的 id 为 null。

</details>

## 4. 如果 handler 抛出一个普通的 ValueError，传输层返回什么？

- **A** Invalid params (-32602)
- **B** 不返回任何东西；连接断开
- **C** Internal error (-32603)，并在 data 中包含异常类名
- **D** Method not found (-32601)

<details>
<summary>查看答案与解析</summary>

**答案**　C

未映射的异常统一返回 -32603。data.exception 保留了异常的类名供客户端参考。

</details>

## 5. 当一个 batch 中只包含 notification 时，服务端返回什么？

- **A** 一个单独的 null 响应
- **B** 一个空数组
- **C** 每个 notification 对应一个 null
- **D** 什么也不返回——不写任何字节

<details>
<summary>查看答案与解析</summary>

**答案**　D

规范规定：如果批量请求中的每一条都是 notification，服务端保持沉默。

</details>

## 6. 会话中间收到一行破损的 JSON，之后的行会怎样？

- **A** 传输层写一个 -32700 响应，然后继续读取下一行作为新的输入
- **B** 后续行被缓冲，直到破损行被重试
- **C** 传输层关闭流
- **D** 后续行全部被 -32600 拒绝

<details>
<summary>查看答案与解析</summary>

**答案**　A

帧定界层不能污染整个流。一次解析错误只产生一个错误响应，循环继续运行。

</details>

## 7. 为什么传输层不直接查询工具注册中心？

- **A** 因为注册中心是异步的
- **B** 因为注册中心存有机密信息
- **C** 为了让传输层只负责 JSON-RPC 协议；由 handler 来连接传输层和注册中心
- **D** 因为传输层运行在不同的进程中

<details>
<summary>查看答案与解析</summary>

**答案**　C

传输层只管线路协议。Dispatcher（下一课）才是传输层、注册中心和超时逻辑汇合的地方。

</details>


[返回本课](docs/zh.md)
