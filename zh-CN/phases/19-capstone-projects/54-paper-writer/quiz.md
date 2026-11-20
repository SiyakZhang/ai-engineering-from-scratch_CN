# 论文生成器 · 自测

每题先选答案，再展开解析。

## 1. 为什么 writer 在写任何正文之前，先把 sections、figures 和 citations 声明为数据？

- **A** 因为模型需要 system prompt
- **B** 因为 BibTeX 无法解析前向引用
- **C** 因为结构就是契约：harness 可以在生成正文之前就验证完整性
- **D** 因为 LaTeX 要求前向声明

<details>
<summary>查看答案与解析</summary>

**答案**　C

结构优先让 harness 能在调用正文生成器之前就验证唯一性、引用覆盖和图表覆盖。骨架就是契约。

</details>

## 2. 图表注入步骤从实验 manifest 中产生什么？

- **A** 参考文献存根
- **B** 带图表描述的模型 prompt
- **C** 从产物编译出的 PDF
- **D** 一个 Figure 记录列表，带有稳定的 id 和归一化到论文目录的路径

<details>
<summary>查看答案与解析</summary>

**答案**　D

read_experiment_manifest 返回 Figure 记录。id 是确定性的，路径是归一化的，标题来自 manifest。

</details>

## 3. 哪种验证失败会在写入任何文件之前抛出 PaperValidationError？

- **A** 摘要超过 200 个词
- **B** 作者数量是奇数
- **C** 某个 section 引用了一个未在参考文献中声明的 key
- **D** 图表路径在磁盘上不存在

<details>
<summary>查看答案与解析</summary>

**答案**　C

缺少参考文献 key、重复图表 id、空标题、空摘要以及未知图表引用都会抛出 PaperValidationError。磁盘上是否存在不做检查，因为 LaTeX 编译器会在后面执行这个校验。

</details>

## 4. 为什么正文生成器是一个注入 PaperWriter 的 callable，而不是它的一个方法？

- **A** 因为 Python 不允许方法以 Paper 为参数
- **B** 因为 dataclass 不能持有状态
- **C** 因为 LaTeX 要求回调
- **D** 因为测试可以换一个确定性的 MockProseGenerator 替代模型调用，而不需要改动 writer

<details>
<summary>查看答案与解析</summary>

**答案**　D

writer 把正文生成器作为依赖注入。测试替换成 MockProseGenerator，生产替换成模型调用。writer 本身不变。

</details>

## 5. PaperWriter.write 成功时输出哪三个文件？

- **A** outline.json、paper.tex、figures.tar
- **B** paper.tex、paper.pdf、references.bib
- **C** paper.tex、references.bib、manifest.json
- **D** manifest.json、prose.txt、paper.pdf

<details>
<summary>查看答案与解析</summary>

**答案**　C

paper.tex 是 LaTeX 源文件。references.bib 是参考文献。manifest.json 是 critic loop 下一步读取的结构化产物。

</details>

## 6. 为什么 manifest 是 writer 契约的一部分，而不只有 LaTeX 文件？

- **A** 因为下游工具（评审、仪表盘）读取的是结构化 manifest，而不是 LaTeX
- **B** 因为 manifest.json 是 BibTeX 唯一接受的文件
- **C** 因为 LaTeX 太大无法解析
- **D** 因为 LaTeX 编译器拒绝无类型的 section

<details>
<summary>查看答案与解析</summary>

**答案**　A

manifest 是面向下游阶段的稳定接口。评审和仪表盘查看 manifest.json。LaTeX 是人类可读的产物，不是机器接口。

</details>


[返回本课](docs/zh.md)
