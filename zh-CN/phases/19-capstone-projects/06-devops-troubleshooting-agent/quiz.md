# 顶点项目 06 —— 面向 Kubernetes 的 DevOps 排障 agent · 自测

每题先选答案，再展开解析。

## 1. 排障 agent 的 RBAC 权限默认姿态是什么？

- **A** cluster-admin，以便它能自愈
- **B** 默认只读，破坏性动词被门控在一个独立服务器之后并需人工批准
- **C** 仅在受影响的命名空间内拥有 namespace-admin
- **D** 等同于值班工程师

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 2. agent 在根因分析时遍历的知识图谱是什么？

- **A** 节点是 K8s 对象加上遥测来源；边编码归属、调度和观察关系
- **B** 一张 GitHub 提交和 PR 评审的图
- **C** 一个最近重启 pod 的扁平列表
- **D** 按团队组织的 Prometheus 指标名

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 3. 用于 Slack 简报的根因假设是如何排序的？

- **A** 通过一个证据分数，综合近因性、具体性、图路径长度和引用数
- **B** 仅按模型的对数概率
- **C** 按告警名的字母顺序
- **D** 按它们被生成的顺序

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 4. 为什么审计日志要既记录 agent 执行过的命令，也记录它考虑过的命令？

- **A** Slack API 需要两者才能投递
- **B** ArgoCD 只接受被考虑过的命令
- **C** 重放攻击需要这两份列表
- **D** 评审者可以捕捉到那些 agent 差点就运行破坏性命令的险些失误

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 5. 哪种机制阻止 agent 在一次糟糕的部署上单方面回滚？

- **A** 由第二个 LLM 裁判对回滚投票
- **B** PagerDuty 自动暂停部署
- **C** GitOps 仓库上的分支保护
- **D** 破坏性工具驻留在一个独立的 MCP 服务器上，受来自 Slack 卡片的批准令牌保护

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 6. 评分细则衡量的 p50「达成假设时间」目标是多少？

- **A** 30 秒以内
- **B** 1 小时以内
- **C** 从告警到 Slack 简报 5 分钟以内
- **D** 在下一个值班班次之内

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 7. 用于评分 RCA 准确率的合成事件套件有多大？

- **A** 5 个场景
- **B** 1 个脚本化的演示事件
- **C** 20 个场景，覆盖 OOMKill、DNS 抖动、HPA 抖振、PVC 占满等
- **D** 100 条随机采样的生产告警

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>


[返回本课](docs/zh.md)
