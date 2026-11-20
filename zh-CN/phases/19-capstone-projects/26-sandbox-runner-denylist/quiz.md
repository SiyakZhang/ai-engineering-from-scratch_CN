# 顶点课 26：带 Denylist 与 Path Jail 的 Sandbox Runner · 自测

每题先选答案，再展开解析。

## 1. 在阅读本课之前：为什么沙箱要检查 python3 -c 这类解释器调用的 argv 形状？

- **A** 不用解释器时模型写的代码更好。
- **B** 解释器太慢，浪费 agent 预算。
- **C** 解释器完全无法被安全地沙箱化。
- **D** 带 -c 的解释器本质上就是换了个名字的 shell 调用，会绕过可执行文件黑名单。

<details>
<summary>查看答案与解析</summary>

**答案**　D

python3 -c、bash -c、node -e 等在功能上等同于给模型一个 shell。光拦可执行文件名是不够的。

</details>

## 2. 沙箱配置了 project_root=/work。一个路径参数是 ./src/main.py。路径隔离检查怎么做？

- **A** 沙箱拒绝所有相对路径。
- **B** 对 /work 做字面字符串前缀匹配。
- **C** 沙箱先启动子进程，事后再检查工作目录。
- **D** 对拼接后的绝对路径执行 os.path.realpath，然后检查是否以 /work 为前缀。

<details>
<summary>查看答案与解析</summary>

**答案**　D

realpath 会解析符号链接。字面前缀匹配会被项目根目录下指向外部的符号链接绕过。realpath 加前缀相等才是安全的检查方式。

</details>

## 3. SandboxResult 返回 denied=True、timed_out=False、exit_code=-100。规范解读是什么？

- **A** 墙钟超时触发了。
- **B** 子进程已启动并被 SIGKILL 杀掉。
- **C** 子进程显式返回了 -100。
- **D** 沙箱在 exec 之前就拒绝了，从未启动子进程。

<details>
<summary>查看答案与解析</summary>

**答案**　D

哨兵值 exit_code -100 搭配 denied=True 表示沙箱在调用 subprocess.run 之前就短路了。

</details>

## 4. 为什么沙箱默认使用 shell=False 并拒绝 shell 元字符？

- **A** 这样测试套件写起来更简单。
- **B** subprocess 在 macOS 上不接受 shell=True。
- **C** shell=True 在 CPython 上更慢。
- **D** Shell 解析会把整个 shell DSL 暴露给模型，而沙箱的目的就是缩小这个攻击面。

<details>
<summary>查看答案与解析</summary>

**答案**　D

shell=True 会把 argv 变成 shell 解释的字符串。管道、重定向、命令替换和通配符全部可用。一旦 shell 解析运行起来，沙箱就无法有效拒绝任何负载了。

</details>

## 5. 你想给沙箱加上进程级内存限制。本课的沙箱没有实现这个。正确的下一步是什么？

- **A** 跳过：黑名单足以应对内存炸弹。
- **B** 增加墙钟超时来弥补。
- **C** 在传给 subprocess.run 的 preexec_fn 中使用 os.setrlimit(RLIMIT_AS)。
- **D** 把限制作为字符串加到黑名单里。

<details>
<summary>查看答案与解析</summary>

**答案**　C

subprocess.run 接受 preexec_fn（POSIX）或类似机制。setrlimit(RLIMIT_AS) 限制子进程的地址空间。本课的沙箱没有提供这个功能；第 29 课的端到端演示会讨论如何在上面叠加容器级限制。

</details>

## 6. 模型用 argv=['cat', 'src/../src/main.py'] 调用沙箱。文件确实在 project_root 下。这个调用能通过路径隔离吗？

- **A** 取决于用户是否是 root。
- **B** 不能：argv 在沙箱看到之前就被正则 gate 拒绝了。
- **C** 不能，路径中有 .. 就自动拒绝。
- **D** 能：realpath 把 src/../src 折叠为 src，解析后的路径在 project_root 内。

<details>
<summary>查看答案与解析</summary>

**答案**　D

realpath 会规范化路径。沙箱不会一刀切地拒绝 .. 标记；它检查的是解析后的目标。这是有意为之：合法路径有时确实会经过 ..。

</details>


[返回本课](docs/zh.md)
