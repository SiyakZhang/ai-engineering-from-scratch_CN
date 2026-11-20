# leaderboard 聚合 · 自测

每题先选答案，再展开解析。

## 1. 为什么聚合器要求每个输入分数都落在 [0, 1] 区间？

- **A** Numpy 要求如此
- **B** Markdown 渲染期望两位小数
- **C** 这是 ECE 的 bin 范围
- **D** 没有统一的尺度，某个范围在 0-100 的 metric 就会主导每个模型的均值

<details>
<summary>查看答案与解析</summary>

**答案**　D

如果通过率在 [0,1]、BLEU 在 [0,100]，后者会把均值压垮。归一化应当在 metric 层完成，并在这里做检查。

</details>

## 2. 均值分数隐藏了哪些信息，而 win-rate 能暴露出来？

- **A** 模型是否校准良好
- **B** bootstrap 区间
- **C** 完成的任务数量
- **D** 逐任务的胜场能抗住离群点和尺度漂移；均值对两者都敏感

<details>
<summary>查看答案与解析</summary>

**答案**　D

win-rate 一项项数任务的胜场。一个模型可能靠一道简单任务拿到高均值，却在大多数两两比较里都输。

</details>

## 3. bootstrap_mean_ci 是如何估计置信区间的？

- **A** 用解析方式算标准差
- **B** 假定均值服从正态分布
- **C** 对任务分数有放回地重采样，对每个采样算均值，再取 alpha/2 和 1 - alpha/2 的百分位
- **D** 调用 scipy.stats.bootstrap

<details>
<summary>查看答案与解析</summary>

**答案**　C

对逐任务分数做非参数百分位 bootstrap；不做分布假设，不用 scipy。

</details>

## 4. 两两差值的 CI 在什么时候报告 `significant`？

- **A** 当两者 win-rate 不相等时
- **B** 当 CI 不包含零时
- **C** 当两个模型都有超过三十个任务时
- **D** 当均值差大于 0.1 时

<details>
<summary>查看答案与解析</summary>

**答案**　B

一个严格不含零的 CI 意味着在所选水平下差异不太可能为零；这就是本课采用的可操作定义。

</details>

## 5. 为什么两两 bootstrap 是配对（paired）的，而不是独立的？

- **A** 独立 bootstrap 在 Python 里非法
- **B** 配对 bootstrap 是 numpy 唯一支持的
- **C** 配对 bootstrap 尊重「同一个任务同时喂给两个模型」这一点；差值是在重采样之前逐任务算出来的
- **D** 配对 bootstrap 跑得更快

<details>
<summary>查看答案与解析</summary>

**答案**　C

配对 bootstrap 能降噪：我们是在任务上采样，而不是在模型上采样，所以每一轮迭代比较的都是同一套任务集。

</details>

## 6. 为什么聚合器在给出头条数字的同时，还要返回各 category 的均值？

- **A** 分 category 的均值比整体均值跑得更快
- **B** 头条均值可能掩盖某个 category 上的弱点（整体好、代码差）；分 category 能把这暴露出来
- **C** Markdown 渲染需要它
- **D** JSON Schema 要求如此

<details>
<summary>查看答案与解析</summary>

**答案**　B

一个模型在总分上胜出，可能是因为处处都还行，也可能是因为在某个 category 上碾压。分 category 拆解能让消费者看清是哪一种。

</details>


[返回本课](docs/zh.md)
