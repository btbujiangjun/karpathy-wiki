---
title: arXiv AI Research Paper Search Report
type: synthesis
created: 2026-08-18
updated: 2026-08-18
sources: []
tags: [arxiv, AI, LLM, recommendation, CTR, advertising, sequential-modeling, games, reinforcement-learning]
---

# arXiv AI Research Paper Search Report

> Generated: 2026-08-18 | Topics: AI, LLMs, Recommendation, Advertising, Sequential Modeling, CTR, Games, RL

---

## 1. Large Language Models (LLMs)

### 1.1 Understanding Large Language Models

| Field | Detail |
|-------|--------|
| **Title** | Understanding Large Language Models |
| **Authors** | Yannik Keller, Thomas Eisenmann |
| **Institution** | (Not specified) |
| **Date** | 2026-07-01 |
| **arXiv** | [2607.01006](https://arxiv.org/abs/2607.01006) |

**Abstract:** LLMs represent one of the most significant advances in AI and NLP in recent years. This paper reviews mechanisms, capabilities, and relationship to human cognition, addressing pressing questions that remain highly debated.

**Key Innovations:** Comprehensive survey of LLM mechanisms, capabilities, and cognitive parallels.

---

### 1.2 Large Language Model Reasoning Failures

| Field | Detail |
|-------|--------|
| **Title** | Large Language Model Reasoning Failures |
| **Authors** | Peiyang Song, Pengrui Han, Noah Goodman |
| **Institution** | Stanford University |
| **Date** | 2026-02-05 |
| **arXiv** | [2602.06176](https://arxiv.org/abs/2602.06176) |

**Abstract:** Despite remarkable reasoning capabilities, significant reasoning failures persist in LLMs even in seemingly simple scenarios. This paper catalogues and analyzes these failure modes.

**Key Innovations:** Systematic taxonomy of LLM reasoning failures; identification of fundamental limitations in current reasoning approaches.

---

### 1.3 Numeracy in Large Language Models

| Field | Detail |
|-------|--------|
| **Title** | Numeracy in Large Language Models: Fundamental Limitations and Paths to Improvement |
| **Authors** | Aoxin Ni |
| **Institution** | (Not specified) |
| **Date** | 2026-08-13 |
| **arXiv** | [2608.13129](https://arxiv.org/abs/2608.13129) |

**Abstract:** LLMs remain unreliable on elementary numerical tasks (magnitude comparison, large-integer arithmetic, fractions, scientific notation). Proposes the Numerical Grounding Framework (NGF) decomposing numeracy into Representational Grounding and Procedural Grounding. Evaluates three frontier model families.

**Key Innovations:** Numerical Grounding Framework (NGF); systematic evaluation of frontier models on atomic, contextual, and reasoning-assisted numeracy; mitigation strategies including digit-aware tokenization and Abacus Embeddings.

---

### 1.4 The Evolution of MoE Architectures in LLMs

| Field | Detail |
|-------|--------|
| **Title** | The Evolution of Mixture-of-Experts Architectures in Large Language Models: Routing, Topology, Load Balancing, and Expert Parallelism |
| **Authors** | Jiguo Li |
| **Institution** | (Not specified) |
| **Date** | 2026-08-09 |
| **arXiv** | [2608.08650](https://arxiv.org/abs/2608.08650) |

**Abstract:** Technical survey organizing modern MoE systems along five dimensions: expert granularity, expert topology, routing freedom, load balancing scope, and execution structure. Describes eight architectural milestones as a dependency graph. Analyzes systems through four control planes: Topology, Routing, Balance, and Parallelism.

**Key Innovations:** Four-plane control framework for MoE analysis; dependency graph of MoE evolution; identification of the trend toward decoupling semantic routing from physical execution.

---

### 1.5 Position Encoding in Transformers

| Field | Detail |
|-------|--------|
| **Title** | Position Encoding in Transformers: From Absolute and Relative Methods to Rotary Position Embeddings and Long-Context Scaling |
| **Authors** | Jiguo Li |
| **Institution** | (Not specified) |
| **Date** | 2026-08-09 |
| **arXiv** | [2608.10021](https://arxiv.org/abs/2608.10021) |

**Abstract:** Unified account of position encoding methods from sinusoidal absolute embeddings through RoPE and long-context extensions (Position Interpolation, NTK-aware scaling, YaRN, LongRoPE). Central conclusion: computing positional features beyond training length does not imply reliable long-context generalization.

**Key Innovations:** Comprehensive comparison of position encoding methods; analysis of long-context extension techniques; evaluation protocols for position encoding choices.

---

## 2. CTR Prediction & Advertising

### 2.1 Dual-Stream MLP for CTR Prediction

| Field | Detail |
|-------|--------|
| **Title** | Dual-Stream MLP is All You Need for CTR Prediction |
| **Authors** | Kesha Ou, Zhen Tian, Wayne Xin Zhao, Long Zhang, Sheng Chen, Ji-Rong Wen |
| **Institution** | Renmin University of China |
| **Date** | 2026-06-03 |
| **Venue** | Accepted by TKDD |
| **arXiv** | [2606.04944](https://arxiv.org/abs/2606.04944) |

**Abstract:** Proposes DS-MLP, a novel feature interaction framework using knowledge distillation to consolidate explicit feature interaction learning into a main MLP network, while a parallel MLP captures implicit interactions. Achieves SOTA across three benchmarks with a vanilla MLP structure.

**Key Innovations:** Dual-stream MLP architecture with knowledge distillation; two alignment strategies for MLP compatibility; demonstrates that simple MLP structures can achieve SOTA in CTR prediction.

---

### 2.2 CADET: Decoder-Only Transformer for Ads CTR

| Field | Detail |
|-------|--------|
| **Title** | CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer |
| **Authors** | David Pardoe, Neil Daftary, Miro Furtado, +20 authors |
| **Institution** | LinkedIn |
| **Date** | 2026-02-11 (revised 2026-08-10) |
| **Venue** | Accepted at AdKDD 2026 |
| **arXiv** | [2602.11410](https://arxiv.org/abs/2602.11410) |

**Abstract:** End-to-end decoder-only transformer for ads CTR prediction deployed at LinkedIn. Introduces context-conditioned decoding with multi-tower prediction heads, self-gated attention, timestamp-based RoPE, session masking strategies, and production engineering techniques (tensor packing, sequence chunking, custom Flash Attention kernels). Achieves 11.04% CTR lift over LiRank baseline.

**Key Innovations:** Context-conditioned decoding architecture resolving the CTR-ranking chicken-and-egg problem; self-gated attention mechanism; timestamp-based RoPE for temporal relationships; session masking for train-serve skew; deployed on LinkedIn's homefeed sponsored updates.

---

### 2.3 EST: Efficient Scaling Laws for CTR via Unified Modeling

| Field | Detail |
|-------|--------|
| **Title** | EST: Towards Efficient Scaling Laws in Click-Through Rate Prediction via Unified Modeling |
| **Authors** | Mingyang Liu, Yong Bai, Zhangming Chan, Sishuo Chen, Xiang-Rong Sheng, Han Zhu, Jian Xu, Xiang Chen |
| **Institution** | Alibaba (Taobao & Tmall Group) |
| **Date** | 2026-02-11 |
| **arXiv** | [2602.10811](https://arxiv.org/abs/2602.10811) |

**Abstract:** Proposes Efficiently Scalable Transformer (EST) achieving fully unified modeling by processing all raw inputs in a single sequence. Integrates Lightweight Cross-Attention (LCA) and Content Sparse Attention (CSA). Exhibits stable power-law scaling relationship. Deployed on Taobao's display advertising platform with 3.27% RPM increase and 1.22% CTR lift.

**Key Innovations:** Fully unified modeling eliminating information bottleneck from early aggregation; Lightweight Cross-Attention pruning redundant self-interactions; Content Sparse Attention for dynamic behavior selection; demonstrated power-law scaling for CTR prediction.

---

### 2.4 Are AI Agents Interacting with Online Ads?

| Field | Detail |
|-------|--------|
| **Title** | Are AI Agents interacting with Online Ads? |
| **Authors** | Andreas Stöckl, Joel Nitu |
| **Institution** | University of Applied Sciences Upper Austria |
| **Date** | 2025-04 (revised 2026) |
| **arXiv** | [2504.07112](https://arxiv.org/abs/2504.07112) |

**Abstract:** Examines how different AI agents (GPT-4, Claude, Gemini, Perplexity, Operator) interact with online advertising in hotel booking contexts. Finds that AI agents prioritize structured data over visual/emotional cues; banner ads can influence agent behavior but with inconsistent reliability.

**Key Innovations:** First systematic study of AI agent interaction with online ads; identifies need for API-driven marketing; demonstrates that traditional ad formats are less effective for AI-mediated decision-making.

---

## 3. Recommendation Systems & Sequential Modeling

### 3.1 RecRec: Recursive Refinement for Sequential Recommendation

| Field | Detail |
|-------|--------|
| **Title** | RecRec: Recursive Refinement for Sequential Recommendation |
| **Authors** | Pervez Shaik, Prosenjit Biswas, Abhinav Thorat, Ravi Kolla, Niranjan Pedanekar |
| **Institution** | Sony Research India |
| **Date** | 2026-07-12 |
| **arXiv** | [2607.10541](https://arxiv.org/abs/2607.10541) |

**Abstract:** Revisits sequential recommendation from a recursive inference perspective. Proposes RecRec, a lightweight model (3.9M-14M parameters) that maintains a compact latent state updated through a shared recursive module with evidence-anchored correction mechanism. Matches or outperforms SOTA sequential, graph-based, and reasoning-enhanced recommenders.

**Key Innovations:** Recursive latent state inference for sequential recommendation; evidence-anchored correction mechanism preventing semantic drift; lightweight architecture competitive with much larger models.

---

### 3.2 GALLM: Graph-Aware LLMs for Sequential Recommendation

| Field | Detail |
|-------|--------|
| **Title** | Making Collaborative Signals Count: Graph-Aware Large Language Models for Sequential Recommendation |
| **Authors** | Fenglin Yan, Bohao Wang, Jian Zhang, Yu Cui, Tongya Zheng, Ye Feng, Can Wang, Jiawei Chen |
| **Institution** | (Not specified) |
| **Date** | 2026-08-12 |
| **arXiv** | [2608.12184](https://arxiv.org/abs/2608.12184) |

**Abstract:** Addresses LLMs' difficulty capturing collaborative signals in user-item interactions. Constructs a collaborative graph over text and item tokens, modeling Text-Text, Item-Text, and Item-Item relations as learnable attention biases incorporated into LLM attention. Improves over strongest baseline by 9.76% on HR@5.

**Key Innovations:** Collaborative graph construction over text/item tokens; three-type relation modeling as attention biases; no additional graph encoder needed; enables collaborative-aware token interactions in LLMs.

---

### 3.3 DrEM: Robust Ensemble Ranking for Video Recommendation

| Field | Detail |
|-------|--------|
| **Title** | DrEM: Dual-Side Robust Ensemble Ranking from Noisy User Preference Predictions in Video Recommendation |
| **Authors** | Canwei Huang, Tiantian He, Xiaoxiao Xu, Jun Zhang, Ziran Deng, Weike Pan, Chunjie Chen, Kaiqiao Zhan |
| **Institution** | (Not specified) |
| **Date** | 2026-08-13 |
| **arXiv** | [2608.12778](https://arxiv.org/abs/2608.12778) |

**Abstract:** Addresses prediction noise in multi-stage video recommendation systems. Introduces risk-denoising robust loss correcting empirical risk using estimated preference flip probability, and preference-preserving ranking consistency regularizer. Validated with offline experiments and large-scale online A/B tests.

**Key Innovations:** Dual-side noise robustness framework (supervision side + feature side); risk-denoising robust loss; preference-preserving consistency regularizer; theoretical analysis of prediction noise distribution.

---

### 3.4 HCGRec: Hint-Conditioned Generative Recommendation

| Field | Detail |
|-------|--------|
| **Title** | Learning from Unreachable Rewards: Hint-Conditioned Reinforcement Learning for Generative Recommendation |
| **Authors** | Kangning Zhang, Haotian Fang, Xukun Luo, Hao Yin, Yang Gao, Peng Yan, Weiwen Liu, Weinan Zhang, Yong Yu |
| **Institution** | Shanghai Jiao Tong University |
| **Date** | 2026-08-12 |
| **Venue** | Accepted by CIKM 2026 |
| **arXiv** | [2608.11980](https://arxiv.org/abs/2608.11980) |

**Abstract:** Addresses the zero-reward bottleneck in RL-based post-training for semantic-ID generative recommenders. HCGRec supplies minimal target-prefix hints when the generator cannot reach the correct item, turning zero-reward groups into informative comparisons. Introduces hint-aware credit decomposition combining supervised learning and GRPO.

**Key Innovations:** Hint-conditioned RL for generative recommendation; checkpoint-based reachability diagnosis; hint-aware credit decomposition (SL for hinted tokens + GRPO for suffix); reduces zero-advantage samples from >70% to <20%.

---

### 3.5 FSGR: Fairness in SID-Based Generative Recommendation

| Field | Detail |
|-------|--------|
| **Title** | FSGR: Mitigating Token Frequency Bias for Fair SID-Based Generative Recommendation |
| **Authors** | Yuchen Zheng, Sihan Xu, Jingwen Yang, Xiangrui Cai, Haiwei Zhang, Xiaojie Yuan |
| **Institution** | (Not specified) |
| **Date** | 2026-08-13 |
| **arXiv** | [2608.12845](https://arxiv.org/abs/2608.12845) |

**Abstract:** Identifies and addresses Token Frequency Bias in semantic-ID generative recommendation, where high-frequency tokens are over-predicted. FSGR employs OT-based Assignment Optimization and Dual-Criteria Re-anchor during SID construction, plus Hierarchical Frequency Calibration during training. Achieves >20% Gini fairness improvement while maintaining accuracy.

**Key Innovations:** Identification of Token Frequency Bias in SID-based generative recommendation; OT-based SID construction optimization; Hierarchical Frequency Calibration for layer-specific fairness.

---

### 3.6 MARS: Multi-Agent Resource Allocation for Recommender Systems

| Field | Detail |
|-------|--------|
| **Title** | MARS: Multi-Agent Reinforcement Learning for Computation Resource Allocation in Recommender Systems |
| **Authors** | (From search results) |
| **Institution** | Leading global e-commerce platform |
| **Date** | 2025-12 |
| **arXiv** | [2512.24324](https://arxiv.org/abs/2512.24324) |

**Abstract:** Multi-agent RL framework for end-to-end computation resource allocation in large-scale recommender systems using Centralized Training with Decentralized Execution (CTDE). Includes AutoBucket TestBench and MPC-based Revenue-Cost Balancer. Handles hundreds of billions of ad requests per day with 16.67% revenue uplift.

**Key Innovations:** CTDE-based multi-agent resource allocation; AutoBucket TestBench for cost estimation; MPC-based revenue-cost balancing; deployed at massive scale in production.

---

## 4. Game AI & Reinforcement Learning

### 4.1 Augmenting Game AI with Deep Reinforcement Learning

| Field | Detail |
|-------|--------|
| **Title** | Augmenting Game AI with Deep Reinforcement Learning |
| **Authors** | Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén |
| **Institution** | Electronic Arts (EA), Stockholm |
| **Date** | 2026-06-18 |
| **Venue** | Conference on Games 2026 |
| **arXiv** | [2606.20210](https://arxiv.org/abs/2606.20210) |

**Abstract:** Vision paper on applying RL to game AI for more believable, authentic characters. Proposes a framework for training RL models suited to game AI and game development. Presents real deployment examples and identifies bottlenecks: sample efficiency, generalization, tension between optimal and human-like behavior.

**Key Innovations:** Framework for training RL models for game AI with game development constraints; real deployment examples; identification of key research bottlenecks for ML adoption in games industry.

---

### 4.2 NitroGen: Open Foundation Model for Generalist Gaming Agents

| Field | Detail |
|-------|--------|
| **Title** | NitroGen: An Open Foundation Model for Generalist Gaming Agents |
| **Authors** | Loïc Magne, Anas Awadalla, Guanzhi Wang, +11 authors |
| **Institution** | NVIDIA, University of Washington, UT Austin, Caltech, NYU |
| **Date** | 2026-01-04 |
| **arXiv** | [2601.02427](https://arxiv.org/abs/2601.02427) |

**Abstract:** Vision-action foundation model trained on 40,000 hours of gameplay across 1,000+ games. Uses automatically extracted player actions from public gameplay videos. Achieves up to 52% relative improvement in task success rates on unseen games. Open-sources dataset, evaluation suite, and model weights.

**Key Innovations:** Internet-scale video-action dataset construction; multi-game benchmark for cross-game generalization; unified vision-action model via large-scale behavior cloning; strong transfer to unseen games.

---

### 4.3 Game-RL: Multimodal Verifiable Game Data for VLM Reasoning

| Field | Detail |
|-------|--------|
| **Title** | Game-RL: Synthesizing Multimodal Verifiable Game Data to Boost VLMs' General Reasoning |
| **Authors** | Jingqi Tong, Jixin Tang, + multiple authors |
| **Institution** | Peking University, WeChat AI |
| **Date** | 2025 (ICLR 2026) |
| **arXiv** | [2505.13886](https://arxiv.org/abs/2505.13886) |

**Abstract:** Uses game environments to synthesize multimodal verifiable training data for improving VLM reasoning. The code has been adopted by Shanghai AI Lab (MoTiF), Princeton (Vero), and NUS (Gym-V).

**Key Innovations:** Game-based data synthesis pipeline for VLM training; verifiable reasoning supervision from game environments; cross-institution adoption.

---

## 5. Industrial-Scale Systems & Trends

### 5.1 Token-Based Recommendation at Scale (ByteDance)

| Field | Detail |
|-------|--------|
| **Title** | TokenMixer-Large: Scaling Up Large Ranking Models in Industrial Recommenders |
| **Institution** | ByteDance |
| **Date** | 2026 |
| **Source** | [modern-recsys-papers](https://github.com/ubear/modern-recsys-papers) |

**Summary:** Scaled RankMixer to 7B online / 15B offline parameters. Fixes residual misalignment, adds inter-layer residuals + Sparse Per-token MoE. Ads MFU reaches 60%. E-commerce GMV +2.98%, advertising ADSS +2.0%.

---

### 5.2 Generative Recommendation at Scale (Meta)

| Field | Detail |
|-------|--------|
| **Title** | ULTRA-HSTU (HSTU 2.0) |
| **Institution** | Meta AI |
| **Date** | 2026 |
| **Source** | [modern-recsys-papers](https://github.com/ubear/modern-recsys-papers) |

**Summary:** Action encoding (single token for item + action), semi-local attention O(L·(K₁+K₂)), mixed-precision training. 5.3× training, 21.4× inference speedup vs standard HSTU. Builds on the foundational HSTU work that first demonstrated scaling laws at billion-user scale.

---

### 5.3 Convergence of ID → Semantic Tokens

| Trend | Key Papers |
|-------|------------|
| **ID → Semantic Tokens** | TokenMixer-Large (ByteDance), TRM, ReSID |
| **Unified Architectures** | OneTrans → HyFormer → MixFormer → UniMixer |
| **Generative Retrieval+Ranking** | OneRec series, HSTU |
| **LLM for Recommendation** | R²ec (reasoning chains), RecZero (GRPO), GALLM |

---

## Summary of Key Trends (2026)

1. **Transformer-based CTR**: Decoder-only transformers are entering production ad systems (CADET at LinkedIn, EST at Taobao), achieving significant lifts over DLRM baselines.

2. **Scaling Laws for CTR**: Power-law scaling relationships are being demonstrated for recommendation models, analogous to LLM scaling laws (EST).

3. **Generative Recommendation**: Semantic-ID based generative approaches are maturing, with RL-based post-training (HCGRec) and fairness concerns (FSGR) being actively addressed.

4. **LLM + Graph for RecSys**: Incorporating collaborative signals into LLM-based recommenders via graph attention biases (GALLM) is a promising direction.

5. **Lightweight Recursive Models**: Recursive inference (RecRec) offers a parameter-efficient alternative to deep architectures and LLMs for sequential recommendation.

6. **Game AI + RL**: Foundation models for gaming (NitroGen) and RL-augmented game characters are advancing, with real industry deployment at EA.

7. **MoE & Position Encoding**: Comprehensive surveys track the rapid evolution of MoE architectures and position encoding techniques critical for LLM scaling.

8. **AI Agents vs Advertising**: AI agents interacting with ads present new challenges for ad format design and measurement.
