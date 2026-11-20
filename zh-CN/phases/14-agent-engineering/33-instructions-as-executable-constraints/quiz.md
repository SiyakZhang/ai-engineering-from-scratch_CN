# Agent 指令即可执行约束 · 自测

每题先选答案，再展开解析。

## 1. 愿景性规则（aspirational rule）和操作性规则（operational rule）之间的区别是什么？

- **A** 愿景性规则没有检查（「小心点」）；操作性规则携带一个工作台可运行的机器可校验函数
- **B** 操作性规则更长
- **C** 愿景性规则收费；操作性规则免费
- **D** 愿景性规则需要一个经理

<details>
<summary>查看答案与解析</summary>

**答案**　A

操作性规则是可测试的；愿景性规则只是愿望。

</details>

## 2. 本课用哪五个类别覆盖了大多数规则？

- **A** 低、中、高、严重、致命
- **B** Read、write、exec、fork、exit
- **C** 启动、禁止、完成定义、不确定性、审批
- **D** Plan、act、reflect、refine、ship

<details>
<summary>查看答案与解析</summary>

**答案**　C

启动、禁止、完成定义（definition of done）、不确定性处理、审批边界是这五类。

</details>

## 3. 哪个严重级标签会停止执行并要求操作员覆盖（override）？

- **A** info
- **B** soft
- **C** block
- **D** warn

<details>
<summary>查看答案与解析</summary>

**答案**　C

block 是硬失败；warn 是标注；info 是报告。

</details>

## 4. 为什么本课建议在写入时就标注严重级？

- **A** linter 要求它
- **B** 团队早期会高估严重级，并在截止压力下削弱它；在前面就写好严重级能强制完成校准
- **C** 它省 token
- **D** 它在 markdown 里更好看

<details>
<summary>查看答案与解析</summary>

**答案**　B

严重级校准必须是有意为之的，而不是在压力下事后补的。

</details>

## 5. 「markdown 为源、JSON 为缓存」的模式做什么？

- **A** 替换 markdown
- **B** 加密规则
- **C** agent-rules.md 是编写的文件；agent-rules.lock.json 是由 pre-commit hook 重新生成的热路径缓存（与 package.json + lock 形态相同）
- **D** 禁用审查

<details>
<summary>查看答案与解析</summary>

**答案**　C

markdown 保持可审查；JSON 解析留在热路径之外。

</details>

## 6. 规则过期（rule expiry）作为一种强制机制是什么？

- **A** 规则自动过期；无需审查
- **B** 超过 24 小时的规则会 fail closed
- **C** 每条规则携带一个 expires_at（默认 90 天）；从未触发的规则会触发一次季度审查，要为它辩护、削弱或删除
- **D** 缓存满时规则过期

<details>
<summary>查看答案与解析</summary>

**答案**　C

Cloudflare 的数据显示带过期的规则集保持在 30 条以下；不带过期的则增长到 80+ 条未使用规则。

</details>

## 7. 规则与框架护栏（guardrails）有什么关系？

- **A** 两者只需其一
- **B** 护栏是规则的替代品
- **C** 护栏在运行时强制执行规则；规则集是这些护栏所实现的、人类可读的契约
- **D** 规则替换护栏

<details>
<summary>查看答案与解析</summary>

**答案**　C

两者都需要：运行时捕获违规；规则集证明运行时在做正确的事。

</details>


[返回本课](docs/zh.md)
