# 多模态评测 · 自测

每题先选答案，再展开解析。

## 1. 为什么单看训练 loss 不足以衡量一个多模态模型的质量？

- **A** loss 值是随机的
- **B** loss 很难算
- **C** 训练 loss 衡量的是在训练分布上的拟合；评测面（检索、VQA、captioning）衡量的是模型能否泛化到留出任务上
- **D** loss 是个字符串

<details>
<summary>查看答案与解析</summary>

**答案**　C

最小化 loss 是必要的，但不充分。在三个任务面上的留出指标，才衡量模型到底能做什么。

</details>

## 2. 在一个 100 样本的检索评测里，R@5 衡量的是什么？

- **A** 在 100 个候选里，正确匹配落进检索 top 5 的 query 所占的比例
- **B** 第五个 caption 总是对的
- **C** 每秒 5 个 query
- **D** 5% 的准确率

<details>
<summary>查看答案与解析</summary>

**答案**　A

R@K = 目标落在排序后 top K 候选里的 query 所占比例。越高越好。

</details>

## 3. 为什么 BLEU-4 对 1 到 4-gram 的 precision 取几何平均，而不是算术平均？

- **A** 算术平均更慢
- **B** 只要任何一个 n-gram precision 为零，几何平均就是零，这正是 BLEU 想要的严格匹配特性；平滑负责处理这个零的情况
- **C** 几何平均数值更大
- **D** PyTorch 只支持几何平均

<details>
<summary>查看答案与解析</summary>

**答案**　B

几何平均强制所有 n-gram 阶数都得有贡献；4-gram precision 为零会在平滑之前直接把分数压垮。

</details>

## 4. BLEU-4 里的简短惩罚（brevity penalty）防的是什么？

- **A** 长 caption 被惩罚
- **B** tokenizer 错误
- **C** 短 caption 靠只输出安全的高频 token 来刷高 precision；当生成长度 < 参考长度时 BP < 1
- **D** 内存泄漏

<details>
<summary>查看答案与解析</summary>

**答案**　C

没有 BP 的话，一个只匹配一个参考词的单词 caption 就能得 1.0。BP 会把过短生成的分数压低。

</details>

## 5. 为什么对同一个生成结果，多参考 BLEU 通常比单参考 BLEU 得分更高？

- **A** 数学不一样
- **B** 单参考是坏的
- **C** 生成里的每个 n-gram 都能匹配任意一个参考，所以参考越多，clipped count 越高
- **D** 参考会多占内存

<details>
<summary>查看答案与解析</summary>

**答案**　C

更多参考给了 n-gram 更多被匹配的机会；clipped count 增长，precision 随之上升。

</details>

## 6. 哪个评测面不用任何模型 embedding，只做 id 级别的匹配？

- **A** BLEU-4
- **B** 检索
- **C** 余弦相似度
- **D** VQA 精确匹配：预测的答案 id 直接和参考 id 比较，没有 embedding 这一步

<details>
<summary>查看答案与解析</summary>

**答案**　D

VQA 精确匹配是模型吐出答案 token 之后的一次整数比较，不涉及任何 embedding 或相似度计算。

</details>


[返回本课](docs/zh.md)
