---
title: "arXiv Paper Check — 2026-07-05"
type: synthesis
created: 2026-07-05
updated: 2026-07-05
sources: []
tags: [arxiv, ai, ctr, recommendation, llm]
---

# arXiv Paper Check — 2026-07-05

> Latest submissions from cs.AI, cs.LG, cs.IR (Fri 3 Jul 2026). No new submissions on weekends.

## AI / LLM Highlights

### 1. Wiola: A Novel SLM Architecture
- **Authors**: Aryuemaan Kumar Chowdhury et al.
- **arXiv**: [2607.01394](https://arxiv.org/abs/2607.01394)
- **Key idea**: A from-scratch Small Language Model with 5 novel components: Spiral Rotary Positional Encoding (SRPE), Gated Cross-Layer Attention (GCLA), Adaptive Token Merging (ATM), Dual Stream FF, and WiolaRMSNorm. Released in 120M–1.5B sizes.
- **Significance**: Fully original architecture (no GPT/LLaMA lineage); shows there is still room for architectural innovation at small scale.

### 2. Discrete Diffusion for Radiology Report Drafting
- **Authors**: Max Van Puyvelde et al.
- **arXiv**: [2607.01436](https://arxiv.org/abs/2607.01436)
- **Key idea**: Adapted DiffusionGemma-26B for radiology; matches or exceeds autoregressive Gemma-4-26B with 3.5–4.4× faster decoding. Offers any-order infill capability — radiologists can fix fragments and have the model fill between them.
- **Significance**: First diffusion LLM applied to medical vision-language tasks; inherent bidirectional infill is a natural fit for clinical drafting.

### 3. Procedural Memory Distillation (PMD)
- **Authors**: Ye Liu et al. (Salesforce)
- **arXiv**: [2607.01480](https://arxiv.org/abs/2607.01480)
- **Key idea**: Stores cross-episode signals (trajectories, strategies, behavioral patterns) as reusable procedural memory and distills into policy weights. Improves over SDPO by 3.8–5.5% on SCIKNOWEVAL and 7.9–13.6% on LiveCodeBench.
- **Significance**: Co-evolution of policy and memory — addresses the limitation of episode-local RLVR updates.

### 4. Scaling Lie Detector Oversight (SOLiD) to 405B
- **Authors**: Oskar J. Hollinsworth et al.
- **arXiv**: [2607.01567](https://arxiv.org/abs/2607.01567)
- **Key idea**: Scales SOLiD to 405B models — undetected deception drops from 34% (1B) to 14% (405B). Human labelers can be removed entirely without statistically significant increase in deception.
- **Significance**: Favorable scaling for scalable oversight; but sensitive to distribution shift.

### 5. Diverse Evidence, Better Forecasts (InfoDelphi)
- **Authors**: Yuante Li et al.
- **arXiv**: [2607.01661](https://arxiv.org/abs/2607.01661)
- **Key idea**: Introduces designed information asymmetry — partitions evidence into public + private subsets so each agent holds exclusive knowledge. Outperforms baselines by 12–18% Brier score on forecasting benchmark.
- **Significance**: Shows that diversity of input (not just model diversity) is key for multi-agent deliberation.

### 6. C3RL + CAS: Confidence Calibration for LLMs
- **Authors**: Xuqing Yang et al.
- **arXiv**: [2607.01612](https://arxiv.org/abs/2607.01612)
- **Key idea**: RL algorithm that jointly optimizes correctness and confidence calibration. Enables Confidence-based Adaptive Test Time Scaling (CAS) — reduces inference budget by up to 12.33×.
- **Significance**: Practical path to resource-efficient, well-calibrated LLM inference.

### 7. Black-Box Inference of LLM Architecture (NightVision)
- **Authors**: Christopher Ellis et al.
- **arXiv**: [2607.01313](https://arxiv.org/abs/2607.01313)
- **Key idea**: Recovers hidden dimension (~23% avg error), depth, and parameter count of LLMs using only logprobs and TTFT measurements, even under restrictive APIs.
- **Significance**: Current LLM APIs are not sufficiently locked down to hide architectural details.

## ML Systems & Theory

### 8. Token Geometry (Ember Optimizer)
- **Authors**: Kathan Shah
- **arXiv**: [2607.01455](https://arxiv.org/abs/2607.01455)
- **Key idea**: Embedding/LM-head matrices have distinct gradient geometry. Ember uses O(V+D) VRAM instead of Adam's O(2VD), with no performance loss.
- **Significance**: Frees optimizer state memory bottleneck for large vocab models.

### 9. FADE: Focal Advantage with Dynamic Entropy
- **Authors**: Juliette Decugis et al.
- **arXiv**: [2607.01490](https://arxiv.org/abs/2607.01490)
- **Key idea**: Decomposes advantage functions along sign and difficulty axes; FADE self-adapts the gradient weight schedule, reaching peak pass@1 20k steps earlier at 7B scale.
- **Significance**: Improves RL training stability and accuracy-diversity trade-off.

### 10. Multi-Head Recurrent Memory (MHM-LRU)
- **Authors**: Jiatong Li et al.
- **arXiv**: [2607.01523](https://arxiv.org/abs/2607.01523)
- **Key idea**: Partitions recurrent memory into independent heads with select-then-update strategy. Retention rate at 896K tokens improves from <30% to 73.96%.
- **Significance**: Training-free architectural fix for long-context recurrent memory collapse.

### 11. Minimax Optimal KV Cache Compression
- **Authors**: Lukas Haverbeck et al.
- **arXiv**: [2607.01520](https://arxiv.org/abs/2607.01520)
- **Key idea**: Characterizes minimax risk of KV cache compression; proposes principled design achieving minimax-optimal risk. Validated on LongBench.
- **Significance**: Theoretical foundation for KV cache compression — moves beyond empirical approaches.

## CTR / Recommendation Systems

### 12. MixFormer (KDD 2026) — Industrial Recommender Co-Scaling
- **Authors**: Xu Huang et al.
- **arXiv**: [2602.14110](https://arxiv.org/abs/2602.14110) (replaced, accepted KDD 2026)
- **Key idea**: Unified Transformer jointly modeling sequential behavior + feature interactions. Co-scales dense capacity and sequence length. Deployed at Douyin / Douyin Lite.
- **Significance**: First unified architecture for dense feature interaction + sequence modeling in industrial recommenders.

### 13. GR2: Generative Reasoning Re-Ranker (Technical Report)
- **Authors**: Yufei Li et al.
- **arXiv**: [2606.31984](https://arxiv.org/abs/2606.31984) (replaced)
- **Key idea**: End-to-end re-ranking with reasoning-trace distillation + RL with verifiable rewards. Context compressor amortizes cost. +18.7% R@1, +7.1% R@3 over legacy baselines.
- **Significance**: First RLVR-based re-ranker deployed at industrial scale; shows reward hacking is a critical issue in re-ranking.

### 14. Bi-NAS: Bi-Level NAS for Recommender Explanations
- **Authors**: Longfeng Wu et al.
- **arXiv**: [2607.01387](https://arxiv.org/abs/2607.01387)
- **Key idea**: NAS jointly optimizes cross-attention and feature interaction for explainable recommendations. Integrates LLM zero-shot prompting for personalized explanations.
- **Significance**: First NAS approach to optimize recommendation explanations.

### 15. CoPersona: Collaborative Persona Graphs (KDD 2026)
- **Authors**: Yangtian Zhang et al.
- **arXiv**: [2607.01485](https://arxiv.org/abs/2607.01485)
- **Key idea**: Multiplex persona graph across users for collaborative personalization. Dual-branch: non-parametric peer retrieval + parametric graph reasoning.
- **Significance**: Addresses sparse user history problem by borrowing from similar users at facet level.

### 16. IntentTune — Query Intent Resolution for E-Commerce Search
- **Authors**: Rachith Aiyappa et al.
- **arXiv**: [2607.01530](https://arxiv.org/abs/2607.01530)
- **Key idea**: Resolves under-specified queries (e.g. "watch") using user-specific behavioral signals. Prior search queries outperform both population-level stats and profile info.
- **Significance**: Practical insight for e-commerce search — user-specific signals beat aggregated demand patterns.

### 17. Monosemanticity in Recommender Systems
- **Authors**: Yagel Alfasi et al.
- **arXiv**: [2606.29341](https://arxiv.org/abs/2606.29341) (replaced)
- **Key idea**: Applies Matryoshka Sparse Autoencoders (MSAE) to matrix factorization embeddings to extract interpretable monosemantic features. Demonstrates gender-associated latent neurons.
- **Significance**: Opens the black box of collaborative filtering embeddings — hierarchical sparsity reveals interpretable structure.

## Key Takeaways

1. **Diffusion LLMs are becoming practical** — competitive with autoregressive models, faster, and offer unique any-order infill for specialized domains.
2. **RL training for LLMs is maturing** — PMD, FADE, and C3RL each address different limitations (episode-local updates, training instability, confidence calibration).
3. **Collaborative personalization** for LLMs (CoPersona, Bi-NAS) is an emerging trend in IR.
4. **CTR/Recommendation continues to adopt generative architectures** — MixFormer and GR2 show the industry shift toward unified Transformer + RL-based ranking.
5. **KV cache compression** is getting theoretical grounding (minimax risk analysis), while recurrent memory gets a practical fix (MHM-LRU).
