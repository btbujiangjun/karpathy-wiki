---
title: 大模型技术报告摘要 — LLM Tech Report Digest (2026-07-07 综合版，22家机构全面覆盖)
type: synthesis
created: 2026-07-07
updated: 2026-07-07
sources: [web-search]
tags: [tech-report, llm, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, zhipu, internlm, moonshot, bytedance, stepfun, baichuan, yi]
---

# 大模型技术报告摘要 — LLM Tech Report Digest

> 2026-07-07 全面更新版。覆盖 22 家 AI 机构，重点聚焦近期正式发布的 Tech Report / System Card / Model Card。
> 本版亮点：DeepSeek-V4（arXiv 正式版）、Seed 2.0（首份 arXiv Model Card）、Claude Opus 4.8 System Card、Nemotron 3 Super Technical Report、GLM-5 Technical Report、Kimi K2.5、Step 3.5 Flash。

---

## 目录

1. [DeepSeek — DeepSeek-V4](#1-deepseek--deepseek-v4)
2. [OpenAI — GPT-5 / GPT-5.5 / o1](#2-openai--gpt-5--gpt-55--o1)
3. [Meta AI — Llama 4](#3-meta-ai--llama-4)
4. [Google DeepMind — Gemini 2.5](#4-google-deepmind--gemini-25)
5. [Anthropic — Claude Opus 4.8 / Mythos / Sonnet 5](#5-anthropic--claude-opus-48--mythos--sonnet-5)
6. [Mistral AI — Ministral 3 / Magistral](#6-mistral-ai--ministral-3--magistral)
7. [Qwen (Alibaba) — Qwen3 / Qwen3.5-Omni / Qwen3-Coder-Next / Qwen-VLA](#7-qwen-alibaba--qwen3--qwen35-omni--qwen3-coder-next--qwen-vla)
8. [Yi (01.AI) — Yi-Lightning](#8-yi-01ai--yi-lightning)
9. [Baichuan — Baichuan-M3 / M4 / Omni-1.5](#9-baichuan--baichuan-m3--m4--omni-15)
10. [Microsoft — Phi-4-reasoning / Phi-4-reasoning-vision](#10-microsoft--phi-4-reasoning--phi-4-reasoning-vision)
11. [Apple — Apple Intelligence Foundation Language Models (2025)](#11-apple--apple-intelligence-foundation-language-models-2025)
12. [NVIDIA — Nemotron 3 (Nano / Super / Ultra)](#12-nvidia--nemotron-3-nano--super--ultra)
13. [xAI (Grok) — Grok 4 / 4.1 / 4.20](#13-xai-grok--grok-4--41--420)
14. [Amazon — Amazon Nova Family](#14-amazon--amazon-nova-family)
15. [Zhipu AI (GLM) — GLM-5](#15-zhipu-ai-glm--glm-5)
16. [InternLM (Shanghai AI Lab) — Intern-S1-Pro](#16-internlm-shanghai-ai-lab--intern-s1-pro)
17. [Moonshot AI (Kimi) — Kimi K2 / K2.5](#17-moonshot-ai-kimi--kimi-k2--k25)
18. [StepFun (阶跃星辰) — Step 3.5 Flash / STEP3-VL](#18-stepfun-阶跃星辰--step-35-flash--step3-vl)
19. [ByteDance (Seed/Doubao) — Seed 2.0 / Seed 1.8](#19-bytedance-seeddoubao--seed-20--seed-18)
20. [Others — MiniMax / EXAONE / Ling & Ring 2.6](#20-others--minimax--exaone--ling--ring-26)

---

## 1. DeepSeek — DeepSeek-V4

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V4：迈向高效百万 Token 上下文智能 |
| **英文标题** | DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence |
| **发布机构** | DeepSeek-AI |
| **模型系列** | DeepSeek-V4-Pro / DeepSeek-V4-Flash |
| **发布日期** | 2026-04-26 |
| **arXiv** | [2606.19348](https://arxiv.org/abs/2606.19348) |
| **总参数量** | V4-Pro: 1.6T (49B activated); V4-Flash: 284B (13B activated) |
| **架构** | MoE (Mixture-of-Experts) |
| **上下文长度** | 1M tokens |
| **训练数据** | 32T+ tokens |
| **主要创新** | ① **混合注意力架构**：Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA)，1M 上下文下推理 FLOPs 仅 V3.2 的 27%，KV Cache 仅 10%；② **Manifold-Constrained Hyper-Connections (mHC)**：增强残差连接；③ **Muon 优化器**：更快收敛与训练稳定性；④ **两阶段后训练**：独立领域专家 SFT/RL + on-policy 蒸馏整合；⑤ **三档推理模式**：Non-think / Think High / Think Max |
| **精度** | FP4 (MoE expert) + FP8 (其他参数) 混合精度 |

---

## 2. OpenAI — GPT-5 / GPT-5.5 / o1

### GPT-5 System Card

| 项目 | 内容 |
|------|------|
| **英文标题** | GPT-5 System Card |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5 (unified smart + fast + deep reasoning) |
| **发布日期** | 2025-08 |
| **arXiv** | [2601.03267](https://arxiv.org/abs/2601.03267) |
| **主要创新** | 统一系统，智能模型 + 深度推理模型；安全评估、外部红队测试全面覆盖 |
| **引用量** | 667+ (截至 2026) |

### GPT-5.5 System Card

| 项目 | 内容 |
|------|------|
| **英文标题** | GPT-5.5 System Card |
| **发布机构** | OpenAI |
| **发布日期** | 2026-04-23 |
| **主要创新** | 面向复杂真实工作（编程、在线研究、信息分析）；增强 agent 能力 |
| **链接** | [deploymentsafety.openai.com](https://deploymentsafety.openai.com/gpt-5-5) |

### OpenAI o1 System Card

| 项目 | 内容 |
|------|------|
| **英文标题** | OpenAI o1 System Card |
| **发布机构** | OpenAI |
| **发布日期** | 2024-12-21 |
| **arXiv** | [2412.16720](https://arxiv.org/abs/2412.16720) |
| **引用量** | 2293+ |

---

## 3. Meta AI — Llama 4

| 项目 | 内容 |
|------|------|
| **英文标题** | The Llama 4 Herd: Architecture, Training, Evaluation, and Deployment Notes |
| **发布机构** | Meta AI |
| **模型系列** | Llama 4 Scout / Maverick / Behemoth (teacher) |
| **发布日期** | 2026-01-15 (已撤回) |
| **arXiv** | [2601.11659](https://arxiv.org/abs/2601.11659) (withdrawn) |
| **架构** | MoE, early-fusion 多模态 |
| **主要创新** | Scout: 10M context (iRoPE); Maverick: 128专家 MoE; Behemoth: 2T teacher; 轻量 SFT + online RL + 轻量 DPO 后训练 |
| **备注** | 该论文为社区整理的公开信息聚合，非 Meta 官方技术报告。Meta 官方 Llama 4 博客：[ai.meta.com](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) |

---

## 4. Google DeepMind — Gemini 2.5

| 项目 | 内容 |
|------|------|
| **英文标题** | Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 2.5 Pro / Gemini 2.5 Flash / Gemini 2.0 Flash |
| **发布日期** | 2025-07-07 |
| **arXiv** | [2507.06261](https://arxiv.org/abs/2507.06261) |
| **引用量** | 3329+ |
| **上下文长度** | 支持最长 3 小时视频处理 |
| **核心能力** | 思考型模型（thinking model）；多模态理解（文本、音频、图像、视频）；长上下文；agentic 能力 |
| **下载** | [storage.googleapis.com](https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf) |

---

## 5. Anthropic — Claude Opus 4.8 / Mythos / Sonnet 5

### Claude Opus 4.8 System Card

| 项目 | 内容 |
|------|------|
| **英文标题** | Claude Opus 4.8 System Card |
| **发布机构** | Anthropic |
| **模型系列** | Claude Opus 4.8 |
| **发布日期** | 2026-05-28 (更新: 2026-06-17) |
| **链接** | [System Card PDF](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf) |
| **上下文长度** | 1M tokens |
| **核心能力** | Opus 4.7 的升级版，软件工程、agentic tool use、知识工作全面提升；Anthropic 最强通用模型 |
| **安全评估** | RSP 评估（化生武器、AI R&D、高风险 misalignment）；网络安防评估；对齐评估（欺骗/过度拒绝显著降低） |
| **主要发现** | Opus 4.8 在对齐指标上达到新高，支持用户自主性；misaligned 行为率大幅低于 Opus 4.7 |

### Claude Mythos Preview System Card

| 项目 | 内容 |
|------|------|
| **发布日期** | 2026-04-08 |
| **链接** | [System Card PDF](https://www-cdn.anthropic.com/08ab9158070959f88f296514c21b7facce6f52bc.pdf) |

### Claude Sonnet 5 System Card

| 项目 | 内容 |
|------|------|
| **发布日期** | 2026 |
| **链接** | [System Card PDF](https://www-cdn.anthropic.com/480e0bb54327b9622282e9c39a83a4f490ed377e/Claude%20Sonnet%205%20System%20Card.pdf) |
| **所有模型卡片** | [anthropic.com/system-cards](https://www.anthropic.com/system-cards) |

---

## 6. Mistral AI — Ministral 3 / Magistral

### Ministral 3

| 项目 | 内容 |
|------|------|
| **英文标题** | Ministral 3 Technical Report |
| **发布机构** | Mistral AI |
| **模型系列** | Ministral 3 |
| **发布日期** | 2026-01-13 |
| **arXiv** | [2601.08584](https://arxiv.org/abs/2601.08584) |
| **特点** | 高效小型语言模型 |

### Magistral

| 项目 | 内容 |
|------|------|
| **英文标题** | Magistral |
| **发布机构** | Mistral AI |
| **发布日期** | 2025-06-12 |
| **arXiv** | [2506.10910](https://arxiv.org/abs/2506.10910) |
| **特点** | Mistral 的新一代架构 |

---

## 7. Qwen (Alibaba) — Qwen3 / Qwen3.5-Omni / Qwen3-Coder-Next / Qwen-VLA

### Qwen3 Technical Report

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3 技术报告 |
| **英文标题** | Qwen3 Technical Report |
| **发布机构** | Alibaba Cloud / Qwen Team |
| **模型系列** | Qwen3 (0.6B ~ 235B) |
| **发布日期** | 2025-05-14 |
| **arXiv** | [2505.09388](https://arxiv.org/abs/2505.09388) |
| **架构** | Dense + MoE (Qwen3-235B-A22B: 235B total, 22B activated, 128 experts, 8 activated) |
| **上下文长度** | 32K tokens |
| **主要创新** | ① 统一 thinking + non-thinking 模式，动态切换；② Thinking budget 推理预算机制；③ 从 29 语言扩展到 119 语言/方言 |
| **许可** | Apache 2.0 |

### Qwen3.5-Omni Technical Report

| 项目 | 内容 |
|------|------|
| **英文标题** | Qwen3.5-Omni Technical Report |
| **发布日期** | 2026-04 |
| **arXiv** | [2604.15804](https://arxiv.org/abs/2604.15804) |

### Qwen3-Coder-Next Technical Report

| 项目 | 内容 |
|------|------|
| **英文标题** | Qwen3-Coder-Next Technical Report |
| **arXiv** | [2603.00729](https://arxiv.org/abs/2603.00729) |
| **参数量** | 80B total, 3B active (MoE) |
| **主要创新** | 代理编程专用；MegaFlow 大规模并行执行系统；SWE 基准 SOTA |

### Qwen-VLA Technical Report

| 项目 | 内容 |
|------|------|
| **英文标题** | Qwen-VLA: Unifying Vision-Language-Action Modeling |
| **发布日期** | 2026-05-28 |
| **arXiv** | [2605.30280](https://arxiv.org/abs/2605.30280) |
| **基础模型** | Qwen3.5-4B |
| **主要创新** | DiT-based flow-matching action decoder；统一操控/导航/轨迹预测；本体感知 prompt conditioning |

---

## 8. Yi (01.AI) — Yi-Lightning

| 项目 | 内容 |
|------|------|
| **中文标题** | Yi-Lightning 技术报告 |
| **英文标题** | Yi-Lightning Technical Report |
| **发布机构** | 01.AI |
| **模型系列** | Yi-Lightning |
| **发布日期** | 2024-12-02 |
| **arXiv** | [2412.01253](https://arxiv.org/abs/2412.01253) |
| **核心表现** | Chatbot Arena 总排名第 6；采用数据工程驱动的训练方法 |

---

## 9. Baichuan — Baichuan-M3 / M4 / Omni-1.5

### Baichuan-M3

| 项目 | 内容 |
|------|------|
| **英文标题** | Baichuan-M3: Modeling Clinical Inquiry for Reliable Medical Decision-Making |
| **发布机构** | Baichuan Intelligence |
| **发布日期** | 2026-02-06 |
| **arXiv** | [2602.06570](https://arxiv.org/abs/2602.06570) |
| **领域** | 医疗决策支持 |

### Baichuan-M4

| 项目 | 内容 |
|------|------|
| **英文标题** | Baichuan-M4: A Clinical-Grade Medical Agent System for Continuous Care |
| **发布日期** | 2026-06 |
| **arXiv** | [2606.08982](https://arxiv.org/abs/2606.08982) |
| **特点** | 临床级医疗大模型，医师监督式连续照护 |

### Baichuan-Omni-1.5 Technical Report

| 项目 | 内容 |
|------|------|
| **英文标题** | Baichuan-Omni-1.5 Technical Report |
| **发布日期** | 2025-01-26 |
| **arXiv** | [2501.15368](https://arxiv.org/abs/2501.15368) |
| **特点** | 全模态模型（文本+音频+视觉）；自研 Baichuan-Audio-Tokenizer；500B 高质量多模态数据；多阶段训练策略 |

---

## 10. Microsoft — Phi-4-reasoning / Phi-4-reasoning-vision

### Phi-4-reasoning Technical Report

| 项目 | 内容 |
|------|------|
| **英文标题** | Phi-4-reasoning Technical Report |
| **发布机构** | Microsoft Research |
| **发布日期** | 2025-04-30 |
| **arXiv** | [2504.21318](https://arxiv.org/abs/2504.21318) |

### Phi-4-reasoning-vision-15B Technical Report

| 项目 | 内容 |
|------|------|
| **英文标题** | Phi-4-reasoning-vision-15B Technical Report |
| **发布机构** | Microsoft Research |
| **发布日期** | 2026-03-04 |
| **arXiv** | [2603.03975](https://arxiv.org/abs/2603.03975) |
| **参数量** | 15B |
| **主要创新** | 紧凑型开源多模态推理模型；高分辨率动态分辨率编码器；推理/非推理数据混合 + 显式模式 token；系统过滤、纠错、合成增强 |

---

## 11. Apple — Apple Intelligence Foundation Language Models (2025)

| 项目 | 内容 |
|------|------|
| **英文标题** | Apple Intelligence Foundation Language Models: Tech Report 2025 |
| **发布机构** | Apple |
| **模型系列** | On-Device (~3B) + Server Foundation Models |
| **发布日期** | 2025-07-17 |
| **arXiv** | [2507.13575](https://arxiv.org/abs/2507.13575) |
| **引用量** | 14+ |
| **特点** | 多语言、多模态；针对 Apple Silicon 架构优化；低延迟设备端推理 |

---

## 12. NVIDIA — Nemotron 3 (Nano / Super / Ultra)

### Nemotron 3 总览

| 项目 | 内容 |
|------|------|
| **英文标题** | NVIDIA Nemotron 3: Efficient and Open Intelligence |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3 Nano / Super / Ultra |
| **发布日期** | 2025-12-24 (白皮书); 2026-04 (Super/Ultra 技术报告) |
| **arXiv (白皮书)** | [2512.20856](https://arxiv.org/abs/2512.20856) |

### Nemotron 3 Super Technical Report

| 项目 | 内容 |
|------|------|
| **英文标题** | Nemotron 3 Super: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning |
| **发布日期** | 2026-04-03 |
| **arXiv** | [2604.12374](https://arxiv.org/abs/2604.12374) |
| **参数量** | 120B total, 12B active |
| **架构** | MoE Hybrid Mamba-Transformer |
| **上下文长度** | 1M tokens |
| **主要创新** | ① LatentMoE：新型 MoE 提升质量；② NVFP4 预训练（GB300 上相比 FP8 提升 3× 吞吐）；③ MTP (Multi-Token Prediction) 层加速生成长文本；④ 多环境 RL 训练（推理预算控制、多步工具调用）；⑤ 无 RoPE（Mamba 提供隐式位置信息） |

### Nemotron 3 Ultra

| 项目 | 内容 |
|------|------|
| **参数量** | 最大模型，含 LatentMoE + NVFP4 + MTP |
| **特点** | 最高精度与推理性能 |

---

## 13. xAI (Grok) — Grok 4 / 4.1 / 4.20

### Grok 4 Model Card

| 项目 | 内容 |
|------|------|
| **英文标题** | Grok 4 Model Card |
| **发布机构** | xAI |
| **发布日期** | 2025-08-20 |
| **链接** | [data.x.ai](https://data.x.ai/2025-08-20-grok-4-model-card.pdf) |
| **特点** | 推理模型，高级 tool-use 能力，SOTA 推理 |

### Grok 4.1 Model Card

| 项目 | 内容 |
|------|------|
| **发布日期** | 2025-11-17 |
| **链接** | [data.x.ai](https://data.x.ai/2025-11-17-grok-4-1-model-card.pdf) |
| **特点** | 更自然、流畅的对话，保持核心推理 |

### Grok 4.20 System Card

| 项目 | 内容 |
|------|------|
| **发布日期** | 2026-04-07 |
| **链接** | [data.x.ai](https://data.x.ai/2026-04-07-grok-4-20-model-card.pdf) |

### Grok Code Fast 1

| 项目 | 内容 |
|------|------|
| **发布日期** | 2025-08-26 |
| **链接** | [data.x.ai](https://data.x.ai/2025-08-26-grok-code-fast-1-model-card.pdf) |
| **特点** | 编程专用推理模型，agentic harness 中高效运行 |

---

## 14. Amazon — Amazon Nova Family

| 项目 | 内容 |
|------|------|
| **英文标题** | The Amazon Nova Family of Models: Technical Report and Model Card |
| **发布机构** | Amazon AGI |
| **模型系列** | Amazon Nova Pro / Lite / Micro / Canvas / Reel |
| **发布日期** | 2025-03-17 |
| **arXiv** | [2506.12103](https://arxiv.org/abs/2506.12103) |
| **引用量** | 58+ |
| **核心能力** | Pro: 最强多模态；Lite: 低延迟低成本多模态；Micro: 最低延迟纯文本；Canvas: 图像生成；Reel: 视频生成 |
| **覆盖评估** | 核心能力、agentic 性能、长上下文、功能适配、运行性能、人工评估 |

---

## 15. Zhipu AI (GLM) — GLM-5

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5：从 Vibe Coding 到 Agentic Engineering |
| **英文标题** | GLM-5: from Vibe Coding to Agentic Engineering |
| **发布机构** | Zhipu AI (智谱 AI) |
| **模型系列** | GLM-5 / GLM-5-FP8 |
| **发布日期** | 2026-02-17 |
| **arXiv** | [2602.15763](https://arxiv.org/abs/2602.15763) |
| **参数量** | 744B total, 40B active (MoE, 256 专家, 80 层) |
| **训练数据** | 28.5T tokens (GLM-4.5 为 23T) |
| **架构** | MoE + DSA (DeepSeek Sparse Attention) + MLA-256 变体 |
| **主要创新** | ① **DSA 稀疏注意力**：大幅降低训练/推理成本，保持长上下文保真度；② **异步 RL 基础设施**：decouple 生成与训练，大幅提升后训练效率；③ **异步 Agent RL 算法**：从复杂长程交互中学习；④ **DP-aware routing**：多轮 agentic 工作负载中最大化 KV cache 复用；⑤ **三域验环境**：10K+ SWE/terminal/多跳搜索任务 |
| **最新版本** | GLM-5.2（2026-06-16）针对长程任务优化 |

---

## 16. InternLM (Shanghai AI Lab) — Intern-S1-Pro

| 项目 | 内容 |
|------|------|
| **英文标题** | Intern-S1-Pro: Scientific Multimodal Foundation Model at Trillion Scale |
| **发布机构** | Shanghai AI Laboratory (上海人工智能实验室) |
| **模型系列** | Intern-S1-Pro |
| **发布日期** | 2026-03-26 |
| **arXiv** | [2603.25040](https://arxiv.org/abs/2603.25040) |
| **参数量** | 1 trillion (首个万亿级科学多模态基础模型) |
| **主要创新** | ① 通用 + 科学领域全面增强；② 100+ 科学任务专家（化学、材料、生命科学、地球科学）；③ XTuner + LMDeploy 支持万亿参数级 RL 训练；④ "Specializable Generalist" 范式 |
| **前代** | Intern-S1 (arXiv 2508.15763) |

### InternLM3-8B-Instruct

| 项目 | 内容 |
|------|------|
| **发布日期** | 2025-01-15 |
| **参数量** | 8B |
| **链接** | [Hugging Face](https://huggingface.co/internlm/internlm3-8b-instruct) |

---

## 17. Moonshot AI (Kimi) — Kimi K2 / K2.5

### Kimi K2

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2：开放智能体智能 |
| **英文标题** | Kimi K2: Open Agentic Intelligence |
| **发布机构** | Moonshot AI (月之暗面) |
| **模型系列** | Kimi K2 |
| **发布日期** | 2025-07-28 |
| **arXiv** | [2507.20534](https://arxiv.org/abs/2507.20534) |
| **参数量** | 1T total, 32B activated (MoE) |
| **主要创新** | 开源非思考型模型 agentic 能力 SOTA；开放权重 |

### Kimi K2.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2.5：视觉智能体智能 |
| **英文标题** | Kimi K2.5: Visual Agentic Intelligence |
| **发布机构** | Moonshot AI (月之暗面) |
| **模型系列** | Kimi K2.5 (多模态) |
| **发布日期** | 2026-02-02 |
| **arXiv** | [2602.02276](https://arxiv.org/abs/2602.02276) |
| **参数量** | 1.04T total, 32B activated (384 专家, 8 activated/token) |
| **上下文长度** | 256K tokens |
| **主要创新** | ① 图文联合优化（joint text-vision pretraining, zero-vision SFT, joint text-vision RL）；② **Agent Swarm**：自导演化并行代理编排框架，相比单代理延迟降低 4.5×；③ 编码、视觉、推理、agent 任务全面 SOTA |
| **开源** | 开放后训练 checkpoint |

---

## 18. StepFun (阶跃星辰) — Step 3.5 Flash / STEP3-VL

### Step 3.5 Flash

| 项目 | 内容 |
|------|------|
| **中文标题** | Step 3.5 Flash：开放前沿级 11B 激活参数智能 |
| **英文标题** | Step 3.5 Flash: Open Frontier-Level Intelligence with 11B Active Parameters |
| **发布机构** | StepFun (阶跃星辰) |
| **模型系列** | Step 3.5 Flash |
| **发布日期** | 2026-02-11 |
| **arXiv** | [2602.10604](https://arxiv.org/abs/2602.10604) |
| **参数量** | 稀疏 MoE，11B active |
| **架构** | MoE Transformer，高吞吐、低 VRAM |
| **主要创新** | PaCoRe (Parallel Coordinated Reasoning) test-time compute scaling；前沿级推理与 agent 能力 |

### STEP3-VL-10B

| 项目 | 内容 |
|------|------|
| **英文标题** | STEP3-VL-10B Technical Report |
| **发布日期** | 2026-01-14 |
| **arXiv** | [2601.09668](https://arxiv.org/abs/2601.09668) |
| **参数量** | 10B |
| **主要创新** | ① 1.2T 多模态 token 统一预训练；② Qwen3-8B decoder + Perception Encoder；③ 1000+ 迭代 RL；④ PaCoRe 推理扩展；⑤ 性能比肩 10-20× 更大模型（MMMU 80.11%, AIME2025 94.43%） |

---

## 19. ByteDance (Seed/Doubao) — Seed 2.0 / Seed 1.8

### Seed 2.0 Model Card

| 项目 | 内容 |
|------|------|
| **中文标题** | Seed 2.0 Model Card：迈向真实世界复杂性的智能前沿 |
| **英文标题** | Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity |
| **发布机构** | ByteDance Seed (字节跳动豆包大模型团队) |
| **模型系列** | Seed 2.0 (Pro / Code 等) |
| **发布日期** | 2026-06-30 (arXiv 提交) |
| **arXiv** | [2607.00248](https://arxiv.org/abs/2607.00248) |
| **主要创新** | ① 基于真实用户需求构建评估体系；② 解决长尾知识与复杂指令跟随两大挑战；③ 世界领先的推理/视觉理解/搜索能力；④ 系统级优化适配大规模生产环境 |
| **应用** | 支持豆包 App (亿万用户)、TRAE (开发工具) |

### Seed 1.8 Model Card

| 项目 | 内容 |
|------|------|
| **英文标题** | Seed1.8 Model Card: Towards Generalized Real-World Agency |
| **发布日期** | 2026-03-21 |
| **arXiv** | [2603.20633](https://arxiv.org/abs/2603.20633) |
| **特点** | 面向通用真实世界 agent 的基础模型 |

---

## 20. Others — MiniMax / EXAONE / Ling & Ring 2.6

### Ling & Ring 2.6

| 项目 | 内容 |
|------|------|
| **英文标题** | Ling and Ring 2.6 Technical Report: Efficient and Instant Agentic Intelligence at Trillion-Parameter Scale |
| **发布日期** | 2026-06 |
| **arXiv** | [2606.15079](https://arxiv.org/abs/2606.15079) |
| **特点** | 万亿参数级高效即时 agent 智能 |

---

## 趋势分析

### 1. MoE 普及化
- 几乎所有头部玩家均已采用 MoE 架构（DeepSeek V4, Qwen3, GLM-5, Kimi K2/K2.5, Nemotron 3, Step 3.5 Flash）
- 激活参数量与总参数量比值持续优化（V4-Flash: 13B/284B, V4-Pro: 49B/1.6T）

### 2. 混合架构兴起
- **NVIDIA Nemotron 3**: Mamba-Transformer Hybrid MoE
- **DeepSeek V4**: CSA + HCA 混合注意力

### 3. 百万 Token 上下文成标配
- DeepSeek V4 (1M), Nemotron 3 (1M), Claude Opus 4.8 (1M)
- 长上下文效率创新（稀疏注意力、压缩注意力）是关键使能技术

### 4. 推理/思考模式成为基本功能
- DeepSeek V4 (Non-think/Think High/Think Max)
- Qwen3 (thinking + non-thinking)
- GLM-5 (reasoning_effort 参数)
- 推理预算控制（thinking budget）成为标准功能

### 5. Agent 原生化
- Kimi K2.5 Agent Swarm, GLM-5 异步 Agent RL
- Qwen3-Coder-Next 代理编程
- Nemotron 3 多环境 RL 训练
- 几乎所有新模型都强调 agentic 能力

### 6. 多模态融合加速
- Kimi K2.5 图文联合优化
- Phi-4-reasoning-vision, STEP3-VL-10B
- Qwen-VLA 统一视觉-语言-行动

### 7. 开源与开放科学
- DeepSeek V4 (开源权重), Qwen3 (Apache 2.0)
- Kimi K2/K2.5 (开放 checkpoint)
- GLM-5 (开源), Nemotron 3 (开源权重+配方+数据)

### 8. 后训练范式进化
- 两阶段后训练（DeepSeek V4: 独立专家培养 → on-policy 蒸馏）
- 异步 RL（GLM-5: decouple 生成与训练）
- 多环境 RL（Nemotron 3, Kimi K2.5）

---

*本报告基于各机构公开发布的技术报告 / System Card / Model Card 整理。发布日期以 arXiv 提交或官方发布日期为准。*
