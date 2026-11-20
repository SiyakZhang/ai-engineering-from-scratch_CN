# 验证关卡 · 自测

每题先选答案，再展开解析。

## 1. 验证门回答哪一个单一问题？

- **A** 模型快不快？
- **B** prompt 是否最优？
- **C** 这个任务真的完成了吗？（读取范围、规则、反馈和 diff 产物）
- **D** token 预算是否健康？

<details>
<summary>查看答案与解析</summary>

**答案**　C

门是工作台产物上的一个确定性函数，产出一个通过/失败的裁决。

</details>

## 2. 为什么门必须是确定性的？

- **A** 它省钱
- **B** 提供商要求它
- **C** 同一组产物必须每次都产生同样的裁决；LLM 评判属于审查者（定性），不属于门（状态）
- **D** 确定性是免费的

<details>
<summary>查看答案与解析</summary>

**答案**　C

把模型判断混进门里会瓦解「确定性/定性」的分工。

</details>

## 3. 门的覆盖（override）纪律是什么？

- **A** 任何人都能静默覆盖
- **B** block 级别的发现只能由人覆盖，需在签名审计日志中记录 override_reason 和 overridden_by 用户 id
- **C** 禁止覆盖
- **D** 覆盖需要一封经理邮件

<details>
<summary>查看答案与解析</summary>

**答案**　B

签名的覆盖落进 outputs/verification/overrides.jsonl；agent 不能自我覆盖。

</details>

## 4. 本课引用的「混合范式」（Hybrid Norm）配对是什么？

- **A** 热/冷 prompt
- **B** 可验证奖励（测试、schema、退出码）回答「它解决了问题吗？」；LLM 评分标准回答「它是否可读、安全、合规风格？」
- **C** GPU 和 CPU 拆分
- **D** 缓存 vs 无缓存

<details>
<summary>查看答案与解析</summary>

**答案**　B

Anthropic 2026 指引：门运行第一类；审查者（第 39 课）运行第二类。

</details>

## 5. 纵深防御如何对门分层？

- **A** 在合并时设单个门
- **B** pre-commit hook -> CI 状态检查 -> 工具前授权 hook -> 合并前门；每一层都是确定性的，一层失误由下一层捕获
- **C** 只有一条聊天提醒
- **D** 只有 IDE 警告

<details>
<summary>查看答案与解析</summary>

**答案**　B

多个不可绕过的层捕获单层会漏掉的东西。

</details>

## 6. coverage_floor（覆盖率下限）检查防范什么？

- **A** 过时的锁文件
- **B** 热路径延迟
- **C** agent 悄悄删掉失败的测试；若测得的覆盖率比下限或上次合并低超过 1 个百分点，门就失败
- **D** 冷启动

<details>
<summary>查看答案与解析</summary>

**答案**　C

没有下限，agent 可以悄悄降低覆盖率来让裁决保持绿色。

</details>

## 7. 什么时候 --strict 模式应该把每个 warn 升级为 block？

- **A** 永不
- **B** 只在周日
- **C** 总是
- **D** 发布分支、阻止上线的 PR、事故后分诊；不是日常默认，因为对一切都 strict 会腐蚀流程

<details>
<summary>查看答案与解析</summary>

**答案**　D

--strict 按分支选择开启；保留给高风险时刻。

</details>


[返回本课](docs/zh.md)
