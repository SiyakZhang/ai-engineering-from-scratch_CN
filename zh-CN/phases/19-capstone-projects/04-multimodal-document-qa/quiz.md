# 顶点项目 04 —— 多模态文档问答（视觉优先的 PDF、表格、图表） · 自测

每题先选答案，再展开解析。

## 1. 为什么在金融 PDF 和科学论文上，2026 年的前沿做法更偏好视觉优先的延迟交互（late interaction），而非「先 OCR 再处理文本」？

- **A** OCR 无法在 GPU 上运行
- **B** 视觉模型每页更便宜
- **C** OCR 比渲染更慢
- **D** OCR 流水线会弄乱旋转的表格、密集的公式和图表图像，丢失一半信号

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 2. 在 ColPali 式检索中，延迟交互（late interaction）是什么意思？

- **A** 嵌入被推迟到评测时才计算
- **B** 嵌入在用户点击某个结果后才计算
- **C** 每个查询 token 都与每个 patch token 打分，再通过 MaxSim 把逐 token 的最大值相加
- **D** 重排器只在最终候选上运行

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 3. ColQwen 嵌入每页大约产生多少个 patch 向量，这造成了什么存储问题？

- **A** 正好 128 个向量，能干净地装进任何向量数据库
- **B** 16 个向量，存储开销可忽略
- **C** 每页约 2048 个 patch 向量，相比单向量索引使原始存储急剧膨胀
- **D** 每页 1 个向量，没有存储问题

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 4. DocPruner 在这条流水线中做什么？

- **A** 在摄入前移除重复的 PDF 页面
- **B** 围绕证据区域裁剪边界框
- **C** 为更短的向量重写查询嵌入
- **D** 通过保留约 50% 的高信号 patch 来压缩多向量索引，且准确率损失可忽略

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 5. 为什么仍要为某些页面拼接进一条 OCR 文本通道？

- **A** VLM 无法读取 180 DPI 的图像
- **B** 它能提升 PDF 渲染质量
- **C** OCR 是主要的检索模态
- **D** 公式密集和表格繁多的页面，在图像之外辅以文本回退会受益

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 6. 本毕业项目针对视觉优先检索评估，瞄准哪个基准？

- **A** SWE-bench Pro
- **B** ViDoRe v3
- **C** MMLU-Pro
- **D** RewardBench-2

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 7. 评分细则中所说的「证据区域接地（evidence-region grounding）」是什么意思？

- **A** 重排器在 p99 长尾处的延迟
- **B** 每次查询检索到的页面总数
- **C** 被引用的边界框中实际包含答案片段的比例
- **D** DocPruner 达成的压缩比

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>


[返回本课](docs/zh.md)
