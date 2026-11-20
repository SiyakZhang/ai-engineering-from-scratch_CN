# AI 开发中的 Linux · 自测

每题先选答案，再展开解析。

## 1. 在 Linux 文件路径中，'~' 符号代表什么？

- **A** 当前用户的主目录
- **B** 安装系统程序的目录
- **C** 临时文件目录
- **D** 文件系统的根目录

<details>
<summary>查看答案与解析</summary>

**答案**　A

波浪号（~）是当前用户主目录的快捷写法，在 Linux 上通常是 /home/username。无论身处何处，'cd ~' 都能让你回到主目录。

</details>

## 2. 在命令前加 'sudo' 的目的是什么？

- **A** 它把命令输出记录到一个系统文件
- **B** 它以 root（管理员）权限运行该命令
- **C** 它在沙箱环境中运行该命令
- **D** 它能加快命令的执行

<details>
<summary>查看答案与解析</summary>

**答案**　B

sudo（superuser do）会为单条命令临时把你的权限提升到 root 级别。像用 apt 安装软件包这样的系统级操作就需要它。

</details>

## 3. 在尝试运行一个 shell 脚本时你收到 'Permission denied'。哪个命令能解决这个问题？

- **A** mv script.sh /usr/bin/
- **B** chown root script.sh
- **C** sudo rm script.sh
- **D** chmod +x script.sh

<details>
<summary>查看答案与解析</summary>

**答案**　D

chmod +x 为文件添加执行权限。如果没有设置可执行位，即使你是文件的所有者，shell 也会拒绝运行该脚本。

</details>

## 4. 在一台远程 GPU 机器上，你的训练数据把磁盘塞满了。哪个命令能显示占用空间最多的那些目录？

- **A** cat /proc/meminfo
- **B** du -h --max-depth=1 / | sort -hr | head -20
- **C** free -h
- **D** ls -la /

<details>
<summary>查看答案与解析</summary>

**答案**　B

du -h 显示每个目录的磁盘占用，--max-depth=1 把范围限制到顶层目录，sort -hr 按大小降序排序。这样就能看出哪些目录占用空间最多。

</details>

## 5. macOS 和 Linux 版本的 'sed -i' 之间一个关键区别是什么？

- **A** macOS 的 sed 在 -i 后需要一个空字符串参数（'sed -i ""'），而 Linux 不需要
- **B** Linux 的 sed 不支持正则表达式
- **C** Linux 的 sed 比 macOS 的 sed 快
- **D** macOS 的 sed 无法就地修改文件

<details>
<summary>查看答案与解析</summary>

**答案**　A

macOS 使用 BSD 版的 sed，需要写成 'sed -i "" pattern file'，而 Linux 使用 GNU 版的 sed，可以写成 'sed -i pattern file'。在系统之间迁移脚本时这是一个常见的坑。

</details>


[返回本课](docs/zh.md)
