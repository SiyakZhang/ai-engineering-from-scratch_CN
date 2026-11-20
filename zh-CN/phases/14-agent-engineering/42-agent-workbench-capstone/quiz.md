# 综合项目：交付一个可复用的 Agent 工作台包 · 自测

每题先选答案，再展开解析。

## 1. 这个毕业项目产出什么？

- **A** 一篇研究论文
- **B** 一个监控仪表盘
- **C** 一个带版本的、可直接放入的目录（agent-workbench-pack/），含七个面，外加一个能幂等铺设它们的 bin/install.sh
- **D** 一个新的 LLM

<details>
<summary>查看答案与解析</summary>

**答案**　C

这个包是配方；每次安装是一份上桌的菜。

</details>

## 2. 下列哪一个不是这个包的布局之一？

- **A** AGENTS.md + docs/
- **B** scripts/
- **C** vendor_proprietary_weights/
- **D** schemas/

<details>
<summary>查看答案与解析</summary>

**答案**　C

包布局是 AGENTS.md、docs/、schemas/、scripts/、bin/、README.md。这个包与框架和厂商无关。

</details>

## 3. 为什么这个包携带一个 VERSION 文件？

- **A** 为了 SEO
- **B** 为了追踪 agent 智商
- **C** 需要迁移的 schema/脚本变更升主版本；新增升次版本；仅文档升补丁版本；目标 repo 记录它是对照哪个版本安装的
- **D** 为了在 Hacker News 上打广告

<details>
<summary>查看答案与解析</summary>

**答案**　C

与 npm、Cargo、pyproject.toml 形态相同；VERSION 是契约，不是营销。

</details>

## 4. 在这个包里，跨工具分发长什么样？

- **A** 硬编码每个工具的路径
- **B** 为每个工具手动复制
- **C** 一个源文件加符号链接（ln -s AGENTS.md CLAUDE.md、.cursor/rules/、.github/copilot-instructions.md），使同一来源扇出到每个编码 agent
- **D** 每个工具一处厂商锁定

<details>
<summary>查看答案与解析</summary>

**答案**　C

Nx 的 nx ai-setup 是参考；这个包的安装器用符号链接做同样的事。

</details>

## 5. 本课建议卸载器（uninstaller）如何行为？

- **A** 禁用 git
- **B** 遇到非平凡状态就拒绝；绝不删除用户的 agent_state.json、task_board.json 或 outputs/；只移除 schemas、scripts、docs 和 AGENTS.md（可选退出）
- **C** 只删 docs
- **D** 删除一切，包括状态

<details>
<summary>查看答案与解析</summary>

**答案**　B

状态属于用户；这个包不拥有它。

</details>

## 6. 什么东西被排除在这个包之外？

- **A** Schemas
- **B** Scripts
- **C** 安装器
- **D** 项目特定的任务、厂商 SDK 调用、团队入职文字——这个包与框架无关，应与入职材料并列、而非嵌入其中

<details>
<summary>查看答案与解析</summary>

**答案**　D

任务属于目标 repo 的任务板，而非这个包；厂商 SDK 调用会把包锁死到一个框架上。

</details>

## 7. 这个包通过什么渠道一次性发布到众多编码 agent？

- **A** 邮件附件
- **B** 只有 GitHub release notes
- **C** SkillKit 式分发（skillkit install agent-workbench-pack）从单一来源把它铺设到 32 个 AI agent 上
- **D** 手动复制

<details>
<summary>查看答案与解析</summary>

**答案**　C

包仓库是真相来源；SkillKit 是分发渠道；厂商锁定随之瓦解。

</details>


[返回本课](docs/zh.md)
