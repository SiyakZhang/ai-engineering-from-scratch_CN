# 用 HTN 和演化搜索做规划 · 自测

每题先选答案，再展开解析。

## 1. 相比自由形式的 LLM 计划，HTN 多提供了什么？

- **A** 更短的 prompt
- **B** 更好的 embedding
- **C** 更便宜的推理
- **D** 在强制执行算子的前置条件和效果时具备可证明的正确性

<details>
<summary>查看答案与解析</summary>

**答案**　D

HTN 带前置条件和效果的符号算子，从构造上保证了可靠性（soundness）。

</details>

## 2. AlphaEvolve 是为哪类问题构建的？

- **A** 多轮聊天记忆
- **B** 自由形式的散文生成
- **C** 拥有机器可校验、确定性适应度函数的优化问题
- **D** 向量搜索排序

<details>
<summary>查看答案与解析</summary>

**答案**　C

进化搜索需要一个确定性的评估器；AlphaEvolve 针对存在这种评估器的领域。

</details>

## 3. ChatHTN 在使用 LLM 的同时如何保持计划可靠性？

- **A** LLM 的建议只作为候选分解进入，并对照算子 schema 校验；符号层掌管正确性
- **B** 它使用一个向量数据库
- **C** 它做不到；可靠性只是尽力而为
- **D** 它在 HTN 轨迹上微调 LLM

<details>
<summary>查看答案与解析</summary>

**答案**　A

LLM 扩展了方法库，但无法绕过算子的前置条件和效果。

</details>

## 4. 本课引用了 AlphaEvolve 的哪个结果？

- **A** 56 年来首次对 4x4 复数矩阵乘法超越 Strassen
- **B** Gemini 推理加速 10 倍
- **C** 首次证明 P=NP
- **D** 在 HumanEval 上击败 GPT-4

<details>
<summary>查看答案与解析</summary>

**答案**　A

AlphaEvolve 为 4x4 复数矩阵乘法找到了 48 次标量乘法，这是 56 年来对 Strassen 的首次改进。

</details>

## 5. HTN 中哪个元素是带前置条件和效果的、可直接执行的原始动作？

- **A** 任务（Task）
- **B** 算子（Operator）
- **C** 状态（State）
- **D** 方法（Method）

<details>
<summary>查看答案与解析</summary>

**答案**　B

算子是原语；方法分解复合任务；状态是一组事实。

</details>

## 6. 本课对「没有真正评估器的 AlphaEvolve」给出了什么警告？

- **A** 它违反 Apache 2.0
- **B** 问 LLM 代码是否更好并不是一个适应度函数；评估器必须是确定性且快速的
- **C** 它无法在 GPU 上运行
- **D** 它很慢

<details>
<summary>查看答案与解析</summary>

**答案**　B

没有确定性评估器，搜索就没有信号去收敛。

</details>

## 7. 什么时候你应该选用 ReAct 或 ReWOO 而非 HTN 或 AlphaEvolve？

- **A** 当你不需要形式可靠性或机器可校验的适应度时；大多数 agent 任务都落在这里
- **B** 当你有可用的 GPU 集群时
- **C** 当延迟低于 100 毫秒时
- **D** 永不；HTN 严格更好

<details>
<summary>查看答案与解析</summary>

**答案**　A

本课明确警告不要过度工程化：大多数任务不需要形式规划或进化搜索。

</details>


[返回本课](docs/zh.md)
