---
title: 各大 AI 公司最新技术报告汇总 (2026年5月)
type: synthesis
created: 2026-05-25
updated: 2026-05-25
sources:
  - DeepSeek V4 Technical Report
  - OpenAI GPT-5 System Card
  - OpenAI GPT-5.5 System Card
  - OpenAI o3/o4-mini System Card
  - The Llama 4 Herd
  - Gemini 2.5 Technical Report
  - Claude Opus 4 System Card
  - Claude Opus 4.6 System Card
  - Mistral Large 3 Technical Report
  - Qwen3.5 Technical Report
  - Qwen3.5-Omni Technical Report
  - Phi-4 Technical Report
  - Phi-4-Mini Technical Report
  - Apple Intelligence Foundation Language Models: Tech Report 2025
  - NVIDIA Nemotron 3 Technical Report
  - Amazon Nova Family Technical Report
  - Amazon Nova 2 Technical Report
  - GLM-5 Technical Report
  - InternLM2 Technical Report
  - Kimi K2 Technical Report
  - Yi-Lightning Technical Report
  - ByteDance Seed 2.0 Technical Report
tags: [tech-report, survey, 2026, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, zhipu, internlm, moonshot, bytedance]
---

# 各大 AI 公司最新技术报告汇总

> 截至 2026 年 5 月，覆盖 17 家 AI 机构的最新 Model Card / System Card / Technical Report。重点关注：新架构、训练方法、对齐技术、Scaling Law、长上下文、推理模型。

---

## DeepSeek — 深度求索

### DeepSeek V4

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek V4 技术报告 |
| **英文标题** | DeepSeek V4 Technical Report |
| **机构** | DeepSeek AI |
| **模型名称** | DeepSeek V4 Pro / Flash |
| **核心参数** | Pro: 1.6T 总参数, 49B 激活参数; Flash: 284B 总参数, 13B 激活参数; MoE; 1M context |
| **创新点** | mHC (Manifold-Constrained Hyper-Connections) 稳定千层信号传播; 混合注意力 (CSA 稀疏 + HCA 密集压缩); Muon 优化器替代 AdamW; KV cache 降低 90% |
| **论文链接** | [Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) / [PDF](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf) |
| **发布日期** | 2026-04-24 |

> DeepSeek V4 经历 484 天研发，在算力受限条件下通过激进架构创新实现效率反超。Pro 和 Flash 均支持 1M context window，定价差异化。

---

## OpenAI

### GPT-5 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5 System Card |
| **英文标题** | GPT-5 System Card |
| **机构** | OpenAI |
| **模型名称** | GPT-5 (gpt-5-thinking / gpt-5-main / gpt-5-thinking-mini) |
| **核心参数** | 统一系统含智能路由: 快速模型 + 深度推理模型 + 实时路由器; 1M context |
| **创新点** | 实时路由持续训练; 幻觉降低 8x vs o3; 安全完成 (safe-completions); 多模态集成; Preparedness Framework High capability 评级 |
| **论文链接** | [arXiv:2601.03267](https://arxiv.org/abs/2601.03267) / [PDF](https://cdn.openai.com/gpt-5-system-card.pdf) |
| **发布日期** | 2025-08 |

### GPT-5.5 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.5 System Card |
| **英文标题** | GPT-5.5 System Card |
| **机构** | OpenAI |
| **模型名称** | GPT-5.5 (代号 "Spud") |
| **核心参数** | 完全重建的基础模型 (非增量更新); 原生全模态 (text/image/audio/video 统一架构) |
| **创新点** | 与 NVIDIA GB200/GB300 硬件协同设计; Codex 自动重写 serving 基础设施 (速度提升 20%); Terminal-Bench 2.0 SOTA 82.7%; SWE-Bench Pro 58.6% |
| **论文链接** | [System Card](https://cdn.openai.com/gpt-5-system-card.pdf) |
| **发布日期** | 2026-04 |

### o3 & o4-mini System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | OpenAI o3 和 o4-mini System Card |
| **英文标题** | OpenAI o3 and o4-mini System Card |
| **机构** | OpenAI |
| **模型名称** | o3 / o4-mini |
| **核心参数** | 推理模型; o4-mini 为轻量推理变体 |
| **创新点** | 推理缩放; 网络安全评估; 自主 CBRN 风险评估 |
| **论文链接** | [PDF](https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf) |
| **发布日期** | 2025-04 |

---

## Meta — LLaMA

### The Llama 4 Herd

| 项目 | 内容 |
|------|------|
| **中文标题** | Llama 4 模型族: 架构、训练、评估与部署 |
| **英文标题** | The Llama 4 Herd: Architecture, Training, Evaluation, and Deployment Notes |
| **机构** | Meta |
| **模型名称** | Llama 4 Scout / Maverick / Behemoth (preview only) |
| **核心参数** | Scout: 109B 总, 17B 激活, 16 experts, 10M context; Maverick: ~400B 总, 17B 激活, 128 experts, 1M context; Behemoth: ~2T, 288B 激活 (未发布) |
| **创新点** | 全系 MoE 架构; 原生多模态 (early fusion, text + image); iRoPE 交错位置编码实现超长上下文; 预训练 22T tokens |
| **论文链接** | [arXiv:2601.11659](https://arxiv.org/abs/2601.11659) (已撤回) |
| **发布日期** | 2025-04-05 |

> 全系 MoE 架构是 Llama 4 最大的架构变革。Scout 的 10M context 理论窗口为开源模型最长。Benchmark 表现弱于 DeepSeek V4 和 Qwen 3.5。

---

## Google DeepMind — Gemini

### Gemini 2.5 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 2.5: 推动推理、多模态、长上下文和智能体能力的边界 |
| **英文标题** | Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities |
| **机构** | Google DeepMind |
| **模型名称** | Gemini 2.5 Pro / Flash / 2.0 Flash / Flash-Lite |
| **核心参数** | Sparse MoE; 1M context window (Pro); 原生多模态 (video/audio/text) |
| **创新点** | Thinking Mode 推理; 3 小时视频理解; Agentic 工作流; SOTA coding/reasoning benchmarks |
| **论文链接** | [PDF](https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf) / [arXiv:2507.06261](https://arxiv.org/abs/2507.06261) |
| **发布日期** | 2025-06-17 |

### Gemini 3.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 3.5: 边界智能与行动能力 |
| **英文标题** | Gemini 3.5: Frontier Intelligence with Action |
| **机构** | Google DeepMind |
| **模型名称** | Gemini 3.1 Pro Preview / 3.5 |
| **核心参数** | 1M context; 原生多模态; Deep Think 推理 |
| **创新点** | 更强的 agentic 能力; Google Search grounding; Gemini Omni 支持视频生成 |
| **论文链接** | [deepmind.google](https://deepmind.google/) |
| **发布日期** | 2026-05 (Google I/O) |

---

## Anthropic — Claude

### Claude Opus 4 & Sonnet 4 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 4 & Sonnet 4 System Card |
| **英文标题** | System Card: Claude Opus 4 & Claude Sonnet 4 |
| **机构** | Anthropic |
| **模型名称** | Claude Opus 4 / Sonnet 4 |
| **核心参数** | 混合推理模型; ASL-3 (Opus 4) / ASL-2 (Sonnet 4) |
| **创新点** | Hybrid Reasoning (extended thinking); 首次包含 Alignment Assessment (欺骗、隐藏目标、自保行为); Model Welfare 评估; SWE-bench SOTA |
| **论文链接** | [PDF](https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2ff47/claude-opus-4-and-claude-sonnet-4-system-card.pdf) |
| **发布日期** | 2025-05 |

### Claude Opus 4.6 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 4.6 System Card |
| **英文标题** | Claude Opus 4.6 System Card |
| **机构** | Anthropic |
| **模型名称** | Claude Opus 4.6 |
| **核心参数** | ASL-3; 改进的 agentic 能力和 long context reasoning |
| **创新点** | 使用 Activation Oracles / Attribution Graphs / Sparse Autoencoders 进行可解释性; Extended + Adaptive Thinking modes; SWE-bench Verified SOTA |
| **论文链接** | [PDF](https://www-cdn.anthropic.com/14e4fb01875d2a69f646fa5e574dea2b1c0ff7b5.pdf) |
| **发布日期** | 2026-02 |

### Claude Opus 4.7 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 4.7 System Card |
| **英文标题** | Claude Opus 4.7 System Card |
| **机构** | Anthropic |
| **模型名称** | Claude Opus 4.7 |
| **核心参数** | 最新旗舰; ASL-3 |
| **创新点** | SWE-bench Pro 64.3%; 增强 agentic coding 和 long-horizon 任务 |
| **论文链接** | [PDF](https://cdn.sanity.io/files/4zrzovbb/website/037f06850df7fbe871e206dad004c3db5fd50340.pdf) |
| **发布日期** | 2026-04 |

---

## Mistral AI

### Mistral Large 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral Large 3 技术报告 |
| **英文标题** | Mistral Large 3 Technical Report |
| **机构** | Mistral AI |
| **模型名称** | Mistral Large 3 |
| **核心参数** | 675B 总参数, 41B 激活参数; Sparse MoE; 256K context; Apache 2.0 |
| **创新点** | 开源 MoE 旗舰; MMLU-Pro 73.11%; MATH-500 93.60%; 3,000 H200 GPUs 训练 |
| **论文链接** | [mistral.ai](https://mistral.ai/news/) |
| **发布日期** | 2025-12 |

### Mistral Small 4

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral Small 4 |
| **英文标题** | Mistral Small 4 |
| **机构** | Mistral AI |
| **模型名称** | Mistral Small 4 (mistral-small-2603) |
| **核心参数** | 119B 总, ~6B 激活 (128 experts, 4 active/token); 256K context; 多模态 (text + image); Apache 2.0 |
| **创新点** | 合并 Magistral (推理) + Pixtral (视觉) + Devstral (编码) 三个产品于一体 |
| **论文链接** | [Hugging Face](https://huggingface.co/mistralai) |
| **发布日期** | 2026-03-16 |

### Mistral Medium 3.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral Medium 3.5 |
| **英文标题** | Mistral Medium 3.5 |
| **机构** | Mistral AI |
| **模型名称** | Mistral Medium 3.5 |
| **核心参数** | 128B Dense; 256K context; 多模态; 可配置 reasoning effort |
| **创新点** | 开源权重; Gmail/Slack/Jira 集成; agentic workflow; 50+ 语言 |
| **论文链接** | [mistral.ai](https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5) |
| **发布日期** | 2026-04-29 |

---

## Qwen — Alibaba (阿里巴巴)

### Qwen3.5 系列

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3.5 技术报告 |
| **英文标题** | Qwen3.5 Technical Report |
| **机构** | Alibaba Cloud Qwen Team |
| **模型名称** | Qwen3.5 系列 (397B-A17B, 122B-A10B, 35B-A3B, 27B, 9B, 4B, 2B, 0.8B, Flash, Omni-Plus) |
| **核心参数** | 旗舰: 397B 总, 17B 激活; MoE + Gated DeltaNet 混合架构; 256K context (可扩展至 1M); Apache 2.0 |
| **创新点** | ~75% Gated DeltaNet (linear attention) + ~25% softmax attention; 原生多模态 early fusion; 201 语言; Thinking / Non-Thinking 双模式; Vocabulary 从 150K 扩展到 250K |
| **论文链接** | [arXiv:2604.15804](https://arxiv.org/abs/2604.15804) (Omni) |
| **发布日期** | 2026-02-16 (旗舰) / 2026-03-02 (小模型) |

> Qwen3.5-9B 以 1/13 的参数达到 GPT-OSS-120B 级别性能，标志着"效率 > 规模"的范式转变。Hugging Face 下载超 6 亿。

---

## Yi — 01.AI (零一万物)

### Yi-Lightning

| 项目 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning 技术报告 |
| **英文标题** | Yi-Lightning Technical Report |
| **机构** | 01.AI |
| **模型名称** | Yi-Lightning |
| **核心参数** | Enhanced MoE; 6th Chatbot Arena (2024-10); 中文/数学/编程类别 2-4 名 |
| **创新点** | 细粒度 expert segmentation + routing; 优化 KV-caching; RAISE (Responsible AI Safety Engine) 四组件安全框架; 多阶段训练 + 合成数据 + Reward Modeling |
| **论文链接** | [arXiv:2412.01253](https://arxiv.org/abs/2412.01253) |
| **发布日期** | 2024-12 |

> Yi-Lightning 的观察指出传统静态 benchmark 结果与动态人类偏好之间存在显著差距，警示了对 benchmark 效用的过度依赖。

---

## Microsoft — Phi

### Phi-4

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4 技术报告 |
| **英文标题** | Phi-4 Technical Report |
| **机构** | Microsoft Research |
| **模型名称** | Phi-4 |
| **核心参数** | 14B Dense Decoder-only; 合成数据为主 |
| **创新点** | 数据质量驱动的训练 (synthetic data 超过 organic data); Multi-agent prompting + self-revision + instruction reversal 数据生成; 超越教师模型 GPT-4 在 STEM QA 上; Pivotal Token DPO |
| **论文链接** | [arXiv:2412.08905](https://arxiv.org/abs/2412.08905) / [Microsoft Research](https://www.microsoft.com/en-us/research/publication/phi-4-technical-report/) |
| **发布日期** | 2024-12 |

### Phi-4-Reasoning & Phi-4-Reasoning-Plus

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4-Reasoning 技术报告 |
| **英文标题** | Phi-4-reasoning Technical Report |
| **机构** | Microsoft Research |
| **模型名称** | Phi-4-reasoning / Phi-4-reasoning-plus / Phi-4-mini-reasoning |
| **核心参数** | 14B / 3.8B (mini); 基于 Phi-4 |
| **创新点** | o3-mini 合成推理链训练; 超越 DeepSeek-R1-Distill-70B 和接近 DeepSeek-R1 |
| **论文链接** | [PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf) |
| **发布日期** | 2025-04 |

### Phi-4-Mini & Phi-4-Multimodal

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4-Mini 技术报告: 通过 Mixture-of-LoRAs 实现紧凑多模态 |
| **英文标题** | Phi-4-Mini Technical Report: Compact yet Powerful Multimodal Language Models via Mixture-of-LoRAs |
| **机构** | Microsoft Research |
| **模型名称** | Phi-4-Mini (3.8B) / Phi-4-Multimodal |
| **核心参数** | 3.8B; 200K vocabulary; GQA; 128K context |
| **创新点** | Mixture-of-LoRAs 多模态架构; 超越同尺寸开源模型 2x; 中文/多语言优化 |
| **论文链接** | [arXiv:2503.01743](https://arxiv.org/abs/2503.01743) |
| **发布日期** | 2025-02 |

---

## Apple

### Apple Intelligence Foundation Language Models: Tech Report 2025

| 项目 | 内容 |
|------|------|
| **中文标题** | Apple Intelligence 基础语言模型: 2025 技术报告 |
| **英文标题** | Apple Intelligence Foundation Language Models: Tech Report 2025 |
| **机构** | Apple |
| **模型名称** | AFM-on-device (~3B) / AFM-server (PT-MoE) |
| **核心参数** | 设备端: ~3B, KV-cache sharing, 2-bit QAT; 服务端: Parallel-Track MoE (PT-MoE) |
| **创新点** | KV-cache sharing (37.5% 减少); 2-bit 量化感知训练; PT-MoE (track parallelism + MoE sparse + interleaved global-local attention); Swift Foundation Models framework; LoRA adapter fine-tuning |
| **论文链接** | [arXiv:2507.13575](https://arxiv.org/abs/2507.13575) |
| **发布日期** | 2025-07-17 |

> Apple 的差异化在于设备端优先 + Private Cloud Compute。尽管模型参数规模远小于竞品，但通过架构创新 (KV-cache sharing, 2-bit training) 实现设备端高效推理。

---

## NVIDIA

### Nemotron 3 Family

| 项目 | 内容 |
|------|------|
| **中文标题** | NVIDIA Nemotron 3 模型族 |
| **英文标题** | NVIDIA Nemotron 3 Family of Models |
| **机构** | NVIDIA |
| **模型名称** | Nemotron 3 Nano (30B-A3B) / Super (120B-A12B) / Ultra (~500B-A50B) |
| **核心参数** | Nano: 31.6B 总, 3.6B 激活; Super: 120B 总, 12.7B 激活; Ultra: ~500B 总, ~50B 激活; 混合 Mamba-Transformer MoE; 1M context |
| **创新点** | Hybrid Mamba-2 + Transformer MoE; LatentMoE (Super/Ultra); Multi-Token Prediction; NVFP4 训练; Multi-environment RL 后训练; Granular Reasoning Budget Control; 1M context (RULER 91.75%) |
| **论文链接** | [Nano Tech Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Nano-Technical-Report.pdf) / [Super Tech Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf) / [Whitepaper](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-White-Paper.pdf) |
| **发布日期** | Nano: 2025-12-15 / Super: 2026-03-11 |

> Nemotron 标志着 NVIDIA 从 GPU 供应商转型为 LLM 供应商。Super 在 DeepInfra 上仅 $0.10/1M input，449 tokens/sec 推理速度。

---

## xAI — Grok

### Grok 4 & 4.3

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4 系统报告 |
| **英文标题** | Grok 4 System Report |
| **机构** | xAI |
| **模型名称** | Grok 4 / Grok 4 Heavy / Grok 4.3 Beta / Grok 4.20 / Grok 4.1 Fast |
| **核心参数** | Grok 4: 256K context, always-on reasoning; Grok 4.3: ~0.5T params, 1M context; Grok 4.20: 2M context |
| **创新点** | Colossus 200K GPU 训练; RL at pretraining scale; 6x 训练效率提升 vs Grok 3; 并行推理 (Grok 4 Heavy); Humanity's Last Exam 50%; 原生 PDF/表格/PPT 生成 (4.3) |
| **论文链接** | [x.ai](https://x.ai/news/grok-4) |
| **发布日期** | Grok 4: 2025-07 / Grok 4.3: 2026-04-17 |

> xAI 尚未发布详细的 System Card/Technical Report — 目前公开信息主要来自 Elon Musk 的 X 帖子和第三方评测。Grok 4.3 的 benchmark 数据尚未官方披露。

---

## Amazon — AWS

### Amazon Nova Family

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 模型族: 技术报告和模型卡 |
| **英文标题** | The Amazon Nova Family of Models: Technical Report and Model Card |
| **机构** | Amazon AGI |
| **模型名称** | Nova Micro / Lite / Pro / Premier / Canvas / Reel |
| **核心参数** | Micro: text-only, 128K context; Lite: multimodal, 300K; Pro: multimodal, 300K; Premier: 1M context; 200+ 语言 |
| **创新点** | Transformer + DPO/PPO 对齐; Nova Micro 210 tokens/sec (vs Claude 3.5 Sonnet 57); 图像/视频生成 (Canvas/Reel); Agentic workflow 表现突出 |
| **论文链接** | [arXiv:2506.12103](https://arxiv.org/abs/2506.12103) |
| **发布日期** | 2024-12 |

### Amazon Nova 2

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 2: 多模态推理和生成模型 |
| **英文标题** | Amazon Nova 2: Multimodal Reasoning and Generation Models |
| **机构** | Amazon AGI |
| **模型名称** | Nova 2 Lite / Pro / Omni / Sonic |
| **核心参数** | 1M context; 端到端多模态; Dynamic reasoning controls |
| **创新点** | Extended Thinking 控制; Nova 2 Omni unified multimodal (text/image/video/audio in, text/image out); Nova 2 Sonic 语音到语音; Nova Forge 模型定制服务 |
| **论文链接** | [Amazon Science](https://www.amazon.science/publications/amazon-nova-2-multimodal-reasoning-and-generation-models) |
| **发布日期** | 2025-12-02 |

---

## Zhipu AI — 智谱 AI

### GLM-5

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5 技术报告 |
| **英文标题** | GLM-5 Technical Report |
| **机构** | Zhipu AI (Z.ai) / Tsinghua University KEG Lab |
| **模型名称** | GLM-5 |
| **核心参数** | 744B MoE, 40B 激活; 200K context; 预训练 28.5T tokens; MIT 许可证 |
| **创新点** | DeepSeek Sparse Attention (DSA); SWE-bench Verified 77.8%; Agent 模式 (8 小时自主执行); "Slime" RL 基础设施; 华为 Ascend 910B 原生训练 (GLM-5.1) |
| **论文链接** | [z.ai](https://z.ai/blog/glm-5) |
| **发布日期** | 2026-02-11 |

### GLM-5.1

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5.1 |
| **英文标题** | GLM-5.1 |
| **机构** | Zhipu AI (Z.ai) |
| **模型名称** | GLM-5.1 |
| **核心参数** | 754B MoE, 40B 激活; 200K context; MIT 许可证 |
| **创新点** | SWE-Bench Pro 58.4% (2026-04 排名 #1); 8 小时自主执行循环; Ascend-Native 训练 (完全脱离美国芯片); AIME 2026: 95.3% |
| **论文链接** | [Hugging Face](https://huggingface.co/zhipuai) |
| **发布日期** | 2026-04-07 |

---

## InternLM — 上海 AI 实验室

### InternLM2

| 项目 | 内容 |
|------|------|
| **中文标题** | InternLM2 技术报告 |
| **英文标题** | InternLM2 Technical Report |
| **机构** | Shanghai AI Laboratory / SenseTime / CUHK |
| **模型名称** | InternLM2 (7B / 20B) / InternLM3-8B |
| **核心参数** | 预训练 4K→32K context; SFT + COOL RLHF |
| **创新点** | COOL RLHF (Conditional Online RLHF) 解决偏好冲突和 reward hacking; 200K "Needle-in-a-Haystack" 测试优异 |
| **论文链接** | [arXiv:2403.17297](https://arxiv.org/abs/2403.17297) |
| **发布日期** | 2024-03-26 |

> InternLM3-8B 于 2025-01-15 发布，支持 deep thinking mode 和 normal response mode 双模式。

---

## Moonshot AI — 月之暗面 (Kimi)

### Kimi K2

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2: 开放智能体智能 |
| **英文标题** | Kimi K2: Open Agentic Intelligence |
| **机构** | Moonshot AI (月之暗面) |
| **模型名称** | Kimi K2 (Base / Instruct) |
| **核心参数** | 1T 总参数, 32B 激活参数; MoE (384 experts, 8 active/token); MLA; 128K context; 15.5T tokens 预训练 |
| **创新点** | MuonClip 优化器 (Muon + QK-clip 解决训练不稳定); 零 loss spike 训练; 大规模 agentic data pipeline; 强化学习 agent 框架 |
| **论文链接** | [arXiv:2507.20534](https://arxiv.org/abs/2507.20534) / [GitHub](https://github.com/MoonshotAI/Kimi-K2) |
| **发布日期** | 2025-07 |

### Kimi K2.6

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2.6 |
| **英文标题** | Kimi K2.6 |
| **机构** | Moonshot AI (月之暗面) |
| **模型名称** | Kimi K2.6 |
| **核心参数** | 1T MoE; 262K context; 原生多模态 agentic model |
| **创新点** | Agent Swarm 多智能体编排; long-horizon coding; 开源 (Modified MIT) |
| **论文链接** | [Hugging Face](https://huggingface.co/moonshotai/Kimi-K2.6) |
| **发布日期** | 2026-04 |

---

## ByteDance — 字节跳动 (豆包)

### Doubao Seed 2.0

| 项目 | 内容 |
|------|------|
| **中文标题** | Seed 2.0 技术报告 |
| **英文标题** | Seed 2.0 Technical Report |
| **机构** | ByteDance Seed Team |
| **模型名称** | Seed 2.0 Pro / Lite / Mini / Code |
| **核心参数** | Pro: 旗舰多模态; 256K context; 多模态 (text/image/video); Pro $0.43/$2.15 per MTok |
| **创新点** | AIME 2025: 98.3; Codeforces 3020; SWE-Bench Verified 76.5%; VideoMME 89.5%; ICPC 金牌 / IMO 金牌级别; 小时级视频理解; ~10x cheaper vs 西方竞品 |
| **论文链接** | [seed.bytedance.com](https://seed.bytedance.com/en/seed2) |
| **发布日期** | 2026-02-14 |

> 豆包 App 在中国拥有 1.55 亿周活跃用户。Seed 2.0 通过火山引擎提供 API，价格仅为 GPT-5.2 的 1/3.7 (input) 到 1/5.9 (output)。

---

## 跨机构对比总结

### 架构趋势

| 趋势 | 代表机构 |
|------|---------|
| MoE 成为主流 | DeepSeek, Meta, Mistral, Qwen, NVIDIA, Zhipu, Moonshot, 01.AI |
| 混合注意力 (Linear + Softmax) | Qwen (Gated DeltaNet), NVIDIA (Mamba-Transformer) |
| 原生多模态 (Early Fusion) | Meta (Llama 4), Qwen (3.5), Apple (PT-MoE), ByteDance (Seed 2.0) |
| 推理 / Thinking 模式标配 | OpenAI, Anthropic, Google, DeepSeek, Qwen, Mistral, NVIDIA |
| 长上下文竞争 (1M+) | DeepSeek, Google, Meta (Scout 10M), NVIDIA, xAI (Grok 4.20 2M) |

### 对齐与安全

| 方法 | 代表机构 |
|------|---------|
| RLHF / DPO / PPO | 几乎所有 |
| ASL 分级 (Responsible Scaling) | Anthropic (ASL-2/3), OpenAI (Preparedness Framework) |
| 可解释性 Sparse Autoencoders | Anthropic (Claude 4.6) |
| Model Welfare 评估 | Anthropic (首次在 Claude 4 引入) |
| RAISE 框架 | 01.AI (Yi-Lightning) |

### 训练创新

| 创新 | 机构 | 详情 |
|------|------|------|
| Muon 优化器 | DeepSeek V4 | 替代 AdamW, 矩阵正交化 |
| MuonClip | Moonshot K2 | Muon + QK-clip, 零训练不稳定 |
| Synthetic Data 为主 | Microsoft Phi-4 | Multi-agent prompting + self-revision |
| COOL RLHF | InternLM2 | Conditional Online RLHF |
| Multi-Token Prediction | DeepSeek V3, NVIDIA Nemotron 3 | |
| FP8 训练 | DeepSeek V3, Qwen 3.5 | |
| NVFP4 | NVIDIA Nemotron 3 | 4-bit 浮点训练 |
| 2-bit QAT | Apple AFM | 设备端 2-bit 量化训练 |

### 长上下文能力

| 模型 | Context Window | 备注 |
|------|---------------|------|
| Llama 4 Scout | 10M | iRoPE, 理论值 |
| Grok 4.20 | 2M | |
| DeepSeek V4 | 1M | CSA + HCA hybrid |
| Gemini 2.5 Pro | 1M | |
| GPT-5.5 | 1M | |
| Claude Opus 4.7 | 1M | |
| NVIDIA Nemotron 3 | 1M | RULER 91.75%@1M |
| Amazon Nova Premier | 1M | |
| Qwen 3.5 | 256K (可扩展至 1M) | |
| GLM-5 | 200K | DSA |
| Kimi K2 | 128K | |
| Phi-4-Mini | 128K | |
| Apple AFM-server | 未披露 | Private Cloud Compute |

### 推理模型 (Reasoning Models) 格局

| 组织 | 推理模型 | 方式 |
|------|---------|------|
| OpenAI | o3 / o4-mini / GPT-5-thinking | Thinking tokens |
| Anthropic | Claude Opus 4+ Extended Thinking | Extended/Adaptive thinking |
| Google | Gemini 2.5 Pro Deep Think | Thinking + Deep Think |
| DeepSeek | V4 (thinking / max-thinking) | 三种推理强度 |
| xAI | Grok 4 (always-on reasoning) | 实时推理模式 |
| Qwen | Qwen 3.5 Thinking / Non-thinking | 双模式 |
| Microsoft | Phi-4-reasoning / Plus | CoT reasoning |
| NVIDIA | Nemotron 3 | Granular Reasoning Budget Control |
| Mistral | Medium 3.5 | Configurable reasoning_effort |

---

## 未公开发布正式 Tech Report 的机构

下列机构发布了重要模型，但截至 2026 年 5 月尚未公开详细的 Technical Report 或 System Card：

- **xAI (Grok 4.3)** — 仅有 Elon Musk 的 X 帖子和第三方评测，无正式 System Card
- **ByteDance Seed 2.0** — 官方网页提供了 Model Card 级别信息但无完整 arXiv 论文
- **InternLM3-8B** — 仅有模型权重，无独立 Tech Report（InternLM2 是最近的完整报告）
- **Mistral Large 3 / Small 4 / Medium 3.5** — 缺少独立详尽的 Tech Report PDF
- **Google Gemini 3.5** — 2026-05 刚发布，暂无独立 Tech Report
