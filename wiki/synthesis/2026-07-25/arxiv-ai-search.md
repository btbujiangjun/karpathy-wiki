---
title: "arXiv AI/LLM/RecSys/Ads/CTR/Games Paper Search Report"
type: synthesis
created: 2026-07-25
updated: 2026-07-25
sources: []
tags: [arxiv, llm, recommendation, ctr, ads, sequential-modeling, games, reinforcement-learning]
---

# arXiv AI Search Report — 2026-07-25

Curated selection of recent arXiv papers spanning **LLMs, Recommendation Systems, CTR Prediction, Advertising, Sequential Modeling, and AI for Games**.

---

## 1. CTR Prediction & Feature Interaction

### 1.1 CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer

| Field | Detail |
|-------|--------|
| **Authors** | David Pardoe, Neil Daftary, Miro Furtado, Aditya Aiyer, Yu Wang, Liuqing Li, Tao Song, Lars Hertel, Young Jin Yun, Senthil Radhakrishnan, Zhiwei Wang, Tommy Li, Khai Tran, Ananth Nagarajan, Ali Naqvi, Yue Zhang, Renpeng Fang, Avi Romascanu, Arjun Kulothungun, Deepak Kumar, Praneeth Boda, Fedor Borisyuk, Ruoyan Wang |
| **Institution** | LinkedIn |
| **Date** | Feb 2026 |
| **Key Innovation** | End-to-end decoder-only transformer for ads CTR prediction with: (1) context-conditioned decoding with multi-tower prediction heads for post-scoring signals; (2) self-gated attention for training stability; (3) timestamp-based RoPE for multi-scale temporal relationships; (4) session masking to address train-serve skew; (5) production engineering (tensor packing, custom Flash Attention kernels) |
| **Result** | **11.04% CTR lift** vs. LiRank baseline (DCNv2 + sequential encoders). Deployed on LinkedIn's ad platform for homefeed sponsored updates. |
| **Link** | [arXiv:2602.11410](https://arxiv.org/abs/2602.11410) |

### 1.2 GRAB: An LLM-Inspired Sequence-First CTR Prediction Modeling Paradigm

| Field | Detail |
|-------|--------|
| **Authors** | Shaopeng Chen, Chuyue Xie, Huimin Ren, Shaozong Zhang, Han Zhang, Ruobing Cheng, Zhiqiang Cao, Zehao Ju, Yu Gao, Jie Ding, Xiaodong Chen, Xuewu Jiao, Shuanglong Li, Liu Lin |
| **Institution** | Baidu |
| **Date** | Feb 2026 |
| **Key Innovation** | Generative Ranking for Ads at Baidu (GRAB): end-to-end generative framework with Causal Action-aware Multi-channel Attention (CamA) mechanism to capture temporal dynamics and action signals in user behavior sequences. Shows monotonic scaling behavior with longer interaction sequences. |
| **Result** | **+3.05% revenue, +3.49% CTR** in full-scale online deployment at Baidu. Demonstrates approximately linear improvement as sequence length increases. |
| **Link** | [arXiv:2602.01865](https://arxiv.org/abs/2602.01865) |

### 1.3 Dual-Stream MLP is All You Need for CTR Prediction

| Field | Detail |
|-------|--------|
| **Authors** | Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen |
| **Institution** | Renmin University of China |
| **Date** | Jun 2026 |
| **Key Innovation** | DS-MLP framework that uses knowledge distillation to consolidate explicit feature interaction learning into a main MLP network, with a parallel MLP capturing implicit interactions. Despite being a vanilla MLP structure, achieves SOTA across three benchmarks. Accepted by TKDD. |
| **Result** | State-of-the-art performance on three widely used CTR benchmarks with a simple MLP structure. |
| **Link** | [arXiv:2606.04944](https://arxiv.org/abs/2606.04944) |

### 1.4 ML-DCN: Masked Low-Rank Deep Crossing Network for Ads CTR Prediction at Pinterest

| Field | Detail |
|-------|--------|
| **Authors** | Jiacheng Li, Yixiong Meng, Yi Wu, Yun Zhao, Sharare Zehtabian, Jiayin Jin, Degao Peng, Jinfeng Zhuang, Qifei Shen, Kungang Li |
| **Institution** | Pinterest |
| **Date** | Feb 2026 |
| **Key Innovation** | Scalable and compute-efficient deep crossing network with masked low-rank design for ads CTR prediction. Achieves improvements with neutral serving cost. |
| **Result** | **+1.89% relative CTR increase** and improved click quality metrics in production at Pinterest. |
| **Link** | [arXiv:2602.09194](https://arxiv.org/abs/2602.09194) |

---

## 2. Generative Recommendation & Foundation Models

### 2.1 TokenMixer-Large: Scaling Up Large Ranking Models in Industrial Recommenders

| Field | Detail |
|-------|--------|
| **Authors** | ByteDance team |
| **Institution** | ByteDance |
| **Date** | 2026 |
| **Key Innovation** | Scaled RankMixer to **7B online / 15B offline parameters**. Fixes residual misalignment, adds inter-layer residuals + Sparse Per-token MoE. Achieves 60% Ads MFU (Model FLOPs Utilization). |
| **Result** | E-commerce GMV **+2.98%**, advertising ADSS **+2.0%**. |
| **Link** | [arXiv (2026)](https://github.com/ubear/modern-recsys-papers) |

### 2.2 UniMixer: A Unified Architecture for Scaling Laws in Recommendation Systems

| Field | Detail |
|-------|--------|
| **Authors** | ByteDance team |
| **Institution** | ByteDance |
| **Date** | 2026 |
| **Key Innovation** | Unifies attention, token-mixing, and FM-based paradigms under a single parametric framework. Establishes theoretical foundation for recommendation scaling blocks. |
| **Result** | Provides theoretical grounding for scaling laws in recommendation systems. |
| **Link** | [Referenced in modern-recsys-papers](https://github.com/ubear/modern-recsys-papers) |

### 2.3 ULTRA-HSTU (HSTU 2.0): Action Encoding for Generative Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Meta AI team |
| **Institution** | Meta |
| **Date** | 2026 |
| **Key Innovation** | Action encoding (single token for item + action), semi-local attention O(L·(K₁+K₂)), mixed-precision training. Builds on HSTU (Actions Louder than Words, ICML 2024). |
| **Result** | **5.3× training, 21.4× inference speedup** vs. standard HSTU. |
| **Link** | [Referenced in modern-recsys-papers](https://github.com/ubear/modern-recsys-papers) |

### 2.4 OneRec: Unifying Retrieve and Rank with Generative Recommender

| Field | Detail |
|-------|--------|
| **Authors** | Kuaishou team |
| **Institution** | Kuaishou |
| **Date** | KDD 2025 |
| **Key Innovation** | First end-to-end generative model replacing cascaded retrieval + ranking in production. Sparse MoE + session-wise generation + iterative DPO. Dubbed the "GPT moment" for generative recommendation in industry. |
| **Result** | Online watch time **+1.6%**. |
| **Link** | [Referenced in modern-recsys-papers](https://github.com/ubear/modern-recsys-papers) |

### 2.5 RecGPT-V3: Stateful Hybrid-Modal Recommender

| Field | Detail |
|-------|--------|
| **Authors** | Ke Chen, Jian Wu, Han Zhu |
| **Institution** | Alibaba (Taobao) |
| **Date** | Jul 2026 |
| **Key Innovation** | Memory Hub maintains structured, continually evolving user memory; Hybrid-modal Foundation Model jointly reasons over text tags and SIDs; Latent Intent Reasoning internalizes verbose rationales into compact latent tokens (200× output token cost reduction). |
| **Result** | Deployed in Taobao's "Guess What You Like" feed: **IPV +1.28%, CTR +1.00%, TC +1.97%, GMV +3.97%**, serving resources cut by **52.4%**. |
| **Link** | [arXiv (Jul 2026)](https://arxiv.org/abs/2607.17476) (referenced on papers.cool) |

### 2.6 PinFM: Foundation Model for User Activity Sequences at Pinterest

| Field | Detail |
|-------|--------|
| **Authors** | Pinterest team |
| **Institution** | Pinterest |
| **Date** | RecSys 2025 |
| **Key Innovation** | First industrial foundation model for user activity sequences at billion scale. Three losses (next-token, multi-token, future-token). Decouples ID embedding table (CPU) from dense Transformer (GPU). 1:1000 user-to-candidate serving ratio. |
| **Result** | Validated at Pinterest scale. Pinterest's "GPT moment" for recommendation. |
| **Link** | [Referenced in modern-recsys-papers](https://github.com/ubear/modern-recsys-papers) |

---

## 3. Sequential Modeling & Long Sequence

### 3.1 LONGER: Scaling Up Long Sequence Modeling in Industrial Recommenders

| Field | Detail |
|-------|--------|
| **Authors** | Zheng Chai, Qin Ren, Xijun Xiao, Huizhi Yang, Bo Han, Sijun Zhang, Di Chen, Hui Lu, Wenlin Zhao, Lele Yu, Xionghang Xie, Shiru Ren, Xiang Sun, Yaocheng Tan, Peng Xu, Yuchao Zheng, Di Wu |
| **Institution** | ByteDance |
| **Date** | May 2025 (RecSys 2025) |
| **Key Innovation** | Long-sequence Optimized traNsformer for GPU-Efficient Recommenders: (i) global token mechanism for stabilizing attention over long contexts; (ii) token merge module with lightweight InnerTransformers and hybrid attention to reduce quadratic complexity; (iii) engineering optimizations including mixed-precision training, KV cache serving, fully synchronous training/serving framework. |
| **Result** | Fully deployed at **10+ scenarios at ByteDance**, serving billions of users. Validates industrial-level scaling laws. |
| **Link** | [arXiv:2505.04421](https://arxiv.org/abs/2505.04421) |

### 3.2 HLLM: Hierarchical Large Language Models for Sequential Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Junyi Chen, Lu Chi, Bingyue Peng, Zehuan Yuan |
| **Institution** | Industry (China) |
| **Date** | Sep 2024 |
| **Key Innovation** | Decouples recommendation into an Item LLM (compresses text into embeddings) and a User LLM (models interests over these embeddings). Achieves scalability and efficiency by avoiding direct text input into LLMs. Shows performance scales with sequence length. |
| **Result** | Performance steadily improves as sequence length grows. Demonstrates scaling behavior in sequential recommendation. |
| **Link** | [arXiv:2409.12740](https://arxiv.org/abs/2409.12740) |

### 3.3 R²ec: Towards Large Recommender Models with Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | HIT/SJTU team |
| **Institution** | Harbin Institute of Technology / Shanghai Jiao Tong University |
| **Date** | NeurIPS 2025 |
| **Key Innovation** | First unified large recommendation model with dual-head architecture (reasoning chain + efficient item prediction). Trained with RecPO (RL framework with reward mechanisms). Proves recommenders can chain-of-thought like LLMs. |
| **Result** | Validated at NeurIPS 2025. |
| **Link** | [Referenced in modern-recsys-papers](https://github.com/ubear/modern-recsys-papers) |

### 3.4 RecZero: Think before Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Institution** | — |
| **Date** | NeurIPS 2025 |
| **Key Innovation** | Abandons multi-model distillation paradigm. Uses pure RL (GRPO) to train a single LLM to autonomously develop reasoning for rating prediction. "Think before recommend" template. |
| **Result** | NeurIPS 2025. |
| **Link** | [Referenced in modern-recsys-papers](https://github.com/ubear/modern-recsys-papers) |

---

## 4. Advertising & Auto-Bidding

### 4.1 GRAD: Generative Reward-driven Ad-bidding with Mixture-of-Experts

| Field | Detail |
|-------|--------|
| **Authors** | Yu Lei, Jiayang Zhao, Yilei Zhao, Zhaoqi Zhang, Linyou Cai, Qianlong Xie, Xingxing Wang |
| **Institution** | Meituan |
| **Date** | Aug 2025 (KDD 2026) |
| **Key Innovation** | Scalable foundation model for auto-bidding combining Action-Mixture-of-Experts module for diverse bidding action exploration with Value Estimator of Causal Transformer for constraint-aware optimization. Handles CPM/ROI constraints in dynamic environments. |
| **Result** | Deployed at Meituan: **+2.18% GMV, +10.68% ROI** across multiple marketing scenarios. |
| **Link** | [arXiv:2508.02002](https://arxiv.org/abs/2508.02002) |

### 4.2 Generative Click-through Rate Prediction with Applications to Search Advertising (GenCTR)

| Field | Detail |
|-------|--------|
| **Authors** | Lingwei Kong, Lu Wang, Changping Peng, Zhangang Lin, Ching Law, Jingping Shao |
| **Institution** | Major e-commerce platform (China) |
| **Date** | Jul 2025 |
| **Key Innovation** | Two-stage training: (1) generative pre-training for next-item prediction; (2) fine-tuning generative model within discriminative CTR prediction framework. Reconciles data aggregation needs of generative and discriminative models. |
| **Result** | Deployed on one of the world's largest e-commerce platforms. Dataset and code planned for release. |
| **Link** | [arXiv:2507.11246](https://arxiv.org/abs/2507.11246) |

### 4.3 JD-BP: Joint-Decision Generative Framework for Auto-Bidding

| Field | Detail |
|-------|--------|
| **Authors** | JD.com team |
| **Institution** | JD.com |
| **Date** | Apr 2026 |
| **Key Innovation** | Generative model that learns to produce good bidding and pricing decisions from training data, moving beyond traditional calculus-based optimization. |
| **Result** | — |
| **Link** | [Referenced on aimodels.fyi](https://www.aimodels.fyi/papers/arxiv/jd-bp-joint-decision-generative-framework-auto) |

---

## 5. LLM for Recommendation (LLM4Rec)

### 5.1 Full-Stack Optimized Large Language Models for Lifelong Sequential Behavior Comprehension in Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Institution** | — |
| **Date** | Jan 2025 |
| **Key Innovation** | Full-stack optimization for LLMs to comprehend lifelong sequential user behavior for recommendation. |
| **Link** | [arXiv:2501.13344](https://arxiv.org/abs/2501.13344) |

### 5.2 Do Recommendation Algorithms Work When Users Are LLM Agents?

| Field | Detail |
|-------|--------|
| **Authors** | Daming Li, Simeng Han, Jialu Zhang |
| **Institution** | — |
| **Date** | Jun 2026 |
| **Key Innovation** | Investigates whether recommendation algorithms designed for human users still work when users are LLM agents that may not have well-defined preferences. Studies on Moltbook platform. |
| **Link** | [arXiv:2606.29762](https://arxiv.org/abs/2606.29762) |

### 5.3 Autonomous Information Seeking: A Roadmap for Agentic Recommender Systems

| Field | Detail |
|-------|--------|
| **Authors** | Xinyu Lin, Yashar Deldjoo, Sunhao Dai, Honghui Bao et al. |
| **Date** | Jul 2026 |
| **Key Innovation** | Comprehensive survey on LLM-based agents in recommender systems. Maps the shift from static ranking-based pipelines toward autonomous interactive systems that can reason, plan, and act. |
| **Link** | [arXiv:2607.04433](https://arxiv.org/abs/2607.04433) |

### 5.4 RecGPT-V1/V2/V3 Series: LLM-Powered Recommendation at Taobao

| Field | Detail |
|-------|--------|
| **Authors** | Alibaba (Taobao) team |
| **Institution** | Alibaba |
| **Date** | 2025–2026 |
| **Key Innovation** | Progressive series transforming recommendation from co-occurrence pattern matching to intent reasoning. V3 introduces Memory Hub, Hybrid-modal Foundation Model, and Latent Intent Reasoning. |
| **Result** | V3 deployed in Taobao feed with significant online gains (see §2.5). |

---

## 6. Semantic ID & Generative Retrieval

### 6.1 GPSD: Scaling Transformers via Generative Pretraining

| Field | Detail |
|-------|--------|
| **Authors** | Alibaba team |
| **Institution** | Alibaba |
| **Date** | KDD 2025 |
| **Key Innovation** | Uses generative pretraining (next-item prediction) to mitigate ID embedding overfitting and enable scaling. Pretrained Transformer ID embeddings injected into discriminative CTR models. Validates predictable power-law scaling. |
| **Link** | [Referenced in modern-recsys-papers](https://github.com/ubear/modern-recsys-papers) |

### 6.2 UniSID: End-to-End Semantic ID for Generative Ad Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Date** | 2026 |
| **Key Innovation** | Unified end-to-end embedding and semantic ID optimization (vs two-stage RQ compression). Addresses objective misalignment in two-stage quantization for ads. |
| **Link** | [Referenced in modern-recsys-papers](https://github.com/ubear/modern-recsys-papers) |

### 6.3 Generative Retrieval for Industrial Search/Recommendation/Advertising

| Field | Detail |
|-------|--------|
| **Authors** | Dan Ou, Gui Ling, Hao Wan, Hongbin Zhou et al. |
| **Date** | Jul 2026 |
| **Key Innovation** | Combines user behavior sequences with LLM capabilities for generative retrieval in industrial systems. Most existing work in this area delivers significant online gains. |
| **Link** | [arXiv (Jul 2026)](https://arxiv.org/abs/2607.15114) (referenced on Distill AI) |

---

## 7. AI for Games & Game Theory + RL

### 7.1 Game-Theory-Assisted Reinforcement Learning for Border Defense

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Date** | Mar 2026 |
| **Key Innovation** | Hybrid approach leveraging game-theoretic insights to improve RL training efficiency. Uses Apollonius Circle to compute equilibrium in post-detection phase, enabling early termination of RL episodes. RL focuses on learning search strategies while game theory handles pursuit dynamics. |
| **Link** | [arXiv:2603.15907](https://arxiv.org/abs/2603.15907) |

### 7.2 SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn RL

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Date** | ICLR 2026 Poster |
| **Key Innovation** | Self-play on zero-sum games as a training paradigm to incentivize reasoning capabilities in LLMs via multi-agent multi-turn reinforcement learning. |
| **Link** | [ICLR 2026](https://openreview.net/forum?id=7Yayy5fNLg) |

### 7.3 Think in Games: Learning to Reason in Games via RL with LLMs

| Field | Detail |
|-------|--------|
| **Authors** | Yi Liao, Yu Gu, Yuan Sui, Zining Zhu, Yifan Lu, Guohua Tang, Zhongqian Sun, Wei Yang |
| **Date** | Aug 2025 |
| **Key Innovation** | Uses reinforcement learning with large language models to learn reasoning strategies within game environments. |
| **Link** | [arXiv:2508.21365](https://arxiv.org/abs/2508.21365) |

### 7.4 NitroGen: An Open Foundation Model for Generalist Gaming Agents

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Date** | Jan 2026 |
| **Key Innovation** | Open foundation model designed as a generalist gaming agent, capable of playing across diverse game environments. |
| **Link** | [arXiv:2601.02427](https://arxiv.org/abs/2601.02427) |

### 7.5 Nemobot Games: Crafting Strategic AI Gaming Agents for Interactive Learning with LLMs

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Date** | Apr 2026 |
| **Key Innovation** | Strategic AI gaming agents powered by LLMs for interactive learning scenarios. |
| **Link** | [arXiv:2604.21896](https://arxiv.org/abs/2604.21896) |

### 7.6 Multi-agent KTO: Reinforcing Strategic Interactions of LLM in Language Game

| Field | Detail |
|-------|--------|
| **Authors** | Rong Ye, Yongxin Zhang, Yikai Zhang, Haoyu Kuang, Zhongyu Wei, Peng Sun |
| **Date** | Jan 2025 |
| **Key Innovation** | Applies KTO (Knowledge-enhanced Task Optimization) to reinforce strategic interactions between LLM agents in language game settings. |
| **Link** | [arXiv:2501.14225](https://arxiv.org/abs/2501.14225) |

---

## 8. LLM Infrastructure & Serving

### 8.1 Towards Efficient Large Language Model Serving: System-Aware KV Cache Optimization (Survey)

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Date** | Jul 2026 |
| **Key Innovation** | Comprehensive taxonomy of KV cache optimization techniques categorized by temporal, spatial, and structural dimensions. Analyzes cross-behavior co-design for LLM serving infrastructure. |
| **Link** | [arXiv:2607.08057](https://arxiv.org/abs/2607.08057) |

### 8.2 Dynamic Agent Skills: A Lifecycle Survey and Taxonomy of Evolving Skill Libraries

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Date** | Jul 2026 |
| **Key Innovation** | Six-sense taxonomy for skill artifacts, eight-stage lifecycle architecture for skill management, and standardized schema for comparing dynamic library updates in agent systems. |
| **Link** | [arXiv:2607.10113](https://arxiv.org/abs/2607.10113) |

### 8.3 Understanding Large Language Models

| Field | Detail |
|-------|--------|
| **Authors** | — |
| **Date** | Jul 2026 |
| **Key Innovation** | Comprehensive overview of LLM mechanisms, emergent cognitive capabilities, and debate on machine understanding vs. pattern memorization. Synthesizes architecture, emergent behaviors, and interpretability methods. |
| **Link** | [arXiv:2607.01006](https://arxiv.org/abs/2607.01006) |

---

## 9. Emerging Trends & Key Takeaways

| Trend | Observation |
|-------|-------------|
| **Generative CTR** | Paradigm shift from discriminative to generative models for CTR prediction (CADET, GRAB, GenCTR, GRAD). Generative pre-training + discriminative fine-tuning emerges as dominant pattern. |
| **Token-Based Ranking** | ByteDance's RankMixer → TokenMixer-Large → UniMixer series establishes token-based feature interaction as a new standard. Scaling to 7B+ params. |
| **Foundation Models for Rec** | Netflix, Pinterest, Meta, Kuaishou, Alibaba all investing in large foundation models for recommendation. Power-law scaling validated. |
| **LLM4Rec Maturing** | From feature encoding to reasoning chains. R²ec, RecZero, RecGPT series demonstrate LLMs can reason about recommendations. |
| **Semantic IDs** | Replacing traditional item IDs with semantic tokens from LLMs. UniSID, GPSD validate end-to-end optimization. |
| **Long Sequence Modeling** | LONGER (ByteDance) and TWIN V2 (Kuaishou) push industrial-scale long sequence modeling. Quadratic complexity reduction via token merging. |
| **AI for Games** | LLM-based game agents maturing: self-play for reasoning (SPIRAL), generalist gaming agents (NitroGen), strategic interactions. |
| **Auto-Bidding as Generation** | GRAD (Meituan) and JD-BP reframe ad bidding as a generative sequence modeling problem with constraint-aware optimization. |

---

*Generated by arXiv search on 2026-07-25. Papers selected for relevance to LLM, recommendation, advertising, CTR prediction, sequential modeling, and AI for games.*
