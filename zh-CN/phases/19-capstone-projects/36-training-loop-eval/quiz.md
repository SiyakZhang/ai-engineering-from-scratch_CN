# 训练循环与评估 · 自测

每题先选答案，再展开解析。

## 1. 为什么 target tensor 必须是 input tensor 偏移一位？

- **A** next-token prediction 就是训练目标：模型在每个位置预测下一个 token；忘了做偏移就等于训模型预测自己，什么有用的都学不到
- **B** cross entropy 需要两个一模一样的 tensor
- **C** AdamW 要求的
- **D** 加速优化器

<details>
<summary>查看答案与解析</summary>

**答案**　A

input 是 token 0..T-1；target 是 token 1..T；loss 在 flatten 后的 (batch*seq, vocab) 和 (batch*seq,) shape 上计算。

</details>

## 2. evaluate_model 做了什么训练步没做的事？

- **A** 运行优化器
- **B** 算两次梯度
- **C** 在 no_grad 且关闭 dropout 的条件下跑固定数量的验证 batch，返回可复现的平均 loss
- **D** 修改模型权重

<details>
<summary>查看答案与解析</summary>

**答案**　C

held-out 评估不需要梯度、不需要 dropout，且用固定的验证数据切片来保证跨次运行可复现。

</details>

## 3. AdamW 中哪些参数会接受 weight decay？

- **A** 所有参数一视同仁
- **B** 只有 LM head
- **C** 矩阵形状的 tensor（linear weight、embedding table）接受 weight decay；scale、shift 和 bias tensor 的 decay 为零
- **D** 只有 LayerNorm 的 scale

<details>
<summary>查看答案与解析</summary>

**答案**　C

如果对 LayerNorm 的 scale 施加 decay，scale 会被推向零从而破坏归一化；这种分组是标准的生产做法。

</details>

## 4. warmup + cosine 学习率调度从 step 0 到最后一步画出什么形状？

- **A** 阶梯函数
- **B** 从零线性上升到最大值（warmup_steps 步），然后从最大值余弦衰减到 min_lr（剩余步数）
- **C** 指数增长
- **D** 常数

<details>
<summary>查看答案与解析</summary>

**答案**　B

warmup 阶段让优化器状态充分填充；cosine decay 逐渐缩小步长，让最后阶段对权重做精调。

</details>

## 5. 为什么在 optimizer.step() 之前做梯度范数裁剪？

- **A** 减少内存用量
- **B** 加速 matmul
- **C** 去掉对 warmup 的需求
- **D** 一个坏 batch 可能产生巨大梯度，瞬间毁掉几小时的训练；裁剪到 max_norm=1.0 把优化器限制在安全范围内，又不会扭曲正常的更新

<details>
<summary>查看答案与解析</summary>

**答案**　D

梯度裁剪是防止发散的最低成本保险；1.0 是在大多数场景下都能用的默认值。

</details>

## 6. 为什么把每步记录以 JSONL 而不是 pickle 状态来保存？

- **A** JSONL 记录在重构后仍然有效、可以 grep、用三十行代码就能画图，而且能扛住 crash；pickle 状态则绑定在生成它的模块结构上
- **B** JSONL 占用更少 GPU 内存
- **C** JSONL 训练更快
- **D** JSONL 是优化器要求的

<details>
<summary>查看答案与解析</summary>

**答案**　A

任何 crash 都会留下可读的产物；恢复时读最后一步就行；上面搭工具链极其简单。

</details>


[返回本课](docs/zh.md)
