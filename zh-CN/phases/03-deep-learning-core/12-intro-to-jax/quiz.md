# JAX 入门 · 自测

每题先选答案，再展开解析。

## 1. PyTorch 和 JAX 之间根本的设计差异是什么？

- **A** PyTorch 即时地原地修改张量，而 JAX 编译没有副作用的纯函数
- **B** JAX 不支持 GPU
- **C** PyTorch 不支持自动微分
- **D** PyTorch 更快

<details>
<summary>查看答案与解析</summary>

**答案**　A

PyTorch 使用带可变状态的即时执行（例如 tensor.grad 被原地修改）。JAX 拥抱函数式编程：函数是纯的，状态是显式的，jit 编译会优化整个计算图。

</details>

## 2. jax.jit 做什么？

- **A** 它把一个 Python 函数编译为优化过的 XLA 代码，运行速度远快于被解释执行的 Python
- **B** 它初始化模型权重
- **C** 它计算梯度
- **D** 它添加 dropout 正则化

<details>
<summary>查看答案与解析</summary>

**答案**　A

jax.jit 跟踪一个函数并把它编译为 XLA（加速线性代数）机器码。第一次调用很慢（编译），但后续调用运行的是优化过的已编译版本。

</details>

## 3. jax.vmap 做什么？

- **A** 计算二阶梯度
- **B** 管理 GPU 显存
- **C** 验证模型架构
- **D** 把一个函数向量化，使其在批维度上运行，而无需编写显式循环

<details>
<summary>查看答案与解析</summary>

**答案**　D

jax.vmap 自动把为单个样本编写的函数向量化，以处理整个批次。你只为一个样本编写代码，vmap 负责处理批量，通常比手动的批量循环更高效。

</details>

## 4. JAX 处理模型状态（权重）的方式与 PyTorch 有何不同？

- **A** JAX 只把权重存储在 CPU 上
- **B** JAX 不支持可训练权重
- **C** JAX 和 PyTorch 处理状态的方式完全相同
- **D** JAX 要求显式地传递状态——权重是函数参数，而不是可变的对象属性

<details>
<summary>查看答案与解析</summary>

**答案**　D

在 PyTorch 中，权重存在于 nn.Module 对象内部并被原地修改。在 JAX 中，权重作为函数参数显式传入并作为新值返回。没有原地修改，没有隐藏状态。

</details>

## 5. 什么时候你会选择 JAX 而不是 PyTorch？

- **A** 用于快速搭建小模型原型时
- **B** 当你需要最大的预训练模型生态时
- **C** 用于部署到移动设备时
- **D** 当在 TPU pod 上进行超大规模训练时，编译和函数式变换能带来显著的提速

<details>
<summary>查看答案与解析</summary>

**答案**　D

JAX 擅长大规模场景：jit 编译消除了 Python 开销，pmap 天然地处理多设备并行，而对整个计算图的 XLA 优化在 TPU 集群上带来显著提速。

</details>


[返回本课](docs/zh.md)
