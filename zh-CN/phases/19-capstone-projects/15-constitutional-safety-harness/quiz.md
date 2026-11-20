# Constitutional safety harness（基于原则的安全评估框架） · 导读自测

先独立作答，再展开参考解析。

## 1. 模型评审给出“允许”，应用权限检查却拒绝了这一动作。系统应如何处理？

<details>
<summary>查看参考解析</summary>

遵守应用层权限决定，记录拒绝原因，确保工具未执行且状态未改变。

</details>

## 2. 修订一条安全规则后，需要一起复跑哪些用例？

<details>
<summary>查看参考解析</summary>

一起复跑应拦截与应放行的历史用例，检查规则编号、判定、误报与实际动作的执行结果。

</details>

[返回本课导读](docs/zh.md)
