# 阶段 11：LLM 工程

> 让 LLM 在生产应用中真正干活。

## 在 GitHub 上开始本阶段

**前置要求：** 阶段 10 的第 01 至 05 课，或具备等价的分词、数据管线、预训练和扩展知识。

**第一课：** [提示词工程](01-prompt-engineering/docs/zh.md)

从仓库根目录运行：

```bash
python3 phases/11-llm-engineering/01-prompt-engineering/code/prompt_engineering.py
```

记录命令、退出码、生成的 prompt 元数据、测试结果，以及一次 prompt 改动及其造成的输出差异。该演示使用模拟模型响应，无需 API key。

**下一步：** 解释哪个 prompt 变量改变了行为及其原因，然后继续学习[Few-Shot、Chain-of-Thought 与 Tree-of-Thought](02-few-shot-cot/docs/zh.md)。

浏览[阶段 11 的完整课程列表](../../README.md#phase-11)或[跨阶段路线图](../../ROADMAP.md)。

## 本阶段中文课文

- [01 · Prompt Engineering（提示词工程）：技巧与模式](01-prompt-engineering/docs/zh.md)
- [02 · 少样本提示、思维链与思维树](02-few-shot-cot/docs/zh.md)
- [03 · 结构化输出：JSON、Schema 校验、约束解码](03-structured-outputs/docs/zh.md)
- [04 · 嵌入（embedding）与向量表示](04-embeddings/docs/zh.md)
- [05 · Context Engineering（上下文工程）：窗口、预算、记忆与检索](05-context-engineering/docs/zh.md)
- [06 · RAG（检索增强生成）](06-rag/docs/zh.md)
- [07 · 进阶 RAG（分块、重排、混合搜索）](07-advanced-rag/docs/zh.md)
- [08 · 用 LoRA（低秩适配） 和 QLoRA fine-tuning（微调）](08-fine-tuning-lora/docs/zh.md)
- [09 · Function Calling（函数调用） 与 Tool Use（工具使用）](09-function-calling/docs/zh.md)
- [10 · 评估与测试 LLM（大语言模型） 应用](10-evaluation/docs/zh.md)
- [11 · 缓存、限流与成本优化](11-caching-cost/docs/zh.md)
- [12 · 护栏、安全与内容过滤](12-guardrails/docs/zh.md)
- [13 · 构建一个生产级 LLM（大语言模型） 应用](13-production-app/docs/zh.md)
- [14 · MCP（模型上下文协议）](14-model-context-protocol/docs/zh.md)
- [15 · Prompt（提示词） Caching 与上下文缓存](15-prompt-caching/docs/zh.md)
- [16 · Agent（智能体） 状态机——图、节点与检查点](16-langgraph-state-machines/docs/zh.md)
- [17 · Agent（智能体） 框架取舍——图、角色与 Actor 编排](17-agent-framework-tradeoffs/docs/zh.md)
