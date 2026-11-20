# Cosine 学习率 + 线性 Warmup · 自测

每题先选答案，再展开解析。

## 1. 为什么 cosine-with-warmup schedule 从零开始，而不是从 lr_max 开始？

- **A** 因为 lr_max 在 step 0 是非法的。
- **B** 因为 Adam 要求这样做。
- **C** 随意的传统。
- **D** 前一千步更新很不稳定；从零线性升到 lr_max 让优化器在运行估计稳定之前保持较小的有效步长。

<details>
<summary>查看答案与解析</summary>

**答案**　D

Warmup 把脆弱的早期更新控制在较小幅度；否则模型要么发散要么停滞。

</details>

## 2. 为什么 schedule 用一个关于 step 的单一函数来实现，而不是三段拼接？

- **A** 单函数更短。
- **B** 随意的。
- **C** 拼接式 schedule 在 lr_max 第一次被修改时就会丢失一个边界；单函数始终求值同一个封闭形式表达式，在 warmup 和 total 端点处保持连续。
- **D** Linter 要求这样做。

<details>
<summary>查看答案与解析</summary>

**答案**　C

lr(warmup_steps) 和 lr(total_steps) 处的连续性由封闭形式自然保证。

</details>

## 3. step > total_steps 时 schedule 会怎样？

- **A** 返回 nan。
- **B** 循环回绕。
- **C** 钉在 lr_min；schedule 不做外推，需要延长训练的 trainer 会显式修改 total_steps。
- **D** 抛出异常。

<details>
<summary>查看答案与解析</summary>

**答案**　C

钉住下限让超出的 trainer 停在一个有据可查的状态，而不是直接崩溃。

</details>

## 4. 为什么要在学习率旁边记录 gradient L2 norm？

- **A** 传统。
- **B** Adam 要求这样做。
- **C** Norm 是训练健康的另一半信号：发散的 run 会在 loss 之前先让 norm 飙升；过于激进的 peak 会表现为 warmup 之后 norm 一直居高不下。
- **D** 看起来好看。

<details>
<summary>查看答案与解析</summary>

**答案**　C

一起记录能让有问题的 schedule 在训练时而非事后被发现。

</details>

## 5. 为什么在生产中把 warmup_steps 配成 total_steps 的百分比？

- **A** 适合 2 万步 run 的固定 warmup 步数在 2 亿步 run 里几乎等于没有 warmup；百分比（通常 1-3%）随训练时长自动缩放。
- **B** 随意偏好。
- **C** 百分比更简洁。
- **D** 硬件要求。

<details>
<summary>查看答案与解析</summary>

**答案**　A

绝对 warmup 步数在不同训练时长下表现不一致。

</details>

## 6. 为什么生产中通常设非零的 lr_min？

- **A** 接近 lr_max 10% 的下限让优化器在长尾阶段继续学习；lr_min 设为零会产出一条看起来漂亮但模型并没有训完的曲线。
- **B** 数值稳定性。
- **C** 向后兼容。
- **D** Adam 要求非零。

<details>
<summary>查看答案与解析</summary>

**答案**　A

Schedule 的尾部正是后期精细调整落地的地方；把它归零就浪费了这些信号。

</details>


[返回本课](docs/zh.md)
