# 端到端研究 Demo · 自测

每题先选答案，再展开解析。

## 1. 这节课里 demo 的职责是什么？

- **A** 在每个分支上调用真实的语言模型
- **B** 用一个全新框架替换之前的课程
- **C** 通过普通的 Python import 把前面课程中的基元组合起来
- **D** 拿调度器和一个 baseline 做基准测试

<details>
<summary>查看答案与解析</summary>

**答案**　C

demo 是一次组合测试。每个阶段存在于自己的课程中。demo 导入它们并组装报告。没有新框架，没有新抽象。

</details>

## 2. 为什么这节课用 importlib 加载前面的课程，而不是普通的 package import？

- **A** 因为 asyncio 要求 importlib
- **B** 因为 importlib 更快
- **C** 因为每节前置课程是独立的 code/ 文件夹，不是已安装的 package；importlib 按文件路径加载它们
- **D** 因为各课程共享模块名会冲突

<details>
<summary>查看答案与解析</summary>

**答案**　C

各课程不是已安装的 package。每节课在自己的 code/ 文件夹里有一个 main.py。importlib.util.spec_from_file_location 按路径加载它们，不会污染全局模块命名空间。

</details>

## 3. 当多个分支都触发了论文生成时，最佳结果选择器如何决定？

- **A** 随机选择以保证公平
- **B** 选均值奖励最高的分支，平局时按 branch id 字母序打破
- **C** 选第一个触发的分支
- **D** 选运行实验最多的分支

<details>
<summary>查看答案与解析</summary>

**答案**　B

最高均值胜出。平局按 branch id 打破，保证 demo 的确定性。随机选择会破坏确定性测试。

</details>

## 4. 当调度器报告零次论文触发时，选择器抛出什么错误？

- **A** NoTriggerError，在 writer 运行之前就短路了 demo
- **B** PaperValidationError
- **C** ValueError
- **D** 返回 None

<details>
<summary>查看答案与解析</summary>

**答案**　A

NoTriggerError 是类型化的失败模式。返回 None 会让 writer 在畸形输入上运行，然后在后面以更难定位的错误失败。

</details>

## 5. 为什么 demo 在确定性测试中用相同种子运行两次？

- **A** 为了检测内存泄漏
- **B** 为了证明调度器是公平的
- **C** 为了断言两次运行中选中的分支、奖励和论文 section id 完全一致
- **D** 为了执行两次 asyncio

<details>
<summary>查看答案与解析</summary>

**答案**　C

确定性是契约的一部分。用相同种子的两次运行必须产出相同的产物。这个测试锁定了这一点。

</details>

## 6. 成功运行后，demo 报告包含什么？

- **A** 仅实验数量和一个状态字符串
- **B** 仅最终 LaTeX 文件
- **C** scheduler_report、best_branch、best_reward、critic_result、paper_manifest 和 stop_reason
- **D** 模型 prompt 和 completion 日志

<details>
<summary>查看答案与解析</summary>

**答案**　C

每个阶段的输出都保留了下来。报告是上游输出的组合，不是变换后的摘要。下游工具读 manifest；调试人员读 scheduler_report 里的 trace。

</details>


[返回本课](docs/zh.md)
