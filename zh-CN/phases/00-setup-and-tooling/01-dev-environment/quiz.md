# 开发环境 · 自测

每题先选答案，再展开解析。

## 1. 为什么 AI 项目需要单独的虚拟环境？

- **A** 它们隔离依赖，使不同项目之间不会相互冲突
- **B** 虚拟环境能让代码运行得更快
- **C** 虚拟环境提供 GPU 访问能力
- **D** Python 必须有虚拟环境才能导入包

<details>
<summary>查看答案与解析</summary>

**答案**　A

虚拟环境为每个项目隔离包版本。没有它们，为一个项目升级 PyTorch 可能会破坏另一个依赖旧版本的项目。

</details>

## 2. CUDA 为 AI 工作负载提供了什么？

- **A** 用于 ML 库的 Python 包管理器
- **B** 用于部署模型的 Web 框架
- **C** 用于模型服务的容器运行时
- **D** 在 NVIDIA GPU 上进行矩阵运算的并行计算

<details>
<summary>查看答案与解析</summary>

**答案**　D

CUDA 是 NVIDIA 的并行计算平台，让你能在数千个 GPU 核心上同时运行矩阵运算。PyTorch 和 TensorFlow 在底层都使用它。

</details>

## 3. 在四层环境技术栈中，哪一层必须最先安装？

- **A** 系统底座（操作系统、shell、GPU 驱动）
- **B** 语言运行时（Python、Node.js）
- **C** 包管理器（pip、npm、cargo）
- **D** AI/ML 库（PyTorch、JAX）

<details>
<summary>查看答案与解析</summary>

**答案**　A

安装顺序是自底向上：先装系统底座（操作系统、驱动），再装包管理器，然后是语言运行时，最后是 AI 库。每一层都依赖于下面那一层。

</details>

## 4. 在 Python AI 项目中，uv 的用途是什么？

- **A** 一个 GPU 监控工具
- **B** 一个神经网络可视化库
- **C** 一个超快的 Python 包安装器和依赖解析器
- **D** 一个用于自定义内核的 CUDA 编译器

<details>
<summary>查看答案与解析</summary>

**答案**　C

uv 是用 Rust 编写的快速 Python 包安装器。它替代 pip，依赖解析和安装速度快得多，通常快 10 到 100 倍。

</details>

## 5. 如何验证 PyTorch 能访问你的 GPU？

- **A** python -c 'import gpu'
- **B** import torch; print(torch.__version__)
- **C** nvidia-smi --query
- **D** import torch; print(torch.cuda.is_available())

<details>
<summary>查看答案与解析</summary>

**答案**　D

如果 PyTorch 能访问 CUDA GPU，torch.cuda.is_available() 会返回 True。在 Apple Silicon 上，请使用 torch.backends.mps.is_available() 来检测 Metal Performance Shaders。

</details>


[返回本课](docs/zh.md)
