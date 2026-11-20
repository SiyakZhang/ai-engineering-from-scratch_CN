# 顶点项目 14 —— 推测解码推理服务器 · 自测

每题先选答案，再展开解析。

## 1. 推测解码背后的两层机制是什么？

- **A** 一个嵌入模型和一个综合器
- **B** draft 模型提议 k 个候选 token；目标模型一次性验证它们
- **C** 两个目标模型逐 token 交替
- **D** 一个检索缓存和一个重排器

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 2. EAGLE-3 做了 ngram draft 所没有做的什么事？

- **A** 它在目标模型的隐藏状态上训练 draft head，以获得更高的接受率
- **B** 它完全避免分词
- **C** 它只在 CPU 上运行
- **D** 它替换目标模型

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 3. 为什么要在批次大小 1、8、32 上报告 p99 长尾延迟？

- **A** 稳态的每秒 token 数可能掩盖了：被拒绝时的验证趟（verify pass）比普通 decode 更昂贵
- **B** vLLM 无法服务低于 8 的批次大小
- **C** p99 只在批次大小 32 时才重要
- **D** 长尾延迟与批次大小无关

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 4. 为什么当流量分布变化时接受率会漂移？

- **A** 操作系统调度器重新洗牌 GPU 显存
- **B** 量化在运行时发生变化
- **C** draft 的对齐取决于输入分布：ShareGPT、代码和领域数据会激发不同的模式
- **D** vLLM 每小时轮换模型

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 5. 该部署基于哪个 Kubernetes HPA 信号进行扩缩？

- **A** CPU 利用率
- **B** 推理请求的队列等待时间（queue-wait time）
- **C** 集群自动扩缩节点
- **D** 磁盘 IOPS

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 6. 相比串行 EAGLE-3，P-EAGLE 增加了什么？

- **A** 移除目标模型
- **B** 量化到 FP4 权重
- **C** 跨 draft 分支树的并行推测，在一次目标趟中验证
- **D** 自动数据集策展

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 7. 相对非推测基线，细则要求达到哪个吞吐目标？

- **A** 任何高于基线的提升
- **B** 任何质量下都恰好 10 倍吞吐
- **C** 质量匹配时约 1.1 倍
- **D** 在两个模型上、质量匹配时至少 2.5 倍

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>


[返回本课](docs/zh.md)
