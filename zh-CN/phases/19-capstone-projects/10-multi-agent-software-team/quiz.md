# 顶点项目 10 —— 多 agent 软件工程团队 · 自测

每题先选答案，再展开解析。

## 1. 为什么即便有 200k token 上下文，单 agent harness 在大型任务上仍会触及天花板？

- **A** 单个 agent 无法进行工具调用
- **B** 模型缺乏对 git 的支持
- **C** 上下文无法同时容纳架构计划、四份并行的代码库切片、评审者评论和测试输出
- **D** 沙箱拒绝托管一个以上的进程

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 2. 在这种工厂形态中，架构师（architect）角色负责什么？

- **A** 审查合并后的 diff 是否有幻觉
- **B** 在干净的沙箱中运行测试套件
- **C** 阅读 issue 并产出一份带有显式接口的子任务计划
- **D** 当编码者意见不一致时强制合并分支

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 3. 为什么每个编码者要在自己的 git worktree 加上一个 Daytona 沙箱中工作？

- **A** 隔离的工作树让 N 个编码者并行实现子任务，而不会互相踩踏共享文件
- **B** Daytona 是唯一支持 SSH 的沙箱
- **C** worktree 比分支克隆更快
- **D** 架构师需要 worktree 的 ID

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 4. 为保持评审者诚实，对它施加了什么约束？

- **A** 它不能批准自己编写或提议的 diff
- **B** 它只能在测试者签字之后运行
- **C** 它必须与架构师是同一个模型
- **D** 它必须批准它读到的每一个 diff

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 5. 为什么细则要把 token 效率与单 agent 基线作权衡？

- **A** 单 agent 没有可观测性方案
- **B** 角色边界增加了摘要和交接上下文，因此真正的问题是这个工厂是否按每美元胜出
- **C** 多 agent 总是更便宜
- **D** token 成本与性能无关

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 6. 复盘期间，从每个失败的 issue 中产出哪种产物？

- **A** 一份更新的 A2A 协议规范
- **B** 一张交接失败直方图，指明是哪个角色边界出了问题（计划、合并、评审、测试）
- **C** 一份强制推送日志
- **D** 一个新的架构师计划模板

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 7. 本毕业项目用哪个评估集来对各角色评分 pass@1？

- **A** MT-Bench-v2
- **B** HumanEval-Java
- **C** MigrationBench
- **D** SWE-bench Pro 50 个 issue 的子集

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>


[返回本课](docs/zh.md)
