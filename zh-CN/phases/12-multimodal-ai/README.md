# 阶段 12：多模态 AI

> 能看、能听、能读，并跨模态推理的模型。

## 在 GitHub 上开始本阶段

**前置要求：** 阶段 7 的 Transformer 与阶段 4 的计算机视觉。

**第一课：** [视觉 Transformer 的图像块 token](01-vision-transformer-patch-tokens/docs/zh.md)

从仓库根目录运行：

```bash
python3 phases/12-multimodal-ai/01-vision-transformer-patch-tokens/code/main.py
```

记录命令、退出码、图像块网格和序列长度、参数量，以及一句解释：为什么更高分辨率会产生更多视觉 token。

**下一步：** 改变图像或图像块尺寸之一，预测序列长度，然后继续学习[CLIP 与对比式预训练](02-clip-contrastive-pretraining/docs/zh.md)。

浏览[阶段 12 的完整课程列表](../../README.md#phase-12)或[跨阶段路线图](../../ROADMAP.md)。

## 本阶段中文课文

- [01 · Vision Transformer 与 patch-token 原语](01-vision-transformer-patch-tokens/docs/zh.md)
- [02 · CLIP 与对比式视觉-语言 pretraining（预训练）](02-clip-contrastive-pretraining/docs/zh.md)
- [03 · 从 CLIP 到 BLIP-2 —— Q-Former 作为模态桥](03-blip2-qformer-bridge/docs/zh.md)
- [04 · Flamingo 与用于少样本 VLM（视觉语言模型） 的门控 cross-attention（交叉注意力）](04-flamingo-gated-cross-attention/docs/zh.md)
- [05 · LLaVA 与视觉指令 fine-tuning（微调）](05-llava-visual-instruction-tuning/docs/zh.md)
- [06 · 任意分辨率视觉：Patch-n'-Pack 与 NaFlex](06-any-resolution-patch-n-pack/docs/zh.md)
- [07 · 开放权重 VLM（视觉语言模型） 配方：到底什么才重要](07-open-weight-vlm-recipes/docs/zh.md)
- [08 · LLaVA-OneVision：单图、多图、视频于一个模型](08-llava-onevision-single-multi-video/docs/zh.md)
- [09 · Qwen-VL 家族与动态 FPS 视频](09-qwen-vl-family-dynamic-fps/docs/zh.md)
- [10 · InternVL3：原生多模态 pretraining（预训练）](10-internvl3-native-multimodal/docs/zh.md)
- [11 · Chameleon 与早融合的纯 token（词元） 多模态模型](11-chameleon-early-fusion-tokens/docs/zh.md)
- [12 · Emu3：用下一 token（词元） 预测做图像和视频生成](12-emu3-next-token-for-generation/docs/zh.md)
- [13 · Transfusion：一个 transformer（基于注意力机制的神经网络架构） 里的自回归文本 + 扩散图像](13-transfusion-autoregressive-diffusion/docs/zh.md)
- [14 · Show-o 与离散扩散统一模型](14-show-o-discrete-diffusion-unified/docs/zh.md)
- [15 · Janus-Pro：用于统一多模态模型的解耦编码器](15-janus-pro-decoupled-encoders/docs/zh.md)
- [16 · MIO 与任意到任意的流式多模态模型](16-mio-any-to-any-streaming/docs/zh.md)
- [17 · 视频-语言模型：时间 token（词元） 与 grounding](17-video-language-temporal-grounding/docs/zh.md)
- [18 · 百万 token（词元） 上下文下的长视频理解](18-long-video-million-token/docs/zh.md)
- [19 · 音频-语言模型：从 Whisper 到 Audio Flamingo 3 的弧线](19-audio-language-whisper-to-af3/docs/zh.md)
- [20 · Omni 模型：Qwen2.5-Omni 与 Thinker-Talker 拆分](20-omni-models-thinker-talker/docs/zh.md)
- [21 · 具身 VLA：RT-2、OpenVLA、π0、GR00T](21-embodied-vlas-openvla-pi0-groot/docs/zh.md)
- [22 · 文档与图表理解](22-document-diagram-understanding/docs/zh.md)
- [23 · ColPali 与视觉原生文档 RAG（检索增强生成）](23-colpali-vision-native-rag/docs/zh.md)
- [24 · 多模态 RAG（检索增强生成） 与跨模态检索](24-multimodal-rag-cross-modal/docs/zh.md)
- [25 · 多模态 agent（智能体） 与 computer-use（综合实战）](25-multimodal-agents-computer-use/docs/zh.md)
