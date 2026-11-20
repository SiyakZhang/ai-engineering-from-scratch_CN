# 重建并证明等价：差分测试、字节比较与证据循环 · 自测

每题先选答案，再展开解析。

## 1. 重建的 percent_change 通过四个手写测试。这证明什么？

- **A** 重建编译成相同字节
- **B** 重建对所有输入都等于原版
- **C** 反编译输出正确
- **D** 只证明重建与原版在这四个输入上一致

<details>
<summary>查看答案与解析</summary>

**答案**　D

测试集只证明其中输入一致。零值、负数、舍入和溢出单元才是重建出现分歧的位置。

</details>

## 2. 原版用 32 位 int 计算 (after - before) * 100 / before，重建用 64 位中间值。何时不同？

- **A** 永远不，因为转回 int 会消除差异
- **B** 32 位乘积回绕，且 before 不是 1 或 -1 时
- **C** 只有 before 为零时
- **D** before 为负的所有输入

<details>
<summary>查看答案与解析</summary>

**答案**　B

原版先回绕 32 位乘积再除，重建先除精确的 64 位乘积再截断。before 为 1 或 -1 时，截断后两者一致。

</details>

## 3. 两个 x86-64 ELF 目标含相同的 grade 46 字节代码，重定位字段也都是零。为什么还不足以证明一致？

- **A** RELA 目标无法比较
- **B** 机器码从不出现零字节
- **C** 函数大小存在 .rodata
- **D** 加数在 .rela.text 中，记录指向的表可能不同

<details>
<summary>查看答案与解析</summary>

**答案**　D

RELA 字段为零，加数在重定位记录中。应屏蔽字段、比较记录形状，再逐项读取比较目标常量。

</details>

## 4. 网格含 before = -1、after = 536870911。x86-64 原版执行 INT_MIN / -1 的 idiv，会发生什么？

- **A** 返回 INT_MIN
- **B** 保护分支返回 0
- **C** 返回 INT_MAX
- **D** 触发除法错误，进程收到 SIGFPE

<details>
<summary>查看答案与解析</summary>

**答案**　D

x86-64 idiv 在商无法放入时触发 #DE。AArch64 sdiv 同操作数返回 INT_MIN，因此基准依赖架构。

</details>

## 5. 2026 年 LLM 反编译改进研究中，构建率由 75% 升到 90% 时，行为匹配发生了什么？

- **A** 同幅度提高
- **B** 研究没有测量行为
- **C** 由 74% 降到 62%
- **D** 可读性降低，行为不变

<details>
<summary>查看答案与解析</summary>

**答案**　C

Liu、Raff、Micinski（arXiv 2609.05370）发现，杜撰类型、被调用者和保护使更多候选可编译，却使更少候选在模糊输入上匹配原版。

</details>

## 6. 主机无 C 编译器，第一条验证路径无法运行；两函数第二条路径通过。证明状态是什么？

- **A** pass，因为已运行的都通过
- **B** unknown，因为未验证主张不能聚合为 pass
- **C** pass，因为字节相等意味着行为相等
- **D** fail，因为一条路径没运行

<details>
<summary>查看答案与解析</summary>

**答案**　B

fail 优先，其次 unknown。未检查主张保持 unknown，unknown 不能变成 pass。

</details>


[返回本课](docs/zh.md)
