# PyTorch 入门 · 自测

每题先选答案，再展开解析。

## 1. PyTorch 中的 autograd 是什么？

- **A** 一个自动微分引擎，它记录运算并计算梯度，无需手动实现反向传播
- **B** 一个数据加载库
- **C** 一个模型压缩工具
- **D** 一个超参数调优框架

<details>
<summary>查看答案与解析</summary>

**答案**　A

PyTorch 的 autograd 在前向计算过程中构建计算图，并在你调用 .backward() 时自动计算梯度。这免去了在每个模块中手动实现 backward() 的需要。

</details>

## 2. torch.no_grad() 做什么，你应该在什么时候使用它？

- **A** 它防止过拟合
- **B** 它启用 GPU 加速
- **C** 它在推理时禁用梯度追踪，在你不需要训练时节省内存和计算
- **D** 它冻结所有模型权重

<details>
<summary>查看答案与解析</summary>

**答案**　C

在推理时你不需要梯度。torch.no_grad() 禁用梯度追踪，从而节省本会用于存储计算图的内存并加快计算。

</details>

## 3. 在 PyTorch 中 nn.Linear(784, 256) 创建了什么？

- **A** 一个 p=784/256 的 dropout 层
- **B** 一个 ReLU 激活层
- **C** 一个批归一化层
- **D** 一个全连接层，带有一个 (256, 784) 的权重矩阵和一个 (256,) 的偏置向量

<details>
<summary>查看答案与解析</summary>

**答案**　D

nn.Linear(in_features, out_features) 创建一个计算 y = x @ W^T + b 的层，其中 W 的形状为 (256, 784)，b 的形状为 (256,)。这是你从零构建的 Layer 类在 PyTorch 中的等价物。

</details>

## 4. 哪个 PyTorch 方法为计算图中的所有参数计算梯度？

- **A** model.forward()
- **B** optimizer.step()
- **C** loss.backward()
- **D** optimizer.zero_grad()

<details>
<summary>查看答案与解析</summary>

**答案**　C

loss.backward() 反向遍历计算图，为每个需要梯度的参数 p 计算 dL/dp。随后 optimizer.step() 使用这些梯度来更新参数。

</details>

## 5. 为什么 PyTorch 的训练循环比纯 Python 的迷你框架快得多？

- **A** PyTorch 跳过了反向传播
- **B** PyTorch 把运算作为优化过的 C++/CUDA 内核在 GPU 上运行，而纯 Python 循环是逐个运算被解释执行的
- **C** PyTorch 使用更小的数据类型
- **D** PyTorch 使用了不同的算法

<details>
<summary>查看答案与解析</summary>

**答案**　B

PyTorch 把矩阵运算交给高度优化的 C++ 和 CUDA 内核，它们在 GPU 上以大规模并行运行。纯 Python 则顺序执行循环，每个运算都带有解释器开销。

</details>


[返回本课](docs/zh.md)
