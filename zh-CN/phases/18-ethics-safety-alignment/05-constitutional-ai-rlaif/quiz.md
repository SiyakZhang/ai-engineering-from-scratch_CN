# Constitutional AI 与 RLAIF · 自测

每题先选答案，再展开解析。

## 1. 相比标准 RLHF，宪法式 AI（Constitutional AI）的核心替换是什么？

- **A** 它完全移除了奖励模型
- **B** 它用 DPO 替换 PPO
- **C** 它用合成 prompt 替换真实 prompt
- **D** 它用一个会阅读一系列原则的 AI 标注者来替换人类偏好标注者

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 2. 宪法式 AI 的第一（SFT）阶段做什么？

- **A** 通过对标注者评论聚类来生成合成原则
- **B** 用宪法派生的奖励进行 PPO
- **C** 生成初始响应，依据一条采样到的宪法原则对其进行批判，然后修订，并把修订结果用作 SFT 目标
- **D** 仅在 AI 生成的偏好上训练一个奖励模型

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 3. 第二（RLAIF）阶段做什么？

- **A** 把宪法蒸馏进 tokenizer
- **B** 让人类重新标注 SFT 的输出
- **C** 用反馈模型产生的 AI 生成偏好训练一个奖励模型，并据此运行 PPO
- **D** 跳过 PPO，只施加单一的监督损失

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 4. 在 Anthropic 2026 年 1 月的四层 Claude 宪法中，各层的顺序是什么？

- **A** 避免灾难性后果 > 遵循 Anthropic 准则 > 广义合乎伦理 > 有用且坦诚
- **B** 平台规则 > 避免灾难 > 有用 > 广义合乎伦理
- **C** 有用 > 广义合乎伦理 > 平台规则 > 避免灾难
- **D** 广义合乎伦理 > 有用 > 平台规则 > 避免灾难

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 5. 从 RLHF 切换到 RLAIF 并不一定能修复哪种失败模式？

- **A** 标注者心理上的不一致
- **B** 标注者稀缺
- **C** 奖励黑客 / 古德哈特定律
- **D** 标注者成本

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 6. 宪法分类器（Constitutional Classifiers）v1 与 v2（2026）之间最主要的变化是什么？

- **A** v2 只作用于输入，不作用于输出
- **B** v2 移除了分类器，仅依赖宪法
- **C** v2 把计算开销从 23.7% 降到约 1%，同时保持较低的攻击成功率
- **D** v2 把计算开销从 1% 提升到 23.7%

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>


[返回本课](docs/zh.md)
