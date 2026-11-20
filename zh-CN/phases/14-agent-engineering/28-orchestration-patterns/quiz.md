# 编排模式：Supervisor、Swarm、Hierarchical · 自测

每题先选答案，再展开解析。

## 1. 本课列出哪四种编排模式？

- **A** Push、pull、batch、stream
- **B** Supervisor-worker、swarm/点对点、hierarchical、debate
- **C** Plan、act、reflect、refine
- **D** Sequential、parallel、distributed、federated

<details>
<summary>查看答案与解析</summary>

**答案**　B

Supervisor-worker、swarm、hierarchical 和 debate 在 2026 年的各框架中反复出现。

</details>

## 2. 关于监督，2026 年 LangChain 的建议是什么？

- **A** 为了更精细的上下文工程控制，优先使用直接工具调用而非 create_supervisor
- **B** 在 GPU 上运行监督者
- **C** 完全避免监督
- **D** 总是用 create_supervisor

<details>
<summary>查看答案与解析</summary>

**答案**　A

基于工具调用的监督让你精确控制每个专家看到什么。

</details>

## 3. swarm 与 supervisor-worker 拓扑的区别在哪里？

- **A** swarm 是单 agent
- **B** swarm 使用 GPU
- **C** swarm 没有中央路由器；agent 通过一个共享工具面直接转交
- **D** swarm 只在 cron 上运行

<details>
<summary>查看答案与解析</summary>

**答案**　C

swarm 是点对点的；supervisor 通过一个 LLM 集中路由。

</details>

## 4. 层级式编排什么时候有正当理由？

- **A** 总是；它免费扩展
- **B** 永不；它是反模式
- **C** 当单个 supervisor 的上下文预算装不下所有专家的描述时
- **D** 只在有 GPU 时

<details>
<summary>查看答案与解析</summary>

**答案**　C

嵌套 supervisor 适用于超过单个 supervisor 预算的大型专家群体。

</details>

## 5. Anthropic 支持的推荐决策顺序是什么？

- **A** 从 debate 开始
- **B** 总是从层级式多 agent 开始
- **C** 从 swarm 开始向单 agent 收缩
- **D** 从单 agent 加工作流模式开始；只在需要时增加拓扑；supervisor 先于 swarm 先于 hierarchical；当准确率胜过成本时再用 debate

<details>
<summary>查看答案与解析</summary>

**答案**　D

Anthropic 的指引是构建满足你需求的系统，而非最复杂的系统。

</details>

## 6. 本课中的假层级（fake hierarchy）是什么？

- **A** 一个测试夹具
- **B** 因为「企业级」而设三层 supervisor，实际只有两个真实团队；把它压扁
- **C** 用 TypeScript 写的编排器
- **D** 标错的 YAML

<details>
<summary>查看答案与解析</summary>

**答案**　B

不对应真实团队的层级只会增加运维复杂度而无回报。

</details>

## 7. 如何缓解 swarm 中的反复转交（A -> B -> A -> B）？

- **A** 禁用 tracing
- **B** 把温度固定到 0
- **C** 降低限流
- **D** 加一个跳数计数器，在 N 次转交后拒绝

<details>
<summary>查看答案与解析</summary>

**答案**　D

跳数计数器在 swarm 循环无限往复之前对其设上限。

</details>


[返回本课](docs/zh.md)
