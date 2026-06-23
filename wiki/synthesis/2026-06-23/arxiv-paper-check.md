---
title: "arXiv Paper Check — AI & CTR (June 23, 2026)"
type: synthesis
created: 2026-06-23
updated: 2026-06-23
sources: [arxiv.org]
tags: [arxiv, ai, ctr, rlvr, recommendation, retrieval, kv-cache, multi-agent]
---

# arXiv Paper Check — AI & CTR (June 23, 2026)

Coverage: cs.AI (~220 new, 1181 total, Fri 19 Jun) + cs.IR (18 new, 90 total, Fri 19 Jun) + cs.LG (~201 new, 1113 total, Fri 19 Jun)

## Top Picks

### LLM Reasoning & RLVR

| Paper | Authors | Venue | Contribution |
|-------|---------|-------|-------------|
| [VIMPO: Value-Implicit Policy Optimization for LLMs](https://arxiv.org/abs/2606.20008) | Kang, Feng, Levine, Song, Zhao (Berkeley/MIT) | — | Critic-free RLVR using policy-implied value function derived from KL-regularized RL optimality conditions. Separates value loss (reward incorporation) from actor update (PPO-style). Beats GRPO on MATH-500, AIME 2024/2025, OlympiadBench; especially robust under noisy rewards. |
| [Beyond Entropy: Learning from Token-Level Distributional Deviations for LLM Reasoning](https://arxiv.org/abs/2606.19771) | Feng, Li, Liu et al. | — | ICT framework — shifts RLVR from scalar uncertainty to token logit distributional properties. JS divergence identifies critical branching tokens. Top 10% token updates → +4.58% avg pass@4 (max +14.9%) over GRPO on 7 math/commonsense/Olympiad benchmarks. |
| [Connect the Dots: Training LLMs for Long-Lifecycle Agents via RL](https://arxiv.org/abs/2606.20002) | Chen, Shi, Xie, Hu, Li, Ding, Zhou (Alibaba) | — | Framework for training LLMs to solve long task sequences, learn from experience, and self-update context. GRPO-style RL with fine-grained credit assignment. OOD generalization across domains and to Ralph-loop settings. |

### Multi-Agent Systems

| Paper | Authors | Venue | Contribution |
|-------|---------|-------|-------------|
| [Multi-Agent Transactive Memory](https://arxiv.org/abs/2606.19911) | Kim, He, Jain, Agrawal, Arabzadeh, Diaz | — | Population-level trajectory sharing for LLM agents via RAG. Producer agents contribute trajectories to shared repo; consumer agents retrieve them. Improves task performance and reduces interaction steps on ALFWorld and WebArena without coordination or joint training. |

### KV Cache & Inference Efficiency

| Paper | Authors | Venue | Contribution |
|-------|---------|-------|-------------|
| [UltraQuant: 4-bit KV Caching for Context-Heavy Agents](https://arxiv.org/abs/2606.20474) | Chakrabarti, Limpus et al. (AMD) | — | 4-bit KV cache compression for long-context agent workloads. TurboQuant-style rotation + codebook quantization. Asymmetric K/V, Walsh-Hadamard rotation, block-scale variants. 3.47× P50 TTFT reduction (cache-pressured rounds), 1.63× output throughput over FP8 baseline on AMD CDNA4. |

### CTR Prediction & Recommendation

| Paper | Authors | Venue | Contribution |
|-------|---------|-------|-------------|
| [Token Factory: Efficiently Integrating Diverse Signals into Large Recommendation Models](https://arxiv.org/abs/2606.19635) | Chen, Wang, Cakici et al. (Google) | — | Transforms traditional signals into "soft tokens" for LRMs. Prevents prompt length explosion. Production-scale validation. |
| [OneRank: Unified Transformer-Native Ranking for Multi-Task Recommendation](https://arxiv.org/abs/2606.16838) | Tang, Dai, Wang et al. | KDD 2026 | Eliminates encoder-predictor separation. Task-private channels with gradient detachment. Dynamic matching-based scoring. Outperforms SOTA on industrial-scale datasets. |
| [DIF: Denoising Implicit Feedback for Cold-start Recommendation](https://arxiv.org/abs/2606.19658) | Chen, Wang, Li et al. (Kuaishou) | KDD 2026 | Model-agnostic denoising using pseudo-labels from content-similar warm items. Adaptive uncertainty estimation. Deployed on billion-user scale Kuaishou. |

### Retrieval

| Paper | Authors | Venue | Contribution |
|-------|---------|-------|-------------|
| [ELVA: Exploring Ranking-Driven Universal Multimodal Retrieval](https://arxiv.org/abs/2606.20280) | Liu, Fu, Li et al. | ECCV 2026 | Extends RLVR to multimodal retrieval. Addresses "grain blindness" via ranking-driven MLLMs. Rule-based rewards, no explicit ranking labels. +13.1% on MRBench (new multi-grain benchmark). |
| [TPOUR: Temporal Preference Optimization for Unsupervised Retrieval](https://arxiv.org/abs/2606.17664) | Kim, Shim, Kim, Bak | ICML 2026 | Preference learning in temporal dimension via TRPO. Temporal embedding interpolation for unseen periods. Outperforms Qwen-Embedding-8B (+12.15% nDCG@5) while being 72.7× smaller. |

### LLM Quantization

| Paper | Authors | Venue | Contribution |
|-------|---------|-------|-------------|
| [Rethinking Shrinkage Bias in LLM FP4 Pretraining](https://arxiv.org/abs/2606.20381) | Zhao, Chen, Tian et al. | — | Identifies geometric origin of shrinkage bias in FP4 LLM pretraining. Proposes UFP4 recipe. 18 pages, 12 figures. |

## Key Themes

- **RLVR optimization** — VIMPO (critic-free value), ICT (token-level distributional) both push beyond GRPO's limitations
- **Long-lifecycle agents** — Alibaba's Connect the Dots + MATM (shared trajectory memory) address persistent agent challenges
- **KV cache compression** — UltraQuant pushes 4-bit KV for agent workloads with impressive speedups
- **Generative recommendation** — Token Factory (Google soft tokens) + OneRank (unified MTL ranking) + DIF (cold-start denoising) show industrial RecSys maturation
- **RLVR extends to retrieval** — ELVA brings RLVR to multimodal retrieval, TPOUR brings preference optimization to temporal retrieval
- **FP4 pretraining** — Shrinkage bias identified and addressed
