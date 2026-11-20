# 语音 Agent：Pipecat 与 LiveKit · 自测

每题先选答案，再展开解析。

## 1. 一条 Pipecat 流水线使用哪两个流动方向？

- **A** 热和冷
- **B** 读和写
- **C** DOWNSTREAM（源到汇）和 UPSTREAM（反馈、取消、插话打断）
- **D** 入站和出站

<details>
<summary>查看答案与解析</summary>

**答案**　C

帧（frame）向下游从源流向汇，向上游用于控制和取消。

</details>

## 2. 经典的 Pipecat 语音流水线是什么？

- **A** 音频 -> JSON -> SQL -> 响应
- **B** LLM -> embed -> retrieve -> answer
- **C** VAD -> STT -> LLM -> TTS -> 传输
- **D** TTS -> STT -> LLM -> VAD

<details>
<summary>查看答案与解析</summary>

**答案**　C

VAD 检测语音活动，STT 转写，LLM 回复，TTS 朗读，传输层投递。

</details>

## 3. LiveKit Agents 提供哪两类语音 agent？

- **A** LocalAgent 和 CloudAgent
- **B** MultimodalAgent（直接音频）和 VoicePipelineAgent（STT/LLM/TTS 级联）
- **C** BatchAgent 和 StreamAgent
- **D** TextAgent 和 SpeechAgent

<details>
<summary>查看答案与解析</summary>

**答案**　B

MultimodalAgent 使用直接音频（Realtime 风格）；VoicePipelineAgent 使用 STT->LLM->TTS 以获得文本级控制。

</details>

## 4. 什么是插话打断（barge-in），它是如何处理的？

- **A** 提供商中断；换区域
- **B** 用户在 agent 说话时打断；UPSTREAM 取消帧在话语中途停止 TTS
- **C** 验证码失败；重试
- **D** LLM 成本飙升；减少 token

<details>
<summary>查看答案与解析</summary>

**答案**　B

插话打断是用户打断；UPSTREAM 取消是 Pipecat 干净处理它的方式。

</details>

## 5. 本课把多少的端到端延迟描述为高端水平？

- **A** 约 1500 毫秒
- **B** 约 5000 毫秒
- **C** 约 450-600 毫秒
- **D** 约 50 毫秒

<details>
<summary>查看答案与解析</summary>

**答案**　C

高端技术栈落在约 450-600 毫秒；800-1200 毫秒很常见；超过 1500 毫秒会感觉坏掉了。

</details>

## 6. 如果忽略 STT 置信度会出什么问题？

- **A** 低置信度的转写被当作圣经一样喂给 LLM，产生错误答案；应按置信度设门槛或请求确认
- **B** 通话变便宜
- **C** TTS 变快
- **D** 延迟改善

<details>
<summary>查看答案与解析</summary>

**答案**　A

把低置信度的 STT 当成真相，是语音 agent 的头号失败模式。

</details>

## 7. 为什么本课建议在上线前先把各组件延迟加起来？

- **A** 每个组件都增加 50-200 毫秒；总和决定了体验是否会感觉坏掉
- **B** 提供商按延迟计费
- **C** WebRTC 要求延迟
- **D** 它满足某项合规要求

<details>
<summary>查看答案与解析</summary>

**答案**　A

上线前把整条链（VAD + STT + LLM + TTS + 传输）加起来；目标很紧。

</details>


[返回本课](docs/zh.md)
