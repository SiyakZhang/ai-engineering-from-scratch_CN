# 调用约定与栈帧：System V、Windows x64 与 AArch64 · 自测

每题先选答案，再展开解析。

## 1. 同一 C 函数 double mixed(int i, double d, long long l, float f) 分别编为 Linux x86-64 和 Windows x64。四参数在哪些寄存器？

- **A** System V 用 edi、xmm0、rsi、xmm1（双列表）；Microsoft 用 ecx、xmm1、r8、xmm3（位置槽）
- **B** 都用 edi、xmm0、rsi、xmm1，因为都按整数和 SSE 双列表填充
- **C** 都用 ecx、xmm0、rdx、xmm1，因为整数列表都从 rcx 开始
- **D** System V 将 d、f 放栈，因为 SSE 仅返回结果

<details>
<summary>查看答案与解析</summary>

**答案**　A

psABI 3.2.3 分别从整数和 SSE 列表分配。Microsoft 按位置 k 使用 RCX/RDX/R8/R9 或 XMM0–3，因此槽 1 的 double 用 XMM1，槽 3 的 float 用 XMM3。

</details>

## 2. -O2 Microsoft eight_args 没有序言，第五参数在 0x28(%rsp)。0x28 如何得出？

- **A** 八字节返回地址加四个寄存器参数的三十二字节影子空间
- **B** 从 SP 起数五个八字节参数槽
- **C** 编译器为十六字节对齐选择的填充
- **D** 帧指针偏移加序言保存的 rbp

<details>
<summary>查看答案与解析</summary>

**答案**　A

入口 0(rsp) 为返回地址，8–39 为四个 home，因此首栈参数从 40 即 0x28 开始。

</details>

## 3. -O2 System V keeps 先 pushq rbp、r14、rbx，再不经 subq 调用 ext。为何对齐？

- **A** 红区吸收未对齐，所以不需 subq
- **B** ext 使用前会自行重新对齐
- **C** 24 字节 push 加八字节返回地址为 32，是 16 的倍数
- **D** 每次 pushq 都保留十六字节对齐，所以任意次数都行

<details>
<summary>查看答案与解析</summary>

**答案**　C

psABI 3.2.2 规定入口 rsp+8 是十六倍数。三次 push 深度 24，24+8=32，无需 subq 即可对齐调用。

</details>

## 4. AArch64 keeps 的序言为 stp x29,x30,[sp,#-0x30]!; str x21,[sp,#0x10]; mov x29,sp; stp x20,x19,[sp,#0x20]。帧记录在哪？

- **A** 序言后 sp+0、sp+8：低地址 x29、高地址 x30，x29 指向它
- **B** 没有，保存 x21 的函数不需要帧记录
- **C** 在 x19/x20，因为最后一次 stp 保存记录
- **D** 帧顶部靠调用者，因为记录必须高于保存区

<details>
<summary>查看答案与解析</summary>

**答案**　A

前索引 stp 将 x29 存新 sp，x30 存 sp+8，mov x29,sp 指向这对值。相同函数的 Apple arm64 构建将记录放帧顶部。

</details>

## 5. -O0 System V eight_args 没有 subq，却把六参数寄存器存到 -0x8(rbp) 至 -0x30(rbp)。为什么合法？

- **A** 调用者已作为输出区分配 48 字节
- **B** 写到调用者帧，被调用者返回前拥有它
- **C** 它们在 rsp 下 128 字节红区，叶函数不发出覆盖它们的调用
- **D** 序言后 rbp 比 rsp 低 48，所以存储在 rsp 上方

<details>
<summary>查看答案与解析</summary>

**答案**　C

红区为 rsp 下方信号处理器不修改的 128 字节。Microsoft 和 AArch64 Linux 没有红区，同函数用 subq 或 sub sp 分配。

</details>

## 6. struct big big_ret(long long seed) 返回 32 字节结构，各 ABI 如何返回？

- **A** System V/Microsoft 用 rax:rdx，AArch64 用 x0:x1
- **B** 都在调用者帧返回地址上方返回
- **C** 缓冲地址在 rdi（seed 移 rsi）、rcx（seed 移 rdx）、x8（seed 留 x0）
- **D** 都用四寄存器，因为各有四结果寄存器

<details>
<summary>查看答案与解析</summary>

**答案**　C

psABI 将 32 字节组合类型分为 MEMORY，rdi 传隐含首参。Microsoft RCX 隐含指针将其余参数右移。AAPCS64 6.9 用间接结果 x8，不动 x0–x7。

</details>

## 7. radare2 6.2.4 对 -O2 System V eight_args 只列 rdi、rsi、rdx、r8、r9 和两栈槽。漏了什么、为什么？

- **A** r9，因为它是被调用者保留寄存器，工具跳过
- **B** rcx，因为唯一读取是 leaq (%rdx,%rcx),%rax 的索引
- **C** 没漏，函数只读取七个输入
- **D** 第二栈槽，因为 rsp 上十六字节在帧外

<details>
<summary>查看答案与解析</summary>

**答案**　B

源码有八参，字节在 lea 中读取 rcx 一次。本课将基址和索引都计为读，找到六寄存器参数。工具输出与源码不同，应记录为待验证发现。

</details>

## 8. Windows keeps 的 .xdata 是 01 07 04 00 07 32 03 30 02 70 01 60。含义是什么？

- **A** 版本 1，七字节序言，将三个非易失寄存器保存进影子空间
- **B** 版本 1，rbp 帧寄存器偏移 0x70，保存 rbx/rdi/rsi
- **C** 版本 1，七字节序言，在偏移 7 分配八字节，再推 rbx/rdi/rsi
- **D** 版本 1，七字节序言，在偏移 7 分配三十二字节，再列 rbx/rdi/rsi 的 push

<details>
<summary>查看答案与解析</summary>

**答案**　D

0x32 是 op 2（UWOP_ALLOC_SMALL）、info 3，故 3*8+8=32。0x30/0x70/0x60 是 op 0（UWOP_PUSH_NONVOL）与寄存器号 3/7/6，即 rbx/rdi/rsi，与序言 56 57 53 48 83 ec 20 一致。

</details>


[返回本课](docs/zh.md)
