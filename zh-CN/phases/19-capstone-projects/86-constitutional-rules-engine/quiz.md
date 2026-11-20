# Constitutional 规则引擎 · 自测

每题先选答案，再展开解析。

## 1. 为什么要用声明式的 YAML constitution，而不是临时写在代码里的检查？

- **A** 因为 YAML 解析比 Python 快
- **B** 因为标准库更偏好 YAML
- **C** 因为 YAML 里的规则非工程师也能 review，能进版本控制，还能不改代码就替换
- **D** 因为 YAML 支持 anchor

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 2. 每条规则至少必须具备哪些字段？

- **A** name、regex、fix
- **B** id、owner、timestamp
- **C** predicate、severity、owner
- **D** name、severity、must、explanation

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 3. 这个 engine 是怎么组合 predicate 的？

- **A** 通过 all_of、any_of 和 not_ 递归地包裹原子 predicate
- **B** 每条规则只能用单个 contains_regex
- **C** 靠一个神经网络 classifier
- **D** 靠把置信度分数相乘

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 4. applies_when 的作用是什么？

- **A** 它覆盖 severity
- **B** 它永远求值为 true
- **C** 它挑选 fixer 操作
- **D** 它给 must predicate 加了道门：不适用的规则会被记为 not_applicable，而不是 violation

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 5. Fixer 是做什么的？

- **A** 它重写规则文件
- **B** 它调用一个远程模型来修复文本
- **C** 它应用每条规则上声明的 fix（append、prepend、replace_regex），产出一段修订后的文本
- **D** 它从 fix 里算出 severity

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 6. 为什么 demo 在 fixer 之后要再跑一遍 engine？

- **A** 因为第一遍只是 dry run
- **B** 为了验证修订后的文本确实满足规则，并暴露出 fixer 在本地修不了的规则
- **C** 为了重新加载 constitution
- **D** 为了把报告撑大

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>


[返回本课](docs/zh.md)
