---
title: "Frontier Model Tech Reports — Comprehensive Digest (2025–2026)"
type: synthesis
created: 2026-06-20
updated: 2026-06-20
sources: []
tags: [tech-report, deepseek-v4, llama-4, gemini-2.5, claude-4, claude-5, mistral-large-3, kimi-k2, gpt-5.5, qwen3, moe, reasoning, long-context]
---

# Frontier Model Tech Reports — Comprehensive Digest

> 2026-06-20 | Covers the 8 major tech reports published between April 2025 and June 2026
>
> All major frontier labs converged on: **MoE architecture**, **reasoning/thinking modes**, **million-token contexts**, **RLVR post-training**, and **agentic capabilities**

---

## 1. DeepSeek V4 (2026-04-24)

| Attribute | V4-Pro | V4-Flash |
|-----------|--------|----------|
| **Total params** | 1.6T | 284B |
| **Active params** | 49B | 13B |
| **Architecture** | MoE (DeepSeekMoE) | MoE |
| **Context** | 1M tokens | 1M tokens |
| **Training tokens** | 33T | 32T |
| **License** | MIT | MIT |

**Key Innovations:**
- **Hybrid Attention**: Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA) — 1M context at 27% FLOPs and 10% KV cache of V3.2
- **Manifold-Constrained Hyper-Connections (mHC)**: Constrains residual mixing onto doubly stochastic matrices (Birkhoff polytope) via Sinkhorn-Knopp for stable signal propagation across 61 layers
- **Muon Optimizer**: Replaces AdamW for faster convergence at trillion-parameter scale
- **On-Policy Distillation**: Post-training replaces RL with distillation from 10+ domain specialist teachers (SFT + GRPO per domain → unified distillation)

**Key Benchmarks:**
- SWE-bench Verified: 80.6% (V4-Pro-Max)
- Codeforces: 3206 rating (first open model matching closed-source)
- $0.87/M output tokens (vs Opus 4.8 at $25/M, GPT-5.5 at $30/M)

**Sources:** [DeepSeek V4 Technical Report (PDF)](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf)

---

## 2. Llama 4 (2025-04-05)

| Attribute | Scout | Maverick | Behemoth |
|-----------|-------|----------|----------|
| **Total params** | 109B | 400B | 2T |
| **Active params** | 17B | 17B | — |
| **Architecture** | MoE (16E) | MoE (128E) | MoE |
| **Context** | 10M tokens | 1M tokens | — |
| **Training tokens** | ~40T | ~22T | — |
| **License** | Llama 4 Community | Llama 4 Community | — |

**Key Innovations:**
- **Early-fusion multimodality**: Native text+image input, trained end-to-end
- **iRoPE**: Interpolated Rotary Position Embedding for 10M context (Scout)
- **MoE with alternating layers**: Maverick alternates MoE and dense layers, applying experts in roughly half the layers
- **Behemoth teacher → student distillation**: 2T-param teacher used to distill Scout and Maverick

**Key Benchmarks:**
- Scout: Outperforms Gemma 3 27B and Mistral 3.1 on MT-Bench
- Maverick: 1M context, strong multimodal understanding (images, charts, documents)

**Sources:** [arXiv:2601.11659](https://arxiv.org/abs/2601.11659) | [Meta Llama 4 Model Card](https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md)

---

## 3. Gemini 2.5 (2025-07-07)

| Attribute | Gemini 2.5 Pro | Gemini 2.5 Flash | Gemini 2.0 Flash |
|-----------|---------------|-----------------|-----------------|
| **Architecture** | Sparse MoE | Sparse MoE | Sparse MoE |
| **Context** | 2M tokens | 1M tokens | 1M tokens |
| **Thinking** | Dynamic | Dynamic | No |
| **Input modalities** | Text, Image, Audio, Video | Text, Image, Audio, Video | Text, Image, Audio, Video |
| **Knowledge cutoff** | January 2025 | January 2025 | June 2024 |

**Key Innovations:**
- **Dynamic thinking**: Controllable inference-time compute budget (1,024–32,768 tokens) enabling monotonic performance scaling
- **3-hour video processing**: Optimized visual encoding at 66 tokens/frame (down from 258)
- **Agentic autonomy**: Demonstrated via "Gemini Plays Pokémon" — autonomous game completion in 406.5 hours over 100K+ token contexts
- **Training infrastructure**: TPUv5p at 93.4% compute utilization, slice-granularity elasticity maintaining 97% throughput during hardware failures
- **Lightweight deterministic replay**: Immediate repeat of any step with suspicious metrics to localize Silent Data Corruption (SDC) within minutes

**Key Benchmarks:**
- +122 Elo on LMArena over Gemini 1.5 Pro
- Aider Polyglot: 16.9% → 82.2% (400% improvement over 1.5 Pro)
- AIME 2025: Significant gains from thinking mode

**Sources:** [arXiv:2507.06261](https://arxiv.org/abs/2507.06261) | [Gemini 2.5 Report PDF](https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf)

---

## 4. Claude 4 & Claude 5 (2025-05 — 2026-06)

### Claude 4 (2025-05-22)

| Attribute | Opus 4 | Sonnet 4 |
|-----------|--------|----------|
| **Architecture** | Hybrid reasoning LLM | Hybrid reasoning LLM |
| **Context** | 200K tokens | 200K tokens |
| **Max output** | 32K tokens | 64K tokens |
| **Safety Level** | ASL-3 | ASL-2 |

### Claude Sonnet 4.5 (2025-09-29)

- SWE-bench Verified: 77.2% (82.0% with parallel compute)
- Terminal-Bench: 50.0%
- AIME 2025: 100% (with Python tools)
- Pricing: $3/$15 per M tokens (input/output)

### Claude Fable 5 & Mythos 5 (2026-06-09)

| Attribute | Fable 5 | Mythos 5 |
|-----------|---------|----------|
| **Context** | 500K tokens | 500K tokens |
| **Safety** | Full safeguards (ASL-3) | Safeguards lifted for trusted partners |
| **Availability** | General | Project Glasswing only |

- Mythos 5: Most capable Anthropic model to date
- Cybersecurity evaluations: "far ahead of Claude Opus 4.8"
- RSP evaluations: CB-1 capabilities; below CB-2 threshold but "much less clear judgement than for previous models"

**Sources:** [Claude 4 System Card (PDF)](https://www-cdn.anthropic.com/6be99a52cb68eb70eb9572b4cafad13df32ed995.pdf) | [Claude Fable 5 System Card (PDF)](https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf)

---

## 5. Mistral Large 3 (2025-12-02)

| Attribute | Value |
|-----------|-------|
| **Total params** | 675B |
| **Active params** | 41B |
| **Architecture** | Sparse MoE |
| **Context** | 256K tokens |
| **Training hardware** | 3,000 NVIDIA H200 GPUs |
| **License** | Apache 2.0 |
| **Pricing** | $0.50/$1.50 per M tokens |

**Key Innovations:**
- **Granular MoE**: First MoE from Mistral since Mixtral; fine-grained expert routing
- **NVFP4 quantization**: High-quality FP4 quantization for deployment on single H100/A100 node
- **EAGLE-3 speculation**: Speculative decoding for inference speedup
- **Cascade Distillation** (for Ministral 3 series): Iterative pruning + continued training with distillation for 3B/8B/14B models

**Key Benchmarks:**
- MMLU (8-language): ~85.5%
- HumanEval: ~92% pass@1
- LMArena: #2 among open-source non-reasoning models
- GPQA Diamond: ~43.9% (trading off extreme reasoning for general capability)

**Also released: Ministral 3 series** (3B, 8B, 14B dense models via Cascade Distillation, Apache 2.0, image understanding)

**Sources:** [mistral.ai/news/mistral-3](https://mistral.ai/news/mistral-3/) | [arXiv:2601.08584](https://arxiv.org/abs/2601.08584) (Ministral 3)

---

## 6. Kimi K2 → K2.6 (2025-07 — 2026-04)

### Kimi K2 (2025-07-28)

| Attribute | Value |
|-----------|-------|
| **Total params** | 1.04T |
| **Active params** | 32B |
| **Architecture** | MoE with MLA attention |
| **Context** | 128K tokens (YaRN) |
| **Training tokens** | 15.5T |
| **License** | Modified MIT |

**Key Innovations:**
- **MuonClip optimizer**: Muon + novel QK-Clip technique for training stability; zero loss spikes across 15.5T tokens
- **Agentic data synthesis pipeline**: Systematically generates tool-use demonstrations via simulated and real-world environments
- **Joint RL stage**: Combines verifiable rewards (RLVR) with self-critique rubric reward mechanism

**Key Benchmarks (non-thinking):**
- SWE-bench Verified: 65.8%
- Tau2-Bench: 66.1
- ACEBench (En): 76.5
- LiveCodeBench v6: 53.7
- AIME 2025: 49.5
- GPQA-Diamond: 75.1

### Kimi K2.6 (2026-04)

- +256K context via YaRN
- Thinking (default) + Instant modes
- MoonViT-3D vision encoder (~400M params)
- SWE-Bench Verified: 80.2 (Thinking mode)
- Terminal-Bench 2.0: 66.7
- #1 of 77 open-weights models on Artificial Analysis Intelligence Index (behind only Opus 4.6, GPT-5.4, Gemini 3.1 Pro)

**Sources:** [arXiv:2507.20534](https://arxiv.org/abs/2507.20534) | [Kimi K2.6 tech blog](https://www.kimi.com/blog/kimi-k2-6)

---

## 7. OpenAI GPT-5.5 (2026-04-23)

| Attribute | GPT-5.5 | GPT-5.5 Pro | GPT-5.5 Instant |
|-----------|---------|-------------|-----------------|
| **Architecture** | Proprietary reasoning LLM | Same + parallel test-time compute | Optimized for speed |
| **Context** | 1,050,000 tokens | 1,050,000 tokens | 1,050,000 tokens |
| **Max output** | 128K tokens | 128K tokens | 128K tokens |
| **Knowledge cutoff** | December 1, 2025 | December 1, 2025 | December 1, 2025 |
| **Pricing** | $5/$30 per M tokens | $30/$180 per M tokens | Included in ChatGPT |
| **Reasoning effort** | none/low/medium/high/xhigh | Same | Default mode |

**Key Benchmarks:**
- SWE-bench Verified: 88.7%
- Terminal-Bench 2.0: 82.7%
- MMLU: 92.4%
- FrontierMath Tier 1-3: 51.7%
- SWE-Bench Pro: 58.6%
- GDPval: 84.9%
- Codex task efficiency: Significantly fewer tokens than GPT-5.4 for same tasks

**Safeguards:**
- Full Preparedness Framework evaluation
- GPT-5.5-Cyber variant (May 7) for vetted cybersecurity teams under Trusted Access for Cyber program
- Codename "Spud"; known for "goblin" quirk (Nerdy personality reward signal removed post-launch)

**Sources:** [openai.com/index/introducing-gpt-5-5](https://openai.com/index/introducing-gpt-5-5/) | [GPT-5.5 System Card](https://deploymentsafety.openai.com/gpt-5-5/)

---

## 8. Qwen3 (2025-05-14)

| Model | Architecture | Total Params | Active Params | Context |
|-------|-------------|-------------|---------------|---------|
| Qwen3-235B-A22B | MoE (128E/8A) | 235B | 22B | 128K |
| Qwen3-30B-A3B | MoE (128E/8A) | 30B | 3B | 128K |
| Qwen3-32B | Dense | 32B | 32B | 128K |
| Qwen3-14B | Dense | 14B | 14B | 128K |
| Qwen3-8B | Dense | 8B | 8B | 128K |
| Qwen3-4B | Dense | 4B | 4B | 128K |

**Key Innovations:**
- **Hybrid Thinking Mode**: Single model supports both thinking (step-by-step reasoning) and non-thinking (fast response) modes with dynamic switching via chat template
- **Thinking Budget**: Users allocate compute adaptively per query — balances latency vs performance
- **Multilingual**: 119 languages and dialects (up from 29 in Qwen2.5)
- **Training data**: 36T tokens across dense and MoE models

**Key Benchmarks:**
- Qwen3-235B-A22B competitive with DeepSeek-R1, o1, o3-mini, Grok-3, Gemini 2.5 Pro
- Qwen3-30B-A3B outperforms QwQ-32B (10× active params)
- Qwen3-4B rivals Qwen2.5-72B-Instruct

**Sources:** [arXiv:2505.09388](https://arxiv.org/abs/2505.09388) | [Qwen3 Blog](https://qwenlm.github.io/blog/qwen3/)

---

## 9. Key Themes & Synthesis

### Architecture Convergence

| Theme | Adopters |
|-------|----------|
| **MoE (Mixture-of-Experts)** | DeepSeek V4, Llama 4, Gemini 2.5, Mistral Large 3, Kimi K2, Qwen3 |
| **Thinking/Reasoning modes** | DeepSeek V4 (think-high/max), Gemini 2.5 (dynamic), Claude 4/5 (extended), Kimi K2.6 (thinking/instant), Qwen3 (hybrid switchable), GPT-5.5 (configurable effort) |
| **Million-token context** | DeepSeek V4 (1M), Llama 4 Scout (10M), Gemini 2.5 Pro (2M), GPT-5.5 (1M), Kimi K2.6 (256K) |
| **RLVR post-training** | DeepSeek V4 (GRPO + on-policy distillation), Kimi K2 (MuonClip + joint RL), Gemini 2.5 (RL scaling) |
| **Muon-family optimizers** | DeepSeek V4, Kimi K2 (MuonClip) |

### Pricing Landscape (per 1M tokens, input/output)

| Model | Input $/M | Output $/M |
|-------|-----------|------------|
| DeepSeek V4-Pro | $0.435 | $0.87 |
| DeepSeek V4-Flash | $0.14 | $0.28 |
| GPT-5.5 | $5.00 | $30.00 |
| GPT-5.5 Pro | $30.00 | $180.00 |
| Claude Opus 4.7 | $15.00 | $75.00 |
| Claude Sonnet 4.5 | $3.00 | $15.00 |
| Gemini 2.5 Pro (standard) | $1.25 | $10.00 |
| Gemini 2.5 Pro (extended) | $2.50 | $15.00 |
| Mistral Large 3 | $0.50 | $1.50 |
| Qwen3-235B-A22B | ~$0.50 | ~$1.50 |

### Open-Weight Landscape

| Model | License | Total params |
|-------|---------|-------------|
| DeepSeek V4-Pro | MIT | 1.6T |
| Llama 4 Scout | Community | 109B |
| Llama 4 Maverick | Community | 400B |
| Mistral Large 3 | Apache 2.0 | 675B |
| Kimi K2/K2.6 | Modified MIT | 1.04T |
| Qwen3-235B-A22B | Apache 2.0 | 235B |

### Unresolved Questions

- **RLVR debate**: Does RL actually expand reasoning capability or just improve sampling efficiency? (NeurIPS 2025 Best Paper Runner-Up critique)
- **Long-context evaluation gap**: Benchmarks like RULER, LongBench-v2 may not capture real agentic long-context use
- **Safety-utility frontier**: Claude Mythos 5 shows CB-1 capabilities approaching CB-2 threshold — safety checks narrowing
- **Open-weight vs frontier gap**: Narrowing significantly in coding/agentic (DeepSeek V4, Kimi K2.6), still present in multimodal and broad knowledge
