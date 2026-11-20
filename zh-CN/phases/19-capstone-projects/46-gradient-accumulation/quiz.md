# 梯度累积 · 自测

每题先选答案，再展开解析。

## 1. 梯度累积表达的 effective batch 等式是什么？

- **A** effective_batch = micro_batch * accum_steps
- **B** effective_batch = micro_batch / accum_steps
- **C** effective_batch = world_size only
- **D** effective_batch = micro_batch + accum_steps

<details>
<summary>查看答案与解析</summary>

**答案**　A

Micro batch 是显存能装下的大小；accumulation steps 是在一次 optimizer step 之前把梯度堆进同一个 buffer 的 forward + backward 次数。

</details>

## 2. 为什么每个 micro batch backward 之前要把 loss 除以 accum_steps？

- **A** 为了避免 NaN。
- **B** 只在混合精度下才需要。
- **C** PyTorch 默认把梯度累加到 param.grad 里，不除的话累积梯度会大 N 倍，optimizer step 也会激进 N 倍。
- **D** 让 loss 曲线更好看。

<details>
<summary>查看答案与解析</summary>

**答案**　C

累积 buffer 是求和的。每个 micro batch 乘以 1/N，就把求和结果拉回到单次全 batch backward 产生的相同尺度。

</details>

## 3. 在累积循环里，optimizer step 什么时候执行？

- **A** 永远不执行；optimizer 被替换了。
- **B** 每个窗口执行两次以确保安全。
- **C** 只在累积窗口的最后一个 micro batch 之后。
- **D** 每个 micro batch 之后。

<details>
<summary>查看答案与解析</summary>

**答案**　C

在累积中途 step 会污染后续依赖的所有参数。Optimizer step 每个 effective batch 只触发一次。

</details>

## 4. 在真正的多 GPU run 上，no_sync context 包裹的是什么？

- **A** Optimizer step。
- **B** 前向传播。
- **C** 非最后一个 micro batch，这样 gradient all-reduce 只在最后一次 backward 之后触发，而不是触发 N 次。
- **D** Data loader。

<details>
<summary>查看答案与解析</summary>

**答案**　C

DDP 的 no_sync 跳过梯度 collective。把除最后一个之外的 micro batch 都包起来，就把每个 effective step 的 N 次 collective 变成了一次。

</details>

## 5. main.py 中的 equivalence_check 函数断言了什么？

- **A** 梯度为零。
- **B** 吞吐量是常量。
- **C** 单次全 batch backward 和 accum_steps 次分块 backward（loss 除以 N）产生相同的梯度 buffer 和相同的 step 后参数，在一个小容差内。
- **D** Loss 收敛了。

<details>
<summary>查看答案与解析</summary>

**答案**　C

断言界限是 max-abs-diff 低于 1e-4。不做 loss 缩放时差值会爆炸；做了缩放后差值停留在浮点噪声水平。

</details>

## 6. 从吞吐量随 effective batch 的变化曲线上看，什么基本不变、什么在缩放？

- **A** Samples per second 随更大的 effective batch 下降。
- **B** 吞吐量会上升因为模型变快了。
- **C** Samples per second 在硬件上限附近饱和，而每次 optimizer step 的 wall time 随 accum_steps 线性增长；真正下降的是 optimizer steps per second。
- **D** 两个指标都随 accum 线性增长。

<details>
<summary>查看答案与解析</summary>

**答案**　C

每个 micro batch 的 forward + backward 开销不变。累积买到的是每次 optimizer step 的统计平滑，而非原始吞吐量；这条曲线是对流行说法的有效现实检验。

</details>


[返回本课](docs/zh.md)
