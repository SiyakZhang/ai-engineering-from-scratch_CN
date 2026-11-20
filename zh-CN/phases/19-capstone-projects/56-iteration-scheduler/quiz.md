# 迭代调度器 · 自测

每题先选答案，再展开解析。

## 1. 为什么调度器用 UCB 评分而不是总选当前最优的分支？

- **A** 因为不用 UCB 就无法排序队列
- **B** 因为贪心选择永远不会探索；UCB 平衡了利用与探索
- **C** 因为 asyncio 要求 UCB
- **D** 因为 UCB 计算更快

<details>
<summary>查看答案与解析</summary>

**答案**　B

贪心会锁死在第一个领先者上。均匀分配永远不利用。UCB 选择领先者的同时，通过 sqrt(ln N / n) 项为探索不足的分支保留容量。

</details>

## 2. 在 UCB1 下，一个已完成零次运行的分支得到什么分数？

- **A** 零
- **B** 所有其他分支的平均奖励
- **C** 探索常数 c
- **D** 正无穷，保证未尝试的分支总是优先被选中

<details>
<summary>查看答案与解析</summary>

**答案**　D

课程中 runs=0 时分配 +inf。这保证每个分支至少被尝试一次，之后才会有分支被重新选择。

</details>

## 3. 调度器如何让多个槽位同时保持忙碌？

- **A** 用 asyncio.create_task 为每个已分发的假设创建任务，并在 in-flight 集合上 await FIRST_COMPLETED
- **B** 在事件循环上 sleep 阻塞
- **C** 在线程池中运行 runner
- **D** 使用 multiprocessing

<details>
<summary>查看答案与解析</summary>

**答案**　A

每个分发的假设变成一个 task。主循环等待 FIRST_COMPLETED，完成的槽位立即释放，另一个假设随即被分发。

</details>

## 4. 调度器在什么时候为一个分支发出 paper.trigger？

- **A** 仅在运行结束时
- **B** 每当该分支有结果返回时
- **C** 在该分支首次均值达到或超过论文阈值时触发，且每个分支只触发一次
- **D** 当触及剪枝下限时

<details>
<summary>查看答案与解析</summary>

**答案**　C

trigger 在分支均值首次跨过阈值时触发，每个分支只触发一次。BranchStats 上的 paper_triggered 标志防止重复。

</details>

## 5. 当一个分支的均值在达到最低运行次数后仍低于剪枝下限，会怎样？

- **A** 调度器抛出异常
- **B** 没什么；UCB 最终会选其他分支
- **C** 该分支被标记为已剪枝，该分支上剩余的假设从队列中移除
- **D** 奖励下限自动降低

<details>
<summary>查看答案与解析</summary>

**答案**　C

剪枝把分支从未来的调度中移除。剪枝与选择器分离：UCB 排序，剪枝淘汰。

</details>

## 6. 调度器以哪两项预算作为硬性限制？

- **A** 内存和 CPU
- **B** 槽位数和队列深度
- **C** 论文触发次数和剪枝次数
- **D** max_experiments（总运行次数）和 max_seconds（挂钟时间）

<details>
<summary>查看答案与解析</summary>

**答案**　D

两者都会作为停止原因被触发。max_experiments 限制总工作量，max_seconds 限制墙上时间。trace 记录了是哪个限制终止了运行。

</details>


[返回本课](docs/zh.md)
