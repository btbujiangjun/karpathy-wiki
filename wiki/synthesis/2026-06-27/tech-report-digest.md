---
title: LLM Tech Report Digest 2026-06-27
type: synthesis
created: 2026-06-27
updated: 2026-06-27
sources: []
tags: [tech-report-digest, llm, architecture, training, scaling-laws, multimodal, long-context, reasoning]
---

# LLM Tech Report Digest — 2026-06-27

> A comprehensive scan of the latest technical reports and system cards from major AI labs worldwide. Covers architecture, training methods, scaling laws, multimodal capabilities, long context, and reasoning models.

---

## 1. DeepSeek

### DeepSeek-V4

| Field | Value |
|-------|-------|
| **中文标题** | 深度求索 V4 技术报告 |
| **Publisher** | DeepSeek |
| **Model Name** | DeepSeek-V4-Pro / DeepSeek-V4-Flash |
| **Release Date** | 2026-04-24 |
| **License** | MIT (open-weight) |
| **Architecture** | Mixture-of-Experts (MoE) + DeepSeek Sparse Attention (DSA) + token-wise compression |
| **Total Params** | V4-Pro: 1.6T; V4-Flash: 284B |
| **Active Params** | V4-Pro: 49B; V4-Flash: 13B |
| **Context Length** | 1M tokens (default), 384K max output |
| **Training Data** | N/A |
| **Key Innovations** | Open-weight MoE with 1M context; DSA for efficient sparse attention over long sequences; MIT license enabling broad usage; 28-34x cheaper than GPT-5.5 / Opus 4.8 per output token; 80.6% SWE-bench Verified (highest open-weights entry) |
| **Link** | https://arxiv.org/abs/ (search: DeepSeek V4 technical report) |

### DeepSeek-V3 / DeepSeek-R1

| Field | Value |
|-------|-------|
| **中文标题** | 深度求索 V3 与 R1 技术报告 |
| **Publisher** | DeepSeek |
| **Model Name** | DeepSeek-V3-Base / DeepSeek-R1 |
| **Release Date** | 2024-12 (V3), 2025-01-20 (R1) |
| **License** | MIT (open-weight) |
| **Architecture** | MoE with Multi-head Latent Attention (MLA) + DeepSeekMoE |
| **Total Params** | 671B |
| **Active Params** | 37B |
| **Context Length** | 128K tokens |
| **Training Data** | 14.8T tokens (V3); RL + cold-start SFT (R1) |
| **Key Innovations** | MLA compresses KV cache via latent vectors; GRPO (Group Relative Policy Optimization) eliminates critic model in RL; R1 uses RLVR (Reinforcement Learning with Verifiable Rewards) for reasoning; multi-token prediction training objective |
| **Link** | https://arxiv.org/abs/2501.12948 (R1) |

---

## 2. OpenAI

### GPT-5 System Card

| Field | Value |
|-------|-------|
| **中文标题** | GPT-5 系统卡 |
| **Publisher** | OpenAI |
| **Model Name** | GPT-5 (gpt-5-main / gpt-5-thinking) |
| **Release Date** | 2025-08 |
| **License** | Proprietary |
| **Architecture** | Routed duo: main model + thinking model; optimal routing auto-selected per query |
| **Total Params** | N/A (proprietary) |
| **Active Params** | N/A |
| **Context Length** | ~400K tokens |
| **Training Data** | N/A |
| **Key Innovations** | Safe-completions paradigm shift — model is fine-tuned to *decline* unsafe requests at generation time (vs. refusal at input); routed architecture enables seamless reasoning vs. quick response; major focus on safety evaluations (CBRN, cyber, model autonomy) |
| **Link** | https://cdn.openai.com/gpt-5-system-card.pdf |

---

## 3. Meta (FAIR)

### Llama 4

| Field | Value |
|-------|-------|
| **中文标题** | Llama 4 模型族技术报告 |
| **Publisher** | Meta AI (FAIR) |
| **Model Name** | Llama 4 Scout / Maverick / Behemoth |
| **Release Date** | 2025-04 (Scout, Maverick); Behemoth announced |
| **License** | Open-weight (custom) |
| **Architecture** | Mixture-of-Experts (MoE) with early-fusion multimodal (text + vision jointly trained from early layers) |
| **Total Params** | Scout: 109B (17B active); Maverick: 400B (12B active per token via 128 experts w/ 1 active); Behemoth: 2T (288B active) |
| **Active Params** | Scout: 17B; Maverick: 12B; Behemoth: 288B |
| **Context Length** | Scout: 10M tokens (10,000,000 — staged cache + temperature-based RoPE); Maverick: 1M tokens; Behemoth: N/A |
| **Training Data** | 30T+ tokens (text + image + video) |
| **Key Innovations** | Massive scaling of context (10M — largest in industry); MoE-as-multimodal — early fusion of vision/text before MoE router; MetaP (meta-init hyperparameter discovery) for automated architecture search; iRoPE (interleaved RoPE) for long-context stability; Behemoth teacher for Scout/Maverick distillation |
| **Link** | https://arxiv.org/abs/2501.11659 (withdrawn, updated version available) |

---

## 4. Google DeepMind

### Gemini 3 Pro

| Field | Value |
|-------|-------|
| **中文标题** | Gemini 3 Pro 技术报告 |
| **Publisher** | Google DeepMind |
| **Model Name** | Gemini 3 Pro |
| **Release Date** | 2025-11 |
| **License** | Proprietary |
| **Architecture** | Proprietary (non-reasoning model with fast inference) |
| **Total Params** | N/A (proprietary) |
| **Active Params** | N/A |
| **Context Length** | 2M tokens |
| **Training Data** | N/A |
| **Key Innovations** | 2M context window — largest among closed-source frontier models; positions as general-purpose non-reasoning model vs. OpenAI's routed duo; strong on long-document and multimodal tasks |
| **Link** | System card available via Google AI |

---

## 5. Anthropic

### Claude Opus 4 & Sonnet 4

| Field | Value |
|-------|-------|
| **中文标题** | Claude Opus 4 & Sonnet 4 系统卡 |
| **Publisher** | Anthropic |
| **Model Name** | Claude Opus 4 / Claude Sonnet 4 |
| **Release Date** | 2025-01 |
| **License** | Proprietary |
| **Architecture** | N/A (proprietary) |
| **Total Params** | N/A |
| **Active Params** | N/A |
| **Context Length** | 200K tokens |
| **Training Data** | N/A |
| **Key Innovations** | Opus 4 focuses on safety and nuanced instruction following; Sonnet 4 as cost-efficient alternative; system card details evals across safety, coding, and reasoning dimensions |
| **Link** | https://anthropic.com (system card) |

---

## 6. Mistral AI

### Mistral 3 Family

| Field | Value |
|-------|-------|
| **中文标题** | Mistral 3 大模型技术报告 |
| **Publisher** | Mistral AI |
| **Model Name** | Mistral Large 3 / Ministral 3 (14B, 8B, 3B) / Mistral Small 4 / Mistral Medium 3.5 |
| **Release Date** | 2025-12 (Mistral 3); 2026-03 (Small 4); 2026-04 (Medium 3.5) |
| **License** | Apache 2.0 (Mistral 3 line); proprietary (Medium 3.5) |
| **Architecture** | Large 3: Sparse MoE (675B total, 41B active, 256K context); Small 4: hybrid instruct+reasoning dense; Medium 3.5: frontier multimodal |
| **Total Params** | Large 3: 675B; Small 4: N/A; Medium 3.5: N/A |
| **Active Params** | Large 3: 41B |
| **Context Length** | Large 3: 256K tokens; Small 4: 128K |
| **Training Data** | Large 3 trained on 3,000 NVIDIA H200 GPUs |
| **Key Innovations** | Large 3 is Mistral's first MoE since Mixtral; Apache 2.0 — fully open-weight; state-of-the-art multilingual (non-English/Chinese); Small 4 unifies instruct + reasoning + coding in single model; Medium 3.5 optimized for agentic/coding use cases |
| **Link** | https://mistral.ai/news/mistral-3 |

---

## 7. Alibaba / Qwen (通义千问)

### Qwen3 Technical Report

| Field | Value |
|-------|-------|
| **中文标题** | 通义千问 Qwen3 技术报告 |
| **Publisher** | Alibaba Cloud / Qwen Team |
| **Model Name** | Qwen3 |
| **Release Date** | ~2025 (PDF on GitHub) |
| **License** | Open-weight |
| **Architecture** | N/A (likely MoE or dense variant) |
| **Total Params** | N/A |
| **Active Params** | N/A |
| **Context Length** | Up to 128K+ |
| **Training Data** | N/A |
| **Key Innovations** | Qwen3 series covers multiple sizes including reasoning variants; strong multilingual (Chinese + English); Qwen-Image (Aug 2025) as image generation foundation model |
| **Link** | https://github.com/QwenLM/Qwen3 (PDF on GitHub) |

---

## 8. xAI

### Grok 4.20 System Card

| Field | Value |
|-------|-------|
| **中文标题** | Grok 4.20 系统卡 |
| **Publisher** | xAI |
| **Model Name** | Grok 4.20 |
| **Release Date** | 2026-04 |
| **License** | Proprietary |
| **Architecture** | N/A (proprietary) |
| **Total Params** | N/A |
| **Active Params** | N/A |
| **Context Length** | ~1M tokens |
| **Training Data** | N/A |
| **Key Innovations** | Single-agent and multi-agent modes; CBRN/cybersecurity safety evaluations; real-time X/Twitter data integration |
| **Link** | https://x.ai (system card) |

---

## 9. Microsoft

### Phi-4-Reasoning-Vision

| Field | Value |
|-------|-------|
| **中文标题** | Phi-4 推理视觉版技术报告 |
| **Publisher** | Microsoft Research |
| **Model Name** | Phi-4-Reasoning-Vision-15B |
| **Release Date** | 2026-03 |
| **License** | Open-weight (MIT) |
| **Architecture** | Dense Transformer with multimodal reasoning |
| **Total Params** | 15B |
| **Active Params** | 15B (dense) |
| **Context Length** | N/A |
| **Training Data** | Data quality focused (curated over scale) |
| **Key Innovations** | Small model achieving strong reasoning + vision; "data quality over quantity" philosophy extended to multimodal domain |
| **Link** | https://arxiv.org/abs/2603.03975 |

---

## 10. NVIDIA

### Nemotron 3 Ultra

| Field | Value |
|-------|-------|
| **中文标题** | Nemotron 3 Ultra 技术报告 |
| **Publisher** | NVIDIA |
| **Model Name** | Nemotron 3 Ultra |
| **Release Date** | 2026-06 |
| **License** | Open-weight (permissive) |
| **Architecture** | MoE hybrid |
| **Total Params** | N/A |
| **Active Params** | N/A |
| **Context Length** | N/A |
| **Training Data** | 19T+ tokens with curriculum pretraining |
| **Key Innovations** | Curriculum pretraining strategy progressing from easy→hard data; legal domain boost; optimized for NVIDIA hardware stack |
| **Link** | https://build.nvidia.com/nvidia/nemotron-3-ultra |

---

## 11. Apple

### Apple Intelligence Foundation Language Models

| Field | Value |
|-------|-------|
| **中文标题** | Apple 智能基础语言模型技术报告 |
| **Publisher** | Apple |
| **Model Name** | Apple Foundation Model (on-device ~3B + server model) |
| **Release Date** | 2025-07 |
| **License** | Proprietary (on-device) |
| **Architecture** | Parallel-Track MoE |
| **Total Params** | ~3B (on-device); server model N/A |
| **Active Params** | N/A |
| **Context Length** | N/A |
| **Training Data** | N/A |
| **Key Innovations** | On-device MoE via Parallel-Track design for efficient phone inference; privacy-first design; tight integration with iOS ecosystem; demonstrates on-device LLM viability at small scales |
| **Link** | https://machinelearning.apple.com (technical report) |

---

## 12. Amazon

### Amazon Nova

| Field | Value |
|-------|-------|
| **中文标题** | Amazon Nova 技术报告 |
| **Publisher** | Amazon (AGI) |
| **Model Name** | Amazon Nova Pro / Lite / Micro |
| **Release Date** | 2025-12 (tech report) |
| **License** | Proprietary |
| **Architecture** | N/A (proprietary) |
| **Total Params** | N/A |
| **Active Params** | N/A |
| **Context Length** | N/A |
| **Training Data** | N/A |
| **Key Innovations** | Strong translation and core capabilities; three-tier (Pro/Lite/Micro) for cost-performance tradeoffs; RAG integration for factual grounding |
| **Link** | https://aws.amazon.com/ai/nova |

---

## 13. ByteDance (字节跳动)

### Doubao-Seed-2.0

| Field | Value |
|-------|-------|
| **中文标题** | 豆包 Seed 2.0 技术报告 |
| **Publisher** | ByteDance |
| **Model Name** | Doubao-Seed-2.0 (Pro/Lite/Mini/Code variants) |
| **Release Date** | 2026-02 |
| **License** | Proprietary |
| **Architecture** | MoE + Sparse Attention + Multi-token Prediction |
| **Total Params** | N/A (proprietary) |
| **Active Params** | N/A |
| **Context Length** | N/A |
| **Training Data** | N/A |
| **Key Innovations** | Multi-token prediction training objective (predicting multiple future tokens simultaneously); sparse attention for long-context efficiency; dense-to-sparse training curriculum (starts dense, transitions to MoE for efficiency) |
| **Link** | Technical report available via ByteDance (web search) |

---

## 14. Zhipu AI (智谱 AI)

### GLM-5

| Field | Value |
|-------|-------|
| **中文标题** | GLM-5 技术报告 |
| **Publisher** | Zhipu AI (智谱 AI) |
| **Model Name** | GLM-5 |
| **Release Date** | 2026-02 |
| **License** | Open-weight |
| **Architecture** | Dense Sparse Attention (DSA) + async RL infrastructure |
| **Total Params** | N/A |
| **Active Params** | N/A |
| **Context Length** | N/A |
| **Training Data** | N/A |
| **Key Innovations** | DSA for efficient long-context; async RL training infrastructure for scalable post-training; strong agentic coding focus |
| **Link** | https://zhipu.ai (GLM-5 technical report) |

---

## 15. Moonshot AI / Kimi (月之暗面)

### Kimi K2 / K2.5

| Field | Value |
|-------|-------|
| **中文标题** | Kimi K2 与 K2.5 技术报告 |
| **Publisher** | Moonshot AI (月之暗面) |
| **Model Name** | Kimi K2 / Kimi K2.5 |
| **Release Date** | 2025 (K2); 2026-01 (K2.5) |
| **License** | Open-weight (K2); proprietary |
| **Architecture** | MoE (MuonClip optimizer — Muon optimizer + global gradient clipping) |
| **Total Params** | K2: 1T+ total, ~32B active; K2.5: N/A |
| **Active Params** | K2: ~32B |
| **Context Length** | 128K tokens |
| **Training Data** | 15.5T tokens (K2) |
| **Key Innovations** | MuonClip optimizer stabilizes ultra-large-scale MoE training; K2.5 introduces Agent Swarm (100 parallel agents for complex tasks); strong reasoning + coding performance; fully open-source reasoning MoE |
| **Link** | https://arxiv.org/abs/ (K2 technical report) |

---

## 16. StepFun (阶跃星辰)

### Step 3

| Field | Value |
|-------|-------|
| **中文标题** | Step 3 技术报告 |
| **Publisher** | StepFun (阶跃星辰) |
| **Model Name** | Step 3 |
| **Release Date** | 2025-07 |
| **License** | Open-source |
| **Architecture** | MoE |
| **Total Params** | 321B total |
| **Active Params** | 38B |
| **Context Length** | N/A |
| **Training Data** | N/A |
| **Key Innovations** | Native multimodal reasoning (text + images jointly); open-source SOTA at release; 8.5x inference efficiency vs. comparable models |
| **Link** | https://arxiv.org/abs/ (Step 3 technical report) |

---

## 17. Baichuan (百川智能)

### Baichuan M-Series

| Field | Value |
|-------|-------|
| **中文标题** | 百川智能 M 系列技术报告 |
| **Publisher** | Baichuan Intelligent Technology (百川智能) |
| **Model Name** | Baichuan-M1 / M2 / M3 |
| **Release Date** | M1: 2025-02; M2: 2025-09; M3: 2026-02 |
| **License** | Open-source (M1/M2); open-weight (M3) |
| **Architecture** | M1: Dense 14B trained from scratch; M2: Dense 32B; M3: medical-enhanced LLM |
| **Total Params** | M2-32B |
| **Active Params** | 32B (dense) |
| **Context Length** | 131K (Baichuan 3/4) |
| **Training Data** | M1: 20T tokens from scratch |
| **Key Innovations** | M1 trained from scratch (not continued pretraining); M2: Large Verifier System + GRPO RL for medical domain — outperforms all open-source models on HealthBench, only GPT-5 surpasses M2 on HealthBench Hard; M3: Surpasses GPT-5.2 in hallucination rate, proactive clinical inquiry |
| **Link** | https://arxiv.org/abs/2509.02208 (M2); https://arxiv.org/abs/2602.06570 (M3); https://arxiv.org/abs/2502.12671 (M1) |

---

## 18. InternLM (书生·浦语)

| Field | Value |
|-------|-------|
| **中文标题** | InternLM 技术报告 |
| **Publisher** | Shanghai AI Laboratory |
| **Model Name** | InternLM (104B; InternLM 2/3 follow-ups) |
| **Release Date** | 2024-01 (original 104B report) |
| **License** | Open-source |
| **Architecture** | Dense Transformer |
| **Total Params** | 104B (original) |
| **Active Params** | 104B (dense) |
| **Context Length** | N/A |
| **Key Innovations** | Strong Chinese-language performance; no InternLM 4 tech report found in current search |
| **Link** | https://github.com/InternLM/InternLM |

---

## 19. 01.AI / Yi (零一万物)

| Field | Value |
|-------|-------|
| **Publisher** | 01.AI (零一万物) |
| **Status** | Enterprise platform focus (WorldWise 2.5, multi-agent systems); no new model tech report found in current scan |
| **Latest** | Yi-Lightning / Yi-Large via API; shift toward enterprise AI applications and multi-agent orchestration |
| **Link** | https://01.ai |

---

## Key Themes & Cross-Cutting Insights

| Theme | Details | Labs |
|-------|---------|------|
| **MoE Dominance** | Mixture-of-Experts is now the default architecture for frontier models | DeepSeek, Meta, Mistral, ByteDance, StepFun, Moonshot, NVIDIA |
| **Scaling Context Windows** | Competition drives context from 128K → 1M → 10M tokens | Meta (10M), DeepSeek (1M), Google (2M), xAI (~1M) |
| **Reasoning Models** | Separate reasoning modes / routed architectures become standard | OpenAI (GPT-5 duo), DeepSeek (R1/V3), Moonshot (K2) |
| **Sparse Attention** | Architectural innovations to handle long sequences | DeepSeek (DSA), Zhipu (DSA), ByteDance (Sparse Attn) |
| **Open-Weight Race** | MIT/Apache 2.0 open-weight releases from multiple labs compete with proprietary | DeepSeek (MIT), Meta, Mistral (Apache 2.0), NVIDIA, Baichuan |
| **Domain Specialization** | Vertical models for medicine, legal, coding | Baichuan (medical), Microsoft (reasoning+vision), Mistral (Codestral/Leanstral) |
| **Multi-token Prediction** | Predicting multiple future tokens improves training efficiency | DeepSeek (V3), ByteDance (Seed 2.0) |
| **Reinforcement Learning Innovation** | GRPO, RLVR, async RL paradigms emerge | DeepSeek (GRPO/RLVR), Zhipu (async RL), Baichuan (GRPO + verifier) |

## Missing / Pending

- DeepSeek R2: Officially not yet released (R1 is latest)
- Baichuan 5: No tech report found (latest is M3 medical model)
- InternLM 4: No tech report found
- Amazon Nova 2: No tech report found (original family remains most recent)
- Qwen4: No tech report found (Qwen3 is latest confirmed)

---

*Auto-generated on 2026-06-27 via web search aggregation. Links and parameter counts sourced from public technical reports, system cards, and official documentation. Some proprietary model details are N/A where the lab does not disclose them.*
