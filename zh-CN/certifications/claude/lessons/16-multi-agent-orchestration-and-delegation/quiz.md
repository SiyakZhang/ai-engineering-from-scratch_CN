# 多 Agent 编排与委派 · 自测

每题先选答案，再展开解析。

## 1. 什么情况下 subagent 比简单 tool 更合适？

- **A** 长推理任务与 parent 共享全部上下文、权限与评估时
- **B** 任务需要自己的有界推理循环、证据、上下文与停止条件时
- **C** 确定性转换需要独立日志与重试策略时
- **D** 模糊任务还没有输出合约或完成标准时

<details>
<summary>查看答案与解析</summary>

**答案**　B

当任务需要有界推理、隔离、专门化或独立审查时，单独的 subagent 上下文才有价值。确定性操作应该放在代码或 tool 中。

</details>

## 2. 哪项要求应该由编排代码强制执行，而不是写进 coordinator prompt？

- **A** synthesis 前，哪项有歧义的主张需要再收集一轮证据
- **B** 哪个权威来源更直接地支持有争议的语义主张
- **C** 必需的逐文件结果达到 complete 或明确的 partial 前，不得开始跨文件审查
- **D** 某种解释是否更符合定性的清晰度 rubric

<details>
<summary>查看答案与解析</summary>

**答案**　C

阶段前置条件是稳定的 invariant。代码应跟踪 manifest 并阻止非法状态转换，Claude 则在允许状态内处理语义判断。

</details>

## 3. partial subagent 结果应该包含什么？

- **A** 一份看似完整、附有不确定性说明，但没有明确覆盖边界的产物
- **B** 完整推理 transcript 与 tool 历史，但没有规范化结果合约
- **C** 失败标记、最后尝试的操作，以及要求 coordinator 重试的请求
- **D** 有效的已完成工作，加上具名缺口、失败证据与安全的后续操作

<details>
<summary>查看答案与解析</summary>

**答案**　D

partial 是一等状态。它既保留可用工作，又防止 coordinator 把缺失证据误当成完成或反面证据。

</details>

## 4. 为什么独立 reviewer 应获得全新上下文？

- **A** 减少继承 generator 的 framing 与缺少依据的假设
- **B** 让 reviewer 凭直觉判断，不受 rubric 约束
- **C** 阻止 reviewer 看到 generator 使用过的任何证据
- **D** 让 reviewer 获得比 generator 更大的独立 token 预算

<details>
<summary>查看答案与解析</summary>

**答案**　A

上下文隔离让 reviewer 根据 rubric 判断产物与证据，而不是延续 generator 有说服力的叙述。

</details>

## 5. 三名 source researcher 可以独立工作。哪种编排最可靠？

- **A** 顺序运行，让后续 agent 继承之前所有 framing 与来源
- **B** 并行运行有界任务，规范化结果并保留失败，再执行 reduce
- **C** 给每名 researcher 相同的可写 tool，让任何一名都能补完缺失工作
- **D** 让每名 researcher 分别起草完整报告，再选择内容最全面的一版

<details>
<summary>查看答案与解析</summary>

**答案**　B

独立工作可以通过并行 fan-out 降低延迟，但可靠的 reduction 需要共享 schema、来源身份、错误传递与冲突规则。

</details>

## 6. 多 agent 设计成本更高，却没有改善结果。架构师首先应该做什么？

- **A** 保留拓扑，但只评价最终答案，避免协调成本主导结果
- **B** 在改变现有角色前，先增加 coordinator agent 减少重复工作
- **C** 与单 agent 基线比较，并删除无法测得隔离、独立或并行价值的上下文
- **D** 增加每个 agent 的上下文与推理预算，挽回协调造成的质量损失

<details>
<summary>查看答案与解析</summary>

**答案**　C

每个上下文都要带来可测量的收益，才能覆盖协调成本。删除不必要的 agent 通常会改善延迟、成本与可调试性。

</details>


[返回本课](docs/zh.md)
