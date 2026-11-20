# Agent Harness Loop 契约 · 自测

每题先选答案，再展开解析。

## 1. 为什么要把驱动循环建模为显式状态机，而不是用 while 循环加标志位？

- **A** 在 CPython 上跑得更快
- **B** 状态机可以在一处集中拦截非法转换，还能通过事件日志回放整个会话
- **C** 这是模型唯一能调用的形状
- **D** 这样就不需要写测试了

<details>
<summary>查看答案与解析</summary>

**答案**　B

状态机把合法性规则全放在一个转换函数里。同样的输入序列一定产出同样的状态——这正是会话回放能成立的前提。

</details>

## 2. 循环中的 pull point（拉取点）代表什么？

- **A** 一个每隔 N 秒触发的定时器
- **B** 模型调用后返回工具名称的地方
- **C** 循环在此交出控制权并等待调用方提供输入的位置
- **D** 一个会修改 payload 的 hook 订阅者

<details>
<summary>查看答案与解析</summary>

**答案**　C

Pull point 是 return，不是异常。调用方获取驱动层要求的东西，然后调用 resume()。

</details>

## 3. 哪个状态是工具调用唯一合法的 pull point？

- **A** EXECUTING
- **B** AWAITING_TOOL
- **C** REFLECTING
- **D** PLANNING

<details>
<summary>查看答案与解析</summary>

**答案**　B

只有 AWAITING_TOOL 会产生工具 pull point。EXECUTING 在某个步骤需要工具时转换到它。

</details>

## 4. 当 hook 在 before_tool_call 中抛出 HookAbort 时会发生什么？

- **A** 该 hook 被注销
- **B** 会话立即转换到 DONE
- **C** 预算被重置
- **D** 工具调用被跳过，on_error 触发，循环进入 REFLECTING

<details>
<summary>查看答案与解析</summary>

**答案**　D

HookAbort 取消正在进行的工具分发，用中止原因触发 on_error，然后继续运行。

</details>

## 5. 为什么 hook 和 event 要作为两个独立关注点来维护？

- **A** 因为事件类型是 bytes，而 hook 是字符串
- **B** 因为事件日志不能存 dict
- **C** 因为审计脚本不允许订阅者存在
- **D** Hook 是命令式的，能修改或中止操作；Event 是观测式的，只追加不修改

<details>
<summary>查看答案与解析</summary>

**答案**　D

Hook 改变行为，Event 描述行为。把两者混在一起会导致策略和遥测耦合——这正是我们要避免的坑。

</details>

## 6. 当实际耗时超过预算时，下一个状态是什么？

- **A** EXECUTING —— 循环重试
- **B** IDLE —— 返回一个带 budget_exceeded 原因的 pull point
- **C** PLANNING —— 起草新计划
- **D** DONE —— 会话终止

<details>
<summary>查看答案与解析</summary>

**答案**　B

预算耗尽是一次 yield。驱动层转换到 IDLE，触发 on_budget_exceeded，并返回一个 PullRequest，让调用方决定是延长预算还是关闭会话。

</details>

## 7. 为什么本课用 stub 代替真实模型作为 planner？

- **A** 为了在绑定任何模型之前就能对循环契约做确定性测试
- **B** 因为在本地调用模型太慢
- **C** 为了省 token
- **D** 因为模型无法返回工具调用

<details>
<summary>查看答案与解析</summary>

**答案**　A

先把循环契约钉死，后续课程才能在不重新协商状态机的前提下换入真正的 planner、registry 和 dispatcher。

</details>


[返回本课](docs/zh.md)
