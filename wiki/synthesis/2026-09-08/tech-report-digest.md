---
title: 2026-09-08 LLM Tech Report Digest
type: synthesis
created: 2026-09-08
updated: 2026-09-08
sources: [tech-report-digest.md]
tags: [llm, tech-report, 2026, moe, reasoning, multimodal, scaling-law, hybrid-attention, long-context, agentic, daily-digest]
---

## 2026-09-08 LLM Tech Report Digest

> 19 家公司最新大模型 Tech Report / System Card 摘要（截至 2026-09-08）。双语要点：模型名与机构均为中英对照；核心参数与创新点聚焦 MoE / hybrid attention / long-context / reasoning-agent / multimodal。
> Latest technical reports & system cards across 19 labs, as of 2026-09-08.

### 1. DeepSeek

**DeepSeek-V4**

- **Organization**: DeepSeek (深度求索)
- **Model**: DeepSeek-V4 (V4-Pro / V4-Flash)
- **Date**: April 2026 (arXiv 2606.19348)
- **Core Parameters**: V4-Pro 1.6T total / 49B active; V4-Flash 284B total / 13B active; sparse MoE; 1M context
- **Key Innovations**: Combined Sparse Attention (CSA) + Hybrid Context Attention (HCA) for efficient million-token context; Muon optimizer with joint momentum/Zo spaces; heavily synthetic/screened math data for reasoning; Flash-tier long-context intelligence
- **ArXiv**: https://arxiv.org/abs/2606.19348

> ⚠️ NOTE: 07-27 digest listed DeepSeek-V4 under arXiv 2507.06810; the Tech Report "Towards Highly Efficient Million-Token Context Intelligence" is arXiv 2606.19348 (2026-04-26).

---

### 2. OpenAI

**GPT-6 Astra System Card**

- **Organization**: OpenAI
- **Model**: GPT-6 Astra (also GPT-5.6 Sol/Terra/Luna)
- **Date**: September 3, 2026 (system card)
- **Core Parameters**: Not disclosed; context 1,050,000 tokens, 128K max output
- **Key Innovations**: agentic computer-task frontier model; alignment-faking / metagaming evaluations; UK AISI external safety evaluation included; full Preparedness framework chapter; dual-published system card (openai.com + deploymentsafety)
- **Source**: https://deploymentsafety.openai.com/gpt-6-astra · https://openai.com/gpt-5-6-system-card/

---

### 3. Meta AI

**Llama 4 + Muse Spark 1.3 / Muse Glimmer 30B**

- **Organization**: Meta AI
- **Model**: Llama 4 Scout / Maverick; Muse Spark 1.3; Muse Glimmer 30B
- **Date**: Sept 2, 2026 (Muse Spark 1.3); Aug 2026 (Muse Glimmer); July 2026 (Llama 4 mid-cycle checkpoint)
- **Core Parameters**: Scout 17B / 16 experts (up to 10M context); Maverick 17B / 128 experts; Muse Glimmer 30B open weights
- **Key Innovations**: Llama 4 Scout mid-cycle checkpoint improves instruction-following & code; Muse Glimmer 30B Apache 2.0 open assistant model; Muse Spark 1.3 upgrades coding & AI-agent capabilities
- **Source**: https://ai.meta.com/blog/llama-4-multimodal-intelligence/ · Muse announcements via Meta AI blog (Aug–Sep 2026)

---

### 4. Google DeepMind

**Gemini Model Cards**

- **Organization**: Google DeepMind
- **Model**: Gemini 3.6 Flash (updated Jul 21, 2026); Gemini 3.5 Flash-Lite; Gemini 3.1 Pro; Gemini Omni Flash (May 19, 2026); Gemini 3.5 Audio
- **Date**: 2026 (cards continuously updated)
- **Core Parameters**: Not disclosed
- **Key Innovations**: centralized model-cards hub; Pro-grade reasoning/code distilled to Flash tiers; 1M context; native multimodal incl. real-time audio (Omni Flash); multi-agent checkpoint releases
- **Source**: https://deepmind.google/models/model-cards/

---

### 5. Anthropic

**Claude Fable 5.1 / Mythos 5.1 System Cards**

- **Organization**: Anthropic
- **Model**: Claude Fable 5.1 and Mythos 5.1 (Sept 2026); Claude Opus 5 (July 2026); Sonnet 5 (June 2026); Fable 5 / Mythos 5 (June 2026); Opus 4.8 / 4.7
- **Date**: September 2026 (latest cards); July 2026 (Opus 5)
- **Core Parameters**: Not disclosed
- **Key Innovations**: system-cards central hub; dual-track product strategy — Fable (fast, everyday) vs Mythos (reasoning/agentic); extensive safety & misalignment documentation
- **Source**: https://www.anthropic.com/system-cards

---

### 6. Mistral AI

**Mistral Large 3**

- **Organization**: Mistral AI
- **Model**: Mistral Large 3 (v25.12); Ministral 3 (3B/8B/14B); Magistral (reasoning)
- **Date**: Dec 2, 2025 (GA); Ministral 3 report Jan 13, 2026 (arXiv 2601.08584)
- **Core Parameters**: 675B total / 41B active granular MoE; 256K context; multimodal
- **Key Innovations**: fully open-weight (Apache 2.0) frontier-scale MoE trained from scratch (~3,000 H200s, NVIDIA co-design with wide expert-parallelism / NVFP4); Magistral pure-RL reasoning from scratch (arXiv 2506.10910); Ministral 3 Cascade Distillation (iterative prune + distill, outperforms larger teacher distillation)
- **Sources**: https://arxiv.org/abs/2601.08584 · https://arxiv.org/abs/2506.10910 · https://docs.mistral.ai/models/mistral-large-3-25-12

---

### 7. Qwen (Alibaba)

**Qwen3.5-397B-A17B**

- **Organization**: Qwen Team (Alibaba Cloud, 通义千问)
- **Model**: Qwen3.5-397B-A17B (Qwen3.5 family)
- **Date**: Feb 16, 2026
- **Core Parameters**: 397B total / 17B active; sparse MoE + gated linear attention; 262K context
- **Key Innovations**: Gated DeltaNetwork (DeltaNet) hybrid linear-attention + sparse-MoE; natively multimodal via early text–image–video fusion (no separate encoders); non-padding tabular training data; Apache 2.0 open weights. (Base: Qwen3 tech report, arXiv 2505.09388)
- **Sources**: https://qwen.ai/blog?id=qwen3.5 · https://arxiv.org/abs/2505.09388

---

### 8. Yi (01.AI)

**Yi-Lightning**

- **Organization**: 01.AI (Yi, 零一万物)
- **Model**: Yi-Lightning
- **Date**: Dec 2024 (tech report)
- **Core Parameters**: Not disclosed (compact dual-expert MoE design)
- **Key Innovations**: RLHF (incl. SPMF preference alignment) + Verifier-RL that reset LMArena at release; RAISE safety framework; no new 2026 tech report published as of 2026-09-08
- **ArXiv**: https://arxiv.org/abs/2412.01253

---

### 9. Baichuan

**Baichuan-M4**

- **Organization**: Baichuan (百川智能) + THUBPM Group, Tsinghua University
- **Model**: Baichuan-M4 (clinical-grade medical agent)
- **Date**: June 8, 2026 (arXiv 2606.08982)
- **Core Parameters**: Not disclosed
- **Key Innovations**: designed for physician-supervised *continuous care* (multi-stage, long-horizon), not single-turn Q&A; Harness–Model–Tool architecture w/ long-term patient memory, tool use, evidence-based retrieval, multi-agent orchestration; hallucination rate lowered to 3.3%; citation precision 90 on Baichuan-EBM vs GPT-5.5 54.7
- **ArXiv**: https://arxiv.org/abs/2606.08982

---

### 10. Microsoft

**MAI-Thinking-1**

- **Organization**: Microsoft
- **Model**: MAI-Thinking-1 (MAI family — 7 models at Build 2026: reasoning/coding/image/voice/transcription); Phi-4-reasoning
- **Date**: June 2, 2026 (Build 2026); MAI-Thinking-1 report June 6, 2026
- **Core Parameters**: Not disclosed
- **Key Innovations**: Microsoft's first reasoning model trained from scratch — zero third-party distillation, clean commercially validated data; "hill-climbing machine" RL recipe; MAI-Image-2.5 top-2 on image-editing leaderboards; open-weight Phi-4-reasoning (14B) continues the small-model research line
- **Sources**: https://microsoft.ai/pdf/mai-thinking-1.pdf · https://arxiv.org/abs/2504.21318 (Phi-4-reasoning) · https://arxiv.org/abs/2412.08905 (Phi-4)

---

### 11. Apple

**Apple Foundation Models (Generation 3)**

- **Organization**: Apple
- **Model**: Third-generation Apple Foundation Models (AFM) — 5-model family
- **Date**: June 8, 2026 (announced at WWDC; tech report promised "later this summer")
- **Core Parameters**: 5-model family (on-device 1.4B up to 8B-class), built in collaboration with Google
- **Key Innovations**: all-new model generation trained with Google TPUs; hybrid on-device + Private Cloud Compute (PCC) deployment; privacy-preserving local + server foundation models; full technical report pending
- **Source**: https://machinelearning.apple.com/research/appintellifm

---

### 12. NVIDIA

**Nemotron 3 (hybrid Mamba–Transformer MoE)**

- **Organization**: NVIDIA
- **Model**: Nemotron 3 family — incl. Nemotron-3-Nano-30B-A3B, Nemotron 3 Super
- **Date**: 2025–2026 (white paper; arXiv 2512.20856)
- **Core Parameters**: hybrid state-space (Mamba) + Transformer MoE variants, from 30B-A3B Nano to Super tier; 1M context supported
- **Key Innovations**: Mamba–Attention hybrid MoE white paper — linear-time long-context + frontier reasoning; papers on Nemotron-Cascade 2 / Nemotron 3 Super / Nano (Omni); enterprise inference efficiency via sparse activation
- **Sources**: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-White-Paper.pdf · https://arxiv.org/abs/2512.20856

---

### 13. xAI

**Grok 4.6 / Grok 4 series (Grok 5 still in training)**

- **Organization**: xAI
- **Model**: Grok 4.6 (Aug 12, 2026); Grok 4.5 (Jul 8, 2026); Grok 4.20 Beta 2 (multi-agent); Grok 4 / Grok 4 Fast model cards
- **Date**: latest release Aug 2026; last published model cards Aug–Sep 2025
- **Core Parameters**: Not disclosed; Grok 4.6 context 500K, Grok 4.20 ~2M; Grok 5 (rumored 6–10T MoE) in training on Colossus 2 — no card yet
- **Key Innovations**: multi-agent parallel architecture in Grok 4.20 (4 specialist agents); fast agentic-coding line (Grok 4 Fast); Grok 5 remains unreleased (target slipped late-2025 → Q2 2026+), interim updates shipped as Grok 4.5 / 4.6 / 4.7-track
- **Sources**: https://data.x.ai/2025-08-20-grok-4-model-card.pdf · https://docs.x.ai/docs/models

---

### 14. Amazon

**Amazon Nova 2**

- **Organization**: Amazon (AWS)
- **Model**: Amazon Nova 2 family (multimodal reasoning + generation; Nova Pro / Premier / Flash)
- **Date**: December 2025 (Amazon Technical Reports)
- **Core Parameters**: Not disclosed
- **Key Innovations**: unified multimodal reasoning and generation models — one API for text/image/video understanding + image/video generation; enterprise security and cost tiers; Nova family tech report documents recipe
- **Sources**: https://www.amazon.science/publications/amazon-nova-foundation-models-technical-report · https://arxiv.org/abs/2506.12103

---

### 15. Zhipu AI

**GLM-5**

- **Organization**: Zhipu AI (智谱AI / Z.ai)
- **Model**: GLM-5 (GLM-5.1 / 5.3 iterative releases)
- **Date**: February 2026 (arXiv 2602.15763)
- **Core Parameters**: Not disclosed
- **Key Innovations**: Dynamic Sparse Attention (DSA) for cost-efficient long context; asynchronous RL post-training; state-of-the-art agentic coding; GLM ecosystem expansions incl. GLM-OCR technical report (arXiv 2603.10910)
- **Sources**: https://arxiv.org/abs/2602.15763 · https://arxiv.org/abs/2603.10910

---

### 16. InternLM

**Intern-S2-Mobius + Intern-S1-Pro**

- **Organization**: InternLM Team (Shanghai AI Laboratory, 上海人工智能实验室)
- **Model**: Intern-S2-Mobius (35B); Intern-S1-Pro (1T); Intern-S1 (2025)
- **Date**: Aug 14, 2026 (Mobius, arXiv 2608.14290); Mar 26, 2026 (S1-Pro, arXiv 2603.25040)
- **Core Parameters**: Mobius 35B; S1-Pro 1T — first trillion-parameter scientific multimodal FM
- **Key Innovations**: Mobius-v0 decouples knowledge storage (globally shared FFN Memory) from reasoning (Self-Attn Reasoners) — Backward Residual Connection + Dynamic Latent Reasoning; ~4× end-to-end inference speedup via shorter reasoning traces while matching Qwen3.5-35B quality; S1-Pro covers 100+ scientific tasks (SmolInstruct 74.8, AIME-2025 93.1)
- **Sources**: https://arxiv.org/abs/2608.14290 · https://arxiv.org/abs/2603.25040 · https://arxiv.org/abs/2508.15763

---

### 17. Moonshot AI

**Kimi K2.5**

- **Organization**: Moonshot AI (月之暗面)
- **Model**: Kimi K2.5 (Kimi-K2.6-1T-A32B follow-on)
- **Date**: Feb 2, 2026 (arXiv 2602.02276)
- **Core Parameters**: 1T total / 32B active MoE (K2.5); K2.6 1T-A32B
- **Key Innovations**: open-source multimodal agentic model — joint text–vision pre-training + zero-vision SFT + joint text–vision RL; Agent Swarm parallel multi-agent orchestration; up to 4.5× latency reduction in agentic workloads; flexible thinking modes
- **ArXiv**: https://arxiv.org/abs/2602.02276

---

### 18. StepFun

**Step 3.5 Flash / STEP3-VL-10B**

- **Organization**: StepFun (阶跃星辰)
- **Model**: Step 3.5 Flash; STEP3-VL-10B; Step-DeepResearch
- **Date**: 2026 (arXiv 2602.10604; STEP3-VL arXiv 2601.09668)
- **Core Parameters**: STEP3-VL-10B 10B; Step 3.5 Flash fast/efficient dense-class tier
- **Key Innovations**: high-speed efficient inference for general agent & dialogue tasks; STEP3-VL multimodal coding VLM (native 4K-resolution vision); Step-DeepResearch long-horizon research agent with ADR-Bench evaluation
- **Sources**: https://arxiv.org/abs/2602.10604 · https://arxiv.org/abs/2601.09668

---

### 19. ByteDance

**Seed 2.0 / Doubao 2.0**

- **Organization**: ByteDance (字节跳动) Seed / Doubao (火山引擎)
- **Model**: Seed2.0 series (Pro / Lite / Mini); Doubao 2.0
- **Date**: Feb 14, 2026 (release); Seed2.0 Model Card arXiv June 30, 2026 (2607.00248)
- **Core Parameters**: Not disclosed; multimodal; 256K context; flagship + Flash price floor ($0.022/M output)
- **Key Innovations**: eval system built from real user needs → long-horizon real-world agent tasks; agentic-coding focus; ecosystem — Seedance 2.0 video gen (arXiv 2604.14148), Seedream image gen, Seed-Thinking-v1.5 reasoning (arXiv 2504.13914)
- **Sources**: https://arxiv.org/abs/2607.00248 · https://arxiv.org/abs/2604.14148

---

## Key Trends Observed (2026)

### Architecture Evolution
- **Hybrid & linear attention ascend**: DeepSeek CSA+HCA, NVIDIA Mamba+Transformer MoE, Qwen3.5 DeltaNet linear attention, InternLM Mobius knowledge–reasoning decoupling — attention-only Transformers losing the efficiency narrative
- **MoE still ubiquitous**: active-parameter efficiency (DeepSeek 49B/13B, Mistral 41B, Qwen3.5 17B, Kimi 32B) is the norm at frontier scale
- **Trillion-scale beyond language**: Intern-S1-Pro (1T) targets scientific multimodal; Grok 5 (6–10T, rumored) still training

### Context Window Expansion
- **1M+ tokens**: DeepSeek-V4 (1M), OpenAI GPT-6 Astra (1.05M), Gemini/Nemotron (1M-class) standard; Qwen3.5 262K; Grok 500K–2M

### Reasoning, Agents & System Cards
- **Agents become the headline**: OpenAI GPT-6 Astra, Anthropic Mythos/Fable dual track, Microsoft MAI-Thinking-1 (trained from scratch, no distillation), Kimi Agent Swarm, Seed 2.0 agent-general models, Mistral Magistral
- **Domain-specialized agents**: Baichuan-M4 (clinical/medical), Intern-S1-Pro (scientific) — frontier output increasingly goes vertical
- **Safety documentation industrializes**: system/model cards now include UK AISI external evals (GPT-6 Astra), alignment-faking & metagaming tests, refusal/political-bias sections (xAI), multi-source eval schemas (Anthropic)

### Open-Weight Momentum
- Apache 2.0 frontier releases keep growing: Mistral Large 3, Qwen3.5-397B, Muse Glimmer 30B, Nemotron-Nano, Phi-4-reasoning, Kimi K2.5

### Efficiency & Small Models
- On-device / edge: Apple Gen-3 AFM 5-model family, Phi/StepFlash tiers; open-weight "small frontier" models rival much larger closed ones

---

*Last updated: 2026-09-08*