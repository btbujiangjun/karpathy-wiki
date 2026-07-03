---
title: "arXiv Daily — 2026-07-03"
type: synthesis
created: 2026-07-03
updated: 2026-07-03
tags: [arxiv, daily, LLM, recommendation, CTR, games, RL, sequential-modeling, advertising]
---

# arXiv Daily Report — 2026-07-03

Curated recent papers from arXiv spanning AI, LLMs, recommendation, CTR, advertising, sequential modeling, reinforcement learning, and games.

---

## LLMs & Alignment

### 1. Constructive Alignment: Governing Preference Dynamics in Human-AI Interaction
- **Authors**: Max Kanwal, Caryn Tran
- **Affiliation**: — (AAAI-26 Workshop on Machine Ethics)
- **Date**: 2026-07-02 (arXiv:2607.00001)
- **Abstract**: Proposes a paradigm shift where AI alignment treats human preferences as dynamic, evolving state variables rather than static targets. Uses a control-theoretic framework to model how AI systems shape preference trajectories, arguing alignment should govern long-term value formation.
- **Key Innovation**: Frames alignment as a control problem over evolving human preference dynamics rather than static satisfaction.
- **Link**: [https://arxiv.org/abs/2607.00001](https://arxiv.org/abs/2607.00001)

### 2. A Penny for Your Prompts: Experiments Detecting and Mitigating LLM Usage by Survey Respondents
- **Authors**: —
- **Affiliation**: —
- **Date**: 2026-07-01 (arXiv:2607.00403)
- **Abstract**: Introduces detection methods and mitigation strategies for LLM-generated survey responses, including prompt-based watermarking and response pattern analysis.
- **Key Innovation**: Establishes a baseline for detecting AI-generated human-subject data in surveys.
- **Link**: [https://arxiv.org/abs/2607.00403](https://arxiv.org/abs/2607.00403)

### 3. Positive Alignment: Artificial Intelligence for Human Flourishing
- **Authors**:多位作者 (M. Kringelbach, A. Elwood, D. Ford, F. Rosas, M. Bohacek et al.)
- **Affiliation**: —
- **Date**: 2026-05-11 (arXiv:2605.10310)
- **Abstract**: Argues that alignment research should move beyond safety/harm prevention toward "positive alignment" — AI systems that actively support human and ecological flourishing, while remaining safe.
- **Key Innovation**: Proposes a Positive Alignment agenda parallel to conventional safety alignment.
- **Link**: [https://arxiv.org/abs/2605.10310](https://arxiv.org/abs/2605.10310)

### 4. Beyond the Black Box: A Survey on the Theory and Mechanism of Large Language Models
- **Authors**: Zeyu Gan, Ruifeng Ren, Wei Yao et al.
- **Affiliation**: —
- **Date**: 2026-01-06 (arXiv:2601.02907)
- **Abstract**: Comprehensive survey proposing a lifecycle-based taxonomy (Data Preparation → Model Preparation → Training → Alignment → Inference → Evaluation) and analyzing theoretical foundations of LLMs.
- **Key Innovation**: Unified lifecycle taxonomy; identifies frontier challenges like synthetic data limits, safety guarantees bounds, and mechanistic origins of emergent intelligence.
- **Link**: [https://arxiv.org/abs/2601.02907](https://arxiv.org/abs/2601.02907)

### 5. The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity?
- **Authors**: Alexander Hägele et al.
- **Affiliation**: — (ICLR 2026)
- **Date**: 2026-01-30 (arXiv:2601.23045)
- **Abstract**: Empirical study showing misalignment scales unpredictably — more capable models show more "hot mess" (noisy, unpredictable misbehavior) rather than coherent misaligned goals.
- **Key Innovation**: Suggests reward hacking/goal misspecification research is relatively more important than deception-focused alignment.
- **Link**: [https://arxiv.org/abs/2601.23045](https://arxiv.org/abs/2601.23045)

---

## CTR Prediction & Advertising

### 6. Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Affiliation**: Renmin University of China
- **Date**: 2026-06-03 (arXiv:2606.04944)
- **Abstract**: Proposes DS-MLP, a dual-stream MLP framework for CTR that uses knowledge distillation to consolidate explicit feature interaction learning into a main MLP, while a parallel MLP captures implicit interactions.
- **Key Innovation**: Teacher-agnostic distillation makes it compatible with any future SOTA CTR model as teacher.
- **Link**: [https://arxiv.org/abs/2606.04944](https://arxiv.org/abs/2606.04944)

### 7. EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling
- **Authors**: Mingyang Liu, Yong Bai, Zhangming Chan et al. (Taobao & Tmall Group, Alibaba)
- **Affiliation**: Alibaba
- **Date**: 2026-02-11 (arXiv:2602.10811)
- **Abstract**: Proposes Efficiently Scalable Transformer (EST) that processes all raw inputs in a single sequence without lossy aggregation. Integrates Lightweight Cross-Attention (LCA) and Content Sparse Attention (CSA).
- **Key Innovation**: Demonstrates stable power-law scaling relationship in CTR prediction, enabling predictable performance gains with model scale.
- **Link**: [https://arxiv.org/abs/2602.10811](https://arxiv.org/abs/2602.10811)

### 8. IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs
- **Authors**: Yubin Zhang, Haiming Xu, Guillaume Salha-Galvan et al.
- **Affiliation**: Xiaohongshu
- **Date**: 2026-03-02 (arXiv:2603.01590)
- **Abstract**: Uses MLLMs to generate proxy embeddings from content signals for cold-start items. Proxy embeddings are aligned with existing ID embedding space and optimized end-to-end under CTR objectives.
- **Key Innovation**: Deployed in production at Xiaohongshu serving hundreds of millions of users daily.
- **Link**: [https://arxiv.org/abs/2603.01590](https://arxiv.org/abs/2603.01590)

### 9. RIA: A Ranking-Infused Approach for Optimized Listwise CTR Prediction
- **Authors**: —
- **Affiliation**: Meituan
- **Date**: 2025-11-27 (arXiv:2511.21394)
- **Abstract**: Unified framework for end-to-end listwise CTR prediction integrating ranking and reranking. Deployed in Meituan's ad system.
- **Key Innovation**: +1.69% CTR and +4.54% CPM improvements in online A/B tests at Meituan.
- **Link**: [https://arxiv.org/abs/2511.21394](https://arxiv.org/abs/2511.21394)

---

## Recommendation & Sequential Modeling

### 10. POEM: Partial-Order Enhanced Real-Time Sequential Modeling for Recommendation
- **Authors**: —
- **Affiliation**: —
- **Date**: 2026-06-30 (arXiv:2606.29946)
- **Abstract**: Addresses real-time recommendation by capturing partial-order signals hidden within multi-stage ranking pipelines, going beyond static historical click sequences.
- **Key Innovation**: Models structured signals from industrial multi-stage ranking pipelines for real-time sequential recommendation.
- **Link**: [https://arxiv.org/abs/2606.29946](https://arxiv.org/abs/2606.29946)

### 11. Diffusion-GR2: Diffusion Generative Reasoning Re-ranker
- **Authors**: —
- **Affiliation**: —
- **Date**: 2026-07-02 (arXiv:2607.01170)
- **Abstract**: Uses block-diffusion language models for generative reasoning in recommendation reranking, decoding many positions in parallel rather than autoregressively.
- **Key Innovation**: Block-diffusion approach reduces inference cost of chain-of-thought reasoning for ranking.
- **Link**: [https://arxiv.org/abs/2607.01170](https://arxiv.org/abs/2607.01170)

### 12. LUMOS: LLM-Driven Federated Sequential Recommendation
- **Authors**: T.M.C. Nguyen et al.
- **Affiliation**: —
- **Date**: 2026-02-10 (arXiv:2602.09306)
- **Abstract**: Uses on-device LLMs to generate three complementary sequence variants (future-oriented, semantically equivalent, preference-inconsistent) and jointly encodes them via tri-view contrastive optimization in federated setting.
- **Key Innovation**: Privacy-preserving sequential recommendation via LLM-driven semantic data augmentation in federated learning.
- **Link**: [https://arxiv.org/abs/2602.09306](https://arxiv.org/abs/2602.09306)

### 13. HoloMambaRec: Scalable Sequential Recommendation under Latency and Memory Constraints
- **Authors**: Adithya Parthasarathy et al.
- **Affiliation**: —
- **Date**: 2026-01-13 (arXiv:2601.08360)
- **Abstract**: Combines holographic reduced representations for attribute-aware embedding with a selective state space encoder (Mamba-style) for linear-time sequence processing.
- **Key Innovation**: Constant-time recurrent inference via Mamba-style backbone for long-horizon sequential recommendation.
- **Link**: [https://arxiv.org/abs/2601.08360](https://arxiv.org/abs/2601.08360)

### 14. MuSTRec: Multimodal Enhancement of Sequential Recommendation
- **Authors**: Bucher Sahyouni, Matthew Vowels, Liqun Chen, Simon Hadfield
- **Affiliation**: —
- **Date**: 2026-02-06 (arXiv:2602.07207)
- **Abstract**: Unifies multimodal and sequential recommendation by building item-item graphs from text and visual features, with frequency-based self-attention capturing short/long-term preferences.
- **Key Innovation**: Up to 33.5% improvement over multimodal and sequential SOTA baselines.
- **Link**: [https://arxiv.org/abs/2602.07207](https://arxiv.org/abs/2602.07207)

---

## Reinforcement Learning & Games

### 15. SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: Bo Liu, Leon Guertler, Simon Yu, Zichen Liu et al.
- **Affiliation**: —
- **Date**: 2025-06 (v3: 2026-03-02, arXiv:2506.24119)
- **Abstract**: Self-play framework where LLMs learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) against continuously improving versions of themselves. Introduces role-conditioned advantage estimation (RAE).
- **Key Innovation**: Up to 10% improvement across 8 reasoning benchmarks. Benefits even models already trained with RLVR (e.g., DeepSeek-R1-Distill-Qwen-7B).
- **Link**: [https://arxiv.org/abs/2506.24119](https://arxiv.org/abs/2506.24119)

### 16. CART: Conservative Adversarially Robust Decision Transformer
- **Authors**: Xiaohang Tang, Zhuowen Cheng, Satyabrat Kumar
- **Affiliation**: UCL / Independent
- **Date**: 2025-10-13 (arXiv:2510.11877)
- **Abstract**: First framework to enhance robustness of Decision Transformers in adversarial stochastic games. Conditions Transformer policies on NashQ values derived from stage games for adversarial robustness.
- **Key Innovation**: Combines sequence modeling (Decision Transformer) with game-theoretic robustness (NashQ conditioning).
- **Link**: [https://arxiv.org/abs/2510.11877](https://arxiv.org/abs/2510.11877)

### 17. Coachable Agents for Interactive Gameplay
- **Authors**: —
- **Affiliation**: Google DeepMind (Gran Turismo 7, Horizon Forbidden West)
- **Date**: 2026-07 (arXiv:2607.00642)
- **Abstract**: Framework for training RL agents that can be "coached" at runtime — controlling style as well as task completion — demonstrated in AAA video games GT7 and HFW.
- **Key Innovation**: Coachable agents with style control in commercial AAA games; goes beyond optimality to believability.
- **Link**: [https://arxiv.org/abs/2607.00642](https://arxiv.org/abs/2607.00642)

### 18. GameCraft-Bench: Can Agents Build Playable Games End-to-End in a Real Game Engine?
- **Authors**: Tongxu Luo, Rongsheng Wang et al.
- **Affiliation**: —
- **Date**: 2026-06-16 (arXiv:2606.17861)
- **Abstract**: Benchmark evaluating whether LLM agents can build playable games end-to-end in a real game engine.
- **Key Innovation**: First comprehensive benchmark for LLM-based end-to-end game development.
- **Link**: [https://arxiv.org/abs/2606.17861](https://arxiv.org/abs/2606.17861)

---

## Diffusion & Transformers

### 19. Rethinking Cross-Layer Information Routing in Diffusion Transformers (DAR)
- **Authors**: Chao Xu, Maohua Li et al.
- **Affiliation**: —
- **Date**: 2026-05-20 (arXiv:2605.20708)
- **Abstract**: Identifies three symptoms of traditional residual connections in DiTs (magnitude inflation, gradient decay, block redundancy) and proposes Diffusion-Adaptive Routing (DAR), a learnable, timestep-adaptive aggregation over sublayer outputs.
- **Key Innovation**: Improves SiT-XL/2 by 2.11 FID; 8.75× fewer training iterations to match baseline quality.
- **Link**: [https://arxiv.org/abs/2605.20708](https://arxiv.org/abs/2605.20708)

---

## Agents & Memory

### 20. AutoMem: Automated Learning of Memory as a Cognitive Skill
- **Authors**: Shengguang Wu, Hao Zhu, Yuhui Zhang, Xiaohan Wang, Serena Yeung-Levy
- **Affiliation**: Stanford
- **Date**: 2026-07-02 (arXiv:2607.01224)
- **Abstract**: Treats memory itself as a learnable cognitive skill that can be optimized rather than a fixed retrieval mechanism for LLM agents.
- **Key Innovation**: Meta-learning approach to memory management for agents.
- **Link**: [https://arxiv.org/abs/2607.01224](https://arxiv.org/abs/2607.01224)

---

## Summary Statistics

| Category | Papers Count |
|---|---|
| LLMs & Alignment | 5 |
| CTR & Advertising | 4 |
| Recommendation & Sequential | 5 |
| RL & Games | 4 |
| Diffusion & Transformers | 1 |
| Agents & Memory | 1 |
| **Total** | **20** |
