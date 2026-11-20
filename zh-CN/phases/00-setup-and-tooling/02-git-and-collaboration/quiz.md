# Git 与协作 · 自测

每题先选答案，再展开解析。

## 1. “版本控制”主要帮助你做什么？

- **A** 压缩文件以节省磁盘空间
- **B** 自动修复代码中的 bug
- **C** 随时间追踪文件的变更，并与他人协作
- **D** 加速代码执行

<details>
<summary>查看答案与解析</summary>

**答案**　C

像 git 这样的版本控制系统会追踪对文件的每一次变更，让你能够回退到之前的状态，并与他人在同一代码库上协作。

</details>

## 2. 在软件开发的语境中，“仓库（repository）”是什么？

- **A** 由版本控制管理的一组文件及其完整变更历史
- **B** 用于存储用户数据的数据库
- **C** 像 Google Drive 那样的云存储服务
- **D** 用于安装库的包管理器

<details>
<summary>查看答案与解析</summary>

**答案**　A

仓库（repo）是由 git 追踪的目录，包含所有项目文件以及对这些文件所做变更的完整历史。

</details>

## 3. 在 git 中保存并备份你的工作的正确顺序是什么？

- **A** git push, git add, git commit
- **B** git add, git commit, git push
- **C** git clone, git add, git push
- **D** git commit, git add, git push

<details>
<summary>查看答案与解析</summary>

**答案**　B

首先用 'git add' 暂存变更，然后用 'git commit' 保存一个快照，再用 'git push' 上传到远端。这是日常的工作流。

</details>

## 4. 'git checkout -b experiment/new-optimizer' 的作用是什么？

- **A** 删除 experiment/new-optimizer 分支
- **B** 将所有文件回退到与 experiment/new-optimizer 分支一致
- **C** 创建一个名为 experiment/new-optimizer 的新分支并切换到它
- **D** 从 GitHub 下载一个名为 experiment/new-optimizer 的分支

<details>
<summary>查看答案与解析</summary>

**答案**　C

'-b' 选项会创建一个指定名称的新分支并立即切换过去，让你能在不影响主分支的情况下做实验。

</details>

## 5. 为什么应该把 '.pt'、'.pth' 和 '.safetensors' 加入 .gitignore？

- **A** Git 无法追踪任何类型的二进制文件
- **B** 它们是不应被提交的 Python 测试文件
- **C** 它们是模型检查点文件，对 git 来说太大，而且可以重新生成
- **D** 它们包含敏感的 API 密钥

<details>
<summary>查看答案与解析</summary>

**答案**　C

模型检查点文件（.pt、.pth、.safetensors）通常有数 GB 大小。Git 并不是为大型二进制文件设计的，因此应当排除这些文件，重新生成或单独存储。

</details>


[返回本课](docs/zh.md)
