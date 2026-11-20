# 阶段 14：Agent 工程

> 现代 AI 工程的核心。从第一性原理构建 agent。

## 在 GitHub 上开始本阶段

**前置要求：** 阶段 11“LLM 工程”与阶段 13“工具与协议”。

**第一课：** [Agent 循环](01-the-agent-loop/docs/zh.md)

如果不需要学完整个阶段，可以选择两条聚焦路径：

- [Agent 辅助工程](../../../learning-paths/using-coding-agents.json)：涵盖任务界定、仓库证据、harness、隔离、验证、评审和可持续的反馈。
- [产品判断与交付](../../../learning-paths/shaping-the-build.json)：涵盖目标、工作流发现、假设、切片、规格、指标、分阶段发布和反馈责任。

从仓库根目录运行：

```bash
python3 phases/14-agent-engineering/01-the-agent-loop/code/main.py
```

记录命令、退出码、思考-行动-观察轨迹、最终答案、回合数，以及终止运行的确切停止条件。

**下一步：** 改变脚本化任务或回合预算，预测效果，然后继续学习[ReWOO 与 Plan-and-Execute](02-rewoo-plan-and-execute/docs/zh.md)。

浏览[阶段 14 的完整课程列表](../../README.md#phase-14)或[跨阶段路线图](../../ROADMAP.md)。

## 本阶段中文课文

- [01 · Agent（智能体） 循环：观察、思考、行动](01-the-agent-loop/docs/zh.md)
- [02 · ReWOO 与 Plan-and-Execute：解耦的规划](02-rewoo-plan-and-execute/docs/zh.md)
- [03 · Reflexion：言语 reinforcement learning（强化学习）](03-reflexion-verbal-rl/docs/zh.md)
- [04 · Tree of Thoughts 与 LATS：刻意搜索](04-tree-of-thoughts-lats/docs/zh.md)
- [05 · Self-Refine 与 CRITIC：迭代式输出改进](05-self-refine-and-critic/docs/zh.md)
- [06 · 工具使用与函数调用](06-tool-use-and-function-calling/docs/zh.md)
- [07 · Agent（智能体） 记忆——虚拟上下文与记忆分页](07-memory-virtual-context-memgpt/docs/zh.md)
- [08 · 记忆块与休眠时计算](08-memory-blocks-sleep-time-compute/docs/zh.md)
- [09 · 混合记忆：向量 + 图 + KV](09-hybrid-memory-mem0/docs/zh.md)
- [10 · 技能库与终身学习（Voyager）](10-skill-libraries-voyager/docs/zh.md)
- [11 · 用 HTN 和演化搜索做规划](11-planning-htn-and-evolutionary/docs/zh.md)
- [12 · Anthropic 的工作流模式：简单胜过复杂](12-anthropic-workflow-patterns/docs/zh.md)
- [13 · 有状态图编排——持久执行与检查点](13-langgraph-stateful-graphs/docs/zh.md)
- [14 · Agent（智能体） 的 Actor 模型——异步消息与类型化运行时](14-autogen-actor-model/docs/zh.md)
- [15 · 基于角色的 Agent（智能体） 团队——角色、任务与流程](15-crewai-role-based-crews/docs/zh.md)
- [16 · OpenAI Agents SDK（软件开发工具包）：交接、护栏与追踪](16-openai-agents-sdk/docs/zh.md)
- [17 · Harness 即库——子 agent（智能体） 与会话存储](17-claude-agent-sdk/docs/zh.md)
- [18 · 生产级 Agent（智能体） 运行时——快速实例化与类型化工作流](18-agno-and-mastra-runtimes/docs/zh.md)
- [19 · 基准：SWE-bench、GAIA、AgentBench](19-benchmarks-swebench-gaia/docs/zh.md)
- [20 · 基准：WebArena 与 OSWorld](20-benchmarks-webarena-osworld/docs/zh.md)
- [21 · 计算机操作：Claude、OpenAI CUA、Gemini](21-computer-use-agents/docs/zh.md)
- [22 · 语音 Agent（智能体）：Pipecat 与 LiveKit](22-voice-agents-pipecat-livekit/docs/zh.md)
- [23 · OpenTelemetry GenAI 语义约定](23-otel-genai-conventions/docs/zh.md)
- [24 · Agent（智能体） 可观测性：Langfuse、Phoenix、Opik](24-agent-observability-platforms/docs/zh.md)
- [25 · 多 Agent（智能体） 辩论与协作](25-multi-agent-debate/docs/zh.md)
- [26 · 失败模式：agent（智能体） 为什么会坏](26-failure-modes-agentic/docs/zh.md)
- [27 · Prompt injection（提示注入）防御](27-prompt-injection-defense/docs/zh.md)
- [28 · 编排模式：Supervisor、Swarm、Hierarchical](28-orchestration-patterns/docs/zh.md)
- [29 · 生产运行时：Queue、Event、Cron](29-production-runtimes/docs/zh.md)
- [30 · 评估驱动的 Agent（智能体） 开发](30-eval-driven-agent-development/docs/zh.md)
- [31 · Agent（智能体） 工作台工程：能干的模型为什么还会失败](31-agent-workbench-why-models-fail/docs/zh.md)
- [32 · 最小 Agent（智能体） 工作台](32-minimal-agent-workbench/docs/zh.md)
- [33 · Agent（智能体） 指令即可执行约束](33-instructions-as-executable-constraints/docs/zh.md)
- [34 · 仓库记忆与持久状态](34-repo-memory-and-state/docs/zh.md)
- [35 · Agent（智能体） 初始化脚本](35-initialization-scripts/docs/zh.md)
- [36 · 范围契约与任务边界](36-scope-contracts/docs/zh.md)
- [37 · 运行时反馈循环](37-runtime-feedback-loops/docs/zh.md)
- [38 · 验证关卡](38-verification-gates/docs/zh.md)
- [39 · 审查者 Agent（智能体）：把构建者和打分者分开](39-reviewer-agent/docs/zh.md)
- [40 · 多会话交接](40-multi-session-handoff/docs/zh.md)
- [41 · 真实仓库上的工作台](41-workbench-for-real-repos/docs/zh.md)
- [42 · 综合项目：交付一个可复用的 Agent（智能体） 工作台包](42-agent-workbench-capstone/docs/zh.md)
- [43 · 在 agent（智能体） 写代码前框定任务](43-frame-the-task-before-code/docs/zh.md)
- [44 · 制定由证据支撑的执行计划](44-plan-from-evidence/docs/zh.md)
- [45 · 通过隔离与合并契约委派 agent（智能体） 工作](45-delegate-with-isolation/docs/zh.md)
- [46 · 把每次 agent（智能体） 纠正变成系统改进](46-turn-feedback-into-system/docs/zh.md)
- [47 · 在选择产出前定义结果](47-outcomes-before-output/docs/zh.md)
- [48 · 发现人们实际执行的工作流](48-discover-the-real-workflow/docs/zh.md)
- [49 · 绘制假设地图，先化解风险最高的一项](49-map-assumptions-and-risk/docs/zh.md)
- [50 · 选择能改变决定的最小可测试切片](50-choose-the-smallest-testable-slice/docs/zh.md)
- [51 · 编写保留判断空间的规格说明](51-write-specifications-that-preserve-judgment/docs/zh.md)
- [52 · 在结果出现前设计成功指标](52-design-success-metrics/docs/zh.md)
- [53 · 有意识地选择原型、试点或生产](53-prototype-pilot-or-production/docs/zh.md)
- [54 · 构建带所有权与淘汰机制的反馈棘轮](54-build-the-feedback-ratchet/docs/zh.md)
