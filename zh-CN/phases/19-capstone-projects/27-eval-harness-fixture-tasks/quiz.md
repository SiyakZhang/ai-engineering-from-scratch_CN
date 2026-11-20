# 顶点课 27：带 Fixture Tasks 的 Eval Harness · 自测

每题先选答案，再展开解析。

## 1. 在阅读本课之前：一个好的 agent 评估验证器最需要具备什么特性？

- **A** 对候选代码的每一行都有覆盖。
- **B** 对判定结果的自然语言解释。
- **C** 跨运行的确定性。
- **D** 毫秒级的执行速度。

<details>
<summary>查看答案与解析</summary>

**答案**　C

确定性是让回归可检测的前提。一个非确定性的验证器会让每个红灯变成掷硬币。

</details>

## 2. 一个候选在单个任务的 5 次采样中通过了 3 次。本课的 pass@5 公式返回多少（保留两位小数）？

- **A** 0.60
- **B** 0.99
- **C** 0.75
- **D** 1.00

<details>
<summary>查看答案与解析</summary>

**答案**　B

pass@k = 1 - (1 - p)^k = 1 - (1 - 0.6)^5 = 1 - 0.4^5 = 1 - 0.01024 = 0.98976，四舍五入为 0.99。原始单样本通过率 0.6 是选项 (a) 的值，但公式在 k 次采样上对其做了放大。对于相同的统计次数，第 72 课的无偏估计量会给出 1.00，因为在 n = k = 5 时只要有任意样本通过结果就为 1。

</details>

## 3. 为什么报告中同时包含 pass@1 和 pass@k？

- **A** pass@1 是验证器注册中心支持的版本；pass@k 留给未来的验证器使用。
- **B** 当 k > 1 时 pass@k 和 pass@1 在数学上完全相同。
- **C** pass@1 是面板上给用户看的值；pass@k 供内部调试使用。
- **D** pass@k 可能掩盖一个只在多次采样中偶尔答对的模型，所以 pass@1 用首次尝试质量来锚定结果。

<details>
<summary>查看答案与解析</summary>

**答案**　D

pass@k 会让那些多次中碰巧答对一次的模型看起来很强；pass@1 是首次尝试的下限。两者都报告可以防止过度宣称。

</details>

## 4. 驱动层在每个 sample 之前都调用 _prepare_scratch。为什么这对 pass@k > 1 很重要？

- **A** 避免共享临时目录上的竞态条件。
- **B** 确保每个 sample 从有 bug 的初始状态开始，而不是前一个 sample 的输出。
- **C** 只和 shell 验证器有关。
- **D** 这纯粹是性能优化。

<details>
<summary>查看答案与解析</summary>

**答案**　B

如果不重置 scratch，第 N+1 个 sample 会从第 N 个 sample 的输出开始。驱动层测的就变成了「第二次尝试收尾」而不是首次尝试成功率。

</details>

## 5. 你想新增一个 'pytest_passes' 验证器，在 scratch 目录里跑 pytest。应该基于哪个现有验证器来实现？

- **A** file_equals，因为 pytest 会写结果文件。
- **B** shell_exit_zero，因为 pytest 用退出码 0 表示通过。
- **C** regex_match，因为 pytest 输出里有 'passed' 这个词。
- **D** 没法把 pytest 表达为验证器。

<details>
<summary>查看答案与解析</summary>

**答案**　B

pytest 通过时退出码为 0，失败时非零。shell_exit_zero 是正确的原语。生产环境中会通过第 26 课的沙箱来路由这个调用。

</details>

## 6. 审阅者问：「这个回归是模型的问题还是驱动层的问题？」哪个产物能回答这个问题？

- **A** Agent 的思维链记录。
- **B** Fixture JSON 文件。
- **C** 验证器注册中心的源码。
- **D** 逐任务、逐 sample 的 SampleResult 加验证器详情消息。

<details>
<summary>查看答案与解析</summary>

**答案**　D

每个 sample 的延迟、验证器详情和通过/失败结果让你能分诊：同样的 fixture、不同的判定说明模型变了；同样的判定但延迟不同，说明其他东西在动。

</details>


[返回本课](docs/zh.md)
