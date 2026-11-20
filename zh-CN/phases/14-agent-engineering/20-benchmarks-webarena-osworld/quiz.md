# 基准：WebArena 与 OSWorld · 自测

每题先选答案，再展开解析。

## 1. 为什么 WebArena 自托管它的四个目标应用？

- **A** 为了在 GPU 上运行
- **B** 为了避免 TLS
- **C** 为了固定可复现的版本，使评估是基于执行的、不会不稳定
- **D** 为了省钱

<details>
<summary>查看答案与解析</summary>

**答案**　C

固定的自托管应用使基于执行的评估随时间都可靠、可比较。

</details>

## 2. 为什么 OSWorld 使用真实的操作系统截图，而不是无障碍 API？

- **A** 无障碍 API 太快了
- **B** 截图迫使 agent 在 1920x1080 下做真正的 GUI 接地（grounding），匹配生产约束
- **C** 截图成本更低
- **D** 无障碍 API 会泄露 PII

<details>
<summary>查看答案与解析</summary>

**答案**　B

截图驱动的评估迫使「像素到元素」的接地，这正是真实的生产约束。

</details>

## 3. OSWorld 暴露了哪两种主要的失败模式？

- **A** 延迟和带宽
- **B** embedding 漂移和 token 泄露
- **C** 幻觉和拒答
- **D** GUI 接地和操作性知识

<details>
<summary>查看答案与解析</summary>

**答案**　D

接地（像素到元素）和操作性知识（菜单、快捷键）是头号拦路虎。

</details>

## 4. OSWorld-Human 在基础基准之上增加了什么？

- **A** 更大的屏幕分辨率
- **B** 人工筛选的黄金动作轨迹，暴露出 agent 1.4-2.7 倍的步骤低效差距
- **C** 一个新的操作系统
- **D** 更多任务

<details>
<summary>查看答案与解析</summary>

**答案**　B

黄金轨迹使轨迹效率可衡量，而不只是成功率。

</details>

## 5. 本课引用了 WebArena 的哪个发布时数字？

- **A** 最佳 agent 50%，人类 50%
- **B** 最佳 agent 全面 0%
- **C** 最佳 agent 99%，人类 100%
- **D** 最佳 GPT-4 agent 成功率 14.41%，对比人类 78.24%

<details>
<summary>查看答案与解析</summary>

**答案**　D

14.41% 对 78.24% 的差距是 WebArena 的发布时数字。

</details>

## 6. 本课警告，当 agent 使用 DOM 或无障碍 API 时，仅截图评估会发生什么？

- **A** 没有变化
- **B** 你超出限流
- **C** 测试轻易就通过
- **D** 你会错过 OSWorld 旨在衡量的接地挑战

<details>
<summary>查看答案与解析</summary>

**答案**　D

在仅截图的基准上评估一个用无障碍 API 的 agent，会跳过接地测试。

</details>

## 7. 为什么忽略轨迹长度是一个基准测试上的失误？

- **A** 轨迹不可衡量
- **B** 长度是唯一重要的指标
- **C** 它掩盖了仅看成功率会遗漏的成本和低效（OSWorld-Human 暴露的 1.4-2.7 倍差距）
- **D** 轨迹长度总是与黄金轨迹一致

<details>
<summary>查看答案与解析</summary>

**答案**　C

两个都达到 60% 成功率的 agent，步数可能相差 2-3 倍；成本和效率只有衡量轨迹长度才显现。

</details>


[返回本课](docs/zh.md)
