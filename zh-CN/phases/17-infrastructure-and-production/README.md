# 阶段 17：基础设施与生产

> 把 AI 交付到真实世界。扩展、监控、优化。

## 在 GitHub 上开始本阶段

**前置要求：** 阶段 11“LLM 工程”与阶段 13“工具与协议”。

**第一课：** [托管式 LLM 平台](01-managed-llm-platforms/docs/zh.md)

从仓库根目录运行：

```bash
python3 phases/17-infrastructure-and-production/01-managed-llm-platforms/code/main.py
```

记录命令、退出码、成本与延迟对比、冗余提升，以及一份简短的决策记录，写明所选方案背后的工作负载假设。

**下一步：** 改变一个工作负载或 SLA 输入，说明新的选择，然后继续学习[推理平台经济学](02-inference-platform-economics/docs/zh.md)。

浏览[阶段 17 的完整课程列表](../../README.md#phase-17)或[跨阶段路线图](../../ROADMAP.md)。

## 本阶段中文课文

- [01 · 托管 LLM（大语言模型） 平台 —— Bedrock、Vertex AI、Azure OpenAI](01-managed-llm-platforms/docs/zh.md)
- [02 · 推理平台经济学 —— Fireworks、Together、Baseten、Modal、Replicate、Anyscale](02-inference-platform-economics/docs/zh.md)
- [03 · Kubernetes 上的 GPU（图形处理器） 自动扩缩 —— Karpenter、KAI Scheduler、Gang Scheduling](03-gpu-autoscaling-kubernetes/docs/zh.md)
- [04 · 推理服务引擎内部机制——PagedAttention、连续批处理与分块预填充](04-vllm-serving-internals/docs/zh.md)
- [05 · 生产环境中的 EAGLE-3 Speculative Decoding](05-eagle3-speculative-decoding/docs/zh.md)
- [06 · 前缀缓存推理服务——RadixAttention 与 KV 复用](06-sglang-radixattention/docs/zh.md)
- [07 · 硬件专用推理编译——Blackwell 上的 FP8 与 NVFP4](07-tensorrt-llm-blackwell/docs/zh.md)
- [08 · 推理指标 —— TTFT（首个词元延迟）、TPOT、ITL、Goodput、P99](08-inference-metrics-goodput/docs/zh.md)
- [09 · 生产量化 —— AWQ、GPTQ、GGUF K-quant、FP8、MXFP4/NVFP4](09-production-quantization/docs/zh.md)
- [10 · Serverless LLM（大语言模型） 的冷启动缓解](10-cold-start-mitigation/docs/zh.md)
- [11 · 多区域 LLM（大语言模型） 服务与 KV Cache（键值缓存） 局部性](11-multi-region-kv-locality/docs/zh.md)
- [12 · 边缘推理 —— Apple Neural Engine、Qualcomm Hexagon、WebGPU/WebLLM、Jetson](12-edge-inference/docs/zh.md)
- [13 · LLM（大语言模型） 可观测性栈选型](13-llm-observability/docs/zh.md)
- [14 · Prompt（提示词） 缓存与语义缓存经济学](14-prompt-semantic-caching/docs/zh.md)
- [15 · Batch API（应用程序编程接口） —— 5 折成为行业标准](15-batch-apis/docs/zh.md)
- [16 · 模型路由作为降本原语](16-model-routing/docs/zh.md)
- [17 · 分离式 Prefill/Decode —— NVIDIA Dynamo 与 llm-d](17-disaggregated-prefill-decode/docs/zh.md)
- [18 · 生产级推理服务栈——KV 卸载与缓存感知路由](18-vllm-production-stack-lmcache/docs/zh.md)
- [19 · AI 网关 —— LiteLLM、Portkey、Kong AI Gateway、Bifrost](19-ai-gateways/docs/zh.md)
- [20 · LLM（大语言模型） 的影子流量、Canary 上线与渐进式部署](20-shadow-canary-progressive/docs/zh.md)
- [21 · A/B 测试 LLM（大语言模型） 特性 —— GrowthBook、Statsig 与"凭感觉"问题](21-ab-testing-llm-features/docs/zh.md)
- [22 · 压测 LLM（大语言模型） API（应用程序编程接口） —— 为什么 k6 和 Locust 会骗你](22-load-testing-llm-apis/docs/zh.md)
- [23 · 面向 AI 的 SRE —— 多 agent（智能体） 事件响应、Runbook、预测性检测](23-sre-for-ai/docs/zh.md)
- [24 · LLM（大语言模型） 生产环境的混沌工程](24-chaos-engineering-llm/docs/zh.md)
- [25 · 安全 —— 密钥、API（应用程序编程接口） Key 轮换、审计日志、Guardrails](25-security-secrets-audit/docs/zh.md)
- [26 · 合规 —— SOC 2、HIPAA、GDPR、PCI-DSS、EU AI Act、ISO 42001](26-compliance-frameworks/docs/zh.md)
- [27 · LLM（大语言模型） 的 FinOps —— 单位经济学与多租户归因](27-finops-llms/docs/zh.md)
- [28 · 自托管推理服务选型——让引擎匹配硬件与规模](28-self-hosted-serving-selection/docs/zh.md)
- [29 · 模型演示接口 —— 从函数到可分享应用](29-model-demo-interfaces/docs/zh.md)
