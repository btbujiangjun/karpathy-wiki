---
title: arXiv Digest — AI & CTR (June 4, 2026)
type: synthesis
created: 2026-06-04
updated: 2026-06-04
sources: []
tags: [arxiv, paper-review, ctr, recommendation, ai, llm, transformers, memory, agents, scaling]
---

# arXiv Digest — AI & CTR (June 4, 2026)

Scan of cs.LG (236 entries), cs.IR (27 entries), and cs.AI (207 entries) from Thu 4 Jun 2026.

---

## CTR / Recommendation / Ranking

| Paper | Authors | Venue | Key Contribution |
|-------|---------|-------|-----------------|
| **Dual-Stream MLP is All You Need for CTR Prediction** (2606.04944) | Ou, Tian, Zhao, Zhang, Chen, Wen | TKDD | DS-MLP: knowledge distillation consolidates explicit feature interaction learning into a main MLP; a parallel MLP captures implicit interactions. Vanilla MLP achieves SOTA on 3 benchmarks. Scalable and efficient — challenges the necessity of complex architectures. |
| **SAILRec: Steering LLM Attention to Dual-Side Semantically Aligned Collaborative Embeddings** (2606.04514) | Wu, Wang, Wang et al. | — | LLM-based recommender. Attention diagnostics reveal collaborative embedding utilization is depth-dependent & alignment-sensitive. Dual-side alignment (item with item-text, user with codebook profiles) + hierarchical attention steering (suppress shallow-layer interference, strengthen deep-layer evidence). |
| **BEATS: Bootstrapping E-commerce Attribute Taxonomies for Search** (2606.04909) | Shih, Su, Ho et al. | SIGIR 2026 Industry | Iterative human-AI collaboration to bootstrap e-commerce attribute taxonomies — practical contribution for product search infrastructure. |
| **EviRank: Evidence-Based Confidence Estimation for LLM-Based Ranking** (2606.04727) | Yan, Xv, Wang et al. | — | Estimates ranking confidence from evidence, addressing LLM ranker calibration. |
| **Bridging Short Videos and Live Streams: Reasoning-Guided Multimodal LLMs** (2606.04448) | Zhang, Zhu, Wang et al. (Kuaishou, Kun Gai) | — | Cross-domain representation learning for short video & live streams via reasoning-guided MLLMs. |
| **Beyond Retrieval: Learning Compact User Representations for Scalable LLM Personalization** (2606.04547) | Cao, Zhang, Yao et al. | — | Compact user representations to avoid expensive retrieval at inference time for LLM personalization. |
| **Trading Engagement for Sustainability: Carbon-Aware Re-ranking** (2606.04550) | Syrdal, Vestrum, Bergh | — | Novel paradigm: re-ranking with explicit carbon footprint optimization vs. engagement. |
| **DSIRM: Learning Query-Bridged Discrete Semantic Identifiers for E-commerce Relevance** (2606.04374) | Wang, Fang, Jin et al. | — | Query-bridged discrete semantic IDs for e-commerce relevance modeling. |
| **Distributional ANN Search for Uncertainty-Aware Retrieval** (2606.04603) | Jeunen | — | Reformulates ANN search as distributional — returns uncertainty estimates alongside neighbors. |
| **Rethinking Sales Lead Scoring with LLM-based Hierarchical Preference Ranking** (2606.04387) | Zhang, Liu, Sun et al. | — | LLMs for hierarchical preference ranking in B2B lead scoring. |

## AI / LLM Systems & Theory

| Paper | Authors | Venue | Key Contribution |
|-------|---------|-------|-----------------|
| **STRIDE: Training Data Attribution via Sparse Recovery** (2606.05165) | Dagli, Harrasse, Zhang, Draye, Abdullah, Schölkopf, Jin | — | TDA in activation space (not parameter space). Formulated as sparse recovery (compressive sensing). Learns lightweight "steering operators" mimicking training subset effects. **13× faster** than prior art; SOTA for LLM pre-training attribution. Applications in data selection, contamination detection. |
| **Neuron Populations Exhibit Divergent Selectivity with Scale** (2606.03990) | Dravid, Bahri, Efros, Gandelsman | — | Scaling law for neuron-level structure: Rosetta Neurons follow **sublinear power law** (grow in number, shrink as fraction of total). **Neuron Polarization Effect**: Rosetta Neurons become more monosemantic with scale while non-Rosetta population grows less selective. Analytical model balancing feature utility vs. capacity explains both effects. Studied in LMs up to 30B and vision models up to 5B. |
| **AutoLab: Long-Horizon Auto Research & Engineering Benchmark** (2606.05080) | Xu, Chen, Huang et al. (MIT, 19 authors) | — | 36 expert-curated tasks across system optimization, puzzles, model development, CUDA kernels. Key finding: **persistence > initial attempt quality**. claude-opus-4.6 leads; most frontier models terminate prematurely. Open-source benchmark & harness. |
| **Scaling Self-Evolving Agents via Parametric Memory (TMEM)** (2606.04536) | Ren, Luo, Yang et al. | — | Agents compress history into fast LoRA weights $\Delta_t$ via online updates within a single episode — genuinely alters future behavior. RL-optimizable extraction policy. SVD-based LoRA initialization accelerates online convergence. Outperforms summary/retrieval baselines on LoCoMo, LongMemEval-S, multi-objective search. |
| **Sequential Data Poisoning in LLM Post-Training** (2606.04929) | Sanderson, Wang, Lu, Kamath, Lu | — | **"Single-attacker illusion"**: each adversary alone appears negligible, but cross-stage (SFT→DPO / SFT→PPO) collaboration reveals compound vulnerabilities. Additive in SFT→DPO, complementary in SFT→PPO. Security analysis of individual stages systematically underestimates risk. |
| **FLAGG: Flexible Autoregressive Graph Generation** (2606.05067) | Cognolato, Sperduti, Serafini | JMLR | Framework making one-shot graph models autoregressive via stochastic node removal/insertion. Outperforms both pure one-shot and pure sequential baselines across graph sizes and domains. |
| **AlphaQ: Calibration-Free Bit Allocation for MoE Quantization** (2606.04980) | Yang, Ma, Conzelmann et al. | — | Quantization for Mixture-of-Experts models without calibration data — important for deploying large MoE models. |
| **STaR-Quant: State-Time Consistent PTQ for Diffusion LLMs** (2606.04945) | Yan, Wang, Wan et al. | — | Post-training quantization for diffusion-based LLMs (e.g., LLaDA) preserving state-time consistency. |
| **AdaKoop: Efficient Koopman Operator Regression from Nonstationary Data** (2606.04930) | Chihara, Fujiwara, Matsubara, Sakurai | KDD 2026 | Online Koopman operator learning from nonstationary streams. |
| **Beyond Structural Symmetries: Linear Mode Connectivity via Neuron Identifiability** (2606.04754) | Bürgin, Herbst, Lin, Jegelka | ICML 2026 | Connects neuron identifiability to linear mode connectivity — explains why independently trained models can be linearly interpolated. |
| **Validity Threats for Foundation Model Research** (2606.05029) | König, Pawelczyk, von Luxburg, Bordt | — | Structured catalog of validity threats in FM research — methodological contribution for improving experimental rigor. |
| **Failed Reasoning Traces Tell You What Is Fixable** (2606.05145) | Islah, Abbes, Rish, Chandar, Muller | — | Analyzes failed CoT traces to predict fixability. Counterintuitive: traces reveal fixability but not how to fix. |
| **Data Attribution in LLMs via Bidirectional Gradient Optimization** (2606.04928) | Berdoz, Lanzendörfer, Bayraktar, Wattenhofer | AAAI 2026 AIGOV | Bidirectional gradient-based TDA for LLMs. |
| **Reinforcement Learning from Rich Feedback with Distributional DAgger** (2606.05152) | Agrawal, Fein-Ashley, Rashidinejad | — | Extends DAgger to rich (non-binary) feedback for RL. |
| **Graph Cascades: Contagion-Based Mesoscopic Rewiring** (2606.05046) | Chaitanya, Le, Ruiz | — | Novel structure-aware graph learning via contagion dynamics. |

## IR / RAG / Retrieval

| Paper | Authors | Venue | Key Contribution |
|-------|---------|-------|-----------------|
| **LLM Knowledge Distillation for Conversational Search** (2606.04650) | Fris, Hutter, Bertrand et al. | SCAI@SIGIR '26 | Efficiency/effectiveness analysis of distilling LLMs for conversational search. |
| **Argus-Retriever: Vision-LLM Late-Interaction Retrieval** (2606.04300) | Abdallah, Abdalla, Ali, Jatowt | — | Region-aware query-conditioned MoE for visual document retrieval with late interaction. |
| **CHARM: Cascading Hallucination in Agentic RAG** (2606.04435) | Mishra | — | Detection and mitigation framework for cascading hallucination in multi-step RAG agents. |
| **Cartridges at Scale: Training Modular KV Caches** (2606.04557) | Hardalov, Iglesias, de Gispert | — | Modular KV caches trained over large doc collections for efficient long-context retrieval. |
| **Cost-Aware Query Routing in RAG** (2606.02581) | Mishra | — | Depth-cost tradeoff analysis for RAG routing strategies. |

## Key Themes

1. **CTR architecture simplification** — DS-MLP shows a vanilla MLP with knowledge distillation can match complex interaction architectures. A counterpoint to the scaling/transformer trend in CTR.

2. **LLM × Recommendation convergence continues** — SAILRec (attention steering), BEATS (human-AI taxonomy bootstrapping), Bridging Short Videos & Live Streams (MLLMs). The LLM4Rec pipeline is maturing with deeper architectural integration.

3. **Training data attribution (TDA) comes of age** — STRIDE achieves practical speeds (13× faster) for LLM attribution. Bidirectional gradient TDA also appears. This is becoming a practical tool.

4. **Neuron-level scaling laws** — Dravid et al. extend scaling laws below loss to individual neuron behavior. Rosetta Neurons' polarization (more monosemantic at scale) is a concrete prediction for interpretability.

5. **Self-evolving agents** — TMEM's parametric memory (online LoRA updates) and AutoLab's persistence benchmark both point toward agents that learn continuously rather than relying purely on context.

6. **Compound security vulnerabilities** — "Single-attacker illusion" in sequential poisoning shows that cross-stage security analysis is necessary for LLM post-training pipelines.

7. **Sustainability in recommendation** — Carbon-aware re-ranking (Syrdal et al.) introduces environmental optimization as a first-class objective in ranking.
