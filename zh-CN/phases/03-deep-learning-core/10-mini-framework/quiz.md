# 搭一个你自己的迷你框架 · 自测

每题先选答案，再展开解析。

## 1. 在深度学习框架中，Module 抽象承担哪三项职责？

- **A** forward() 负责计算，backward() 负责梯度，parameters() 负责可训练权重
- **B** 编译、优化、部署
- **C** 加载数据、预处理数据、增强数据
- **D** 分词、嵌入、解码

<details>
<summary>查看答案与解析</summary>

**答案**　A

每个 Module 都实现 forward() 来计算输出、backward() 来传播梯度、parameters() 来暴露可训练权重。这种统一的接口让任意模块都能与任意其他模块组合。

</details>

## 2. 为什么 Sequential 在反向传播时以相反的顺序处理各模块？

- **A** 它防止梯度爆炸
- **B** 这是随意的——两个方向都可以
- **C** 相反顺序占用更少内存
- **D** 梯度从损失出发向后流经网络，因此最后一层最先计算梯度

<details>
<summary>查看答案与解析</summary>

**答案**　D

反向传播从损失开始，把梯度向输入方向传播。最后一层最先收到损失梯度，计算它的局部梯度，然后把它们传给前一层。

</details>

## 3. 为什么 optimizer.zero_grad() 是一次单独的调用，而不是自动完成？

- **A** 它允许在执行一次优化器步骤之前跨多个批次累积梯度
- **B** 它让调试更容易
- **C** 它节省内存
- **D** 这是 PyTorch 的一个设计失误

<details>
<summary>查看答案与解析</summary>

**答案**　A

把 zero_grad 与 step 分开可实现梯度累积：你可以多次运行 backward()（跨多个小批量）并在调用 step() 前把梯度求和。这模拟了更大的批大小。

</details>

## 4. 训练循环中各操作的正确顺序是什么？

- **A** backward、forward、zero_grad、step
- **B** forward、loss、zero_grad、backward、step
- **C** zero_grad、forward、loss、backward、step
- **D** forward、zero_grad、backward、loss、step

<details>
<summary>查看答案与解析</summary>

**答案**　C

标准模式是：zero_grad（清除旧梯度）、forward（计算预测）、loss（计算标量损失）、backward（计算梯度）、step（更新参数）。把这个顺序弄错会导致难以察觉的 bug。

</details>

## 5. 在框架中 DataLoader 的作用是什么？

- **A** 它计算损失函数
- **B** 它训练模型
- **C** 它初始化权重
- **D** 它把数据切分成批，并可选择在各 epoch 之间打乱，以进行小批量梯度下降

<details>
<summary>查看答案与解析</summary>

**答案**　D

DataLoader 处理两个实际问题：分批（你无法把所有数据都装进内存）和打乱（随机顺序防止模型记住数据序列）。

</details>


[返回本课](docs/zh.md)
