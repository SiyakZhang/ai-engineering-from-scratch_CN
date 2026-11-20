# 语言模型评测框架 · 自测

每题先选答案，再展开解析。

## 1. 在评测框架的 JSONL 格式中，定义一个 task example 的四个字段是什么？

- **A** input 和 output
- **B** name, score, payload, vendor
- **C** id, prompt, targets, metric，以及一个可选的 extras 字典用于放指标需要的附加数据。
- **D** weights 和 bias

<details>
<summary>查看答案与解析</summary>

**答案**　C

JSONL 行就是契约。extras 字段让 code_exec 指标可以传 io_pairs 而不污染 prompt。

</details>

## 2. 为什么 metric 函数签名是 (prediction, targets, extras) -> float？

- **A** 它返回的是整数。
- **B** 随意选择。
- **C** 这是能同时处理单 target 字符串匹配、多 reference rouge-l 和带附加数据的 code_exec 的最小签名，同时保持分数在可比较的 [0.0, 1.0] 范围内。
- **D** 它需要 model 对象。

<details>
<summary>查看答案与解析</summary>

**答案**　C

[0,1] 范围内的浮点数意味着 per-task 和 overall 分数都是可解释的平均值。extras 槽位是 code_exec 获取 io_pairs 的方式。

</details>

## 3. code_exec 指标如何防御恶意预测？

- **A** 它拒绝任何包含 def 的内容。
- **B** 它在一个剥离了 __builtins__ 的命名空间里运行预测，只暴露少数安全名称；import 语句会失败因为 importer 不在作用域内。
- **C** 它使用沙箱容器。
- **D** 它没有防御。

<details>
<summary>查看答案与解析</summary>

**答案**　B

这节课的安全命名空间把 builtins 削减到少数几个名称。测试断言 import os 返回分数 0.0 而不是被执行。

</details>

## 4. Model adapter 抽象带来了什么好处？

- **A** 没有好处。
- **B** torch 要求它。
- **C** 它让模型更快。
- **D** 它是框架中唯一与模型相关的代码；换一个 adapter 指向新的供应商，task、metric、runner 和排行榜格式全都不用动。

<details>
<summary>查看答案与解析</summary>

**答案**　D

课程里的 ToyAdapter 是一个确定性的模式匹配器。一个面向真实供应商的 HttpAdapter 有同样的 generate(prompts) -> list[str] 接口。

</details>

## 5. 为什么排行榜 JSON 带一个类似 leaderboard.v1 的 schema 字符串？

- **A** 随意的。
- **B** 为了 SEO。
- **C** 压缩文件用。
- **D** 这样未来格式变更时升级版本号，下游 dashboard 可以据此分发处理逻辑而不是静默出错。

<details>
<summary>查看答案与解析</summary>

**答案**　D

跟第 47 课 checkpoint payload 一样的套路。Schema 字段就是迁移钩子。

</details>

## 6. 看排行榜，overall_score 怎么算的？比较两次 run 时要注意什么？

- **A** 正确数求和。
- **B** 随机采样。
- **C** 取最好的 task 分数。
- **D** Per-task 分数（各在 [0,1]）取平均；比较时还要 diff 分数变动的 task 的 per-example 预测，因为光看分数会掩盖到底哪些样例退步了。

<details>
<summary>查看答案与解析</summary>

**答案**　D

Per-task mean 的 mean 让每个 task 权重相等。用 --include-per-example 把预测级别的证据放在分数旁边，这样退步就看得到了。

</details>


[返回本课](docs/zh.md)
