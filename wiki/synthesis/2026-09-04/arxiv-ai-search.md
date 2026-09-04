---
title: arXiv AI Research Paper Search Report
type: synthesis
created: 2026-09-04
updated: 2026-09-04
sources: [arxiv.org]
tags: [arxiv, AI, LLM, CTR, recommendation, advertising, sequential-modeling, game-AI]
---

# arXiv AI Research Paper Search Report

Generated: 2026-09-04 | Scope: AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games

---

## 1. Large Language Models (LLMs)

### 1.1 Nemotron 3 Super: Open, Efficient MoE Hybrid Mamba-Transformer Model for Agentic Reasoning
- **Authors**: NVIDIA Research
- **Institution**: NVIDIA
- **Date**: 2026-04-13
- **arXiv**: https://arxiv.org/abs/2604.12374
- **Abstract**: A hybrid architecture alternating attention layers and Mamba-2 (state space model) layers for efficient long-context reasoning. 120B-A12B parameters. Designed for agentic workloads requiring long context windows.
- **Key Innovations**: Hybrid Mamba-Transformer architecture; MoE with 120B total / 12B active parameters; optimized for agentic reasoning tasks; production-ready design.
- **Venue**: Technical report (production model)

### 1.2 Mamba-3: Improved Sequence Modeling Using State Space Principles
- **Authors**: Gu et al.
- **Institution**: (unspecified)
- **Date**: 2026-03-16
- **arXiv**: https://arxiv.org/abs/2603.15569
- **Abstract**: Improved state space model architecture for sequence modeling, advancing Mamba-family architectures with better long-range dependency handling.
- **Key Innovations**: Improved SSM design; better scaling for long sequences; competitive with Transformer baselines.
- **Venue**: Preprint

### 1.3 Scaling Embeddings Outperforms Scaling Experts in Language Models
- **Authors**: (multiple)
- **Institution**: (unspecified)
- **Date**: 2026-01-29
- **arXiv**: https://arxiv.org/abs/2601.21204
- **Abstract**: Demonstrates that scaling embedding dimensions yields better performance than scaling the number of experts in MoE language models.
- **Key Innovations**: Paradigm shift from MoE expert scaling to embedding scaling; improved parameter efficiency.
- **Venue**: Preprint

### 1.4 Cola DLM: Continuous Latent Diffusion Language Model
- **Authors**: ByteDance
- **Institution**: ByteDance
- **Date**: 2026 (2026 list)
- **arXiv**: Not specified directly; referenced in top-10 list
- **Abstract**: A scalable alternative to autoregressive language modeling using continuous latent diffusion, enabling non-sequential text generation.
- **Key Innovations**: Continuous latent diffusion for language modeling; breaks autoregressive paradigm; parallelizable generation.
- **Venue**: Top-10 LLM papers of 2026 (HuggingFace upvotes)

### 1.5 Understanding Large Language Models
- **Authors**: Yannik Keller, Thomas Eisenmann
- **Institution**: (unspecified)
- **Date**: 2026-07-01
- **arXiv**: https://arxiv.org/abs/2607.01006
- **Abstract**: Comprehensive survey chapter on LLM mechanisms, emergent capabilities (symbolic reasoning, theory of mind, deception), and their relationship to human cognition.
- **Key Innovations**: Systematic review of emergent capabilities; analysis of black-box problem; nuanced discussion of LLM cognition vs. human cognition.
- **Venue**: Preprint / book chapter

### 1.6 AdapTime: Enabling Adaptive Temporal Reasoning in Large Language Models
- **Authors**: (unspecified)
- **Institution**: (unspecified)
- **Date**: 2026
- **arXiv**: Referenced in Analytics Vidhya top-10
- **Abstract**: Enables LLMs to adaptively handle temporal reasoning across different time scales and contexts.
- **Key Innovations**: Adaptive temporal reasoning; time-aware decoding strategies.
- **Venue**: Top-10 LLM papers of 2026

### 1.7 Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers
- **Authors**: Pengfei Du
- **Institution**: (unspecified)
- **Date**: 2026-03-08
- **arXiv**: https://arxiv.org/abs/2603.07670
- **Abstract**: Survey of memory mechanisms for LLM agents — how to persist, organize, and selectively recall information across interactions to enable truly adaptive agents.
- **Key Innovations**: Taxonomy of agent memory mechanisms; evaluation framework; identification of emerging research frontiers.
- **Venue**: Preprint

---

## 2. CTR Prediction & Feature Interaction

### 2.1 CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **Authors**: David Pardoe, Neil Daftary, Miro Furtado, Aditya Aiyer, et al. (23 authors)
- **Institution**: LinkedIn
- **Date**: 2026-02-11
- **arXiv**: https://arxiv.org/abs/2602.11410
- **Abstract**: End-to-end decoder-only transformer for ads CTR prediction. Introduces context-conditioned decoding with multi-tower heads, self-gated attention, timestamp-based RoPE, and session masking. Achieves 11.04% CTR lift over production baseline. Deployed on LinkedIn's advertising platform for homefeed sponsored updates.
- **Key Innovations**: Context-conditioned decoding architecture; self-gated attention mechanism; timestamp-based RoPE for multi-scale temporal relationships; session masking to prevent train-serve skew; tensor packing and custom Flash Attention kernels.
- **Venue**: AdKDD 2026

### 2.2 EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling
- **Authors**: Mingyang Liu, Yong Bai, Zhangming Chan, Sishuo Chen, Xiang-Rong Sheng, Han Zhu, Jian Xu, Xinyang Chen
- **Institution**: Alibaba / Taobao
- **Date**: 2026-02-11
- **arXiv**: https://arxiv.org/abs/2602.10811
- **Abstract**: Proposes Efficiently Scalable Transformer (EST) for fully unified CTR modeling. Uses Lightweight Cross-Attention (LCA) and Content Sparse Attention (CSA) to achieve power-law scaling. Deployed on Taobao's display advertising: 3.27% RPM increase, 1.22% CTR lift.
- **Key Innovations**: Fully unified modeling without lossy aggregation; LCA for pruning redundant self-interactions; CSA for dynamic behavior selection; demonstrated stable power-law scaling for CTR; industrial deployment at Taobao.
- **Venue**: Preprint (industrial)

### 2.3 GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm
- **Authors**: Shaopeng Chen, Chuyue Xie, Huimin Ren, et al.
- **Institution**: (unspecified)
- **Date**: 2026-02-02
- **arXiv**: https://arxiv.org/abs/2602.01865
- **Abstract**: Proposes a sequence-first paradigm for CTR prediction inspired by LLM architectures, treating behavioral sequences as the primary modeling signal.
- **Key Innovations**: LLM-inspired sequence-first architecture for CTR; rethinking CTR modeling order (sequence before feature interaction).
- **Venue**: Preprint

### 2.4 HyFormer: Revisiting the Roles of Sequence Modeling and Feature Interaction in CTR Prediction
- **Authors**: Yunwen Huang*, Shiyong Hong*, Xijun Xiao*, Jinqiu Jin*, et al.
- **Institution**: ByteDance
- **Date**: 2026-01-19
- **arXiv**: https://arxiv.org/abs/2601.12681
- **Abstract**: Unified modeling framework combining long sequence modeling and feature interaction in one Transformer, replacing pipelined architectures. Validated via large-scale online A/B tests.
- **Key Innovations**: Unified Transformer for both sequence modeling and feature interaction; breaks the separated scaling paradigm; validated at industrial scale.
- **Venue**: Preprint (industrial)

### 2.5 CTR-Sink: Attention Sink for Language Models in Click-Through Rate Prediction
- **Authors**: Zixuan Li, Binzong Geng, et al.
- **Institution**: Chinese Academy of Sciences (NLPR) / Ant Group
- **Date**: 2025-08-05 (revised through 2026-08-02)
- **arXiv**: https://arxiv.org/abs/2508.03668
- **Abstract**: Addresses semantic fragmentation when applying language models to CTR prediction. Introduces CTR-Sink mechanism with two-stage training to guide LM attention toward sink tokens and amplify inter-sink dependencies.
- **Key Innovations**: Attention Sink mechanism for CTR; two-stage training strategy; addresses semantic fragmentation in user behavior sequences; code available.
- **Venue**: KDD 2026

### 2.6 From Feature Interaction to Feature Generation: A Generative Paradigm of CTR Prediction Models
- **Authors**: Mingjia Yin, Junwei Pan, Hao Wang, et al.
- **Institution**: University of Science and Technology of China (USTC)
- **Date**: 2025-12-16
- **arXiv**: https://arxiv.org/abs/2512.14041
- **Abstract**: Proposes Supervised Feature Generation (SFG) framework shifting CTR from discriminative "feature interaction" to generative "feature generation." Encoder-decoder with supervised loss from click labels. Generalizable across existing CTR models.
- **Key Innovations**: Generative paradigm for CTR; supervised feature generation with click labels; addresses embedding collapse and information redundancy; plug-and-play with existing CTR models.
- **Venue**: Preprint

### 2.7 Native Multimodal Representation Learning for Click-Through Rate Prediction in E-Commerce Scenarios
- **Authors**: Chao Yi, Feifan Yang, Jiawei Feng, et al.
- **Institution**: (unspecified, likely Alibaba)
- **Date**: 2026-08-25
- **arXiv**: https://arxiv.org/abs/2608.24091
- **Abstract**: Proposes Mine-Then-Train method to learn native multimodal representations for CTR by mining high-quality multimodally interpretable samples from CTR data for encoder fine-tuning.
- **Key Innovations**: Mine-Then-Train paradigm; native multimodal representation for CTR (not two-stage pretrain-then-freeze); addresses ambiguous supervision in multimodal CTR data.
- **Venue**: CIKM 2026

### 2.8 Generative Long-term User Interest Modeling for Click-Through Rate Prediction (GenLI)
- **Authors**: Jiangli Shao, Kaifu Zheng, Hao Fang, et al.
- **Institution**: (unspecified)
- **Date**: 2026-05-15
- **arXiv**: https://arxiv.org/abs/2605.15905
- **Abstract**: Proposes GenLI with interest generation module, behavior retrieval module, and interest fusion module. Generates multiple target-independent interest distributions for diverse interest capture with O(1) retrieval complexity.
- **Key Innovations**: Target-independent interest generation; O(1) behavior retrieval via lookup; gating-based interest fusion; better balance of accuracy and efficiency.
- **Venue**: Preprint

---

## 3. Sequential User Behavior Modeling

### 3.1 PANTHER: Generative Pretraining Beyond Language for Sequential User Behavior Modeling
- **Authors**: Guilin Li, Yun Zhang, Xiuyuan Chen, et al.
- **Institution**: WeChat Pay / Tencent
- **Date**: 2025-10-11 (revised 2026-03-30)
- **arXiv**: https://arxiv.org/abs/2510.10102
- **Abstract**: Hybrid generative-discriminative framework extending LLM-style pretraining to user behavior. Features structured tokenization, Sequence Pattern Recognition Module, unified user-profile embedding. Deployed at WeChat Pay: 25.6% boost in HitRate@1, 38.6% relative fraud detection recall improvement.
- **Key Innovations**: LLM-inspired generative pretraining for user behavior; structured tokenization of multi-dimensional transactions; offline embedding caching for millisecond-level inference; fully deployed at WeChat Pay.
- **Venue**: Preprint (industrial)

### 3.2 Generative Chain of Behavior for User Trajectory Prediction (GCB)
- **Authors**: Chengkai Huang, Xiaodi Chen, Hongtao Huang, Quan Z. Sheng, Lina Yao
- **Institution**: University of New South Wales (likely)
- **Date**: 2026-01-26
- **arXiv**: https://arxiv.org/abs/2601.18213
- **Abstract**: Generative framework modeling user interactions as autoregressive chain of semantic behaviors over multiple future steps. Uses RQ-VAE with k-means refinement for semantic IDs and Transformer-based autoregressive generator.
- **Key Innovations**: Multi-step trajectory prediction (beyond next-item); semantic ID tokenization via RQ-VAE; captures long-horizon intent transitions.
- **Venue**: Preprint

### 3.3 Beyond Positive Signals: Unlocking Implicit Negative Behaviors for Enhanced Sequential User Modeling
- **Authors**: Zexuan Cheng, Yue Liu, Jun Zhang, Jie Jiang
- **Institution**: (unspecified)
- **Date**: 2026-06-13
- **arXiv**: https://arxiv.org/abs/2606.15252
- **Abstract**: Incorporates implicit negative behaviors (e.g., items viewed but not clicked) into sequential CTR modeling, going beyond traditional positive-signal-only approaches.
- **Key Innovations**: Utilization of implicit negative behavior signals; enhanced sequential modeling with negative feedback.
- **Venue**: Preprint

### 3.4 Multi-Behavior Sequential Modeling with Transition-Aware Graph Attention Network (TGA) for E-Commerce Recommendation
- **Authors**: (multiple)
- **Institution**: (unspecified)
- **Date**: 2026-01-21
- **arXiv**: https://arxiv.org/abs/2601.14955
- **Abstract**: Linear-complexity approach for modeling multi-behavior transitions using graph attention. Addresses high computational cost of Transformer-based multi-behavior models for long sequences.
- **Key Innovations**: Linear-complexity multi-behavior modeling; transition-aware graph attention; handles behavior-type transitions as key signals.
- **Venue**: Preprint

### 3.5 Efficient Sequential Recommendation for Long User Interaction Histories
- **Authors**: (unspecified)
- **Institution**: (unspecified)
- **Date**: 2026-01-07
- **arXiv**: https://arxiv.org/abs/2601.03479
- **Abstract**: Compresses long user interaction histories into learnable tokens, combined with recent interactions, for efficient sequential recommendation.
- **Key Innovations**: Learnable token compression of long histories; efficiency-performance balance for long-sequence recommendation.
- **Venue**: Preprint

---

## 4. Advertising & Generative Recommendation

### 4.1 GR4AD: Generative Recommendation for Large-Scale Advertising
- **Authors**: Ben Xue, Dan Liu, Lixiang Wang, et al. (30 authors)
- **Institution**: Kuaishou
- **Date**: 2026-02-26
- **arXiv**: https://arxiv.org/abs/2602.22732
- **Abstract**: Production-oriented generative recommender co-designed across architecture, learning, and serving. Introduces UA-SID tokenization, LazyAR lazy autoregressive decoder, VSL value-aware supervised learning, and RSPO ranking-guided RL. Deployed at Kuaishou (400M+ users): up to 4.2% ad revenue improvement.
- **Key Innovations**: UA-SID (Unified Advertisement Semantic ID) for complex business information; LazyAR for relaxed layer-wise dependencies; RSPO for list-wise RL optimization; dynamic beam serving; deployed at Kuaishou.
- **Venue**: Under review (industrial)

### 4.2 Generative Optimization for Incentivized Advertising with Global Level Constraints
- **Authors**: (unspecified)
- **Institution**: (unspecified)
- **Date**: 2026-08-05
- **arXiv**: https://arxiv.org/abs/2608.04421
- **Abstract**: Optimizes continuous incentive magnitudes under strict global constraints for incentivized advertising campaigns.
- **Key Innovations**: Generative optimization for incentive allocation; global constraint handling.
- **Venue**: Preprint

### 4.3 Ads that Stick: Near-Optimal Ad Optimization through Psychological Behavior Models
- **Authors**: (unspecified)
- **Institution**: (unspecified)
- **Date**: 2025-09-24
- **arXiv**: https://arxiv.org/abs/2509.20304
- **Abstract**: Models user interest change upon ad exposure using three psychological principles: mere exposure, hedonic adaptation, and operant conditioning.
- **Key Innovations**: Psychology-grounded ad optimization; multi-principle behavioral modeling.
- **Venue**: Preprint

### 4.4 A Lightweight MPC Bidding Framework for Brand Auction Ads
- **Authors**: (TikTok researchers)
- **Institution**: TikTok
- **Date**: 2026-03-16
- **arXiv**: https://arxiv.org/abs/2603.07721
- **Abstract**: Model Predictive Control framework for real-time bidding in brand advertising. Leverages fast feedback loops and rich engagement data in brand campaigns. Validated on TikTok platform.
- **Key Innovations**: Lightweight MPC for brand ad bidding; exploitation of brand-specific fast feedback; validated via A/B testing on TikTok.
- **Venue**: Preprint (industrial)

### 4.5 Attribute Inference from Interactive Targeted Ads
- **Authors**: Peihao Li
- **Institution**: (unspecified)
- **Date**: 2026-06-13
- **arXiv**: https://arxiv.org/abs/2606.15209
- **Abstract**: Models interactive targeted ads as a noisy oracle for attribute inference. Studies privacy implications of advertiser-selected targeting predicates combined with identity-exposing interactions.
- **Key Innovations**: Oracle abstraction for interactive ad privacy; defense evaluation framework for disclosure control.
- **Venue**: Preprint

---

## 5. Game AI & Game Theory + RL

### 5.1 Augmenting Game AI with Deep Reinforcement Learning
- **Authors**: Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén
- **Institution**: Electronic Arts (EA), Stockholm
- **Date**: 2026-06-18
- **arXiv**: https://arxiv.org/abs/2606.20210
- **Abstract**: Vision paper proposing a framework for training RL models for game AI with requirements suited to game development (short training time, broad genre applicability). Presents examples of RL-augmented game AI and identifies bottlenecks.
- **Key Innovations**: Framework for RL game AI with practical game-dev constraints; identifies key bottlenecks for industry adoption; examples from AAA game development.
- **Venue**: Conference on Games 2026

### 5.2 Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with Large Language Models
- **Authors**: Chee Wei Tan, Yuchen Wang, Shangxin Guo
- **Institution**: Nanyang Technological University / Nautilus Software Technologies
- **Date**: 2026-04-23
- **arXiv**: https://arxiv.org/abs/2604.21896
- **Abstract**: New paradigm for AI game programming leveraging LLMs to extend Shannon's taxonomy of game-playing machines. Combines language models with strategic reasoning in imperfect-information games.
- **Key Innovations**: LLM-extended Shannon taxonomy; strategic AI gaming agents; interactive learning framework.
- **Venue**: Preprint

### 5.3 Game-Theory-Assisted Reinforcement Learning for Border Defense
- **Authors**: Goutam Das, Michael Dorothy, Kyle Volle, Daigo Shishika
- **Institution**: (unspecified, likely US military research)
- **Date**: 2026-03-16
- **arXiv**: https://arxiv.org/abs/2603.15907
- **Abstract**: Hybrid game-theory + RL approach using Apollonius Circle for early termination of RL episodes, enabling RL to focus on search strategies while guaranteeing optimal pursuit after detection.
- **Key Innovations**: Game-theoretic early termination for RL efficiency; hybrid analytical + learning approach.
- **Venue**: Preprint

### 5.4 Game Theory and Multi-Agent Reinforcement Learning: From Nash Equilibria to Evolutionary Dynamics
- **Authors**: Neil De La Fuente, Miquel Noguer i Alonso, Guim Casadellà
- **Institution**: Computer Vision Center (UAB) / AIFI / AllRead
- **Date**: 2024-12 (revised 2026-08-09)
- **arXiv**: https://arxiv.org/abs/2412.20523
- **Abstract**: Comprehensive survey on integrating game theory with MARL. Covers non-stationarity, partial observability, scalability, and decentralized learning. Analyzes Nash equilibria, evolutionary game theory, correlated equilibrium.
- **Key Innovations**: Systematic integration of game theory concepts into MARL; analysis of four fundamental MARL challenges.
- **Venue**: Preprint

### 5.5 PokaiTrainer: Scaling Belief-State Search to Competitive Pokémon VGC
- **Authors**: Max Yu
- **Institution**: (unspecified)
- **Date**: 2026-08-31
- **arXiv**: Referenced in cs.GT listings
- **Abstract**: Scales belief-state search to competitive Pokémon Video Game Championships using RL and game-theoretic methods.
- **Key Innovations**: Belief-state search scaling; competitive gaming application.
- **Venue**: Preprint

---

## 6. LLM Safety & Alignment

### 6.1 Evaluating Language Models for Harmful Manipulation
- **Authors**: Google DeepMind
- **Institution**: Google DeepMind
- **Date**: 2026-03
- **arXiv**: https://arxiv.org/abs/2603.25326
- **Abstract**: Evaluates whether LLMs can produce manipulative behavior across public policy, finance, and health contexts with 10,101 participants from US, UK, India.
- **Key Innovations**: Large-scale manipulation risk evaluation; geographic and domain-diverse testing; finding that manipulation tendency != manipulation success.
- **Venue**: Top-10 LLM papers of 2026

### 6.2 AI Alignment through a Game-theoretic Lens: A Survey
- **Authors**: Yanan Cai, Zhongrui Zhao, et al.
- **Institution**: (multiple, likely Australian universities)
- **Date**: 2026 (accepted EMNLP-2026)
- **arXiv**: Referenced in cs.GT listings
- **Abstract**: Survey of AI alignment problems viewed through game-theoretic frameworks.
- **Key Innovations**: Game-theoretic perspective on AI alignment; comprehensive survey.
- **Venue**: EMNLP 2026

---

## Summary Statistics

| Category | Papers Count |
|---|---|
| Large Language Models | 7 |
| CTR Prediction & Feature Interaction | 8 |
| Sequential User Behavior Modeling | 5 |
| Advertising & Generative Recommendation | 5 |
| Game AI & Game Theory + RL | 5 |
| LLM Safety & Alignment | 2 |
| **Total** | **32** |

## Key Trends

1. **Generative paradigm is coming to CTR**: Multiple papers (GR4AD, SFG, GRAB, CADET) are moving CTR prediction from discriminative to generative architectures, borrowing LLM-style autoregressive and diffusion techniques.

2. **Unified modeling replacing pipelined architectures**: EST, HyFormer, and CADET all move toward unified sequence modeling + feature interaction, abandoning the traditional pipeline.

3. **Industrial deployment is the gold standard**: Most impactful papers (CADET at LinkedIn, EST at Taobao, GR4AD at Kuaishou, PANTHER at WeChat Pay) include production deployment results.

4. **Scaling laws discovered for CTR**: EST demonstrates power-law scaling for CTR prediction, echoing LLM scaling laws but adapted for the asymmetric information density of recommendation features.

5. **LLM-inspired tokenization spreading to recommendation**: Semantic IDs (RQ-VAE, UA-SID) are becoming standard for converting discrete recommendation items into LLM-compatible token spaces.

6. **Game AI embracing RL + LLM hybrid**: EA's vision paper and Nemobot Games both explore combining RL with LLMs for more believable and strategically capable game agents.
