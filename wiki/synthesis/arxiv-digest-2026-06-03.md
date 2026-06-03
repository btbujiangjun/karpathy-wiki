---
title: arXiv Digest — AI & CTR (June 3, 2026)
type: synthesis
created: 2026-06-03
updated: 2026-06-03
sources: []
tags: [arxiv, paper-review, ctr, recommendation, ai, llm, transformers, lora]
---

# arXiv Digest — AI & CTR (June 3, 2026)

Scan of cs.LG and cs.IR new listings from Wed 3 Jun 2026. 247 entries in cs.LG, 20 in cs.IR.

---

## CTR / Recommendation / Ranking

| Paper | Authors | Venue | Key Contribution |
|-------|---------|-------|-----------------|
| **Taiji** (2606.03866) | Li, Song, Yao, Lu, Jiang, Gai (Kuaishou) | — | LLM-as-Enhancer framework for industrial recommender systems. Pareto Optimal Policy Optimization (POPO) adaptively balances LLM semantic rewards vs. recommendation preference rewards. Reverse-engineered reasoning + open-ended rejection sampling for high-quality CoT data. Deployed on Kuaishou's ad platform since May 2026, serving 400M+ daily users. |
| **MARS** (2606.03718) | Yu, Zhou | — | Multi-rate Aggregation of Recency Signals for sequential recommendation. Encoder-agnostic operator consuming real timestamps producing K summaries at distinct recency scales fused by context-adaptive gate. Automatically selects Transformer (sparse data) or Mamba (dense data) based on avg sequence length. Best HR@10 on all 5 public benchmarks; +19.7% mean relative gain over strongest Transformer baseline on sparse data. |
| **UniPinRec** (2606.00422) | Li et al. (Pinterest) | — | First full-stack unification of retrieval and ranking at Pinterest scale. Shared transformer with Masked Action Modeling (MAM) eliminates interleaving; blended training pairs; cross-stage KV cache reuse. ~+1% online engagement, 11.1% latency reduction, 63.6% QPS lift. |
| **Can LLM Rerankers Predict Their Own Ranking Performance?** (2606.03535) | Ni, Bi, Guo et al. | — | Reranker-internal QPP. Self-consistency across sampled rankings matches SOTA and is better calibrated; verbalized confidence is severely overconfident. Proposes Verb-Num and Verb-List supervised methods for calibrated estimates with few extra tokens. |
| **Decoupled Residual Quantization** (2606.01844) | Wang et al. | — | Robust Semantic IDs for recommendation. Decouples quantization into separate residual streams to reduce error compounding. |
| **Dynamic Spectral Denoising with Global-Context Attention** (2606.02417) | Cai et al. | KDD 2026 | Multi-behavior recommendation with spectral denoising + global-context attention. |
| **BAHSD** (2606.03091) | Zhou et al. | — | Black-box sequential recommendation with adaptive distillation bridging the long-tail gap. |
| **Time-Aware Diffusion based on Preference Disentanglement** (2606.01670) | Zhu et al. | — | Generative recommendation via diffusion with time-aware preference disentanglement. |
| **Quantizing Intent** (2606.01396) | Choi et al. | — | Cross-domain Semantic IDs from organic activity for industrial ranking systems. |
| **Trustworthy Recommendation in the Era of LLMs** (2606.00540) | Wang, Cui et al. | — | Survey covering opportunities and challenges for trustworthy LLM-based recommendation. |

## AI / LLM Systems

| Paper | Authors | Venue | Key Contribution |
|-------|---------|-------|-----------------|
| **Language Models Need Sleep** (2606.03979) | Behrouz, Hashemi, Mirrokni | — | Introduces "Sleep" paradigm for continual learning: (1) Memory Consolidation via Knowledge Seeding (on-policy distillation + RL-based imitation learning); (2) Dreaming via RL-based synthetic curriculum generation for self-improvement without human supervision. |
| **Skill-RM** (2606.03980) | Chen, Jiang, Cheng et al. | — | Unifies heterogeneous evaluation criteria (rule verifiers, ground-truth refs, checklists, rubrics) into a single Reward-Evaluation Skill agent. Treats reward computation as a structured agentic task; dynamically selects and aggregates evidence. Outperforms traditional judge baselines in best-of-N and RL settings. |
| **Dynamic Short Convolutions Improve Transformers** (2606.03825) | Sieberling, Runwal, Panda, Kim | — | Input-dependent dynamic convolutions on K/Q/V. 1.33× compute advantage over standard Transformers at 150M–2B scale; 1.60× when applied after every linear layer. Also improves Mamba-2, Gated DeltaNet, and MoE. Custom Triton kernels make it practical. |
| **Compress then Merge (CtM)** (2606.03723) | He, Ding et al. | ICML 2026 | Merges T LoRAs into a single rank-r LoRA by computing shared r-dimensional subspaces before merging (reversing the usual Merge-then-Compress pipeline). Guarantees rank-r output by construction; narrows gap to full-parameter merging. |
| **Value-Aware Stochastic KV Cache Eviction (VaSE)** (2606.03928) | Chang, Fu et al. | — | Stochastic KV cache eviction for reasoning models. Value-aware approach preserves critical tokens probabilistically. |
| **TreeFlash** (2606.03819) | Rheinboldt, Berdoz, Wattenhofer | — | Parallel AR-approximation for faster speculative decoding using tree structures. |
| **Denoise First, Orthogonalize Later** (2606.03899) | Li, Zhang, Liu, Bao | — | Understanding momentum in the Muon optimizer via spectral filtering: denoising precedes orthogonalization. |
| **Rethinking Tensor Decompositions in Post-Training LLM Compression** (2606.03465) | Zagitov et al. | — | Systematic analysis of tensor decomposition methods (CP, Tucker, SVD) for LLM compression post-training. |
| **KVarN** (2606.03458) | Muller et al. | — | Variance-normalized KV-cache quantization mitigating error accumulation in reasoning tasks. |
| **Conformal Language Modeling via Posterior Sampling** (2606.03731) | Emmenegger, Olausson, Solar-Lezama, Podimata | — | Conformal prediction framework for LM decoding with statistical guarantees. |
| **When Graph Tokens Sink** (2606.03712) | Zhang et al. | — | Mechanistic analysis of graph language models: attention sink phenomenon in graph token representations. |
| **Exploiting Verification-Generation Gap** (2606.03608) | Li et al. | — | Test-time RL with confidence-conditioned verification; exploits gap between verifier and generator. |
| **CauTion** (2606.03602) | Peng et al. | — | Knowing when to trust LLMs for ensemble causal discovery. |
| **MAdam** (2606.03904) | Liu et al. | — | Metric-aware multi-objective Adam optimizer. |
| **q0** (2606.03938) | Mandal et al. | — | Primitives for hyper-epoch pretraining methodology. |
| **Speedrunning Tabular Foundation Model Pretraining** (2606.03681) | Ozturk, Pfefferle, Hutter | — | Efficient pretraining recipes for tabular foundation models. |
| **Flicker-DDPM** (2606.03393) | Mao | — | Accelerates denoising diffusion via 1/f colored noise injection. |

## IR / RAG / Retrieval

| Paper | Authors | Venue | Key Contribution |
|-------|---------|-------|-----------------|
| **Critic-R** (2606.00590) | Alam, Salemi, Zamani | — | Instruction-tuned retrievers with natural language introspective feedback for agentic search improvement. |
| **Cost-Aware Query Routing in RAG** (2606.02581) | Mishra | — | Empirical analysis of retrieval depth tradeoffs; cost-aware routing strategies. |
| **Do Neural Retrievers Prefer Certain Documents?** (2606.02814) | Valentini, Altszyler, Fajcik | — | Evidence of learned relevance priors in neural retrievers; systematic bias analysis. |
| **Attention Calibration for Position-Fair Dense IR** (2606.02737) | Michail et al. | — | Calibrates attention to mitigate position bias in dense retrieval. |
| **Slipstream** (2606.02992) | Yang, Zhao | — | Locality-aware graph index construction for streaming approximate nearest neighbor search. |
| **TechGraphRAG** (2606.01613) | Singh | — | Agentic graph-augmented RAG framework for technical literature reasoning. |
| **MemGraphRAG** (2606.00610) | Wu et al. | KDD 2026 | Memory-based multi-agent system for graph RAG. |

## Key Themes

1. **LLM x Recommendation convergence** — Taiji (Kuaishou) and UniPinRec (Pinterest) both show production deployments unifying LLM reasoning with traditional recsys pipelines, with significant online gains.
2. **Architecture improvements for Transformers** — Dynamic short convolutions offer a simple, hardware-efficient drop-in improvement across attention, linear RNNs, and MoE architectures.
3. **LoRA merging** — CtM (ICML 2026) solves the practical problem of consolidating multiple LoRA adapters into one without sacrificing low-rank structure.
4. **Continual learning for LLMs** — "Sleep" paradigm introduces biologically-inspired memory consolidation and dreaming phases, relevant for long-horizon adaptation.
5. **Sequential recommendation with temporal structure** — MARS makes multi-scale recency explicit, outperforming both Transformer and SSM baselines across data-density regimes.
6. **KV cache innovation** — Multiple papers (VaSE, KVarN) tackle KV cache efficiency for reasoning models, a hot topic as reasoning-lengths grow.
