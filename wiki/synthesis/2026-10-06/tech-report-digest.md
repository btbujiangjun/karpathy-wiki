---
title: "LLM Tech Report Digest — 2026-10-06"
type: synthesis
created: 2026-10-06
updated: 2026-10-06
sources: []
tags: [tech-report, LLM, technical-report, system-card, model-card, arXiv, moe, hybrid-attention, scaling-law, long-context, multimodal, reasoning, RL, post-training]
---

# LLM Tech Report Digest — 2026-10-06

> 搜索各大 AI 公司最新大模型技术报告（Tech Report / Technical Report / System Card），重点关注大模型新架构（MoE, Mamba, hybrid）、训练方法（pre-training, post-training, alignment, RL）、Scaling Law / 缩放分析、多模态模型、长上下文模型、推理模型 / reasoning model。

> 本次检索基于最新公开技术报告与系统卡，聚焦 DeepSeek、OpenAI、Meta AI、Google DeepMind、Anthropic、Mistral AI、Qwen、Yi、Baichuan、Microsoft、Apple、NVIDIA、xAI、Amazon、Zhipu AI、InternLM、Moonshot AI、StepFun、ByteDance 等 19 家机构。


## DeepSeek

| 项目 | 信息 |
|---|---|
| 中文标题 | DeepSeek-V3 技术报告 |
| 英文标题 | DeepSeek-V3 Technical Report |
| 发布机构 | DeepSeek-AI |
| 模型名称/系列 | DeepSeek-V3 |
| 发布日期 | 2025-02-18 (arXiv v2) |
| 核心参数 | 671B 总参数，37B 激活参数（MoE）；14.8T token 预训练；Multi-head Latent Attention (MLA) |
| 主要创新点 | MLA + DeepSeekMoE 架构；无辅助损失的负载均衡策略（auxiliary-loss-free load balancing）；多 token 预测（Multi-Token Prediction, MTP）；训练稳定，2.788M H800 GPU 小时 |
| arXiv/论文链接 | [arXiv:2412.19437](https://arxiv.org/abs/2412.19437) |

### DeepSeek-V4 系列

| 项目 | 信息 |
|---|---|
| 中文标题 | DeepSeek-V4：迈向高效百万 token 上下文智能体 |
| 英文标题 | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| 发布机构 | DeepSeek-AI |
| 模型名称/系列 | DeepSeek-V4-Pro, DeepSeek-V4-Flash |
| 发布日期 | 2026-04-26 (preview) |
| 核心参数 | V4-Pro：1.6T 总参数，49B 激活；V4-Flash：284B 总参数，13B 激活；上下文 1M token |
| 主要创新点 | 混合 CSA + HCA 注意力（Compressed Sparse Attention + Hybrid Cross-attention）；Manifold-Constrained Hyper-Connections (mHC)；Muon 优化器（1.6T 规模）；FP4 量化感知训练（QAT）；显著降低 KV cache 与推理 FLOPs |
| arXiv/论文链接 | [arXiv:2606.19348](https://arxiv.org/abs/2606.19348) |

## OpenAI

| 项目 | 信息 |
|---|---|
| 中文标题 | GPT-5 系统卡 |
| 英文标题 | GPT-5 System Card |
| 发布机构 | OpenAI |
| 模型名称/系列 | GPT-5 (gpt-5-main, gpt-5-main-mini, gpt-5-thinking, gpt-5-thinking-mini, gpt-5-thinking-nano, gpt-5-thinking-pro) |
| 发布日期 | 2025-08-13 |
| 核心参数 | 未公开参数量（系统卡聚焦能力、安全与路由） |
| 主要创新点 | 统一系统 + 实时路由（dynamic router）自动选择 fast/deep reasoning；thinking 与 non-thinking 模式；safe-completions 安全训练；改进指令遵循、减少幻觉、sycophancy 降低 |
| arXiv/论文链接 | [arXiv:2601.03267](https://arxiv.org/abs/2601.03267) · [系统卡 PDF](https://cdn.openai.com/gpt-5-system-card.pdf) |

## Google DeepMind

| 项目 | 信息 |
|---|---|
| 中文标题 | Gemini 4 技术报告（系统卡/发布信息） |
| 英文标题 | Gemini 4 Technical/System Documentation |
| 发布机构 | Google DeepMind |
| 模型名称/系列 | Gemini 4 |
| 发布日期 | 2026-09-30（发布信息） |
| 核心参数 | 未详述 |
| 主要创新点 | 长上下文能力（百万级 token）；推理与 agent 能力强化；多模态基础模型 |
| arXiv/论文链接 | 发布信息：[Google Blog](https://deepmind.google/models/gemini/)（系统卡/技术报告见官方页面） |

## Meta AI

| 项目 | 信息 |
|---|---|
| 中文标题 | LLaMA 系列技术文档 |
| 英文标题 | Llama Technical Reports |
| 发布机构 | Meta AI |
| 模型名称/系列 | LLaMA 3/3.1/4 系列 |
| 发布日期 | 最新迭代持续更新 |
| 核心参数 | 多尺寸（8B–405B 等） |
| 主要创新点 | 标量混合精度训练、大规模预训练、指令微调与安全对齐；开源权重影响广泛 |
| arXiv/论文链接 | [LLaMA 3 技术报告](https://ai.meta.com/research/publications/llama-3-open-foundation-and-fine-tuned-chat-models/) |

## Anthropic

| 项目 | 信息 |
|---|---|
| 中文标题 | Claude 系统卡与评估 |
| 英文标题 | Claude System Cards |
| 发布机构 | Anthropic |
| 模型名称/系列 | Claude Sonnet 5.5, Claude Opus 5.5（等） |
| 发布日期 | 2025-09-28（Sonnet 5.5） |
| 核心参数 | 未公开 |
| 主要创新点 | Constitutional AI（宪法 AI）对齐；计算机使用（Computer Use）、推理与编码能力强化；安全优先 |
| arXiv/论文链接 | [Anthropic 系统卡](https://www.anthropic.com/research/system-cards) |

## Mistral AI

| 项目 | 信息 |
|---|---|
| 中文标题 | Mistral Medium 3.5 技术信息 |
| 英文标题 | Mistral Medium 3.5 |
| 发布机构 | Mistral AI |
| 模型名称/系列 | Medium 3.5 |
| 发布日期 | 2025-04-28（最新有据版本） |
| 核心参数 | 未详述 |
| 主要创新点 | 高效推理、工具调用、多模态能力；注重推理速度与成本平衡 |
| arXiv/论文链接 | [Mistral 发布页](https://mistral.ai/news/) |

## Qwen (Alibaba)

| 项目 | 信息 |
|---|---|
| 中文标题 | Qwen3.8-Next 架构设计：评估、效率与训练稳定性 |
| 英文标题 | On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability |
| 发布机构 | Qwen Team（阿里巴巴） |
| 模型名称/系列 | Qwen3.8-Flash-Next |
| 发布日期 | 2026-08-31 |
| 核心参数 | 125B 总参数，6B 激活（MoE）；额外 51B n-gram embedding 表（host offload）；稀疏混合专家架构 |
| 主要创新点 | Gated DeltaNet (GDN) + Qwen Sparse Attention (QSA) 混合注意力；Gated Residual (GR) 残差设计；n-gram embedding 扩展容量；Muon 优化器与训练稳定性改进；1/9 训练 FLOPs 达到接近 397B-A17B 水平 |
| arXiv/论文链接 | [arXiv:2608.30320](https://arxiv.org/abs/2608.30320) |

### Qwen3.8-Omni

| 项目 | 信息 |
|---|---|
| 中文标题 | Qwen3.8-Omni：迈向原生全模态智能体 |
| 英文标题 | Qwen3.8-Omni: Towards Native Omni-Modal Agents |
| 发布机构 | Qwen Team |
| 模型名称/系列 | Qwen3.8-Omni-Flash |
| 发布日期 | 2026-09-22 |
| 核心参数 | 基于 Qwen3.8-Next MoE 架构，上下文扩展至 1M token；原生多模态协同训练 |
| 主要创新点 | 原生全模态（文本-图像-音频-视频）协同训练；长上下文多模态推理；从文本向音视频迁移 agent 能力；配套 Qwen-MM-Plugins、Qwen-Live-Harness |
| arXiv/论文链接 | [arXiv:2609.25611](https://arxiv.org/abs/2609.25611) |

## NVIDIA

| 项目 | 信息 |
|---|---|
| 中文标题 | Nemotron 3 Ultra 技术报告 |
| 英文标题 | NVIDIA Nemotron 3 Ultra Technical Report |
| 发布机构 | NVIDIA |
| 模型名称/系列 | Nemotron 3 Ultra |
| 发布日期 | 近期发布（技术报告公开） |
| 核心参数 | 550B 总参数，55B 激活（MoE）；混合 Mamba–Transformer 架构 |
| 主要创新点 | 混合 Mamba–Transformer MoE 架构（hybrid Mamba–Transformer MoE）；推理效率优化；面向企业与推理场景 |
| arXiv/论文链接 | 详见 NVIDIA 技术博客/报告页：[NVIDIA Technical Reports](https://www.nvidia.com/en-us/research/publications/) |

## xAI

| 项目 | 信息 |
|---|---|
| 中文标题 | Grok 系统卡与技术文档 |
| 英文标题 | Grok System Cards |
| 发布机构 | xAI |
| 模型名称/系列 | Grok 4.6 等 |
| 发布日期 | 2025-08-12（Grok 4.6） |
| 核心参数 | 未公开 |
| 主要创新点 | 实时信息访问、推理能力强化；产品导向但持续迭代 |
| arXiv/论文链接 | [xAI 博客](https://x.ai/blog/) |

## Amazon

| 项目 | 信息 |
|---|---|
| 中文标题 | Amazon Nova 系列文档 |
| 英文标题 | Amazon Nova Model Documentation |
| 发布机构 | Amazon Web Services (AWS) |
| 模型名称/系列 | Amazon Nova（多模态/推理系列） |
| 发布日期 | 持续更新 |
| 核心参数 | 多尺寸 |
| 主要创新点 | AWS 原生多模态模型；推理成本优化；与 Bedrock 深度集成 |
| arXiv/论文链接 | [AWS Bedrock 文档](https://docs.aws.amazon.com/bedrock/) |

## Zhipu AI

| 项目 | 信息 |
|---|---|
| 中文标题 | GLM 系列技术报告 |
| 英文标题 | GLM Technical Reports |
| 发布机构 | Zhipu AI（智谱 AI） |
| 模型名称/系列 | GLM-5.3 系列 |
| 发布日期 | 2025-09-23（GLM-5.3 Prime） |
| 核心参数 | 753B MoE，总激活 40B（5.3 系列） |
| 主要创新点 | MoE 架构，post-training 强化；工具调用与推理能力；安全评估驱动发布节奏 |
| arXiv/论文链接 | [智谱 AI 官网](https://www.zhipuai.com/) |

## InternLM（上海 AI 实验室）

| 项目 | 信息 |
|---|---|
| 中文标题 | InternLumina-U2：面向全视觉理解、图像生成与编辑的多码本扩散大语言模型 |
| 英文标题 | InternLumina U2 — A Multi-Codebook Diffusion Large Language Model for Omni-Visual Understanding, Image Generation and Editing |
| 发布机构 | 上海人工智能实验室（Shanghai AI Laboratory） |
| 模型名称/系列 | InternLumina-U2 |
| 发布日期 | 2026-09-10（HuggingFace 上线）；技术报告 "Coming Soon" |
| 核心参数 | 16B-A1B MoE（16B 总参数，1B 激活）；8 码本全离散视觉表征（基于 AToken） |
| 主要创新点 | 全离散扩散路线统一理解+生成；昇腾 NPU 与 NVIDIA GPU 双硬件栈权重同步发布；系统性算子融合（FLA、GMM 融合算子）实现昇腾千卡集群端到端训练效率提升 1.85×；Apache 2.0 许可 |
| arXiv/论文链接 | 模型卡：[internlm/InternLumina-U2](https://huggingface.co/internlm/InternLumina-U2)（技术报告待发布） |

## Moonshot AI

| 项目 | 信息 |
|---|---|
| 中文标题 | Kimi 系列技术文档 |
| 英文标题 | Kimi Technical Reports |
| 发布机构 | Moonshot AI |
| 模型名称/系列 | Kimi K3（2.8T MoE，104B 激活）等 |
| 发布日期 | 2025-07-16（Kimi K3） |
| 核心参数 | 2.8T 总参数，104B 激活（MoE）；超长上下文能力 |
| 主要创新点 | 大规模 MoE、长上下文优化；工具调用与推理能力强化 |
| arXiv/论文链接 | [Moonshot AI 官网](https://www.moonshot.cn/) |

## StepFun（阶跃星辰）

| 项目 | 信息 |
|---|---|
| 中文标题 | Step 系列技术信息 |
| 英文标题 | StepFun Model Technical Reports |
| 发布机构 | StepFun（阶跃星辰） |
| 模型名称/系列 | Step 5 Preview、Step 3.7 Flash 等 |
| 发布日期 | 2025-09-18（Step 5 Preview 官宣） |
| 核心参数 | Step 5 Preview：600B-A27B 稀疏 MoE，1M 上下文；Step 3.7 Flash：196B MoE，11B 激活，400 tok/s |
| 主要创新点 | 大规模稀疏 MoE、长上下文（1M）、音频/多模态能力（StepAudio 系列）；StepAudio 3 Realtime 等技术报告见 arXiv |
| arXiv/论文链接 | [arXiv 搜索 StepFun/StepAudio](https://arxiv.org/search/?query=StepAudio+OR+StepFun&searchtype=all) |

## ByteDance（字节跳动）

| 项目 | 信息 |
|---|---|
| 中文标题 | Douyin 多模态嵌入模型技术报告 |
| 英文标题 | Douyin Multimodal Embedding Model Technical Report |
| 发布机构 | 字节跳动 Douyin Search Multimodal Team + 中国人民大学高瓴人工智能学院 |
| 模型名称/系列 | Douyin Multimodal Embedding（DME） |
| 发布日期 | 2026-08-03（arXiv v3） |
| 核心参数 | 2B / 9B 两档；MMEB-v2：74.8（2B）/ 78.4（9B） |
| 主要创新点 | 两阶段对比训练：Evidence-Grounded Typed Latent Reasoning + Cross-Conditional Reconstruction；只在训练期引入推理机制，推理期边际开销极小，线上效率接近标准对比编码器 |
| arXiv/论文链接 | [arXiv:2608.02148](https://arxiv.org/abs/2608.02148) |

## Microsoft

| 项目 | 信息 |
|---|---|
| 中文标题 | VibeVoice-ASR-Streaming：流式说话人归属 ASR 的 LLM 端到端方案 |
| 英文标题 | VibeVoice-ASR-Streaming Technical Report |
| 发布机构 | Microsoft Research + 中国科学院大学 + 上海交通大学 |
| 模型名称/系列 | VibeVoice-ASR-Streaming |
| 发布日期 | 2026-09-02（arXiv v2） |
| 核心参数 | LLM-based end-to-end 流式方案（未公开参数量） |
| 主要创新点 | 端到端流式说话人归属 ASR；统一架构减少模块堆叠；流式处理适配实时场景 |
| arXiv/论文链接 | [arXiv:2609.02812](https://arxiv.org/abs/2609.02812) |

## Xiaomi

| 项目 | 信息 |
|---|---|
| 中文标题 | CocktailASR-1：面向目标说话人语音识别的多维能力模型 |
| 英文标题 | CocktailASR-1: A Multidimensional Capability Model for Target-Speaker Speech Recognition |
| 发布机构 | Xiaomi Inc. |
| 模型名称/系列 | CocktailASR-1 |
| 发布日期 | 2026-09-13（arXiv） |
| 核心参数 | 未详述 |
| 主要创新点 | 目标说话人语音识别（Target-Speaker ASR）；多维能力建模；不依赖独立语音分离模块 |
| arXiv/论文链接 | [arXiv:2609.11274](https://arxiv.org/abs/2609.11274) |

## 其他关注机构（Yi、Baichuan、Apple）

| 机构 | 状态（2026-10-06） | 备注 |
|---|---|---|
| Yi（01.AI） | 较低活跃度 | 最新公开版本多为 Yi 1.5（2024）；近期未见新的 frontier 技术报告/系统卡 |
| Baichuan | 持续更新 | Baichuan-Omni-1.5、Baichuan-M3-235B 等公开，商业版本 Baichuan4 系列；需持续跟踪技术报告发布 |
| Apple | 技术报告缺席 | 近期未见公开的 frontier 大模型技术报告/系统卡；研究更多体现在系统层面 |

## 补充说明

- **去重原则**：所有条目均基于公开技术报告/系统卡，优先选择 arXiv 链接，避免重复收录同一模型不同版本。
- **时间范围**：覆盖 2025–2026 年最新重要报告，重点关注 2026 年发布的技术报告（DeepSeek-V4、Qwen3.8-Next/Omni、InternLumina-U2、DME、VibeVoice-ASR-Streaming、CocktailASR-1）。
- **口径说明**：部分模型（OpenAI/Gemini/Claude）未公开全部参数量，系统卡侧重能力评估、安全与路由设计。

