# Agent 记忆——虚拟上下文与记忆分页 · 自测

每题先选答案，再展开解析。

## 1. MemGPT 建立在什么操作系统类比之上？

- **A** 网络套接字
- **B** 进程与线程
- **C** 虚拟内存：主上下文如同 RAM，外部存储如同磁盘，记忆工具如同换入换出（page in/out）
- **D** 文件描述符

<details>
<summary>查看答案与解析</summary>

**答案**　C

MemGPT 把 prompt 映射为 RAM，外部存储映射为磁盘，记忆工具映射为缺页式的传输。

</details>

## 2. 为什么更大的上下文窗口并不能完全解决记忆问题？

- **A** 长上下文不花钱
- **B** 模型拒绝长输入
- **C** 提供商把它们限制在 4k token
- **D** 即使有 128k 窗口，溢出、注意力被稀释、缺乏跨会话持久化仍然会出问题

<details>
<summary>查看答案与解析</summary>

**答案**　D

Mem0 测得 128k 窗口的基线仍会漏掉一个带外部记忆的 4k agent 能抓住的事实；溢出、稀释和持久化问题依旧存在。

</details>

## 3. 下列哪一个不是 MemGPT 的经典记忆工具之一？

- **A** gradient_memory_update
- **B** core_memory_append
- **C** archival_memory_search
- **D** conversation_search

<details>
<summary>查看答案与解析</summary>

**答案**　A

不存在梯度记忆工具；其工具面是 core/archival/conversation 操作。

</details>

## 4. MemGPT 中的中断（interrupt）模式做什么？

- **A** 它完全绕过上下文窗口
- **B** 它触发模型重训练
- **C** 在对话中途，agent 调用一个记忆工具，运行时执行它，结果拼接进下一轮
- **D** 它在任何错误时停止整个 agent 运行

<details>
<summary>查看答案与解析</summary>

**答案**　C

记忆即中断：调用记忆工具，运行时取数据，结果在下一轮作为新的 observation 返回（就像 Unix 的 read()）。

</details>

## 5. MemGPT 在 2024 年演化成了哪个生产系统？

- **A** Letta
- **B** Zep
- **C** Mem0
- **D** Pinecone

<details>
<summary>查看答案与解析</summary>

**答案**　A

MemGPT 在 2024 年 9 月变成了 Letta；研究仓库 cpacker/MemGPT 仍作为起源存在。

</details>

## 6. 在此语境下，记忆投毒（memory poisoning）是什么？

- **A** 在 RAM 可用时仍从磁盘读取
- **B** 破坏向量索引的一个 bug
- **C** embedding 模型版本漂移
- **D** 攻击者的内容被存成一条记忆笔记，并在未来的回忆中被重新摄入

<details>
<summary>查看答案与解析</summary>

**答案**　D

外部记忆是被检索回来的文本；如果攻击者可触及的内容进入了一条记忆笔记，agent 在下次会话就会重新摄入它。

</details>

## 7. 为什么本课说生产级记忆系统都是 MemGPT 的变体？

- **A** Letta、Mem0、Assistants 的 thread，以及 Claude Agent SDK 都运行两层（或更多）分页记忆模式；差异在于运维形态
- **B** 它们使用同一个向量数据库
- **C** MemGPT 拥有商标
- **D** 它们共享权重

<details>
<summary>查看答案与解析</summary>

**答案**　A

按运维形态而非模式来选；它们都共享 MemGPT 的换入/换出骨架。

</details>


[返回本课](docs/zh.md)
