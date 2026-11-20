# ZeRO Optimizer State 分片 · 自测

每题先选答案，再展开解析。

## 1. 为什么 ZeRO 先分片 optimizer state，而不是先分片参数？

- **A** DeepSpeed 强制要求
- **B** optimizer 更重要
- **C** 参数更好处理
- **D** optimizer state 是最大的那块内存项，而且只在 step 时才被触碰，forward 和 backward 都用不到

<details>
<summary>查看答案与解析</summary>

**答案**　D

在混合精度的 Adam 下，fp32 master 加两个动量，每个 rank 是 12P 字节，而 fp16 参数+梯度只有 4P。先分片最大的那一项，单位复杂度换来的内存收益最大。

</details>

## 2. ZeRO stage 1 每一步的线缆模式是什么？

- **A** 一次 broadcast
- **B** 对梯度做一次 reduce-scatter，外加对更新后的参数做一次 all-gather
- **C** 一次 all-reduce
- **D** 什么都没有

<details>
<summary>查看答案与解析</summary>

**答案**　B

reduce-scatter 只把各自的梯度 shard 交给对应 rank；all-gather 再把更新后的参数 shard 分发回去。总字节数与 all-reduce 相同，内存被除以 N。

</details>

## 3. 为什么每一步的带宽和 DDP 一样？

- **A** ZeRO 用了压缩
- **B** 在带宽上 all-reduce 等于 reduce-scatter 加 all-gather；ZeRO 只是把它拆成两半、作用在不同数据上
- **C** 其实并不一样
- **D** 魔法

<details>
<summary>查看答案与解析</summary>

**答案**　B

ring all-reduce 本就是 reduce-scatter 再 all-gather 实现的。ZeRO 做的是同样两个操作，只是 all-gather 轮转的是更新后的参数，而不是求和后的梯度。

</details>

## 4. 对一个 7B 模型、混合精度 Adam、8 个 rank，相比原版 DDP 内存下降多少？

- **A** 10%
- **B** 0%
- **C** 99%
- **D** 约 65%（原版 16P 对比 ZeRO-1 的 4P + 12P/N = 5.5P）

<details>
<summary>查看答案与解析</summary>

**答案**　D

原版：2P + 2P + 4P + 4P + 4P = 16P。ZeRO-1：2P + 2P + (4P+4P+4P)/8 = 5.5P。下降为 (16-5.5)/16 = 65.6%。

</details>

## 5. 相比 ZeRO-1，ZeRO-2 多做了什么？

- **A** 把后端切到 NCCL
- **B** 还会在 reduce-scatter 之后丢掉非本 shard 的梯度，释放每个 rank 的梯度内存；带宽保持不变
- **C** 什么都没多做
- **D** 去掉了 optimizer

<details>
<summary>查看答案与解析</summary>

**答案**　B

ZeRO-2 在 reduce-scatter 之后把非本 shard 的那部分梯度清零；带宽与 ZeRO-1 相同，但梯度内存更低。

</details>

## 6. 为什么 ZeRO 要求 optimizer state 的 checkpoint 记录哪个 rank 拥有哪个 shard？

- **A** 它并不需要
- **B** 没有逐 rank 的归属信息，保存的状态在重启时无法读取；在相同 world size 上恢复需要把对的 shard 放回对的 rank
- **C** 为了压缩
- **D** 纯装饰

<details>
<summary>查看答案与解析</summary>

**答案**　B

第 80 课构建分片 checkpoint 清单（manifest），正是为了让 ZeRO 运行能在相同拓扑上恢复。

</details>


[返回本课](docs/zh.md)
