# A/B 测试 LLM 特性 —— GrowthBook、Statsig 与"凭感觉"问题 · 自测

每题先选答案，再展开解析。

## 1. 本课中，评测（evals）与 A/B 测试的精确区别是什么？

- **A** 评测面向用户；A/B 测试在离线进行
- **B** 它们可以互换
- **C** 只需要 A/B 测试
- **D** 评测在带标注的数据集上回答「模型能否胜任这项工作？」；A/B 测试用线上随机化流量回答「用户是否在意？」

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 2. CUPED 为一项实验做了什么？

- **A** 通过招募更多用户来增大样本量
- **B** 禁用多重比较校正
- **C** 完全替代序贯检验
- **D** 在比较实验后期之前，先回归剔除实验前期的方差，通常能把方差降低 30-70% 并提升有效样本量

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 3. 为什么在跑很多 A/B 测试时需要多重比较校正（Bonferroni 或 Benjamini-Hochberg）？

- **A** 它们是 GDPR 的要求
- **B** 在 95% 置信度下跑 20 个测试，会因偶然产生一个假阳性；校正可控制族系误差率（family-wise error）或错误发现率（false discovery rate）
- **C** 它们只在序贯检验时才需要
- **D** 它们能加快实验

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 4. SRM（样本比例失配，sample ratio mismatch）能检测什么？

- **A** 实验平台的内存泄漏
- **B** 分配哈希的 bug 导致实际投放的切分偏离了预期（例如目标 50/50 却出现 47/53）
- **C** PII 泄露
- **D** Tokenizer 性能缓慢

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 5. 为什么 LLM 的非确定性需要为样本量预留缓冲？

- **A** 非确定性会减少所需样本量
- **B** 它只在离线时才重要
- **C** 它与功效（power）计算无关
- **D** 它违反了 IID 假设；有效样本量下降，因此要把所需样本量乘以约 1.3-1.5 倍作为安全裕度

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 6. 本课如何对比 Statsig 和 GrowthBook？

- **A** GrowthBook 是闭源的
- **B** Statsig 仅支持数仓原生（warehouse-native）
- **C** 功能集完全相同
- **D** Statsig 是一体化 SaaS（2025 年 9 月被 OpenAI 以 11 亿美元收购）；GrowthBook 是 MIT 开源、数仓原生，具备贝叶斯/频率派/序贯引擎以及 CUPED/SRM/BH

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>


[返回本课](docs/zh.md)
