---
title: "arXiv Paper Check — AI & CTR (July 17, 2026)"
type: synthesis
created: 2026-07-17
updated: 2026-07-17
sources: [arxiv-search]
tags: [arxiv, ctr, recommendation, ai-agents, machine-learning, daily-digest]
---

# arXiv Paper Check — AI & CTR (July 17, 2026)

> Curated from ~204 cs.AI entries, ~143 cs.LG entries, and ~925 cs.IR/CTR results. Focus: papers submitted July 16–17, 2026.

## Summary

16 curated papers across 4 categories: CTR/Recommendation (5), AI Agents & Systems (4), Machine Learning (4), Advertising & Search (3).

---

## CTR Prediction & Recommendation

### 1. Long-History User Transformers for Real-Time Ad Ranking
- **arXiv**: [2607.14331](https://arxiv.org/abs/2607.14331) | **Category**: cs.IR
- **Authors**: Viacheslav Ovchinnikov, Georgii Smirnov, Nikolai Savushkin, Veronika Ivanova, Maksim Kuzin (Yandex)
- **Key Contribution**: Decouples history encoding from real-time inference — a high-capacity offline transformer asynchronously encodes full cross-surface interaction history into a cached representation, while a lightweight runtime model combines it with request context at serving time. Pre-trained with dual objective (feedback prediction + next-item prediction).
- **Results**: Recovers 72–80% of full-history quality. Production A/B: **+2.77% search ad ranking, +2.1% Yandex Ad Network, +2.26% revenue** — without latency increase.
- **Significance**: Practical resolution of the "long history vs. low latency" tension in production CTR. The offline-online decoupling pattern may become standard for large-scale ad systems.

### 2. TMallGS: Scaling Unified Feature and Sequence Modeling for Generative E-commerce Search
- **arXiv**: [2607.13398](https://arxiv.org/abs/2607.13398) | **Category**: cs.IR
- **Authors**: Zhentao Song, Yufeng Gao, Xing Fang et al. (Alibaba)
- **Key Contribution**: Proposes 5 components for unified Transformer search ranking: Hierarchical Distribution-Calibrated Tokenization (FSR+DCP), Field-Adaptive Gated Transformer (per-field QKV + noise-adaptive gating), Decoupled FiLM Late Fusion, Context-Aware Bias Net, and Error-Aware Progressive Training.
- **Results**: Improved training throughput and substantial gains in UCTCVR and GMV on Tmall Search.
- **Significance**: Continues the DLRM→Transformer transition with careful handling of feature heterogeneity. The all-in-tokenization approach is refined with distribution-calibrated projections.

### 3. Mitigating Early Training Collapse in CTR Models
- **arXiv**: [2607.09696](https://arxiv.org/abs/2607.09696) | **Category**: cs.LG cs.AI
- **Authors**: Ergun Biçici, Erkan Çetinyamaç
- **Key Contribution**: Analyzes sharp validation decline after epoch 1 in deep CTR models. Finding: controlling feature sparsity (removing highly sparse features, aggregating infrequent values) yields substantial improvement, while LR tuning provides only incremental gains.
- **Results**: Stabilizes training, extends useful learning beyond 1 epoch, improves offline metrics and online performance.
- **Significance**: Simple, practical diagnosis for a common but under-studied CTR training pathology.

### 4. Privacy Preserving Recommender Systems: Balancing Personalization with Privacy
- **arXiv**: [2607.13328](https://arxiv.org/abs/2607.13328) | **Category**: cs.CR cs.AI cs.LG
- **Authors**: Ranjeet K Jha, Venkata Suresh Gummadilli
- **Key Contribution**: Framework combining federated learning, differential privacy, cohort-level modeling, and privacy-aware agents. Evaluates matrix factorization, neural collaborative filtering, and GRU4Rec under varying privacy budgets.
- **Results**: Maintains competitive CTR/Precision/NDCG at ε≈5, demonstrating strong privacy with limited quality impact. Interactive Streamlit dashboard for visualization.
- **Significance**: Practical reference for GDPR/CCPA-compliant recommendation deployment.

### 5. Mutable Low-Rank Sketches for Retrain-Free Recommendation
- **arXiv**: [2607.15242](https://arxiv.org/abs/2607.15242) | **Category**: cs.LG
- **Authors**: Hector J. Garcia, Nick Clayton
- **Key Contribution**: Low-rank sketch method for recommendation that avoids full retraining — enables continual adaptation with mutable representations.
- **Significance**: Addresses the growing concern about retraining costs in large-scale recommendation systems.

---

## AI Agents & Systems

### 6. SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration
- **arXiv**: [2607.15257](https://arxiv.org/abs/2607.15257) | **Category**: cs.AI cs.IR
- **Authors**: Yuyao Zhang, Junjie Gao, Zhengxian Wu et al. (Renmin University)
- **Key Contribution**: Multi-agent collaboration framework for open-domain information seeking. Code: [github.com/antins-labs/SearchOS](https://github.com/antins-labs/SearchOS)
- **Significance**: Open-source agent system for search — relevant to Karpathy's "Agentic Engineering" and LLM-as-OS themes.

### 7. AutoSynthesis: An Agentic System for Automated Meta-Analysis
- **arXiv**: [2607.15247](https://arxiv.org/abs/2607.15247) | **Category**: cs.AI
- **Authors**: Moein Taherinezhad, Sebastian Maier, Gerardo Vitagliano, Francesco Pierri, Stefan Feuerriegel
- **Key Contribution**: End-to-end agentic system that automates meta-analysis — from literature search to statistical synthesis.
- **Significance**: Demonstrates "autoresearch" pattern (cf. Karpathy's autoresearch concept) applied to scientific methodology.

### 8. Proof-or-Stop: Loop Engineering for Verifiable Evidence-Gated Lifecycle Control
- **arXiv**: [2607.14890](https://arxiv.org/abs/2607.14890) | **Category**: cs.AI cs.SE
- **Authors**: Jek Huang, Jeffery Hsia, Jiayi Sun et al.
- **Key Contribution**: Evidence-gated lifecycle control for agents — "don't trust the agent, trust the evidence." 48-page comprehensive framework for verifiable agent behavior.
- **Significance**: Addresses agent trust/verification gap — aligns with Karpathy's emphasis on verifiability and Software 3.0 principles.

### 9. Are LLM-Generated GPU Kernels Production-Ready? A Trace-Driven Benchmark
- **arXiv**: [2607.14541](https://arxiv.org/abs/2607.14541) | **Category**: cs.AI
- **Authors**: Lingyun Yang, Yuxiao Wang et al. (Alibaba)
- **Key Contribution**: Trace-driven benchmark (Atrex-Bench) + optimization agent (Atrex-Kernel-Agent) for LLM-generated GPU kernels. Open source.
- **Results**: Comprehensive evaluation of whether LLM-generated CUDA kernels meet production standards.
- **Significance**: Directly relevant to Karpathy's llm.c work and the "agentic coding for systems" theme.

---

## Machine Learning

### 10. PolyQ: End-to-End Quantization Framework for Scalable Edge CPU LLM Inference
- **arXiv**: [2607.14618](https://arxiv.org/abs/2607.14618) | **Category**: cs.LG cs.AR cs.OS
- **Authors**: Hyunwoo Oh, Suyeon Jang, Hanning Chen et al.
- **Key Contribution**: Codesign end-to-end quantization framework for edge CPU LLM inference. Accepted at ICCAD 2026.
- **Significance**: Edge deployment aligns with the on-device AI trend (cf. Apple AFM, Phi-4 on-device).

### 11. xHC: Expanded Hyper-Connections
- **arXiv**: [2607.14530](https://arxiv.org/abs/2607.14530) | **Category**: cs.LG cs.CL
- **Authors**: Xiangdong Zhang, Xiaohan Qin et al.
- **Key Contribution**: Expanded Hyper-Connections architecture — technical report with code.
- **Significance**: Novel architectural building block for transformer scaling.

### 12. Muse: Representation Geometry of Muon Beyond Normalized Momentum
- **arXiv**: [2607.14536](https://arxiv.org/abs/2607.14536) | **Category**: cs.LG
- **Authors**: Da Chang, Qiankun Shi et al.
- **Key Contribution**: Analyzes the Muon optimizer's representation geometry beyond the normalized momentum view.
- **Significance**: Deepens understanding of Muon, which has gained significant adoption (cf. Karpathy's modded-nanogpt, ICLR 2026 Honorable Mention for Muon).

### 13. Long-Context Fine-Tuning with Limited VRAM
- **arXiv**: [2607.15105](https://arxiv.org/abs/2607.15105) | **Category**: cs.AI
- **Authors**: Vladimir Fedosov, Aleksandr Sazhin et al.
- **Key Contribution**: Techniques for fine-tuning long-context models when VRAM is limited.
- **Significance**: Practical engineering for the long-context era (10M+ token models now common).

---

## Advertising & Search

### 14. Adaptive Ad Load Design for Sponsored Search Markets
- **arXiv**: [2607.14418](https://arxiv.org/abs/2607.14418) | **Category**: cs.LG econ.GN
- **Authors**: Mohammad Rashid, Hema Yoganarasimhan
- **Key Contribution**: Evidence, theory, and deployment of adaptive ad load design — how many ads to show per page in sponsored search.
- **Significance**: Bridges economic theory with ML systems — the ad load problem is often overlooked but has massive revenue impact.

### 15. ToolRec: Calibrated Preference Alignment for Query Recommendation in On-Device Assistants
- **arXiv**: [2607.08466](https://arxiv.org/abs/2607.08466) | **Category**: cs.IR
- **Authors**: Zihan Luo, Lingkui Chen et al. (OPPO)
- **Key Contribution**: Calibrated preference alignment for on-device query recommendation, integrating system tools (SysToolKit, 708 tools). Uses dual-level calibration to mitigate user behavioral noise.
- **Results**: Online A/B on OPPO Xiaobu (150M+ MAU): significant CTR and click volume improvements.
- **Significance**: On-device LLM recommendation with tool integration — relevant to "Build for Agents" and LLM GUI themes.

### 16. Position Auctions with a Capacity Constraint
- **arXiv**: [2607.12040](https://arxiv.org/abs/2607.12040) | **Category**: cs.GT
- **Authors**: Eleni Batziou, Georgios Birmpas et al.
- **Key Contribution**: First truthful constant-approximation mechanism for capacity-constrained position auctions with heterogeneous ad sizes. Algorithmic technique with density-based ordering + capacity-aware local improvements.
- **Significance**: Novel auction theory result applicable to modern ad formats where ad sizes vary.

---

## Key Themes

1. **Offline-Online Decoupling for CTR**: Long-History User Transformers demonstrate that async offline encoding + cached representations can capture 72-80% of full-history quality at zero latency cost — a pattern that may generalize.

2. **Unified Transformer Ranking**: TMallGS continues the trend of replacing DLRM with unified Transformer architectures, adding distribution-calibrated tokenization to handle feature heterogeneity.

3. **Simplicity Wins in CTR**: Mitigating Early Training Collapse shows that sparsity control > LR tuning — simple feature engineering outperforms optimization tricks.

4. **Autoresearch Goes Production**: AutoSynthesis and SearchOS-V1 demonstrate agentic meta-analysis and search at scale.

5. **Agent Verifiability**: Proof-or-Stop and the GPU kernel benchmark (Atrex) both address the trust/verification gap in AI systems — directly aligned with Karpathy's "verifiability" and "Software 3.0" themes.

6. **Muon Optimizer Deepened**: Muse provides geometric analysis of Muon, which is becoming a standard optimizer in the post-Adam era.
