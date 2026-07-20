---
title: "arXiv Daily Report — 2026-07-20"
type: synthesis
created: 2026-07-20
updated: 2026-07-20
tags: [arxiv, daily-report, LLM, recommendation, CTR, sequential-modeling, advertising, game-AI]
---

# arXiv Daily Report — 2026-07-20

Curated papers from recent arXiv submissions across AI, LLMs, recommendation systems, advertising/CTR, sequential modeling, and game AI.

---

## 1. Generative Recommendation & LLM-based RecSys

### 1.1 Unleashing the Native Recommendation Potential: LLM-Based Generative Recommendation via Structured Term Identifiers
- **Authors:** Qihang Luo, Ruiming Tang, Han Li, Kun Gai, Guorui Zhou (+ others)
- **Affiliation:** [Not explicitly stated in search results]
- **Date:** 2026-01-11
- **Abstract:** Proposes Structured Term Identifiers to bridge the gap between text-based and Semantic ID methods for LLM-based generative recommendation. Addresses hallucination from LLM's vast output space and the semantic gap between SIDs and LLM's native vocabulary. Introduces a structured identifier scheme that aligns with the LLM's token vocabulary without costly expansion.
- **Key Innovation:** Structured Term Identifiers that exploit the LLM's native vocabulary for item representation, eliminating vocabulary expansion and alignment training overhead.
- **Link:** https://arxiv.org/abs/2601.06798

### 1.2 Scaling Laws for LLM Recommendation with Synthetic Data
- **Authors:** Benyu Zhang, Qiang Zhang, Jianpeng Cheng, Hong-You Chen, Qifei Wang, Wei Sun, Shen Li, Jia Li, Jiahao Wu, Xiangjun Fan, Hong Yan
- **Affiliation:** [Not explicitly stated]
- **Date:** 2026-02-07
- **Abstract:** Introduces a layered framework for generating high-quality synthetic data to create a pedagogical curriculum for LLMs in recommendation. Demonstrates standard sequential models trained on synthetic data outperform (+130% on recall@100 for SasRec) models trained on real data. Establishes the first robust power-law scaling for an LLM continually pre-trained on recommendation-specific data.
- **Key Innovation:** Principled synthetic data generation framework that enables the first demonstration of predictable power-law scaling laws for LLMs in recommendation.
- **Link:** https://arxiv.org/abs/2602.07298

### 1.3 LLM4Rec: Large Language Models for Multimodal Generative Recommendation with Causal Debiasing
- **Authors:** Bo Ma, Hang Li, ZeHua Hu, XiaoFan Gui, LuYao Liu, Simon Lau
- **Affiliation:** [Not explicitly stated]
- **Date:** 2025-10-02
- **Abstract:** Enhanced generative recommendation framework addressing multimodal data handling, algorithmic bias elimination, and transparent decision-making. Incorporates five innovations: multimodal fusion architecture, retrieval-augmented generation, causal inference-based debiasing, explainable recommendation generation, and real-time adaptive learning. Achieves up to 2.3% improvement in NDCG@10 and 1.4% enhancement in diversity.
- **Key Innovation:** Causal inference-based debiasing combined with multimodal fusion and RAG mechanisms in a unified generative recommendation framework.
- **Link:** https://arxiv.org/abs/2510.01622

### 1.4 Incumbent Advantage: Brand Bias and Cognitive Manipulation Dynamics in LLM Recommendation Systems
- **Authors:** Xi Chu, Yupeng Hou
- **Affiliation:** [Not explicitly stated]
- **Date:** 2026-06-16
- **Abstract:** Studies brand competition dynamics in LLM recommendations using skincare products across GPT-4o-mini, Claude Sonnet, and Gemini 3 Flash. Discovers a "Conditional Monopoly" where well-known brands get recommended 100% of the time when specs are equal, authority-style marketing language can break this monopoly, and multi-brand GEO competition creates a social dilemma with Nash equilibrium dynamics.
- **Key Innovation:** First systematic study of brand bias and Generative Engine Optimization (GEO) as game-theoretic competition in LLM recommendation systems.
- **Link:** https://arxiv.org/abs/2606.17443

### 1.5 A Survey on Generative Recommendation: Data, Model, and Tasks
- **Authors:** Min Hou, Le Wu, Yuxin Liao, Yonghui Yang, Zhen Zhang, Yu Wang, Changlong Zheng, Han Wu, Richang Hong
- **Affiliation:** [Not explicitly stated]
- **Date:** 2025-10-31 (revised 2026-05-09)
- **Abstract:** Comprehensive survey of generative recommendation through a unified tripartite framework spanning data, model, and task dimensions. Covers data augmentation/unification, model alignment/training (LLM-based, large recommendation models, diffusion approaches), and task formulation/execution. Identifies five key advantages: world knowledge integration, natural language understanding, reasoning capabilities, scaling laws, and creative generation.
- **Key Innovation:** Unified tripartite framework (data-model-task) for systematically organizing and analyzing the generative recommendation paradigm.
- **Link:** https://arxiv.org/abs/2510.27157

---

## 2. CTR Prediction & Advertising

### 2.1 EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling
- **Authors:** Mingyang Liu, Yong Bai, Zhangming Chan, Sishuo Chen, Xiang-Rong Sheng, Han Zhu, Jian Xu, Xinyang Chen
- **Affiliation:** [Not explicitly stated]
- **Date:** 2026-02-11
- **Abstract:** Addresses the information bottleneck in CTR prediction caused by early aggregation of user behaviors. Identifies two critical properties distinguishing CTR from LLMs: asymmetry in information density between behavioral and non-behavioral features, and modality-specific priors of content-rich signals. Proposes unified modeling that preserves fine-grained, token-level signals.
- **Key Innovation:** Unified modeling framework that preserves token-level behavioral signals for efficient scaling in CTR prediction, identifying CTR-specific scaling properties.
- **Link:** https://arxiv.org/abs/2602.10811

### 2.2 CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer
- **Authors:** Ruoyan Wang (+ LinkedIn team)
- **Affiliation:** LinkedIn
- **Date:** 2026-02-11
- **Abstract:** Introduces a decoder-only Transformer for ad CTR prediction with five key innovations: (1) context-conditioned decoding with multi-tower prediction heads modeling post-scoring signals; (2) self-gated attention for stable training; (3) timestamp-based RoPE capturing temporal relationships from seconds to months; (4) session masking to prevent train-serve skew; (5) production engineering with tensor packing, sequence chunking, and custom Flash Attention kernels. Achieves 11.04% CTR lift in online A/B testing vs. LiRank baseline. Deployed on LinkedIn's advertising platform.
- **Key Innovation:** Decoder-only Transformer architecture for ad CTR with timestamp-aware RoPE, session masking, and production-grade efficiency, achieving 11% CTR lift at LinkedIn scale.
- **Link:** https://arxiv.org/abs/2602.11410

### 2.3 COINS: SemantiC Ids Enhanced COLd Item RepresentatioN for CTR Prediction in E-commerce Search
- **Authors:** Qihang Zhao, Zhongbo Sun, Xiaoyang Zheng, Xian Guo, Siyuan Wang, Zihan Liang, Mingcan Peng, Ben Chen, Chenyi Lei
- **Affiliation:** University of Science and Technology of China, Kuaishou Technology
- **Date:** 2026-01-15
- **Abstract:** Enhances cold-start item representations for CTR prediction by adaptively fusing hierarchical semantic IDs with collaborative signals. Demonstrates improved AUC/GAUC offline, boosts online buyers by 1.720% and order volume by 2.230% overall, with even greater gains for new items.
- **Key Innovation:** Adaptive fusion of hierarchical semantic IDs with collaborative signals specifically targeting the cold-start problem in e-commerce CTR prediction.
- **Link:** https://arxiv.org/abs/2510.12604

### 2.4 Disentangled Interest Network for Out-of-Distribution CTR Prediction (DiseCTR)
- **Authors:** [Multiple authors]
- **Affiliation:** [Not explicitly stated]
- **Date:** 2026-02-02
- **Abstract:** Introduces a causal perspective to CTR prediction, disentangling user interest, exposure model, and click model. Uses sparse attention interest encoder and weakly supervised interest disentangler. Achieves best accuracy and robustness in OOD recommendation, improving AUC and GAUC by over 0.02 and reducing logloss by over 13.7%. Accepted by ACM TOIS.
- **Key Innovation:** Causal factorization of CTR into user interest × exposure × click, with disentangled interest embeddings for OOD generalization.
- **Link:** https://arxiv.org/abs/2602.00002

### 2.5 ML-DCN: Pinterest Ads Ranking Model
- **Authors:** [Pinterest team]
- **Affiliation:** Pinterest
- **Date:** 2026-02 (estimated from content)
- **Abstract:** Presents ML-DCN, an ads ranking model for Pinterest's advertising ecosystem. Discusses CTR prediction using three feature types (Pin/item, user, and user-Pin interaction features). Builds upon DCNv2 and MaskNet architectures for feature interaction learning.
- **Key Innovation:** Multi-layer DCN architecture adapted for Pinterest's advertising ecosystem at scale.
- **Link:** https://arxiv.org/abs/2602.09194

---

## 3. Sequential Recommendation & User Behavior Modeling

### 3.1 Beyond Positive Signals: Unlocking Implicit Negative Behaviors for Enhanced Sequential User Modeling
- **Authors:** Zexuan Cheng, Yue Liu, Jun Zhang, Jie Jiang
- **Affiliation:** [Not explicitly stated]
- **Date:** 2026-06-13
- **Abstract:** Challenges the convention of constructing behavior sequences exclusively from positive interactions. Demonstrates that mixed-polarity sequences (chronologically interleaving positive and negative tokens) consistently outperform positive-only sequences across diverse model architectures with negligible computational overhead. Proposes Target-Aware Polarity Fusion (TAPF) for differentiating behavioral evidence. Achieves +1.9% to +9.6% relative AUC improvement across five architectures.
- **Key Innovation:** Mixed-polarity behavior sequences paradigm incorporating implicit negative behaviors (skips, low engagement, scroll-past) into sequential modeling.
- **Link:** https://arxiv.org/abs/2606.15252

### 3.2 SRPFN: One Sequential Recommendation Model Pretrained from Synthetic Priors Predicts Multiple Datasets
- **Authors:** Woosung Kang, Jiwon Jeong, Jonghyeok Shin, Jeongwhan Choi, Noseong Park
- **Affiliation:** [Not explicitly stated]
- **Date:** 2026-06-14
- **Abstract:** Proposes a Prior-data Fitted Network (SRPFN) that predicts next items in a single forward pass without gradient-based parameter updates. Pretrained on 25.6M synthetic sequences spanning diverse transition patterns. Achieves 7.53% average improvement over baselines across five benchmarks while running inference in ~1 minute vs. minutes-to-hours for trained baselines. Accepted at KDD 2026.
- **Key Innovation:** Update-free inference paradigm using synthetic priors — a single pretrained model generalizes across diverse real-world recommendation domains.
- **Link:** https://arxiv.org/abs/2606.15752

### 3.3 Efficient Sequential Recommendation for Long User Interaction Histories (PerSRec)
- **Authors:** Qiang Zhang, Xinyang Wang, Christopher E. Lambert, Ren Chen, Chen Kovacs, Xinzhu Bei, Renqin Cai, Rui Li, Lizhu Zhang, Xiangjun Fan, Qunshu Zhang, Benyu Zhang
- **Affiliation:** Meta (Facebook Research)
- **Date:** 2026-01-07
- **Abstract:** Compresses long user interaction histories into learnable tokens combined with recent interactions, significantly reducing computational costs while maintaining accuracy. Applicable to existing Transformer-based recommendation models (e.g., HSTU and HLLM). Accepted at ICDM 2025.
- **Key Innovation:** Personalization-based history compression into learnable tokens for efficient long-sequence recommendation, applicable as a plug-in to existing architectures.
- **Link:** https://arxiv.org/abs/2601.03479

### 3.4 Do Recommendation Algorithms Work When Users Are LLM Agents? (Moltbook)
- **Authors:** Daming Li, Simeng Han, Jialu Zhang
- **Affiliation:** [Not explicitly stated]
- **Date:** 2026-06-29
- **Abstract:** Studies whether recommendation algorithms designed for humans work when users are LLM agents. Evaluates nine methods on Moltbook (a social media platform for autonomous AI agents on OpenClaw). Finds that popularity-based rules or item-side collaborative filtering outperform user-representation-based methods, and static persona descriptions fail to add prediction value. Structural signals matter more than personalization for agent users.
- **Key Innovation:** First systematic study revealing that standard personalization-based recommendation fails for LLM agent users, suggesting structural signals dominate.
- **Link:** https://arxiv.org/abs/2606.29762

### 3.5 RecPO: Preference Optimization with Intensity and Temporal Context for LLM Recommendation
- **Authors:** Zhongyu Ouyang, Qianlong Wen, Chunhui Zhang, Yanfang Ye, Soroush Vosoughi
- **Affiliation:** [Not explicitly stated]
- **Date:** 2025-06-02 (revised 2026-04-16)
- **Abstract:** Reveals that existing LLM preference alignment relies on binary pairwise comparisons, overlooking preference intensity and temporal context. Proposes RecPO that maps both explicit and implicit feedback into common preference signals with adaptive reward margins. Consistently outperforms baselines across five datasets, exhibiting human-like decision patterns. Accepted at ACL 2026.
- **Key Innovation:** Unified preference optimization framework incorporating preference intensity (structured strength) and temporal context (recency weighting) for LLM-based recommendation.
- **Link:** https://arxiv.org/abs/2506.02261

### 3.6 HORIZON: A Benchmark for in-the-wild User Behavior Modelling
- **Authors:** Arnav Goel, Pranjal A. Chitale, Bhawna Paliwal, Bishal Santra, Amit Sharma
- **Affiliation:** Carnegie Mellon University, Microsoft Research India, UC Berkeley
- **Date:** 2026-04 (estimated)
- **Abstract:** Benchmark for temporally robust, cross-domain user behavior modeling. Evaluates sequential recommendation architectures and LLM-based baselines on temporal generalization, sequence-length variation, and unseen user modeling. Establishes HORIZON as a foundation for general-purpose user models.
- **Key Innovation:** Comprehensive benchmark addressing temporal generalization and cross-domain generalization gaps in current sequential recommendation research.
- **Link:** https://arxiv.org/abs/2604.17259

---

## 4. Game AI & Multi-Agent Systems

### 4.1 Augmenting Game AI with Deep Reinforcement Learning
- **Authors:** Alessandro Sestini (+ others)
- **Affiliation:** [Not explicitly stated]
- **Date:** 2026-06-18
- **Abstract:** Vision paper from Conference on Games 2026 surveying how RL can create more believable game AI. Identifies key bottlenecks: sample efficiency, generalization, and the tension between optimal and believable behavior. Proposes a genre-level readiness framework for game studio AI teams. Notes that RL game AI has shipped in production but mostly in constrained single-skill scenarios.
- **Key Innovation:** Genre-level readiness framework for deploying RL-based game AI, identifying believability (not optimality) as the hard problem.
- **Link:** https://arxiv.org/abs/2606.20210

### 4.2 SMAC-Talk: Natural Language Extension of StarCraft Multi-Agent Challenge for LLMs
- **Authors:** Joel Sol, Homayoun Najjaran
- **Affiliation:** [Not explicitly stated]
- **Date:** 2026-06-04
- **Abstract:** Introduces SMAC-Talk, a natural language extension of the StarCraft Multi-Agent Challenge for evaluating LLM-based cooperative multi-agent coordination. Bridges the gap between language-grounded planning and tactical coordination in multi-agent settings.
- **Key Innovation:** Natural language interface for StarCraft multi-agent scenarios enabling evaluation of LLM-based cooperative coordination.
- **Link:** https://arxiv.org/abs/2606.04202

### 4.3 Insurance of Agentic AI
- **Authors:** Quanyan Zhu
- **Affiliation:** [Not explicitly stated]
- **Date:** 2026-06
- **Abstract:** Cross-listed in cs.AI, cs.GT (game theory), and econ.EM. Addresses insurance frameworks for agentic AI systems, applying game-theoretic analysis to the economics of AI agent liability and risk management.
- **Key Innovation:** Game-theoretic insurance framework for managing risk and liability in deployed agentic AI systems.
- **Link:** https://arxiv.org/abs/2606.05449

### 4.4 Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning (SAO)
- **Authors:** Zhenyu Hou, Yujiang Li, Jie Tang, Yuxiao Dong
- **Affiliation:** [Not explicitly stated]
- **Date:** 2026-07-08
- **Abstract:** Addresses instability in asynchronous RL for LLM post-training. Replaces group-wise sampling (GRPO) with single-rollout sampling per prompt and introduces strict double-side token-level clipping. Trains stably for 1000 steps and outperforms GRPO on SWE-Bench Verified, BeyondAIME, and IMOAnswerBench. Deployed for training GLM-5.2 (750B-A40B).
- **Key Innovation:** Single-rollout asynchronous optimization (SAO) with practical value-model training and double-side clipping for stable, effective agentic RL.
- **Link:** https://arxiv.org/abs/2607.07508

---

## 5. LLM Embedding & Representation for Recommendation

### 5.1 ACE: Anisotropy-Controllable Embedding for LLM-enhanced Sequential Recommendation
- **Authors:** Dongcheol Lee, Hye-young Kim, Jongwuk Lee
- **Affiliation:** [Not explicitly stated]
- **Date:** 2026-05-28
- **Abstract:** Addresses anisotropy in LLM-generated embeddings where vectors concentrate in similar directions. Uses a linear autoencoder (LAE) with L2-regularization to control dispersion while preserving semantic structure. Achieves up to 12.4% and 11.8% improvement in Recall@20 and NDCG@20. Accepted at SIGIR 2026.
- **Key Innovation:** Anisotropy-controllable embedding framework balancing geometric uniformity and semantic preservation for LLM-enhanced sequential recommendation.
- **Link:** https://arxiv.org/abs/2605.29322

### 5.2 SpecTran: Spectral-Aware Transformer-based Adapter for LLM-Enhanced Sequential Recommendation
- **Authors:** Yu Cui, Feng Liu, Zhaoxiang Wang, Changwang Zhang, Jun Wang, Can Wang, Jiawei Chen
- **Affiliation:** Zhejiang University, OPPO Research Institute
- **Date:** 2026-01-29
- **Abstract:** Addresses dimension collapse in adapter-based methods and information loss in SVD-based methods for injecting LLM embeddings into sequential recommenders. Operates in the spectral domain with learnable spectral-position encoding. Achieves average improvement of 9.17% across four datasets and three backbones.
- **Key Innovation:** Spectral-domain adapter that attends to the full spectrum (not just principal components) with learnable spectral-position encoding for LLM embedding injection.
- **Link:** https://arxiv.org/abs/2601.21986

### 5.3 MLTFR: Multi-LLM Token Filtering and Routing for Sequential Recommendation
- **Authors:** Wuhan Chen, Min Gao, Xin Xia, Zongwei Wang, Wentao Li, Shane Culpepper
- **Affiliation:** Chongqing University, University of Queensland, University of Leicester
- **Date:** 2026-04-20
- **Abstract:** Investigates whether recommendation can benefit from LLM token embeddings alone without textual input. Shows single-LLM token injection leads to unstable/limited gains due to semantic misalignment, insufficient task adaptation, and restricted coverage. Proposes multi-LLM token filtering and routing framework for corpus-free sequential recommendation.
- **Key Innovation:** Multi-LLM token filtering and routing that mitigates individual LLM limitations for corpus-free sequential recommendation.
- **Link:** https://arxiv.org/abs/2604.18200

---

## 6. Multimodal & Cross-domain

### 6.1 MaRCA: Multi-Agent Reinforcement Learning for Dynamic Computation Allocation in Large-Scale Recommender Systems
- **Authors:** Wan Jiang, Xinyi Zang, Yudong Zhao, Yusi Zou, Yunfei Lu, Junbo Tong, Yang Liu, Ming Li, Jiani Shi, Xin Yang
- **Affiliation:** [Leading global e-commerce platform — likely Alibaba]
- **Date:** 2025-12-31
- **Abstract:** Multi-agent RL framework for end-to-end computation resource allocation in large-scale recommender systems. Models pipeline stages as cooperative agents using CTDE. Includes AutoBucket TestBench for cost estimation and MPC-based Revenue-Cost Balancer. Deployed since November 2024, handles hundreds of billions of ad requests/day with 16.67% revenue uplift.
- **Key Innovation:** End-to-end multi-agent RL for computation allocation across recommender pipeline stages, achieving 16.67% revenue uplift at industrial scale.
- **Link:** https://arxiv.org/abs/2512.24325

### 6.2 On-Device Large Language Models for Sequential Recommendation (OD-LLM)
- **Authors:** Xin Xia, Hongzhi Yin, Shane Culpepper
- **Affiliation:** [Not explicitly stated]
- **Date:** 2026-01-14
- **Abstract:** First task-adaptive compression framework for deploying LLMs on-device for sequential recommendation. Combines SVD-based low-rank compression with tokenization normalization and progressive layer-wise alignment. Halves model size with no effectiveness loss.
- **Key Innovation:** Combined low-rank compression + tokenization normalization + progressive alignment for on-device LLM deployment in sequential recommendation.
- **Link:** https://arxiv.org/abs/2601.09306

---

## Summary of Key Trends

| Trend | Papers | Signal |
|-------|--------|--------|
| **Scaling Laws for Rec** | EST, Scaling Laws (synthetic data), Wukong references | CTR/recsys is entering the scaling era — power-law behavior validated |
| **Negative Behavior Signals** | Beyond Positive Signals | Rich signal in implicit negative behaviors; mixed-polarity sequences |
| **LLM Agent Users** | Moltbook | Recommendation for AI agents ≠ recommendation for humans; structural signals dominate |
| **Synthetic Priors / Zero-shot Rec** | SRPFN | Training-free generalization across domains via synthetic priors |
| **Decoder-only for Ads** | CADET (LinkedIn) | Decoder-only Transformers entering production ad systems |
| **GEO Brand Competition** | Incumbent Advantage | LLM recommendation creates new brand dynamics; game-theoretic implications |
| **On-device LLM Rec** | OD-LLM, PerSRec | Efficiency-focused compression and tokenization for edge deployment |
| **Agentic RL** | SAO (GLM-5.2) | Asynchronous single-rollout RL for stable LLM agent post-training |
