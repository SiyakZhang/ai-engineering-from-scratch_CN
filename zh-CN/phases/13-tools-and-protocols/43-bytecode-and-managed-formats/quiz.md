# 超越原生代码：Python、JVM、.NET 与 WebAssembly 字节码 · 自测

每题先选答案，再展开解析。

## 1. 反编译器对前四字节为 2b 0e 0d 0a 的 .pyc 文件输出“Unsupported opcode”。头部说明了什么？

- **A** 文件基于哈希，且哈希检查失败
- **B** 文件损坏，因为 pyc 必须以单词 cpython 的字节开头
- **C** 文件使用优化级别 2 编译
- **D** 魔数字为 3627，这是 CPython 3.14 写入的值，而工具没有该版本的操作码表

<details>
<summary>查看答案与解析</summary>

**答案**　D

前两个字节是小端魔数字 0x0e2b = 3627，即 CPython 3.14 头文件中的值。后跟 CR LF，使文本模式读取破坏魔数。这与损坏或哈希无关。

</details>

## 2. 为什么 main.py 在 3.14 下运行时能读取 3.11 pyc 的名称、常量和行表，却不能列出指令？

- **A** 因为名称存在单独的 .pyi 文件里
- **B** 因为 marshal 的类型码格式稳定，本课重新实现了它；操作码编号和缓存布局则跨版本变化，dis 只认识当前解释器的表
- **C** 因为 3.14 移除了 dis 模块
- **D** 因为 3.11 文件已加密

<details>
<summary>查看答案与解析</summary>

**答案**　B

反序列化器从 marshal.c 读取类型码与代码对象字段顺序。缺少生成该文件版本的操作码表时，指令字节无法解释，因此夹具采集了 python3.11 -m dis 的输出。

</details>

## 3. Ledger-g.class 的 pc 4 处字节是 aa 00 00 00 00 00 00 2c 00 00 00 06 00 00 00 0a，之后是五个 4 字节值。aa 后的三个零字节是什么？

- **A** 三条 nop 指令
- **B** switch 的常量池索引
- **C** 填充，使 default、low 和 high 字从 4 的整数倍 pc 开始，符合 JVMS 6.5 tableswitch 的要求
- **D** 默认偏移的高位字节

<details>
<summary>查看答案与解析</summary>

**答案**　C

操作码在 pc 4，因此下一个四字节对齐的 pc 为 8。默认偏移 0x2c = 44 相对于操作码地址，得到目标 48。之后 low 6 和 high 10 表示五项。

</details>

## 4. javac -g:none 将 Ledger.class 从 1832 字节（javac -g）缩为 1404 字节。哪些字节被去掉了？

- **A** 只有调试器使用的 StackMapTable
- **B** LineNumberTable、LocalVariableTable、SourceFile 属性及其常量池字符串被去掉，每个 Code 数组仍逐字节相同
- **C** JVM 在加载时重建的常量池
- **D** 方法体被重新编译为紧凑形式

<details>
<summary>查看答案与解析</summary>

**答案**　B

本课测试比较三种构建的 grade Code 数组，得到相同的 50 字节。消失的只有调试属性及它们引用的 Utf8 条目。StackMapTable 保留，因为校验器需要它。

</details>

## 5. ledger.wasm 没有 name 节，wasm-objdump 却在函数旁输出 <grade>。这个名称来自哪里，仍缺少什么名称？

- **A** 来自偏移 1024 的 Data 段
- **B** 来自 Export 节，它将字符串 grade 映射到函数索引 2；局部变量名 score 和 bucket 仍缺失，直到 wat2wasm --debug-names 添加 name 自定义节
- **C** 来自 Code 节头部，每个函数体都以名称开头
- **D** 来自 Type 节，每个函数类型存一个名称

<details>
<summary>查看答案与解析</summary>

**答案**　B

导出只为导出函数携带字符串。普通模块中完全没有局部变量名。带名称构建将文件从 290 字节增至 425 字节，以自定义节加入函数和局部变量名。

</details>

## 6. Grade 的 MethodDef 行签名 blob 为 00 01 08 08，函数体头部的局部签名 token 为 0x11000001，其 blob 为 07 01 08。程序集仍缺少 Grade 的哪项信息？

- **A** 参数名
- **B** 返回类型
- **C** 参数类型
- **D** 局部变量名，因为 ECMA-335 元数据将局部类型保存在 StandAloneSig，将名称留给单独的 PDB 文件

<details>
<summary>查看答案与解析</summary>

**答案**　D

blob 表示 static int32(int32)，Param 表给出 score，StandAloneSig 表示一个 int32 局部变量。没有表保存局部变量名。夹具以 DebugType none 构建，因此没有 PDB。

</details>

## 7. 五种容器中，哪些需要反编译器从跳转重建 switch，而不能直接读成一条指令或一个块？

- **A** CPython pyc 中 grade 是四对 COMPARE_OP 与 POP_JUMP_IF_FALSE；原生对象中则是经重定位表的 jmpq
- **B** WebAssembly 模块，因为 br_table 没有结构
- **C** .NET 程序集，因为 switch 是前缀
- **D** JVM class，因为 tableswitch 是跳转表

<details>
<summary>查看答案与解析</summary>

**答案**　A

tableswitch、br_table 和 CIL switch 都在一条指令中携带 case 目标，Wasm 还以块嵌套 case。CPython 和 x86-64 只保存跳转，因此其反编译器依赖控制流分析，并会在跳转形态变化时失效。

</details>


[返回本课](docs/zh.md)
