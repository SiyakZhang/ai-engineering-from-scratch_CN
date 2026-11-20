# 带 Schema 校验的 Tool Registry · 自测

每题先选答案，再展开解析。

## 1. 为什么要把工具的 schema 和 handler 分开注册？

- **A** 因为 schema 必须写在 YAML 里
- **B** 因为 schema 必须经过编译
- **C** 这样 validator 可以保持为纯数据操作，handler 则保持为不透明代码
- **D** 因为 handler 不能返回 JSON

<details>
<summary>查看答案与解析</summary>

**答案**　C

把 schema 保持为数据、handler 保持为代码，validator 就能作为一个纯函数在 schema 树上递归执行。

</details>

## 2. 本课实现的子集故意不包含哪些关键字？

- **A** type、properties、required
- **B** items、enum
- **C** oneOf、anyOf、$ref、allOf
- **D** minLength、maxLength、pattern

<details>
<summary>查看答案与解析</summary>

**答案**　C

被省略的关键字会引入循环和引用解析。我们保持子集为线性的，这样 validator 只需一次递归遍历就能完成。

</details>

## 3. 为什么 register() 默认拒绝重复注册？

- **A** 因为 schema 不能被重新校验
- **B** 因为 handler 不能被替换
- **C** 因为注册中心每个名称只能存一条记录
- **D** 静默覆写是生产环境工具目录漂移的根源

<details>
<summary>查看答案与解析</summary>

**答案**　D

强制使用 override=True 能暴露出代码中两个不同模块试图拥有同一个工具名的情况。

</details>

## 4. 当 schema 指定 type 为 integer 但收到值 True 时，validator 会怎么做？

- **A** 返回类型错误，因为在这个 validator 中 bool 不是 integer
- **B** 当作 1 处理并通过
- **C** 静默强制转换为 integer
- **D** 抛出未处理异常

<details>
<summary>查看答案与解析</summary>

**答案**　A

Python 的 bool 是 int 的子类，但 validator 在 integer 检查中过滤掉了 bool。JSON 中的布尔值和整数是两种不同类型。

</details>

## 5. 输入对象是 {'user': {'email': 0}}，schema 要求 user.email 为 string 类型，此时错误路径是什么？

- **A** /user
- **B** /
- **C** user.email
- **D** /user/email

<details>
<summary>查看答案与解析</summary>

**答案**　D

JSON Pointer 把经过 user 再到 email 的下钻路径编码为 /user/email。

</details>

## 6. 为什么注册中心不是安全边界？

- **A** 因为注册中心在进程内运行
- **B** 因为 handler 是异步的
- **C** 因为即使校验通过，handler 仍然可能行为不当
- **D** 因为 schema 是 JSON 格式的

<details>
<summary>查看答案与解析</summary>

**答案**　C

注册中心只检查形状。行为、超时和隔离是 dispatcher 和沙箱的职责。

</details>


[返回本课](docs/zh.md)
