# 写给 AI 的复数 · 自测

每题先选答案，再展开解析。

## 1. 虚数单位 i 由什么定义？

- **A** i^2 = 1
- **B** i^2 = -1
- **C** i = sqrt(2)
- **D** i = -1

<details>
<summary>查看答案与解析</summary>

**答案**　B

虚数单位 i 由性质 i^2 = -1 定义。它把实数轴扩展为一个二维平面。在几何上，乘以 i 是一次 90 度旋转——两次相乘（i^2）就是 180 度旋转，即 -1。

</details>

## 2. 欧拉公式 e^(i*theta) 等于什么？

- **A** i^theta
- **B** cos(theta) + i*sin(theta)
- **C** sin(theta) + cos(theta)
- **D** theta + i

<details>
<summary>查看答案与解析</summary>

**答案**　B

欧拉公式表明 e^(i*theta) = cos(theta) + i*sin(theta)。这把复指数与三角函数联系起来，并表明当 theta 变化时 e^(i*theta) 描绘出单位圆。

</details>

## 3. (3 + 2i)(1 + 4i) 的结果是多少？

- **A** 5 + 14i
- **B** 4 + 6i
- **C** 3 + 8i
- **D** -5 + 14i

<details>
<summary>查看答案与解析</summary>

**答案**　D

使用 FOIL 展开：(3)(1) + (3)(4i) + (2i)(1) + (2i)(4i) = 3 + 12i + 2i + 8i^2 = 3 + 14i + 8(-1) = 3 + 14i - 8 = -5 + 14i。

</details>

## 4. 为什么 transformer 的旋转位置编码（RoPE）要使用复数？

- **A** 复数压缩位置编码以使用更少内存
- **B** RoPE 使用虚数来处理负位置
- **C** 将 query/key 向量乘以复数旋转，可以把相对位置编码为一个旋转角度
- **D** attention 的 softmax 函数要求使用复数

<details>
<summary>查看答案与解析</summary>

**答案**　C

RoPE 把 query 和 key 向量乘以复数旋转矩阵 e^(i*m*theta)，其中 m 是位置。两个 token 之间的相对位置变成了一个旋转角度，通过复数乘法，attention 自然地对相对位置（而非绝对位置）变得敏感。

</details>

## 5. N 次单位根是单位圆上 N 个等间距的点。它们的和是多少？

- **A** N
- **B** N/2
- **C** 1
- **D** 0

<details>
<summary>查看答案与解析</summary>

**答案**　D

N 个单位根是 e^(2*pi*i*k/N)，其中 k = 0, ..., N-1。它们对称地分布在单位圆周围，因此其向量和相互抵消为零。正是这种对称性使得 DFT 可逆。

</details>


[返回本课](docs/zh.md)
