# 混合记忆：向量 + 图 + KV · 自测

每题先选答案，再展开解析。

## 1. KV 存储最擅长处理哪类查询？

- **A** 对长对话的语义相似度
- **B** 「某时刻有效」的时间性查询
- **C** 共享某个计费实体的客户之间的可达性
- **D** 以（user, type, entity）为键的直接事实查找

<details>
<summary>查看答案与解析</summary>

**答案**　D

KV 在精确键上是 O(1) 的；向量用于相似度，图用于关系。

</details>

## 2. Mem0 在每次 add() 时并行写入的三个存储是什么？

- **A** Cache、queue、log
- **B** 向量、KV、图
- **C** Embedding、attention、FFN
- **D** Postgres、Redis、ClickHouse

<details>
<summary>查看答案与解析</summary>

**答案**　B

Mem0 把每次写入扇出到向量、KV 和图存储。

</details>

## 3. 哪三个维度喂给 Mem0 的融合分数（fusion score）？

- **A** 精确率、召回率、F1
- **B** 置信度、困惑度、BLEU
- **C** 相关性、重要性、新近性
- **D** 延迟、吞吐量、成本

<details>
<summary>查看答案与解析</summary>

**答案**　C

分数是相关性、重要性和新近性的加权和；权重按产品调优。

</details>

## 4. 当一个新进来的事实与现有的边矛盾时，Mem0g 会怎么做？

- **A** 把现有的边标记为无效但不删除，使时间性查询仍能遍历
- **B** 删除这条边
- **C** 抛出异常
- **D** 重写 user_id

<details>
<summary>查看答案与解析</summary>

**答案**　A

软失效（soft invalidation）保留了历史，以便进行时间性（某时刻有效）查询。

</details>

## 5. 为什么本课建议按产品调优融合权重？

- **A** 向量库拒绝相等的权重
- **B** Apache 2.0 要求这样
- **C** 对聊天 agent 新近性占主导，对合规 agent 重要性占主导，对检索 agent 相关性占主导
- **D** 提供商要求这样

<details>
<summary>查看答案与解析</summary>

**答案**　C

不同产品对相关性/重要性/新近性想要不同的偏置；一套权重并不适合所有情况。

</details>

## 6. Mem0 使用的作用域分类（scope taxonomy）是什么？

- **A** User、session、agent
- **B** Read、write、admin
- **C** Local、regional、global
- **D** Public、private、secret

<details>
<summary>查看答案与解析</summary>

**答案**　A

作用域为 user（跨会话）、session（单个线程）、agent（每实例状态）。

</details>

## 7. 在此模式中，embedding 漂移（embedding drift）是什么，本课建议如何缓解？

- **A** embedding API 更换了 URL；固定一个域名
- **B** embedding 整数溢出；改用 float64
- **C** 向量被加密；轮换密钥
- **D** 随着语料增长，向量检索质量下降；定期对使用最多的 top-N 记录重新做 embedding

<details>
<summary>查看答案与解析</summary>

**答案**　D

定期对热记录重新做 embedding，能在语料增长时保持检索质量稳定。

</details>


[返回本课](docs/zh.md)
