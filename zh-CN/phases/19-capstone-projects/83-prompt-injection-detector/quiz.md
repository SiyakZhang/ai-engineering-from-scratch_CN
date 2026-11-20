# Prompt 注入检测器 · 自测

每题先选答案，再展开解析。

## 1. 对于一条 prompt，detector 返回的是什么？

- **A** 模型完整的 system prompt
- **B** 返回 rulebase 里的全部规则列表
- **C** 一个分类，外加一个落在 [0, 1] 区间的置信度
- **D** 只返回一个布尔的拦截决策

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 2. 为什么 normalize 要在 substring 和 regex 规则之前先跑？

- **A** 因为 regex 比 substring 慢
- **B** 因为标准库禁止在原始文本上跑规则
- **C** 因为 normalize 能减小磁盘上的文件体积
- **D** 因为 normalize 会把 base64、rot13、zero-width 插入这类隐藏 token 暴露出来，交给下游规则处理

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 3. 对于分类 C，true positives = 6，false positives = 2，precision 是多少？

- **A** 0.86
- **B** 0.50
- **C** 0.60
- **D** 0.75

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 4. 为什么 benign prompt 语料也是评估的一部分？

- **A** 为了预训练这些规则
- **B** 为了算出攻击上的 recall
- **C** 为了把准确率数字做得好看一点
- **D** 为了在安全文本上测出 false-positive 率，抓出那些过于宽泛的规则

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 5. 当没有任何规则命中时，analyze 方法会怎么做？

- **A** 返回分类 benign，置信度为 0.0
- **B** 返回最近一次尝试的那条规则的分类
- **C** 抛出异常
- **D** 返回一个随机分类

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 6. 为什么本课主张 detector 并不等于 safety gate？

- **A** 因为 detector 是用 Python 实现的
- **B** 因为这些规则是以数据形式存储的
- **C** 因为 detector 只是 gate 将要组合的众多信号之一，而每个信号在 precision 和 recall 之间的取舍各不相同
- **D** 因为 detector 跑得太快，没什么用

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>


[返回本课](docs/zh.md)
