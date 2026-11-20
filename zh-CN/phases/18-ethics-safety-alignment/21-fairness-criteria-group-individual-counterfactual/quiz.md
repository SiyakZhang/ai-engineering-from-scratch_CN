# 公平判据 —— 群体、个体、反事实 · 自测

每题先选答案，再展开解析。

## 1. 对于群体 A=a 和 A=a'，哪一项最符合人口统计均等（demographic parity）的定义？

- **A** 各群体的预测值（predictive value）相等
- **B** 接受率相等：P(Y=1 | A=a) = P(Y=1 | A=a')
- **C** 各群体的真阳性率和假阳性率相等
- **D** 各群体的 Lipschitz 常数相等

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 2. Chouldechova / Kleinberg-Mullainathan-Raghavan 2017 的不可能性结果说了什么？

- **A** 反事实公平蕴含人口统计均等
- **B** 群体公平总能通过重新加权来实现
- **C** 在基率不等的情况下，人口统计均等、等化几率（equalized odds）和条件使用准确率均等无法同时成立
- **D** 对任意 DAG，个体公平都蕴含反事实公平

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 3. Dwork 等人 2012 通过什么来定义个体公平（individual fairness）？

- **A** 一个带敏感属性干预的因果 DAG
- **B** 决策映射相对于一个任务专属相似度度量满足 Lipschitz 条件，使相似的个体得到相似的决策
- **C** 个体层面的人口统计均等
- **D** 跨受保护群体的准确率相等

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 4. 反事实公平（Kusner 等人 2017）要求：

- **A** 仅群体层面的统计量
- **B** 无需任何因果假设
- **C** 所有群体的 Lipschitz 常数相等
- **D** 一个因果 DAG；当个体的敏感属性被反事实地改变时，决策保持不变

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 5. 为什么回溯反事实（backtracking counterfactuals，arXiv:2401.13935）对法律合规很重要？

- **A** 它们不在受保护属性上做干预（那在法律上有问题），而是追问：哪一组实际特征本会产生该反事实结果
- **B** 它们取代了基于嵌入的偏见度量
- **C** 它们消除了对任何因果模型的需求
- **D** 它们证明了不可能性定理是错的

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 6. ICLR Blogposts 2024 的哲学性调和论点是什么？

- **A** 不可能性定理可通过重新加权来化解
- **B** 在有显式因果图的情况下，满足某些群体公平度量就蕴含反事实公平，因此两类之间看似的对立，部分是因为让因果模型保持隐式而造成的假象
- **C** 只有个体公平是站得住脚的
- **D** 群体公平与反事实公平互不相关

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>


[返回本课](docs/zh.md)
