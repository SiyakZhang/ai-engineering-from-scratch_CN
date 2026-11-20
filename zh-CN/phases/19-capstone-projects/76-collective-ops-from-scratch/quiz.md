# 从零实现集合通信 · 自测

每题先选答案，再展开解析。

## 1. 在 N 个 rank 上，对一个 T 字节的张量做 ring all-reduce，每个 rank 的带宽开销是多少？

- **A** 2T(N-1)/N 字节
- **B** T 字节
- **C** T log2(N) 字节
- **D** N * T 字节

<details>
<summary>查看答案与解析</summary>

**答案**　A

ring all-reduce 把 N-1 个大小为 T/N 的 chunk 搬运两遍（先 reduce-scatter 再 all-gather）；每个 rank 的总量是 2T(N-1)/N，与集群规模无关。

</details>

## 2. 为什么本课的队列网格（queue mesh）是真实集群上 NCCL 的一个诚实替身？

- **A** 它用硬件卸载来做 reduce
- **B** 它实现了相同的线缆模式（沿 ring 有序点对点发送），只是介质不同
- **C** 它压缩消息
- **D** 它跑在 CUDA core 上

<details>
<summary>查看答案与解析</summary>

**答案**　B

算法正确性取决于线缆模式而非介质；队列 ring 暴露出的竞态形态和 chunk 调度与 NCCL ring all-reduce 完全一样。

</details>

## 3. ring all-reduce 的 reduce-scatter 这一半结束后，rank r 手里拿着什么？

- **A** 某一个 chunk 的归约和（张量的 1/N）
- **B** 两个 chunk 的归约和
- **C** 什么都没有
- **D** 未归约的完整张量

<details>
<summary>查看答案与解析</summary>

**答案**　A

reduce-scatter 把某个 chunk 的和停放在某个 rank 上；接着 all-gather 那一半把这些已完成的 chunk 沿 ring 轮转开来。

</details>

## 4. 为什么用树形 broadcast，而不是从源头发 N-1 次直连发送？

- **A** 直连发送会丢包
- **B** 树用更少内存
- **C** PyTorch 里树是强制的
- **D** 树每一轮把持有者集合翻倍；深度是 log2(N)，所以延迟按 log 而非 N 增长

<details>
<summary>查看答案与解析</summary>

**答案**　D

当每跳延迟是瓶颈时，log2(N) 跳数占主导；N-1 次串行发送要把这个延迟底线付上 N 遍。

</details>

## 5. 为什么要在相同输入上对照 torch.distributed 的 gloo 做校验？

- **A** gloo 是集合通信语义的合法参照；字节相等的输出能在真上集群之前证明你的算法符合规范
- **B** gloo 不用任何 setup
- **C** gloo 会自动写 JSONL
- **D** gloo 更快

<details>
<summary>查看答案与解析</summary>

**答案**　A

没有参照，这个原语看起来一直对，直到真实训练的第 10000 步才出岔子；gloo 在 CPU 上给出字节相等的事实基准。

</details>

## 6. 树形 all-reduce 在什么情况下胜过 ring all-reduce？

- **A** 消息很大时
- **B** 总是
- **C** 永远不会
- **D** 小消息或高延迟链路时；在交叉点以下，log2(N) 的跳数会击败带宽项 2T(N-1)/N

<details>
<summary>查看答案与解析</summary>

**答案**　D

NCCL 在约 1 MB 以上选 ring、以下选树；交叉点取决于给定集群拓扑上的带宽与延迟之争。

</details>


[返回本课](docs/zh.md)
