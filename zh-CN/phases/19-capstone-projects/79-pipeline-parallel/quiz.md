# Pipeline Parallel 与 Bubble 分析 · 自测

每题先选答案，再展开解析。

## 1. 什么是 pipeline bubble？

- **A** 流水线首尾的空闲时间：在第一个 microbatch 到达之前各 stage 无活可干，以及最后一个 microbatch 离开之后
- **B** 一个网络数据包
- **C** NCCL 里的一个 bug
- **D** 内存泄漏

<details>
<summary>查看答案与解析</summary>

**答案**　A

有 M 个 microbatch、N 个 stage 时，每 stage 的 bubble 是 (N-1)/(M+N-1)。让 M 远大于 N 就能把它压小。

</details>

## 2. 为什么 GPipe 的激活内存与 M 成正比？

- **A** 硬件限制
- **B** Bug
- **C** 所有 M 个 microbatch 的激活都得保留到对应的 backward；在排空（drain）开始之前什么都不会释放
- **D** 编译器限制

<details>
<summary>查看答案与解析</summary>

**答案**　C

GPipe 在任何 backward 之前先把所有 forward 灌满流水线。每个在飞的 microbatch 都带着它的激活，直到它的 backward 启动。

</details>

## 3. 1F1B 相比 GPipe 改进在哪？

- **A** 更高的吞吐量
- **B** bubble 相同但激活内存有界；一旦 mb 0 的 forward 到达最后一个 stage，它的 backward 就开始、激活随之释放
- **C** 更低的 bubble
- **D** 更小的模型

<details>
<summary>查看答案与解析</summary>

**答案**　B

Megatron-LM 和 PipeDream 用 1F1B 把激活内存的上界从 microbatch 数量改为流水线深度。

</details>

## 4. 为什么各 stage 的算力相等比参数量相等更重要？

- **A** 最慢的那个 stage 卡住每一个周期，其他 stage 都得空等它。embedding 层参数很多但算力很小，所以按参数量切分会让流水线失衡
- **B** 内存对齐
- **C** 更好写代码
- **D** 美观

<details>
<summary>查看答案与解析</summary>

**答案**　A

Megatron-LM 暴露 --num-layers-per-stage 为一个列表，好在每层开销不同的时候允许不均匀的层数。

</details>

## 5. 如果每个 stage 都先 send 再 recv，会出什么问题？

- **A** 内存泄漏
- **B** 慢
- **C** 线缆上死锁；标准修法是交错安排：偶数 rank 先发、奇数 rank 先收
- **D** 更高的 bubble

<details>
<summary>查看答案与解析</summary>

**答案**　C

同步的 send/recv 配对需要一方在另一方发送时正好在接收。本课显式地调度各 rank，好让这个模式看得见。

</details>

## 6. pipeline 加上 ZeRO-1 组合了哪两项内存收益？

- **A** 什么都没有
- **B** 按 stage 的参数分片（每个 rank 只持有一个 stage 的层）外加按 rank 的 optimizer 分片（每个 rank 只持有其 stage 的 1/N optimizer state）
- **C** 只省激活
- **D** 压缩与量化

<details>
<summary>查看答案与解析</summary>

**答案**　B

pipeline 把层切分到各 rank；ZeRO 在每个 pipeline rank 上的数据并行组内分片 optimizer state。两项收益叠加复利。

</details>


[返回本课](docs/zh.md)
