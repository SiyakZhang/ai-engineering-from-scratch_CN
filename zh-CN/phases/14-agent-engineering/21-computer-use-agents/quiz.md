# 计算机操作：Claude、OpenAI CUA、Gemini · 自测

每题先选答案，再展开解析。

## 1. Claude 的计算机使用接收什么输入，发出什么？

- **A** 输入截图（基于视觉），输出键盘/鼠标命令
- **B** 输入 JSON，输出 SQL
- **C** 输入 DOM XML，输出 JavaScript
- **D** 输入无障碍树，输出键盘/鼠标命令

<details>
<summary>查看答案与解析</summary>

**答案**　A

Claude 读取像素并发出键盘/鼠标动作；不使用操作系统的无障碍 API。

</details>

## 2. Gemini 2.5 计算机使用的标志性安全特性是什么？

- **A** 一个每步安全服务，在执行前评估每个动作并拒绝不安全的
- **B** 硬编码的 WAF 规则
- **C** 默认只读模式
- **D** 强制的验证码

<details>
<summary>查看答案与解析</summary>

**答案**　A

Gemini 2.5 计算机使用以一个每步安全分类器作为标志性特性。

</details>

## 3. 本课把什么认定为这三个模型共同的不可信输入？

- **A** 没有；一切都可信
- **B** 只有 HTTPS 响应
- **C** 截图、DOM 文本、工具输出、PDF 内容，任何被检索回来的东西
- **D** 只有 PDF 内容

<details>
<summary>查看答案与解析</summary>

**答案**　C

只有直接的用户指令才算授权；其余一切都是不可信的。

</details>

## 4. 本课为 OpenAI CUA 发布时引用了哪些 OSWorld / WebArena 数字？

- **A** 未报告数字
- **B** OSWorld 38.1%、WebArena 58.1%、WebVoyager 87%
- **C** OSWorld 99%、WebArena 99%
- **D** OSWorld 0%、WebArena 0%

<details>
<summary>查看答案与解析</summary>

**答案**　B

这些是引用的发布时数字。

</details>

## 5. 下列哪个防御模式不在 2026 年的收敛清单里？

- **A** 导航目标的允许列表/封禁列表
- **B** 每步安全分类器
- **C** 对敏感动作的人在回路
- **D** 为省时间自动点掉对话框

<details>
<summary>查看答案与解析</summary>

**答案**　D

自动点掉对话框与安全恰恰相反；本课建议显式确认。

</details>

## 6. 本课强调的针对计算机使用 agent 的主要攻击是什么？

- **A** 一个恶意页面或 PDF 在被检索的内容里嵌入指令，模型把它当作用户意图
- **B** 网络中断
- **C** 操作系统更新滞后
- **D** 渲染缓慢

<details>
<summary>查看答案与解析</summary>

**答案**　A

把截图或 DOM 文本当作授权来信任，是经典的间接 prompt 注入失败。

</details>

## 7. 什么时候特别推荐人在回路确认？

- **A** 永不
- **B** 在只读导航时
- **C** 只在模型主动询问时
- **D** 在登录、购买、删除文件这类敏感动作上

<details>
<summary>查看答案与解析</summary>

**答案**　D

敏感动作（涉及金钱、数据暴露、新登录）需要显式的人工确认。

</details>


[返回本课](docs/zh.md)
