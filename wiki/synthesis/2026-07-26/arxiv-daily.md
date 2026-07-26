---
title: "arXiv Daily Report - 2026-07-26"
type: synthesis
created: 2026-07-26
updated: 2026-07-26
sources: []
tags: [arxiv, daily, llm, recommendation, advertising, sequential-modeling, ctr, games, ai]
---

# arXiv Daily Report — 2026-07-26

Curated selection of recent papers across AI, LLMs, recommendation, advertising, sequential modeling, CTR prediction, and games.

---

## Recommendation Systems

### 1. DLMRec: Diffusion Language Model for Recommendation

- **Authors:** Chengyi Liu, Yongqi Zhou, Junwei Pan, Zhixiang Feng, Chengguo Yin, Haijie Gu, Jie Jiang, Yinghao Liu, Yujuan Ding, Qing Li, Wenqi Fan
- **Affiliation:** Tencent / affiliated institutions
- **arXiv:** [2607.21519](https://arxiv.org/abs/2607.21519) (Jul 23, 2026)
- **Abstract:** Proposes DLMRec, a discrete diffusion language model tailored for recommendation as an alternative to autoregressive generation. Introduces a collaborative-aware stochastic tokenizer that encodes multi-hop collaborative signals into discrete tokens, a curriculum-driven training strategy aligning denoising with preference recovery, and a stability-aware voting mechanism for robust generation. Addresses limitations of LLM-based generative recommenders including prefix-constrained generation and error accumulation.
- **Key Innovations:**
  - Discrete diffusion for recommendation (non-autoregressive paradigm)
  - Collaborative-aware stochastic tokenizer
  - Curriculum-driven training for preference recovery
  - Stability-aware voting for generation consistency

---

### 2. UniRank: Benchmarking Ranking Models for Unified Sequential Modeling and Feature Interaction

- **Authors:** Honghao Li, Xianquan Wang, Zibin Zhang, Yi Zhang, Kangyi Lin, Yiwen Zhang
- **Affiliation:** Not specified
- **arXiv:** [2607.19987](https://arxiv.org/abs/2607.19987) (Jul 22, 2026)
- **Abstract:** Proposes an open benchmark for ranking models that unify sequential modeling and feature interaction. Benchmarks 15 representative models on 5 large-scale public datasets from short-video, advertising, and e-commerce (largest: 700M+ instances, sequences >10^5). Provides a PyTorch toolkit with DDP training, operator optimization, and mixed-precision for reproducible comparison. Studies scaling laws under limited compute.
- **Key Innovations:**
  - Open benchmark unifying sequential + feature interaction modeling
  - 15 models benchmarked across 5 large-scale datasets
  - Reproducible PyTorch toolkit with efficiency techniques
  - Scaling law analysis for ranking models

---

### 3. DeltaGate: Zero-Observation User Reactivation with Gap-Driven Dimensional Gating

- **Authors:** Jiandong Ding, Tianying Liu, Fuyuan Liu, Huijie Qin, Tiandeng Wu
- **Affiliation:** Not specified
- **arXiv:** [2607.19802](https://arxiv.org/abs/2607.19802) (Jul 22, 2026) — Accepted at RecSys 2026
- **Abstract:** Defines Zero-Observation Reactivation: returning users with no interactions during macro-gaps. Proposes DeltaGate, a lightweight frozen-backbone plugin that routes each representation dimension between personalized history and a learned global prior, conditioned on gap duration. In >365d gap setting, DG-SASRec reaches 0.047 Hit@10 vs 0.031 SASRec, with only 66K trainable parameters (2-4% overhead).
- **Key Innovations:**
  - Novel problem definition: Zero-Observation Reactivation
  - Lightweight dimensional gating conditioned on gap duration
  - Frozen backbone preserves zero drift; ~40x fewer parameters than retraining
  - Applicable to multiple SR backbones (SASRec, BERT4Rec)

---

### 4. PRL: Probabilistic Residual Learning for Online Recommendations

- **Authors:** Wenyuan Wang, Yusong Zhao, Zihao Xu, Hengyi Wang, Qi Xu, Zhigang Hua, Yan Xie, Yi Wang, Zihao Zhao, Bo Long, Chengzhi Mao, Shuang Yang, Hengguan Huang, Hao Wang
- **Affiliation:** Not specified (industry-scale)
- **arXiv:** [2607.20863](https://arxiv.org/abs/2607.20863) (Jul 23, 2026) — Accepted at RecSys 2026
- **Abstract:** Proposes Probabilistic Residual Learning (PRL), a causal Bayesian recommendation model that models the residual between ground-truth and base predictions. Probabilistically groups users for localized residual modeling, models domain-level confounders, and aggregates cluster-specific residual predictions using do-calculus. Plug-and-play compatible with various DL recommender systems.
- **Key Innovations:**
  - Causal Bayesian framework for residual modeling
  - do-calculus based aggregation over confounders
  - Plug-and-play: improves existing DL recommender systems
  - Automatic discovery of meaningful user clusters

---

### 5. CCBR: Controllable and Content-Based Recommendations

- **Authors:** Fırat Öncel, Jihoon Jeong, Emiliano Penaloza, Mirco Ravanelli, Laurent Charlin, Cem Subakan
- **Affiliation:** Mila / Université de Montréal
- **arXiv:** [2607.20938](https://arxiv.org/abs/2607.20938) (Jul 23, 2026)
- **Abstract:** Proposes CCBR framework that builds recommendations from textual user profile representations with controllability via text bottlenecks. Infers text summaries directly from item contents (images, audio, video). Enables text-based and multimodal interventions for user steering. Competitive with latent-representation models while providing interpretable, controllable summaries.
- **Key Innovations:**
  - Text bottleneck for controllable recommendation
  - Content-based inference from multimodal sources
  - User steering via textual interventions
  - Interpretable recommendation via text profiles

---

### 6. HiCore: Multi-Hypergraph Boosted Multi-Interest Self-Supervised Learning for Conversational Recommendation

- **Authors:** Yongsen Zheng, Ruilin Xu, Guohua Wang, Liang Lin, Kwok-Yan Lam
- **Affiliation:** Nanyang Technological University / Sun Yat-sen University
- **arXiv:** [2607.18609](https://arxiv.org/abs/2607.18609) (Jul 21, 2026)
- **Abstract:** Addresses Matthew effect in conversational recommender systems via multi-hypergraph construction (item-, entity-, word-oriented multiple-channel hypergraphs) for learning multi-level user interests. Self-supervised learning framework mitigates popularity bias in dynamic user-system feedback loops.
- **Key Innovations:**
  - Multi-hypergraph construction for multi-level interest modeling
  - Self-supervised learning for Matthew effect mitigation
  - Dynamic feedback loop modeling in CRS

---

### 7. PRTA: Personalized Recommendation Tool Learning via Autonomous Language Agents

- **Authors:** Mingdai Yang, Zhiwei Liu, Weizhi Zhang, Yibo Wang, Hao Peng, Philip Yu
- **Affiliation:** University of Illinois Chicago
- **arXiv:** [2607.19739](https://arxiv.org/abs/2607.19739) (Jul 22, 2026) — Accepted at RecSys 2026
- **Abstract:** Proposes an agent-based recommendation framework where an LLM acts as central planner interacting with multiple recommendation models as tools. The LLM handles high-level reasoning and personalized tool selection while traditional models perform full-ranking. Design includes reflection mechanisms for per-user tool evaluation.
- **Key Innovations:**
  - LLM as meta-planner over recommendation tool ensemble
  - Personalized tool selection via reflection mechanisms
  - Combines LLM reasoning with traditional model scalability

---

### 8. Learning Sparse Representations for Cold Item Recommendation

- **Authors:** Gregor Meehan, Johan Pauwels
- **Affiliation:** Not specified
- **arXiv:** [2607.17184](https://arxiv.org/abs/2607.17184) (Jul 19, 2026) — Accepted at RecSys 2026
- **Abstract:** Argues sparse embeddings outperform dense vectors for content-based cold-start. Uses linear attention-inspired pre-sparsification activation for sharpness and denoising. Sparse embeddings achieve significant cold-start accuracy improvements at lower storage costs, with interpretability benefits.
- **Key Innovations:**
  - Sparse embeddings for cold-start recommendation
  - Pre-sparsification activation from linear attention
  - Interpretability + storage efficiency trade-off

---

### 9. Spectral Biclustering for Post-Hoc Explainability in Recommender Systems

- **Authors:** Jose L. Salmeron, Irina Arévalo
- **Affiliation:** Universidad de Granada
- **arXiv:** [2607.19189](https://arxiv.org/abs/2607.19189) (Jul 21, 2026) — Published in Knowledge-Based Systems
- **Abstract:** Uses spectral biclustering to group users/items for block-deletion diagnostics, reducing retraining cost of observation-level deletion. Produces explanations at user-segment and item-group levels. Evaluated on SVD and Neural CF with MovieLens and Amazon datasets.
- **Key Innovations:**
  - Block-deletion diagnostic via spectral biclustering
  - Scalable post-hoc explainability
  - Model-agnostic analysis framework

---

## Advertising / CTR Prediction

### 10. LO-FAR: A Cost-Aware Local Filter for Sparse Feature Ranking in Industrial Ad Recommendation

- **Authors:** Egemen Erbayat, Luis Duque, Sohini Roychowdhury, Mohammad Amin, Srihari Reddy
- **Affiliation:** Industry (likely Snap or similar)
- **arXiv:** [2607.20873](https://arxiv.org/abs/2607.20873) (Jul 23, 2026) — Accepted at RecSys 2026
- **Abstract:** Presents Localized Feature Ranking (LO-FAR), a CPU-only, model-agnostic workflow ranking sparse ID-list features from standalone held-out predictive signal using lightweight local estimators. On a production dataset of 1M+ interactions and 475 sparse features, completes ranking in ~2 CPU-hours. Preserves downstream NE gains on CTR/CVR competitive with shuffle-based importance.
- **Key Innovations:**
  - CPU-only, model-agnostic feature ranking
  - Lightweight local estimators replace GPU-bound retraining
  - Practical production workflow for feature selection
  - 2 CPU-hour turnaround for 475 features

---

## Sequential Modeling

### 11. Generative Sequential Recommendation with Topology-Preserving Tokenization

*(Referenced in Distill AI feed, Jul 2026)*

- **Key Context:** Addresses topology distortion in item tokenization for autoregressive generative recommendation, where indexing semantics are disrupted by tokenization methods.

---

## LLMs / AI

### 12. GEAR: Copy Less, Ground More — Overcoming Repetitive Copying in Long-Context Reasoning

- **Authors:** Not specified in detail
- **arXiv:** Referenced in arXiv TLDR weekly (Jul 26, 2026)
- **Abstract:** Identifies "repetitive copying" as a critical failure mode in long-context LLMs that worsens with context length. Proposes GEAR, a reward shaping method using grounding rewards for key evidence and penalties for irrelevant context, with evidence-aware reinforcement learning.
- **Key Innovations:**
  - Identification of repetitive copying failure mode
  - Evidence-aware RL reward shaping
  - Automated pipeline for evidence-annotated training data

---

### 13. RAGAL: A Frugal, Fully Local RAG Assistant for Government Tech Support

- **Authors:** Not specified in detail
- **arXiv:** Referenced in arXiv TLDR weekly (Jul 26, 2026)
- **Abstract:** Fully local RAG assistant for government tech support. Hybrid retrieval with intent routing raised evaluation from 62% to 81%. Fine-tuned bge-m3 embedder improved recall@10 from 0.663 to 0.850 in 72 minutes. Addresses data-locality constraints.
- **Key Innovations:**
  - Hybrid retrieval with intent routing
  - Local fine-tuning of embedder for domain adaptation
  - Fully local deployment for data-sensitive environments

---

### 14. SciCodePile: 128GB Corpus and Benchmark for Scientific Code Generation

- **Authors:** Not specified in detail
- **arXiv:** Referenced in arXiv TLDR weekly (Jul 26, 2026)
- **Abstract:** 128GB scientific code corpus from 37,737 repositories. Executable benchmark of 200 tasks with sandboxed environments. Evaluates 15 LLMs showing scientific code generation is highly challenging (12.30% Pass@1 on executable tasks).
- **Key Innovations:**
  - Large-scale scientific code corpus
  - Executable benchmark with automated testing
  - Reveals significant gap in LLM scientific code capabilities

---

### 15. Augmenting Game AI with Deep Reinforcement Learning

- **Authors:** Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén
- **Affiliation:** Electronic Arts (EA), Stockholm, Sweden
- **arXiv:** [2606.20210](https://arxiv.org/abs/2606.20210) (Jun 18, 2026) — Conference on Games 2026
- **Abstract:** Vision paper surveying RL for game AI. Argues believability (not optimality) is the hard problem — agents that play perfectly feel inhuman. Proposes a framework for training RL models with game-AI-specific requirements. Identifies sample efficiency as the key bottleneck. Presents genre-level readiness framework for game studios.
- **Key Innovations:**
  - Framework for RL-based game AI with deployment requirements
  - Genre-level readiness assessment
  - Addresses believability vs optimality tension
  - Real deployment examples from EA games

---

## Weekly Top Papers (arXiv TLDR, Jul 20-26, 2026)

| # | Title | Category | One-Line Summary |
|---|-------|----------|-----------------|
| 1 | UAV-DualCog | cs.CV | Dual-cognition benchmark for MLLM spatio-temporal reasoning in UAV scenarios |
| 2 | MeetingToM | cs.CL | Benchmark for MLLM Theory-of-Mind in multi-party meetings |
| 3 | Appearance Pointers | cs.CV | Region-aware multimodal control in Diffusion Transformers without retraining |
| 4 | HumorSafe | cs.CR | Safety risks in LLM-driven content humorization |
| 5 | Agentic Real2Sim | cs.RO | Vision-language agents for real-world to physics simulation conversion |
| 6 | MV-Bench | cs.CV | Benchmark for multi-view interface construction by MLLMs |
| 7 | Salience Induction | cs.CR | Attack on Multi-Hop RAG agents via fact presentation manipulation |
| 8 | SciCodePile | cs.SE | 128GB scientific code corpus; 12.30% Pass@1 on executable tasks |
| 9 | GEAR | cs.CL | Evidence-aware RL to reduce repetitive copying in long-context reasoning |
| 10 | RAGAL | cs.IR | Fully local RAG assistant with hybrid retrieval reaching 81% accuracy |

---

## Trends & Observations

1. **Generative Recommendation is Maturing:** Diffusion-based (DLMRec) and autoregressive approaches are converging; topology-preserving tokenization and curriculum training are key challenges.

2. **LLM-Agent for RecSys:** Multiple papers explore LLMs as planners/tool-selectors over traditional RecSys models (PRTA, general agent trend), avoiding LLM limitations in full-ranking.

3. **Practical Production Focus:** LO-FAR, UniRank, and PRL all emphasize deployability — CPU-only feature selection, reproducible benchmarks, and plug-and-play residual learning.

4. **Cold-Start & Reactivation:** DeltaGate (zero-observation reactivation) and sparse embeddings for cold items address real-world catalog challenges.

5. **Causal & Explainability:** PRL's causal Bayesian framework and spectral biclustering diagnostics show growing interest in interpretable, causally-grounded recommendation.

6. **Game AI + RL:** EA's vision paper highlights the believability gap and sample efficiency as core bottlenecks for RL in production games.

7. **RAG & Long-Context:** Frugal local RAG (RAGAL) and evidence-aware RL (GEAR) address practical deployment and reasoning quality.

---

*Generated: 2026-07-26 | Source: arXiv, Distill AI, arXiv TLDR*
