# 推理指标 —— TTFT、TPOT、ITL、Goodput、P99 · 自测

每题先选答案，再展开解析。

## 1. 哪些组成部分主导了 TTFT（首 token 时延）？

- **A** 权重的磁盘 I/O
- **B** 排队时间、网络请求时间和 prefill 时间
- **C** 仅 decode 的前向计算时间
- **D** Tokenizer 的 GIL 开销

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 2. 本课把哪个指标称为对产品真正重要的那个？

- **A** 平均 ITL
- **B** Goodput —— 同时满足所有 SLO 约束的请求所占比例
- **C** 以每秒 token 数计的总吞吐量
- **D** GPU 占空比

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 3. 为什么用平均值来报告 LLM 延迟是错误的统计量？

- **A** LLM 延迟分布是右偏的；用户会经常遭遇被平均值掩盖的 P99 离群值
- **B** GenAI-Perf 不支持平均值
- **C** 平均值只适用于 prefill，不适用于 decode
- **D** 平均值在流式响应上永远无法计算

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 4. 为什么 GenAI-Perf 和 LLMPerf 对同一次运行的 TPOT 会得出不一致的结果？

- **A** GenAI-Perf 只在 Blackwell 上运行
- **B** 它们采样了不同的请求
- **C** LLMPerf 用微秒，GenAI-Perf 用毫秒
- **D** GenAI-Perf 在计算 ITL 时排除了 TTFT，而 LLMPerf 把它包含进去，因此工具的选择改变了数值

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 5. 对于长输出请求（>500 个 token），哪个指标主导了端到端延迟？

- **A** 网络响应时间
- **B** TTFT
- **C** TPOT 乘以输出长度
- **D** 冷启动时间

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 6. 哪一组最能体现本课对 2026 年一个 70B 对话模型所设定的合理面向消费者的 SLO？

- **A** TTFT P99 800 ms，TPOT P99 25 ms，输出 <300 token 时 E2E P99 3 秒，goodput >= 99%
- **B** TTFT P99 8 秒，TPOT P99 200 ms，goodput 50%
- **C** 平均 TTFT 10 ms，平均 TPOT 1 ms
- **D** 仅 P50，不设更高的分位数

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>


[返回本课](docs/zh.md)
