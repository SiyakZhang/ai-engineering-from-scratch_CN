# OpenTelemetry GenAI 语义约定 · 自测

每题先选答案，再展开解析。

## 1. 在 GenAI 约定中，哪个 span 名称代表一次 agent 运行？

- **A** invoke_agent（可选地以 gen_ai.agent.name 作后缀）
- **B** run_chain
- **C** agent_loop
- **D** agent.start

<details>
<summary>查看答案与解析</summary>

**答案**　A

invoke_agent 是规范名称；设置了 agent 名称属性时，它会出现在 span 名称中。

</details>

## 2. GenAI SIG 定义了哪三种 span 类别？

- **A** 模型/客户端、agent、工具
- **B** Read、write、exec
- **C** 延迟、错误、吞吐量
- **D** Frontend、backend、db

<details>
<summary>查看答案与解析</summary>

**答案**　A

模型/客户端（LLM 调用）、agent（创建/调用）、工具（每次调用）是这三类。

</details>

## 3. invoke_agent span 什么时候用 kind CLIENT 而非 INTERNAL？

- **A** 总是 INTERNAL
- **B** 总是 CLIENT
- **C** 只有 HTTPS 才用 CLIENT
- **D** 远程 agent 服务（OpenAI Assistants、Bedrock Agents）用 CLIENT；进程内框架（LangChain、CrewAI、本地 ReAct）用 INTERNAL

<details>
<summary>查看答案与解析</summary>

**答案**　D

远程 agent 调用是 CLIENT；进程内 agent 运行是 INTERNAL。

</details>

## 4. 内容捕获（输入和输出）的默认规则是什么？

- **A** 只捕获输出，绝不捕获输入
- **B** 只在错误时捕获
- **C** 默认捕获一切
- **D** instrumentation 默认不应捕获；捕获通过 gen_ai.* 属性显式选择开启

<details>
<summary>查看答案与解析</summary>

**答案**　D

默认关闭的内容捕获保护 PII 和秘密；选择开启是显式的。

</details>

## 5. 哪个属性标识一次检索所查询的语料或存储？

- **A** gen_ai.provider.name
- **B** gen_ai.agent.name
- **C** gen_ai.data_source.id
- **D** gen_ai.request.model

<details>
<summary>查看答案与解析</summary>

**答案**　C

gen_ai.data_source.id 标注检索命中的 RAG 语料或存储。

</details>

## 6. 本课建议在生产中如何存储 prompt 内容？

- **A** 在每个 span 上以明文捕获完整 prompt
- **B** 在 span 属性中加密 prompt
- **C** 把内容外部存储（S3、日志存储），转而在 span 上记录引用 ID
- **D** 绝不存储任何内容

<details>
<summary>查看答案与解析</summary>

**答案**　C

外部存储加指针 ID 避免 PII 泄露进运维可读的 trace 中。

</details>

## 7. 如何选择开启 GenAI 约定的实验性稳定预览？

- **A** 从源码重建 SDK
- **B** 为许可证付费
- **C** 设置 OTEL_SEMCONV_STABILITY_OPT_IN=gen_ai_latest_experimental
- **D** 编辑 OTel collector 配置

<details>
<summary>查看答案与解析</summary>

**答案**　C

这个环境变量固定实验性约定，使属性不会被悄悄改名。

</details>


[返回本课](docs/zh.md)
