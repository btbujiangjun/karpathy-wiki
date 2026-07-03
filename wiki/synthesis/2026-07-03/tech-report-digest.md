---
title: "大模型技术报告综合摘要 — 2026年7月"
type: synthesis
created: 2026-07-03
updated: 2026-07-03
tags: [tech-report-digest, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, zhipu, internlm, moonshot, bytedance, stepfun, baichuan, 01-ai]
---

# 大模型技术报告综合摘要 — 2026年7月

> 覆盖 18+ 机构的最新大模型技术报告/System Card。数据截至 2026-07-03。

---

## 目录

1. [DeepSeek — DeepSeek-V4](#1-deepseek--deepseek-v4)
2. [OpenAI — GPT-5.6 / GPT-5.5 / GPT-5](#2-openai--gpt-56--gpt-55--gpt-5)
3. [Meta AI — Llama 4](#3-meta-ai--llama-4)
4. [Google DeepMind — Gemini 3.1 Pro](#4-google-deepmind--gemini-31-pro)
5. [Anthropic — Claude Sonnet 5 / Opus 4.8 / Mythos Preview](#5-anthropic--claude-sonnet-5--opus-48--mythos-preview)
6. [Mistral AI — Mistral Large 3 / Ministral 3 / Magistral](#6-mistral-ai--mistral-large-3--ministral-3--magistral)
7. [Alibaba Qwen — Qwen3 / Qwen3.5-Omni](#7-alibaba-qwen--qwen3--qwen35-omni)
8. [Microsoft — Phi-4-reasoning-vision](#8-microsoft--phi-4-reasoning-vision)
9. [Apple — Apple Foundation Models 三代](#9-apple--apple-foundation-models-三代)
10. [NVIDIA — Nemotron 3 Ultra / Nemotron-Labs-Diffusion](#10-nvidia--nemotron-3-ultra--nemotron-labs-diffusion)
11. [xAI — Grok 4.3](#11-xai--grok-43)
12. [Amazon — Amazon Nova Premier](#12-amazon--amazon-nova-premier)
13. [Zhipu AI — GLM-5](#13-zhipu-ai--glm-5)
14. [Shanghai AI Lab — Intern-S1-Pro](#14-shanghai-ai-lab--intern-s1-pro)
15. [Moonshot AI — Kimi K2 / K2.5](#15-moonshot-ai--kimi-k2--k25)
16. [ByteDance — Seed1.8](#16-bytedance--seed18)
17. [StepFun — Step 3.5 Flash / Step-3](#17-stepfun--step-35-flash--step-3)
18. [Baichuan — Baichuan-M3/M4](#18-baichuan--baichuan-m3m4)
19. [01.AI — Yi-Lightning](#19-01ai--yi-lightning)

---

## 1. DeepSeek — DeepSeek-V4

| 字段 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4：面向高效百万 Token 上下文智能 |
| **英文标题** | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| **发布机构** | DeepSeek-AI |
| **模型名称** | DeepSeek-V4-Pro (1.6T total / 49B activated), DeepSeek-V4-Flash (284B total / 13B activated) |
| **发布日期** | 2026-06-19 (arXiv) |
| **核心参数** | MoE；1M context length；32T+ tokens pre-training；FP4 + FP8 混合精度 |
| **主要创新点** | (1) 混合注意力架构：Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA)，1M context 下仅需 V3.2 的 27% FLOPs 和 10% KV cache；(2) Manifold-Constrained Hyper-Connections (mHC) 增强残差连接；(3) Muon optimizer 加速收敛 |
| **arXiv** | https://arxiv.org/abs/2606.19348 |

## 2. OpenAI — GPT-5.6 / GPT-5.5 / GPT-5

### GPT-5.6 Preview

| 字段 | 内容 |
|------|------|
| **英文标题** | GPT-5.6 Preview System Card |
| **发布机构** | OpenAI |
| **模型名称** | GPT-5.6 Sol（旗舰）、Terra（经济型）、Luna（快速型） |
| **发布日期** | 2026-06-25 |
| **核心参数** | 推理模型系列；Preparedness Framework 评估下 Cybersecurity / Biological 为 High 等级 |
| **主要创新点** | 三模型产品体系；real-time output monitoring 安全栈升级；Sol/Terra/Luna 分层覆盖不同场景 |
| **链接** | https://deploymentsafety.openai.com/gpt-5-6-preview/gpt-5-6-preview.pdf |

### GPT-5.5

| 字段 | 内容 |
|------|------|
| **英文标题** | GPT-5.5 System Card |
| **发布机构** | OpenAI |
| **模型名称** | GPT-5.5 / GPT-5.5 Pro |
| **发布日期** | 2026-04-23 |
| **主要创新点** | 复杂实际工作优化（coding, research, document/spreadsheet creation）；~200 early-access partners 测试；最强安全防护 |
| **链接** | https://openai.com/index/gpt-5-5-system-card/ |

### GPT-5

| 字段 | 内容 |
|------|------|
| **英文标题** | GPT-5 System Card |
| **发布机构** | OpenAI |
| **模型名称** | GPT-5-main / GPT-5-thinking / GPT-5-thinking-pro |
| **发布日期** | 2025-08-13 (System Card) |
| **主要创新点** | 统一系统含 router 自动分配 fast/thinking model；parallel test-time compute；safe-completions 安全训练 |
| **arXiv** | https://arxiv.org/abs/2601.03267 |

## 3. Meta AI — Llama 4

| 字段 | 内容 |
|------|------|
| **英文标题** | The Llama 4 Herd: Architecture, Training, Evaluation, and Deployment Notes |
| **发布机构** | Meta AI |
| **模型名称** | Llama 4 Scout (17Bx16E, 109B total), Llama 4 Maverick (17Bx128E, 400B total) |
| **发布日期** | 2026-01-14 (Zenodo), 2025-04-05 (模型发布) |
| **核心参数** | MoE；Scout: 10M context, ~40T tokens；Maverick: 1M context, ~22T tokens；Bfloat16 / FP8 / int4 量化 |
| **主要创新点** | early-fusion 原生多模态（文本+图像从预训练开始融合）；iRoPE 长上下文长度泛化；MoE with routed/shared experts；post-training: lightweight SFT → online RL → lightweight DPO |
| **arXiv** | 已撤回（原 arXiv:2601.11659）；完整版见 Zenodo: https://doi.org/10.5281/zenodo.18246522 |

## 4. Google DeepMind — Gemini 3.1 Pro

| 字段 | 内容 |
|------|------|
| **英文标题** | Gemini 3.1 Pro Model Card |
| **发布机构** | Google DeepMind |
| **模型名称** | Gemini 3.1 Pro |
| **发布日期** | 2026-02-19 |
| **核心参数** | 原生多模态（text, audio, images, video, code repositories）；Deep Think mode |
| **主要创新点** | 多模态推理模型显著优于 Gemini 3 Pro；Deep Think 模式在 IMO、ICPC 等竞赛中达到金牌水平；在数学、物理、计算机科学领域辅助研究 |
| **链接** | https://deepmind.google/models/model-cards/gemini-3-1-pro/ |

> 另见：Gemini Robotics-ER 1.6（2026-04-20）— 基于 Gemini 3.0 Flash 的具身推理 VLM；Gemini Embedding 2（2026-05）— 原生多模态 embedding 模型。

## 5. Anthropic — Claude Sonnet 5 / Opus 4.8 / Mythos Preview

### Claude Sonnet 5

| 字段 | 内容 |
|------|------|
| **英文标题** | Claude Sonnet 5 System Card |
| **发布机构** | Anthropic |
| **发布日期** | 2026-06-30 |
| **主要创新点** | Sonnet 系列最强；coding, agentic search, multimodal reasoning 全面超越 Sonnet 4.6；near-Opus intelligence at Sonnet pricing |
| **链接** | https://www.anthropic.com/claude-sonnet-5-system-card |

### Claude Opus 4.8

| 字段 | 内容 |
|------|------|
| **发布日期** | 2026-05-28 |
| **主要创新点** | 通用访问中最强模型；编码、agentic tool use、知识工作全面提升；4 生物风险评估安全 |
| **链接** | https://www.anthropic.com/system-cards |

### Claude Mythos Preview

| 字段 | 内容 |
|------|------|
| **发布日期** | 2026-04-07 |
| **主要创新点** | Anthropic 迄今最强前沿模型，大幅跨越能力阈值；因极强能力未公开发布，仅限防御性网络安全合作；首个在 RSP v3.0 框架下评估的模型 |
| **链接** | https://www.anthropic.com/system-cards |

## 6. Mistral AI — Mistral Large 3 / Ministral 3 / Magistral

### Mistral Large 3

| 字段 | 内容 |
|------|------|
| **英文标题** | Mistral Large 3 |
| **发布机构** | Mistral AI |
| **模型名称** | Mistral Large 3 (675B total, 41B active) |
| **发布日期** | 2025-12-02 |
| **核心参数** | MoE；256K context；8×H200 训练；FP8 量化；Apache 2.0 |
| **主要创新点** | Mistral 首个 MoE 模型（自 Mixtral 以来）；原生多模态（+2.5B vision encoder）；multilingual 支持数十种语言；Eagle speculative decoding |
| **链接** | https://mistral.ai/news/mistral-3/ |

### Ministral 3

| 字段 | 内容 |
|------|------|
| **英文标题** | Ministral 3 |
| **模型名称** | Ministral 3 (3B, 8B, 14B) — each with base/instruct/reasoning 变体 |
| **发布日期** | 2026-01-13 |
| **核心参数** | Dense; 131K tokens 训练 / 256K tokens 最大上下文；Apache 2.0 |
| **主要创新点** | Cascade Distillation（迭代剪枝+持续训练+蒸馏）；发现 capacity gap 现象（教师过强不一定对学生有利）；支持 vision |
| **arXiv** | https://arxiv.org/abs/2601.08584 |

### Magistral

| 字段 | 内容 |
|------|------|
| **英文标题** | Magistral |
| **发布机构** | Mistral AI |
| **模型名称** | Magistral Medium / Magistral Small |
| **发布日期** | 2025-06-12 |
| **主要创新点** | Mistral 首个 reasoning 模型；纯 RL 训练（无蒸馏）；RL on text 保持多模态/指令遵循/函数调用能力 |
| **arXiv** | https://arxiv.org/abs/2506.10910 |

## 7. Alibaba Qwen — Qwen3 / Qwen3.5-Omni

### Qwen3

| 字段 | 内容 |
|------|------|
| **中文标题** | Qwen3 技术报告 |
| **英文标题** | Qwen3 Technical Report |
| **发布机构** | Alibaba Qwen Team |
| **模型名称** | Qwen3 系列 (0.6B ~ 235B-A22B MoE) |
| **发布日期** | 2025-05-14 |
| **核心参数** | Dense + MoE 混合；235B total / 22B active（MoE 旗舰）；36T tokens pre-training；119 语言支持 |
| **主要创新点** | thinking + non-thinking 统一框架（动态切换）；thinking budget 机制（用户控制推理计算量）；多语言从 29→119 种 |
| **arXiv** | https://arxiv.org/abs/2505.09388 |

### Qwen3.5-Omni

| 字段 | 内容 |
|------|------|
| **英文标题** | Qwen3.5-Omni Technical Report |
| **发布机构** | Alibaba Qwen Team |
| **模型名称** | Qwen3.5-Omni (Plus / Flash) |
| **发布日期** | 2026-04-17 |
| **核心参数** | Hybrid Attention MoE；256K context；100M+ hours audio-visual 训练；hundreds of billions 参数 |
| **主要创新点** | ARIA (Adaptive Rate Interleave Alignment) 实现自然流畅的流式语音合成；10h+ 音频 + 400s 720P 视频理解；全模态 agent（自动 WebSearch, FunctionCall, 语音输出, 实时流式交互）|
| **arXiv** | https://arxiv.org/abs/2604.15804 |

## 8. Microsoft — Phi-4-reasoning-vision

| 字段 | 内容 |
|------|------|
| **英文标题** | Phi-4-reasoning-vision-15B Technical Report |
| **发布机构** | Microsoft Research |
| **模型名称** | Phi-4-reasoning-vision-15B |
| **发布日期** | 2026-03-04 |
| **核心参数** | 15B 参数；混合推理/非推理模式（explicit mode tokens）；动态分辨率视觉编码器 |
| **主要创新点** | 小模型多模态推理的实践指南；合成数据 augmentation 驱动质量提升；high-resolution + dynamic-resolution encoder 系统消融；scientific/mathematical reasoning + UI understanding |
| **arXiv** | https://arxiv.org/abs/2603.03975 |

## 9. Apple — Apple Foundation Models 三代

| 字段 | 内容 |
|------|------|
| **英文标题** | Introducing the Third Generation of Apple's Foundation Models |
| **发布机构** | Apple |
| **模型名称** | AFM 3 Core (~3B dense)；AFM 3 Core Advanced (20B sparse, 1-4B activated)；AFM 3 Cloud；ADM 3 Cloud (Image)；AFM 3 Cloud Pro |
| **发布日期** | 2026-06-08 (WWDC 宣布) |
| **核心参数** | 与 Google 合作定制；Private Cloud Compute；sparse architecture for on-device |
| **主要创新点** | 第三代 AFM 家族共 5 个模型；PT-MoE (Parallel-Track Mixture-of-Experts) 升级版；全新 Siri、高级照片编辑等 |
| **2025 版 arXiv** | https://arxiv.org/abs/2507.13575 |

## 10. NVIDIA — Nemotron 3 Ultra / Nemotron-Labs-Diffusion

### Nemotron 3 Ultra

| 字段 | 内容 |
|------|------|
| **英文标题** | Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning |
| **发布机构** | NVIDIA |
| **模型名称** | Nemotron 3 Ultra (550B-A55B) |
| **发布日期** | 2026-06-09 |
| **核心参数** | MoE Hybrid Mamba-Attention；20T tokens (NVFP4)；1M context；LatentMoE；MTP |
| **主要创新点** | Hybrid Mamba-Attention 实现 ~6× throughput 对比同类模型；LatentMoE（优于标准 Granular MoE）；NVFP4 低精度预训练；agent-focused post-training |
| **链接** | https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf |

### Nemotron-Labs-Diffusion

| 字段 | 内容 |
|------|------|
| **英文标题** | Nemotron-Labs-Diffusion: A Tri-Mode Language Model Unifying Autoregressive, Diffusion, and Self-Speculation Decoding |
| **发布机构** | NVIDIA |
| **模型名称** | Nemotron-Labs-Diffusion (3B, 8B, 14B) |
| **发布日期** | 2026-05-19 |
| **核心参数** | 1.3T tokens pre-training + 45B tokens post-training |
| **主要创新点** | 统一 AR + diffusion + self-speculation 三种模式；joint AR-diffusion 训练目标；diffusion draft + AR verify 优于 MTP；8B 模型解码 5.9× 更多 tokens/forward 优于 Qwen3-8B |
| **链接** | HuggingFace collection: https://huggingface.co/collections/nvidia/nemotron-labs-diffusion |

## 11. xAI — Grok 4.3

| 字段 | 内容 |
|------|------|
| **英文标题** | Grok 4.3 |
| **发布机构** | xAI |
| **模型名称** | Grok 4.3 |
| **发布日期** | 2026-04-30 |
| **核心参数** | 1M context；reasoning effort (none/low/medium/high) 可配置；text+image input |
| **主要创新点** | 最低幻觉率（Artificial Analysis Omniscience #1）；configurable reasoning；agentic tool calling 领先；Mantle 推理引擎 |
| **链接** | https://docs.x.ai/developers/models/grok-4.3 |

## 12. Amazon — Amazon Nova Premier

| 字段 | 内容 |
|------|------|
| **英文标题** | Amazon Nova Premier: Technical Report and Model Card |
| **发布机构** | Amazon AGI |
| **模型名称** | Amazon Nova Premier |
| **发布日期** | 2025-04-30 |
| **核心参数** | 1M context；多模态（text, images, video）；可作为 teacher 进行 distillation |
| **主要创新点** | Amazon Nova 家族最强大模型；1M token 长上下文支持；为 Nova Pro/Lite/Micro 定制化提供 teacher |
| **arXiv** | https://arxiv.org/abs/2506.12103 |

## 13. Zhipu AI — GLM-5

| 字段 | 内容 |
|------|------|
| **中文标题** | GLM-5：从 Vibe Coding 到 Agentic Engineering |
| **英文标题** | GLM-5: from Vibe Coding to Agentic Engineering |
| **发布机构** | Zhipu AI & Tsinghua University |
| **模型名称** | GLM-5 |
| **发布日期** | 2026-02-17 |
| **核心参数** | MoE with DSA (DeepSeek Sparse Attention)；27T tokens pre-training；200K context（4K→200K mid-training 扩展） |
| **主要创新点** | DSA 稀疏注意力降低成本；异步 RL 基础设施（解耦生成与训练，大幅提升 GPU 利用率）；异步 Agent RL 算法（long-horizon interaction）；全栈支持国产 GPU 芯片（华为昇腾、摩尔线程等 7 个平台）|
| **arXiv** | https://arxiv.org/abs/2602.15763 |

## 14. Shanghai AI Lab — Intern-S1-Pro

| 字段 | 内容 |
|------|------|
| **英文标题** | Intern-S1-Pro: Scientific Multimodal Foundation Model at Trillion Scale |
| **发布机构** | Shanghai AI Laboratory |
| **模型名称** | Intern-S1-Pro (1T 参数) |
| **发布日期** | 2026-03-26 |
| **核心参数** | 首个万亿参数科学多模态基础模型；100+ 科学任务（化学、材料、生命科学、地球科学）|
| **主要创新点** | Grouped Routing 扩展专家策略；XTuner + LMDeploy 支撑万亿级 RL 训练；Specializable Generalist 范式：通用与科学专业能力融合 |
| **arXiv** | https://arxiv.org/abs/2603.25040 |

> 前序工作：Intern-S1 (241B total / 28B activated; 2025-08-21; arXiv:2508.15763)

## 15. Moonshot AI — Kimi K2 / K2.5

### Kimi K2

| 字段 | 内容 |
|------|------|
| **英文标题** | Kimi K2: Open Agentic Intelligence |
| **发布机构** | Moonshot AI |
| **模型名称** | Kimi K2 (1T total / 32B activated) |
| **发布日期** | 2025-07-28 |
| **核心参数** | MoE；15.5T tokens；MuonClip optimizer；256K context |
| **主要创新点** | MuonClip（Muon + QK-clip 稳定训练，zero loss spike）；大规模 agentic data synthesis pipeline；joint RL stage（实 + 合成环境交互）；open-source 非 thinking 模型 SOTA 在 agentic 任务 |
| **arXiv** | https://arxiv.org/abs/2507.20534 |

### Kimi K2.5

| 字段 | 内容 |
|------|------|
| **英文标题** | Kimi K2.5: Visual Agentic Intelligence |
| **发布机构** | Moonshot AI |
| **模型名称** | Kimi K2.5 (1T total / 32B activated) |
| **发布日期** | 2026-02-02 |
| **核心参数** | MLA attention; MoonViT (400M vision encoder); 256K context; 160K vocabulary |
| **主要创新点** | joint text-vision pre-training + zero-vision SFT + joint text-vision RL；Agent Swarm（自编配并行 agent 编排，延迟降低 4.5×）；instant + thinking mode 双模式 |
| **arXiv** | https://arxiv.org/abs/2602.02276 |

## 16. ByteDance — Seed1.8

| 字段 | 内容 |
|------|------|
| **英文标题** | Seed1.8 Model Card: Towards Generalized Real-World Agency |
| **发布机构** | ByteDance Seed |
| **模型名称** | Seed1.8 |
| **发布日期** | 2026-03-21 |
| **主要创新点** | generalized real-world agency（tool use, environment feedback, multi-step execution）；search + code generation/execution + GUI interaction 统一 agentic interface；configurable thinking modes；optimized visual encoding |
| **arXiv** | https://arxiv.org/abs/2603.20633 |

> 前序：Seed1.5-VL (532M vision encoder + 20B active MoE LLM; 2025-05-11; arXiv:2505.07062)

## 17. StepFun — Step 3.5 Flash / Step-3

### Step 3.5 Flash

| 字段 | 内容 |
|------|------|
| **中文标题** | Step 3.5 Flash：110 亿活跃参数开放前沿智能 |
| **英文标题** | Step 3.5 Flash: Open Frontier-Level Intelligence with 11B Active Parameters |
| **发布机构** | StepFun (阶跃星辰) |
| **模型名称** | Step 3.5 Flash (196B total / 11B active) |
| **发布日期** | 2026-02-17 |
| **核心参数** | MoE；3:1 Sliding Window/Full Attention；MTP-3；~170 tokens/s on Hopper GPUs |
| **主要创新点** | 极低活跃参数实现前沿能力；RL 框架融合 verifiable signals + preference feedback；IMO-AnswerBench 85.4%, LiveCodeBench-v6 86.4%, Tau2-Bench 88.2% |
| **arXiv** | https://arxiv.org/abs/2602.10604 |

### Step-3

| 字段 | 内容 |
|------|------|
| **英文标题** | Step-3 is Large yet Affordable: Model-system Co-design for Cost-effective Decoding |
| **发布机构** | StepFun (阶跃星辰) |
| **模型名称** | Step-3 (321B total / 38B active) |
| **发布日期** | 2025-07-25 |
| **核心参数** | MoE + MFA (Multi-Matrix Factorization Attention) |
| **主要创新点** | Multi-Matrix Factorization Attention (MFA) 大幅降低 KV cache 和计算量；Attention-FFN Disaggregation (AFD) 解耦推理系统；decoding throughput 4039 tokens/s/GPU (50ms TPOT, FP8)，超越 DeepSeek-V3 (2324) |
| **arXiv** | https://arxiv.org/abs/2507.19427 |

## 18. Baichuan — Baichuan-M3/M4

| 字段 | 内容 |
|------|------|
| **英文标题** | Baichuan-M3: Modeling Clinical Inquiry for Reliable Medical Decision-Making |
| **发布机构** | Baichuan Inc. |
| **模型名称** | Baichuan-M3 |
| **发布日期** | 2026-02-06 |
| **核心参数** | 医疗增强 LLM |
| **主要创新点** | 从被动 QA 转向主动临床决策支持；proactive information acquisition + long-horizon reasoning + adaptive hallucination suppression；HealthBench SOTA |
| **arXiv** | https://arxiv.org/abs/2602.06570 |

> 前序：Baichuan-M1 (14B, 20T tokens, from-scratch 医疗训练; 2025-02; arXiv:2502.12671)；Baichuan-M2 (32B, 大型 verifier RL 系统; 2025-09; arXiv:2509.02208)；Baichuan-M4 (2026-06; 临床级 medical agent system; arXiv:2606.08982)

## 19. 01.AI — Yi-Lightning

| 字段 | 内容 |
|------|------|
| **英文标题** | Yi-Lightning Technical Report |
| **发布机构** | 01.AI |
| **模型名称** | Yi-Lightning (MoE) |
| **发布日期** | 2024-12-02 |
| **主要创新点** | Chatbot Arena 第6名（中文/数学/编程/Hard Prompts 第2-4名）；增强型 MoE 路由 + KV-cache 优化；RAISE 安全框架四组件 |
| **arXiv** | https://arxiv.org/abs/2412.01253 |

> ⚠️ 注：01.AI 自 2024 年底后发布节奏显著放缓，已被 DeepSeek、Qwen、Kimi、GLM 等超越。

---

## 关键趋势总结

### 架构趋势
- **MoE 成为标配**：几乎所有前沿模型（DeepSeek-V4, Llama 4, Qwen3, Mistral Large 3, GLM-5, Kimi K2, Step 3.5 Flash）均采用 MoE 架构
- **混合注意力兴起**：DeepSeek-V4 (CSA+HCA)、NVIDIA Nemotron 3 (Mamba-Attention)、Step 3.5 Flash (Sliding Window/Full Attention) 探索稀疏/混合注意力降低长上下文成本
- **扩散模型进入语言模型**：NVIDIA Nemotron-Labs-Diffusion 开创 AR + Diffusion + Self-Speculation 三模统一框架
- **多模态成为基线**：几乎所有新模型都原生支持文本+图像，部分支持音频和视频

### 训练方法趋势
- **纯 RL 训练 reasoning**：Mistral Magistral、DeepSeek-V4、GLM-5 均强调 RL 在 post-training 中的核心作用
- **Agentic RL 新范式**：GLM-5 异步 Agent RL、Kimi K2 joint RL stage、Step 3.5 Flash agent-focused RL 成为新方向
- **Data quality > scale**：Microsoft Phi-4、Ministral 3 Cascade Distillation 强调数据质量和过滤的重要性

### 推理 / Reasoning 趋势
- **Thinking + Non-Thinking 统一**：Qwen3、Phi-4-reasoning-vision、GPT-5 均在一个模型中融合两种模式
- **Configurable reasoning effort**：GPT-5.6 (Sol/Terra/Luna)、Grok 4.3 (none/low/medium/high)、Step models 支持推理深度调节
- **Test-time compute scaling**：DeepSeek-V4-Pro-Max、GPT-5-thinking-pro、Kimi K2.5 thinking mode 持续扩展推理时计算

### 长上下文趋势
- **1M context 成为旗舰标配**：DeepSeek-V4, Grok 4.3, Amazon Nova Premier, Llama 4 Scout (10M)
- **百万级上下文变得高效**：DeepSeek-V4 通过 CSA+HCA 实现 73% FLOPs 降低

### 安全趋势
- **System Card 标准化**：OpenAI、Anthropic、xAI 均发布详细 System Card
- **能力阈值评估**：Anthropic Mythos Preview 因能力过强未公开发布；OpenAI Preparedness Framework 持续升级
