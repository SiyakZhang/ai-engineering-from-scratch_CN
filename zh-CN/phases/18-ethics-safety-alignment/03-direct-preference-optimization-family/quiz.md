# 直接偏好优化家族 · 自测

每题先选答案，再展开解析。

## 1. 为什么 DPO 可以跳过训练一个显式的奖励模型？

- **A** RLHF 的闭式最优解让你能把奖励表示为策略的对数比值，再代入 Bradley-Terry 损失
- **B** Bradley-Terry 偏好恰好对奖励函数不变
- **C** DPO 在第二个优化循环中隐式地训练自己的奖励模型
- **D** 偏好数据不需要标量奖励

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 2. IPO（Azar 等人，2024）主要解决 DPO 中的哪种失败模式？

- **A** 被选中响应的长度偏置
- **B** 对参考策略的依赖
- **C** 由极小的偏好概率导致的无界隐式奖励差距
- **D** 对成对数据的需求

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 3. 什么时候你会选择 KTO 而非 DPO？

- **A** 当你想完全移除 KL 惩罚时
- **B** 当你拥有未配对的单一标签（可取 / 不可取），并想使用损失厌恶（loss-aversion）效用时
- **C** 当你必须保证零隐式奖励漂移时
- **D** 当你只有具有强 margin 的成对数据时

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 4. 与 DPO 相比，SimPO 独有的特性是哪一项？

- **A** 它移除了参考策略，并按序列长度对对数似然进行归一化
- **B** 它使用带 NLL 的赔率比（odds-ratio）损失
- **C** 它保留参考策略并增加一个 margin
- **D** 它把 Bradley-Terry 的 log-sigmoid 换成了恒等映射

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 5. BPO 针对的、DPO 中的「被选中响应退化（Degraded Chosen Response）」问题是什么？

- **A** 被选中响应不在参考策略的支撑集（support）中
- **B** 被选中响应在推理时以低概率被采样
- **C** 被选中响应变得比被拒绝响应更长
- **D** 只要被拒绝响应的对数概率下降得更快，DPO 就可能把被选中响应的绝对对数概率也压低

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 6. Rafailov 等人（NeurIPS 2024）关于直接对齐算法（DAA）缩放律的研究表明：

- **A** 当成对数据超过 10 万条样本时，过度优化就消失了
- **B** 在黄金奖励上，DAA 表现出与 Gao 等人相同的「先升后崩」的过度优化形态
- **C** DAA 在设计上消除了古德哈特问题
- **D** DPO 会过度优化，但 IPO 和 SimPO 不会

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>


[返回本课](docs/zh.md)
