# Many-shot jailbreaking（多示例越狱）的评估 · 导读自测

先独立作答，再展开参考解析。

## 1. 为什么应分开测量不同长度的上下文？

<details>
<summary>查看参考解析</summary>

短输入的安全表现不能代表长输入。分组测量可以发现风险是否随上下文长度和组成而改变。

</details>

## 2. 如何检查防护是否误伤正常长文档？

<details>
<summary>查看参考解析</summary>

在同一长度分组加入经授权的正常任务，观察任务通过率、误拦率和延迟。

</details>

[返回本课导读](docs/zh.md)
