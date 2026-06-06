---
title: arXiv Paper Check — 2026-06-01
type: synthesis
created: 2026-06-01
updated: 2026-06-01
sources: []
tags: [arxiv, paper-review, ctr, recommendation, ai, llm, rag]
---

# arXiv Paper Check — 2026-06-01

Scan of cs.AI, cs.IR, and cs.LG listings from the last 24 hours (Mon 1 Jun 2026 submissions, plus late May postings). 140 entries in cs.IR, 226+ in cs.AI, 264+ in cs.LG.

---

## CTR / Recommendation / Ranking

| Paper | Authors | Venue | Key Contribution |
|-------|---------|-------|-----------------|
| **Rec-Distill** (2605.29755) | Ding et al. (18 authors) | — | Industrial distillation pipeline for large-scale recommendation. Scales teacher to 24B params / 20K seq len; lightweight student recovers >60% gains. Validated on real-world platforms. |
| **Scaling Search CVR Prediction** (2605.29232) | Pak et al. (16 authors) | — | Empirical study of scaling CVR models on high-traffic e-commerce platform. Key findings: backbone/embedding/data scaling effects are largely independent. Deployed 2.5× data / 8× compute with minimal latency impact; +2.6% CVR gain. |
| **SaFeAU / Semantic Factor Learning for CF** (2605.31414) | Yu et al. | KDD 2026 | Beyond instance-level alignment: disentangles item representations into semantic factors to mitigate false negatives in CF. Outperforms GCN-based SOTA on sparse datasets with MF-level efficiency. |
| **Graph-GRPO** (2605.31003) | Che et al. | CIKM 2026 | Extends GRPO with dependency-aware credit assignment for generative e-commerce search relevance. Models CoT steps as a graph; propagates outcome rewards over edges. Online A/B wins on leading e-commerce platform. |
| **ACE** (2605.29322) | Lee, Kim, Lee | SIGIR 2026 | Anisotropy-Controllable Embedding for LLM-enhanced sequential rec. Linear autoencoder reshapes LLM embedding distribution while preserving semantics. +12.4% Recall@20, +11.8% NDCG@20. |
| **UniNote** (2605.29287) | Zhao et al. | KDD Ads Track 2026 | Unified multimodal embedding model for I2I retrieval deployed at Xiaohongshu. Two-stage: contrastive SFT + RL alignment. Integrated with Matryoshka Representation Learning. |
| **FOSTER** (2605.30772) | Tran et al. | — | First-order dataset distillation for text-based sequential recommendation. First-order optimization avoids bi-level gradient cost. Approximates full-dataset performance with only 20 synthetic sequences. |
| **LoopFM** (2605.29280) | Jiang et al. (~40 authors) | — | Learning from historical representations of foundation models for recommendation. Large industry recipe (likely Meta). |

## AI / LLM Systems

| Paper | Authors | Venue | Key Contribution |
|-------|---------|-------|-----------------|
| **AutoSci** (2605.31468) | Qian et al. (19 authors) | — | Memory-centric agentic system covering the full scientific research lifecycle. Four modules: SciMem (knowledge memory), SciFlow (5-stage lifecycle), SciDAG (DAG-shaped multi-agent ops), SciEvolve (self-improvement from feedback). |
| **LinTree** (2605.31492) | Kang, Teh, Lee | — | Explicitly structured search histories for LLM reasoning. Adding parent pointers (LinTree) to reasoning traces improves search efficiency over implicit CoT and heuristic-guided search in Blocks World, Navigation, Sokoban. |
| **UniScale** (2605.30898) | Huang et al. | ICML 2026 | Unifies model routing and test-time scaling as a contextual bandit problem. LinUCB-based online policy adapts to dynamic inference scenarios for better quality-cost trade-off. |
| **COLLEAGUE.SKILL** (2605.31264) | Zhou et al. | — | Automated trace-to-skill distillation for person-grounded AI skills. Produces versioned, inspectable, updateable skill packages. 18.5k GitHub stars, 215 skills from 165 contributors. |
| **DecomposeR** (2605.30824) | Hussain, Wu, Lu | — | Planner-centric RL for deep research. Represents research plans as typed DAGs; separate RL stages for planner and answerer. Qwen3-8B improves 5.1-8.0 points on long-form benchmarks. |
| **Planner-Centric RL for Deep Research** (2605.30824) | Hussain, Wu, Lu | — | Structure-aware reward via typed DAG research plans. Decouples planning from execution for better credit assignment. |
| **Balanced LoRA** (2605.31484) | Castin et al. | ICML 2026 | Removes parameter invariance in LoRA to accelerate convergence without extra compute. |
| **Positional vs Symbolic Attention Heads** (2605.31558) | Urrutia et al. | — | Study of learning dynamics, RoPE geometry, and length generalization. Distinguishes positional vs symbolic attention heads. |

## IR & RAG

| Paper | Authors | Venue | Key Contribution |
|-------|---------|-------|-----------------|
| **SPECTRA** (2605.31575) | Eric Liang | — | Framework for generating synthetic IR test collections with controllable topical structure, relevance oracles, and distractor diagnostics. 60K doc corpora with linear generation cost. |
| **Factual Density for RAG** (2605.31506) | Michael R. DeMarco | — | Introduces Factual Density (FD*) as a retrieval optimization signal for medical RAG. FD*-optimized retrieval achieves 100% systematic review saturation in top-5 results on HealthFC. |
| **No More K-means** (2605.30120) | Guo et al. | ICML 2026 | Single-stage sparse coding for efficient multi-vector retrieval. Eliminates K-means clustering bottleneck. |
| **FLASH-MAXSIM** (2605.29517) | Pony et al. | — | IO-aware fused kernels for late-interaction scoring. Optimizes ColBERT-style MaxSim computation. |
| **Latent Terms** (2605.29384) | Clavié et al. | — | Dense retrievers contain trivially extractable BM25-ready Zipfian vocabularies. Suggests dense models encode lexical patterns. |

## Notable Trends

1. **RL for recommendation is solidifying**: Graph-GRPO extends GRPO to e-commerce search relevance; UniNote uses RL alignment for ranking. GRL (Generative RL) is becoming a standard paradigm for recsys optimization.
2. **Scaling law papers go practical**: Both Rec-Distill and Scaling CVR Prediction tackle the reality gap between offline scaling gains and online deployment constraints. Independent additive effects of backbone/embedding/data scaling (CVR paper) is a practically useful finding.
3. **Agentic systems mature**: AutoSci covers the full research lifecycle; COLLEAGUE.SKILL standardizes skill packaging; DecomposeR uses typed DAG plans for deep research. The field is converging on structured, memory-centric, multi-agent architectures.
4. **Synthetic data for IR evaluation**: SPECTRA provides a rigorous framework for generating test collections on demand — useful for diagnosing failure modes before building human-judged collections.
5. **LLM embedding quality gets attention**: ACE tackles anisotropy in LLM-generated item embeddings. This is a recurring issue (see also Latent Terms paper showing dense retrievers encode lexical patterns).
