# 多会话交接 · 自测

每题先选答案，再展开解析。

## 1. 交接包（handoff packet）中承重的字段是哪一个？

- **A** next_action（没有它，这份文档就是状态报告，而不是交接）
- **B** verdict_pointer
- **C** commands_run
- **D** summary

<details>
<summary>查看答案与解析</summary>

**答案**　A

除了 next_action 什么都有的交接，是一份状态报告；下一个具体步骤才是让下一个会话高效的东西。

</details>

## 2. 为什么交接是被生成的，而不是被手写的？

- **A** 生成器加密更好
- **B** Apache 2.0 要求它
- **C** 生成器更快
- **D** 手写的交接在难熬的一天会被跳过；生成器读取工作台产物并发出交接包，于是 agent 只需把工作台留在生成器能总结的状态

<details>
<summary>查看答案与解析</summary>

**答案**　D

自动化弥合了意图与一致性之间的鸿沟。

</details>

## 3. 交接包以哪两种形式发布？

- **A** YAML 和 TOML
- **B** handoff.md（人类可读）和 handoff.json（机器可读，二者来自同一来源产物；分歧时 JSON 胜出）
- **C** 邮件和 Slack
- **D** PDF 和 PNG

<details>
<summary>查看答案与解析</summary>

**答案**　B

markdown 给人，JSON 给下一个 agent；二者都来自同一个生成器。

</details>

## 4. 本课如何区分压实（compaction）和交接（handoff）？

- **A** 压实收费，交接免费
- **B** 交接需要 GPU
- **C** 它们是一回事
- **D** 压实延长一个会话；交接干净地结束一个并在全新上下文中开始下一个。交接包就是让这个转换变廉价的东西

<details>
<summary>查看答案与解析</summary>

**答案**　D

Hermes Issue 20372 的框架：在原地压缩降低质量之前写一份紧凑的交接，然后在全新会话中恢复。

</details>

## 5. 本课关于何时收尾一个会话有何建议？

- **A** 只在合并之后
- **B** 在 50-75% 上下文预算之前、趁上下文完好时；在压缩产物污染状态之前写很便宜
- **C** 只在午夜
- **D** 在 100% 上下文时，然后慌乱

<details>
<summary>查看答案与解析</summary>

**答案**　B

提早收尾能让生成器的输入保持干净。

</details>

## 6. 本课建议在交接包中把反馈日志裁剪成什么？

- **A** 只取前 K 条
- **B** 只取最近一条
- **C** 最后 K 条加上每一条非零退出的记录，使交接包保持小而失败历史得以存活
- **D** 随机 N 条

<details>
<summary>查看答案与解析</summary>

**答案**　C

非对称裁剪：失败必须存活；尾部的琐碎内容留着也便宜。

</details>

## 7. 哪些元数据让跨多 agent 会话的协调得以运转？

- **A** 绝密加密
- **B** branch、last_known_good_commit 和 status（active | superseded | archived）；每个分支和主题只有一个 active 交接
- **C** 一个共享的 Slack 频道
- **D** 一个中央队列

<details>
<summary>查看答案与解析</summary>

**答案**　B

陈旧的交接是多 agent 的主要失败；status + branch + LKG 让 active 集合保持很小。

</details>


[返回本课](docs/zh.md)
