# Agent 初始化脚本 · 自测

每题先选答案，再展开解析。

## 1. 一个 init 脚本消除了什么？

- **A** 推理带来的延迟
- **B** 认证 token
- **C** 提供商限流
- **D** 每会话的设置税：探测运行时、列出 repo、在每个新会话重复同样的检查

<details>
<summary>查看答案与解析</summary>

**答案**　D

脚本只交一次税，并把答案写进 agent 会读取的 init_report.json。

</details>

## 2. init 脚本的失败模式契约是什么？

- **A** 总是成功
- **B** 大声失败、快速失败、在一处失败；当工作台坏掉时拒绝启动
- **C** 软失败并继续
- **D** 永远重试

<details>
<summary>查看答案与解析</summary>

**答案**　B

整个要点就是当工作台坏掉时拒绝启动；静默回退会破坏这个目的。

</details>

## 3. 下列哪一个不是本课列出的探测项之一？

- **A** 测试命令可解析性
- **B** 逐 token 采样温度
- **C** 运行时版本
- **D** 依赖可用性

<details>
<summary>查看答案与解析</summary>

**答案**　B

探测项包括运行时版本、依赖、测试命令、路径、环境变量、状态新鲜度、最近已知良好提交（LKG）。

</details>

## 4. 为什么本课说 init 必须是幂等的？

- **A** 这是 JSON Schema 要求的
- **B** 幂等性省钱
- **C** 运行两次除了新时间戳外应是无操作，这样它就能被接入 CI、hook 或一个任务前的 slash 命令
- **D** 它满足 SOC 2

<details>
<summary>查看答案与解析</summary>

**答案**　C

幂等性让 init 能安全地从多个入口（hook、CI、slash 命令）调用。

</details>

## 5. 什么是最近已知良好提交锚定（last-known-good commit anchoring）？

- **A** 团队负责人最近的提交
- **B** repo 中最早的提交
- **C** HEAD 与 main 的合并基
- **D** 把当前提交与一个 LKG 文件对照探测；若 diff 在未经人工批准下超过预算就拒绝启动

<details>
<summary>查看答案与解析</summary>

**答案**　D

Cloudflare 的 AI Code Review 用 LKG 来界定审查者范围，防止漂移跨会话累积。

</details>

## 6. 带 TTL 的锁文件模式做什么？

- **A** 禁用 CI
- **B** 在一次成功探测通过后写入 prereqs.lock；后续运行在 24 小时内信任该锁，若清单哈希匹配就跳过昂贵的探测
- **C** 把 repo 锁住禁止编辑
- **D** 把所有写入封锁 24 小时

<details>
<summary>查看答案与解析</summary>

**答案**　B

与 Docker 层缓存形态相同：幂等探测 + 内容哈希 = 跳过。

</details>

## 7. 什么绝不应出现在 init 的热路径中？

- **A** 读取环境变量
- **B** 网络调用、LLM 调用、外部许可证检查；探测是三秒内的确定性管道
- **C** 本地文件系统读取
- **D** 读取锁文件

<details>
<summary>查看答案与解析</summary>

**答案**　B

一个调用 LLM 的探测是工作流，不是探测；让 init 保持确定性。

</details>


[返回本课](docs/zh.md)
