---
title: arXiv Paper Check — AI & CTR (July 27, 2026)
type: synthesis
created: 2026-07-27
updated: 2026-07-27
sources: [arxiv-cs.AI, arxiv-cs.IR, arxiv-cs.LG]
tags: [arxiv, daily-check, ai, ctr, recommendation, reasoning, scaling]
---

# arXiv Paper Check — AI & CTR (July 27, 2026)

> Curated from cs.AI (144 new Jul 27), cs.IR, and cs.LG submissions.

## 🔥 Highlights

### AI Reasoning & Agents

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **PoTRE: Test-Time Reasoning via Cognitive Heterogeneity** | - | 4-agent ensemble (Adversarial Refinement, Strategic Planning, Spectrum Search, Direct Chain) with Task-Adaptive Aggregation. Achieves 49.92% on HLE, surpassing previous best official score. Uses fewer tokens than scaled homogeneous baselines. Published TMLR 2026. |
| **Loopie: Most Powerful Looped Transformer** | Zitian Gao, Yilong Chen, Yihao Xiao, Xinyu Yang, Ran Tao, Joey Zhou, Bryan Dai | 20B-param (2B active) MoE looped Transformer. First to demonstrate looped Transformers outperform vanilla baselines at same compute. Gold-medal performance at 2025 IMO and IPhO without tools. |
| **From Black Box to Executable Logic** | Eduardo C. Garrido-Merchán et al. | 3-stage post-hoc RL→Prolog transformation with machine-checkable return-loss bounds. On key-and-door task: exact optimal return in every seed. Matches neural teacher within noise on Acrobot with 11 clauses. |
| **LatentMT: Machine Translation with Latent Reasoning** | Wei-Rui Chen, Samar M. Magdy, et al. | First latent-reasoning LoopLM for MT. 2.6B backbone matches 3-5× larger models. Recurrent computation improves early then saturates. Lower training/inference compute than comparable non-latent models. |
| **Black-Mamba: Evidence-Gated State Tracking** | - | Test-time adaptive forecasting with event-triggered memory updates. Accumulates surprisal with leak, writes to LoRA adapter only when persistent evidence supports update. Reduces memory writes while maintaining accuracy. |

### CTR Prediction & Recommendation

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **GRAB: LLM-Inspired Sequence-First CTR** | Baidu | End-to-end generative CTR framework with Causal Action-aware Multi-channel Attention (CamA). Deployed at Baidu: +3.05% revenue, +3.49% CTR. Shows monotonic scaling with longer sequences. |
| **Dual-Stream MLP (DS-MLP) for CTR** | Kesha Ou, Zhen Tian, Wayne Xin Zhao, et al. | Knowledge distillation consolidates explicit interaction into main MLP, parallel MLP captures implicit. Vanilla MLP achieves SOTA on 3 benchmarks. Simple, efficient, scalable. |
| **GenCI: Generative Cohort Intent for CTR** | WWW 2026 | Generative NTP model produces candidate interest cohorts. Hierarchical candidate-aware network injects recall-stage contextual signal into ranking. End-to-end training. |
| **IDProxy: Cold-Start CTR with MLLMs** | Xiaohongshu | Multimodal LLMs generate proxy embeddings for cold items. Proxy aligned with ID embedding space, optimized end-to-end. Deployed serving hundreds of millions daily. |
| **PRECTR-V2: Unified Relevance-CTR** | - | Cross-user relevance preference mining for cold-start, exposure bias correction via synthetic hard negatives, LLM-distilled lightweight encoder (2M vs 110M params). |
| **DAIAN: Intent-Aware CTR for Trigger-Induced Rec** | - | Dynamically adapts to user intent preferences in TIR scenarios. Hybrid enhancer with ID + semantic similarity. +1.59% CTR, +1.73% diversity, +2.37% bills online. |
| **EST: Efficient Scaling Laws for CTR** | Alibaba/Taobao | Fully unified modeling without lossy aggregation. Lightweight Cross Attention + Content Sparse Attention. Power-law scaling confirmed. Deployed: +3.27% RPM, +1.22% CTR. |
| **Field-Aware Transformer (FAT)** | Alibaba/TDD | Reconstructs Transformer with field-centric parameters. Scaling depends on number of fields F, not vocabulary size n. +4.38% AUC, +2.33% CTR deployed at Taobao. KDD 2026. |

### Generative Models

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **Expanding Flow Maps (EFMs)** | Sophia Tang, Pranam Chatterjee | Flow maps between distributions of increasing dimensionality. Expand operator augments state, transport map pushes forward. Enables variable-size graph/sequence generation. |

### Attention & Transformers

| Paper | Authors | Key Contribution |
|-------|---------|------------------|
| **L1 Augmented Attention** | Kurt Godden | Subtracts learned L1 distance from dot product score. Hybrid: dot product rewards directional alignment, L1 penalizes coordinate deviations. Up to 14.5% perplexity reduction on WikiText-2. |

## 📊 Summary Statistics

- **Total curated**: 18 papers
- **AI Reasoning & Agents**: 5 papers
- **CTR Prediction & Recommendation**: 8 papers
- **Generative Models**: 1 paper
- **Attention & Transformers**: 1 paper
- **Other AI**: 3 papers

## 🔑 Key Trends

1. **Looped/Recurrent Architectures Maturing**: Loopie (20B MoE) and LatentMT demonstrate looped Transformers now outperform vanilla baselines. Latent computation is a viable alternative to explicit chain-of-thought.
2. **CTR Scaling Laws Validate in Production**: EST (Alibaba) and FAT (Alibaba/TDD) both confirm power-law scaling for CTR models, with significant production gains (+3.27% RPM, +4.38% AUC).
3. **Simplicity Wins in CTR**: DS-MLP shows vanilla MLP with distillation achieves SOTA. Not all CTR gains need complex architectures.
4. **Generative CTR Gains Traction**: GRAB (Baidu) and GenCI (WWW 2026) both use generative models for CTR, with GRAB deployed showing +3.49% CTR.
5. **Test-Time Adaptation Goes Event-Driven**: Black-Mamba and PoTRE both move away from continuous updates toward selective, evidence-gated adaptation.
6. **Cold-Start Solved via MLLMs**: IDProxy (Xiaohongshu) deploys multimodal LLMs to generate proxy embeddings for cold items, serving hundreds of millions daily.
