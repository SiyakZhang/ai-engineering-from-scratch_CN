# 分片 Checkpoint 与原子化恢复 · 自测

每题先选答案，再展开解析。

## 1. 为什么「先汇集再写出」在大规模下是错误的 checkpoint 模式？

- **A** 它看起来丑
- **B** 它占用太多 CPU
- **C** 所有状态都过 rank 0；写带宽是最慢的那条单链路、而非聚合带宽，所以 TB 级的写入要花几个小时
- **D** 它需要特殊硬件

<details>
<summary>查看答案与解析</summary>

**答案**　C

分片写入随集群规模扩展：64 个 rank 并行写，完成时间是单 rank 写汇集状态的 1/64。

</details>

## 2. 清单（manifest）记录了哪些 shard 文件本身记不下的信息？

- **A** 主机名
- **B** 随机数
- **C** world_size、schema 版本、每个 shard 的 sha256，以及 shard 归属；给加载器一份契约，让它在触碰状态前先校验
- **D** 文件系统名

<details>
<summary>查看答案与解析</summary>

**答案**　C

没有清单，加载器只能猜哪个 shard 属于哪个 rank，并盲信文件数量是对的。

</details>

## 3. 为什么要写到 <name>.tmp 再 rename，而不是直接写？

- **A** 更快
- **B** torch 要求如此
- **C** 同一文件系统内的 POSIX rename 是原子的：写到一半崩溃也不会动到前一个文件。直接写可能留下写了一半的 checkpoint，毒害下一次恢复
- **D** 省内存

<details>
<summary>查看答案与解析</summary>

**答案**　C

没有原子写，一次写了一半的保存加上一份指向它的更新清单，会在下次加载时损坏状态。

</details>

## 4. 每个 shard 的 sha256 防的是什么？

- **A** 网络攻击
- **B** 性能变慢
- **C** 内存泄漏
- **D** 写了一部分或被损坏的写入；加载时校验哈希能在截断的 shard 触碰模型状态之前抓住它

<details>
<summary>查看答案与解析</summary>

**答案**　D

没有 sha256 校验，一个被截断的 shard 会悄悄加载并损坏 optimizer，之后以 NaN loss 的形式暴露出来。

</details>

## 5. 为什么加载路径要对 world_size 不匹配大声报错？

- **A** 在 8 个 rank 上恢复 4-rank 的 shard 布局会悄悄错配 shard；大声拒绝逼操作者改用跨 world size 的再平衡路径
- **B** 纯装饰
- **C** 硬件需要
- **D** 更好写代码

<details>
<summary>查看答案与解析</summary>

**答案**　A

跨 world size 的再平衡是一个独立操作；悄悄拼接尺寸不对的 shard 会损坏状态。

</details>

## 6. 为什么生产环境要轮转 checkpoint（只保留最近 K 个）？

- **A** 其实并不需要
- **B** 美观
- **C** 压缩
- **D** 不轮转的话磁盘会在运行中途写满、下一个 checkpoint 就失败；轮转在写新的之前删掉最旧的，把磁盘占用约束住

<details>
<summary>查看答案与解析</summary>

**答案**　D

真实运行通常保留 3-5 个近期 checkpoint；每次新保存前丢掉最旧的，磁盘预算就固定了。

</details>


[返回本课](docs/zh.md)
