# 顶点项目 07 —— 端到端微调流水线（数据到 SFT 到 DPO 到服务） · 自测

每题先选答案，再展开解析。

## 1. 在数据准备阶段，污染检查（contamination check）防范的是什么？

- **A** MMLU-Pro、MT-Bench-v2 等公开基准的测试集泄漏进训练数据
- **B** 跨 llama.cpp 构建的 GGUF 版本偏差
- **C** 训练与部署之间的 GPU 驱动不匹配
- **D** SFT 与 DPO 阶段之间的 tokenizer 漂移

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 2. 为什么流水线要先 SFT 再 DPO（或 GRPO），而不是仅用 DPO？

- **A** SFT 在带标注的补全上建立领域行为，而 DPO 或 GRPO 则依据偏好对或可验证奖励来对齐模型
- **B** DPO 无法在量化权重上运行
- **C** Axolotl 没有实现 DPO
- **D** DPO 需要一个单独的基础模型架构

<details>
<summary>查看答案与解析</summary>

**答案**　A



</details>

## 3. EAGLE-3 为 vLLM 服务阶段贡献了什么？

- **A** 一个用于工具调用的 OPA 策略
- **B** 提前预测 N 个 token 的 draft head；目标模型一次性验证，带来 2-3 倍吞吐
- **C** 一个自动的数据去重步骤
- **D** 一个新的 prompt 缓存层

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 4. 哪个指标报告推测解码的 draft 与目标模型的对齐程度？

- **A** PSI
- **B** 接受率（acceptance rate）
- **C** 覆盖率增量（coverage delta）
- **D** 困惑度

<details>
<summary>查看答案与解析</summary>

**答案**　B



</details>

## 5. 为了部署灵活性，流水线交付哪三种量化格式？

- **A** FP32、FP16、BF16
- **B** 三种运行时上仅 INT8
- **C** ONNX、CoreML、TFLite
- **D** GPTQ-INT4-Marlin、AWQ-INT4 和 GGUF-Q4_K_M

<details>
<summary>查看答案与解析</summary>

**答案**　D



</details>

## 6. 本毕业项目中的 2026 年模型卡遵循哪个框架约定？

- **A** Datasheets for Datasets
- **B** 仅 HuggingFace 的 YAML 前置元数据
- **C** Model Openness Framework（MOF）2026 模板，涵盖数据、训练、评测、安全、许可证和可复现性
- **D** OpenAI 的模型卡格式

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>

## 7. 用哪个 HPA 指标对服务副本进行自动扩缩？

- **A** 网络出站字节数
- **B** GPU 温度
- **C** 队列等待时间（queue-wait time）
- **D** CPU 利用率

<details>
<summary>查看答案与解析</summary>

**答案**　C



</details>


[返回本课](docs/zh.md)
