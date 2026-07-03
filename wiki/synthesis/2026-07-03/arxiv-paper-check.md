---
title: arXiv Paper Check — AI & CTR (July 3, 2026)
type: synthesis
created: 2026-07-03
updated: 2026-07-03
sources: [arxiv.org]
tags: [arxiv, ai, ctr, recommender-systems, llm, personalization]
---

# arXiv Paper Check — AI & CTR (July 3, 2026)

Scanned new listings for Friday, July 3, 2026. **cs.AI: 353 total (86 new), cs.IR: 23 total (8 new), cs.LG: 273 total (101 new).**

---

## AI Highlights

### 1. Epistemic Goggles: Gradient Editing for Epistemic Framing
- **arXiv**: 2607.01690
- **Key contribution**: A learned module that edits gradients during SFT to impart an epistemic frame (e.g., "this is fictional"). Trained once for a given base model + LoRA config, then applied frozen to unseen documents. Models treat content as fictional ~91% of the time (vs 9% without), while preserving capability on GPQA/TruthfulQA. Supports other frames (e.g., "this is an AI safety eval"). Frame persists under continued fine-tuning.
- **Significance**: Path toward training on known-misaligned data without absorbing demonstrated behaviors. Addresses Negation Neglect in a principled way.

### 2. Procedural Memory Distillation (PMD): Self-Improving LLMs
- **arXiv**: 2607.01480
- **Authors**: Ye Liu, Srijan Bansal, Bo Pang et al.
- **Key contribution**: Converts cross-episode rollout signals into reusable procedural memory at three abstraction levels (raw trajectories, self-reflected strategies, recurring behavioral patterns). Memory-conditioned self-teacher supervises the student on its own rollouts. Co-evolution design: policy generates rollouts → updates memory → memory shapes supervision → updates policy.
- **Results**: Qwen3-8B, OLMo3-Instruct-7B: +3.8–5.5% on SCIKNOWEVAL, +7.9–13.6% on LIVECODEBENCH over SDPO. Freezing either memory or policy trails by >10%.
- **Significance**: First framework to systematically capture and reuse procedural knowledge across episodes in LLM post-training.

### 3. Scaling with Confidence: C3RL + CAS
- **arXiv**: 2607.01612
- **Authors**: Xuqing Yang, Yi Yuan et al.
- **Key contribution**: C3RL (Correctness and Confidence Calibration RL) — novel RL algorithm integrating correctness, calibration, and dataset-informed reference rewards. Produces well-calibrated verbalized confidence without sacrificing accuracy. CAS (Confidence-based Adaptive Test Time Scaling) — adjustable inference strategy allocating compute based on response confidence.
- **Results**: Outperforms SOTA on 8 text + multimodal datasets. CAS reduces inference budget by up to 12.33× while surpassing majority voting.
- **Significance**: Addresses the critical problem of LLMs being overconfident when uncertain. Practical for deployment where reliability matters.

### 4. Scaling Trends for Lie Detector Oversight (SOLiD) at 405B
- **arXiv**: 2607.01567
- **Authors**: Oskar J. Hollinsworth, Ann-Kathrin Dombrowski et al.
- **Key contribution**: Scales SOLiD (Scalable Oversight via Lie Detectors) to 405B models. Undetected deception drops from 34% (1B) to 14% (405B) at 99% detector TPR. Expensive human labelers can be removed entirely from fine-tuning without statistically significant increase in deception.
- **Limitation**: Sensitive to distribution shift between detector training and preference-training data (FPR can become impractical).
- **Significance**: Favorable scaling of automated oversight for large models.

### 5. Diverse Evidence, Better Forecasts (InfoDelphi)
- **arXiv**: 2607.01661
- **Authors**: Yuante Li, Yicheng Tao et al.
- **Key contribution**: Designed information asymmetry — partitioning evidence into shared public + disjoint private subsets so each agent holds exclusive knowledge. InfoDelphi: relevance-aware evidence routing, rationale-based iterative deliberation, confidence-weighted aggregation.
- **Results**: Outperforms strongest single-agent and multi-agent baselines by 12–18% Brier score, 4–8pp accuracy on PolyGym (375 binary forecasting questions). Removing asymmetry eliminates most deliberation gains.
- **Significance**: Identifies input diversity as key enabler of effective multi-agent reasoning, not deliberation per se.

### 6. Auto-FL-Research: Agentic Search for FL Algorithms
- **arXiv**: 2607.01366
- **Authors**: Holger R. Roth, Ziyue Xu et al. (NVIDIA)
- **Key contribution**: Coding-agent workflow for federated learning algorithmic recipe search. Agents propose/implement candidate training algorithms (server aggregation, client schedules, local objectives). Evaluated on 5 FLamby + 6 LEAF tasks. Gains on 4/5 FLamby and 5/6 LEAF profiles, but same-budget controls show some gains are from fixed-surface tuning.
- **Significance**: Exposes that agent-generated candidates must be carefully separated into repeated FL mechanisms vs tuning artifacts.

### 7. PACE: Neuro-Symbolic Counterfactual Explanations
- **arXiv**: 2607.01306
- **Key contribution**: Modular neuro-symbolic framework separating prediction (neural classifier) from reasoning (ASP-based symbolic layer enforcing domain constraints). Produces feasibility-aware counterfactuals consistent with domain knowledge.
- **Case study**: Adult Income dataset — symbolic constraints yield explanations satisfying domain-specific feasibility vs validity-only approaches.
- **Significance**: Practical bridge between deep learning and symbolic reasoning for XAI.

### 8. The Agentic Garden of Forking Paths
- **arXiv**: 2607.01507
- **Authors**: Jiacheng Miao, Jonathan K Pritchard, James Zou
- **Key contribution**: AI agents reproduce 72% of human ideological gap in reported effect estimates. 86% of AI analyses pass independent AI review, 78% pass human expert review. Introduces m-value (multiverse value) and Agentic Bootstrap to estimate the distribution of plausible analysis paths.
- **Significance**: AI agents can amplify the forking-paths problem in science by making selective exploration cheap and scalable. Proposes a statistical remedy (m-value).

---

## CTR / Recommender Systems / IR Highlights

### 9. MixFormer: Co-Scaling Up Dense and Sequence in Industrial Recommenders
- **arXiv**: 2602.14110 (v2, replaced Jul 2) — **Accepted KDD 2026**
- **Authors**: Xu Huang, Hao Zhang et al. (ByteDance)
- **Key contribution**: Unified Transformer architecture jointly modeling sequential behaviors + feature interactions in a single backbone. User-item decoupling for efficiency. Enables effective co-scaling of dense capacity and sequence length.
- **Results**: Deployed on Douyin and Douyin Lite — consistent improvements in active days and in-app usage duration.
- **Significance**: Breaks the fragmented design where sequence and feature interaction are separate modules. Practical co-scaling paradigm for industrial recommenders.

### 10. GR2: Generative Reasoning Re-Ranker
- **arXiv**: 2606.31984 (v2, replaced Jul 1)
- **Authors**: Yufei Li, Zaiwei Zhang et al. (large team)
- **Key contribution**: End-to-end generative re-ranking combining (i) mid-training on semantic IDs (≥99% uniqueness), (ii) reasoning-trace distillation from stronger teacher, (iii) RL with verifiable rewards for re-ranking, (iv) context compressor + On-Policy Distillation.
- **Results**: +18.7% R@1, +7.1% R@3, +9.6% N@3 over legacy baselines on industrial-scale traffic. Critical finding: reward hacking is a real issue — LLMs preserve incoming order or exploit position bias, motivating conditional verifiable rewards.
- **Significance**: Addresses 3 industrial gaps for LLMs in recommendation re-ranking (most efforts target retrieval/ranking, not re-ranking).

### 11. CoPersona: Collaborative Persona Graphs for Robust LLM Personalization
- **arXiv**: 2607.01485 — **Accepted KDD '26**
- **Authors**: Yangtian Zhang, Leyao Wang et al.
- **Key contribution**: Graph-based collaborative personalization completing sparse user profiles by borrowing signals from behaviorally similar peers. Decomposes histories into facet-level representations with multiplex persona graph. Dual-branch architecture: non-parametric peer retrieval + parametric graph reasoning.
- **Significance**: Addresses sparse/skewed user histories — the fundamental bottleneck in real-world LLM personalization.

### 12. Bi-NAS: Bi-Level NAS for Recommender Explanations
- **arXiv**: 2607.01387
- **Authors**: Longfeng Wu, Yao Zhou et al.
- **Key contribution**: Bi-level NAS optimizing cross-attention + feature interaction for explanation generation. LLM zero-shot prompting for personalized justifications. Aligns user feature preferences with item quality scores.
- **Results**: Improves both recommendation accuracy AND explanation effectiveness on 4 real-world datasets.
- **Significance**: First NAS-based approach for explanation quality in RecSys.

### 13. IntentTune: Resolving Ambiguous Query Intents for E-Commerce Search
- **arXiv**: 2607.01530
- **Authors**: Rachith Aiyappa, Ishita Khan et al.
- **Key contribution**: Framework resolving under-specified queries ("watch", "shirt") by leveraging user-specific behavioral signals (search history, browsing, profile) vs population-level demand patterns. Finding: population patterns alone are insufficient; user-specific signals (especially prior search queries) outperform both population stats and static profiles.
- **Significance**: Practical insight for e-commerce search intent detection — personalization history beats aggregated demand.

### 14. Planning over Matrix-Factorization MDPs for Candidate Generation
- **arXiv**: 2607.02115 — **KDD 2026 Workshop**
- **Authors**: Mikhail Trapeznikov, Maksim Utushkin
- **Key contribution**: Casts top-K retrieval as MDP over implicit-ALS posterior. Single-step lookahead captures most of the gain. Lightweight planning layer turns static scoring into short decision-making without retraining.
- **Results**: Dynamics-aware planning overcomes static retrieval on all datasets.
- **Significance**: Minimal (one-step) planning already improves fixed CF embeddings — practical for deployment.

---

## Key Themes

1. **LLM self-improvement via procedural memory** (PMD) — moving beyond per-episode RLVR signals
2. **Confidence calibration as first-class RL objective** (C3RL + CAS) — cheaper inference through calibrated abstention
3. **Collaborative personalization for sparse user profiles** (CoPersona, IntentTune) — graph-based peer borrowing
4. **Generative re-ranking with RL** (GR2, MixFormer) — LLMs moving into the re-ranking stage of industrial RecSys
5. **Information asymmetry in multi-agent systems** (InfoDelphi) — evidence diversity as the key lever
6. **Gradient editing for epistemic control** (Epistemic Goggles) — training on misaligned data without absorbing behaviors
