# 经典评测指标 · 自测

每题先选答案，再展开解析。

## 1. 为什么 tokenizer 是在 metric 层选定，而不是在 runner 层？

- **A** tokenizer 是模型相关的，而 runner 看不到模型
- **B** Numpy 在 import 时就需要一个 tokenizer
- **C** tokenizer 定义了什么才算 token 匹配；换一个就会改变 benchmark
- **D** 无论选哪个 tokenizer，metric 实现都是 O(n)

<details>
<summary>查看答案与解析</summary>

**答案**　C

BLEU 和 F1 对分词很敏感。把 tokenizer 绑定到 metric 上能让分数可复现，也让你能指着规则说清楚。

</details>

## 2. 修正后的 n-gram 精度比朴素 n-gram 精度多做了什么？

- **A** 它用了不同的对数底
- **B** 它比朴素精度跑得更快
- **C** 它把每个候选 n-gram 的计数，按任一参考中出现的最大计数进行截断（clip）
- **D** 它返回 0 到 100 的值而不是 0 到 1

<details>
<summary>查看答案与解析</summary>

**答案**　C

按参考的上限截断，能防止候选靠反复重复某个高精度词来虚高分数。

</details>

## 3. BLEU 为什么要用简短惩罚（brevity penalty）？

- **A** 长候选会让几何平均在数值上不稳定
- **B** 简短惩罚替代了 n-gram 计数上限
- **C** 不加的话，一个只匹配上几个词的极短候选会拿到很高的精度，进而拿到不公平的高 BLEU
- **D** 它用来补偿加一平滑（additive-one smoothing）

<details>
<summary>查看答案与解析</summary>

**答案**　C

光看精度会奖励短输出。BP 用 exp(1 - r/c) 对比参考更短的候选做降权。

</details>

## 4. ROUGE-L 比较的是什么？

- **A** 候选与参考 token 序列的最长公共子序列（LCS）
- **B** 字符级的 Jaccard 系数
- **C** 4-gram 精度，对照任一参考的 4-gram
- **D** 候选串与参考串之间的 Levenshtein 距离

<details>
<summary>查看答案与解析</summary>

**答案**　A

ROUGE-L 用 LCS 长度，再算精度（LCS/候选长度）和召回（LCS/参考长度），结合 F-beta。

</details>

## 5. token 级 F1 在哪种情况下返回 1.0？

- **A** 预测和目标都为空时
- **B** 预测为空、目标非空时
- **C** 预测是目标的超集、还带了额外噪声时
- **D** 预测和目标恰好共享一个 token 时

<details>
<summary>查看答案与解析</summary>

**答案**　A

按惯例，空对空算完美匹配。任何非空目标搭配空预测都是 0.0。

</details>

## 6. 在打分函数里，为什么要按 metric_name 分派而不是按 category？

- **A** metric_name 比 category 更短
- **B** category 比 metric_name 更难校验
- **C** runner 访问不到 category 字段
- **D** 这样同一个 category 在不同任务里能用不同的 metric，并让分派器对 metric 无感知

<details>
<summary>查看答案与解析</summary>

**答案**　D

metric_name 才是契约。一个 summary 任务可以在某条记录上用 rouge_l、在另一条上用 bleu_4；分派器根本不用操心。

</details>


[返回本课](docs/zh.md)
