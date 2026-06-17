---
title: arXiv AI Search — June 2026
type: synthesis
created: 2026-06-17
updated: 2026-06-17
tags: [arxiv, survey, ai, llm, recommendation, ctr, games, sequential-modeling]
---

# arXiv AI Research Roundup — June 2026

A curated collection of recent arXiv papers spanning AI, LLMs, recommender systems, CTR prediction, advertising, sequential modeling, games, and reinforcement learning. Papers are drawn from June 2026 submissions (with a few notable May 2026 entries).

---

## 1. CTR Prediction & Advertising

### 1.1 Dual-Stream MLP is All You Need for CTR Prediction

- **arXiv**: [2606.04944](https://arxiv.org/abs/2606.04944)
- **Date**: Jun 3, 2026
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen
- **Institution**: Renmin University of China (RUCAIBox)
- **Venue**: ACM TKDD
- **Abstract**: Proposes DS-MLP, a dual-stream MLP framework for CTR prediction. Uses knowledge distillation to consolidate explicit feature interaction learning into a main MLP network while a parallel MLP captures implicit interactions. Two alignment strategies optimize compatibility. Achieves SOTA across three benchmarks with vanilla MLP structure.
- **Key Innovations**:
  - Knowledge distillation between dual MLP streams
  - Alignment strategies for cross-stream compatibility
  - Simplicity: pure MLP architecture matches/exceeds complex interaction models
- **Code**: https://github.com/RUCAIBox/DS-MLP

---

### 1.2 Generative Long-term User Interest Modeling for CTR Prediction (GenLI)

- **arXiv**: [2605.15905](https://arxiv.org/abs/2605.15905)
- **Date**: May 15, 2026
- **Authors**: Jiangli Shao, Kaifu Zheng, Hao Fang, Huimu Ye, Zhiwei Liu, Bo Zhang, Shu Han, Xingxing Wang
- **Institution**: Industry (Alibaba-affiliated)
- **Abstract**: Proposes GenLI for CTR with three modules: Interest Generation Module (target-independent, generates multiple interest distributions), Behavior Retrieval Module (O(1) lookup, no pairwise matching), and Interest Fusion Module (gating mechanisms). Solves target-bias and O(n) complexity of traditional two-stage long-term interest models.
- **Key Innovations**:
  - Generative (not retrieval-based) long-term interest modeling
  - Target-independent diverse interest distributions
  - O(1) behavior retrieval vs O(n) matching

---

### 1.3 IDProxy: Cold-Start CTR at Xiaohongshu with Multimodal LLMs

- **arXiv**: [2603.01590](https://arxiv.org/abs/2603.01590)
- **Date**: Mar 2, 2026
- **Authors**: Guillaume Salha-Galvan et al.
- **Institution**: Xiaohongshu
- **Abstract**: Uses MLLMs to generate proxy embeddings from content signals for cold-start items. Proxies are aligned with ID embedding space and optimized end-to-end under CTR objectives. Deployed in Content Feed and Display Ads at Xiaohongshu.
- **Key Innovations**:
  - MLLM-based proxy embeddings replacing ID embeddings for cold-start
  - Explicit alignment with existing ID embedding space
  - End-to-end training within ranking pipeline
  - Proven in production A/B tests

---

### 1.4 GenCTR: Generative CTR for Search Advertising

- **arXiv**: [2507.11246](https://arxiv.org/abs/2507.11246)
- **Date**: Jul 2025 (updated)
- **Authors**: Lingwei Kong, Lu Wang, Changping Peng, Zhangang Lin, Ching Law, Jingping Shao
- **Institution**: Industry (large e-commerce platform)
- **Abstract**: Two-stage training: (1) generative pre-training for next-item prediction, (2) fine-tuning within discriminative CTR framework. Deployed on one of world's largest e-commerce platforms. Includes four core techniques: conditional self-condition decoder, conditional negative sampling, parameter sharing, model integration.
- **Key Innovations**:
  - Generative pre-training for discriminative CTR
  - Novel public dataset released from real-world traffic
  - Online A/B validated on large-scale search advertising

---

## 2. Generative & LLM-Based Recommendation

### 2.1 Atomic Intent Reasoning (AIR): LLM Semantics for Cross-Domain Recommendations

- **arXiv**: [2606.10357](https://arxiv.org/abs/2606.10357)
- **Date**: Jun 9, 2026
- **Authors**: Zhuohang Jiang, Yuxin Chen, Shijie Wang, Haohao Qu, Zhou Jindong, Wenqi Fan, Li Qing, Dongxu Liang, Jun Wang
- **Institution**: Kuaishou / Hong Kong Polytechnic University
- **Venue**: KDD 2026
- **Abstract**: LLM-driven cross-domain recommendation framework for content-to-ecommerce. Moves LLM inference to offline, constructs user intent via efficient retrieval + composition online. Achieves 400x inference acceleration. Deployed at Kuaishou E-commerce with +3.446% GMV lift.
- **Key Innovations**:
  - Offline LLM inference + online composition for low-latency
  - ~400x speedup while maintaining semantic consistency
  - Production deployment with significant GMV impact

---

### 2.2 OneReason: Reasoning for Generative Recommendation

- **arXiv**: [2606.06260](https://arxiv.org/abs/2606.06260)
- **Date**: Jun 4, 2026
- **Authors**: OneRec Team (83 authors), Kun Gai, Ruiming Tang et al.
- **Institution**: Industry
- **Abstract**: Explores reasoning ("think before answer") in generative recommendation. Identifies two key factors: perception (grounding tokens in semantics) and cognition (reorganizing behavior into latent interest points). Proposes strong pre-training, three-level cognition-enhanced CoT, and specialize-then-unify RL training.
- **Key Innovations**:
  - First systematic exploration of CoT reasoning for generative recommendation
  - Perception + cognition framework for item token reasoning
  - Three-level CoT format + RL training recipe

---

### 2.3 AdaGRPO: Adaptive Loss Balancing for Noise-Robust GRPO in Generative Recommendation

- **arXiv**: [2606.08480](https://arxiv.org/abs/2606.08480)
- **Date**: Jun 7, 2026
- **Authors**: Kewei Xu, Junbo Qi, Yanyan Zou, Pengfei Zhang, Xingzhi Yao, Shengjie Li
- **Institution**: Industry
- **Abstract**: Identifies that GRPO reward guidance is beneficial only when policy is uncertain AND ranker can discriminate. Proposes AdaGRPO: gates GRPO objective with per-sample binary clip based on policy difficulty and reward discriminability. Elevates HR@10 from 11.01% to 12.18% with hallucination below 0.22%.
- **Key Innovations**:
  - Stratified analysis of when RL reward is beneficial vs harmful
  - Adaptive per-sample GRPO gating
  - Consistent gains in production A/B tests (CTR, dwell time)

---

### 2.4 Trustworthy Recommendation in the Era of LLMs (Survey)

- **arXiv**: [2606.00540](https://arxiv.org/abs/2606.00540)
- **Date**: May 30, 2026
- **Authors**: Bohao Wang, Yu Cui, Xiangnan He, Fuli Feng et al. (16 authors)
- **Institution**: USTC
- **Abstract**: Systematic review of trustworthy LLM-empowered recommendation. Analyzes 200+ studies. Identifies 13 opportunities and 18 challenges across 6 trustworthiness dimensions. LLMs are a double-edged sword: advanced mechanisms enhance trustworthiness but introduce new bias and hallucination risks.
- **Key Innovations**:
  - Comprehensive taxonomy of LLM × trustworthiness in recommendation
  - Dual-impact analysis (opportunities + challenges)
  - Dataset and evaluation metrics review

---

## 3. LLM Agent Training & Reinforcement Learning

### 3.1 SIRI: Self-Internalizing RL with Intrinsic Skills for LLM Agents

- **arXiv**: [2606.02355](https://arxiv.org/abs/2606.02355)
- **Date**: Jun 1, 2026
- **Authors**: Zhongyu He, Yuanfan Li, Fei Huang et al. (12 authors)
- **Institution**: Xiamen University / Industry
- **Abstract**: Three-phase framework: policy warmup (GiGPO) → self-skill mining from successful trajectories → distill beneficial skill-guided tokens into plain policy. No external skill generators or inference-time skill banks. ALFWorld: 0.930, WebShop: 0.813.
- **Key Innovations**:
  - Fully self-contained skill discovery without external generators
  - Trajectory-level utility + action-level advantage for distillation
  - Inference with original prompt only (no added complexity)

---

### 3.2 StraTA: Strategic Trajectory Abstraction for Agentic RL

- **arXiv**: [2605.06642](https://arxiv.org/abs/2605.06642)
- **Date**: May 7, 2026
- **Authors**: Xiangyuan Xue, Yifan Zhou, Zidong Wang, Philip Torr, Wanli Ouyang, Lei Bai, Zhenfei Yin
- **Institution**: University of Oxford / Shanghai AI Lab
- **Abstract**: Introduces explicit trajectory-level strategy into agentic RL. Samples compact strategy from initial state, conditions actions on it, trains jointly with hierarchical GRPO. Enhanced with diverse strategy rollout and critical self-judgment. ALFWorld: 93.1%, WebShop: 84.2%, SciWorld: 63.5%.
- **Key Innovations**:
  - Hierarchical GRPO with explicit strategy planning
  - Diverse strategy rollout for exploration
  - Outperforms frontier closed-source models on SciWorld

---

## 4. Games & Multi-Agent Reasoning

### 4.1 SPIRAL: Self-Play on Zero-Sum Games for Reasoning via Multi-Agent RL

- **arXiv**: [2506.24119](https://arxiv.org/abs/2506.24119) (v3, Mar 2026)
- **Date**: Jun 2025 / updated Mar 2026
- **Authors**: Not specified (multiple authors)
- **Abstract**: Self-play framework where LLMs learn by playing multi-turn zero-sum games against continuously improving versions of themselves. Proposes role-conditioned advantage estimation (RAE). Up to 10% improvement across 8 reasoning benchmarks on Qwen and Llama. Games: TicTacToe, Kuhn Poker, Simple Negotiation.
- **Key Innovations**:
  - Fully online, multi-turn, multi-agent RL system for LLMs
  - Role-conditioned advantage estimation for stable multi-agent training
  - Game-derived cognitive patterns transfer to general reasoning

---

## 5. Sequence Modeling & Architecture

### 5.1 Mamba-3: Improved Sequence Modeling using State Space Principles

- **arXiv**: [2603.15569](https://arxiv.org/abs/2603.15569)
- **Date**: Mar 16, 2026
- **Authors**: Aakash Lahoti, Kevin Y. Li, Berlin Chen, Caitlin Wang, Aviv Bick, J. Zico Kolter, Tri Dao, Albert Gu
- **Institution**: Carnegie Mellon University / Princeton University / Together AI
- **Venue**: ICLR 2026
- **Abstract**: Inference-first SSM design with three improvements: (1) more expressive recurrence from SSM discretization, (2) complex-valued state update for richer state tracking, (3) MIMO formulation for better performance without decode latency increase. Mamba-3 MIMO variant achieves +1.8pp over Gated DeltaNet at 1.5B scale. Half the state size of Mamba-2 for comparable perplexity.
- **Key Innovations**:
  - Complex-valued state space for improved state tracking
  - MIMO (multi-input, multi-output) SSM formulation
  - Inference-first design: efficiency without quality tradeoff
  - Pareto frontier advancement for performance vs efficiency

---

## 6. Cross-Cutting Trends

| Trend | Papers | Description |
|-------|--------|-------------|
| **RL for Recommendation** | OneReason, AdaGRPO | GRPO and RL-based reasoning being applied to generative recommendation with per-sample adaptive strategies |
| **LLM Inference at Scale** | AIR, IDProxy | Moving LLM inference offline with efficient online composition; MLLMs for cold-start |
| **Generative CTR** | GenLI, GenCTR, OneReason | Generative modeling replacing retrieval-based approaches for user interest modeling |
| **Reasoning in RecSys** | OneReason, AIR | Chain-of-thought and reasoning paradigms entering recommendation |
| **Skill-Based Agents** | SIRI, StraTA | Self-contained skill discovery without external generators; hierarchical strategy planning |
| **Game-Driven Reasoning** | SPIRAL | Zero-sum self-play as a general-purpose reasoning training method |
| **SSM Alternatives** | Mamba-3 | State space models advancing performance-efficiency frontier post-Transformer |

---

## 7. How to Stay Current

- **arXiv RSS**: Subscribe to cs.IR, cs.AI, cs.LG, cs.CL new submissions
- **Weekly digests**: `arxivtldr.org`, `shipit.news`, `deeplearn.org`
- **Sebastian Raschka's LLM Paper Lists**: [2026 list (Jan-May)](https://magazine.sebastianraschka.com/p/llm-research-papers-2026-part1)
- **KDD 2026**: Several papers from this roundup accepted at KDD 2026 (Jeju Island, Aug 2026)
