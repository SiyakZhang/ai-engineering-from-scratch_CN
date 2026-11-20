# 程序解剖：从零编写 ELF 读取器 · 自测

每题先选答案，再展开解析。

## 1. 第 32 至 36 课的每个分析目标都必须满足哪条规则？

- **A** 目标是小于一兆字节的程序
- **B** 目标是发布了源码映射的程序
- **C** 目标可以是机器上安装的任意程序
- **D** 目标是你自己编写并编译的程序

<details>
<summary>查看答案与解析</summary>

**答案**　D

本路线只分析你拥有的代码，使课程保持在 17 U.S.C. 1201(f)、Directive 2009/24/EC、Sega 和 Connectix 案例的授权边界内。

</details>

## 2. 可重定位目标文件中某符号的 st_value 为 0x10，st_shndx 为 2；节 2 的 sh_offset 为 0x40，sh_addr 为 0。符号字节在文件哪里？

- **A** 文件偏移 0x42，即节索引加符号值
- **B** 文件偏移 0x40，即所属节起点
- **C** 文件偏移 0x50，即节偏移加符号值
- **D** 文件偏移 0x10，因为 st_value 是文件偏移

<details>
<summary>查看答案与解析</summary>

**答案**　C

目标文件中的 st_value 是符号在所属节内的偏移。文件偏移为 sh_offset + st_value - sh_addr，此处为 0x40 + 0x10 - 0 = 0x50。

</details>

## 3. .rela.text 中有记录：偏移 0x36、R_X86_64_PC32、.rodata+0x10；包含该字段的 lea 指令在 0x3a 结束。链接后 lea 指向哪里？

- **A** .text+0x10，重定位始终指向被修补节内部
- **B** .rodata+0x36，即字段偏移
- **C** .rodata+0x14，因为 S + A - P 被加到指令末尾地址
- **D** .rodata+0x10，加数就是目标

<details>
<summary>查看答案与解析</summary>

**答案**　C

处理器将存储值加到 0x3a。存储值为 S + A - P，其中 P = 0x36，因此结果为 .rodata + 0x10 + 4 = .rodata + 0x14。

</details>

## 4. ELF 加载器读取哪个结构来将可执行文件映射到内存？

- **A** 通过 e_phoff 定位的程序头表
- **B** 通过 e_shoff 定位的节头表
- **C** 通过 e_shstrndx 定位的字符串表
- **D** 通过 .symtab 定位的符号表

<details>
<summary>查看答案与解析</summary>

**答案**　A

程序头属于执行视图。剥离后的可执行文件可以完全没有节头表，仍然能够运行。

</details>

## 5. Mach-O 读取器如何从 nlist_64 条目确定函数长度？

- **A** 读取 n_desc 字段，其中保存函数字节数
- **B** 从 LC_SYMTAB 命令读取每个符号对应的大小字段
- **C** 用同节下一个符号地址减去当前符号地址
- **D** 读取包含该符号的 section_64 记录中的大小

<details>
<summary>查看答案与解析</summary>

**答案**　C

nlist_64 包含 n_strx、n_type、n_sect、n_desc、n_value，没有大小字段。目标文件中的 ELF st_size 在 Mach-O 中没有对应字段。

</details>

## 6. 为什么本课测试将读取器与捕获的 llvm-objdump 文本比较，而不运行工具？

- **A** llvm-objdump 没有 Linux sysroot 就无法读取可重定位目标文件
- **B** 比较可在任意机器运行，且对照基准不会漂移
- **C** 解析捕获文本比每次测试运行工具更快
- **D** 课程禁止所有外部工具，包括编译器

<details>
<summary>查看答案与解析</summary>

**答案**　B

夹具保存已知工具版本的输出。测试无需安装工具，后续工具版本也不会改变读取器的比较基准。

</details>


[返回本课](docs/zh.md)
