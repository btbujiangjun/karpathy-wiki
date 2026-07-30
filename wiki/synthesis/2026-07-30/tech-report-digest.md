---
title: "大模型技术报告摘要（2025-2026）| LLM Tech Report Digest (2025-2026)"
type: synthesis
created: 2026-07-30
updated: 2026-07-30
tags: [tech-report, system-card, llm, survey, deepseek, openai, meta, google, anthropic, mistral, qwen, microsoft, apple, nvidia, xai, amazon, bytedance, zhipu, kimi, internlm, baichuan]
---

# 大模型技术报告摘要（2025-2026）

> 各大 AI 公司最新发布的大模型技术报告 / System Card 汇总。
> 更新日期：2026-07-30

---

## 1. DeepSeek（深度求索）

### 1.1 DeepSeek-V3

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V3 技术报告 |
| **英文标题** | DeepSeek-V3 Technical Report |
| **发布机构** | DeepSeek-AI |
| **模型系列** | DeepSeek-V3 |
| **发布日期** | 2024-12-27 |
| **架构** | MoE（671B 总参数，37B 激活/token） |
| **训练数据** | 14.8T tokens |
| **上下文长度** | 128K |
| **核心创新** | MLA（Multi-head Latent Attention）+ DeepSeekMoE；辅助损失-free 负载均衡；Multi-Token Prediction (MTP) 训练目标；FP8 混合精度训练；从 DeepSeek-R1 蒸馏推理能力 |
| **论文** | https://arxiv.org/abs/2412.19437 |

### 1.2 DeepSeek-R1

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-R1：通过强化学习激励 LLM 推理能力 |
| **英文标题** | DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning |
| **发布机构** | DeepSeek-AI |
| **模型系列** | DeepSeek-R1 / R1-Zero |
| **发布日期** | 2025-01-01 |
| **架构** | MoE（671B 总参数，37B 激活） |
| **核心创新** | 纯 RL 训练推理（R1-Zero 无 SFT）；GRPO 算法；多阶段训练 pipeline（cold-start SFT → RL → rejection sampling SFT → RL）；向小模型蒸馏推理能力 |
| **论文** | https://arxiv.org/abs/2501.12948 |

### 1.3 DeepSeek-V3.1

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V3.1 发布 |
| **英文标题** | DeepSeek-V3.1 Release |
| **发布机构** | DeepSeek |
| **模型系列** | DeepSeek-V3.1 |
| **发布日期** | 2025-08-21 |
| **架构** | MoE（671B 总参数，37B 激活） |
| **上下文长度** | 128K |
| **核心创新** | 混合推理模式（Hybrid Thinking，支持 think/non-think 切换）；增强 Agent 工具调用能力；840B tokens 继续预训练 |
| **链接** | https://api-docs.deepseek.com/news/news250821/ |

### 1.4 DeepSeek-V3.2

| 项目 | 内容 |
|------|------|
| **中文标题** | DeepSeek-V3.2：推动开源大语言模型前沿 |
| **英文标题** | DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models |
| **发布机构** | DeepSeek |
| **模型系列** | DeepSeek-V3.2 / V3.2-Speciale |
| **发布日期** | 2025-12 |
| **架构** | MoE + DSA（DeepSeek Sparse Attention） |
| **核心创新** | DSA 稀疏注意力显著降低计算复杂度；大规模 RL 训练（超过预训练计算量的 10%）；Agentic 任务合成 pipeline；V3.2-Speciale 在 IMO 2025 和 IOI 2025 获得金牌级别成绩 |
| **论文** | https://arxiv.org/abs/2512.02556 |

---

## 2. OpenAI

### 2.1 GPT-5 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5 系统卡 |
| **英文标题** | GPT-5 System Card |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5（gpt-5-main / gpt-5-thinking / gpt-5-thinking-pro） |
| **发布日期** | 2025-08-13 |
| **核心创新** | 统一系统（router 自动切换 fast/thinking 模型）；thinking 模式通过 RL 训练；safe-completions 安全训练；大幅降低幻觉（比 o3 少约 6 倍）；AIME 2025 94.6%，SWE-bench 74.9% |
| **论文** | https://cdn.openai.com/gpt-5-system-card.pdf |

### 2.2 GPT-5.3-Codex System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.3-Codex 系统卡 |
| **英文标题** | GPT-5.3-Codex System Card |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.3-Codex |
| **发布日期** | 2026-02-05 |
| **核心创新** | 最强 Agentic Coding 模型；首次在网络安全领域被标记为 High capability；长时运行任务支持（研究、工具使用、复杂执行） |
| **论文** | https://cdn.openai.com/pdf/23eca107-a9b1-4d2c-b156-7deb4fbc697c/GPT-5-3-Codex-System-Card-02.pdf |

### 2.3 GPT-5.6 System Card

| 项目 | 内容 |
|------|------|
| **中文标题** | GPT-5.6 系统卡 |
| **英文标题** | GPT-5.6 System Card |
| **发布机构** | OpenAI |
| **模型系列** | GPT-5.6（Sol / Terra / Luna） |
| **发布日期** | 2026-07-09 |
| **核心创新** | 三个模型家族（旗舰 Sol、经济 Terra、快速 Luna）；CoT-Control 思维链可控性；Preparedness Framework 评估；推理 effort 曲线报告 |
| **论文** | https://deploymentsafety.openai.com/gpt-5-6/gpt-5-6.pdf |

---

## 3. Meta AI (LLaMA)

### 3.1 Llama 4

| 项目 | 内容 |
|------|------|
| **中文标题** | Llama 4 系列：架构、训练、评估与部署 |
| **英文标题** | The Llama 4 Herd: Architecture, Training, Evaluation, and Deployment Notes |
| **发布机构** | Meta AI |
| **模型系列** | Llama 4 Scout (17Bx16E) / Maverick (17Bx128E) / Behemoth (288B 激活, ~2T 总参) |
| **发布日期** | 2025-04-05 |
| **架构** | MoE（首次 Llama 使用 MoE）；early-fusion 原生多模态 |
| **训练数据** | Scout: ~40T tokens；Maverick: ~22T tokens |
| **上下文长度** | Scout: 10M；Maverick: 1M |
| **核心创新** | iRoPE 架构（interleaved attention + RoPE）支持超长上下文；Scout 可在单张 H100 部署；Behemoth 作为 teacher 进行 co-distillation；首创 MoE 在 Llama 系列的应用 |
| **论文** | https://arxiv.org/abs/2601.11659 |

---

## 4. Google DeepMind (Gemini)

### 4.1 Gemini 2.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Gemini 2.5：以先进推理、多模态、长上下文和下一代 Agent 能力推动前沿 |
| **英文标题** | Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities |
| **发布机构** | Google DeepMind |
| **模型系列** | Gemini 2.5 Pro / 2.5 Flash / 2.0 Flash / 2.0 Flash-Lite |
| **发布日期** | 2025-07-07 |
| **核心创新** | 原生多模态；>1M token 上下文；thinking 模型；Deep Think 技术（并行推理）；AIME 2025 88.0%；GPQA Diamond 86.4%；可处理 3 小时视频；Aider Polyglot SOTA |
| **论文** | https://arxiv.org/abs/2507.06261 |

---

## 5. Anthropic (Claude)

### 5.1 Claude Opus 4 & Sonnet 4

| 项目 | 内容 |
|------|------|
| **中文标题** | Claude Opus 4 和 Claude Sonnet 4 系统卡 |
| **英文标题** | System Card: Claude Opus 4 & Claude Sonnet 4 |
| **发布机构** | Anthropic |
| **模型系列** | Claude Opus 4 / Sonnet 4 |
| **发布日期** | 2025-05（系统卡 2025-07-16 更新） |
| **核心创新** | Hybrid Reasoning（扩展思考模式）；Opus 4 按 ASL-3 标准部署；首次包含 alignment assessment 和 model welfare assessment；在 CBRN、网络安全等领域的评估显著提升 |
| **论文** | https://www-cdn.anthropic.com/6d8a8055020700718b0c49369f60816ba2a7c285.pdf |

### 5.2 后续 Claude 版本

Anthropic 持续发布新模型系统卡，包括：

| 模型 | 发布日期 |
|------|----------|
| Claude Opus 4.1 | 2025-08 |
| Claude Sonnet 4.5 | 2025-09 |
| Claude Haiku 4.5 | 2025-10 |
| Claude Opus 4.5 | 2025-11 |
| Claude Opus 4.6 | 2026-02 |
| Claude Sonnet 4.6 | 2026-02 |
| Mythos Preview | 2026-04 |
| Claude Opus 4.7 | 2026-04 |
| Claude Opus 4.8 | 2026-05 |
| Claude Fable 5 & Mythos 5 | 2026-06 |
| Claude Sonnet 5 | 2026-06 |
| Claude Opus 5 | 2026-07 |

**系统卡索引**: https://www.anthropic.com/system-cards

---

## 6. Mistral AI

### 6.1 Mistral Large 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Mistral Large 3 技术文档 |
| **英文标题** | Mistral Large 3 Technical Documentation |
| **发布机构** | Mistral AI |
| **模型系列** | Mistral Large 3 / Ministral 3 (3B/8B/14B) |
| **发布日期** | 2025-12-02 |
| **架构** | Granular MoE（675B 总参数，41B 激活 + 2.5B Vision Encoder） |
| **上下文长度** | 256K |
| **核心创新** | Mistral 首个大规模 MoE（继 Mixtral 系列后）；Apache 2.0 开源；原生多模态视觉理解；多语言支持；与 NVIDIA 合作优化 |
| **链接** | https://mistral.ai/news/mistral-3/ |

---

## 7. Qwen（阿里通义千问）

### 7.1 Qwen3

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3 技术报告 |
| **英文标题** | Qwen3 Technical Report |
| **发布机构** | Alibaba（Qwen Team） |
| **模型系列** | Qwen3（0.6B ~ 235B-A22B，Dense + MoE） |
| **发布日期** | 2025-05-14 |
| **训练数据** | 36T tokens |
| **核心创新** | 统一 thinking / non-thinking 模式；thinking budget 机制；119 种语言；旗舰 235B-A22B MoE 超越 DeepSeek-R1/V3；Apache 2.0 开源 |
| **论文** | https://arxiv.org/abs/2505.09388 |

### 7.2 Qwen3.5

| 项目 | 内容 |
|------|------|
| **英文标题** | Qwen3.5: Towards Native Multimodal Agents |
| **发布机构** | Alibaba（Qwen Team） |
| **模型系列** | Qwen3.5（397B-A17B 等） |
| **发布日期** | 2026-02-16 |
| **架构** | MoE + Hybrid Attention |
| **核心创新** | 原生多模态 Agent；Thinker-Talker 架构升级 |
| **链接** | https://qwen.ai/blog?id=qwen3.5 |

### 7.3 Qwen3.5-Omni

| 项目 | 内容 |
|------|------|
| **中文标题** | Qwen3.5-Omni 技术报告 |
| **英文标题** | Qwen3.5-Omni Technical Report |
| **发布机构** | Alibaba（Qwen Team） |
| **模型系列** | Qwen3.5-Omni（Plus / Flash） |
| **发布日期** | 2026 |
| **上下文长度** | 256K |
| **核心创新** | 全模态（text + image + audio + video）；Hybrid-Attention MoE；ARIA（自适应文本-语音对齐）；>1 亿小时音视频训练；Audio-Visual Vibe Coding |
| **论文** | https://arxiv.org/abs/2604.15804 |

---

## 8. Microsoft (Phi)

### 8.1 Phi-4

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4 技术报告 |
| **英文标题** | Phi-4 Technical Report |
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4 (14B) |
| **发布日期** | 2024-12-12 |
| **核心创新** | 数据质量优先的预训练策略；大规模合成数据（multi-agent prompting、self-revision、instruction reversal）；超越 teacher 模型（GPT-4）的 STEM QA 能力 |
| **论文** | https://arxiv.org/abs/2412.08905 |

### 8.2 Phi-4-reasoning

| 项目 | 内容 |
|------|------|
| **中文标题** | Phi-4-reasoning 技术报告 |
| **英文标题** | Phi-4-reasoning Technical Report |
| **发布机构** | Microsoft Research |
| **模型系列** | Phi-4-reasoning / Phi-4-reasoning-plus (14B) |
| **发布日期** | 2025-04-30 |
| **核心创新** | 从 o3-mini 蒸馏推理能力；SFT + outcome-based RL；超越 DeepSeek-R1-Distill-Llama-70B；接近完整 DeepSeek-R1 水平 |
| **论文** | https://arxiv.org/abs/2504.21318 |

---

## 9. Apple

### 9.1 Apple Intelligence Foundation Language Models

| 项目 | 内容 |
|------|------|
| **中文标题** | Apple Intelligence 基础语言模型 2025 技术报告 |
| **英文标题** | Apple Intelligence Foundation Language Models: Tech Report 2025 |
| **发布机构** | Apple |
| **模型系列** | On-Device (~3B) / Server (PT-MoE) |
| **发布日期** | 2025-07-17 |
| **核心创新** | On-device: KV-cache sharing + 2-bit QAT；Server: Parallel-Track MoE (PT-MoE) + interleaved global-local attention；Private Cloud Compute；多语言多模态；Swift Foundation Models framework |
| **论文** | https://arxiv.org/abs/2507.13575 |

---

## 10. NVIDIA

### 10.1 Llama-Nemotron

| 项目 | 内容 |
|------|------|
| **中文标题** | Llama-Nemotron：高效推理模型 |
| **英文标题** | Llama-Nemotron: Efficient Reasoning Models |
| **发布机构** | NVIDIA |
| **模型系列** | LN-Nano (8B) / LN-Super (49B) / LN-Ultra (253B) |
| **发布日期** | 2025-05-02 |
| **上下文长度** | 128K |
| **核心创新** | 基于 Llama 3 的 Neural Architecture Search (NAS) + FFN Fusion；Knowledge Distillation + 大规模 RL；动态 reasoning toggle（standard/reasoning 模式切换）；LN-Ultra 超越 DeepSeek-R1 |
| **论文** | https://arxiv.org/abs/2505.00949 |

### 10.2 Nemotron 3 Nano

| 项目 | 内容 |
|------|------|
| **英文标题** | Nemotron 3 Nano: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3 Nano (30B-A3B) |
| **发布日期** | 2025-12-23 |
| **架构** | MoE + Hybrid Mamba-Transformer（31.6B 总参，3.2B 激活） |
| **训练数据** | 25T tokens |
| **上下文长度** | 1M |
| **核心创新** | Mamba-2 + GQA + MoE 混合架构；LV 训练（multi-environment RLVR + RLHF）；比同尺寸模型吞吐量高 3.3x |

### 10.3 Nemotron 3 Ultra

| 项目 | 内容 |
|------|------|
| **英文标题** | Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning |
| **发布机构** | NVIDIA |
| **模型系列** | Nemotron 3 Ultra (550B-A55B) |
| **架构** | MoE + Hybrid Mamba-Attention；LatentMoE；Multi-Token Prediction (MTP) |
| **训练数据** | 20T tokens |
| **上下文长度** | 1M |
| **核心创新** | NVFP4 预训练（最大规模 NVFP4 训练验证）；Multi-teacher On-Policy Distillation (MOPD)；推理吞吐量比 GLM-5.1 高 5.9x |
| **链接** | https://research.nvidia.com/labs/nemotron/ |

---

## 11. xAI (Grok)

### 11.1 Grok 3

| 项目 | 内容 |
|------|------|
| **中文标题** | Grok 3 Beta — 推理 Agent 时代 |
| **英文标题** | Grok 3 Beta — The Age of Reasoning Agents |
| **发布机构** | xAI |
| **模型系列** | Grok 3 / Grok 3 mini / Grok 3 (Think) |
| **发布日期** | 2025-02-19 |
| **上下文长度** | 1M |
| **核心创新** | Colossus 超算训练（10x 前代算力）；大规模 RL 训练推理（Think 模式）；DeepSearch Agent；AIME 2025 93.3%（cons@64）；GPQA 84.6% |
| **链接** | https://x.ai/news/grok-3 |

---

## 12. Amazon (Amazon Nova)

### 12.1 Amazon Nova

| 项目 | 内容 |
|------|------|
| **中文标题** | Amazon Nova 模型家族：技术报告与模型卡 |
| **英文标题** | The Amazon Nova Family of Models: Technical Report and Model Card |
| **发布机构** | Amazon AGI |
| **模型系列** | Nova Pro / Lite / Micro / Canvas / Reel |
| **发布日期** | 2025-06（arXiv） |
| **核心创新** | 多模态（text/image/video/document）；200+ 语言支持；视频理解首个在 Bedrock 上提供；Canvas 图像生成 + Reel 视频生成；SFT + DPO + PPO 对齐 |
| **论文** | https://arxiv.org/abs/2506.12103 |

---

## 13. ByteDance (字节跳动 / 豆包 / Doubao)

### 13.1 Seed1.5-VL

| 项目 | 内容 |
|------|------|
| **中文标题** | Seed1.5-VL 技术报告 |
| **英文标题** | Seed1.5-VL Technical Report |
| **发布机构** | ByteDance Seed |
| **模型系列** | Seed1.5-VL（530M Visual Encoder + 20B Active LLM） |
| **发布日期** | 2025-05-11 |
| **核心创新** | 多模态（视觉 + 语言）；SeedViT + MLP Adapter + LLM；多模态 Scaling Law 分析；SFT + RL（含 verifiable reward）；60 个公开 benchmark 中 38 个 SOTA |
| **论文** | https://arxiv.org/abs/2505.07062 |

### 13.2 Seed-Thinking-v1.5

| 项目 | 内容 |
|------|------|
| **中文标题** | Seed-Thinking-v1.5 技术报告 |
| **英文标题** | Seed-Thinking-v1.5 Technical Report |
| **发布机构** | ByteDance Seed |
| **模型系列** | Seed-Thinking-v1.5（MoE, 200B total, 20B active） |
| **发布日期** | 2025-04-14 |
| **核心创新** | 推理模型；Dual-track reward system；HybridFlow 编程模型；Streaming Reasoning System (SRS) 提速 3x；BeyondAIME 基准 |
| **链接** | https://github.com/ByteDance-Seed/Seed-Thinking-v1.5 |

### 13.3 Seed2.0

| 项目 | 内容 |
|------|------|
| **中文标题** | Seed2.0 系列 |
| **英文标题** | Seed2.0 Series |
| **发布机构** | ByteDance Seed |
| **模型系列** | Seed2.0 Pro / Lite / Mini |
| **发布日期** | 2026-02 |
| **核心创新** | 全模态理解（video/image/audio/text）；Agent 能力升级；Coding Agent 显著提升；Lite 版本为首个全模态理解模型 |

---

## 14. Zhipu AI（智谱 AI）

### 14.1 GLM-4.5 / GLM-4.1V-Thinking

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-4.5：Agentic、Reasoning、Coding（ARC）基础模型 |
| **英文标题** | GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models |
| **发布机构** | Zhipu AI & Tsinghua University |
| **模型系列** | GLM-4.5 (355B total, 32B active) |
| **发布日期** | 2025 |
| **架构** | MoE |
| **训练数据** | 23T tokens |
| **论文** | https://arxiv.org/abs/2508.06471 |

### 14.2 GLM-5

| 项目 | 内容 |
|------|------|
| **中文标题** | GLM-5：从 Vibe Coding 到 Agentic Engineering |
| **英文标题** | GLM-5: From Vibe Coding to Agentic Engineering |
| **发布机构** | Zhipu AI & Tsinghua University |
| **模型系列** | GLM-5 (744B total, 40B active) |
| **发布日期** | 2026-02-12 |
| **架构** | MoE + DSA（DeepSeek Sparse Attention） |
| **训练数据** | 28.5T tokens |
| **上下文长度** | 200K |
| **核心创新** | DSA 降低注意力计算 1.5-2x；异步 RL 基础设施（slime 框架）；异步 Agent RL 算法；全栈适配国产 GPU（华为昇腾、摩尔线程等 7 款芯片）；MIT 开源 |
| **论文** | https://arxiv.org/abs/2602.15763 |

---

## 15. Moonshot AI（月之暗面 / Kimi）

### 15.1 Kimi K2

| 项目 | 内容 |
|------|------|
| **中文标题** | Kimi K2：开放 Agent 智能 |
| **英文标题** | Kimi K2: Open Agentic Intelligence |
| **发布机构** | Moonshot AI (Kimi) |
| **模型系列** | Kimi K2（1T total, 32B active, MoE） |
| **发布日期** | 2025-07-28 |
| **架构** | MoE |
| **训练数据** | 15.5T tokens |
| **核心创新** | MuonClip 优化器（QK-clip 解决训练不稳定）；15.5T tokens 零 loss spike 训练；大规模 Agentic 数据合成 pipeline；Joint RL stage；SWE-Bench Verified 65.8%；开源 |
| **论文** | https://arxiv.org/abs/2507.20534 |

---

## 16. InternLM（上海 AI 实验室 / 上海人工智能实验室）

### 16.1 InternLM3

| 项目 | 内容 |
|------|------|
| **中文标题** | InternLM3 |
| **英文标题** | InternLM3 |
| **发布机构** | Shanghai AI Laboratory |
| **模型系列** | InternLM3-8B-Instruct |
| **发布日期** | 2025-01-15 |
| **训练数据** | 4T tokens（仅同类模型 1/4 成本） |
| **核心创新** | 数据效率革命——仅 4T tokens 达到领先水平；Thinking Density（IQPT）指标；通用-专家融合数据合成；深度推理与普通对话融合于单一模型 |
| **链接** | https://internlm.readthedocs.io/en/latest/model_card/InternLM3.html |

---

## 17. Baichuan（百川智能）

### 17.1 Baichuan4-Finance

| 项目 | 内容 |
|------|------|
| **中文标题** | Baichuan4-Finance 技术报告 |
| **英文标题** | Baichuan4-Finance Technical Report |
| **发布机构** | Baichuan Inc. |
| **模型系列** | Baichuan4-Finance-Base / Baichuan4-Finance |
| **发布日期** | 2024-12-17 |
| **核心创新** | 金融领域 LLM；Domain Self-Constraint 继续预训练策略；双 Scaling Law 确定数据配比；SFT + RLHF + AI Feedback |
| **论文** | https://arxiv.org/abs/2412.15270 |

---

## 18. StepFun（阶跃星辰）

| 项目 | 内容 |
|------|------|
| **中文标题** | Step 系列技术报告 |
| **英文标题** | Step Technical Report |
| **发布机构** | StepFun（阶跃星辰） |
| **模型系列** | Step-1 / Step-2 / Step-3 |
| **备注** | Step-3 为千亿参数多模态模型。详情待补充。 |

---

## 19. Yi / 01.AI（零一万物）

| 项目 | 内容 |
|------|------|
| **中文标题** | Yi 系列模型 |
| **英文标题** | Yi Series |
| **发布机构** | 01.AI（零一万物） |
| **模型系列** | Yi-Lightning / Yi-Large |
| **备注** | Yi-Lightning 为高效推理模型。详情待补充。 |

---

## 关键趋势分析

### 1. 架构趋势
- **MoE 成为主流**：几乎所有前沿模型都采用 MoE 架构（DeepSeek-V3/R1, Llama 4, Qwen3, Mistral Large 3, GLM-5, Kimi K2, Nemotron 3）
- **稀疏注意力**：DeepSeek 提出 DSA（DeepSeek Sparse Attention）被 Zhipu GLM-5 采用
- **混合架构**：NVIDIA Nemotron 3 系列探索 Mamba-Transformer 混合架构
- **Parallel-Track MoE**：Apple 提出 PT-MoE 新型并行 MoE 设计

### 2. 推理 / Reasoning
- **Thinking/Non-Thinking 统一**：Qwen3、DeepSeek-V3.1、GLM-5、Llama-Nemotron 均支持在同一模型中切换推理模式
- **RL 成为推理训练核心**：从 DeepSeek-R1 的纯 RL 到 Phi-4-reasoning 的 SFT+RL，RL 已成为推理能力的关键训练方法
- **推理预算控制**：thinking budget 机制（Qwen3）、reasoning toggle（Nemotron）、CoT-Control（GPT-5.6）

### 3. 多模态
- **原生多模态**：Llama 4 的 early fusion、Gemini 2.5 的原生多模态、Qwen3.5-Omni 的全模态
- **全模态统一**：Qwen3.5-Omni 统一 text/image/audio/video，ByteDance Seed2.0 Lite 支持全模态理解
- **多模态生成**：Amazon Nova Canvas/Reel，ByteDance Seedream，Qwen-Image-2.0

### 4. Agent 能力
- **Agent 成为核心赛道**：OpenAI GPT-5.3-Codex、DeepSeek-V3.1、Kimi K2、GLM-5 均以 Agent 能力为差异化重点
- **Agentic RL**：多环境强化学习、工具调用训练成为标准做法
- **SWE-bench 成为关键基准**：几乎所有厂商报告 SWE-bench Verified 得分

### 5. 长上下文
- **1M+ 上下文成标配**：Gemini 2.5、Grok 3、Nemotron 3、Llama 4 Scout（10M）
- **256K 为常见基线**：Qwen3.5-Omni、Mistral Large 3

### 6. Scaling Law
- **Post-training Scaling**：DeepSeek-V3.2 提出 RL 训练计算量已超过预训练 10%
- **数据效率**：InternLM3 以 4T tokens 实现 SOTA，强调数据质量而非数量
- **蒸馏 + RL 超越 teacher**：Phi-4 超越 GPT-4、Llama-Nemotron 超越 DeepSeek-R1

---

## 论文索引

| # | 机构 | 模型 | arXiv ID | 日期 |
|---|------|------|----------|------|
| 1 | DeepSeek | DeepSeek-V3 | 2412.19437 | 2024-12 |
| 2 | DeepSeek | DeepSeek-R1 | 2501.12948 | 2025-01 |
| 3 | DeepSeek | DeepSeek-V3.2 | 2512.02556 | 2025-12 |
| 4 | OpenAI | GPT-5 System Card | - | 2025-08 |
| 5 | OpenAI | GPT-5.6 System Card | - | 2026-07 |
| 6 | Meta | Llama 4 | 2601.11659 | 2026-01 |
| 7 | Google | Gemini 2.5 | 2507.06261 | 2025-07 |
| 8 | Anthropic | Claude Opus 4 & Sonnet 4 | - | 2025-05 |
| 9 | Alibaba | Qwen3 | 2505.09388 | 2025-05 |
| 10 | Alibaba | Qwen3.5-Omni | 2604.15804 | 2026-04 |
| 11 | Microsoft | Phi-4 | 2412.08905 | 2024-12 |
| 12 | Microsoft | Phi-4-reasoning | 2504.21318 | 2025-04 |
| 13 | Apple | Apple Intelligence FM | 2507.13575 | 2025-07 |
| 14 | NVIDIA | Llama-Nemotron | 2505.00949 | 2025-05 |
| 15 | Amazon | Amazon Nova | 2506.12103 | 2025-06 |
| 16 | ByteDance | Seed1.5-VL | 2505.07062 | 2025-05 |
| 17 | Moonshot | Kimi K2 | 2507.20534 | 2025-07 |
| 18 | Zhipu AI | GLM-5 | 2602.15763 | 2026-02 |
| 19 | Zhipu AI | GLM-4.5 | 2508.06471 | 2025-08 |
| 20 | Baichuan | Baichuan4-Finance | 2412.15270 | 2024-12 |
| 21 | Zhipu AI | GLM-4.5V / GLM-4.1V-Thinking | 2507.01006 | 2025-07 |
| 22 | ByteDance | Seedance 2.0 | 2604.14148 | 2026-04 |
| 23 | Alibaba | Qwen3-TTS | 2601.15621 | 2026-01 |
| 24 | Alibaba | Qwen-Image-2.0 | 2605.10730 | 2026-05 |
