# 来源

> 本手册按权威性排列来源，本页列出各节引用的全部外部来源及使用位置。

等级与[本手册如何编写](r-7-how-this-manual-was-made.md)一致。两个来源冲突时，以较高者为准，并在该节说明。各节使用的 SGLang 源码文件记录在手册源文件中，由审计检查，此处不重复列出。以下页面均于 2026-10-16 阅读。研究更新中新增的论文和报告阅读于 2026-10-22。

<a id="s-ref-sources-the-ranked-sources"></a>

## 来源等级

| 等级 | 来源 | 手册采用的内容 | 来源键 |
|---|---|---|---|
| 1 | 标签对应的 SGLang 源码，`baa9befa` | 全部默认值和机制 | 手册源文件中各节的源码文件列表 |
| 2 | [Mac](../../../../manuals/sglang-101/capture/out) 与 [GPU](../../../../manuals/sglang-101/capture/gpu) 的捕获运行 | 全部 listing 及标为实测的数字 | 捕获文件名 |
| 3 | SGLang issue 与 PR | 事故和各功能设计历史 | `issue` 及编号 |
| 4 | 论文 | RadixAttention 原始设计及 SGLang 实现的方法 | `paper` 及标题 |
| 5 | 标签对应的 SGLang 文档 | 与代码核对后的文档行为 | `docs` 及标题 |
| 6 | 独立实践报告 | 本手册无法运行的 GPU 和规模 | `field`、作者及月份 |
| 7 | SGLang 团队和供应方报告 | 主张，始终注明来自作者 | `team` 或供应方及月份 |

<a id="s-ref-sources-rank-1-and-rank-2-the-code-and-the-captures"></a>

## 第 1、2 级：代码与捕获记录

| 来源 | 使用位置 |
|---|---|
| SGLang 0.5.22，标签 `v0.5.22`，提交 `baa9befa381511cd4d56f83980951e5a45fffc6d`，[github.com/sgl-project/sglang](https://github.com/sgl-project/sglang) | 全部章节 |
| Miles 0.1.2，标签 `v0.1.2`，提交 `a22fd824`，[github.com/radixark/miles](https://github.com/radixark/miles) | [7.2](7-2-sglang-as-an-rl-rollout-engine.md) |
| 捕获工具及其 [Mac 运行](../../../../manuals/sglang-101/capture/out)，录制于 2026-10-16 | 含 listing 的各节 |
| GPU 工具及其[运行记录](../../../../manuals/sglang-101/capture/gpu)，2026-10-16 至 2026-10-21 在 NVIDIA L4 节点和 DGX Spark（GB10）上录制 | 含 GPU 实测的各节 |
| Miles 镜像 `radixark/miles:latest`，Miles 提交 `08752a12`，包含 SGLang 0.5.22.dev46+g7b6993a | [7.2](7-2-sglang-as-an-rl-rollout-engine.md) |

<a id="s-ref-sources-rank-3-pull-requests"></a>

## 第 3 级：PR

issue 见[事故索引](r-3-incident-index.md)。以下 PR 解释设计变更。

| PR | 修改内容 | 使用位置 |
|---|---|---|
| [#9241](https://github.com/sgl-project/sglang/pull/9241) | 预热后冻结垃圾回收器 | [1.2](1-2-check-that-the-server-is-healthy.md) |
| [#11210](https://github.com/sgl-project/sglang/pull/11210) | 同一线程中用两条 CUDA stream 实现重叠 | [2.4](2-4-the-overlap-scheduler.md) |
| [#14312](https://github.com/sgl-project/sglang/pull/14312) | 将 `sgl-router` 重命名为 `sgl-model-gateway` | [6.4](6-4-sgl-model-gateway.md) |
| [#23906](https://github.com/sgl-project/sglang/pull/23906) | 将 prefill graph 字段移到按阶段配置中 | [4.1](4-1-forwardmode-and-cuda-graphs.md) |
| [#29458](https://github.com/sgl-project/sglang/pull/29458) | CUDA 上可断开的 prefill graphs | [4.1](4-1-forwardmode-and-cuda-graphs.md) |
| [#32114](https://github.com/sgl-project/sglang/pull/32114) | 删除 Cutlass MLA、Dual Chunk FlashAttention 和普通 GPTQ CUDA 内核 | [4.2](4-2-attention-backend.md)、[4.3](4-3-quantization.md) |
| [#37898](https://github.com/sgl-project/sglang/pull/37898) | 将 20 至 35 GB GPU 的 decode graph 上限从 24 提高到 48 | [4.1](4-1-forwardmode-and-cuda-graphs.md) |
| [#35455](https://github.com/sgl-project/sglang/pull/35455) | 加载 compressed-tensors checkpoint 的 KV scales，2026-08-20 合并 | [4.3](4-3-quantization.md) |
| [#40795](https://github.com/sgl-project/sglang/pull/40795) | 删除旧基准别名 | [5.1](5-1-sglang-benchmark-serving.md) |
| [#41818](https://github.com/sgl-project/sglang/pull/41818) | 增加 `--attn-dp-size`，让 `--dp-size` 只保留一种含义 | [6.1](6-1-tp-size-dp-size-and-attn-dp-size.md) |
| [#42285](https://github.com/sgl-project/sglang/pull/42285)、[#42286](https://github.com/sgl-project/sglang/pull/42286)、[#42287](https://github.com/sgl-project/sglang/pull/42287) | 移除 prefill graphs 的 torch.compile 路径 | [4.1](4-1-forwardmode-and-cuda-graphs.md) |

<a id="s-ref-sources-rank-4-papers"></a>

## 第 4 级：论文

| 论文 | 使用位置 |
|---|---|
| Zheng 等，SGLang：高效执行结构化语言模型程序（SGLang: Efficient Execution of Structured Language Model Programs），[arXiv 2312.07104](https://arxiv.org/abs/2312.07104) | [2.2](2-2-the-scheduler-loop-and-schedule-policy.md)、[3.1](3-1-kv-bytes-per-token-and-the-kv-pool.md)、[3.3](3-3-radixcache.md)、[4.5](4-5-structured-outputs-with-xgrammar.md) |
| 代码中引用的尾延迟优化 LRU 策略，[arXiv 2510.15152](https://arxiv.org/abs/2510.15152) | [3.5](3-5-eviction-policies-and-hicache.md) |
| Lee 等，从 token 到层：用分层 prefill 重新定义 MoE 服务的无停顿调度（From Tokens to Layers: Redefining Stall-Free Scheduling for MoE Serving with Layered Prefill），[arXiv 2510.08055](https://arxiv.org/abs/2510.08055) | [2.2](2-2-the-scheduler-loop-and-schedule-policy.md) |
| Liu、Yu 和 Yang，当复杂驱逐失效：重新思考 LLM 前缀复用的缓存替换（When Fancy Eviction Fails: Rethinking Cache Replacement For LLM Prefix Reuse），[arXiv 2609.28870](https://arxiv.org/abs/2609.28870) | [3.5](3-5-eviction-policies-and-hicache.md) |
| Abramovich 等，SPEED-Bench：统一且多样的推测解码基准（SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding），[arXiv 2604.09557](https://arxiv.org/abs/2604.09557) | [4.4](4-4-speculative-decoding.md)、[6.2](6-2-moe-serving-deepep-and-eplb.md) |
| Kumar、Sanghavi 和 Das，测试时推测（Test-Time Speculation），[arXiv 2605.09329](https://arxiv.org/abs/2605.09329) | [4.4](4-4-speculative-decoding.md) |
| Agrawal 等，论 LLM 推理服务系统的性能评估（On Evaluating Performance of LLM Inference Serving Systems），[arXiv 2507.09019](https://arxiv.org/abs/2507.09019) | [4.4](4-4-speculative-decoding.md) |
| Zhao 等，CoRun：通过填充简单高效地实现确定性 LLM 推理（CoRun: Padding is Simple and Efficient for Deterministic LLM Inference），[arXiv 2608.14376](https://arxiv.org/abs/2608.14376) | [4.6](4-6-deterministic-inference-and-logprobs.md) |
| Qin 等，Vosti：指定、实现和验证确定性 LLM 推理（Vosti: Specifying, Implementing, and Verifying Deterministic LLM Inference），[arXiv 2609.38981](https://arxiv.org/abs/2609.38981) | [4.6](4-6-deterministic-inference-and-logprobs.md) |
| Patodiya，同一请求，不同回答：量化放大 LLM 服务中缓存引起的分歧（Same Request, Different Answer: Quantization Amplifies Cache-Induced Divergence in LLM Serving），[arXiv 2609.04748](https://arxiv.org/abs/2609.04748) | [4.6](4-6-deterministic-inference-and-logprobs.md) |
| Chandrasekar 和 Kramberger，识别并缓解生产 LLM 推理基准中的系统性测量偏差（Identifying and Mitigating Systemic Measurement Bias in Production LLM Inference Benchmarks），[arXiv 2605.24217](https://arxiv.org/abs/2605.24217) | [5.1](5-1-sglang-benchmark-serving.md) |
| Li 等，重新审视分离式大语言模型服务的性能和能耗影响（Revisiting Disaggregated Large Language Model Serving for Performance and Energy Implications），[arXiv 2601.08833](https://arxiv.org/abs/2601.08833) | [6.3](6-3-prefill-decode-disaggregation.md) |

<a id="s-ref-sources-rank-5-sglang-documentation-at-the-tag"></a>

## 第 5 级：固定标签的 SGLang 文档

| 页面 | 使用位置 |
|---|---|
| `docs/docs/hardware-platforms/apple_metal.mdx` | 前言、[2.1](2-1-sglang-serve-and-the-three-processes.md)、[2.4](2-4-the-overlap-scheduler.md) |
| `docs/docs/advanced_features/hyperparameter_tuning.mdx` | [2.3](2-3-admission-and-retraction.md) |
| `docs/docs/advanced_features/hicache_design.mdx` 和 `radix_eviction_policy.mdx` | [3.5](3-5-eviction-policies-and-hicache.md) |
| `docs/docs/advanced_features/attention_backend.mdx` | [4.2](4-2-attention-backend.md) |
| `docs/docs/advanced_features/quantization.mdx` | [4.3](4-3-quantization.md) |
| `docs/docs/advanced_features/speculative_decoding.mdx` | [4.4](4-4-speculative-decoding.md) |
| `docs/docs/advanced_features/expert_parallelism.mdx` | [6.2](6-2-moe-serving-deepep-and-eplb.md) |
| `docs/docs/advanced_features/pd_disaggregation.mdx` | [6.3](6-3-prefill-decode-disaggregation.md) |
| `docs/docs/get-started/install.mdx` | [7.1](7-1-operating-sglang.md) |
| `docs/docs/advanced_features/sglang_for_rl.mdx` | [7.2](7-2-sglang-as-an-rl-rollout-engine.md) |

<a id="s-ref-sources-rank-6-independent-field-reports"></a>

## 第 6 级：独立实践报告

| 作者 | 报告 | 月份 | 使用位置 |
|---|---|---|---|
| AIMultiple | [推理引擎基准](https://aimultiple.com/inference-engines) | 2026-01，答复于 2026-10 | [1.3](1-3-what-the-server-does-with-your-request.md)、[5.3](5-3-reading-other-peoples-benchmarks.md) |
| Alibaba Cloud、RBG 与 Mooncake 团队 | [用 SGLang、RBG 和 Mooncake 构建生产推理平台](https://www.alibabacloud.com/blog/building-a-production-grade-cloud-native-large-model-inference-platform-with-sglang-rbg-%2B-mooncake_602933) | 2026-03 | [3.5](3-5-eviction-policies-and-hicache.md) |
| Ant Group | [LMSYS 博客：用 SGLang 在 H20 上运行 DeepSeek-R1](https://www.lmsys.org/blog/2025-09-26-sglang-ant-group/) | 2025-09 | [4.4](4-4-speculative-decoding.md)、[6.1](6-1-tp-size-dp-size-and-attn-dp-size.md)、[6.2](6-2-moe-serving-deepep-and-eplb.md)、[7.1](7-1-operating-sglang.md) |
| NVIDIA 开发者论坛的 basbunarhasan | [DGX Spark 上使用 NVFP4 与 DSpark 的 SGLang](https://forums.developer.nvidia.com/t/qwen3-8-27b-at-34-38-tok-s-on-dgx-spark-open-source-one-command-setup-sglang-nvfp4-dspark/380257) | 2026-08 | [3.2](3-2-mem-fraction-static-and-startup-sizing.md) |
| CERIT-SC | [在 CERIT-SC 运行 LLM](https://blog.cerit.io/blog/run-llm2/)和[后续文章](https://blog-dev.cerit.io/blog/llm3/) | 2025-10、2026-04 | [7.1](7-1-operating-sglang.md) |
| Cloudflare | [更小、更快、更安全的模型](https://blog.cloudflare.com/smaller-faster-safer-models/) | 2026-08 | [3.1](3-1-kv-bytes-per-token-and-the-kv-pool.md)、[4.3](4-3-quantization.md) |
| Crusoe | [AMD MI355X 上的 MLPerf Inference v6.1 结果](https://www.crusoe.ai/resources/blog/serving-5-75-million-tokens-per-second-crusoes-mlperf-inference-v6-1-results-on-amd-mi355x) | 2026-09 | [5.3](5-3-reading-other-peoples-benchmarks.md)、[6.2](6-2-moe-serving-deepep-and-eplb.md) |
| David Noel Ng | [GH200 基准，第 4 部分](https://dnhkng.github.io/posts/gh200-benchmarking-part-4-dsv4-released/) | 2026-08 | [4.4](4-4-speculative-decoding.md) |
| DeepInfra | [vLLM 与 SGLang 比较](https://deepinfra.com/blog/vllm-vs-sglang) | 2026-08 | [5.3](5-3-reading-other-peoples-benchmarks.md) |
| Doubleword | [快速启动 SGLang](https://fergusfinn.com/blog/fast-sglang-starts/) | 2026-04 | [7.1](7-1-operating-sglang.md) |
| dstack | [Prefill-decode 比例基准](https://dstack.ai/blog/benchmarking-pd-ratios/) | 2025-09 | [6.3](6-3-prefill-decode-disaggregation.md) |
| Hazy Research | [张量并行 Llama megakernel](https://hazyresearch.stanford.edu/blog/2025-09-28-tp-llama-main) | 2025-09 | [4.1](4-1-forwardmode-and-cuda-graphs.md) |
| SemiAnalysis 的 InferenceX | [MI355X 上的 GLM-5 FP8](https://inferencex.semianalysis.com/blog/mi355x-glm5-fp8-sglang-40-cheaper-than-b200)、[26 天内在 MI355X 上部署 DeepSeek-V4-Pro](https://inferencex.semianalysis.com/blog/mi355x-deepseek-v4-pro-sglang-110x-in-26-days)，以及 [B200 上的 GLM-5 NVFP4](https://inferencex.semianalysis.com/blog/b200-glm5-nvfp4-vs-h200-fp8-3-6x-perf-per-dollar) | 2026-05 | [4.1](4-1-forwardmode-and-cuda-graphs.md)、[5.3](5-3-reading-other-peoples-benchmarks.md) |
| Jarvislabs | [H100 上的 SGLang 与 vLLM 比较](https://jarvislabs.ai/blog/vllm-sglang-trtllm-comparison) | 2026-05 | [4.1](4-1-forwardmode-and-cuda-graphs.md)、[5.3](5-3-reading-other-peoples-benchmarks.md) |
| Jarvislabs | [托管端点](https://jarvislabs.ai/blog/managed-endpoints) | 2026-08 | [3.4](3-4-prefix-friendly-prompts.md)、[6.4](6-4-sgl-model-gateway.md) |
| joshua8.ai | [LLM 推理基准](https://joshua8.ai/llm-inference-benchmark/) | 2026-01 | [4.1](4-1-forwardmode-and-cuda-graphs.md)、[4.3](4-3-quantization.md)、[5.3](5-3-reading-other-peoples-benchmarks.md) |
| LinkedIn Engineering | [在 LinkedIn 用 SGLang 扩展基于 LLM 的排序系统](https://www.linkedin.com/blog/engineering/ai/scaling-llm-based-ranking-systems-with-sglang-at-linkedin) | 2026-02 | [1.2](1-2-check-that-the-server-is-healthy.md)、[2.1](2-1-sglang-serve-and-the-three-processes.md)、[7.1](7-1-operating-sglang.md) |
| Luca Lowndes | [SGLang 优化](https://luca.lowndes.net/blog/sglang-optimisations) | 2025-11 | [6.1](6-1-tp-size-dp-size-and-attn-dp-size.md) |
| Modal | [LLM 年鉴](https://modal.com/llm-almanac/summary) | 2025-06 | [5.3](5-3-reading-other-peoples-benchmarks.md) |
| Novita AI | [Hugging Face：SGLang 与 GLM MoE 模型](https://huggingface.co/blog/novita/sglang-glm4-moe) | 2026-01 | [6.3](6-3-prefill-decode-disaggregation.md) |
| Pivot News | [混合 Blackwell 基准摘要](https://pivotnews.ai/build/benchmarking-vllm-vs-sglang-vs-llama-cpp-on-a-mixed-blackwel) | 2026-05 | [4.3](4-3-quantization.md)、[5.3](5-3-reading-other-peoples-benchmarks.md) |
| RunPod | [何时应选择 SGLang 而非 vLLM](https://runpod.ghost.io/when-to-choose-sglang-over-vllm-multi-turn-conversations-and-kv-cache-reuse/) | 2025-06 | [3.3](3-3-radixcache.md)、[5.3](5-3-reading-other-peoples-benchmarks.md) |
| SemiAnalysis | [InferenceMAX](https://newsletter.semianalysis.com/p/inferencemax-open-source-inference) | 2025-10 | [5.3](5-3-reading-other-peoples-benchmarks.md) |
| Spheron | [vLLM、TensorRT-LLM 与 SGLang 比较](https://www.spheron.network/blog/vllm-vs-tensorrt-llm-vs-sglang-benchmarks/) | 2026 | [5.3](5-3-reading-other-peoples-benchmarks.md) |
| Steve Rawlinson | [双 H100 上的 vLLM 与 SGLang 比较](https://rawlinson.ca/articles/vllm-vs-sglang-performance-benchmark-h100) | 2025-12 | [3.2](3-2-mem-fraction-static-and-startup-sizing.md)、[5.3](5-3-reading-other-peoples-benchmarks.md) |
| Thinking Machines | [消除 LLM 推理中的非确定性](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/) | 2025-09 | [4.6](4-6-deterministic-inference-and-logprobs.md) |
| Varad More | [推理引擎基准系统](https://github.com/varad-more/inference-engine-benchmark-system) | 2026-04 | [3.3](3-3-radixcache.md)、[4.2](4-2-attention-backend.md)、[4.5](4-5-structured-outputs-with-xgrammar.md)、[5.3](5-3-reading-other-peoples-benchmarks.md) |
| vLLM 社区 | [讨论 #17221](https://github.com/vllm-project/vllm/discussions/17221) | 2025-04 | [5.3](5-3-reading-other-peoples-benchmarks.md) |

<a id="s-ref-sources-rank-7-sglang-team-and-vendor-reports"></a>

## 第 7 级：SGLang 团队与供应方报告

| 作者 | 报告 | 月份 | 使用位置 |
|---|---|---|---|
| vLLM 团队 | [vLLM 中 FP8 KV 缓存和注意力量化的现状](https://vllm.ai/blog/2026-04-22-fp8-kvcache) | 2026-04 | [4.3](4-3-quantization.md) |
| LMSYS | [SGLang 与 Llama 3](https://www.lmsys.org/blog/2024-07-25-sglang-llama3/) | 2024-07 | [5.3](5-3-reading-other-peoples-benchmarks.md) |
| LMSYS | [SGLang v0.4：零开销 batch 调度器](https://lmsys.org/blog/2024-12-04-sglang-v0-4/) | 2024-12 | [2.4](2-4-the-overlap-scheduler.md)、[6.1](6-1-tp-size-dp-size-and-attn-dp-size.md)、[6.4](6-4-sgl-model-gateway.md) |
| LMSYS | [96 张 H100 上使用 PD 分离与大规模 EP 的 DeepSeek](https://lmsys.org/blog/2025-05-05-large-scale-ep/) | 2025-05 | [6.2](6-2-moe-serving-deepep-and-eplb.md)、[6.3](6-3-prefill-decode-disaggregation.md) |
| LMSYS 博客上的 Mooncake 团队 | [采用大规模 EP 的 Kimi K2](https://www.lmsys.org/blog/2025-07-20-k2-large-scale-ep/) | 2025-07 | [6.3](6-3-prefill-decode-disaggregation.md) |
| LMSYS | [SGLang HiCache](https://lmsys.org/blog/2025-09-10-sglang-hicache/) | 2025-09 | [3.5](3-5-eviction-policies-and-hicache.md) |
| SGLang | [v0.5.21 发布说明](https://github.com/sgl-project/sglang/releases/tag/v0.5.21) | 2026-10 | [3.5](3-5-eviction-policies-and-hicache.md) |
| Google Cloud | [Vertex AI 上的 EAGLE-3](https://docs.cloud.google.com/gemini-enterprise-agent-platform/blog/posts/from-research-to-production-accelerate-oss-llm-with-eagle-3-on-vertex) | 2025-11 | [4.4](4-4-speculative-decoding.md) |
| Modal 与 Decagon | [Decagon 案例研究](https://frontend.modal.com/blog/decagon-case-study) | 2025-11 | [4.4](4-4-speculative-decoding.md) |
| LMSYS 与 RadixArk | [Miles](https://www.lmsys.org/blog/2025-11-19-miles/) | 2025-11 | [7.2](7-2-sglang-as-an-rl-rollout-engine.md) |
| RadixArk | [Miles v0.1](https://www.lmsys.org/blog/2026-08-18-miles-v0-1/) | 2026-08 | [7.2](7-2-sglang-as-an-rl-rollout-engine.md) |
| Miles 团队 | Miles v0.1.2 的 `docs/advanced/p2p-weight-transfer.md` | 2026-10 | [7.2](7-2-sglang-as-an-rl-rollout-engine.md) |

来源：front.md；sections/ 下所有文件的来源行和引用。

---

[返回中文手册目录](../../README.md) · [本节英文原文](../../../../manuals/sglang-101/sections/r-5-sources.md)
