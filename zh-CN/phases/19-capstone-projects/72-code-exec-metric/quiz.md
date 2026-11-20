# 代码执行评测指标 · 自测

每题先选答案，再展开解析。

## 1. 为什么 runner 要为每个候选起一个全新的 Python 子进程，而不是内联调用 exec？

- **A** 它避免污染 builtins
- **B** exec 在现代 Python 里已经废弃了
- **C** 它把超时、输出溢出和危险的 import 与宿主 eval 进程隔离开
- **D** 它比 exec 更快

<details>
<summary>查看答案与解析</summary>

**答案**　C

候选代码里的死循环或失控的内存分配只会拖垮子进程。宿主 eval 仍然能继续推进。

</details>

## 2. 一个任务有三条断言，两条通过、一条失败，分数是多少？

- **A** 0.5
- **B** 0.0
- **C** 0.667
- **D** 1.0

<details>
<summary>查看答案与解析</summary>

**答案**　C

分数等于通过数除以总数。三分之二是 0.667。退出码为 assertion_fail。

</details>

## 3. 当候选代码无法解析时，runner 返回哪个退出码？

- **A** assertion_fail
- **B** timeout
- **C** syntax_error
- **D** error

<details>
<summary>查看答案与解析</summary>

**答案**　C

compile() 在 runner 内部抛出 SyntaxError，内层脚本捕获它并写入 exit_code=syntax_error。

</details>

## 4. 为什么挂钟超时（wall-clock timeout）才是真正承重的控制手段，而不是 import 黑名单？

- **A** 大多数失败都是死循环，而且铁了心的攻击者能绕过任何进程内黑名单
- **B** subprocess.run 不支持黑名单
- **C** 挂钟在编译时就检查了
- **D** Python 里没法禁掉 import

<details>
<summary>查看答案与解析</summary>

**答案**　A

黑名单只能拦住偷懒的代码，超时才能拦死循环。黑名单是兜底，超时才是底线。

</details>

## 5. 当 n - c < k 时，pass_at_k(n, c, k) 返回什么？

- **A** 抛出 ValueError
- **B** 一，因为采样里必然至少包含一个通过的解
- **C** 零，因为这个采样没有定义
- **D** c / n，经验通过率

<details>
<summary>查看答案与解析</summary>

**答案**　B

如果失败数比采样规模还少，那么任何大小为 k 的采样都必然至少含一个通过项，所以概率为 1。

</details>

## 6. runner 如何暴露输出溢出，又为什么上限是 256 KB？

- **A** 分数值，用两位小数的百分比表示
- **B** 只看 stderr；大小与操作系统管道默认值一致
- **C** 子进程的 stdout 是流式读取的；一旦累计运行量越过 256 KB，子进程就被杀掉，任务记为 exit_code=error，detail 为「output overflow」
- **D** 候选源码大小，设上限好让生成代码保持精简

<details>
<summary>查看答案与解析</summary>

**答案**　C

这个上限是为了保护宿主。狂刷 stdout 的候选代码会被中途杀掉；runner 把结果归一化为 exit_code=error、detail 为「output overflow」，而不是新造一个退出码。

</details>


[返回本课](docs/zh.md)
