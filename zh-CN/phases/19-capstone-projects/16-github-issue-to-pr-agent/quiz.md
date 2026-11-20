# 顶点项目 16 —— GitHub Issue 到 PR 的自主 agent · 自测

每题先选答案，再展开解析。

## 1. 异步云端编码 agent 在生产中如何被触发？

- **A** 定时 cron 任务命中仓库
- **B** 手动上传文件
- **C** 由 issue 标签或 PR 评论触发的 GitHub webhook，分派给一个沙箱 worker
- **D** 进入虚拟机的长连接 SSH 会话

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 2. 为什么 agent 必须使用短期的 GitHub App 安装令牌，而非个人访问令牌（PAT）？

- **A** App 能完全规避 GitHub 限流
- **B** App 比 PAT 需要更少的代码
- **C** App 令牌授予细粒度、有作用域、短期的凭证，适合按任务的 worker
- **D** 个人访问令牌无法开 PR

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 3. 哪两项保护防止 agent 搞坏 main？

- **A** 每次推送都要求验证码
- **B** 分支保护强制禁止直接推送或强制推送到 main，且该 App 不在绕过名单中
- **C** 在 worker 上禁用 git
- **D** 克隆前加密仓库

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 4. 为什么对 .github/workflows 的路径作用域保护要在 worker 上强制执行，而非作为 GitHub App 权限？

- **A** 任何形式的路径作用域都不可能实现
- **B** GitHub App 权限不支持按路径设作用域，因此 worker 对所提议 diff 的允许列表检查才是恰当的执行点
- **C** 工作流存储在仓库之外
- **D** .github/workflows 是一个虚拟路径

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 5. 在 agent 循环结束后、开 PR 之前发生什么门禁？

- **A** 仓库被强制推送到 main
- **B** 在沙箱中跑完整 CI；计算覆盖率增量；回归超过阈值的 PR 被打上 needs-review 标签
- **C** PR 不经任何检查立即开启
- **D** 评审者模型重写 diff

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 6. 分派器对每个仓库每天强制哪些预算旋钮？

- **A** 仅一个轮次上限
- **B** 仅一个挂钟时间上限
- **C** 无限 PR 和无限成本
- **D** 每个 PR 的美元上限，加上每个仓库每天的最大 PR 数

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 7. agent 发布的 PR 正文里包含什么？

- **A** 理由、diff 摘要、trace URL、成本和轮次数，以便评审者审计和跟进
- **B** 仅 diff
- **C** 什么都没有；PR 正文为空
- **D** 仅一份生成的变更日志

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>


[返回本课](docs/zh.md)
