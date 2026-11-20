# 阶段 10：从零构建 LLM

> 构建、训练并理解大语言模型。

## 在 GitHub 上开始本阶段

**前置要求：** 阶段 5 的 NLP 基础。开始模型构建课程前，强烈建议先学阶段 7 的 Transformer。

**第一课：** [分词器](01-tokenizers/docs/zh.md)

从仓库根目录运行：

```bash
python3 phases/10-llms-from-scratch/01-tokenizers/code/main.py
```

记录命令、退出码、编码/解码往返结果、已学习的合并次数和压缩率。`tiktoken` 是可选的对照工具。

**下一步：** 加入一个微型语料从未见过的词，检查它被切成的片段，然后继续学习[从零构建分词器](02-building-a-tokenizer/docs/zh.md)。

浏览[阶段 10 的完整课程列表](../../README.md#phase-10)或[跨阶段路线图](../../ROADMAP.md)。

## 本阶段中文课文

- [01 · tokenizer（分词器）：BPE（字节对编码）、WordPiece、SentencePiece](01-tokenizers/docs/zh.md)
- [02 · 从零构建一个 tokenizer（分词器）](02-building-a-tokenizer/docs/zh.md)
- [03 · pretraining（预训练）的数据流水线](03-data-pipelines/docs/zh.md)
- [04 · pretraining（预训练）一个 Mini GPT（1.24 亿参数）](04-pre-training-mini-gpt/docs/zh.md)
- [05 · 规模化：分布式训练、FSDP（全分片数据并行）、DeepSpeed](05-scaling-distributed/docs/zh.md)
- [06 · 指令微调（SFT）](06-instruction-tuning-sft/docs/zh.md)
- [07 · RLHF（基于人类反馈的强化学习）：奖励模型 + PPO（近端策略优化）](07-rlhf/docs/zh.md)
- [08 · DPO（直接偏好优化）：直接偏好优化](08-dpo/docs/zh.md)
- [09 · Constitutional AI 与自我改进](09-constitutional-ai-self-improvement/docs/zh.md)
- [10 · 评估：基准、eval、LM Harness](10-evaluation/docs/zh.md)
- [11 · 量化：把模型塞进去](11-quantization/docs/zh.md)
- [12 · 推理优化](12-inference-optimization/docs/zh.md)
- [13 · 构建一条完整的 LLM（大语言模型） 流水线](13-building-complete-llm-pipeline/docs/zh.md)
- [14 · 开放模型：架构走读](14-open-models-architecture-walkthroughs/docs/zh.md)
- [15 · 推测解码与 EAGLE-3](15-speculative-decoding-eagle3/docs/zh.md)
- [16 · 差分注意力（V2）](16-differential-attention-v2/docs/zh.md)
- [17 · 原生稀疏注意力（DeepSeek NSA）](17-native-sparse-attention/docs/zh.md)
- [18 · 多 token（词元） 预测（MTP）](18-multi-token-prediction/docs/zh.md)
- [19 · DualPipe 并行](19-dualpipe-parallelism/docs/zh.md)
- [20 · DeepSeek-V3 架构走读](20-deepseek-v3-walkthrough/docs/zh.md)
- [21 · Jamba —— 混合 SSM-Transformer](21-jamba-hybrid-ssm-transformer/docs/zh.md)
- [22 · 异步与 Hogwild! 推理](22-async-hogwild-inference/docs/zh.md)
- [25 · 推测解码与 EAGLE](25-speculative-decoding/docs/zh.md)
- [34 · 梯度检查点与激活重算](34-gradient-checkpointing/docs/zh.md)
