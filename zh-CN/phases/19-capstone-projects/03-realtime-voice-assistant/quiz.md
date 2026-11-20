# 顶点项目 03 —— 实时语音助手（ASR 到 LLM 到 TTS） · 自测

每题先选答案，再展开解析。

## 1. 为什么语音 agent 不能靠串接三个阻塞式 REST 调用来构建？

- **A** 要把端到端延迟压到 800ms 以下，需要在每个阶段都做流水线式流式处理
- **B** JSON 序列化对音频数据来说太慢
- **C** REST 与 WebRTC 不兼容
- **D** REST 端点有 30 秒的硬性超时

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 2. 在 VAD 之外，轮次检测器（turn-detector）的作用是什么？

- **A** 在多方通话中检测是哪位说话人在讲话
- **B** 为 agent 训练一个自定义声音克隆
- **C** 读取部分转写，并判断用户是否真的说完了这句话
- **D** 把背景音乐混入输出流

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 3. 当用户在 agent 回应到一半时开始说话，要让插话（barge-in）体验恰当，必须发生什么？

- **A** 流水线缓冲用户音频，直到 TTS 完成
- **B** agent 提高 TTS 音量以维护优先权
- **C** TTS 先把当前句子说完再让出
- **D** 立即取消 TTS，丢弃剩余的 LLM 输出，并让 ASR 重新就绪

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 4. 为什么在工具耗时超过约 300ms 时要发出一句简短的填充语，比如「稍等，我查一下」？

- **A** 它重置 WebRTC 抖动缓冲区
- **B** 它触发一个回退 ASR 模型
- **C** 它避免了沉默，使对话不会在旁路工具运行时停滞
- **D** 它改善下一句话的 WER

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 5. 第一段音频块必须在第一个 LLM token 之后大约多久内离开服务器？

- **A** 20ms
- **B** 2 秒
- **C** 800ms
- **D** 200ms

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 6. 哪个指标直接衡量不恰当的插话或过于急切的轮次关闭？

- **A** WER
- **B** 误切断率（false-cutoff rate）
- **C** 接受率
- **D** MOS

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 7. 在 3% 丢包率下，流水线依赖哪两种自适应行为？

- **A** 切换到更大的 LLM 并禁用 TTS
- **B** 保留部分转写并提高 VAD 的语音门限阈值
- **C** 重启 LiveKit 房间
- **D** 回退到 PSTN 音频编解码器

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>


[返回本课](docs/zh.md)
