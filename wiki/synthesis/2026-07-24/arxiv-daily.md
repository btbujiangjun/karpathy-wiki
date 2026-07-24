---
title: "arXiv Daily Report — 2026-07-24"
type: synthesis
created: 2026-07-24
updated: 2026-07-24
tags: [arxiv, daily, recommendation, CTR, LLM, game-ai, advertising, sequential-modeling]
---

# arXiv Daily Report — 2026-07-24

Curated selection of recent arXiv papers across AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR Prediction, and Game AI.

---

## 1. Recommendation Systems

### 1.1 RECAP: Feedback-Driven Streaming Semantic User Profiles for Short-Video Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Ziyi Zhao, Xiaoyou Zhou, Xiao Lv, Yangyang Li, Chubo He, Zhao Liu, Jiayao Shen, Yuqi Liu, He Li, Chengyi Zhang, Jian Liang, Ming Li, Chongming Gao, Fuli Feng, Ruiming Tang, Han Li |
| **Institution** | Kuaishou |
| **Published** | 2026-07-17 |
| **Venue** | RecSys 2026 |
| **arXiv** | [2607.15730](https://arxiv.org/abs/2607.15730) |

**Abstract:** Language-based user profiles convert long behavioral histories into explicit semantic representations for recommendation. However, most profile generators are optimized in an open loop: they may summarize past behavior fluently, but are not directly trained to improve future recommendation. We study this problem in real-world short-video recommendation, where user behaviors continuously arrive as streams and profiles must be incrementally updated under limited capacity. RECAP maintains each profile as a bounded structured memory by combining LLM-based semantic updates with deterministic lifecycle and capacity control. RECAP constructs profile-targeted semantic feedback by filtering label-consistent behavior pairs with an LLM judge and training a dual-tower evaluator whose matching score serves as a GRPO reward. Experiments on Kuaishou short-video data show that RECAP improves uAUC by 0.0084 and Recall@2000 by about 4.9% over the base generator. A seven-day online A/B test further shows a statistically significant 0.139% improvement in average application usage time per user.

**Key Innovations:**
- Closed-loop streaming semantic profile optimization using LLM-based feedback + GRPO RL
- Bounded structured memory with lifecycle and capacity control for real-time streaming profiles
- Profile-targeted semantic feedback via LLM judge + dual-tower evaluator
- Validated on Kuaishou production data with online A/B testing

---

### 1.2 CoSimRec: Measuring Coordinated-Content Penetration in Recommender Feedback Loops

| Field | Detail |
|-------|--------|
| **Authors** | Nan Li, Jiahong Shao, Jiuyang Lyu |
| **Institution** | — |
| **Published** | 2026-07-16 |
| **arXiv** | [2607.15114](https://arxiv.org/abs/2607.15114) |

**Abstract:** Recommender systems increasingly shape which content reaches users, making it important to understand whether coordinated activity is amplified beyond the accounts that initiate it. We propose CoSimRec, an offline agent-based evaluation framework that models coordinated accounts, dynamic ranking, non-bot responses, and ranking interventions in a shared closed-loop process. CoSimRec introduces the Algorithmic Penetration Rate (APR) metric family to measure target content's share of non-bot exposure and engagement. Experiments on MIND, MovieLens, and LastFM show that popularity-based and feedback-sensitive ranking produce significant positive APR-Lift.

**Key Innovations:**
- Agent-based closed-loop evaluation framework for coordinated manipulation in rec sys
- Algorithmic Penetration Rate (APR) metric family
- Demonstrates vulnerability of popularity-based and feedback-sensitive ranking to coordinated attacks

---

### 1.3 ZoRRO: A Zero-Weight Personalized Recommender System for Scalable News Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Johannes Kruse, Ryotaro Shimizu, Kasper Lindskow, Jon Tofteskov, Michael Riis Andersen, Julian McAuley, Jes Frellsen |
| **Institution** | — |
| **Published** | 2026-07-12 |
| **Venue** | SIGIR 2026 |
| **arXiv** | [2607.10910](https://arxiv.org/abs/2607.10910) |

**Abstract:** ZoRRO (Zero-Weight Personalized Recommender System) is a zero-weight, training-free framework for personalized news recommendation designed for scalable real-world deployment. ZoRRO outperforms strong neural baselines in offline ranking evaluations and achieves CTR performance in online A/B testing nearly on par with a state-of-the-art deep learning model, while operating more than 600 times faster. Experiments reveal gaps between offline and online performance and demonstrate that models with similar CTR outcomes can produce markedly different recommendation distributions.

**Key Innovations:**
- Zero-weight, training-free framework achieving competitive CTR vs. deep models
- 600x faster inference than neural baselines
- Highlights importance of evaluating rec sys using metrics beyond accuracy (distributional analysis)

---

### 1.4 RecRec: Recursive Refinement for Sequential Recommendation

| Field | Detail |
|-------|--------|
| **Authors** | Pervez Shaik, Prosenjit Biswas, Abhinav Thorat, Ravi Kolla, Niranjan Pedanekar |
| **Institution** | — |
| **Published** | 2026-07-12 |
| **arXiv** | [2607.10541](https://arxiv.org/abs/2607.10541) |

**Abstract:** RecRec is a lightweight model that maintains a compact latent state and updates it through a shared recursive module conditioned on interaction evidence. Unlike prior recursive models, RecRec introduces an evidence-anchored correction mechanism that stabilizes refinement by grounding each update in the original interaction context, preventing semantic drift during deep recursive reasoning. Experiments on three benchmark datasets show that RecRec matches or outperforms state-of-the-art sequential, graph-based, and reasoning-enhanced recommenders while using only 3.9M to 14M parameters.

**Key Innovations:**
- Recursive latent inference paradigm for sequential recommendation
- Evidence-anchored correction gate to prevent semantic drift
- Ultra-lightweight (3.9M–14M parameters) competitive with much larger models

---

### 1.5 NAILS: Normative Alignment of Recommender Systems via Internal Label Shift

| Field | Detail |
|-------|--------|
| **Authors** | Johannes Kruse, Kasper Lindskow, Michael Riis Andersen, Ryotaro Shimizu, Julian McAuley, Pierre-Alexandre Mattei, Jes Frellsen |
| **Institution** | — |
| **Published** | 2026-07-12 |
| **Venue** | RecSys 2025 |
| **arXiv** | [2607.10915](https://arxiv.org/abs/2607.10915) |

**Abstract:** NAILS is a simple and scalable method for aligning recommendation outputs with target distributions over item-level attributes (e.g. categories). It modifies the user-conditional item distribution to induce a specified marginal distribution over attributes while preserving learned preferences and requiring no model retraining. Formulated as label shift applied internally within a hierarchical classification framework.

**Key Innovations:**
- Post-hoc normative alignment (fairness, diversity) without model retraining
- Internal label shift formulation for attribute-level distribution control
- Minimal impact on user engagement while improving attribute alignment

---

### 1.6 From Raw IDs to Semantic Planning: How Recommender Systems Utilize Information at Scale

| Field | Detail |
|-------|--------|
| **Authors** | Changhong Jin, Shiqiu Yang, Roger Zhe Li, Yingjie Niu, Aghiles Salah, Mete Sertkan, Zheng Ju, Xingsheng Guo, Huifeng Guo, Ruihai Dong, Barry Smyth |
| **Institution** | — |
| **Published** | 2026-07-10 |
| **arXiv** | [2607.09540](https://arxiv.org/abs/2607.09540) |

**Abstract:** A survey/examining three connected questions about the evolution of information use in recommender systems: why raw IDs dominated the early development, why semantic information is increasingly being encapsulated in IDs today, and what may come next once recommendations move beyond semantic retrieval. Introduces "semantic planning" as a future direction in which the system first predicts the semantic target of the next exposure, and only then instantiates that target as a specific item or generated creative.

**Key Innovations:**
- Comprehensive taxonomy: Raw IDs → Semantic IDs → Semantic Planning
- Proposes "semantic planning" paradigm where systems predict semantic targets before item instantiation
- Argues for evaluation and coordination changes needed to support the shift

---

### 1.7 Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning

| Field | Detail |
|-------|--------|
| **Authors** | Dingsu Wang, Filip Ryzner, Kelly He, Armando Ordorica et al. (15 authors) |
| **Institution** | Pinterest |
| **Published** | 2026-07-15 |
| **Venue** | RecSys 2026 |
| **arXiv** | [2607.14192](https://arxiv.org/abs/2607.14192) |

**Abstract:** Presents a unified, model-agnostic downstream reward framework for optimizing long-term user value in large-scale recommendation systems. Develops an offline screening framework to identify session-level behaviors that are both observable early and predictive of future retention. Proposes model-agnostic downstream reward signals derived from observed user action patterns. Deployed across multiple Pinterest surfaces (Homefeed, Related Pins, Search, Notifications) with consistent improvements in engagement and retention.

**Key Innovations:**
- Model-agnostic downstream reward learning for long-term engagement
- Offline screening framework for early-predictive session behaviors
- Productionized at Pinterest across multiple surfaces

---

### 1.8 Diffusion-GR2: Diffusion Generative Reasoning Re-ranker

| Field | Detail |
|-------|--------|
| **Authors** | Zhuoxuan Zhang, Kangqi Ni, Yuhang Chen, Mingfu Liang, Xiaohan Wei, Yunchen Pu, Fei Tian, Chonglin Sun, Frank Shyu, Adam Song, Sandeep Pandey, Luke Simon, Tianlong Chen, Xi Liu |
| **Institution** | — |
| **Published** | 2026-07-01 |
| **arXiv** | [2607.01170](https://arxiv.org/abs/2607.01170) |

**Abstract:** Converts an autoregressive reasoning re-ranker into a block-diffusion re-ranker to achieve 2.4–3.5x throughput speedup while maintaining near-parity accuracy. Proposes conversion fine-tuning (CFT) to adapt the model to produce valid permutations, on-policy distillation (OPD) with dense per-token targets from the AR teacher, and an RL stage against a re-ranking reward.

**Key Innovations:**
- Block-diffusion parallel decoding for reasoning re-rankers (2.4–3.5x speedup)
- Conversion fine-tuning for valid permutation generation
- On-policy distillation + RL to close accuracy gap vs. AR teacher

---

### 1.9 Autonomous Information Seeking: A Roadmap for Agentic Recommender Systems

| Field | Detail |
|-------|--------|
| **Authors** | Xinyu Lin, Yashar Deldjoo, Sunhao Dai, Honghui Bao, Xiaopeng Ye, Fatemeh Nazary, Wenjie Wang, Tommaso Di Noia, Jun Xu, Tat-Seng Chua |
| **Institution** | — |
| **Published** | 2026-07-05 |
| **arXiv** | [2607.04433](https://arxiv.org/abs/2607.04433) |

**Abstract:** Comprehensive survey of LLM-based agents in recommender systems with a unified taxonomy grounded in autonomy levels and three core paradigms: agent-assisted recommendation, agent-as-recommender, and agent-as-user-simulator. Covers profiles, memory, tool use, workflows, optimization mechanisms, and evaluation methodologies. Discusses open challenges in lifelong user modeling, multimodal alignment, controllability, trustworthiness, privacy, scalability, and efficiency.

**Key Innovations:**
- Unified taxonomy for agentic recommender systems (3 paradigms × autonomy levels)
- Comprehensive evaluation framework (automated metrics, LLM-judging, simulation-based)
- Roadmap covering lifelong modeling, multimodal alignment, trustworthiness, and scalability

---

## 2. CTR Prediction & Advertising

### 2.1 Dual-Stream MLP is All You Need for CTR Prediction (DS-MLP)

| Field | Detail |
|-------|--------|
| **Authors** | Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen |
| **Institution** | Renmin University of China |
| **Published** | 2026-06-03 |
| **Venue** | TKDD |
| **arXiv** | [2606.04944](https://arxiv.org/abs/2606.04944) |

**Abstract:** DS-MLP leverages knowledge distillation to consolidate the capacity of learning explicit feature interaction into a main MLP network, while a parallel MLP simultaneously captures implicit feature interactions as a complement. Despite being merely a vanilla MLP structure, DS-MLP achieves state-of-the-art performance across three widely used benchmarks.

**Key Innovations:**
- Distillation-based dual-stream architecture collapsing into a single vanilla MLP
- Addresses imbalance between explicit and implicit feature interaction modules
- State-of-the-art with minimal complexity — highly scalable for production

---

### 2.2 CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer

| Field | Detail |
|-------|--------|
| **Authors** | David Pardoe, Neil Daftary, Miro Furtado, Aditya Aiyer, Yu Wang, Liuqing Li, Tao Song, Lars Hertel, Young Jin Yun, Senthil Radhakrishnan, Zhiwei Wang, Tommy Li, Khai Tran, Ananth Nagarajan, Ali Naqvi, Yue Zhang, Renpeng Fang, Avi Romascanu, Arjun Kulothungun, Deepak Kumar, Praneeth Boda, Fedor Borisyuk, Ruoyan Wang |
| **Institution** | LinkedIn |
| **Published** | 2026-02-11 |
| **arXiv** | [2602.11410](https://arxiv.org/abs/2602.11410) |

**Abstract:** CADET is an end-to-end decoder-only transformer for ads CTR prediction deployed at LinkedIn. Key innovations include: (1) context-conditioned decoding with multi-tower prediction heads modeling post-scoring signals like ad position; (2) self-gated attention mechanism for stable training; (3) timestamp-based RoPE capturing temporal relationships across timescales from seconds to months; (4) session masking strategies preventing train-serve skew; (5) production engineering techniques for efficient training/serving at scale. Achieves 11.04% CTR lift vs. production LiRank baseline.

**Key Innovations:**
- Decoder-only transformer architecture for ads CTR (vs. traditional DLRMs)
- Context-conditioned decoding resolving chicken-and-egg problem between predicted CTR and ranking
- Timestamp-based RoPE for multi-scale temporal modeling
- Session masking to prevent train-serve skew
- 11.04% CTR lift in online A/B at LinkedIn

---

### 2.3 GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm

| Field | Detail |
|-------|--------|
| **Authors** | Shaopeng Chen, Chuyue Xie, Huimin Ren, Shaozong Zhang, Han Zhang, Ruobing Cheng, Zhiqiang Cao, Zehao Ju, Yu Gao, Jie Ding, Xiaodong Chen, Xuewu Jiao, Shuanglong Li, Liu Lin |
| **Institution** | Baidu |
| **Published** | 2026-02-02 |
| **arXiv** | [2602.01865](https://arxiv.org/abs/2602.01865) |

**Abstract:** GRAB is an end-to-end generative framework for CTR prediction inspired by LLM scaling success. Integrates a novel Causal Action-aware Multi-channel Attention (CamA) mechanism to capture temporal dynamics and specific action signals within user behavior sequences. Full-scale online deployment demonstrates 3.05% revenue increase and 3.49% CTR rise. Model shows desirable scaling behavior: expressive power improves monotonically with longer interaction sequences.

**Key Innovations:**
- LLM-inspired generative paradigm for CTR (sequence-first, not feature-first)
- Causal Action-aware Multi-channel Attention (CamA) for temporal dynamics + action signals
- Demonstrates scaling law: monotonic, approximately linear improvement with longer sequences
- 3.05% revenue lift in production at Baidu

---

## 3. Game AI & Reinforcement Learning

### 3.1 Augmenting Game AI with Deep Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Authors** | Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén |
| **Institution** | Electronic Arts (EA), Stockholm |
| **Published** | 2026-06-18 |
| **Venue** | Conference on Games 2026 |
| **arXiv** | [2606.20210](https://arxiv.org/abs/2606.20210) |

**Abstract:** Proposes a framework for training RL models with requirements suited towards game AI and game development: short training time, controllability, modularity. Presents examples of games with RL-augmented game AI and describes practicalities of deploying player-facing ML agents in modern games. Identifies bottlenecks and hard problems as promising research directions for accelerating ML adoption in game AI.

**Key Innovations:**
- Practical framework for RL in game AI addressing industry constraints (short training, controllability, modularity)
- Survey of RL-augmented game AI deployment across game genres
- Identifies open problems: rapid retraining, designer control, modular integration

---

## 4. LLM / Neuro-Symbolic Reasoning

### 4.1 SoftReason: A Fully Differentiable Neuro-Soft-Symbolic Deductive Reasoning Architecture over High-Dimensional Perceptual Data

| Field | Detail |
|-------|--------|
| **Authors** | Wael AbdAlmageed |
| **Institution** | — |
| **Published** | 2026-07-22 |
| **Venue** | NeSy 2026 |
| **arXiv** | [2607.20402](https://arxiv.org/abs/2607.20402) |

**Abstract:** SoftReason removes the gradient gap between perception and deduction by representing the deductive state as a local soft interpretation tensor over candidate constants and predicates. Core innovation is a learned differentiable lift of the immediate-consequence operator using predicate-definition embeddings and latent composition channels. Instantiated on Knowledge-aware Visual Question Answering (KVQA) demonstrating end-to-end perceptual grounding, KG evidence injection, and differentiable deductive closure.

**Key Innovations:**
- Fully differentiable deductive reasoning over perceptual data (no discrete interface)
- Learned differentiable immediate-consequence operator
- End-to-end trainability combining perception, knowledge graphs, and logical deduction

---

## 5. Sequential Modeling & Time Series

### 5.1 CUSUM-Shaped Inference-Time Monitoring and Targeted Re-Decoding for Quantized Small Language Model Reasoning

| Field | Detail |
|-------|--------|
| **Authors** | El Hassane Ettifouri et al. |
| **Published** | 2026-07-23 |
| **arXiv** | [2607.20129](https://arxiv.org/abs/2607.20129) |

**Key Innovations:**
- CUSUM-shaped monitoring for quantized small LLM inference
- Targeted re-decoding strategy for quality recovery in quantized models

---

### 5.2 Deep Learning for Sequential Decision Making under Uncertainty: Foundations, Frameworks, and Frontiers

| Field | Detail |
|-------|--------|
| **Authors** | I. Esra Buyuktahtakin |
| **Institution** | — |
| **Published** | 2026-04-13 |
| **arXiv** | [2604.11507](https://arxiv.org/abs/2604.11507) |

**Abstract:** OR/MS-centered tutorial on deep learning for sequential decision-making under uncertainty. Argues that deep learning is valuable not as a replacement for optimization, but as a complement. Reviews key foundations connecting neural architectures (feedforward, LSTM, transformers, deep RL) to decision-making frameworks. Highlights emerging impact in supply chains, healthcare, agriculture, energy, and autonomous operations.

**Key Innovations:**
- Unified OR/MS + deep learning perspective on sequential decision-making
- Complementary role framing: DL for adaptability + OR/MS for structural rigor
- Applications across supply chains, healthcare, agriculture, energy

---

## Summary Table

| # | Paper | Topic | Institution | Key Result |
|---|-------|-------|-------------|------------|
| 1 | RECAP | Rec / Short-Video | Kuaishou | 0.139% usage time lift (A/B) |
| 2 | CoSimRec | Rec / Robustness | — | APR metric for coordinated attacks |
| 3 | ZoRRO | Rec / News | — | 600x faster, competitive CTR |
| 4 | RecRec | Rec / Sequential | — | 3.9M params, SOTA performance |
| 5 | NAILS | Rec / Fairness | — | Post-hoc alignment, no retraining |
| 6 | Raw IDs → Semantic Planning | Rec / Survey | — | Future direction: semantic planning |
| 7 | Long-term Engagement | Rec / RL | Pinterest | Multi-surface production deployment |
| 8 | Diffusion-GR2 | Rec / Re-ranking | — | 2.4–3.5x throughput speedup |
| 9 | Agentic Rec Survey | Rec / Agents | — | Unified taxonomy of 3 paradigms |
| 10 | DS-MLP | CTR | Renmin Univ | SOTA with vanilla MLP |
| 11 | CADET | CTR / Ads | LinkedIn | 11.04% CTR lift |
| 12 | GRAB | CTR / Generative | Baidu | 3.05% revenue lift |
| 13 | Game AI + RL | Game AI | EA | Practical RL framework |
| 14 | SoftReason | LLM / Neuro-Symbolic | — | Differentiable deductive reasoning |
