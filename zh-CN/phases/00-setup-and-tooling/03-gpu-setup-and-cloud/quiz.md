# GPU 配置与云端 · 自测

每题先选答案，再展开解析。

## 1. 为什么训练神经网络时 GPU 比 CPU 快？

- **A** GPU 的时钟频率比 CPU 高
- **B** GPU 的内存比 CPU 多
- **C** GPU 能同时执行数千个并行的矩阵运算
- **D** GPU 使用一种更高效的编程语言

<details>
<summary>查看答案与解析</summary>

**答案**　C

GPU 拥有数千个为并行计算优化的核心，非常适合在神经网络训练中占主导地位的矩阵乘法。

</details>

## 2. VRAM 指的是什么？

- **A** GPU 上的显存，独立于系统内存
- **B** 所有设备上可用内存的总和
- **C** 操作系统用作交换空间的虚拟内存
- **D** 一种 CPU 缓存内存

<details>
<summary>查看答案与解析</summary>

**答案**　A

VRAM（显存）是 GPU 上的专用内存，独立于系统主内存。它限制了你在训练时能使用的模型大小和批大小。

</details>

## 3. 哪个命令可以验证你的 NVIDIA GPU 已被检测到并显示其当前状态？

- **A** gpu --status
- **B** lspci | grep gpu
- **C** torch.cuda.list_devices()
- **D** nvidia-smi

<details>
<summary>查看答案与解析</summary>

**答案**　D

nvidia-smi（NVIDIA 系统管理接口）会显示 GPU 利用率、显存使用、温度和运行中的进程。它是验证 GPU 可用性的标准工具。

</details>

## 4. 在对 GPU 与 CPU 的矩阵乘法做基准测试时，为什么必须在测量 GPU 时间前调用 torch.cuda.synchronize()？

- **A** 为了确保在停止计时之前所有 GPU 操作都已完成
- **B** 为了释放未使用的 GPU 显存
- **C** 为了把 GPU 时钟频率重置为基础频率
- **D** 为了把数据从 CPU 内存传到 GPU 显存

<details>
<summary>查看答案与解析</summary>

**答案**　A

GPU 操作是异步的——当 GPU 仍在计算时，Python 会立即返回。synchronize() 会阻塞直到所有 GPU 操作完成，从而给出准确的计时。

</details>

## 5. 按照 fp16 的经验法则，24 GB 显存大约能容纳多少参数？

- **A** 120 亿参数
- **B** 480 亿参数
- **C** 60 亿参数
- **D** 240 亿参数

<details>
<summary>查看答案与解析</summary>

**答案**　A

在 fp16 下，每个参数占用 2 字节。24 GB / 2 字节 = 120 亿参数。这只是粗略估计；实际占用还包括激活值、梯度和优化器状态。

</details>


[返回本课](docs/zh.md)
