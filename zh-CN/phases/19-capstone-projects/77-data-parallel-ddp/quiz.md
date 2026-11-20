# 数据并行 DDP · 自测

每题先选答案，再展开解析。

## 1. 为什么 DDP 在构造时 broadcast 参数，而不是靠各 rank 用同一个 seed？

- **A** PyTorch 禁止同 seed 初始化
- **B** broadcast 比设种子更快
- **C** broadcast 省内存
- **D** 同 seed 初始化会在各 rank 间漂移到浮点 epsilon 级别；broadcast 能保证训练开始前各处权重字节相等

<details>
<summary>查看答案与解析</summary>

**答案**　D

不同硬件（甚至不同进程顺序）上的浮点运算可能在比特级别有差异。从 rank 0 做一次 broadcast 是让各处权重字节相等的唯一办法。

</details>

## 2. 在 backward 之后、optimizer.step 之前，DDP 做了什么？

- **A** 什么都不做
- **B** broadcast logits
- **C** 存一个 checkpoint
- **D** 对每个参数的梯度做 all-reduce-SUM，再除以 world_size 得到平均梯度

<details>
<summary>查看答案与解析</summary>

**答案**　D

平均梯度对 world_size 不变，所以在单 rank 上调好的学习率在 N 个 rank 上同样适用。

</details>

## 3. 为什么是 all-reduce-SUM 之后再除以 world_size，而不直接用 all-reduce-MEAN？

- **A** world_size 未知
- **B** 在每个 rank 上除以 world_size 是本地运算；all-reduce-MEAN 底层其实也是这么实现的
- **C** 除法会产生 NaN
- **D** gloo 里没有 all-reduce-MEAN

<details>
<summary>查看答案与解析</summary>

**答案**　B

两种做法算术结果一样。NCCL 从 2.10 起带了 all-reduce-AVG，gloo 没有，所以 SUM 之后本地除。

</details>

## 4. 生产级 DDP 里的梯度分桶（gradient bucketing）达到了什么效果？

- **A** 释放梯度内存
- **B** 跳过 backward
- **C** 把梯度量化到 int8
- **D** 把许多小的 all-reduce 合并成一个大的 all-reduce，摊薄每次调用的延迟底线

<details>
<summary>查看答案与解析</summary>

**答案**　D

一个 10 亿参数的模型有上千个梯度张量；每个张量做一次 all-reduce，就要把 gloo 或 NCCL 的延迟付上千遍。

</details>

## 5. PyTorch DDP 里为什么会有 no_sync()？

- **A** 用来调试
- **B** 跨 K 个 microbatch 做梯度累积时，需要对其中 K-1 个跳过 backward 后的 all-reduce；no_sync 把这段暂停包起来
- **C** 用来关掉 DDP
- **D** 用来切换后端

<details>
<summary>查看答案与解析</summary>

**答案**　B

没有 no_sync，每个累积步里 all-reduce 会触发 K 次，吞吐量跌到底线。

</details>

## 6. 为什么本课的参考实现在单进程里顺序地走完每个 rank 的 micro-batch？

- **A** 它给出一个字节相等的基线：顺序计算的平均梯度必须在每一步都等于 DDP all-reduce 后的平均梯度
- **B** 它省内存
- **C** 单进程更快
- **D** 这是用 gloo 的唯一方式

<details>
<summary>查看答案与解析</summary>

**答案**　A

与参考循环等价是承重的正确性测试；没有它，梯度同步的 bug 会一直藏到第 10000 步。

</details>


[返回本课](docs/zh.md)
