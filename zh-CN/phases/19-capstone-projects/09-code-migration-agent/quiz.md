# 顶点项目 09 —— 代码迁移 agent（仓库级语言 / 运行时升级） · 自测

每题先选答案，再展开解析。

## 1. 为什么流水线要把确定性底座与 agent 层结合，而不是只用其中一种？

- **A** 单靠 agent 比配方（recipe）更快
- **B** 确定性配方比 LLM 更慢
- **C** OpenRewrite 或 libcst 能安全且廉价地处理 70-80% 的机械式重写，把模糊的长尾留给 agent
- **D** 只有构建系统才需要确定性

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 2. 流水线用什么信号作为一次迁移成功的真值？

- **A** 沙箱中 CI 通过（变绿），且覆盖率回退不超过一个很小的阈值
- **B** diff 大小低于硬性上限
- **C** 评审者在 PR 上批准
- **D** agent 按细则自评

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 3. agent 循环为每个仓库强制哪些预算上限？

- **A** 30 分钟挂钟时间、8 美元成本和 20 个 agent 轮次
- **B** 时间和成本无限制；仅在出错时中止
- **C** 无轮次上限，100 美元封顶
- **D** 1 小时挂钟时间和 100 轮

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 4. 当迁移后覆盖率下降超过约 2% 时，会触发什么门禁？

- **A** agent 自动强制推送一个修复
- **B** 该仓库被归入 coverage_regression 失败类别，而不是开一个干净的 PR
- **C** 确定性底座重放它的配方
- **D** 绕过评审者

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 5. 为什么失败分类法（failure taxonomy）被当作交付物，而非附带产物？

- **A** 它满足一项合规清单
- **B** 它按类别归类失败的仓库，以便未来的配方作者能针对头部失败模式
- **C** 它是 GitHub 分支保护所要求的
- **D** 它取代了测试套件

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 6. 本毕业项目针对 Java 8 到 17 的迁移瞄准哪个公开基准？

- **A** 亚马逊的 MigrationBench
- **B** SWE-bench Pro
- **C** MMLU-Pro
- **D** ViDoRe v3

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 7. agent 集成细则衡量修复分布的什么？

- **A** 每个仓库的强制推送次数
- **B** 由 OpenRewrite 处理与由 agent 层编写的修复各占的比例
- **C** 源文件的分词速度
- **D** 被固定（pin）的依赖数量

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>


[返回本课](docs/zh.md)
