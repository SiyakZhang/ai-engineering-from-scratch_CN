# 技能库与终身学习（Voyager） · 自测

每题先选答案，再展开解析。

## 1. Voyager 把什么当作动作空间（action space）？

- **A** 仅文本 prompt
- **B** 强化学习的 Q 值
- **C** 原始的 Minecraft 命令
- **D** 可执行代码（JavaScript 函数），被存储、检索和组合

<details>
<summary>查看答案与解析</summary>

**答案**　D

Voyager 的贡献在于让代码成为动作：技能是程序，而非原始命令。

</details>

## 2. 哪三个组件定义了一个 Voyager agent？

- **A** Encoder、decoder、value head
- **B** Planner、executor、judge
- **C** Retriever、generator、ranker
- **D** 自动课程（automatic curriculum）、技能库（skill library）、迭代式 prompting

<details>
<summary>查看答案与解析</summary>

**答案**　D

Voyager 围绕课程、技能库和迭代式 prompting 来构建 agent。

</details>

## 3. 一次技能执行尝试可以返回哪三种信号？

- **A** 绿、黄、红
- **B** Heartbeat、ack、nack
- **C** 成功、错误（带堆栈跟踪）、自核实失败
- **D** Pass、fail、retry

<details>
<summary>查看答案与解析</summary>

**答案**　C

Voyager 的迭代式 prompting 机制由这三种信号驱动，它们被折叠回下一个版本。

</details>

## 4. 自动课程如何挑选下一个任务？

- **A** 总是当前可用的最难任务
- **B** 略高于当前能力，基于环境状态和技能清单（探索的甜区）
- **C** 在动作空间上随机均匀采样
- **D** 仅用户提供的列表

<details>
<summary>查看答案与解析</summary>

**答案**　B

提议者瞄准略高于当前能力的任务，使进步保持稳定。

</details>

## 5. 哪个 2026 年的产品是本课对 Voyager 技能最清晰的对应？

- **A** AWS Lambda 层
- **B** Pinecone 索引
- **C** Claude Agent SDK skills：具名、可检索的代码加指令，按需加载
- **D** OpenAI 微调

<details>
<summary>查看答案与解析</summary>

**答案**　C

Agent SDK skills 对应 Voyager 的具名-可检索-可组合的代码模式。

</details>

## 6. 为什么本课建议对技能库在写入时去重？

- **A** 提供商拒绝重复项
- **B** 不去重的话，同一个技能会被反复添加多次、描述略有不同；检索应返回一个规范版本
- **C** 磁盘很贵
- **D** Git 阻止重复项

<details>
<summary>查看答案与解析</summary>

**答案**　B

近似重复的描述会坍缩成单一的规范技能，使检索保持干净。

</details>

## 7. 组合技能漂移（composed-skill drift）描述的是什么问题？

- **A** 技能在存储中被加密
- **B** 一个父技能悄悄用上了它从未测试过的、被改进的子版本；用固定技能版本来修复
- **C** 检索返回空
- **D** Python 升级后某个技能不再编译

<details>
<summary>查看答案与解析</summary>

**答案**　B

没有版本固定，对子技能的一次改进会悄悄改变父技能的行为。

</details>


[返回本课](docs/zh.md)
