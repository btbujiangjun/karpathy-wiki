---
title: arXiv Daily — 2026-07-05
type: synthesis
created: 2026-07-05
updated: 2026-07-05
tags: [arxiv, survey, llm, recommendation, ctr, reinforcement-learning, games, sequential-modeling, advertising]
---

# arXiv Daily Report — 2026-07-05

Curated recent papers in AI, LLMs, recommendation, advertising, CTR, sequential modeling, and games.

---

## Table of Contents
- [LLM Reasoning & Architecture](#llm-reasoning--architecture)
- [LLM Agents & Self-Evolution](#llm-agents--self-evolution)
- [Recommendation Systems](#recommendation-systems)
- [CTR Prediction & Advertising](#ctr-prediction--advertising)
- [Sequential Modeling](#sequential-modeling)
- [Reinforcement Learning & Games](#reinforcement-learning--games)

---

## LLM Reasoning & Architecture

### 1. ReRec: Reasoning-Augmented LLM-based Recommendation Assistant via Reinforcement Fine-tuning
- **Link:** [2604.07851](https://arxiv.org/abs/2604.07851)
- **Authors:** Jiani Huang, Shijie Wang, Liangbo Ning, Wenqi Fan, Qing Li
- **Institution:** — (Hong Kong)
- **Status:** Accepted by ACL 2026
- **Abstract:** Proposes a reinforcement fine-tuning (RFT) framework to improve LLM reasoning in complex recommendation tasks. Introduces Dual-Graph Enhanced Reward Shaping (integrating NDCG@K with Query/Preference Alignment), Reasoning-aware Advantage Estimation (penalizing incorrect reasoning steps), and an Online Curriculum Scheduler.
- **Key Innovations:** First RFT framework for LLM-based recommendation reasoning; decomposes LLM outputs into reasoning segments for granular reward; maintains instruction-following and general knowledge while improving recommendation.
- **Tags:** `LLM` `recommendation` `reinforcement-learning` `reasoning`

### 2. Understanding Large Language Models
- **Link:** [2607.01006](https://arxiv.org/abs/2607.01006)
- **Authors:** Yannik Keller, Thomas Eisenmann
- **Institution:** —
- **Abstract:** A book chapter/overview examining emergent LLM capabilities — symbolic reasoning, theory of mind, deception strategies. Reviews mechanistic interpretability (neuron activation, circuit tracing) and addresses debates on whether LLMs possess "genuine understanding."
- **Key Innovations:** Synthesizes evidence for/against LLM cognition; argues against overly simplistic reductionist dismissal of AI cognition.
- **Tags:** `LLM` `survey` `interpretability` `cognition`

### 3. Testing Frontier Large Language Models' Physics Literacy in Parallel Physical Worlds
- **Link:** [2607.00276](https://arxiv.org/abs/2607.00276)
- **Authors:** Dong Zhang
- **Institution:** —
- **Abstract:** Introduces a 4-stage diagnostic (induction, formulation, prediction, review) testing whether LLMs can reason inside unfamiliar physics frameworks (F=mv counterfactual, Aristotelian mechanics, Decay World). Tests Claude Opus 4.7, GPT-5.5, Gemini 3.1 Pro. Composite PASS rates: 6/15, 6/15, 0/15.
- **Key Innovations:** Auditable staged evaluation beyond answer accuracy; reveals qualitative-vs-quantitative asymmetry; shows LLM-judge reliability does not transfer across frameworks.
- **Tags:** `LLM` `evaluation` `physics` `reasoning`

### 4. Measuring the Gap Between Human and LLM Research Ideas
- **Link:** [2607.01233](https://arxiv.org/abs/2607.01233)
- **Authors:** Ziyu Chen, Yilun Zhao, Arman Cohan
- **Institution:** Yale
- **Abstract:** Builds a large-scale evaluation framework for ideation. Reverse-engineers prior works that inspired published papers, prompts LLMs to generate ideas from those prior works. Introduces a two-axis research-taste taxonomy. Finds LLM ideas are disproportionately concentrated around bridge-like opportunities and synthesis methods vs. human distribution.
- **Key Innovations:** Quantitative characterization of the "ideation gap"; shows LLM idea distribution is narrower and systematically shifted relative to human research taste.
- **Tags:** `LLM` `creativity` `research` `evaluation`

---

## LLM Agents & Self-Evolution

### 5. Next-Generation Agentic Reinforcement Learning Systems Enable Self-Evolving Agents
- **Link:** [2607.01120](https://arxiv.org/abs/2607.01120)
- **Authors:** Ran Yan, Wei Fu, Jiale Li et al.
- **Institution:** Ant Group, HKUST, Tsinghua University
- **Abstract:** Argues that enterprise-level self-evolving agents are held back not by RL algorithms but by agentic online RL systems. Identifies three missing pillars: standardized agent trajectory data protocol, enterprise-grade data proxy for governed learning substrates, and unified agent evolution control plane. Instantiates AReaL2.0.
- **Key Innovations:** Framework for online RL loops from deployed agent workloads; proposes concrete architectures for self-evolving agent deployment.
- **Tags:** `LLM` `agents` `reinforcement-learning` `self-evolution`

### 6. SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning
- **Link:** [2506.24119](https://arxiv.org/abs/2506.24119)
- **Authors:** P. Qi, D. Balcells, M. Liu, C. Tan, W. Shi, M. Lin, W. S. Lee, N. Jaques
- **Institution:** —
- **Status:** Accepted at ICLR 2026
- **Abstract:** Self-play framework where LLMs learn by playing multi-turn zero-sum games (TicTacToe, Kuhn Poker, Simple Negotiation) against continuously improving versions of themselves. Proposes role-conditioned advantage estimation (RAE) for multi-agent training. Improves reasoning by up to 10% across 8 benchmarks on Qwen and Llama families.
- **Key Innovations:** Fully online multi-turn multi-agent RL for LLMs; games develop distinct cognitive patterns that transfer to reasoning tasks; benefits even DeepSeek-R1-Distill models already trained with RLVR.
- **Tags:** `LLM` `reinforcement-learning` `games` `reasoning` `self-play`

### 7. Reinforcement World Model Learning for LLM-based Agents
- **Link:** [2602.05842](https://arxiv.org/abs/2602.05842)
- **Authors:** Xiao Yu, Baolin Peng, Ruize Xu et al.
- **Institution:** —
- **Abstract:** Self-supervised method learning action-conditioned world models for LLM agents on textual states using sim-to-real gap rewards. Aligns simulated next states with realized next states in a pre-trained embedding space. Outperforms direct task-success reward RL by 6.9 and 5.7 points on ALFWorld and τ² Bench.
- **Key Innovations:** World model learning without task rewards; more robust than next-token prediction or LLM-as-judge; matches expert-data training performance.
- **Tags:** `LLM` `agents` `world-models` `reinforcement-learning`

### 8. ReContext: Recursive Evidence Replay as LLM Harness for Long-Context Reasoning
- **Link:** [2607.02509](https://arxiv.org/abs/2607.02509)
- **Authors:** Yanjun Zhao, Ruizhong Qiu, Tianxin Wei et al.
- **Institution:** —
- **Abstract:** Recursive evidence replay mechanism that iteratively surfaces relevant context chunks for long-context reasoning tasks, reducing the effective context window needed.
- **Key Innovations:** Recursive approach to long-context reasoning; efficient evidence retrieval without full-context processing.
- **Tags:** `LLM` `long-context` `reasoning`

---

## Recommendation Systems

### 9. Self-Evolving Recommendation System: End-To-End Autonomous Model Optimization With LLM Agents
- **Link:** [2602.10226](https://arxiv.org/abs/2602.10226)
- **Authors:** Haochen Wang, Yi Wu, Daryl Chang, Li Wei, Lukasz Heldt
- **Institution:** Google (YouTube)
- **Abstract:** Uses Gemini-family LLMs to autonomously generate, train, and deploy model changes. Two-loop architecture: Offline Agent (Inner Loop) does high-throughput hypothesis generation with proxy metrics; Online Agent (Outer Loop) validates against delayed north-star metrics in live production. Multiple successful YouTube launches.
- **Key Innovations:** First end-to-end LLM-driven model evolution at YouTube scale; agents discover novel optimization algorithms, architectures, and reward functions targeting long-term user engagement.
- **Tags:** `recommendation` `LLM` `agents` `auto-ml` `YouTube`

### 10. POEM: Partial-Order Enhanced Real-Time Sequential Modeling for Recommendation
- **Link:** [2606.29946](https://arxiv.org/abs/2606.29946)
- **Authors:** Linxiao Che, Yijia Sun, Siyuan Lou, Shanshan Huang, Qiang Luo, Ruiming Tang, Han Li, Kun Gai
- **Institution:** Kuaishou
- **Abstract:** Real-time sequential modeling framework exploiting partial-order relations from the recommendation cascade. Uses multi-task ranking scores (CTR, watch duration) from upstream modules as supervision to construct dynamic partial-order sequences. Deployed on Kuaishou — 0.249% and 0.213% per-user watch time lift.
- **Key Innovations:** Partial-order guided sequence construction; multi-objective score fusion into quintuple representation; hierarchical sample learning with graph-mined hard negatives.
- **Tags:** `recommendation` `sequential-modeling` `real-time` `Kuaishou`

### 11. Bradley-Terry Rankings for Recommender Systems Across Dataset Taxonomies
- **Link:** [2606.07492](https://arxiv.org/abs/2606.07492)
- **Authors:** A. Lysenko et al.
- **Institution:** —
- **Status:** KDD'26
- **Abstract:** Data-driven ranking methodology based on Bradley-Terry model. Shows ranking depends on key dataset statistics. Introduces metric for ranking consistency, demonstrates robustness to incomplete data. Proposes BT trees and BT models with covariates for ranking unseen datasets without running models.
- **Key Innovations:** Principled methodology for fair comparison of recommendation algorithms; dataset-specific ranking prediction.
- **Tags:** `recommendation` `evaluation` `benchmarking`

### 12. LAIN: Length-Adaptive Interest Network for Balancing Long and Short Sequence Modeling
- **Link:** [2601.19142](https://arxiv.org/abs/2601.19142)
- **Authors:** Zhicheng Zhang et al. (11 authors)
- **Institution:** —
- **Status:** AAAI 2026
- **Abstract:** Plug-and-play framework conditioning on sequence length. Three components: Spectral Length Encoder, Length-Conditioned Prompting, Length-Modulated Attention. Up to 1.15% AUC gain, 2.25% log loss reduction. Significantly improves short-sequence users without sacrificing long-sequence effectiveness.
- **Key Innovations:** Identifies that longer sequences paradoxically hurt short-sequence users due to attention polarization; explicit length conditioning as a general solution.
- **Tags:** `recommendation` `CTR` `sequential-modeling` `length-bias`

---

## CTR Prediction & Advertising

### 13. CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **Link:** [2602.11410](https://arxiv.org/abs/2602.11410)
- **Authors:** David Pardoe, Neil Daftary, Miro Furtado et al. (23 authors)
- **Institution:** LinkedIn
- **Abstract:** End-to-end decoder-only transformer for ads CTR deployed at LinkedIn. Innovations: (1) context-conditioned decoding with multi-tower prediction heads for post-scoring signals (ad position), (2) self-gated attention, (3) timestamp-based RoPE, (4) session masking for train-serve skew, (5) tensor packing & custom Flash Attention. 11.04% CTR lift vs. production LiRank.
- **Key Innovations:** First decoder-only transformer for ads CTR at LinkedIn scale; resolves the chicken-and-egg problem between predicted CTR and ranking via context-conditioned architecture.
- **Tags:** `CTR` `advertising` `transformer` `LinkedIn`

### 14. From Scaling to Structured Expressivity: Rethinking Transformers for CTR Prediction (FAT)
- **Link:** [2511.12081](https://arxiv.org/abs/2511.12081)
- **Authors:** Bencheng Yan, Yuejie Lei, Zhiyuan Zeng et al.
- **Institution:** Alibaba Group
- **Status:** KDD 2026
- **Abstract:** Identifies structural misalignment between standard Transformers (sequential compositionality) and CTR data (combinatorial reasoning over heterogeneous fields). Proposes Field-Aware Transformer (FAT) with field-centric parameters. Uses Basis-Composed Hypernetwork to decouple capacity from field cardinality. Rademacher complexity-based scaling law. +4.38% AUC, +2.33% CTR, +0.66% RPM in production.
- **Key Innovations:** Formal scaling law for CTR prediction; field-centric transformer reconstruction; proves scalable recommendation arises from structured expressivity, not just size.
- **Tags:** `CTR` `transformer` `scaling-law` `Alibaba`

### 15. IDProxy: Cold-Start CTR Prediction for Ads and Recommendation at Xiaohongshu with Multimodal LLMs
- **Link:** [2603.01590](https://arxiv.org/abs/2603.01590)
- **Authors:** — (Xiaohongshu)
- **Institution:** Xiaohongshu (RedNote)
- **Abstract:** Uses MLLMs to generate proxy embeddings from content signals for cold-start items without usage data. Two-stage alignment: coarse alignment in ID embedding space via contrastive learning, then CTR-aware fine-grained alignment with hierarchical representation partitioning and residual gating. Deployed on Xiaohongshu's Explore Feed.
- **Key Innovations:** Explicit alignment of MLLM proxies with ID embedding space; end-to-end optimization under CTR objectives; handles 300M+ MAU scale.
- **Tags:** `CTR` `cold-start` `multimodal-LLM` `Xiaohongshu`

### 16. Dual-Stream MLP is All You Need for CTR Prediction
- **Link:** [2606.04944](https://arxiv.org/abs/2606.04944)
- **Authors:** —
- **Institution:** —
- **Abstract:** Lightweight alternative for CTR: trains a simple 3-layer MLP using knowledge distillation from a powerful teacher (e.g., GDCN), then augments with a parallel MLP to capture missed signals. Challenges the necessity of complex architectures.
- **Key Innovations:** Distillation-based lightweight CTR; dual-stream design captures complementary signals; strong efficiency-accuracy trade-off.
- **Tags:** `CTR` `distillation` `efficiency`

---

## Sequential Modeling

### 17. Beyond Autoregressive RTG: SlimDT — Conditioning via Injection Outside Sequential Modeling in Decision Transformer
- **Link:** [2605.06104](https://arxiv.org/abs/2605.06104)
- **Authors:** Yongyi Wang, Hanyu Liu, Lingfeng Li et al.
- **Institution:** —
- **Abstract:** Removes Return-to-Go (RTG) from the autoregressive sequence in Decision Transformer. Injects RTG into state representations before sequential modeling, reducing sequence length by 1/3. Surpasses standard DT on D4RL benchmarks with comparable performance to SOTA.
- **Key Innovations:** Decouples sparse conditioning signal from information-rich sequence; demonstrates that RTG as a separate token is computationally wasteful.
- **Tags:** `decision-transformer` `offline-RL` `sequential-modeling` `efficiency`

### 18. Context-Aware Lifelong Sequential Modeling for Online CTR Prediction (CAIN)
- **Link:** [2502.12634](https://arxiv.org/abs/2502.12634)
- **Authors:** —
- **Institution:** WeChat
- **Abstract:** Uses Temporal Convolutional Networks (TCN) to create context-aware representations for each item in lifelong user sequences. Multi-Scope Interest Aggregator (MSIA) captures varying context scopes. Personalized Extractor Generation (PEG) generates user-specific convolution filters. Deployed on WeChat Channels.
- **Key Innovations:** Context-aware (not just item-wise) sequence representations; personalized convolution filters from user profiles.
- **Tags:** `CTR` `sequential-modeling` `lifelong` `WeChat`

---

## Reinforcement Learning & Games

### 19. Conservative Adversarially Robust Decision Transformer (CART)
- **Link:** [2510.11877](https://arxiv.org/abs/2510.11877)
- **Authors:** Xiaohang Tang, Zhuowen Cheng, Satyabrat Kumar
- **Institution:** UCL
- **Abstract:** First framework designed to enhance adversarial robustness of Decision Transformers in stochastic games. Formulates protagonist-adversary interaction as stage games with NashQ conditioning. Produces policies that are simultaneously less exploitable and conservative to transition uncertainty.
- **Key Innovations:** Min-max conditioning for sequence model policies; NashQ-based value estimation for adversarial stochastic games.
- **Tags:** `reinforcement-learning` `decision-transformer` `adversarial` `games`

### 20. Transformer-Enhanced Reinforcement Learning: Fundamentals and Applications in Communication Networks
- **Link:** [2606.05208](https://arxiv.org/abs/2606.05208)
- **Authors:** Nguyen Cong Luong et al. (13 authors)
- **Institution:** —
- **Abstract:** Comprehensive survey of Transformer-based RL algorithms and applications. Covers resource allocation, computation offloading, routing, trajectory control, and network security. Provides mathematical background of both RL and Transformer architectures.
- **Key Innovations:** Systematic taxonomy of how self-attention addresses RL limitations (long-range dependencies, partial observability); cross-domain applications survey.
- **Tags:** `reinforcement-learning` `transformer` `survey` `networks`

### 21. Augmenting Game AI with Deep Reinforcement Learning
- **Link:** [2606.20210](https://arxiv.org/abs/2606.20210)
- **Authors:** Alessandro Sestini et al.
- **Institution:** —
- **Status:** Conference on Games 2026
- **Abstract:** Vision paper proposing a framework for training DRL models for game AI with production requirements in mind. Presents examples of RL-augmented game AI, discusses deployment practicalities, identifies bottlenecks for industry adoption.
- **Key Innovations:** Practical deployment framework for player-facing ML agents in games; bridges the gap between RL research and game industry needs.
- **Tags:** `reinforcement-learning` `games` `game-AI` `deployment`

---

## Summary Statistics

| Domain | Papers This Report |
|--------|-------------------|
| LLM Reasoning & Architecture | 4 |
| LLM Agents & Self-Evolution | 4 |
| Recommendation Systems | 4 |
| CTR Prediction & Advertising | 4 |
| Sequential Modeling | 2 |
| Reinforcement Learning & Games | 3 |
| **Total** | **21** |

### Notable Trends
1. **LLM + Recommendation convergence** is accelerating — RFT (ReRec), self-evolving models (YouTube), MLLM cold-start (Xiaohongshu).
2. **Transformers for CTR** are graduating from research to production at LinkedIn (CADET), Alibaba (FAT), Kuaishou (POEM).
3. **Self-play/self-evolution** for LLMs is a hot topic — SPIRAL (ICLR 2026) shows zero-sum games improve reasoning, Ant Group's agentic RL loop paper.
4. **Sequential modeling in RL** continues to mature — SlimDT challenges DT design assumptions; CART adds adversarial robustness.
5. **Scaling law thinking** is spreading to recommendation (FAT's Rademacher complexity-based law for CTR).
