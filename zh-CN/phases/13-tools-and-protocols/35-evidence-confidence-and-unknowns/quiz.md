# 二进制分析中的证据、置信度与未知项 · 自测

每题先选答案，再展开解析。

## 1. rea 为每条 Evidence 记录赋予 confidence。schema 允许哪组值？

- **A** observed、derived 或 inferred
- **B** 0.0 到 1.0 的数字
- **C** low、medium、high 或 critical
- **D** pass、fail 或 unknown

<details>
<summary>查看答案与解析</summary>

**答案**　A

confidence 是 src/domain/evidence.ts 中的三值枚举。严重度与完成状态是其他字段，各有取值。

</details>

## 2. 两人在不同机器、不同目录中，对相同目标文件运行相同 rea 查询。evidence_id 如何变化？

- **A** 机器时钟不同，所以不同
- **B** 本地路径不同，所以不同
- **C** 只有目录名相同时才相同
- **D** 哈希排除 name 和 local_path，所以相同

<details>
<summary>查看答案与解析</summary>

**答案**　D

语义投影保留 subject 摘要、格式和架构，去掉 name、local_path。相同字节的相同观察，在任何位置都有相同 ID。

</details>

## 3. 主张是 grade(55) == 0。账本已有 Ghidra 伪代码记录及推导表模型。主张状态是什么？

- **A** pass，因为伪代码记录是 observed
- **B** unsupported，因为没有观察执行说明结果
- **C** pass，因为两条记录符合主张
- **D** fail，因为伪代码显示不同表达式

<details>
<summary>查看答案与解析</summary>

**答案**　B

伪代码只观察 Ghidra 打印了什么，并非函数返回什么。只有观察函数执行才能使行为主张晋级。

</details>

## 4. 快照在 profile 摘要 a04af771 下保存。后续 rea 版本将 jump_table_evidence 改为 v2 契约。缓存如何处理快照？

- **A** 重放条目并将其标为过期
- **B** 以 profile_mismatch 拒绝导入
- **C** 启动 Ghidra 并覆盖旧项
- **D** 只重放没有跳转表的条目

<details>
<summary>查看答案与解析</summary>

**答案**　B

profile 摘要覆盖每个契约版本字符串。版本变化产生新摘要，快照不再匹配当前绑定。

</details>

## 5. 什么能以 verified 处置关闭残留未知项？

- **A** 至少一个符合所需 confidence 与 authority 的证据 ID
- **B** 分析者写一条理由
- **C** 新版本状态为 resolved，证据列表为空
- **D** 从账本删除未知项

<details>
<summary>查看答案与解析</summary>

**答案**　A

verified 解决必须引用证据 ID，账本检查其为 observed，并具有未知项要求的 authority。

</details>

## 6. 本机构建执行显示 grade(95) == 4、grade(100) == 4，主张覆盖 90 到 100 所有分数。正确状态是什么？

- **A** unknown，因为 11 个输入中仅 2 个有观察执行
- **B** unsupported，因为 x86-64 目标自身从未运行
- **C** pass，因为所有已观察运行都一致
- **D** fail，因为九个输入没有执行

<details>
<summary>查看答案与解析</summary>

**答案**　A

部分覆盖是 unknown，不是 pass 或 fail。其余九个输入有观察执行前，未知项保持开启。

</details>


[返回本课](docs/zh.md)
