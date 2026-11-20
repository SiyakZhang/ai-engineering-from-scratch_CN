# 运行时反馈循环 · 自测

每题先选答案，再展开解析。

## 1. 反馈运行器（feedback runner）迫使 agent 做什么？

- **A** 对事实做反应：在每条命令上把结构化的 stdout/stderr/exit/duration 记录捕获进循环
- **B** 对想象中的输出做反应
- **C** 用不同的模型
- **D** 跳过验证

<details>
<summary>查看答案与解析</summary>

**答案**　A

运行器弥合了「测试通过了」（想象）与「测试确实运行了并以零退出」（记录在案）之间的鸿沟。

</details>

## 2. 反馈与遥测（telemetry）有何不同？

- **A** 它们是一回事
- **B** 反馈用于本次运行的下一轮；遥测用于运维人员跨时间审查多次运行（不同文件、不同保留期）
- **C** 遥测收费
- **D** 遥测用 OTel；反馈用 GraphQL

<details>
<summary>查看答案与解析</summary>

**答案**　B

两者共享字段但存在不同文件、保留期不同；反馈是运行内的，遥测是跨运行的。

</details>

## 3. 哪个字段必须出现在每条反馈记录中？

- **A** model_id
- **B** prompt_cache_token
- **C** exit_code（且 exit 为 null 时必须拒绝推进循环）
- **D** embedding_vector

<details>
<summary>查看答案与解析</summary>

**答案**　C

exit_code 是无歧义的成功信号；null 退出意味着没有进展。

</details>

## 4. 运行器如何截断大输出？

- **A** 只取前 10 行
- **B** 确定性的头 + 尾，加一个「截断了 N 行」标记，使同样的输出总产生同样的记录
- **C** 随机采样
- **D** 用 gzip 压缩

<details>
<summary>查看答案与解析</summary>

**答案**　B

确定性截断让记录可重放，同时限定 token 成本；尾部携带失败摘要。

</details>

## 5. 为什么在写入时脱敏（redact）而非读取时？

- **A** 压缩
- **B** 磁盘上的文件才是攻击者能触及的；只在读取时脱敏会把秘密留在 JSONL 文件里
- **C** 读取时脱敏会破坏 JSON
- **D** 它更快

<details>
<summary>查看答案与解析</summary>

**答案**　B

在追加前脱敏匹配 Bearer、password=、api_key=、AKIA...、xox[baprs]- 的行；并每季度审计这些模式。

</details>

## 6. parent_command_id 给工作台带来什么？

- **A** 更低的内存
- **B** 更快的文件 I/O
- **C** 重试链接到它们的父尝试，使审查者和审计能看到失败链；没有它，重试看起来像独立的成功
- **D** 更便宜的推理

<details>
<summary>查看答案与解析</summary>

**答案**　C

父级链接让重试链对审查者（第 39 课）和验证门可见。

</details>

## 7. 为什么把 feedback_record.jsonl 限制在 1 MB 并带轮转？

- **A** 磁盘太慢
- **B** agent 只读当前文件；轮转把运行时成本限定住，而 CI 产物捕获完整集合
- **C** 提供商按字节收费
- **D** JSON 处理不了更大的文件

<details>
<summary>查看答案与解析</summary>

**答案**　B

有界的当前文件 + 轮转的历史是 logrotate 用的同一模式；在热循环里成本可预测。

</details>


[返回本课](docs/zh.md)
