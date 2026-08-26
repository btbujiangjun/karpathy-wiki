---
title: "arXiv AI/LLM/RecSys Search Report"
type: synthesis
created: 2026-08-26
updated: 2026-08-26
tags: [arxiv, AI, LLM, recommendation, CTR, sequential-modeling, advertising, multi-agent-RL, games]
---

# arXiv AI Research Search Report — 2026-08-26

> Source: arXiv (cs.AI, cs.IR, cs.LG) | Generated from listings dated Aug 20–26, 2026

---

## 1. CTR Prediction / Click-Through Rate

### 1.1 Native Multimodal Representation Learning for CTR Prediction in E-Commerce Scenarios

- **Authors**: Chao Yi, Feifan Yang, Jiawei Feng, Sishuo Chen, Zhangming Chan, Xiang-Rong Sheng, Han Zhu
- **Institution/Company**: Alibaba (implied by author names & context)
- **Date**: 2026-08-25
- **Venue**: CIKM 2026
- **Abstract**: Addresses the gap between pre-trained multimodal encoders and downstream CTR prediction tasks. Current two-stage paradigms (pre-train then extract) suffer from misaligned objectives. Proposes a "Mine-Then-Train" method that mines high-quality, multimodally interpretable training samples from CTR data and uses them to fine-tune the multimodal encoder for better alignment with user click preferences.
- **Key Innovations**:
  - Identified that end-to-end joint training fails because raw CTR data is driven by both multimodal semantics and non-multimodal factors, causing ambiguous supervision
  - Mine-Then-Train: mines high-quality samples from CTR data that are interpretable via multimodal signals, then fine-tunes the encoder
  - Validated with both offline and online A/B experiments
- **Link**: https://arxiv.org/abs/2608.24091

### 1.2 Cascading Relevance-driven Recommendation Network for CTR Prediction in Trigger-Introduced Recommendation

- **Authors**: Kaixuan Chen, Wenwen Wang, Xing Fang, Yang Huang, Jing Wang
- **Institution/Company**: Not explicitly stated (likely industry lab)
- **Date**: 2026-08-24
- **Abstract**: Proposes CRRN for a new recommendation scenario called Trigger-Introduced Recommendation (TIR), where users click a product ("trigger item") expressing instant interest and then see relevant target items. The model emphasizes trigger-target relevance via three components: Trigger-Target Interaction layer, Cascading Interest Fusion module, and Category-assisted Pairwise Loss.
- **Key Innovations**:
  - Addresses TIR scenario where trigger signals are more implicit than search terms but stronger than standard recommendations
  - Cascading Interest Fusion: explicitly estimates trigger intention and fuses instant/personalized interests adaptively
  - Category-assisted Pairwise Loss leverages category associations between trigger and target items
- **Link**: https://arxiv.org/abs/2608.22973

### 1.3 CTR-Sink: Attention Sink for Language Models in Click-Through Rate Prediction

- **Authors**: Zixuan Li, Binzong Geng, Jing Xiong, Yong He, Yuxuan Hu, Jian Chen, Dingwei Chen, Xiyu Chang, Ngai Wong, Liang Zhang, Linjian Mo, Chengming Li, Chuan Yuan, Zhenan Sun
- **Institution/Company**: Not explicitly stated
- **Date**: Originally 2025-08-05, revised through v4 (2026-08-02)
- **Abstract**: Addresses the structural gap when using Language Models for CTR prediction — user behavior sequences are discrete actions connected by semantically empty separators, unlike coherent natural language. This causes "semantic fragmentation" where LM attention scatters across irrelevant tokens.
- **Key Innovations**:
  - Identifies "semantic fragmentation" problem in LM-based CTR prediction
  - Proposes CTR-Sink mechanism inspired by attention sink phenomena in LLMs
  - Focuses attention on meaningful behavior boundaries and inter-behavior relationships
- **Link**: https://arxiv.org/abs/2508.03668

---

## 2. Sequential Modeling / User Behavior

### 2.1 Beyond Positive Signals: Unlocking Implicit Negative Behaviors for Enhanced Sequential User Modeling

- **Authors**: Zexuan Cheng, Yue Liu, Jun Zhang, Jie Jiang
- **Institution/Company**: Tencent Inc., Beijing, China
- **Date**: 2026-06-13
- **Abstract**: Challenges the practice of constructing behavior sequences exclusively from positive interactions (clicks, purchases). Demonstrates that mixed-polarity behavior sequences — chronologically interleaving positive and negative tokens (skips, low engagement, scroll-past) — consistently outperform positive-only sequences across diverse model architectures with negligible computational overhead.
- **Key Innovations**:
  - **Mixed-Polarity Behavior Sequences**: interleaving positive and negative tokens within a fixed length budget
  - **Target-Aware Polarity Fusion (TAPF)**: lightweight target-conditioned gating mechanism to differentiate behavioral evidence
  - Even simple polarity bias captures majority of improvement, suggesting the paradigm itself is the primary contribution
  - +1.9% to +9.6% relative AUC across five architectures on three benchmarks
- **Link**: https://arxiv.org/abs/2606.15252

### 2.2 Multi-Behavior Sequential Modeling with Transition-Aware Graph Attention Network for E-Commerce Recommendation

- **Authors**: Hanqi Jin, Gaoming Yang, Zhangming Chan, Yapeng Yuan, Longbin Li, Fei Sun, Yeqiu Yang, Jian Wu, Yuning Jiang, Bo Zheng
- **Institution/Company**: Not explicitly stated (likely Alibaba/ant group based on author affiliations)
- **Date**: 2026-01-21
- **Venue**: WWW 2026 (short paper)
- **Abstract**: Proposes TGA (Transition-Aware Graph Attention Network) for modeling multi-behavior transitions in e-commerce. Unlike transformers with O(n²) complexity, TGA constructs a structured sparse graph from three perspectives: item-level, category-level, and neighbor-level transitions, achieving linear complexity.
- **Key Innovations**:
  - **Transition-Aware Graph Attention**: jointly models user-item interactions and behavior transition types on structured sparse graphs
  - **Three-perspective transition modeling**: item-level, category-level, and neighbor-level transitions
  - Linear complexity vs. polynomial complexity of transformer-based approaches
  - Deployed in large-scale industrial production
- **Link**: https://arxiv.org/abs/2601.14955

### 2.3 A Dual-Expert Strategy Integrating LLMs to Mitigate Negative Transfer in Cross-Domain Sequential Recommendation

- **Authors**: Hyeongjun Yun, Kihyuk Song, Jaegul Choo, Chung Park
- **Institution/Company**: Not explicitly stated (likely KAIST or Korean university)
- **Date**: 2026-08-24
- **Venue**: CIKM 2026
- **Abstract**: Addresses negative transfer in Cross-Domain Sequential Recommendation (CDSR) when using LLMs. LLMRec models autoregressive token-level patterns but overlooks item-level collaborative signals. Proposes DuELRec with domain-gated dual experts and contrastive learning.
- **Key Innovations**:
  - **Domain-Gated Dual Experts**: single-domain expert restricts attention within domain; cross-domain expert allows cross-domain attention; gating mechanism adaptively fuses outputs
  - **Item-Aware Attention Transformation**: aggregates textual subtokens into item-level representations with block-level attention masking
  - **Dual-Sampling Token-to-Item Contrastive Learning**: captures item-level collaborative signals from both single and cross domains
  - Outperforms 26 state-of-the-art methods on two datasets across ten domains
- **Link**: https://arxiv.org/abs/2608.23131

---

## 3. Recommendation Systems (Generative / Tokenization)

### 3.1 TAGR: Temporally Adaptive Generative Recommendation for Industrial Live-Streaming Advertising

- **Authors**: Wencai Ye, Guangyi Liu, Chaoyi Wang, Wenbin Luo, Shengyu Wang, Mingjie Sun, Peng Wang, Quanming Yao, Wenjin Wu, Peng Jiang
- **Institution/Company**: Likely Pinduoduo or major Chinese e-commerce platform
- **Date**: 2026-08-25
- **Abstract**: Proposes a generative recommendation framework with temporal adaptation at three levels for live-streaming advertising: tokenization (LSID — Live Semantic-Collaborative ID), intent modeling (Intent-Aware Generation), and preference alignment (Intermittent On-Policy Preference Optimization). Deployed on large-scale e-commerce platform.
- **Key Innovations**:
  - **Live Semantic-Collaborative ID (LSID)**: periodically refreshes each active ad's SID based on current live scene and products while retaining stable hierarchical token vocabulary
  - **Intent-Aware Generation (IAG)**: models live-room entry histories at multiple temporal granularities; weights NTP using post-request intent evidence and business value
  - **Intermittent On-Policy Preference Optimization (IOPO)**: periodically samples fresh candidates for behavior- and value-aligned preference updates
  - **Deployment results**: +8.5% live-room entry rate, +7.4% shopping-cart click rate, +16.1% revenue lift
- **Link**: https://arxiv.org/abs/2608.24034

### 3.2 Tlow: Flow-based Item Tokenizer for Recommendation

- **Authors**: Nian Li, Chonggang Song, Jingtao Ding, Lingling Yi, Yong Li, Qingmin Liao
- **Institution/Company**: Likely Tsinghua University (Yong Li) / WeChat (Tencent)
- **Date**: 2026-08-25
- **Venue**: CIKM 2026 (Applied Research)
- **Abstract**: Addresses limitations of RQ-VAE tokenizer (low decoding efficiency due to codebook dependencies) and OPQ (struggles with dimensional correlations). Proposes flow-based item tokenizer that transforms embeddings into a latent space with standard normal distribution.
- **Key Innovations**:
  - **Flow-based transformation**: maps semantic embeddings to standard normal distribution, enabling both dimensional independence and distributional simplicity
  - **Codebook Guidance**: aligns codebook space with token embedding space for more semantically distinct token embeddings
  - **Online results on WeChat**: +10.32% global CTR, +11.64% CTR for new items
- **Link**: https://arxiv.org/abs/2608.24176

### 3.3 Rethinking Item Tokenization in Generative Recommenders: From Fixed Atoms to Semantic Subwords

- **Authors**: Xinrui Miao, Mingjia Yin, Jiaqing Zhang, Wei Guo, Yong Liu, Yuyang Ye, Hao Wang, Enhong Chen
- **Institution/Company**: Likely University of Science and Technology of China (USTC) / industry coauthors
- **Date**: 2026-08-24
- **Venue**: CIKM 2026
- **Abstract**: Identifies "Intra-item Attention Overload" problem in generative recommenders using fixed-length token sequences — excessive attention on low-level intra-item dependencies rather than high-level inter-item behavioral transitions. Proposes Semantic Subword Tokenization (SST).
- **Key Innovations**:
  - **Semantic Subword Tokenization (SST)**: variable-length semantic subwords for historical items while preserving fixed-length target decoding
  - **Item-level Subword Tokenization (IST)**: merges stable adjacent atom tokens into compact semantic subwords
  - **Behavior-induced Co-occurrence Augmentation (BCA)**: injects coarse-grained semantic prefix transition signals
  - Validated across three public datasets and three generative recommender backbones
- **Link**: https://arxiv.org/abs/2608.22734

### 3.4 RecGPT-Mobile-V2 Technical Report

- **Authors**: Lingqing Zhang, Bin Zhang, Weipeng Huang, Chengfei Lv, et al. (28 authors)
- **Institution/Company**: Not explicitly stated (likely Alibaba/Alibaba DAMO or Meituan)
- **Date**: 2026-08-25
- **Abstract**: End-to-end framework for personalized query prediction mapping implicit behavioral signals to explicit retrieval intent. Handles on-device deployment challenges: noisy multi-scale trajectories, multiple valid queries per trajectory, and variable computation needs. Uses staged design with domain adaptation, RL-based reasoning optimization, and distillation to compact student model.
- **Key Innovations**:
  - **Evidence-preserving trajectory transformation**: converts heterogeneous interactions into structured trajectories
  - **RL-based reasoning cost optimization**: grouped rollouts meet grounding and utility criteria before optimization
  - **Sufficiency-oriented reasoning**: retains decision-relevant evidence, allocates additional computation only when likely to improve prediction
  - Median CoT length reduced from 62 to 14 tokens; Query quality from 73.2% to 78.6%; hard-failure rate from 3.6% to 1.6%
- **Link**: https://arxiv.org/abs/2608.24295

### 3.5 Rethinking Semantic Alignment in LLM-Enhanced Collaborative Filtering: A Spectral Decoupling Approach

- **Authors**: Yedong Jin, Shaowen Peng, Tsunenori Mine, Shoko Wakamiya, Eiji Aramaki
- **Institution/Company**: Likely Kyushu Institute of Technology (Japan)
- **Date**: 2026-08-25
- **Abstract**: Shows from a spectral perspective that collaborative signals (low-frequency, smooth) and semantic signals (non-principal singular components) benefit from different spectral parts. Standard alignment training concentrates representations in dominant subspaces, reducing overlap with useful non-principal semantic components.
- **Key Innovations**:
  - **Spectral analysis of LLM-enhanced CF**: reveals alignment concentrates representations in dominant subspaces, losing useful non-principal semantic information
  - **UniSpecRec**: applies signal-specific spectral filtering while preserving collaborative and semantic representations in separate spaces
  - Combines predictions without cross-space alignment or additional trainable parameters
- **Link**: https://arxiv.org/abs/2608.24363

---

## 4. Advertising

### 4.1 TAGR (see Section 3.1)

- Temporally adaptive generative recommendation for live-streaming advertising
- Deployed on large-scale e-commerce platform with significant business metrics improvement

### 4.2 Auditing Return Conditioning as a Control Knob: An Offline Diagnostic for Decision Transformer Recommendation

- **Authors**: Jingyu Wang
- **Institution/Company**: Not explicitly stated
- **Date**: 2026-08-26
- **Venue**: CONSEQUENCES '26 Workshop (RecSys 2026)
- **Abstract**: Provides offline diagnostic methodology for Decision Transformer-based recommendation models, examining how return conditioning acts as a control knob for recommendation quality.
- **Key Innovations**:
  - Offline diagnostic framework for Decision Transformer recommendation
  - Analyzes return conditioning as controllable parameter
- **Link**: https://arxiv.org/abs/2608.24815

### 4.3 When Ads Become Profiles: Uncovering the Invisible Risk of Web Advertising at Scale with LLMs

- **Authors**: Not fully detailed from search
- **Date**: 2025-09-23
- **Abstract**: Investigates how adversaries can exploit ad exposure signals to reverse-engineer private attributes from ad exposure alone. Introduces a novel pipeline leveraging LLMs as adversarial inference engines for natural language profiling.
- **Key Innovations**:
  - Demonstrates privacy risks from ad exposure data
  - LLM-powered adversarial inference pipeline for profiling from ad signals
- **Link**: https://arxiv.org/abs/2509.18874

---

## 5. LLM Inference & Serving

### 5.1 Challenges and Research Directions for Large Language Model Inference Hardware

- **Authors**: Xiaoyu Ma, David Patterson
- **Institution/Company**: Google (David Patterson is a well-known Google Fellow)
- **Date**: 2026-01-08
- **Abstract**: Analyzes LLM inference challenges, arguing the autoregressive Decode phase makes inference fundamentally different from training. Primary challenges are memory and interconnect rather than compute.
- **Key Innovations**:
  - Comprehensive analysis of LLM inference hardware challenges
  - Identifies memory and interconnect as primary bottlenecks (not compute)
  - Research directions for next-gen inference hardware
- **Link**: https://arxiv.org/abs/2601.05047

### 5.2 MARLIN: Multi-Agent Game-Theoretic Reinforcement Learning for Sustainable LLM Inference in Cloud Datacenters

- **Authors**: Not fully detailed from search
- **Date**: 2026-05-13
- **Abstract**: Uses multi-agent game-theoretic RL to optimize LLM inference scheduling in cloud datacenters for sustainability (energy/cost efficiency).
- **Key Innovations**:
  - Game-theoretic formulation for LLM inference scheduling
  - Multi-agent RL approach for sustainable cloud LLM serving
- **Link**: https://arxiv.org/abs/2605.13496

---

## 6. Multi-Agent RL / Games

### 6.1 MEAL: A Benchmark for Continual Multi-Agent Reinforcement Learning

- **Authors**: Tristan Tomilin, Luka van den Boogaard, Samuel Garcin, Constantin Ruhdorfer, Bram Grooten, Fabrice Kusters, Yali Du, Andreas Bulling, Mykola Pechenizkiy, Meng Fang
- **Institution/Company**: Eindhoven University of Technology; University of Cambridge; IMRS-IS
- **Date**: 2026-06-18
- **Abstract**: Introduces a GPU-accelerated benchmark for continual multi-agent RL enabling long task sequences (previously limited to 3-10 due to CPU-bound environments). Uses a cooperative cooking game scenario.
- **Key Innovations**:
  - GPU-accelerated MARL benchmark enabling long task sequences
  - First benchmark for continual learning in cooperative multi-agent settings
  - Reduces energy footprint: hours on single GPU vs. large clusters
- **Link**: https://arxiv.org/abs/2506.14990

### 6.2 Generalized Intention Modeling in Multi-Agent Reinforcement Learning

- **Authors**: Mateusz Odrowaz-Sypniewski, Jasmine Bayrooti, Ajay Shankar, Amanda Prorok
- **Institution/Company**: University of Cambridge
- **Date**: 2026-05-29
- **Abstract**: Addresses opponent intent modeling for effective decision-making in non-cooperative, competitive, and general-sum MARL settings.
- **Key Innovations**:
  - Generalized framework for opponent intent modeling
  - Applicable across competitive and general-sum game settings
- **Link**: https://arxiv.org/abs/2605.31318

### 6.3 Fluid-Agent Reinforcement Learning

- **Authors**: Shishir Sharma, Doina Precup, Theodore J. Perkins
- **Institution/Company**: Mila – Quebec AI Institute; McGill University; University of Ottawa
- **Date**: 2026-02-14
- **Abstract**: Proposes a framework for MARL where the number of agents is not fixed — agents can create other agents (e.g., cell division, company spinoffs). Defines "fluid-agent environments" and provides theoretical foundations.
- **Key Innovations**:
  - First framework for MARL with dynamic agent populations
  - Theoretical analysis of equilibria in fluid-agent settings
  - Real-world motivated scenarios (biological systems, organizational dynamics)
- **Link**: https://arxiv.org/abs/2602.14559

### 6.4 Markov Potential Game and Multi-Agent Reinforcement Learning for Autonomous Driving

- **Authors**: Huiwen Yan, Mushuang Liu
- **Institution/Company**: Virginia Tech
- **Date**: 2026-03-19
- **Abstract**: Models autonomous driving as Markov potential games, where Nash equilibria are the desired solution. Addresses interactions among vehicles, bicycles, and pedestrians.
- **Key Innovations**:
  - Markov potential game formulation for multi-vehicle interactions
  - Practical MARL framework for autonomous driving scenarios
- **Link**: https://arxiv.org/abs/2603.19188

---

## 7. Multimodal / Representation Learning

### 7.1 HMGCLIP: Heterogeneous Multi-Granularity Contrastive Learning for E-commerce Representation Learning

- **Authors**: Qiuyu Zhu, Yi Gao, Zhichao Wan, Mingyang Ma
- **Institution/Company**: Not explicitly stated
- **Date**: 2026-08-26
- **Abstract**: Applies multi-granularity contrastive learning with CLIP for e-commerce representation learning, handling heterogeneous data types.
- **Key Innovations**:
  - Heterogeneous multi-granularity contrastive learning framework
  - CLIP-based representation learning for e-commerce
- **Link**: https://arxiv.org/abs/2608.24467

### 7.2 Towards a Densing Law for User Representation Learning at Billion-Scale Capacity

- **Authors**: Bin Dou, Junru Zhang, Zhaoyi Yuan, Wuliang Huang, Letian Gong, Baokun Wang, Huan Li, Yu Cheng, Weiqiang Wang
- **Institution/Company**: Not explicitly stated (likely industry)
- **Date**: 2026-08-25
- **Abstract**: Proposes a "densing law" for user representation learning at billion-scale capacity, analogous to scaling laws for language models.
- **Key Innovations**:
  - **Densing Law**: empirical scaling law for user representation capacity
  - Billion-scale user representation learning
  - Technical report format with comprehensive analysis
- **Link**: https://arxiv.org/abs/2608.23392

---

## 8. Unified Ranking Models / Feature Interaction

### 8.1 UniRank: Benchmarking Ranking Models for Unified Sequential Modeling and Feature Interaction

- **Authors**: Multiple authors (referenced extensively in search results)
- **Date**: 2026-07 (approx.)
- **Abstract**: Comprehensive benchmark comparing stacked vs. layer-wise unified interaction paradigms for recommendation across multiple datasets (KuaiRand, TencentGR-10M, Taobao, MerRec). Evaluates models including HeMix, UniMixer, TokenFormer, EST, UltraHSTU, TokenMixer-Large, SSR.
- **Key Innovations**:
  - Unified evaluation protocol across diverse platform types (short-video, e-commerce, advertising)
  - Finding: neither stacked nor layer-wise paradigm consistently dominates
  - Platform-specific inductive biases transfer best across similar platforms
  - No single model performs best across all tasks within same dataset
- **Link**: See https://arxiv.org/abs/2607.19987

---

## Summary of Trends

| Trend | Key Papers | Signal |
|-------|-----------|--------|
| **Generative Recommenders / Tokenization** | TAGR, Tlow, SST, RecGPT-V2 | Strong — industrial deployment, major platforms investing |
| **Negative/Mixed Polarity Signals** | Beyond Positive Signals | Emerging — simple yet effective paradigm shift |
| **LLM × Recommendation** | DuELRec, UniSpecRec, RecGPT-V2 | Maturing — moving beyond naive alignment to careful spectral/structural design |
| **Multi-Behavior Modeling** | TGA, Beyond Positive Signals | Active — graph-based & polarity-aware approaches |
| **Multi-Agent RL for Systems** | MARLIN, MEAL | Growing — applying MARL to LLM serving & benchmarks |
| **CTR Prediction** | Native Multimodal, CRRN, CTR-Sink | Steady — multimodal fusion & new scenarios (TIR) |
| **Scaling Laws for RecSys** | Densing Law | Early — applying LLM-style scaling analysis to user representations |
| **Item Tokenization** | Tlow, SST | Hot topic — flow-based & subword approaches replacing RQ-VAE |

---

*Report generated: 2026-08-26*
*Sources: arXiv cs.AI, cs.IR, cs.LG listings (Aug 20–26, 2026); individual paper pages*
