# 端到端分布式训练 · 自测

每题先选答案，再展开解析。

## 1. 既然每节课都已经有自己的测试，为什么还需要一个顶点项目？

- **A** 更好评分
- **B** 更慢
- **C** 装饰
- **D** 组合是一项独立的性质：各部件可以都通过单元测试，但集成起来却死锁、loss 发散，或者一起跑时内存增长

<details>
<summary>查看答案与解析</summary>

**答案**　D

端到端测试能抓住任何单独部件测不出的接线 bug：rendezvous、barrier 顺序、gather 契约。

</details>

## 2. 这个 demo 校验哪四条不变量？

- **A** 硬件
- **B** 速度
- **C** 每秒 token 数
- **D** (a) loss 跑到第 20 步无 NaN，(b) 每个 rank 的参数范数一致，(c) 每个 rank 的 optimizer 内存符合 ZeRO-1 公式，(d) 第 10 步的 checkpoint 重新加载后字节相等

<details>
<summary>查看答案与解析</summary>

**答案**　D

每条不变量抓一类不同的组合 bug：NaN 抓发散，范数一致抓同步漂移，内存抓分片 bug，checkpoint 抓写入原子性。

</details>

## 3. 为什么模型用一个微型 GPT 而不是 MLP？

- **A** 显得高级
- **B** 更快
- **C** 必需
- **D** GPT 引入了 LayerNorm 的运行统计量、embedding 梯度形状，以及 softmax+cross-entropy 的边界情况，这些是 MLP 会掩盖掉的

<details>
<summary>查看答案与解析</summary>

**答案**　D

MLP 的梯度同步在第 77 课已经验证过了；顶点项目需要一个边界情况更多的模型，来证明组合在真实算子下成立。

</details>

## 4. 在这个语境里「自终止」是什么意思？

- **A** 手动
- **B** 固定步数（20）、完成后 exit 0、无人值守；如果任何部件死锁，demo 永不返回，CI 就能抓到
- **C** 进程把自己杀掉
- **D** 崩溃恢复

<details>
<summary>查看答案与解析</summary>

**答案**　B

一个有界、以 exit 0 结束的运行让测试装置能断言终止；while-True 循环会掩盖死锁。

</details>

## 5. 这个 demo 是怎么把 DDP 和 ZeRO 结合起来的？

- **A** 用 DDP 风格的 init 时 broadcast 做参数同步，用 ZeRO-1 的 reduce-scatter+all-gather 替换 optimizer.step；DDP 的梯度 all-reduce 被吸收进 ZeRO 的 reduce-scatter
- **B** 只用 DDP
- **C** 两者同时
- **D** 只用 ZeRO

<details>
<summary>查看答案与解析</summary>

**答案**　A

ZeRO-1 通过 reduce-scatter 掌管梯度同步，所以 DDP 单独的 all-reduce 就不需要了；init 时的 broadcast 是唯一存活下来的 DDP 专属调用。

</details>

## 6. 为什么生产环境用挂钟（wall-clock）的 checkpoint 节奏，而不是步数？

- **A** 看着更干净
- **B** NCCL 要求
- **C** 步耗时会随序列长度和 microbatch 数量变化；10 分钟一次的节奏不论模型大小都对应相同的算力
- **D** 更快

<details>
<summary>查看答案与解析</summary>

**答案**　C

本课为了清晰用基于步数的方式；生产运行通常每 5-15 分钟挂钟时间保存一次。

</details>


[返回本课](docs/zh.md)
