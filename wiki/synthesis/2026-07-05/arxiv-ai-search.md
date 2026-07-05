---
title: "arXiv AI Research Search — July 2026"
type: synthesis
created: 2026-07-05
updated: 2026-07-05
tags: [arxiv, survey, llm, recommendation, ctr, sequential-modeling, games, advertising]
---

# arXiv AI Research Search — July 5, 2026

Curated recent papers across LLMs, recommendation systems, CTR prediction, sequential modeling, and game AI.

---

## 1. Large Language Models (LLMs)

### 1.1 Understanding Large Language Models
- **Authors**: Yannik Keller, Thomas Eisenmann
- **Date**: Jul 1, 2026
- **arXiv**: [2607.01006](https://arxiv.org/abs/2607.01006)
- **Key Innovations**: Comprehensive chapter reviewing emergent LLM capabilities (reasoning, theory of mind, deception), mechanistic interpretability via neuron activation analysis and circuit tracing, and a defense of LLM cognition against reductionist critiques.
- **Significance**: Provides a balanced survey of what LLMs genuinely understand vs. pattern memorization — useful grounding for any researcher working with LLMs.

### 1.2 Large Language Model Reasoning Failures (Survey)
- **Authors**: Peiyang Song et al.
- **Date**: Feb 5, 2026 (TMLR 2026 — Survey Certification)
- **arXiv**: [2602.06176](https://arxiv.org/abs/2602.06176)
- **Key Innovations**: First comprehensive survey dedicated to reasoning failures in LLMs. Novel categorization framework distinguishing embodied vs. non-embodied reasoning, with failure types spanning fundamental, application-specific, and robustness issues.
- **Significance**: Structured perspective on systemic LLM reasoning weaknesses with mitigation strategies.

### 1.3 Agentic Reasoning for Large Language Models (Survey)
- **Authors**: Lei Fang, Hui Liu, Xianfeng Tang et al.
- **Date**: Jan 18, 2026
- **arXiv**: [2601.12538](https://arxiv.org/abs/2601.12538)
- **Key Innovations**: Three-layer framework — foundational single-agent reasoning (planning, tool use, search), self-evolving reasoning (feedback, memory, adaptation), and collective multi-agent reasoning (coordination, knowledge sharing). Distinguishes in-context reasoning from post-training reasoning.
- **Significance**: Maps the rapidly evolving space of LLM agents and their reasoning paradigms.

### 1.4 Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter RL Training
- **Authors**: Zijian Zhang, Rizhen Hu, Athanasios Glentis et al. (U. Minnesota, Amazon)
- **Date**: Jul 2, 2026
- **arXiv**: [2607.01232](https://arxiv.org/abs/2607.01232)
- **Key Innovations**: Systematic layer-wise study of RL post-training. Introduces *layer contribution* metric. Finds RL gains concentrate in middle layers — training just one layer can recover most full-parameter gains. Pattern holds across Qwen3, Qwen2.5, and multiple RL algorithms (GRPO, GiGPO, Dr. GRPO).
- **Significance**: Could dramatically reduce cost of RL fine-tuning for LLMs.

### 1.5 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL
- **Authors**: P. Qi, D. Balcells, M. Liu et al.
- **Date**: Jun 30, 2025 (ICLR 2026)
- **arXiv**: [2506.24119](https://arxiv.org/abs/2506.24119)
- **Key Innovations**: Self-play framework where LLMs learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Negotiation) against themselves. Proposes role-conditioned advantage estimation (RAE) for multi-agent training. Up to 10% improvement across 8 reasoning benchmarks on Qwen and Llama families.
- **Significance**: Demonstrates zero-sum games as a scalable source of transferable reasoning — no human-curated data needed.

---

## 2. Recommendation Systems

### 2.1 Deep Research for Recommender Systems (RecPilot)
- **Authors**: Kesha Ou, Chenghao Wu, Xiaolei Wang et al.
- **Date**: Mar 8, 2026
- **arXiv**: [2603.07605](https://arxiv.org/abs/2603.07605)
- **Key Innovations**: Proposes a "deep research" paradigm replacing item lists with user-centric reports. RecPilot is a multi-agent framework with two components: a trajectory simulation agent for autonomous item space exploration, and a self-evolving report generation agent synthesizing findings.
- **Significance**: Reframes recommendation from passive filtering to proactive, agent-driven service.

### 2.2 Self-Evolving Recommendation System: End-To-End Autonomous Model Optimization With LLM Agents
- **Authors**: Haochen Wang, Yi Wu, Daryl Chang et al. (Google/YouTube)
- **Date**: Feb 10, 2026
- **arXiv**: [2602.10226](https://arxiv.org/abs/2602.10226)
- **Key Innovations**: Uses Gemini LLM agents as autonomous ML Engineers — offline inner loop for hypothesis generation with proxy metrics, online outer loop for validation against north-star business metrics in production. Discovered novel optimizers, architectures, and reward functions deployed at YouTube.
- **Significance**: Demonstrates LLM-driven auto-evolution of industrial recommendation systems at scale.

### 2.3 Trustworthy Recommendation in the Era of Large Language Models: Opportunities and Challenges
- **Authors**: Bohao Wang, Chongming Gao, Fuli Feng, Xiangnan He, Jiawei Chen et al.
- **Date**: May 30, 2026
- **arXiv**: [2606.00540](https://arxiv.org/abs/2606.00540)
- **Key Innovations**: Systematic review of 200+ studies on trustworthy LLM-empowered recommendation. Maps 13 opportunities and 18 challenges across 6 trustworthiness dimensions. LLMs are a double-edged sword — new bias and hallucination risks alongside improved reasoning and user interaction.
- **Significance**: Essential guide for building reliable LLM-based recommenders.

### 2.4 Meta Lattice: Model Space Redesign for Cost-Effective Industry-Scale Ads Recommendations
- **Authors**: Liang Luo, Yuxin Chen, Zhengyu Zhang et al. (Meta AI)
- **Date**: Dec 9, 2025 (KDD 2026)
- **arXiv**: [2512.09200](https://arxiv.org/abs/2512.09200)
- **Key Innovations**: Comprehensive model space redesign consolidating thousands of domain-objective models into unified framework. Cross-domain knowledge sharing, data consolidation, hierarchical teacher-student design. 10% revenue gain, 11.5% user satisfaction improvement, 6% conversion rate boost, 20% capacity saving at Meta.
- **Significance**: State-of-the-art industrial-scale multi-domain, multi-objective recommendation.

---

## 3. CTR Prediction & Advertising

### 3.1 CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **Authors**: Ruoyan Wang et al. (LinkedIn)
- **Date**: Feb 11, 2026
- **arXiv**: [2602.11410](https://arxiv.org/abs/2602.11410)
- **Key Innovations**: End-to-end decoder-only transformer for ads CTR deployed at LinkedIn. Five key innovations: context-conditioned multi-tower decoding (solves CTR-vs-position chicken-and-egg), self-gated attention, timestamp-based RoPE, session masking for train-serve skew, and production engineering (tensor packing, Flash Attention). 11.04% CTR lift over LiRank baseline.
- **Significance**: First large-scale deployment of decoder-only transformer for ads CTR prediction.

### 3.2 LoopCTR: Unlocking the Loop Scaling Power for CTR Prediction
- **Authors**: Jiakai Tang, Runfeng Zhang et al. (Alibaba)
- **Date**: Apr 21, 2026
- **arXiv**: [2604.19550](https://arxiv.org/abs/2604.19550)
- **Key Innovations**: Loop scaling paradigm — recursive reuse of shared layers decouples computation from parameter growth. Sandwich architecture with Hyper-Connected Residuals and MoE. Process supervision per loop depth. Train-multi-loop, infer-zero-loop strategy outperforms all baselines. Oracle analysis reveals 0.02–0.04 AUC untapped headroom.
- **Significance**: Novel approach to scaling CTR models without parameter growth — highly relevant for industrial deployment constraints.

### 3.3 Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)
- **Authors**: Kesha Ou, Zhen Tian, Wayne Xin Zhao et al. (Renmin University)
- **Date**: Jun 3, 2026 (TKDD 2026)
- **arXiv**: [2606.04944](https://arxiv.org/abs/2606.04944)
- **Key Innovations**: Uses knowledge distillation to consolidate explicit feature interaction learning into a main MLP, while a parallel MLP captures implicit interactions. Two alignment strategies for compatibility. Vanilla 3-layer MLP (final model) achieves SOTA across 3 benchmarks.
- **Significance**: Challenges the assumption that complex architectures are needed for CTR — simplicity + distillation can be SOTA.

---

## 4. Sequential Modeling & State Space Models

### 4.1 Mamba-3: Improved Sequence Modeling using State Space Principles
- **Authors**: Kevin Li, Tri Dao, Albert Gu
- **Date**: Mar 16, 2026 (ICLR 2026)
- **arXiv**: [2603.15569](https://arxiv.org/abs/2603.15569)
- **Key Innovations**: Three SSM-inspired improvements: more expressive recurrence from SSM discretization, complex-valued state update for better state tracking, and multi-input multi-output (MIMO) formulation. Mamba-3 achieves comparable perplexity to Mamba-2 with half the state size. +1.8 pp accuracy gain with MIMO variant at 1.5B scale.
- **Significance**: Advances the performance-efficiency Pareto frontier for linear-time sequence models.

### 4.2 Continuity Laws for Sequential Models
- **Authors**: Annan Yu, Dongwei Lyu, N. Benjamin Erichson (Cornell, UC Berkeley, LBNL, ICSI)
- **Date**: May 8, 2026
- **arXiv**: [2605.08539](https://arxiv.org/abs/2605.08539)
- **Key Innovations**: Formalizes *continuity in time* as an inductive bias. SSMs derived from continuous formulations vs. discrete Transformer interactions. Proposes stage-wise training on temporally subsampled data with progressive refinement for continuous tasks.
- **Significance**: Provides principled framework for model-task fit — explains why SSMs excel on continuous tasks and Transformers on discrete ones.

### 4.3 Mechanistic Evaluation of Transformers and State Space Models
- **Authors**: Aryaman Arora, Neil Rathi, Nikil Roashan Selvam et al. (Stanford)
- **Date**: May 21, 2025 (updated Jan 2026)
- **arXiv**: [2505.15105](https://arxiv.org/abs/2505.15105)
- **Key Innovations**: Causal intervention analysis on Associative Recall tasks. Transformers and Based SSM use induction heads for in-context storage. Mamba implements induction via short convolutions, not its SSM core. New Associative Treecall (ATR) task reveals all architectures learn similar mechanisms. Removing short convolutions forces Mamba to learn attention-like induction.
- **Significance**: Mechanistic understanding reveals that behavioral similarity (accuracy) can mask substantive architectural differences.

---

## 5. AI for Games

### 5.1 Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: Alessandro Sestini et al.
- **Date**: Jun 18, 2026 (Conference on Games 2026)
- **arXiv**: [2606.20210](https://arxiv.org/abs/2606.20210)
- **Key Innovations**: Vision paper proposing a framework for training RL models specifically for game AI, with requirements suited to game development. Presents practical examples of RL-augmented game AI and identifies deployment bottlenecks and hard problems.
- **Significance**: Bridges the gap between RL research and practical game development — relevant for anyone building game AI.

### 5.2 SPIRAL (see §1.5)
- Games used as training environment for transferable LLM reasoning. Multi-game training (TicTacToe, Kuhn Poker, Negotiation) yields strongest reasoning transfer. Distinct cognitive patterns develop from different games.

---

## Cross-Cutting Themes

| Theme | Papers | Implication |
|-------|--------|-------------|
| **LLM as autonomous engineer** | Self-Evolving RecSys, SPIRAL, Agentic Reasoning | LLMs are transitioning from tools to autonomous research/deployment agents |
| **Scaling without parameters** | LoopCTR, Mamba-3, Meta Lattice | Decoupling compute from parameter count is a major research direction |
| **Simplicity beats complexity** | DS-MLP, Is One Layer Enough, Continuity Laws | Growing evidence that simple architectures + proper training match complex ones |
| **Decoder-only for recommendation** | CADET | Transformer decoder architectures entering CTR/ads domain |
| **Trustworthiness gap** | Trustworthy Recommendation, LLM Reasoning Failures | LLM integration introduces new failure modes requiring systematic mitigation |
| **Mechanistic understanding** | Mechanistic Eval of SSMs, Continuity Laws | Moving beyond accuracy benchmarks to understand *how* models work |

---

*Generated 2026-07-05 via arXiv search. Papers selected for relevance to LLMs, recommendation systems, CTR prediction, advertising technology, sequential modeling, and game AI.*
