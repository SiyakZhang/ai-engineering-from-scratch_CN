# 大规模语料下载器 · 自测

每题先选答案，再展开解析。

## 1. 为什么下载器要为每个分片维护一个单独的 .partial.json checkpoint？

- **A** 因为 urllib 要求这样做。
- **B** 这样恢复下载时可以对已验证字节做 sha256 前缀校验再追加，杜绝静默损坏。
- **C** 为了让缓存目录看起来整齐。
- **D** 为了存储 URL 以防分片文件迁移。

<details>
<summary>查看答案与解析</summary>

**答案**　B

Checkpoint 记录了 verified_bytes 和这些字节的 sha256；恢复时只有磁盘上的哈希匹配才会继续。

</details>

## 2. LSH band 方案能做到而精确哈希去重做不到的是什么？

- **A** 常量内存占用。
- **B** 无损压缩。
- **C** 更快的 sha256 计算。
- **D** 亚线性查找，能在文档仅差几个 token 时仍以高 Jaccard 相似度标记近似重复。

<details>
<summary>查看答案与解析</summary>

**答案**　D

MinHash 加 LSH 能捕捉到精确哈希去重漏掉的释义和模板变体。

</details>

## 3. 为什么 checkpoint 是在字节追加之前写入，而不是之后？

- **A** 这样比较方便。
- **B** 这样节省磁盘空间。
- **C** 这样更快。
- **D** 如果进程在写入字节和更新 checkpoint 之间挂掉，下次恢复时会读到一个落后于实际字节的 checkpoint，导致静默重复追加、损坏文件。

<details>
<summary>查看答案与解析</summary>

**答案**　D

先写 checkpoint 符合 write-ahead log 模式：崩溃后已验证偏移量要么等于要么落后于文件实际长度，绝不会超前。

</details>

## 4. Manifest 的 sha256 锁文件起什么作用？

- **A** 加快读取速度。
- **B** 下游阶段在 manifest 内容与锁定哈希不匹配时拒绝启动，封堵攻击者篡改单个文件的静默攻击面。
- **C** 作为 manifest 的备份。
- **D** 记录日期。

<details>
<summary>查看答案与解析</summary>

**答案**　B

锁定 manifest 哈希使代码和数据之间的关联成为内容寻址的契约。

</details>

## 5. 为什么去重放在 tokenization 上游而不是下游？

- **A** Tokenizer 需要先有词表。
- **B** Tokenization 开销很大；对同一篇文档跑两遍只会让成本翻倍，对 loss 曲线没有收益，所以先去重严格更省。
- **C** Tokenizer 不能读 JSONL。
- **D** Tokenizer 会拒绝重复。

<details>
<summary>查看答案与解析</summary>

**答案**　B

去重是流水线第一步，每去掉一篇重复文档就给 tokenizer 省下一次处理。

</details>

## 6. 对被去掉的重复文档做 tombstone 标记，比直接静默删除多保留了什么？

- **A** Manifest sha256 的稳定性。
- **B** 磁盘空间。
- **C** 压缩比。
- **D** 重复文档与它碰撞的 keeper 之间的关联，以及一条在未来调整阈值时仍可追溯的审计记录。

<details>
<summary>查看答案与解析</summary>

**答案**　D

Tombstone 让未来的处理可以回溯去重阈值；直接删除则丢失了证据。

</details>


[返回本课](docs/zh.md)
