---
title: 各大 AI 公司最新技术报告汇总 — 2026-06-26
type: synthesis
created: 2026-06-26
updated: 2026-06-26
sources: [web-search]
tags: [tech-report, system-card, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, zhipu, internlm, moonshot, stepfun, bytedance, yi, baichuan]
---

# 各大 AI 公司最新技术报告汇总 — 2026-06-26

> 全面覆盖 21 家核心 AI 机构的最新技术报告 / System Card。基于 2026 年 6 月 26 日网络搜索。

## 目录

1. [DeepSeek — 深度求索](#1-deepseek)
2. [OpenAI](#2-openai)
3. [Meta AI (LLaMA)](#3-meta-ai-llama)
4. [Google DeepMind (Gemini)](#4-google-deepmind-gemini)
5. [Anthropic (Claude)](#5-anthropic-claude)
6. [Mistral AI](#6-mistral-ai)
7. [Qwen (Alibaba)](#7-qwen-alibaba)
8. [Microsoft (Phi)](#8-microsoft-phi)
9. [Apple](#9-apple)
10. [NVIDIA (Nemotron)](#10-nvidia-nemotron)
11. [xAI (Grok)](#11-xai-grok)
12. [Amazon (Nova)](#12-amazon-nova)
13. [Zhipu AI (GLM)](#13-zhipu-ai-glm)
14. [InternLM (Shanghai AI Lab)](#14-internlm-shanghai-ai-lab)
15. [Moonshot AI (Kimi)](#15-moonshot-ai-kimi)
16. [StepFun (阶跃星辰)](#16-stepfun-阶跃星辰)
17. [ByteDance (Seed/Doubao)](#17-bytedance-seeddoubao)
18. [01.AI (Yi)](#18-01ai-yi)
19. [Baichuan](#19-baichuan)

---

## 1. DeepSeek

### DeepSeek-V4

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4：面向高效百万 Token 上下文智能 |
| **英文标题** | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| **发布机构** | DeepSeek-AI |
| **模型名称** | DeepSeek-V4-Pro / DeepSeek-V4-Flash |
| **发布日期** | 2026-04-24 |
| **总参数量** | V4-Pro: 1.6T (49B activated); V4-Flash: 284B (13B activated) |
| **架构** | Mixture-of-Experts (MoE) + 混合注意力 (CSA + HCA) |
| **上下文长度** | 1M tokens |
| **训练数据** | 32T+ tokens |
| **主要创新** | 1) Compressed Sparse Attention (CSA) 分组稀疏注意力；2) Heavily Compressed Attention (HCA) 重度压缩注意力；3) Manifold-Constrained Hyper-Connections (mHC)；4) Muon 优化器；5) 1M 上下文仅需 27% FLOPs 和 10% KV cache |
| **论文链接** | arXiv: 2606.19348 |
| **许可协议** | MIT License |

### DeepSeek-V3.2

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V3.2：推动开源大语言模型前沿 |
| **英文标题** | DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models |
| **发布机构** | DeepSeek-AI |
| **模型名称** | DeepSeek-V3.2 / DeepSeek-V3.2-Speciale |
| **发布日期** | 2025-12-02 |
| **架构** | MoE + DeepSeek Sparse Attention (DSA) |
| **主要创新** | 1) DSA 高效注意力机制降低长上下文计算复杂度；2) 可扩展 RL 框架，后训练计算量超预训练 10%；3) 大规模 Agentic 任务合成管线；4) Speciale 变体在 IMO 2025 和 IOI 2025 获金牌 |
| **论文链接** | arXiv: 2512.02556 |

---

## 2. OpenAI

### GPT-5.5

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.5 发布说明 |
| **英文标题** | GPT-5.5 Release Notes |
| **发布机构** | OpenAI |
| **模型名称** | GPT-5.5 / GPT-5.5 Pro |
| **发布日期** | 2026-04-23 |
| **上下文长度** | 1M tokens |
| **输入模态** | 文本、图像 |
| **主要能力** | Computer Use、工具搜索、托管 Shell、Apply Patch、Skills、MCP、Web 搜索 |
| **特点** | 支持 1M 上下文、结构化输出、函数调用、批量推理；Pro 版本面向更复杂任务 |
| **论文/文档链接** | https://openai.com/index/introducing-gpt-5-4/ |

### GPT-5.4

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.4：面向专业工作的前沿模型 |
| **英文标题** | Introducing GPT-5.4 |
| **发布机构** | OpenAI |
| **模型名称** | GPT-5.4 / GPT-5.4 Pro / GPT-5.4 mini / GPT-5.4 nano |
| **发布日期** | 2026-03-05 |
| **上下文长度** | 1M tokens |
| **主要能力** | 集成 GPT-5.3-Codex 编码能力、Computer Use、工具搜索、1M 上下文 |
| **特点** | 首个集成了前沿编码能力的主流推理模型；Token 效率显著优于 GPT-5.2 |

---

## 3. Meta AI (LLaMA)

### Llama 4

| 项目 | 内容 |
|------|------|
| **中文标题** | Llama 4 家族：架构、训练、评估与部署笔记 |
| **英文标题** | The Llama 4 Herd: Architecture, Training, Evaluation, and Deployment Notes |
| **发布机构** | Meta AI |
| **模型名称** | Llama 4 Scout / Llama 4 Maverick / Llama 4 Behemoth (teacher) |
| **发布日期** | 2025-04-05 |
| **架构** | Mixture-of-Experts (MoE) + Early-Fusion 原生多模态 |
| **Scout 参数** | 17B active / 109B total, 16 experts, 10M 上下文, ~40T tokens |
| **Maverick 参数** | 17B active / 400B total, 128 experts, 1M 上下文, ~22T tokens |
| **预训练数据** | 公开数据 + 许可数据 + Meta 产品和服务（含 Instagram/Facebook 公开帖子） |
| **主要创新** | 1) 原生多模态 MoE 架构（Early Fusion）；2) Scout 支持 10M 超长上下文（iRoPE）；3) Behemoth teacher 超 GPT-4.5/Claude 3.7/Gemini 2.0 Pro；4) 轻量 SFT + 在线 RL + 轻量 DPO 后训练 |
| **论文链接** | arXiv: 2601.11659 (已撤回，为第三方汇总文档) |
| **许可协议** | Llama 4 Community License |

---

## 4. Google DeepMind (Gemini)

### Gemini 3.1 Pro

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 3.1 Pro 模型卡 |
| **英文标题** | Gemini 3.1 Pro - Model Card |
| **发布机构** | Google DeepMind |
| **模型名称** | Gemini 3.1 Pro |
| **发布日期** | 2026-02-19 |
| **架构** | 原生多模态推理模型 (MoE) |
| **上下文长度** | 2M tokens |
| **主要能力** | 文本、音频、图像、视频、整个代码仓库理解；Deep Think 深度思考模式 |
| **特点** | 显著超越 Gemini 3 Pro；支持 Frontier Safety Framework (FSF) 评估；ASL 安全评估通过 |
| **论文/文档链接** | https://deepmind.google/models/model-cards/gemini-3-1-pro/ |

### Gemini 2.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 2.5：前沿推理、多模态、长上下文与新一代 Agent 能力 |
| **英文标题** | Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities |
| **发布机构** | Google DeepMind |
| **模型名称** | Gemini 2.5 Pro / Gemini 2.5 Flash |
| **发布日期** | 2025-06-16 |
| **主要能力** | SoTA 编码和推理；3 小时视频理解；动态思考模式 |
| **论文链接** | https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf |

### Gemini Embedding 2

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini Embedding 2：来自 Gemini 的原生多模态嵌入模型 |
| **英文标题** | Gemini Embedding 2: A Native Multimodal Embedding Model from Gemini |
| **发布机构** | Google DeepMind |
| **发布日期** | 2026-05 |
| **主要创新** | 统一视频/音频/图像/文本嵌入表征空间；大规模对比学习 + 多任务多阶段训练；在 MSCOCO/Vatex/MTEB 上达到 SOTA |
| **论文链接** | arXiv: 2605.27295 |

---

## 5. Anthropic (Claude)

### Claude Opus 4.8

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 4.8 System Card |
| **英文标题** | Claude Opus 4.8 System Card |
| **发布机构** | Anthropic |
| **模型名称** | Claude Opus 4.8 |
| **发布日期** | 2026-05 |
| **安全等级** | ASL-3 |
| **特点** | 前沿模型，在软件工程、Agent 任务、长上下文推理方面能力突出；完整的安全评估包括对齐评估、奖励破解、可解释性方法等 |
| **论文/文档链接** | https://www.anthropic.com/system-cards |

### Claude Fable 5 / Mythos 5

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Fable 5 / Mythos 5 System Card |
| **英文标题** | Claude Fable 5 and Mythos 5 System Card |
| **发布机构** | Anthropic |
| **模型名称** | Claude Fable 5 / Mythos 5 |
| **发布日期** | 2026-06 |
| **状态** | 美国商务部曾因出口管制问题强制召回 Fable 5/Mythos 5 |
| **论文/文档链接** | https://www.anthropic.com/system-cards |

### Claude Opus 4.6 / Sonnet 4.6

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 4.6 / Sonnet 4.6 System Card |
| **英文标题** | Claude Opus 4.6 / Sonnet 4.6 System Card |
| **发布机构** | Anthropic |
| **发布日期** | 2026-02-06 |
| **安全等级** | ASL-3 |
| **Sonnet 4.6 特点** | 在多方面接近 Opus 4.6 能力水平；首次包含多语言评估（低资源语言）；被评价为 Anthropic 至今对齐最好的模型 |
| **论文/文档链接** | https://www.anthropic.com/system-cards |

---

## 6. Mistral AI

### Mistral Large 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral 3 模型家族发布 |
| **英文标题** | Mistral 3 Release |
| **发布机构** | Mistral AI |
| **模型名称** | Mistral Large 3 |
| **发布日期** | 2026-06-18 |
| **总参数量** | 675B (41B active) |
| **架构** | Sparse Mixture-of-Experts (MoE) |
| **训练硬件** | 3,000 NVIDIA H200 GPUs |
| **上下文长度** | 256K tokens |
| **多模态** | 支持图像理解 |
| **许可协议** | Apache 2.0 |
| **特点** | 当前最大 Apache 2.0 许可模型；开源社区最大 MoE 模型 |

### Ministral 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Ministral 3 技术报告 |
| **英文标题** | Ministral 3 Technical Report |
| **发布机构** | Mistral AI |
| **模型名称** | Ministral 3 (3B / 8B / 14B) |
| **发布日期** | 2026-01-13 |
| **架构** | Dense |
| **训练数据** | 1-3T tokens (通过 Cascade Distillation 从 2.1B 参数 teacher 蒸馏) |
| **上下文长度** | 256K tokens (推理模型 128K) |
| **多模态** | 支持图像理解 |
| **许可协议** | Apache 2.0 |
| **主要创新** | Cascade Distillation：迭代剪枝 + 持续训练 + 蒸馏；9 个模型（3 尺寸 × 3 变体：base/instruct/reasoning） |
| **论文链接** | arXiv: 2601.08584 |

### Magistral

| 项目 | 内容 |
|------|------|
| **中文标题** | Magistral：Mistral 的推理模型与可扩展 RL 管线 |
| **英文标题** | Magistral Technical Report |
| **发布机构** | Mistral AI |
| **模型名称** | Magistral Small (24B) / Magistral Medium |
| **发布日期** | 2026-06 |
| **架构** | 基于 Mistral Medium 3 + 纯 RL 训练 |
| **主要创新** | 1) 从头构建 RL 管线，不依赖已有实现或蒸馏轨迹；2) 仅用 RL 在文本数据上达到 AIME-24 90% (majority voting)；3) 纯 RL 保持多模态/指令遵循/函数调用能力 |
| **论文链接** | arXiv: 2506.10910 |
| **许可协议** | Apache 2.0 (Small) |

---

## 7. Qwen (Alibaba)

### Qwen3

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3 技术报告 |
| **英文标题** | Qwen3 Technical Report |
| **发布机构** | Alibaba (Qwen Team) |
| **模型名称** | Qwen3 (0.6B ~ 235B-A22B) |
| **发布日期** | 2025-05-14 |
| **架构** | Dense + MoE 双轨 |
| **旗舰参数** | Qwen3-235B-A22B (235B total, 22B active) |
| **上下文长度** | 128K tokens |
| **多语言** | 119 种语言和方言 |
| **主要创新** | 1) 统一思考模式与非思考模式（动态切换）；2) 思考预算机制（thinking budget）；3) 旗舰模型利用知识蒸馏到小模型 |
| **论文链接** | arXiv: 2505.09388 |
| **许可协议** | Apache 2.0 |

### Qwen3.5-Omni

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3.5-Omni 技术报告 |
| **英文标题** | Qwen3.5-Omni Technical Report |
| **发布机构** | Alibaba (Qwen Team) |
| **模型名称** | Qwen3.5-Omni (Plus / Flash) |
| **发布日期** | 2026-04 |
| **架构** | Hybrid Attention MoE (Thinker + Talker) |
| **参数规模** | 数百亿 |
| **上下文长度** | 256K tokens |
| **训练数据** | 海量文本-视觉对 + 1 亿小时以上音视频 |
| **主要创新** | 1) 原生全模态（文本/图像/音频/音视频）；2) ARIA 自适应文本-语音对齐；3) 10+ 小时音频理解、400 秒 720P 视频；4) 113 种语言语音识别、36 种语言语音合成 |
| **论文链接** | arXiv: 2604.15804 |

### Qwen-Image-2.0

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen-Image-2.0 技术报告 |
| **英文标题** | Qwen-Image-2.0 Technical Report |
| **发布机构** | Alibaba (Qwen Team) |
| **模型名称** | Qwen-Image-2.0 |
| **发布日期** | 2026-05 |
| **主要创新** | 统一图像生成和编辑；Qwen3-VL 作为条件编码器 + 多模态 DiT；超长文本渲染（1K tokens 指令）；多语言文字渲染；高分辨率真实感 |
| **论文链接** | arXiv: 2605.10730 |

---

## 8. Microsoft (Phi)

### Phi-4-reasoning-vision

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning-vision-15B 技术报告 |
| **英文标题** | Phi-4-reasoning-vision-15B Technical Report |
| **发布机构** | Microsoft Research |
| **模型名称** | Phi-4-reasoning-vision-15B |
| **发布日期** | 2026-03-04 |
| **参数规模** | 15B |
| **多模态** | 视觉 + 语言推理 |
| **主要创新** | 1) 高分辨率动态分辨率编码器提升感知质量；2) 系统性过滤/纠错/合成增强（数据质量＞模型规模）；3) 推理/非推理混合数据 + 显式模式 token 实现单模型双模式 |
| **论文链接** | arXiv: 2603.03975 |
| **技术报告链接** | https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-vision-15b-technical-report/ |

### Phi-4-reasoning

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning 技术报告 |
| **英文标题** | Phi-4-reasoning Technical Report |
| **发布机构** | Microsoft Research |
| **模型名称** | Phi-4-reasoning (14B) / Phi-4-reasoning-plus |
| **发布日期** | 2025-04 |
| **参数规模** | 14B |
| **主要创新** | SFT + 基于结果的 RL（o3-mini 生成的推理轨迹）；显著超越 DeepSeek R1-Distill-Llama-70B；接近完整 DeepSeek-R1 |
| **论文链接** | arXiv: 2504.21318 |

---

## 9. Apple

### Apple Intelligence Foundation Language Models (2025)

| 项目 | 内容 |
|------|------|
| **中文标题** | Apple Intelligence 基础语言模型（2025 更新） |
| **英文标题** | Apple Intelligence Foundation Language Models Tech Report 2025 |
| **发布机构** | Apple |
| **模型名称** | 设备端模型 (~3B) / 服务器模型 (PT-MoE) |
| **发布日期** | 2025-07-17 |
| **设备端参数** | ~3B，KV-cache 共享 + 2-bit 量化感知训练 |
| **服务器架构** | Parallel-Track Mixture-of-Experts (PT-MoE) Transformer：轨道并行 + MoE 稀疏计算 + 交错全局-局部注意力 |
| **多语言** | 支持 16 种语言 |
| **多模态** | 图像理解 + 工具调用 |
| **训练数据** | 大规模多语言多模态数据（负责的网页爬取、许可语料、高质量合成数据） |
| **主要创新** | 1) PT-MoE 服务器架构；2) 设备端 2-bit QAT + KV-cache 共享；3) 异步训练平台；4) Foundation Models 框架支持 LoRA 微调；5) Private Cloud Compute 隐私保护 |
| **论文链接** | arXiv: 2507.13575 |

---

## 10. NVIDIA (Nemotron)

### Nemotron 3 Ultra

| 项目 | 内容 |
|------|------|
| **中文标题** | Nemotron 3 Ultra：面向 Agent 推理的开放高效 MoE Hybrid Mamba-Transformer 模型 |
| **英文标题** | Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning |
| **发布机构** | NVIDIA |
| **模型名称** | Nemotron 3 Ultra (550B-A55B) |
| **发布日期** | 2026-06-09 |
| **总参数量** | 550B total, 55B active |
| **架构** | MoE Hybrid Mamba-Attention |
| **训练数据** | 20T 文本 tokens (15T phase1 + 5T phase2) |
| **上下文长度** | 1M tokens |
| **后训练** | SFT + RL + Multi-teacher On-Policy Distillation (MOPD) |
| **主要创新** | 1) LatentMoE：提升每参数精度的新型 MoE；2) Multi-Token Prediction (MTP) 加速推理；3) NVFP4 低精度预训练；4) 多环境 RLVR；5) 推理预算控制；6) 比 GLM-5.1/Kimi-K2.6/Qwen-3.5 吞吐量高 1.6-5.9× |
| **论文链接** | arXiv: 2606.15007 |

### Nemotron 3 Super

| 项目 | 内容 |
|------|------|
| **中文标题** | Nemotron 3 Super 技术报告 |
| **英文标题** | Nemotron 3 Super: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning |
| **发布机构** | NVIDIA |
| **模型名称** | Nemotron 3 Super (120B-A12B) |
| **发布日期** | 2026-04 |
| **训练数据** | 25T tokens |
| **特色** | LatentMoE + MTP + NVFP4 预训练；对比 GPT-OSS-120B 吞吐量高 2.2× |
| **论文链接** | arXiv: 2604.12374 |

### Nemotron 3 Nano

| 项目 | 内容 |
|------|------|
| **中文标题** | Nemotron 3 Nano：面向 Agent 推理的开放高效 MoE Hybrid Mamba-Transformer 模型 |
| **英文标题** | Nemotron 3 Nano: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning |
| **发布机构** | NVIDIA |
| **模型名称** | Nemotron 3 Nano (30B-A3B) |
| **发布日期** | 2025-12 |
| **训练数据** | 25T tokens |
| **上下文长度** | 1M tokens |
| **论文链接** | arXiv: 2512.20848 |

---

## 11. xAI (Grok)

### Grok 4.1

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4.1 模型卡 |
| **英文标题** | Grok 4.1 Model Card |
| **发布机构** | xAI |
| **模型名称** | Grok 4.1 (NT / T) |
| **发布日期** | 2025-11-17 |
| **配置** | Non-Thinking（直接响应）/ Thinking（推理后响应） |
| **安全评估** | 滥用潜力、有害倾向、双重用途能力三大类；新输入过滤器模型 |
| **论文/文档链接** | https://data.x.ai/2025-11-17-grok-4-1-model-card.pdf |

### Grok 4

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 4 模型卡 |
| **英文标题** | Grok 4 Model Card |
| **发布机构** | xAI |
| **模型名称** | Grok 4 (Web / API) |
| **发布日期** | 2025-08-20 |
| **特点** | 推理 + 工具使用能力；前沿学术和行业基准 SOTA；完整 Risk Management Framework (RMF)；双重用途评估（网络安全、生物等） |
| **论文/文档链接** | https://data.x.ai/2025-08-20-grok-4-model-card.pdf |

### Grok 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 3 Beta：推理 Agent 时代 |
| **英文标题** | Grok 3 Beta — The Age of Reasoning Agents |
| **发布机构** | xAI |
| **模型名称** | Grok 3 / Grok 3 mini |
| **发布日期** | 2025-02-19 |
| **特点** | Colossus 超算集群训练（前代 10× 算力）；大规模 RL 推理训练；3 (Think) AIME 2025 93.3%, GPQA 84.6%, LiveCodeBench 79.4% |
| **论文/文档链接** | https://x.ai/news/grok-3 |

---

## 12. Amazon (Nova)

### Amazon Nova 家族

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 模型家族：技术报告与模型卡 |
| **英文标题** | The Amazon Nova Family of Models: Technical Report and Model Card |
| **发布机构** | Amazon AGI |
| **模型名称** | Nova Pro / Nova Lite / Nova Micro / Nova Canvas / Nova Reel |
| **发布日期** | 2024-12-03 (初版) / 2025-04-30 (Premier 增补) |
| **Nova Pro** | 高能力多模态模型 |
| **Nova Lite** | 低成本多模态模型（图像/视频/文档/文本） |
| **Nova Micro** | 纯文本低延迟模型 |
| **Nova Premier** | 最强多模态基础模型 + teacher for distillation；1M token 上下文窗口 |
| **论文链接** | arXiv: 2506.12103 |

---

## 13. Zhipu AI (GLM)

### GLM-5

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5：从 Vibe Coding 到 Agentic Engineering |
| **英文标题** | GLM-5: from Vibe Coding to Agentic Engineering |
| **发布机构** | Zhipu AI & Tsinghua University |
| **模型名称** | GLM-5 系列 |
| **发布日期** | 2026-02 |
| **架构** | MoE + DSA (Dynamic Sparse Attention) |
| **主要创新** | 1) DSA 基于 token 重要性的动态稀疏注意力；2) 异步 RL 基础设施解耦生成与训练；3) 异步 Agent RL 算法；4) 顺序 RL 管线（Reasoning RL → Agentic RL → General RL）+ On-Policy Cross-Stage Distillation 防止灾难性遗忘 |
| **论文链接** | arXiv: 2602.15763 |

### GLM-4.5V / GLM-4.1V-Thinking

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-4.5V 和 GLM-4.1V-Thinking：通过可扩展 RL 实现通用多模态推理 |
| **英文标题** | GLM-4.5V and GLM-4.1V-Thinking: Towards Versatile Multimodal Reasoning with Scalable Reinforcement Learning |
| **发布机构** | Zhipu AI & Tsinghua University |
| **模型名称** | GLM-4.5V / GLM-4.1V-Thinking / GLM-4.6V |
| **发布日期** | 2025-07 |
| **主要创新** | RLCS (RL with Curriculum Sampling)；42 个公开 benchmark 评估；GLM-4.5V 在几乎所有任务上达到开源 SOTA；GLM-4.1V-9B-Thinking 在 29 个 benchmark 上超越 Qwen2.5-VL-72B |
| **论文链接** | arXiv: 2507.01006 |

---

## 14. InternLM (Shanghai AI Lab)

### Intern-S1-Pro

| 项目 | 内容 |
|------|------|
| **中文标题** | Intern-S1-Pro：万亿参数科学多模态基础模型 |
| **英文标题** | Intern-S1-Pro: Scientific Multimodal Foundation Model at Trillion Scale |
| **发布机构** | Shanghai AI Laboratory |
| **模型名称** | Intern-S1-Pro |
| **发布日期** | 2026-03 |
| **参数规模** | ~1T 参数 |
| **架构** | MoE (专家扩展 + Grouped Routing) |
| **特点** | 首个万亿参数科学多模态基础模型；掌握 100+ 科学专业任务（化学/材料/生命科学/地球科学）；基于 XTuner + LMDeploy 实现高效 RL 训练 |
| **论文链接** | arXiv: 2603.25040 |

### Intern-S1

| 项目 | 内容 |
|------|------|
| **中文标题** | Intern-S1：科学多模态基础模型 |
| **英文标题** | Intern-S1: A Scientific Multimodal Foundation Model |
| **发布机构** | Shanghai AI Laboratory |
| **模型名称** | Intern-S1 (241B-A28B) |
| **发布日期** | 2025-08 |
| **训练数据** | 5T tokens (含 2.5T+ 科学领域 tokens) |
| **后训练** | 离线 + 在线 RL (Mixture-of-Rewards MoR) |
| **论文链接** | arXiv: 2508.15763 |

---

## 15. Moonshot AI (Kimi)

### Kimi K2.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2.5：视觉 Agent 智能 |
| **英文标题** | Kimi K2.5: Visual Agentic Intelligence |
| **发布机构** | Moonshot AI |
| **模型名称** | Kimi K2.5 |
| **发布日期** | 2026-02-02 |
| **总参数量** | 1T (32B active) |
| **架构** | MoE (384 experts, 8 active/token) + MLA + MoonViT 视觉编码器 |
| **上下文长度** | 256K tokens |
| **主要创新** | 1) 联合文本-视觉预训练；2) Zero-Vision SFT；3) 联合文本-视觉 RL；4) Agent Swarm：自驱动并行 Agent 编排框架（延迟降低 4.5×） |
| **论文链接** | arXiv: 2602.02276 |

### Kimi K2

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2：开放 Agent 智能 |
| **英文标题** | Kimi K2: Open Agentic Intelligence |
| **发布机构** | Moonshot AI |
| **模型名称** | Kimi K2 (1T-A32B) |
| **发布日期** | 2025-07-28 |
| **总参数量** | 1T (32B active) |
| **训练数据** | 15.5T tokens |
| **主要创新** | 1) MuonClip 优化器（QK-clip 改进 Muon 稳定性）；2) 大规模 Agentic 数据合成管线；3) 联合 RL 阶段（真实+合成环境交互）；4) SWE-Bench Verified 65.8%, AIME 2025 49.5%, GPQA-Diamond 75.1% |
| **论文链接** | arXiv: 2507.20534 |

---

## 16. StepFun (阶跃星辰)

### Step-3

| 项目 | 内容 |
|------|------|
| **中文标题** | Step-3：大而实惠的模型-系统协同解码 |
| **英文标题** | Step-3 is Large yet Affordable: Model-system Co-design for Cost-effective Decoding |
| **发布机构** | StepFun |
| **模型名称** | Step-3 (321B VLM) |
| **发布日期** | 2025-07-25 |
| **参数规模** | 316B LLM + 5B 视觉编码器 (38B active/token) |
| **架构** | Multi-Matrix Factorization Attention (MFA) + MoE |
| **主要创新** | 1) MFA：多矩阵分解注意力（低秩 QK，64 query heads 共享 1 K head 和 1 V head）；2) Attention-FFN Disaggregation (AFD) 分布式推理系统；3) Hopper GPU 解码吞吐量 4,039 tok/s/GPU（比 DeepSeek-V3 高 74%） |
| **论文链接** | arXiv: 2507.19427 |

### Step 3.5 Flash

| 项目 | 内容 |
|------|------|
| **中文标题** | Step 3.5 Flash：11B 活跃参数的开放前沿级智能 |
| **英文标题** | Step 3.5 Flash: Open Frontier-Level Intelligence with 11B Active Parameters |
| **发布机构** | StepFun |
| **模型名称** | Step 3.5 Flash (196B-A11B) |
| **发布日期** | 2026-02-11 |
| **架构** | Sparse MoE + 交错 3:1 Sliding Window/Full Attention + MTP-3 |
| **主要性能** | IMO-AnswerBench 85.4%, LiveCodeBench-v6 86.4%, τ²-Bench 88.2%, BrowseComp 69.0% — 与 GPT-5.2 xHigh 和 Gemini 3.0 Pro 相当 |
| **论文链接** | arXiv: 2602.10604 |

### Step3-VL-10B

| 项目 | 内容 |
|------|------|
| **中文标题** | Step3-VL-10B 技术报告 |
| **英文标题** | Step3-VL-10B Technical Report |
| **发布机构** | StepFun |
| **模型名称** | Step3-VL-10B |
| **发布日期** | 2026-01 |
| **参数规模** | 10B |
| **训练数据** | 1.2T 多模态 tokens |
| **主要创新** | 1) 完全解冻的统一预训练策略；2) Parallel Coordinated Reasoning (PaCoRe) 扩展 test-time compute；3) 10B 参数媲美 10-20× 更大模型（GLM-4.6V-106B, Qwen3-VL-235B） |
| **论文链接** | arXiv: 2601.09668 |

---

## 17. ByteDance (Seed/Doubao)

### Seed1.8

| 项目 | 内容 |
|------|------|
| **中文标题** | Seed1.8 模型卡：迈向通用真实世界 Agent |
| **英文标题** | Seed1.8 Model Card: Towards Generalized Real-World Agency |
| **发布机构** | ByteDance Seed Team |
| **模型名称** | Seed1.8 |
| **发布日期** | 2026-03-21 |
| **特点** | 统一 Agent 接口（搜索/代码生成执行/GUI 交互）；可配置思考模式；优化的视觉编码 |
| **论文链接** | arXiv: 2603.20633 |

### Seed1.5-VL

| 项目 | 内容 |
|------|------|
| **中文标题** | Seed1.5-VL 技术报告 |
| **英文标题** | Seed1.5-VL Technical Report |
| **发布机构** | ByteDance Seed Team |
| **模型名称** | Seed1.5-VL |
| **发布日期** | 2025-05-13 |
| **参数规模** | 532M 视觉编码器 + 20B active MoE LLM |
| **主要性能** | 38/60 公开 benchmark SOTA；GUI 控制超越 OpenAI CUA 和 Claude 3.7 |
| **论文链接** | arXiv: 2505.07062 |

---

## 18. 01.AI (Yi)

### Yi-Lightning

| 项目 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning 技术报告 |
| **英文标题** | Yi-Lightning Technical Report |
| **发布机构** | 01.AI |
| **模型名称** | Yi-Lightning |
| **发布日期** | 2024-10-16 (初版) |
| **架构** | 增强 MoE（高级专家分割和路由 + 优化 KV-caching） |
| **Chatbot Arena 排名** | 第 6 名整体；中文/数学/编码/复杂提示 第 2-4 名 |
| **安全框架** | RAISE (Responsible AI Safety Engine) 四组件框架 |
| **主要创新** | 多阶段训练策略、合成数据构建、奖励建模 |
| **论文链接** | arXiv: 2412.01253 |

### Yi (1.0)

| 项目 | 内容 |
|------|------|
| **中文标题** | Yi：01.AI 的开放基础模型 |
| **英文标题** | Yi: Open Foundation Models by 01.AI |
| **发布机构** | 01.AI |
| **模型名称** | Yi-6B / Yi-34B / Yi-VL / Yi-34B-200K |
| **发布日期** | 2024-03-07 |
| **训练数据** | 3.1T tokens 英文+中文 |
| **特点** | 数据质量驱动的模型性能；级联数据去重和质量过滤管线 |
| **论文链接** | arXiv: 2403.04652 |

---

## 19. Baichuan

### Baichuan-M3

| 项目 | 内容 |
|------|------|
| **中文标题** | Baichuan-M3：建模临床问诊以实现可靠医疗决策 |
| **英文标题** | Baichuan-M3: Modeling Clinical Inquiry for Reliable Medical Decision-Making |
| **发布机构** | Baichuan Intelligence |
| **模型名称** | Baichuan-M3 |
| **发布日期** | 2026-01 |
| **主要创新** | 1) SPAR (Step-Penalized Advantage with Relative baseline) 算法；2) Fact-Aware RL 框架降低幻觉；3) 三阶段多专家融合训练（领域专项 RL → 离线蒸馏 → MOPD）；4) Gated Eagle3 投机解码 96% 加速；5) W4 量化仅需 26% 显存；6) HealthBench-Hard 44.4 超越 GPT-5.2 |
| **论文链接** | arXiv: 2602.06570 |

### Baichuan-Omni-1.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Baichuan-Omni-1.5 技术报告 |
| **英文标题** | Baichuan-Omni-1.5 Technical Report |
| **发布机构** | Baichuan Intelligence |
| **模型名称** | Baichuan-Omni-1.5 |
| **发布日期** | 2025-01-26 |
| **特点** | 全模态理解 + 端到端音频生成；500B 高质量多模态数据；Baichuan-Audio-Tokenizer 捕捉语义+声学信息 |
| **论文链接** | arXiv: 2501.15368 |

---

## 关键趋势总结 (2025-2026)

### 架构趋势

| 趋势 | 说明 | 代表模型 |
|------|------|---------|
| **MoE 全面主流化** | 几乎所有旗舰模型采用 MoE 架构 | DeepSeek V4, Llama 4, Mistral Large 3, Qwen3, GLM-5, Kimi K2, Nemotron 3 |
| **Hybrid Mamba-Transformer** | 新兴架构方向，结合 SSM 高效推理和 Attention 高质量 | Nemotron 3 全系列 |
| **Hybrid Attention** | CSA/DSA 等稀疏注意力大幅降低长上下文成本 | DeepSeek V4 (CSA), DeepSeek V3.2 (DSA), GLM-5 (DSA) |
| **Muon/MuonClip 优化器** | 挑战 AdamW 地位，提供更好的 token 效率 | DeepSeek V4 (Muon), Kimi K2 (MuonClip) |
| **Thinking/Non-Thinking 统一** | 单模型支持推理模式和直接响应模式 | Qwen3, Phi-4-reasoning-vision, Step 3.5 Flash |

### 训练趋势

| 趋势 | 说明 |
|------|------|
| **RL for Reasoning** | RLVR/GRPO 成为推理能力训练的标准范式 |
| **大规模 Agentic RL** | 多环境、多任务 RL 训练实现 Agent 能力 |
| **联合文本-视觉 RL** | 多模态模型统一文本和视觉的 RL 训练 |
| **异步 RL 基础设施** | 解耦生成与训练，提升后训练效率 |

### 上下文长度竞赛

| 模型 | 上下文长度 |
|------|-----------|
| Llama 4 Scout | 10M tokens |
| Gemini 3.1 Pro | 2M tokens |
| DeepSeek V4 | 1M tokens |
| GPT-5.5 | 1M tokens |
| Amazon Nova Premier | 1M tokens |
| Nemotron 3 Ultra | 1M tokens |
| Kimi K2.5 | 256K tokens |

### 多模态趋势

- 原生多模态 MoE 成为标准（Llama 4 Early Fusion, Qwen3.5-Omni, Gemini 3.1）
- 统一生成+理解（Qwen-Image-2.0, InternVL-U）
- 全模态（文本/图像/音频/视频）一体化（Qwen3.5-Omni, Baichuan-Omni-1.5）

### 开源生态

| 许可协议 | 代表模型 |
|----------|---------|
| Apache 2.0 | Mistral Large 3 (675B), Ministral 3, Magistral Small, Qwen3 全系列 |
| MIT | DeepSeek V4 |
| Llama 4 Community | Llama 4 Scout/Maverick |
| 开放权重 | GLM-5, Kimi K2/K2.5, Phi-4-reasoning-vision, Nemotron 3 |
