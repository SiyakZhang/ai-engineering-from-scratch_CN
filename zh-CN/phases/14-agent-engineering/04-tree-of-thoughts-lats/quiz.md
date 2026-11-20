# Tree of Thoughts 与 LATS：刻意搜索 · 自测

每题先选答案，再展开解析。

## 1. 为什么思维链在 Game of 24 上表现挣扎？

- **A** prompt 太短
- **B** CoT 需要一个 GPT-4 缺少的计算器工具
- **C** 模型无法做整数乘法
- **D** 一次线性的推进在早期某步出错时无法回溯，于是后续步骤把错误层层放大

<details>
<summary>查看答案与解析</summary>

**答案**　D

没有分支，一个错误的早期子表达式会毒化后面的整条链；论文测得 CoT 只有 4%。

</details>

## 2. 在 Tree of Thoughts 搜索中，一个节点是什么？

- **A** 微调期间的一次权重更新
- **B** 模型产出的一个 token
- **C** 一个连贯的中间步骤或想法，可有 K 个子扩展
- **D** 向运行时注册的一个工具

<details>
<summary>查看答案与解析</summary>

**答案**　C

ToT 把推理当作一棵树，每个节点是一个可以扩展出 K 个子节点的中间想法。

</details>

## 3. 下列三者中哪一个不是 LATS 赋予 LLM 的角色？

- **A** 给部分轨迹打分的价值函数（value function）
- **B** 提出下一步行动的策略（policy）
- **C** 在失败时写下反思的自反思器（self-reflector）
- **D** 在 rollout 之间更新模型权重的优化器（optimizer）

<details>
<summary>查看答案与解析</summary>

**答案**　D

LATS 是无梯度的；三个 LLM 角色是策略、价值和自反思器。不存在权重更新。

</details>

## 4. 说出本课列出的 MCTS 四个阶段。

- **A** Plan、Execute、Reflect、Stop
- **B** Search、Synthesize、Synthesize-Again、Stop
- **C** Select、Expand、Simulate、Backpropagate
- **D** Sample、Score、Sort、Submit

<details>
<summary>查看答案与解析</summary>

**答案**　C

MCTS 每次迭代按 select、expand、simulate、backpropagate 进行。

</details>

## 5. 在 UCT 中，探索常数 c 的作用是什么？

- **A** 它设置最大树深度
- **B** 它在探索项 sqrt(ln N / n) 和利用项 Q 之间进行加权
- **C** 它缩放价值估计 Q
- **D** 它控制 rollout 的数量

<details>
<summary>查看答案与解析</summary>

**答案**　B

c 在利用项（Q）和探索项之间取得平衡；按任务调优。

</details>

## 6. 相比单条轨迹，什么时候搜索是主动有害的？

- **A** 只要 token 便宜
- **B** 当任务是代码生成时
- **C** 当任务涉及多个正确答案时
- **D** 当评估器有噪声且只有唯一正确答案时，搜索会收敛到一个得分不错的错误答案

<details>
<summary>查看答案与解析</summary>

**答案**　D

有噪声的价值函数加上唯一正确答案，正是搜索过拟合到噪声的情形。

</details>

## 7. 在 Game of 24 上，相比 CoT，你大致应该为 ToT 预留多少倍的 token 用量？

- **A** 100 到 1000 倍
- **B** 约 2 倍
- **C** 比 CoT 更少，因为有剪枝
- **D** 约 10 倍

<details>
<summary>查看答案与解析</summary>

**答案**　A

本课引用 ToT 在 Game of 24 上相比 CoT 有 100-1000 倍的 token 成本。

</details>


[返回本课](docs/zh.md)
