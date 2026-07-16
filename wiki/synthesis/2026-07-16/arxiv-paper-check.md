---
title: "arXiv Paper Check — AI & CTR (July 16, 2026)"
type: synthesis
created: 2026-07-16
updated: 2026-07-16
sources: [arxiv-web-search]
tags: [arxiv, ai, ctr, recommendation, agents, scaling-laws]
---

# arXiv Paper Check — AI & CTR (July 16, 2026)

> Curated from cs.AI (148 new Jul 16), cs.IR (10 new Jul 16), and cs.LG listings.
> Focus: AI agents, CTR/recommendation, code generation, formal reasoning.

---

## Overview

Today's submissions show **three dominant themes**: (1) agent self-improvement and compounding optimization gains, (2) unified Transformer architectures replacing DLRMs in industrial CTR/search, and (3) generative recommendation with Semantic IDs maturing toward production. A notable ICML 2026 Spotlight paper argues for theory-level autoformalization — moving from isolated theorem statements to complete formal knowledge bases.

---

## 1. AI Agents & Optimization

### Do Agent Optimizers Compound? — Continual-Learning Evaluation on Terminal-Bench 2.0
**Authors:** Wenxiao Wang, Priyatham Kattakinda, Soheil Feizi (RELAI)
**arXiv:** [2607.14004](https://arxiv.org/abs/2607.14004) | **Date:** Jul 15 2026

Most agent-optimization gains are one-shot (optimize → report). This paper asks: do gains **compound** across successive optimization rounds? Using Terminal-Bench 2.0 with a two-phase continual-learning setup, they compare GEPA, Meta Harness, and RELAI-VCL. Key finding: only RELAI-VCL compounds — its optimized agent continues improving after new tasks are added (76.4% lifelong pass rate vs. 66.0% GEPA, 64.6% Meta Harness, 58.7% baseline). The critical ingredient is **regression control** in the optimization loop, which prevents shortcut solutions that erode prior gains.

> **Why it matters:** For deployed agents that face continuous task arrival, compounding is the property that separates real improvement from benchmark overfitting.

---

### Theory-Level Autoformalization: From Isolated Statements to Unified Formal Knowledge Bases
**Authors:** Marcus J. Min, Mike He, Zhaoyu Li, Zixuan Yi, Sharad Malik, Aarti Gupta, Xujie Si, Osbert Bastani
**arXiv:** [2607.13292](https://arxiv.org/abs/2607.13292) | **Date:** Jul 14 2026 | **Venue:** ICML 2026 Spotlight

Position paper arguing that autoformalization should move from translating individual theorems to formalizing **entire theories** — complete webs of axioms, definitions, and lemmas as structured libraries. Identifies three promising paths forward. Survey of autoformalization is available.

> **Why it matters:** Formal verification of AI-generated code/math requires complete theory libraries, not isolated statements. This is a prerequisite for systems like OpenAI's o3/o4 to produce machine-checkable proofs at scale.

---

### Experience Memory Graph: One-Shot Error Correction for Agents
**Authors:** Wenjun Wang, Yuchen Fang, Fengrui Liu, Zibo Liang, Kai Zheng
**arXiv:** [2607.13884](https://arxiv.org/abs/2607.13884) | **Date:** Jul 16 2026

Proposes using experience memory graphs for one-shot error correction in LLM agents — learning from a single failure to prevent recurrence. (11 pages, 6 figures)

---

### A Self-Evolving Agent for Longitudinal Personal Health Management
**Authors:** Haoran Li, Jiebi Deng, Tong Jin et al.
**arXiv:** [2607.13940](https://arxiv.org/abs/2607.13940) | **Date:** Jul 16 2026

Self-evolving agent for long-term health management. (20 pages, code available)

---

### LAPO: Leave-One-Turn Attribution for Self-Generated Process Rewards in Multi-Turn Search Reasoning
**Authors:** Qiang Zhu, Jiajun Wu
**arXiv:** [2607.13501](https://arxiv.org/abs/2607.13501) | **Date:** Jul 16 2026

Process reward attribution for multi-turn search/reasoning agents, enabling self-generated training signals without external reward models. (20 pages, 5 figures)

---

### Self-Improvements in Modern Agentic Systems: A Survey
**Authors:** Zhe Ren, Yimeng Chen et al.
**arXiv:** [2607.13104](https://arxiv.org/abs/2607.13104) | **Date:** Jul 16 2026

Comprehensive 97-page survey on self-improvement in agentic systems, covering self-reflection, self-correction, experience replay, and iterative optimization.

---

## 2. CTR Prediction & Search Ranking

### TMallGS: Scaling Unified Feature and Sequence Modeling for Generative E-commerce Search
**Authors:** Zhentao Song, Yufeng Gao, Xing Fang, Jing Wang et al. (Alibaba Tmall)
**arXiv:** [2607.13398](https://arxiv.org/abs/2607.13398) | **Date:** Jul 15 2026

TmallGS proposes a scalable ranking architecture for Tmall search, moving from DLRM to unified Transformer. Five key components:
1. **Hierarchical Distribution-Calibrated Tokenization** — Field-wise Saliency Reweighting + Distribution-Calibrated Projection
2. **Field-Adaptive Gated Transformer** — per-field QKV projections + noise-adaptive gating
3. **Decoupled FiLM Late Fusion** — preserves high-frequency signals
4. **Context-Aware Bias Net** — decouples systemic bias from user intent
5. **Error-Aware Progressive Training** — dynamically weighted losses

> **Why it matters:** This is the latest evidence that industrial search ranking is moving from DLRM to unified Transformer architectures. Addresses the "all-in-tokenization" weakness of prior approaches (OneTrans, Climber) by respecting feature heterogeneity. Deployed on Tmall with UCTCVR and GMV gains.

---

### DANet: Discount-Aware Network for Conversion Rate Prediction
**Authors:** Ruocong Tang, Yang Huang, Xing Fang et al. (Alibaba Tmall)
**arXiv:** [2607.12578](https://arxiv.org/abs/2607.12578) | **Date:** Jul 14 2026 | **Venue:** SIGIR 2026 Industry Track

Models the relationship between item discount rates and CVR with three components: Fourier transform for long-term discount trends, distribution de-bias for user-specific discounts, and supervised regression auxiliary task. Deployed on Tmall: **+3.63% pCVR, +2.23% GMV** in online A/B test.

> **Why it matters:** Discount/pricing awareness is a largely unexplored signal in CTR/CVR models. This paper demonstrates that explicit modeling of price sensitivity yields substantial production gains.

---

### IBA: Information-Gain Budget Allocation for Generative Recommendation
**Authors:** Shangxin Yang, Min Gao, Zongwei Wang, Junliang Yu
**arXiv:** [2607.12425](https://arxiv.org/abs/2607.12425) | **Date:** Jul 14 2026

In Semantic ID-based generative recommendation, each item is a sequence of tokens generated autoregressively with latent refinement. IBA allocates refinement compute based on per-position information gain: earlier positions (higher IG) get more refinement steps, later positions get fewer. Consistently improves strong baselines across multiple public datasets.

> **Why it matters:** Connects the "test-time compute scaling" paradigm (UTTSI, etc.) to generative recommendation. The observation that early Semantic ID positions carry more information mirrors the hierarchical nature of product catalogs.

---

### Learning to Forget: Satiation-Aware Long-Sequence Transducers for Mitigating Post-Purchase Redundancy
**Authors:** Yipin Dai, Ruocong Tang et al. (Alibaba Tmall)
**arXiv:** [2607.12714](https://arxiv.org/abs/2607.12714) | **Date:** Jul 15 2026 | **Venue:** SIGIR 2026 Industry Track

Addresses a practical problem in long-sequence user behavior modeling: post-purchase items in history create redundant recommendations. Proposes satiation-aware transducers that learn when to "forget" recently purchased items.

---

### Mitigating Early Training Collapse in CTR Models
**Authors:** Ergun Biçici, Erkan Çetinyamaç
**arXiv:** [2607.09696](https://arxiv.org/abs/2607.09696) | **Date:** Jun 20 2026

CTR models often exhibit sharp validation performance decline after the first epoch. Analyzes this on industrial datasets: reducing learning rate helps only incrementally, but **controlling feature sparsity** (removing highly sparse features, aggregating infrequent values) yields substantial improvements, stabilizing training and extending useful learning beyond one epoch.

> **Why it matters:** Provides actionable diagnosis for a common production training failure. The sparsity control insight complements the architecture-focused scaling papers.

---

## 3. Generative Recommendation & Semantic IDs

### Where Reasoning Matters: Rethinking Latent Reasoning in Semantic ID-based Generative Recommendation
**Authors:** Shangxin Yang, Min Gao, Zongwei Wang, Junliang Yu
**arXiv:** [2607.12425](https://arxiv.org/abs/2607.12425) | **Date:** Jul 14 2026

(Same as IBA above — this paper is the one that studies Semantic ID latent reasoning allocation.)

---

### Not Only NTP: Extending Training Signal Coverage for Generative Recommendation
**Authors:** Changhao Li, Shuli Wang et al.
**arXiv:** [2607.12277](https://arxiv.org/abs/2607.12277) | **Date:** Jul 15 2026

Argues that next-token prediction (NTP) alone is insufficient training signal for generative recommendation. Proposes extending training signals to improve coverage and representation quality.

---

### Beyond Semantic IDs: Encoding Business-Value Ranking into Document Identifiers for Generative Retrieval
**Authors:** Gui Ling, Zhihong Chen et al.
**arXiv:** [2607.11392](https://arxiv.org/abs/2607.11392) | **Date:** Jul 14 2026

Incorporates business-value ranking information directly into Semantic ID construction, so that the generative retrieval process naturally produces ranked results rather than requiring separate re-ranking.

---

## 4. Retrieval & Search Infrastructure

### Cluster with Auctions for Vector Search
**Authors:** Swann Bessa, Pierre Fernandez, Gergely Szilvasy, Matthijs Douze, Hervé Jégou
**arXiv:** [2607.13728](https://arxiv.org/abs/2607.13728) | **Date:** Jul 15 2026 | **Venue:** Under review NeurIPS 2026

Novel approach combining clustering with auction mechanisms for vector search efficiency. (10 pages, 6 figures)

---

### MESH: Scaling Up Retrieval with Heterogeneous Content Unification
**Authors:** Jiaxing Qu, Yilin Chen et al.
**arXiv:** [2607.12392](https://arxiv.org/abs/2607.12392) | **Date:** Jul 15 2026

Unified retrieval across heterogeneous content types (text, image, video, structured data) for production search systems.

---

### Optimizing Visibility in Generative Engines: A Critical Survey of GEO (2023–2026)
**Authors:** Olivier Martinez
**arXiv:** [2607.14035](https://arxiv.org/abs/2607.14035) | **Date:** Jul 16 2026

Comprehensive survey of 45 studies on Generative Engine Optimization — how to make content visible to LLM-based search engines (Perplexity, ChatGPT Search, etc.). Maps the emerging field analogous to SEO for the generative search era.

---

## 5. Code Generation & Verification

### Generative Compilation: On-the-Fly Compiler Feedback as AI Generates Code
**Authors:** Niels Mündler-Sasahara, Hristo Venev, Dawn Song, Martin Vechev, Jingxuan He
**arXiv:** [2607.13921](https://arxiv.org/abs/2607.13921) | **Date:** Jul 15 2026

Introduces "sealors" — lightweight transformations that convert partial programs into complete ones that standard compilers can diagnose during generation. Reduces non-compiling outputs and improves functional correctness on challenging repository-level Rust tasks. First partial-program checker for real Rust, with properties mechanized in Lean.

> **Why it matters:** Moves compilers from post-generation checks to active participants in the generation loop. Highly relevant for Karpathy's "verification gap" concept — this brings compiler verification closer to the generation process.

---

## Key Trends

| Theme | Papers | Signal |
|-------|--------|--------|
| **Agent compounding** | Do Agent Optimizers Compound?, Experience Memory Graph, LAPO | Self-improvement must be regression-controlled to compound |
| **Unified Transformer CTR** | TMallGS, DANet | Industrial search moving from DLRM → Transformer (heterogeneous tokenization) |
| **Generative rec maturing** | IBA, Beyond Semantic IDs, Not Only NTP | Semantic IDs + latent reasoning + business-value encoding |
| **Price/discount awareness** | DANet (+3.63% pCVR) | Explicit pricing signals are underexploited in CTR models |
| **Training stability** | Mitigating Early Collapse | Feature sparsity control > learning rate tuning for CTR |
| **Compilers in the loop** | Generative Compilation | Verification during generation, not after |
| **Formal verification** | Theory-Level Autoformalization (ICML Spotlight) | Complete theory libraries needed for AI proof checking |

---

## Summary Statistics

| Category | New Jul 16 | Curated |
|----------|-----------|---------|
| cs.AI | 148 | 6 |
| cs.IR | 10 | 8 |
| cs.LG | ~200+ | 2 |
| **Total** | **~358** | **16** |
