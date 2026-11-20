# 实验执行器 · 自测

每题先选答案，再展开解析。

## 1. 为什么 runner 用子进程而不是在进程内 import 实验脚本？

- **A** 因为独立进程给了 runner 一个超时或内存限制时的 kill 句柄，并且把崩溃隔离在编排器之外
- **B** 因为 subprocess 比 import 更快
- **C** 因为 metrics 格式要求这样做
- **D** 因为 Python 不允许嵌套 import

<details>
<summary>查看答案与解析</summary>

**答案**　A

独立进程是语言自带的最简单的隔离方式。父进程保留了 kill 句柄和独立的地址空间，崩溃的实验不会把编排器一起拖垮。

</details>

## 2. 为什么内存上限被描述为「软」的？

- **A** 因为 numpy 忽略这个限制
- **B** 因为操作系统总是会覆盖它
- **C** 因为它只限制堆，不限制栈
- **D** 因为轮询器有一个非零间隔——进程可以在两次轮询之间短暂飙到上限以上，runner 要到下次观测才能采取行动

<details>
<summary>查看答案与解析</summary>

**答案**　D

上限是通过轮询而不是内核级限制来执行的。轮询间隔就是上限的精度，短暂的峰值可以在下次观测前短暂超过上限。

</details>

## 3. 当 stdout 中有 metrics 但退出码非零时，runner 返回哪个终态标签？

- **A** oom
- **B** ok
- **C** crash
- **D** timeout

<details>
<summary>查看答案与解析</summary>

**答案**　C

终态为 ok 的条件是退出码为零且 metrics 解析成功。退出码非零就是 crash，即使在失败前已经捕获了一些 metrics。

</details>

## 4. runner 如何从 stdout 中识别最终的 metrics blob？

- **A** 读取最后一行能解析为 JSON 且 key 覆盖了所有必需 metric_keys 的行；更早的覆盖行成为中间 metrics
- **B** 扫描 stderr 中的 JSON
- **C** 读取第一行 JSON
- **D** 期望输出恰好只有一行

<details>
<summary>查看答案与解析</summary>

**答案**　A

最终 metrics 是最后一行能解析为 JSON 且包含所有必需 key 的行。更早的覆盖行被保留为中间 metrics，用于学习曲线。

</details>

## 5. 为什么 ablation 辅助函数逐个旋钮扫描，而不是做全因子组合？

- **A** 因为单旋钮扫描能产出评估器可以绘制的干净维度，而全因子组合按指数级爆炸且难以解读
- **B** 因为 runner 无法启动多个子进程
- **C** 因为种子只沿一个旋钮变化
- **D** 因为 numpy 不支持笛卡尔积

<details>
<summary>查看答案与解析</summary>

**答案**　A

单旋钮扫描保持结果可解读。全因子组合的成本随旋钮数量指数增长，结果表格也难以阅读。

</details>

## 6. 把 spec.seed 传入 config['__seed'] 给了评估器什么保证？

- **A** 确定性——用相同种子重跑产生相同 metrics，评估器就能分辨真实变化和随机噪声
- **B** 更快的执行时间
- **C** 免费的显著性检验
- **D** 更低的内存消耗

<details>
<summary>查看答案与解析</summary>

**答案**　A

种子锁定了实验中的随机初始化。用相同种子的两次运行产生相同 metrics，这是评估器区分真实退步和不同随机抽样的基础。

</details>


[返回本课](docs/zh.md)
