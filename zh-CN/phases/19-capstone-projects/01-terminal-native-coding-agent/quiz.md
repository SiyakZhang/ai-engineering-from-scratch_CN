# 顶点项目 01 —— 终端原生编码 agent · 自测

每题先选答案，再展开解析。

## 1. 2026 年的终端编码 agent 共享哪种循环形态？

- **A** 训练、评估、部署、监控
- **B** 编码、解码、采样、流式输出
- **C** 规划、行动、观察、恢复（plan, act, observe, recover）
- **D** 拉取、嵌入、排序、综合

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 2. 为什么 harness 要在 E2B 或 Daytona 沙箱中运行每个任务？

- **A** 为了让 agent 循环能访问 GPU
- **B** 为了绕过模型供应商的限流
- **C** 为了在冷缓存上对 token 吞吐量做基准测试
- **D** 为了把文件系统和工具执行与宿主机隔离，以便在完成时可以销毁该 worktree

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 3. 哪个内置 hook 是在破坏性 shell 命令执行前拦截它们的天然位置？

- **A** SessionStart
- **B** PreToolUse
- **C** Stop
- **D** PostToolUse

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 4. 本毕业项目把每个工具结果上限设为约 4k token。这主要防止哪种失败模式？

- **A** 跨恢复会话的陈旧计划状态
- **B** 通过恶意 shell 元字符发生的沙箱逃逸
- **C** 当工具返回大段转储时的上下文投毒和成本失控
- **D** 模型对工具调用轨迹的过拟合

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 5. 在 150k token 处，PreCompact hook 做什么？

- **A** 取消运行并退还用户预算
- **B** 强制推送当前分支以备份进度
- **C** 把后端模型切换为更小的 draft 模型
- **D** 把较早的轮次摘要为一个先前状态（prior-state）块，使计划和新观察仍能装下

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 6. 本毕业项目在一个 30 个 issue 的 SWE-bench Pro 子集上，把它的 harness 与哪个基线对比？

- **A** Aider
- **B** OpenCode
- **C** Live-SWE-agent
- **D** mini-swe-agent

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 7. 交付物对照哪一组指标进行衡量？

- **A** MRR@10 和 nDCG@10
- **B** WER、MOS 和首段音频输出时间
- **C** 困惑度、BLEU 和 ROUGE
- **D** pass@1、每任务轮次数和每任务成本（美元）

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>


[返回本课](docs/zh.md)
