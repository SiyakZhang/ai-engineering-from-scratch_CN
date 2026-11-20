# 对话中的交互界面 · 自测

每题先选答案，再展开解析。

## 1. 服务器为什么会选择交互界面，而不是返回普通工具内容？

- **A** 让用户探索或配置一段文字无法妥善表达的内容
- **B** 要求先完成登录步骤，才能运行任何工具调用
- **C** 让模型在每次调用前静默改写工具自身参数
- **D** 用单个二进制块替换对话中的所有文本响应

<details>
<summary>查看答案与解析</summary>

**答案**　A

MCP Apps 面向用户希望直接探索或配置的结果，例如下钻图表或填写表单；普通文本已经足够的内容并不需要它。

</details>

## 2. 在读取任何资源之前，客户端在哪里声明自己支持交互界面？

- **A** 在工具列表之前发送的专用 `ui/register` 调用中
- **B** 请求的 `io.modelcontextprotocol/clientCapabilities.extensions` 中
- **C** HTTP `Accept` header 中，并始终与 `text/event-stream` 并列
- **D** 双方在任何请求前完成的一次性 `initialize` 握手中

<details>
<summary>查看答案与解析</summary>

**答案**　B

扩展支持逐请求声明在 clientCapabilities.extensions 中，遵循 2026-07-28 协议对每项能力采用的无状态模式；不存在握手或一次性注册调用。

</details>

## 3. 工具定义带有 `_meta.ui.resourceUri`。host 应如何处理这个字段？

- **A** 把它视为随 host 应用打包的本地模板路径
- **B** 把它存为工具下一次 `structuredContent` 结果的缓存键
- **C** 通过普通 `resources/read` 取得它所指向的 `ui://` 资源
- **D** 在对话之外的新浏览器标签页中打开地址

<details>
<summary>查看答案与解析</summary>

**答案**　C

该字段指向 ui:// 资源，host 与解析其他 MCP 资源一样通过 resources/read 解析它，而不是使用特殊读取方法。

</details>

## 4. host 取得一个 `ui://` 资源，返回的 `mimeType` 是普通 `text/html`。host 应得出什么结论？

- **A** 资源已经是有效应用，因为它使用了 `ui://` scheme
- **B** 只要 `_meta.ui.csp` 中的域名都可信，资源就是有效应用
- **C** 资源有效，因为普通 `text/html` 是安全的默认类型
- **D** 资源不是有效应用；它缺少必需的 profile 参数

<details>
<summary>查看答案与解析</summary>

**答案**　D

只有 text/html;profile=mcp-app 才会把取得的资源标记为可渲染应用；普通 text/html 只是普通 HTML 文档，无论 scheme 如何，host 都不应把它当作应用。

</details>

## 5. 一个从未声明交互界面扩展的 host 仍调用了支持 UI 的工具。接下来会发生什么？

- **A** 工具仍返回普通结果，其中的文本内容保持可用
- **B** 服务器会静默升级请求，视为已经声明扩展
- **C** 调用立即以未知方法错误 `-32601` 失败
- **D** host 收到要求添加扩展的 `input_required` 结果

<details>
<summary>查看答案与解析</summary>

**答案**　A

支持 UI 的工具仍要为从未声明扩展的 host 保留有意义的文本结果。不支持的一方直接回退到核心行为，而不是让请求失败。

</details>

## 6. 交互界面为什么在沙箱 iframe 中渲染，而不是直接嵌入页面？

- **A** 让应用可以自由访问 host 页面的 cookie 和 local storage
- **B** 让应用与 host 隔离，同时要求特权操作先获得同意
- **C** 让模型可以在 host 上下文中执行应用自己的 JavaScript
- **D** 让服务器可以完全不返回任何文本内容

<details>
<summary>查看答案与解析</summary>

**答案**　B

沙箱会阻止应用直接访问 host 页面的 cookie、存储或 DOM，使 host 无需逐行审计也能渲染服务器应用；所有特权操作仍须通过带同意门禁的桥接。

</details>


[返回本课](docs/zh.md)
