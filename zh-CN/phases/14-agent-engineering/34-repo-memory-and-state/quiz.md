# 仓库记忆与持久状态 · 自测

每题先选答案，再展开解析。

## 1. 决定一条信息是否属于 repo 记忆的持久性测试是什么？

- **A** 它在三个月后的一次 CI 重跑中是否仍有用；有用就进 repo，没用就当遥测（telemetry）
- **B** 它是否是 JSON
- **C** 用户是否把它标记为重要
- **D** 它是否能装进 4 kB

<details>
<summary>查看答案与解析</summary>

**答案**　A

repo 记忆用于持久的、三个月后仍有用的状态；瞬时数据是遥测。

</details>

## 2. 哪个 schema 字段携带 agent 的契约版本？

- **A** build_hash
- **B** model_id
- **C** session_uuid
- **D** schema_version

<details>
<summary>查看答案与解析</summary>

**答案**　D

schema_version 是整数契约；管理器拒绝从未知版本加载。

</details>

## 3. 原子写入（atomic write）如何工作？

- **A** 带 CRC 的仅追加
- **B** 在同一目录用 tempfile.mkstemp，写入，fsync，再 os.replace（原子重命名）覆盖目标
- **C** 加密并覆盖
- **D** 对目标先 truncate 再写入

<details>
<summary>查看答案与解析</summary>

**答案**　B

POSIX 和 Windows 上的原子重命名正是防止部分写入损坏的手段。

</details>

## 4. 为什么非幂等的工具调用需要幂等键（idempotency key）？

- **A** 为了缩短输出
- **B** 为了去重日志
- **C** 如果 agent 在一次工具调用之后、检查点结果之前崩溃，能安全重试；执行前先记录调用 ID，重试时跳过该调用
- **D** 为了计费

<details>
<summary>查看答案与解析</summary>

**答案**　C

pending_calls.jsonl 携带调用 ID；恢复时检查并跳过已执行的工作。

</details>

## 5. 大产物（CSV、长转录、生成的文件）相对于状态应放在哪里？

- **A** 在环境变量里
- **B** 内联在 agent_state.json 里
- **C** 拼接进一个巨大的日志里
- **D** 作为单独的文件（或对象存储），只在状态里保留路径，使检查点保持小而快

<details>
<summary>查看答案与解析</summary>

**答案**　D

单独的产物独立于状态增长；检查点读写保持廉价。

</details>

## 6. 「事件溯源用于审计 + 快照用于恢复」给你带来什么？

- **A** 更快的推理
- **B** 更低的磁盘占用
- **C** 通过先读快照再重放其后的事件来逐字重放 agent 决策；与 Postgres WAL 形态相同
- **D** 原生语音支持

<details>
<summary>查看答案与解析</summary>

**答案**　C

每次变更追加到 state.events.jsonl；定期快照到 state.json；重放快照时间戳之后的事件。

</details>

## 7. 本课说当 schema_version 不匹配时会发生什么？

- **A** agent 重试
- **B** 管理器拒绝加载，直到 tools/migrate_state.py 中的迁移脚本运行
- **C** 管理器静默升级
- **D** 状态被删除

<details>
<summary>查看答案与解析</summary>

**答案**　B

做 schema 迁移或拒绝加载；绝不静默升级。

</details>


[返回本课](docs/zh.md)
