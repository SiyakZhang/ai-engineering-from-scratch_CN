# 阶段 18：伦理、安全与对齐

> 构建帮助人类的 AI。这不是可选项。

## 在 GitHub 上开始本阶段

**前置要求：** 阶段 10 的第 06、07、08 课，分别涉及 SFT、RLHF 和 DPO。

**第一课：** [把遵循指令作为对齐信号](01-instruction-following-alignment-signal/docs/zh.md)

从仓库根目录运行：

```bash
python3 phases/18-ethics-safety-alignment/01-instruction-following-alignment-signal/code/main.py
```

记录命令、退出码、使用与不使用 KL 惩罚的策略、奖励和 KL 轨迹，以及一句指出你观察到的代理目标失效。

**下一步：** 改变 KL 系数，预测策略漂移，然后继续学习[奖励黑客与古德哈特定律](02-reward-hacking-goodhart/docs/zh.md)。

浏览[阶段 18 的完整课程列表](../../README.md#phase-18)或[跨阶段路线图](../../ROADMAP.md)。

## 本阶段中文课文

- [01 · 把「遵循指令」当作对齐信号](01-instruction-following-alignment-signal/docs/zh.md)
- [02 · 奖励作弊与古德哈特定律](02-reward-hacking-goodhart/docs/zh.md)
- [03 · DPO（直接偏好优化）家族](03-direct-preference-optimization-family/docs/zh.md)
- [04 · 阿谀奉承：RLHF（基于人类反馈的强化学习） 的放大效应](04-sycophancy-rlhf-amplification/docs/zh.md)
- [05 · Constitutional AI 与 RLAIF](05-constitutional-ai-rlaif/docs/zh.md)
- [06 · Mesa 优化与欺骗性对齐](06-mesa-optimization-deceptive-alignment/docs/zh.md)
- [07 · Sleeper agents（潜伏行为）与分布外评估](07-sleeper-agents-persistent-deception/docs/zh.md)
- [08 · 前沿模型中的上下文阴谋](08-in-context-scheming-frontier-models/docs/zh.md)
- [09 · 对齐伪装](09-alignment-faking/docs/zh.md)
- [10 · AI 控制 —— 哪怕被颠覆也要保安全](10-ai-control-subversion/docs/zh.md)
- [11 · 可扩展监督与弱到强泛化](11-scalable-oversight-weak-to-strong/docs/zh.md)
- [12 · PAIR 与自动化红队评估](12-red-teaming-pair-automated-attacks/docs/zh.md)
- [13 · Many-shot jailbreaking（多示例越狱）的评估](13-many-shot-jailbreaking/docs/zh.md)
- [14 · ASCII art（字符画）与多模态内容审核](14-ascii-art-visual-jailbreaks/docs/zh.md)
- [15 · Indirect prompt injection（间接提示注入）](15-indirect-prompt-injection/docs/zh.md)
- [16 · Garak、Llama Guard 与 PyRIT 在安全评估中的分工](16-red-team-tooling-garak-llamaguard-pyrit/docs/zh.md)
- [17 · WMDP 与两用能力评估](17-wmdp-dual-use-evaluation/docs/zh.md)
- [18 · 前沿安全框架 —— RSP、PF、FSF](18-frontier-safety-frameworks-rsp-pf-fsf/docs/zh.md)
- [19 · Anthropic 的模型福祉项目](19-model-welfare-research/docs/zh.md)
- [20 · LLM（大语言模型） 中的偏见与表征性危害](20-bias-representational-harm/docs/zh.md)
- [21 · 公平判据 —— 群体、个体、反事实](21-fairness-criteria-group-individual-counterfactual/docs/zh.md)
- [22 · 面向 LLM（大语言模型） 的差分隐私](22-differential-privacy-for-llms/docs/zh.md)
- [23 · 水印 —— SynthID、Stable Signature、C2PA](23-watermarking-synthid-stable-signature-c2pa/docs/zh.md)
- [24 · 监管框架 —— 欧盟、美国、英国、韩国](24-regulatory-frameworks-eu-us-uk-korea/docs/zh.md)
- [25 · EchoLeak 与 AI 应用的权限边界](25-echoleak-cves-for-ai/docs/zh.md)
- [26 · 模型卡、系统卡与数据集卡](26-model-system-dataset-cards/docs/zh.md)
- [27 · 数据溯源与训练数据治理](27-data-provenance-training-governance/docs/zh.md)
- [28 · 对齐研究生态 —— MATS、Redwood、Apollo、METR](28-alignment-research-ecosystem/docs/zh.md)
- [29 · 审核系统 —— OpenAI、Perspective、Llama Guard](29-moderation-systems-openai-perspective-llamaguard/docs/zh.md)
- [30 · 两用风险 —— 网络、生物、化学、核能力提升](30-dual-use-risk-cyber-bio-chem-nuclear/docs/zh.md)
