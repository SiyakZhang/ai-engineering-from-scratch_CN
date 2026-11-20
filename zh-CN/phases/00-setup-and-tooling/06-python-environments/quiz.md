# Python 环境 · 自测

每题先选答案，再展开解析。

## 1. 虚拟环境解决了什么问题？

- **A** 它们隔离项目依赖，使不同项目可以使用不同的包版本
- **B** 它们提供一个管理 Python 脚本的图形界面
- **C** 它们自动将包更新到最新版本
- **D** 它们通过优化解释器让 Python 代码运行更快

<details>
<summary>查看答案与解析</summary>

**答案**　A

虚拟环境为每个项目提供一套独立的包。没有它们，为一个项目安装 PyTorch 2.4 会覆盖另一个项目所需的 PyTorch 2.1。

</details>

## 2. 在 Python 依赖管理的语境中，锁文件（lockfile）是什么？

- **A** 一个锁定 Python 解释器版本的文件
- **B** 一个加密你项目依赖的文件
- **C** 一个把每个包都锁定到精确版本以实现可复现安装的文件
- **D** 一个阻止其他用户编辑你代码的文件

<details>
<summary>查看答案与解析</summary>

**答案**　C

锁文件记录每个包的精确版本（包括传递依赖），这样任何人据此安装都会得到完全相同的包，从而确保可复现性。

</details>

## 3. 如何验证你的 pip 和 python 命令用的是虚拟环境而不是系统 Python？

- **A** 检查终端的背景颜色是否变了
- **B** 运行 'python --check-env' 来验证
- **C** 运行 'pip --version' 并检查版本号
- **D** 运行 'which python' 并确认它显示 .venv/bin/python 而不是 /usr/bin/python

<details>
<summary>查看答案与解析</summary>

**答案**　D

'which python'（在 Windows 上是 'where python'）会显示解释器的完整路径。如果它指向 .venv/bin/python，说明你正处于虚拟环境中。

</details>

## 4. 为什么在同一个环境中混用 pip 和 conda 会有问题？

- **A** 它会让每个包占用的磁盘空间翻倍
- **B** conda 无法安装 pip 已经安装过的包
- **C** pip 安装会破坏 conda 的依赖追踪，造成难以排查的冲突
- **D** pip 安装的包与 conda 的 Python 解释器不兼容

<details>
<summary>查看答案与解析</summary>

**答案**　C

conda 维护着自己的依赖求解器。pip 安装会绕过它，于是 conda 不再知道环境的真实状态。这会导致难以解决的依赖冲突。

</details>

## 5. 尽管装有 NVIDIA GPU，你的 PyTorch 代码却报告 'CUDA not available'。最可能的原因是什么？

- **A** 你的 GPU 不支持 CUDA
- **B** 虚拟环境无法访问 GPU 硬件
- **C** 安装的 PyTorch 所带的 CUDA 版本与你的 GPU 驱动不兼容
- **D** 你忘记导入 torch.cuda 模块

<details>
<summary>查看答案与解析</summary>

**答案**　C

PyTorch 附带为特定 CUDA 版本编译的 CUDA 绑定。如果 PyTorch 的 CUDA 版本高于你驱动支持的 CUDA 版本，CUDA 将不可用。可用 nvidia-smi 和 torch.version.cuda 检查。

</details>


[返回本课](docs/zh.md)
