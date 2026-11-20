# 内容分类器集成 · 自测

每题先选答案，再展开解析。

## 1. 输入侧已经检查过了，为什么还要跑输出侧的 classifier？

- **A** 因为任何输入侧的绕过都会产生一个用户将会看到的输出，而输出是抓住它的最后一道关
- **B** 因为输入 classifier 已经废弃了
- **C** 因为标准库要求两侧都得有
- **D** 为了故意让系统变慢

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 2. 本课接入了哪三个 classifier？

- **A** OCR、ASR、TTS
- **B** 情感、语言、长度
- **C** toxicity、PII、instruction-leakage
- **D** 质量、事实性、引用

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 3. 当一个 verdict 是 high、另一个是 medium 时，router 会怎么做？

- **A** 只执行 medium 对应的动作
- **B** 依次执行两个动作
- **C** 取最高 severity 并应用对应动作；block 优先于 redact
- **D** 丢掉两个 verdict，直接放行原文

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 4. 为什么 PII classifier 内部要用 Luhn 校验？

- **A** 为了把数字转成字母
- **B** 为了压缩 regex
- **C** 为了把形状像信用卡的数字串和任意数字序列区分开，且 false positive 很低
- **D** 为了算出 SSN

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 5. instruction-leakage classifier 是怎么做判定的？

- **A** 靠调用另一个模型
- **B** 靠数 token 数量
- **C** 靠计算输出与已知 system prompt 之间的 trigram 余弦相似度，再配一个阈值
- **D** 靠检测输出里的花括号

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 6. 为什么 toxicity classifier 要在左侧一个小窗口里检查否定词（negation）？

- **A** 为了跳过像「you are not stupid」这种命中，免得 classifier 把常见的安慰话也过度 redact 掉
- **B** 为了提高 false-positive 率
- **C** 为了拖慢 regex
- **D** 因为 Unicode 要求必须处理否定

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>


[返回本课](docs/zh.md)
