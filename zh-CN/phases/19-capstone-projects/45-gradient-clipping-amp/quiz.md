# Gradient Clipping 与混合精度训练 · 自测

每题先选答案，再展开解析。

## 1. 全局 L2 gradient clipping 解决了什么问题？

- **A** 训练太慢。
- **B** 一个 bad batch 就能让 gradient norm 飙升好几个数量级；clipping 限制了最坏情况下的优化器步长，防止一个 batch 抹掉几小时的训练成果。
- **C** 随机重启。
- **D** 词表漂移。

<details>
<summary>查看答案与解析</summary>

**答案**　B

Clipping 是安全带，防止一个噪声 batch 把 loss 曲线搞崩。

</details>

## 2. GradScaler 各操作的正确顺序是？

- **A** backward, step, scale, update
- **B** 任意顺序；scaler 内部会重排。
- **C** scaler.scale(loss).backward(); scaler.unscale_(optimizer); clip_grad_norm_; scaler.step(optimizer); scaler.update()
- **D** step, scale, unscale, backward, update

<details>
<summary>查看答案与解析</summary>

**答案**　C

在 unscale_ 和 step 之间对未缩放的梯度做 clip；update 必须始终调用。

</details>

## 3. 在跳过的步上 scaler.update() 做了什么？

- **A** 把 scaling factor 翻倍。
- **B** 关闭整个 run。
- **C** 什么都不做。
- **D** 把 scaling factor 减半并重置 no-inf 计数器；如果跳过路径上忘记调它，就会出现 'scaling factor 一直没变' 的 bug。

<details>
<summary>查看答案与解析</summary>

**答案**　D

Scaler 根据最近若干步的 skip/clean 比例来调整自己的 factor。

</details>

## 4. 即使有 GradScaler，为什么还需要检查 loss 是否有限？

- **A** 纯装饰性的。
- **B** GradScaler 处理的是反向传播的溢出，而非有限的 loss 根本产生不了有用的梯度；在 backward 之前跳过能省计算、避免污染 scaler 状态。
- **C** 因为 GradScaler 很慢。
- **D** PyTorch 强制要求。

<details>
<summary>查看答案与解析</summary>

**答案**　B

Loss 检查覆盖前向传播的故障；scaler 覆盖反向传播的故障。

</details>

## 5. 滚动 skip rate 的生产信号是什么？

- **A** 只有连续 skip 才报警。
- **B** 任何一次 skip 都应该报警。
- **C** 一轮训练里偶尔几次 skip 是正常的；每个 epoch 上百次 skip（滚动率超过约 5%）就是硬告警，说明模型处在 FP16 扛不住的区间。
- **D** Skip rate 无所谓。

<details>
<summary>查看答案与解析</summary>

**答案**　C

基于比率的告警能捕捉到偶发式告警抓不到的静默失败模式。

</details>

## 6. skip 频繁时，为什么从 FP16 切换到 BF16 autocast？

- **A** 随意的传统。
- **B** BF16 的指数范围比 FP16 宽，几乎不需要 loss scaling；同一模型上 skip rate 通常直接降到零。
- **C** BF16 更新。
- **D** BF16 更慢所以 skip 更少。

<details>
<summary>查看答案与解析</summary>

**答案**　B

FP16 在尾数精度和范围之间偏向精度；BF16 反过来，从根本上消除了溢出这一类问题。

</details>


[返回本课](docs/zh.md)
