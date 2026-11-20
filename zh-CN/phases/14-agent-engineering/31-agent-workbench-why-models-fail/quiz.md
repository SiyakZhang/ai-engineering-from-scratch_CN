# Agent 工作台工程：能干的模型为什么还会失败 · 自测

每题先选答案，再展开解析。

## 1. 本课认定 agent 在真实任务上失败的根本原因是什么？

- **A** 工作台失败：模型周围缺失了一些面（surface），而非 LLM 的局限
- **B** 网络慢
- **C** 训练数据过时
- **D** 模型参数不足

<details>
<summary>查看答案与解析</summary>

**答案**　A

模型对 Python 没搞错；它搞错的是这份工作。模型周围的面缺失了。

</details>

## 2. 本课命名的七个工作台面是什么？

- **A** 指令、状态、范围、反馈、验证、审查、交接
- **B** Read、write、exec、fork、exit、wait、kill
- **C** Train、eval、deploy、monitor、retrain、scale、retire
- **D** Plan、act、reflect、refine、debate、vote、ship

<details>
<summary>查看答案与解析</summary>

**答案**　A

七个面是指令、状态、范围、反馈、验证、审查、交接。

</details>

## 3. 下列哪一个不是本课把这些面映射到的八个分布式系统原语之一？

- **A** 反向传播（Backpropagation）
- **B** Worker
- **C** 触发器（Trigger）
- **D** 函数（Function）

<details>
<summary>查看答案与解析</summary>

**答案**　A

八个原语是函数、worker、触发器、运行时、HTTP/RPC、队列、会话持久化、授权策略。

</details>

## 4. Vercel 报告的 harness 改动把成功率从多少提到了多少？

- **A** 20% 到 60%
- **B** 50% 到 70%，靠加 RAG
- **C** 80% 到 100%，靠删掉 agent 80% 的工具
- **D** 0% 到 100%，靠换模型

<details>
<summary>查看答案与解析</summary>

**答案**　C

删掉 80% 的工具把 Vercel 的 agent 从 80% 提到了 100% 成功率。

</details>

## 5. Terminal Bench 2.0 关于模型 vs harness 展示了什么？

- **A** harness 改动无关紧要
- **B** 只有模型本身决定排名
- **C** 只有 GPU 重要
- **D** 仅改变 harness，同一个模型就从 30 名开外升到了第五名

<details>
<summary>查看答案与解析</summary>

**答案**　D

LangChain 的《Anatomy of an Agent Harness》：同一模型，改 harness，排名跳升 25+ 名。

</details>

## 6. 本课建议在你听到新的 harness 词汇时怎么做？

- **A** 原样照搬这套词汇
- **B** 拒绝它
- **C** 等 OpenAI 把它标准化
- **D** 在采纳之前，把它翻译回原语（函数、worker、触发器、运行时、HTTP/RPC、队列、持久化、策略）

<details>
<summary>查看答案与解析</summary>

**答案**　D

从原语出发推理，而非从厂商分类法；词汇会变，但工程不变。

</details>

## 7. 聊天历史相对于工作台处于什么位置？

- **A** 聊天是易失的；repo 才是记录系统
- **B** 两者都不重要
- **C** 两者等价
- **D** 聊天是记录系统（system of record）

<details>
<summary>查看答案与解析</summary>

**答案**　A

循环闭合在状态文件上，而非聊天历史上。

</details>


[返回本课](docs/zh.md)
